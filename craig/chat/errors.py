"""Errors raised by CRAIG's in-memory conversational layer."""

from __future__ import annotations


class ChatError(RuntimeError):
    """Base class for errors safe to expose through the chat API."""


class InvalidChatRequest(ChatError, ValueError):
    """Raised when a chat request violates the public contract."""


class ConversationNotFoundError(ChatError):
    """Raised when an in-memory conversation identifier is unknown."""


class ProviderUnavailableError(ChatError):
    """Raised when the configured model provider cannot serve a request."""
