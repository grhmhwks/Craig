"""Versioned FastAPI adapter for CRAIG's read-only retrieval service."""

from __future__ import annotations

import os
from dataclasses import asdict
from pathlib import Path
from typing import Any, Literal

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

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
    class Config:
        extra = "forbid"


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


def create_app(config: RetrievalConfig | None = None) -> FastAPI:
    """Create the versioned HTTP adapter around one retrieval service."""

    service = RetrievalService(config or default_config())
    app = FastAPI(
        title="CRAIG Retrieval API",
        version="0.2.0",
        description=(
            "Read-only, bounded retrieval over CRAIG's indexed mathematical corpus."
        ),
    )
    app.state.retrieval_service = service

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
                "The request body does not match the retrieval contract.",
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

    return app


app = create_app()
