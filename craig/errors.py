"""Domain errors raised by CRAIG's read-only retrieval service."""

from __future__ import annotations


class RetrievalError(RuntimeError):
    """Base class for errors safe to translate into retrieval API responses."""


class InvalidRetrievalRequest(RetrievalError, ValueError):
    """Raised when a retrieval request violates a public contract."""


class TopicNotFoundError(RetrievalError):
    """Raised when a request names a topic absent from the index."""


class SourceNotFoundError(RetrievalError):
    """Raised when a request names a source absent from the index."""


class UnsafeSourcePathError(InvalidRetrievalRequest):
    """Raised when a source path could leave the approved corpus."""


class IndexStaleError(RetrievalError):
    """Raised when a source no longer matches its indexed hash."""
