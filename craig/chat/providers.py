"""Provider-neutral planning and answer-generation interfaces."""

from __future__ import annotations

import http.client
import ipaddress
import json
import os
import re
import socket
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, Callable, Literal, Protocol

from .errors import ProviderUnavailableError
from .models import (
    AnswerRequest,
    PlanningRequest,
    ProvenanceAnnotation,
    ToolCall,
    ToolResult,
)


@dataclass(frozen=True, slots=True)
class ProviderMetadata:
    """Non-secret provider information safe to return to the browser."""

    name: str
    model: str
    configured: bool
    live: bool
    data_destination: Literal["none", "local_model", "remote_model"] = "none"


class ModelProvider(Protocol):
    """Two-stage provider contract used by the orchestration service."""

    @property
    def metadata(self) -> ProviderMetadata:
        """Return browser-safe provider status."""

    def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
        """Choose initial read-only retrieval calls."""

    def refine(
        self,
        request: PlanningRequest,
        results: tuple[ToolResult, ...],
    ) -> tuple[ToolCall, ...]:
        """Choose a bounded follow-up retrieval step, if one is useful."""

    def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
        """Yield text fragments for the grounded assistant answer."""

    def answer_annotations(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        """Describe non-repository reasoning or knowledge used in the answer."""


class DemoModelProvider:
    """Deterministic local provider for UI development and orchestration tests."""

    metadata = ProviderMetadata(
        name="demo",
        model="deterministic-retrieval",
        configured=True,
        live=False,
    )
    max_expanded_sources = 4

    def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
        """Plan a small lexical search, optionally adding exact-text lookup."""

        lowered = request.message.casefold()
        if any(
            phrase in lowered
            for phrase in ("list topics", "which topics", "what topics")
        ):
            return (ToolCall(name="list_topics", arguments={}),)

        shared = {
            "query": request.message,
            "topic": request.topic,
            "limit": 4,
            "max_chars": 6_000,
        }
        calls = [ToolCall(name="search_content", arguments=shared)]
        quoted = re.search(r"[\"“](.{2,160}?)[\"”]", request.message)
        if quoted:
            calls.append(
                ToolCall(
                    name="find_exact",
                    arguments={
                        "query": quoted.group(1),
                        "topic": request.topic,
                        "case_sensitive": False,
                        "context_lines": 2,
                        "limit": 3,
                        "max_chars": 4_000,
                    },
                )
            )
        return tuple(calls)

    def refine(
        self,
        request: PlanningRequest,
        results: tuple[ToolResult, ...],
    ) -> tuple[ToolCall, ...]:
        """Expand several ranked passages after the initial bounded search."""

        del request
        if any(result.name == "read_source" for result in results):
            return ()
        calls: list[ToolCall] = []
        seen_ranges: set[tuple[str, int, int]] = set()
        for result in results:
            if not result.success or result.name not in {
                "search_content",
                "find_exact",
            }:
                continue
            candidates = result.output.get("results")
            if not isinstance(candidates, (list, tuple)) or not candidates:
                continue
            for candidate in candidates:
                if not isinstance(candidate, dict):
                    continue
                path = candidate.get("path")
                start = candidate.get(
                    "start_line",
                    candidate.get(
                        "excerpt_start_line",
                        candidate.get("match_start_line"),
                    ),
                )
                end = candidate.get(
                    "end_line",
                    candidate.get(
                        "excerpt_end_line",
                        candidate.get("match_end_line"),
                    ),
                )
                if not (
                    isinstance(path, str)
                    and isinstance(start, int)
                    and isinstance(end, int)
                ):
                    continue
                source_range = (path, start, end)
                if source_range in seen_ranges:
                    continue
                seen_ranges.add(source_range)
                calls.append(
                    ToolCall(
                        name="read_source",
                        arguments={
                            "path": path,
                            "start_line": start,
                            "end_line": end,
                            "max_chars": 8_000,
                        },
                    )
                )
                if len(calls) >= self.max_expanded_sources:
                    return tuple(calls)
        return tuple(calls)

    def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
        """Yield a transparent retrieval summary without claiming model insight."""

        answer = self._answer(request)
        pieces = re.findall(r"\S+\s*", answer)
        for index in range(0, len(pieces), 10):
            yield "".join(pieces[index : index + 10])

    def answer_annotations(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        """Label retrieval ranking and optional tutorial guidance explicitly."""

        annotations: list[ProvenanceAnnotation] = []
        citation_ids = tuple(source.citation_id for source in request.sources)
        if citation_ids:
            annotations.append(
                ProvenanceAnnotation(
                    kind="deduction",
                    description=(
                        "CRAIG selected and ordered these passages using lexical "
                        "retrieval; that relevance ordering is not a statement "
                        "made by the repository."
                    ),
                    citation_ids=citation_ids,
                )
            )
        else:
            annotations.append(
                ProvenanceAnnotation(
                    kind="deduction",
                    description=(
                        "The no-result statement describes this bounded lexical "
                        "search; it does not prove that the corpus contains no "
                        "relevant material."
                    ),
                )
            )
        if request.mode == "tutorial" and request.sources:
            annotations.append(
                ProvenanceAnnotation(
                    kind="model_knowledge",
                    description=(
                        "The suggested reading sequence is general pedagogical "
                        "guidance supplied by CRAIG."
                    ),
                )
            )
        return tuple(annotations)

    def _answer(self, request: AnswerRequest) -> str:
        if request.mode == "computation":
            preface = (
                "This conversational turn performed retrieval only; I did not "
                "run repository code. Approved Phase 7 jobs and deterministic "
                "traces are available in "
                "the computation panel. Here is the indexed material most "
                "relevant to the request."
            )
        elif request.mode == "tutorial":
            preface = (
                "Here is a guided starting point through the most relevant "
                "repository material."
            )
        elif request.mode == "explanation":
            preface = (
                "Here are the source passages that most directly support an "
                "explanation of the question."
            )
        else:
            preface = (
                "Here are the strongest indexed findings for this research "
                "question."
            )

        if not request.sources:
            return (
                f"{preface}\n\nNo matching passage was found in the current "
                "lexical index. Try a shorter mathematical term, an exact quoted "
                "phrase, or a different topic scope."
            )

        sections = [preface]
        for index, source in enumerate(request.sources, start=1):
            heading = source.heading or "Source passage"
            compact_excerpt = re.sub(r"\s+", " ", source.excerpt).strip()
            status = source.mathematical_status.replace("_", " ")
            sections.append(
                f"### {index}. {heading} [{source.citation_id}]\n\n"
                f"{compact_excerpt}\n\n"
                f"Status: **{status}**  \n"
                f"`content/{source.path}:{source.start_line}-{source.end_line}`"
            )
        if request.mode == "tutorial":
            sections.append(
                "A useful next step is to open the first cited section, identify "
                "its definitions, and then compare them with the next retrieved "
                "passage."
            )
        return "\n\n".join(sections)


ProviderRequester = Callable[
    [str, dict[str, Any], dict[str, str], float, int],
    dict[str, Any],
]

MAX_PROVIDER_REQUEST_BYTES = 262_144
DEFAULT_PROVIDER_RESPONSE_BYTES = 1_048_576


def _bounded_float(value: str, name: str, minimum: float, maximum: float) -> float:
    try:
        parsed = float(value)
    except ValueError as error:
        raise ValueError(f"{name} must be a number") from error
    if not minimum <= parsed <= maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}")
    return parsed


def _bounded_int(value: str, name: str, minimum: int, maximum: int) -> int:
    try:
        parsed = int(value)
    except ValueError as error:
        raise ValueError(f"{name} must be an integer") from error
    if not minimum <= parsed <= maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}")
    return parsed


