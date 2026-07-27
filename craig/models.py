"""Shared data structures for indexing and search."""

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
