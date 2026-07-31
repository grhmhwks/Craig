"""Typed contracts shared across conversation storage and orchestration."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, Literal
from uuid import uuid4

ChatMode = Literal["research", "explanation", "tutorial", "computation"]
ChatRole = Literal["user", "assistant"]

CHAT_MODES: tuple[ChatMode, ...] = (
    "research",
    "explanation",
    "tutorial",
    "computation",
)


def utc_timestamp() -> str:
    """Return a stable UTC timestamp for public conversation events."""

    return datetime.now(UTC).isoformat()


def new_identifier(prefix: str) -> str:
    """Return an opaque identifier suitable for local in-memory state."""

    return f"{prefix}_{uuid4().hex}"


@dataclass(frozen=True, slots=True)
class SourceReference:
    """A compact source location retained on an assistant message."""

    topic: str
    path: str
    heading: str | None
    environment: str | None
    start_line: int
    end_line: int
    file_hash: str


@dataclass(frozen=True, slots=True)
class ChatMessage:
    """One immutable message in an in-memory conversation."""

    id: str
    role: ChatRole
    content: str
    created_at: str
    sources: tuple[SourceReference, ...] = ()


@dataclass(frozen=True, slots=True)
class ConversationSnapshot:
    """A safe copy of public conversation state."""

    id: str
    mode: ChatMode
    topic: str | None
    created_at: str
    updated_at: str
    messages: tuple[ChatMessage, ...]


@dataclass(frozen=True, slots=True)
class ToolCall:
    """One provider-requested, read-only retrieval operation."""

    name: str
    arguments: dict[str, Any]
    call_id: str = field(default_factory=lambda: new_identifier("call"))


@dataclass(frozen=True, slots=True)
class ToolResult:
    """The structured result of executing one retrieval tool."""

    call_id: str
    name: str
    arguments: dict[str, Any]
    output: dict[str, Any]
    success: bool


@dataclass(frozen=True, slots=True)
class PlanningRequest:
    """Information available to the provider during retrieval planning."""

    message: str
    mode: ChatMode
    topic: str | None
    conversation: ConversationSnapshot
    system_prompt: str


@dataclass(frozen=True, slots=True)
class AnswerRequest:
    """Grounded context available to the answer-generation stage."""

    message: str
    mode: ChatMode
    topic: str | None
    conversation: ConversationSnapshot
    tool_results: tuple[ToolResult, ...]
    sources: tuple[SourceReference, ...]
    system_prompt: str


@dataclass(frozen=True, slots=True)
class ChatEvent:
    """One typed event emitted through the Phase 3 SSE contract."""

    type: str
    conversation_id: str
    data: dict[str, Any]
    created_at: str = field(default_factory=utc_timestamp)
