"""Bounded retrieval-planning and answer-generation orchestration."""

from __future__ import annotations

import json
from collections.abc import Iterator
from dataclasses import asdict, dataclass
from typing import cast

from ..retrieval import RetrievalService
from .errors import InvalidChatRequest
from .models import (
    CHAT_MODES,
    AnswerRequest,
    ChatEvent,
    ChatMode,
    PlanningRequest,
    ProvenanceAnnotation,
    SourceReference,
    ToolCall,
    ToolResult,
)
from .prompts import initial_system_prompt, mode_description, secondary_system_prompt
from .provenance import (
    MAX_SOURCE_EXCERPT_CHARS,
    bounded_excerpt,
    citation_identifier,
    classify_mathematical_status,
)
from .providers import ModelProvider, provider_from_environment
from .store import ConversationStore
from .tools import RetrievalToolRegistry


@dataclass(frozen=True, slots=True)
class ChatConfig:
    """Hard limits for one conversational service."""

    max_message_chars: int = 8_000
    max_tool_rounds: int = 3
    max_tool_calls: int = 8
    external_sources_enabled: bool = False


@dataclass(frozen=True, slots=True)
class PreparedTurn:
    """Validated state created before SSE response headers are sent."""

    conversation_id: str
    message: str
    mode: ChatMode
    topic: str | None
    created: bool
    user_message_id: str


