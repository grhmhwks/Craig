"""Versioned FastAPI adapter for CRAIG's read-only retrieval service."""

from __future__ import annotations

import json
import os
from collections.abc import Iterator
from dataclasses import asdict
from pathlib import Path
from typing import Any, Literal

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict

from .chat.errors import (
    ChatError,
    ConversationNotFoundError,
    InvalidChatRequest,
    ProviderUnavailableError,
)
from .chat.models import ChatEvent
from .chat.service import ChatService
from .errors import (
    IndexStaleError,
    InvalidRetrievalRequest,
    RetrievalError,
    SourceNotFoundError,
    TopicNotFoundError,
    UnsafeSourcePathError,
)
from .retrieval import RetrievalConfig, RetrievalService
from .storage import FTS5UnavailableError, IndexNotFoundError

API_PREFIX = "/api/v1"
CONTRACT_VERSION = 1


class _RequestModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SearchRequest(_RequestModel):
    query: str
    topic: str | None = None
    limit: int | None = None
    offset: int = 0
    max_chars: int | None = None


class FindExactRequest(_RequestModel):
    query: str
    topic: str | None = None
    case_sensitive: bool = True
    context_lines: int = 2
    limit: int | None = None
    offset: int = 0
    max_chars: int | None = None


class ReadSourceRequest(_RequestModel):
    path: str
    start_line: int = 1
    end_line: int | None = None
    max_chars: int | None = None


class ChatStreamRequest(_RequestModel):
    message: str
    mode: Literal["research", "explanation", "tutorial", "computation"]
    topic: str | None = None
    conversation_id: str | None = None


class TopicSummaryResponse(BaseModel):
    topic: str
    file_count: int
    chunk_count: int


class TopicListResponse(BaseModel):
    schema_version: Literal[1]
    topics: list[TopicSummaryResponse]
    total_topics: int


class SearchResultResponse(BaseModel):
    rank: int
    score: float
    topic: str
    path: str
    heading: str | None
    start_line: int
    end_line: int
    snippet: str
    file_type: str
    environment: str | None
    file_hash: str


class SearchPageResponse(BaseModel):
    schema_version: Literal[1]
    query: str
    topic: str | None
    offset: int
    limit: int
    results: list[SearchResultResponse]
    has_more: bool
    next_offset: int | None
    truncated: bool


class ExactMatchResponse(BaseModel):
    topic: str
    path: str
    file_type: str
    heading: str | None
    environment: str | None
    match_start_line: int
    match_end_line: int
    excerpt_start_line: int
    excerpt_end_line: int
    excerpt: str
    file_hash: str


class ExactMatchPageResponse(BaseModel):
    schema_version: Literal[1]
    query: str
    topic: str | None
    case_sensitive: bool
    offset: int
    limit: int
    results: list[ExactMatchResponse]
    has_more: bool
    next_offset: int | None
    truncated: bool


class SourceReadResponse(BaseModel):
    schema_version: Literal[1]
    topic: str
    path: str
    file_type: str
    heading: str | None
    environment: str | None
    start_line: int
    end_line: int | None
    total_lines: int
    text: str
    truncated: bool
    next_start_line: int | None
    file_hash: str


class HealthResponse(BaseModel):
    schema_version: Literal[1]
    status: Literal["ok"]
    topic_count: int


class SourceReferenceResponse(BaseModel):
    citation_id: str
    topic: str
    path: str
    heading: str | None
    environment: str | None
    start_line: int
    end_line: int
    file_hash: str
    excerpt: str
    mathematical_status: Literal[
        "proved_result",
        "computer_assisted_proof",
        "conjecture",
        "computational_evidence",
        "experimental_observation",
        "proof_outline",
        "work_in_progress",
        "unknown",
    ]
    status_basis: str | None


class ProvenanceAnnotationResponse(BaseModel):
    kind: Literal["repository", "deduction", "model_knowledge", "external"]
    description: str
    citation_ids: list[str]


class ChatMessageResponse(BaseModel):
    id: str
    role: Literal["user", "assistant"]
    content: str
    created_at: str
    sources: list[SourceReferenceResponse]
    provenance: list[ProvenanceAnnotationResponse]