def _validated_base_url(value: str, *, loopback_only: bool) -> str:
    parsed = urllib.parse.urlsplit(value.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("CRAIG_MODEL_BASE_URL must be an HTTP(S) URL")
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError(
            "CRAIG_MODEL_BASE_URL cannot contain credentials, query, or fragment"
        )
    if loopback_only:
        hostname = parsed.hostname.casefold()
        is_loopback = hostname == "localhost"
        if not is_loopback:
            try:
                is_loopback = ipaddress.ip_address(hostname).is_loopback
            except ValueError:
                is_loopback = False
        if not is_loopback:
            raise ValueError("local model endpoints must use a loopback host")
    return value.strip().rstrip("/")


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Keep a validated loopback request from being redirected elsewhere."""

    def redirect_request(
        self,
        request: urllib.request.Request,
        file_pointer: Any,
        code: int,
        message: str,
        headers: Any,
        new_url: str,
    ) -> None:
        del request, file_pointer, code, message, headers, new_url
        return None


def _post_json(
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
    timeout_seconds: float,
    max_response_bytes: int,
) -> dict[str, Any]:
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode(
        "utf-8"
    )
    if len(encoded) > MAX_PROVIDER_REQUEST_BYTES:
        raise ProviderUnavailableError("The bounded model request is too large.")
    request = urllib.request.Request(
        url,
        data=encoded,
        headers=headers,
        method="POST",
    )
    try:
        opener = urllib.request.build_opener(_NoRedirectHandler())
        with opener.open(request, timeout=timeout_seconds) as response:
            body = response.read(max_response_bytes + 1)
    except urllib.error.HTTPError as error:
        request_id = error.headers.get("x-request-id") if error.headers else None
        if request_id:
            request_id = re.sub(r"[^A-Za-z0-9._:-]", "", request_id)[:128]
        suffix = f" Request ID: {request_id}." if request_id else ""
        if error.code == 429:
            raise ProviderUnavailableError(
                "The configured model provider's request limit was reached. "
                f"Wait for its quota window to reset and retry.{suffix}"
            ) from error
        raise ProviderUnavailableError(
            f"The configured model endpoint returned HTTP {error.code}.{suffix}"
        ) from error
    except (
        urllib.error.URLError,
        TimeoutError,
        socket.timeout,
        http.client.HTTPException,
        OSError,
    ) as error:
        raise ProviderUnavailableError(
            "The configured model endpoint could not be reached within its timeout."
        ) from error
    if len(body) > max_response_bytes:
        raise ProviderUnavailableError("The model response exceeded its byte limit.")
    try:
        value = json.loads(body)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ProviderUnavailableError(
            "The configured model endpoint returned invalid JSON."
        ) from error
    if not isinstance(value, dict):
        raise ProviderUnavailableError(
            "The configured model endpoint returned an invalid response object."
        )
    return value


class OpenAICompatibleProvider:
    """Grounded synthesis through a bounded Chat Completions-compatible API."""

    def __init__(
        self,
        *,
        name: str,
        model: str,
        base_url: str,
        api_key: str | None,
        data_destination: Literal["local_model", "remote_model"],
        timeout_seconds: float = 60.0,
        max_output_tokens: int = 2_000,
        max_response_bytes: int = DEFAULT_PROVIDER_RESPONSE_BYTES,
        token_parameter: Literal["max_tokens", "max_completion_tokens"] | None = None,
        requester: ProviderRequester | None = None,
    ) -> None:
        if not name.strip() or not model.strip():
            raise ValueError("provider name and model must be non-empty")
        if len(name) > 64 or len(model) > 256:
            raise ValueError("provider name or model identifier is too long")
        if api_key and any(character in api_key for character in "\r\n"):
            raise ValueError("provider API keys cannot contain line breaks")
        if not 1 <= timeout_seconds <= 180:
            raise ValueError("timeout_seconds must be between 1 and 180")
        if not 64 <= max_output_tokens <= 32_768:
            raise ValueError("max_output_tokens must be between 64 and 32768")
        if not 1_024 <= max_response_bytes <= 4_194_304:
            raise ValueError("max_response_bytes must be between 1024 and 4194304")
        self.base_url = _validated_base_url(
            base_url,
            loopback_only=data_destination == "local_model",
        )
        self.api_key = api_key or None
        self.timeout_seconds = timeout_seconds
        self.max_output_tokens = max_output_tokens
        self.max_response_bytes = max_response_bytes
        self.token_parameter = token_parameter or (
            "max_tokens"
            if data_destination == "local_model"
            else "max_completion_tokens"
        )
        self._requester = requester or _post_json
        self._retrieval = DemoModelProvider()
        self.metadata = ProviderMetadata(
            name=name.strip(),
            model=model.strip(),
            configured=True,
            live=True,
            data_destination=data_destination,
        )

    def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
        """Use deterministic bounded planning so models cannot invent tools."""

        return self._retrieval.plan(request)

    def refine(
        self,
        request: PlanningRequest,
        results: tuple[ToolResult, ...],
    ) -> tuple[ToolCall, ...]:
        return self._retrieval.refine(request, results)

    @staticmethod
    def _answer_context(request: AnswerRequest) -> str:
        recent = request.conversation.messages[-6:]
        conversation = [
            {
                "role": message.role,
                "content": message.content[:4_000],
            }
            for message in recent
        ]
        sources = [
            {
                "citation_id": source.citation_id,
                "path": source.path,
                "lines": [source.start_line, source.end_line],
                "mathematical_status": source.mathematical_status,
                "excerpt": source.excerpt[:4_000],
            }
            for source in request.sources
        ]
        return json.dumps(
            {
                "question": request.message,
                "mode": request.mode,
                "topic": request.topic,
                "recent_conversation": conversation,
                "retrieved_sources": sources,
            },
            ensure_ascii=False,
            indent=2,
        )

    @staticmethod
    def _response_text(response: dict[str, Any]) -> str:
        choices = response.get("choices")
        if not isinstance(choices, list) or not choices:
            raise ProviderUnavailableError(
                "The model response did not contain a completion choice."
            )
        first = choices[0]
        message = first.get("message") if isinstance(first, dict) else None
        content = message.get("content") if isinstance(message, dict) else None
        if isinstance(content, str):
            text = content
        elif isinstance(content, list):
            parts: list[str] = []
            for part in content:
                if not isinstance(part, dict):
                    continue
                value = part.get("text")
                if isinstance(value, str):
                    parts.append(value)
            text = "".join(parts)
        else:
            text = ""
        if not text.strip():
            raise ProviderUnavailableError(
                "The model response contained no answer text."
            )
        return text

    def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "craig-local/1.0",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload: dict[str, Any] = {
            "model": self.metadata.model,
            "messages": [
                {"role": "system", "content": request.system_prompt},
                {"role": "user", "content": self._answer_context(request)},
            ],
            self.token_parameter: self.max_output_tokens,
            "stream": False,
        }
        response = self._requester(
            f"{self.base_url}/chat/completions",
            payload,
            headers,
            self.timeout_seconds,
            self.max_response_bytes,
        )
        answer = self._response_text(response)
        pieces = re.findall(r"\S+\s*", answer)
        for index in range(0, len(pieces), 12):
            yield "".join(pieces[index : index + 12])

    def answer_annotations(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        del request
        return (
            ProvenanceAnnotation(
                kind="model_knowledge",
                description=(
                    f"The configured {self.metadata.name} model "
                    f"({self.metadata.model}) synthesized the answer. Any claim "
                    "without a repository citation is model knowledge, not "
                    "corpus evidence."
                ),
            ),
        )


class UnavailableModelProvider:
    """Stable failure provider for unsupported or unconfigured selections."""

    def __init__(self, name: str, model: str, *, reason: str | None = None) -> None:
        self.metadata = ProviderMetadata(
            name=name,
            model=model,
            configured=False,
            live=False,
        )
        self.reason = reason

    def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
        del request
        self._raise()

    def refine(
        self,
        request: PlanningRequest,
        results: tuple[ToolResult, ...],
    ) -> tuple[ToolCall, ...]:
        del request, results
        self._raise()

    def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
        del request
        self._raise()

    def answer_annotations(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        del request
        self._raise()

    def _raise(self) -> None:
        if self.reason:
            raise ProviderUnavailableError(self.reason)
        raise ProviderUnavailableError(
            f"Model provider `{self.metadata.name}` is not configured or supported. "
            "Set CRAIG_MODEL_PROVIDER=demo to use the local retrieval demonstration."
        )


def provider_from_environment() -> ModelProvider:
    """Create the selected provider without reading or returning any secret."""

    name = os.environ.get("CRAIG_MODEL_PROVIDER", "demo").strip().casefold()
    model = os.environ.get("CRAIG_MODEL", "").strip()
    if name == "demo":
        return DemoModelProvider()
    try:
        timeout = _bounded_float(
            os.environ.get("CRAIG_MODEL_TIMEOUT_SECONDS", "60"),
            "CRAIG_MODEL_TIMEOUT_SECONDS",
            1,
            180,
        )
        max_tokens = _bounded_int(
            os.environ.get("CRAIG_MODEL_MAX_OUTPUT_TOKENS", "2000"),
            "CRAIG_MODEL_MAX_OUTPUT_TOKENS",
            64,
            32_768,
        )
        max_bytes = _bounded_int(
            os.environ.get(
                "CRAIG_MODEL_MAX_RESPONSE_BYTES",
                str(DEFAULT_PROVIDER_RESPONSE_BYTES),
            ),
            "CRAIG_MODEL_MAX_RESPONSE_BYTES",
            1_024,
            4_194_304,
        )
        if name == "openai":
            key = os.environ.get("OPENAI_API_KEY", "").strip()
            if not model or not key:
                raise ValueError(
                    "The openai provider requires CRAIG_MODEL and OPENAI_API_KEY."
                )
            return OpenAICompatibleProvider(
                name="openai",
                model=model,
                base_url="https://api.openai.com/v1",
                api_key=key,
                data_destination="remote_model",
                timeout_seconds=timeout,
                max_output_tokens=max_tokens,
                max_response_bytes=max_bytes,
                token_parameter="max_completion_tokens",
            )
        if name == "groq":
            key = os.environ.get("GROQ_API_KEY", "").strip()
            if not model or not key:
                raise ValueError(
                    "The groq provider requires CRAIG_MODEL and GROQ_API_KEY."
                )
            return OpenAICompatibleProvider(
                name="groq",
                model=model,
                base_url="https://api.groq.com/openai/v1",
                api_key=key,
                data_destination="remote_model",
                timeout_seconds=timeout,
                max_output_tokens=max_tokens,
                max_response_bytes=max_bytes,
                token_parameter="max_completion_tokens",
            )
        if name == "cloudflare":
            account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
            token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
            if not model or not account_id or not token:
                raise ValueError(
                    "The cloudflare provider requires CRAIG_MODEL, "
                    "CLOUDFLARE_ACCOUNT_ID, and CLOUDFLARE_API_TOKEN."
                )
            if not re.fullmatch(r"[0-9A-Fa-f]{32}", account_id):
                raise ValueError(
                    "CLOUDFLARE_ACCOUNT_ID must be a 32-character hexadecimal "
                    "Cloudflare account ID."
                )
            return OpenAICompatibleProvider(
                name="cloudflare",
                model=model,
                base_url=(
                    "https://api.cloudflare.com/client/v4/accounts/"
                    f"{account_id}/ai/v1"
                ),
                api_key=token,
                data_destination="remote_model",
                timeout_seconds=timeout,
                max_output_tokens=max_tokens,
                max_response_bytes=max_bytes,
                token_parameter="max_tokens",
            )
        if name == "local":
            if not model:
                raise ValueError("The local provider requires CRAIG_MODEL.")
            return OpenAICompatibleProvider(
                name="local",
                model=model,
                base_url=(
                    os.environ.get("CRAIG_MODEL_BASE_URL", "").strip()
                    or "http://127.0.0.1:11434/v1"
                ),
                api_key=os.environ.get("CRAIG_MODEL_API_KEY", "").strip() or None,
                data_destination="local_model",
                timeout_seconds=timeout,
                max_output_tokens=max_tokens,
                max_response_bytes=max_bytes,
                token_parameter="max_tokens",
            )
    except ValueError as error:
        return UnavailableModelProvider(
            name=name or "unconfigured",
            model=model or "unconfigured",
            reason=str(error),
        )
    return UnavailableModelProvider(
        name=name or "unconfigured",
        model=model or "unconfigured",
    )
