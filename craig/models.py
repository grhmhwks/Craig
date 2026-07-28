"""Shared data structures for indexing and retrieval."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Chunk:
    """A source passage with exact, one-based source line bounds."""

    heading: str | None
    environment: str | None
    start_line: int
    end_line: int
    text: str


@dataclass(frozen=True, slots=True)
class IndexStats:
    """Summary of one indexing run."""

    discovered_files: int
    indexed_files: int
    skipped_files: int
    removed_files: int
    indexed_chunks: int


@dataclass(frozen=True, slots=True)
class SearchResult:
    """One ranked source passage."""

    rank: int
    score: float
    topic: str
    path: str
    heading: str | None
    start_line: int
    end_line: int
    snippet: str
    file_type: str | None = None
    environment: str | None = None
    file_hash: str | None = None


@dataclass(frozen=True, slots=True)
class TopicSummary:
    """Counts for one indexed corpus topic."""

    topic: str
    file_count: int
    chunk_count: int


@dataclass(frozen=True, slots=True)
class TopicList:
    """All topics visible through the retrieval service."""

    topics: tuple[TopicSummary, ...]
    total_topics: int


@dataclass(frozen=True, slots=True)
class SearchPage:
    """One bounded page of ranked search results."""

    query: str
    topic: str | None
    offset: int
    limit: int
    results: tuple[SearchResult, ...]
    has_more: bool
    next_offset: int | None
    truncated: bool


@dataclass(frozen=True, slots=True)
class ExactMatch:
    """One literal source-text match with bounded surrounding context."""

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


@dataclass(frozen=True, slots=True)
class ExactMatchPage:
    """One bounded page of literal source-text matches."""

    query: str
    topic: str | None
    case_sensitive: bool
    offset: int
    limit: int
    results: tuple[ExactMatch, ...]
    has_more: bool
    next_offset: int | None
    truncated: bool


@dataclass(frozen=True, slots=True)
class SourceRead:
    """A bounded line range read from an indexed source file."""

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