class ConversationResponse(BaseModel):
    schema_version: Literal[1]
    id: str
    mode: Literal["research", "explanation", "tutorial", "computation"]
    topic: str | None
    created_at: str
    updated_at: str
    messages: list[ChatMessageResponse]


class ProviderStatusResponse(BaseModel):
    name: str
    model: str
    configured: bool
    live: bool


class ChatModeConfigResponse(BaseModel):
    id: Literal["research", "explanation", "tutorial", "computation"]
    description: str
    computation_enabled: bool


class ChatConfigurationResponse(BaseModel):
    schema_version: Literal[1]
    provider: ProviderStatusResponse
    modes: list[ChatModeConfigResponse]
    stream_transport: Literal["sse"]
    conversation_storage: Literal["memory"]
    max_message_chars: int
    max_source_excerpt_chars: int
    external_sources_enabled: bool


def default_config() -> RetrievalConfig:
    """Build local configuration from the working directory and environment."""

    repository_root = Path.cwd()
    content_root = Path(
        os.environ.get("CRAIG_CONTENT_ROOT", repository_root / "content")
    )
    database_path = Path(
        os.environ.get(
            "CRAIG_INDEX_PATH",
            repository_root / ".craig" / "index.sqlite3",
        )
    )
    return RetrievalConfig(
        content_root=content_root,
        database_path=database_path,
    )


def _success_payload(result: object) -> dict[str, Any]:
    return {
        "schema_version": CONTRACT_VERSION,
        **asdict(result),  # type: ignore[arg-type]
    }


def _error_payload(code: str, message: str, **details: object) -> dict[str, Any]:
    error: dict[str, object] = {"code": code, "message": message}
    error.update(details)
    return {"schema_version": CONTRACT_VERSION, "error": error}


def _encode_sse(event: ChatEvent) -> str:
    payload = {
        "schema_version": CONTRACT_VERSION,
        "type": event.type,
        "conversation_id": event.conversation_id,
        "created_at": event.created_at,
        "data": event.data,
    }
    return (
        f"event: {event.type}\n"
        f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"
    )


