"""Thread-safe, bounded, in-memory conversation storage."""

from __future__ import annotations

from dataclasses import dataclass
from threading import RLock

from .errors import ConversationNotFoundError
from .models import (
    ChatMessage,
    ChatMode,
    ChatRole,
    ConversationSnapshot,
    ProvenanceAnnotation,
    SourceReference,
    new_identifier,
    utc_timestamp,
)


@dataclass(slots=True)
class _Conversation:
    id: str
    mode: ChatMode
    topic: str | None
    created_at: str
    updated_at: str
    messages: list[ChatMessage]


class ConversationStore:
    """Keep bounded conversation context in process memory only."""

    def __init__(
        self,
        *,
        max_conversations: int = 128,
        max_messages_per_conversation: int = 50,
        max_context_messages: int = 16,
        max_context_chars: int = 24_000,
    ) -> None:
        self.max_conversations = max_conversations
        self.max_messages_per_conversation = max_messages_per_conversation
        self.max_context_messages = max_context_messages
        self.max_context_chars = max_context_chars
        self._conversations: dict[str, _Conversation] = {}
        self._lock = RLock()

    def create(self, *, mode: ChatMode, topic: str | None) -> ConversationSnapshot:
        """Create a new empty conversation, evicting the oldest when bounded."""

        now = utc_timestamp()
        conversation = _Conversation(
            id=new_identifier("conv"),
            mode=mode,
            topic=topic,
            created_at=now,
            updated_at=now,
            messages=[],
        )
        with self._lock:
            if len(self._conversations) >= self.max_conversations:
                oldest = min(
                    self._conversations.values(),
                    key=lambda item: item.updated_at,
                )
                self._conversations.pop(oldest.id, None)
            self._conversations[conversation.id] = conversation
            return self._snapshot(conversation)

    def get(self, conversation_id: str) -> ConversationSnapshot:
        """Return one conversation or a stable not-found error."""

        with self._lock:
            conversation = self._conversations.get(conversation_id)
            if conversation is None:
                raise ConversationNotFoundError(
                    f"Conversation is not available in memory: {conversation_id}"
                )
            return self._snapshot(conversation)

    def update_scope(
        self,
        conversation_id: str,
        *,
        mode: ChatMode,
        topic: str | None,
    ) -> ConversationSnapshot:
        """Apply the active mode and topic to a follow-up turn."""

        with self._lock:
            conversation = self._require(conversation_id)
            conversation.mode = mode
            conversation.topic = topic
            conversation.updated_at = utc_timestamp()
            return self._snapshot(conversation)

    def append(
        self,
        conversation_id: str,
        *,
        role: ChatRole,
        content: str,
        sources: tuple[SourceReference, ...] = (),
        provenance: tuple[ProvenanceAnnotation, ...] = (),
    ) -> ChatMessage:
        """Append one message and enforce the per-conversation bound."""

        if role not in {"user", "assistant"}:
            raise ValueError(f"Unsupported chat role: {role}")
        message = ChatMessage(
            id=new_identifier("msg"),
            role=role,
            content=content,
            created_at=utc_timestamp(),
            sources=sources,
            provenance=provenance,
        )
        with self._lock:
            conversation = self._require(conversation_id)
            conversation.messages.append(message)
            if len(conversation.messages) > self.max_messages_per_conversation:
                overflow = (
                    len(conversation.messages) - self.max_messages_per_conversation
                )
                del conversation.messages[:overflow]
            conversation.updated_at = message.created_at
        return message

    def context(self, conversation_id: str) -> ConversationSnapshot:
        """Return the newest bounded messages within the context character cap."""

        with self._lock:
            conversation = self._require(conversation_id)
            selected: list[ChatMessage] = []
            used_chars = 0
            for message in reversed(conversation.messages):
                if len(selected) >= self.max_context_messages:
                    break
                remaining = self.max_context_chars - used_chars
                if remaining < 1:
                    break
                if len(message.content) > remaining:
                    clipped = ChatMessage(
                        id=message.id,
                        role=message.role,
                        content=message.content[-remaining:],
                        created_at=message.created_at,
                        sources=message.sources,
                        provenance=message.provenance,
                    )
                    selected.append(clipped)
                    break
                selected.append(message)
                used_chars += len(message.content)
            selected.reverse()
            snapshot = self._snapshot(conversation)
            return ConversationSnapshot(
                id=snapshot.id,
                mode=snapshot.mode,
                topic=snapshot.topic,
                created_at=snapshot.created_at,
                updated_at=snapshot.updated_at,
                messages=tuple(selected),
            )

    def _require(self, conversation_id: str) -> _Conversation:
        conversation = self._conversations.get(conversation_id)
        if conversation is None:
            raise ConversationNotFoundError(
                f"Conversation is not available in memory: {conversation_id}"
            )
        return conversation

    @staticmethod
    def _snapshot(conversation: _Conversation) -> ConversationSnapshot:
        return ConversationSnapshot(
            id=conversation.id,
            mode=conversation.mode,
            topic=conversation.topic,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at,
            messages=tuple(conversation.messages),
        )