class ChatService:
    """Coordinate provider planning, bounded retrieval, context, and streaming."""

    def __init__(
        self,
        retrieval: RetrievalService,
        *,
        provider: ModelProvider | None = None,
        store: ConversationStore | None = None,
        config: ChatConfig | None = None,
    ) -> None:
        self.retrieval = retrieval
        self.provider = provider or provider_from_environment()
        self.store = store or ConversationStore()
        self.config = config or ChatConfig()
        self.tools = RetrievalToolRegistry(retrieval)

    def public_config(self) -> dict[str, object]:
        """Return browser-safe modes, limits, and provider state."""

        metadata = self.provider.metadata
        return {
            "provider": asdict(metadata),
            "modes": [
                {
                    "id": mode,
                    "description": mode_description(mode),
                    "computation_enabled": mode == "computation",
                }
                for mode in CHAT_MODES
            ],
            "stream_transport": "sse",
            "conversation_storage": "memory",
            "max_message_chars": self.config.max_message_chars,
            "max_source_excerpt_chars": MAX_SOURCE_EXCERPT_CHARS,
            "external_sources_enabled": self.config.external_sources_enabled,
        }

    def prepare(
        self,
        *,
        message: str,
        mode: str,
        topic: str | None,
        conversation_id: str | None,
    ) -> PreparedTurn:
        """Validate and record a user turn before streaming starts."""

        checked_message = self._validate_message(message)
        checked_mode = self._validate_mode(mode)
        checked_topic = self._validate_topic(topic)
        if conversation_id is None:
            conversation = self.store.create(
                mode=checked_mode,
                topic=checked_topic,
            )
            created = True
        else:
            conversation = self.store.update_scope(
                conversation_id,
                mode=checked_mode,
                topic=checked_topic,
            )
            created = False
        user_message = self.store.append(
            conversation.id,
            role="user",
            content=checked_message,
        )
        return PreparedTurn(
            conversation_id=conversation.id,
            message=checked_message,
            mode=checked_mode,
            topic=checked_topic,
            created=created,
            user_message_id=user_message.id,
        )

    def stream(self, turn: PreparedTurn) -> Iterator[ChatEvent]:
        """Yield the complete typed event sequence for one user turn."""

        conversation_event = (
            "conversation.created" if turn.created else "conversation.resumed"
        )
        yield self._event(
            conversation_event,
            turn,
            {"conversation_id": turn.conversation_id},
        )
        yield self._event(
            "message.accepted",
            turn,
            {"message_id": turn.user_message_id},
        )
        try:
            yield self._event(
                "status",
                turn,
                {"phase": "planning", "label": "Planning repository search"},
            )
            conversation = self.store.context(turn.conversation_id)
            planning_request = PlanningRequest(
                message=turn.message,
                mode=turn.mode,
                topic=turn.topic,
                conversation=conversation,
                system_prompt=initial_system_prompt(turn.mode, turn.topic),
            )
            calls = self.provider.plan(planning_request)
            tool_results = self._run_tools(turn, planning_request, calls)
            for event_or_result in tool_results:
                if isinstance(event_or_result, ChatEvent):
                    yield event_or_result

            results = tuple(
                item
                for item in tool_results
                if isinstance(item, ToolResult)
            )
            sources = self._collect_sources(results)
            yield self._event(
                "status",
                turn,
                {"phase": "generating", "label": "Writing grounded response"},
            )
            answer_request = AnswerRequest(
                message=turn.message,
                mode=turn.mode,
                topic=turn.topic,
                conversation=self.store.context(turn.conversation_id),
                tool_results=results,
                sources=sources,
                system_prompt=secondary_system_prompt(
                    turn.mode,
                    turn.topic,
                    results,
                    sources,
                ),
            )
            provenance = self._collect_provenance(answer_request)
            yield self._event(
                "sources.ready",
                turn,
                {
                    "sources": [asdict(source) for source in sources],
                    "provenance": [
                        asdict(annotation) for annotation in provenance
                    ],
                },
            )
            fragments: list[str] = []
            for fragment in self.provider.stream_answer(answer_request):
                text = str(fragment)
                if not text:
                    continue
                fragments.append(text)
                yield self._event("text.delta", turn, {"delta": text})
            content = "".join(fragments).strip()
            if not content:
                content = "No answer text was produced by the configured provider."
                yield self._event("text.delta", turn, {"delta": content})
            assistant = self.store.append(
                turn.conversation_id,
                role="assistant",
                content=content,
                sources=sources,
                provenance=provenance,
            )
            yield self._event(
                "message.completed",
                turn,
                {"message": asdict(assistant)},
            )
        except Exception as error:
            yield self._event(
                "error",
                turn,
                {
                    "code": "chat_failed",
                    "message": str(error),
                },
            )

    def _run_tools(
        self,
        turn: PreparedTurn,
        planning_request: PlanningRequest,
        calls: tuple[ToolCall, ...],
    ) -> list[ChatEvent | ToolResult]:
        emitted: list[ChatEvent | ToolResult] = []
        seen_calls: set[str] = set()
        total_calls = 0
        current_calls = calls
        results: list[ToolResult] = []
        for _round in range(self.config.max_tool_rounds):
            if not current_calls:
                break
            for call in current_calls:
                signature = json.dumps(
                    {"name": call.name, "arguments": call.arguments},
                    sort_keys=True,
                    default=str,
                )
                if signature in seen_calls:
                    continue
                if total_calls >= self.config.max_tool_calls:
                    break
                seen_calls.add(signature)
                total_calls += 1
                emitted.append(
                    self._event(
                        "tool.call",
                        turn,
                        {
                            "call_id": call.call_id,
                            "name": call.name,
                            "arguments": call.arguments,
                        },
                    )
                )
                result = self.tools.execute(call)
                results.append(result)
                emitted.append(result)
                emitted.append(
                    self._event(
                        "tool.result",
                        turn,
                        {
                            "call_id": result.call_id,
                            "name": result.name,
                            "success": result.success,
                            "output": result.output,
                        },
                    )
                )
            current_calls = self.provider.refine(
                planning_request,
                tuple(results),
            )
        return emitted

    @staticmethod
    def _collect_sources(
        results: tuple[ToolResult, ...],
    ) -> tuple[SourceReference, ...]:
        sources: list[SourceReference] = []
        positions: dict[tuple[object, ...], int] = {}
        for result in results:
            if not result.success:
                continue
            if result.name in {"search_content", "find_exact"}:
                raw = result.output.get("results", ())
            elif result.name == "read_source":
                raw = (result.output,)
            else:
                continue
            if not isinstance(raw, (list, tuple)):
                continue
            for item in raw:
                if not isinstance(item, dict):
                    continue
                start = item.get(
                    "start_line",
                    item.get("match_start_line"),
                )
                end = item.get("end_line", item.get("match_end_line"))
                path = item.get("path")
                topic = item.get("topic")
                file_hash = item.get("file_hash")
                if not (
                    isinstance(path, str)
                    and isinstance(topic, str)
                    and isinstance(start, int)
                    and isinstance(end, int)
                    and isinstance(file_hash, str)
                ):
                    continue
                key = (path, start, end, file_hash)
                heading = (
                    str(item["heading"])
                    if item.get("heading") is not None
                    else None
                )
                environment = (
                    str(item["environment"])
                    if item.get("environment") is not None
                    else None
                )
                mathematical_status, status_basis = (
                    classify_mathematical_status(
                        heading=heading,
                        environment=environment,
                    )
                )
                source = SourceReference(
                    citation_id=citation_identifier(
                        path=path,
                        start_line=start,
                        end_line=end,
                        file_hash=file_hash,
                    ),
                    topic=topic,
                    path=path,
                    heading=heading,
                    environment=environment,
                    start_line=start,
                    end_line=end,
                    file_hash=file_hash,
                    excerpt=bounded_excerpt(item),
                    mathematical_status=mathematical_status,
                    status_basis=status_basis,
                )
                existing_position = positions.get(key)
                if existing_position is not None:
                    if (
                        result.name == "read_source"
                        or len(source.excerpt)
                        > len(sources[existing_position].excerpt)
                    ):
                        sources[existing_position] = source
                    continue
                positions[key] = len(sources)
                sources.append(source)
        return tuple(sources)

    def _collect_provenance(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        annotations: list[ProvenanceAnnotation] = []
        if request.sources:
            annotations.append(
                ProvenanceAnnotation(
                    kind="repository",
                    description=(
                        "The displayed source passages are explicit repository "
                        "material."
                    ),
                    citation_ids=tuple(
                        source.citation_id for source in request.sources
                    ),
                )
            )
        provider_annotations = self.provider.answer_annotations(request)
        available_citations = {
            source.citation_id for source in request.sources
        }
        for annotation in provider_annotations:
            if (
                annotation.kind == "external"
                and not self.config.external_sources_enabled
            ):
                continue
            valid_citations = tuple(
                citation_id
                for citation_id in annotation.citation_ids
                if citation_id in available_citations
            )
            annotations.append(
                ProvenanceAnnotation(
                    kind=annotation.kind,
                    description=annotation.description,
                    citation_ids=valid_citations,
                )
            )
        return tuple(annotations)

    def _validate_message(self, message: str) -> str:
        if not isinstance(message, str) or not message.strip():
            raise InvalidChatRequest("message must be a non-empty string.")
        if len(message) > self.config.max_message_chars:
            raise InvalidChatRequest(
                f"message cannot exceed {self.config.max_message_chars} characters."
            )
        return message.strip()

    @staticmethod
    def _validate_mode(mode: str) -> ChatMode:
        if mode not in CHAT_MODES:
            raise InvalidChatRequest(
                f"mode must be one of: {', '.join(CHAT_MODES)}."
            )
        return cast(ChatMode, mode)

    def _validate_topic(self, topic: str | None) -> str | None:
        if topic is None:
            return None
        if not isinstance(topic, str) or not topic:
            raise InvalidChatRequest("topic must be null or a non-empty string.")
        topics = {item.topic for item in self.retrieval.list_topics().topics}
        if topic not in topics:
            raise InvalidChatRequest(f"Unknown indexed topic: {topic}")
        return topic

    @staticmethod
    def _event(
        event_type: str,
        turn: PreparedTurn,
        data: dict[str, object],
    ) -> ChatEvent:
        return ChatEvent(
            type=event_type,
            conversation_id=turn.conversation_id,
            data=data,
        )