def create_app(
    config: RetrievalConfig | None = None,
    *,
    chat_service: ChatService | None = None,
) -> FastAPI:
    """Create the versioned retrieval and conversation HTTP application."""

    service = RetrievalService(config or default_config())
    chat = chat_service or ChatService(service)
    app = FastAPI(
        title="CRAIG Local API",
        version="0.4.0",
        description=(
            "Read-only retrieval and in-memory conversational orchestration over "
            "CRAIG's indexed mathematical corpus."
        ),
    )
    app.state.retrieval_service = service
    app.state.chat_service = chat

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(
        request: Request,
        error: RequestValidationError,
    ) -> JSONResponse:
        del request
        return JSONResponse(
            status_code=422,
            content=_error_payload(
                "validation_error",
                "The request body does not match the API contract.",
                details=jsonable_encoder(error.errors()),
            ),
        )

    @app.exception_handler(RetrievalError)
    async def handle_retrieval_error(
        request: Request,
        error: RetrievalError,
    ) -> JSONResponse:
        del request
        if isinstance(error, UnsafeSourcePathError):
            status_code, code = 422, "unsafe_source_path"
        elif isinstance(error, InvalidRetrievalRequest):
            status_code, code = 422, "invalid_request"
        elif isinstance(error, TopicNotFoundError):
            status_code, code = 404, "topic_not_found"
        elif isinstance(error, SourceNotFoundError):
            status_code, code = 404, "source_not_found"
        elif isinstance(error, IndexStaleError):
            status_code, code = 409, "index_stale"
        else:
            status_code, code = 500, "retrieval_error"
        return JSONResponse(
            status_code=status_code,
            content=_error_payload(code, str(error)),
        )

    @app.exception_handler(IndexNotFoundError)
    @app.exception_handler(FTS5UnavailableError)
    async def handle_index_error(
        request: Request,
        error: RuntimeError,
    ) -> JSONResponse:
        del request
        return JSONResponse(
            status_code=503,
            content=_error_payload("index_unavailable", str(error)),
        )

    @app.exception_handler(ChatError)
    async def handle_chat_error(
        request: Request,
        error: ChatError,
    ) -> JSONResponse:
        del request
        if isinstance(error, InvalidChatRequest):
            status_code, code = 422, "invalid_chat_request"
        elif isinstance(error, ConversationNotFoundError):
            status_code, code = 404, "conversation_not_found"
        elif isinstance(error, ProviderUnavailableError):
            status_code, code = 503, "provider_unavailable"
        else:
            status_code, code = 500, "chat_error"
        return JSONResponse(
            status_code=status_code,
            content=_error_payload(code, str(error)),
        )

    @app.get(
        f"{API_PREFIX}/health",
        tags=["system"],
        response_model=HealthResponse,
    )
    def health() -> dict[str, Any]:
        topics = service.list_topics()
        return {
            "schema_version": CONTRACT_VERSION,
            "status": "ok",
            "topic_count": topics.total_topics,
        }

    @app.get(
        f"{API_PREFIX}/topics",
        tags=["retrieval"],
        response_model=TopicListResponse,
    )
    def list_topics() -> dict[str, Any]:
        return _success_payload(service.list_topics())

    @app.post(
        f"{API_PREFIX}/search",
        tags=["retrieval"],
        response_model=SearchPageResponse,
    )
    def search_content(request: SearchRequest) -> dict[str, Any]:
        return _success_payload(
            service.search_content(
                request.query,
                topic=request.topic,
                limit=request.limit,
                offset=request.offset,
                max_chars=request.max_chars,
            )
        )

    @app.post(
        f"{API_PREFIX}/find-exact",
        tags=["retrieval"],
        response_model=ExactMatchPageResponse,
    )
    def find_exact(request: FindExactRequest) -> dict[str, Any]:
        return _success_payload(
            service.find_exact(
                request.query,
                topic=request.topic,
                case_sensitive=request.case_sensitive,
                context_lines=request.context_lines,
                limit=request.limit,
                offset=request.offset,
                max_chars=request.max_chars,
            )
        )

    @app.post(
        f"{API_PREFIX}/read-source",
        tags=["retrieval"],
        response_model=SourceReadResponse,
    )
    def read_source(request: ReadSourceRequest) -> dict[str, Any]:
        return _success_payload(
            service.read_source(
                request.path,
                start_line=request.start_line,
                end_line=request.end_line,
                max_chars=request.max_chars,
            )
        )

    @app.get(
        f"{API_PREFIX}/chat/config",
        tags=["chat"],
        response_model=ChatConfigurationResponse,
    )
    def chat_config() -> dict[str, Any]:
        return {
            "schema_version": CONTRACT_VERSION,
            **chat.public_config(),
        }

    @app.get(
        f"{API_PREFIX}/conversations/{{conversation_id}}",
        tags=["chat"],
        response_model=ConversationResponse,
    )
    def get_conversation(conversation_id: str) -> dict[str, Any]:
        return _success_payload(chat.store.get(conversation_id))

    @app.post(
        f"{API_PREFIX}/chat/stream",
        tags=["chat"],
        response_class=StreamingResponse,
        responses={
            200: {
                "content": {
                    "text/event-stream": {
                        "schema": {"type": "string"},
                    }
                },
                "description": "Typed Server-Sent Events for one chat turn.",
            }
        },
    )
    def stream_chat(request: ChatStreamRequest) -> StreamingResponse:
        turn = chat.prepare(
            message=request.message,
            mode=request.mode,
            topic=request.topic,
            conversation_id=request.conversation_id,
        )

        def events() -> Iterator[str]:
            for event in chat.stream(turn):
                yield _encode_sse(event)

        return StreamingResponse(
            events(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "X-Accel-Buffering": "no",
            },
        )

    frontend_dist = Path(
        os.environ.get(
            "CRAIG_FRONTEND_DIST",
            Path(__file__).resolve().parent.parent / "app" / "frontend" / "dist",
        )
    )
    if frontend_dist.is_dir():
        app.mount(
            "/",
            StaticFiles(directory=frontend_dist, html=True),
            name="frontend",
        )

    return app


app = create_app()
