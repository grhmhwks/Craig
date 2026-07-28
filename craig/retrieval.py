"""Safe, framework-independent retrieval over CRAIG's indexed corpus."""

from __future__ import annotations

import bisect
import hashlib
import re
import sqlite3
from dataclasses import dataclass, replace
from pathlib import Path, PurePosixPath

from .errors import (
    IndexStaleError,
    InvalidRetrievalRequest,
    SourceNotFoundError,
    TopicNotFoundError,
    UnsafeSourcePathError,
)
from .models import (
    ExactMatch,
    ExactMatchPage,
    SearchPage,
    SourceRead,
    TopicList,
    TopicSummary,
)
from .search import DEFAULT_EXPLANATION_BOOST, DEFAULT_LIMIT, search_index
from .storage import require_index


@dataclass(frozen=True, slots=True)
class RetrievalConfig:
    """Filesystem locations and hard public limits for retrieval requests."""

    content_root: Path
    database_path: Path
    default_limit: int = DEFAULT_LIMIT
    max_results: int = 50
    max_offset: int = 100_000
    max_query_chars: int = 500
    default_read_lines: int = 80
    max_read_lines: int = 200
    max_context_lines: int = 10
    max_excerpt_chars: int = 2_000
    max_response_chars: int = 20_000
    explanation_boost: float = DEFAULT_EXPLANATION_BOOST

    def __post_init__(self) -> None:
        object.__setattr__(self, "content_root", self.content_root.resolve())
        object.__setattr__(self, "database_path", self.database_path.resolve())
        integer_limits = {
            "default_limit": self.default_limit,
            "max_results": self.max_results,
            "max_offset": self.max_offset,
            "max_query_chars": self.max_query_chars,
            "default_read_lines": self.default_read_lines,
            "max_read_lines": self.max_read_lines,
            "max_context_lines": self.max_context_lines,
            "max_excerpt_chars": self.max_excerpt_chars,
            "max_response_chars": self.max_response_chars,
        }
        for name, value in integer_limits.items():
            if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                raise ValueError(f"{name} must be a positive integer.")
        if self.default_limit > self.max_results:
            raise ValueError("default_limit cannot exceed max_results.")
        if self.default_read_lines > self.max_read_lines:
            raise ValueError("default_read_lines cannot exceed max_read_lines.")
        if self.explanation_boost <= 0:
            raise ValueError("explanation_boost must be greater than zero.")


@dataclass(frozen=True, slots=True)
class _IndexedFile:
    path: str
    topic: str
    file_type: str
    file_hash: str


@dataclass(frozen=True, slots=True)
class _ExactCandidate:
    indexed_file: _IndexedFile
    match_start_line: int
    match_end_line: int
    excerpt_start_line: int
    excerpt_end_line: int
    excerpt: str


def _require_integer(name: str, value: int, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        qualifier = "a positive integer" if minimum == 1 else f"an integer >= {minimum}"
        raise InvalidRetrievalRequest(f"{name} must be {qualifier}.")
    return value


def _truncate_text(text: str, limit: int) -> tuple[str, bool]:
    if len(text) <= limit:
        return text, False
    if limit == 1:
        return "…", True
    return f"{text[: limit - 1]}…", True


class RetrievalService:
    """Read-only retrieval operations shared by HTTP and future model tools."""

    def __init__(self, config: RetrievalConfig) -> None:
        self.config = config

    def list_topics(self) -> TopicList:
        """Return indexed topics and their source/chunk counts."""

        connection = require_index(self.config.database_path)
        try:
            rows = connection.execute(
                """
                SELECT
                    f.topic,
                    COUNT(DISTINCT f.path) AS file_count,
                    COUNT(c.id) AS chunk_count
                FROM files AS f
                LEFT JOIN chunks AS c ON c.path = f.path
                GROUP BY f.topic
                ORDER BY f.topic
                """
            ).fetchall()
        finally:
            connection.close()
        topics = tuple(
            TopicSummary(
                topic=str(row[0]),
                file_count=int(row[1]),
                chunk_count=int(row[2]),
            )
            for row in rows
        )
        return TopicList(topics=topics, total_topics=len(topics))

    def search_content(
        self,
        query: str,
        *,
        topic: str | None = None,
        limit: int | None = None,
        offset: int = 0,
        max_chars: int | None = None,
    ) -> SearchPage:
        """Return one bounded, optionally topic-scoped lexical search page."""

        checked_query = self._validate_query(query, lexical=True)
        checked_limit, checked_offset = self._validate_page(limit, offset)
        response_budget = self._validate_response_budget(max_chars)
        if topic is not None:
            self._require_topic(topic)

        try:
            candidates = search_index(
                self.config.database_path,
                checked_query,
                topic=topic,
                limit=checked_limit + 1,
                offset=checked_offset,
                explanation_boost=self.config.explanation_boost,
            )
        except ValueError as error:
            raise InvalidRetrievalRequest(str(error)) from error

        has_unreturned_candidate = len(candidates) > checked_limit
        candidates = candidates[:checked_limit]
        results = []
        used_chars = 0
        budget_truncated = False
        for candidate in candidates:
            remaining = response_budget - used_chars
            if remaining < 1:
                budget_truncated = True
                break
            excerpt_limit = min(self.config.max_excerpt_chars, remaining)
            snippet, snippet_truncated = _truncate_text(
                candidate.snippet,
                excerpt_limit,
            )
            results.append(replace(candidate, snippet=snippet))
            used_chars += len(snippet)
            budget_truncated = budget_truncated or snippet_truncated
            if snippet_truncated and remaining <= excerpt_limit:
                break

        has_more = has_unreturned_candidate or len(results) < len(candidates)
        next_offset = checked_offset + len(results) if has_more else None
        return SearchPage(
            query=checked_query,
            topic=topic,
            offset=checked_offset,
            limit=checked_limit,
            results=tuple(results),
            has_more=has_more,
            next_offset=next_offset,
            truncated=budget_truncated,
        )

    def find_exact(
        self,
        query: str,
        *,
        topic: str | None = None,
        case_sensitive: bool = True,
        context_lines: int = 2,
        limit: int | None = None,
        offset: int = 0,
        max_chars: int | None = None,
    ) -> ExactMatchPage:
        """Find literal source text with exact line locations and context."""

        checked_query = self._validate_query(query, lexical=False)
        checked_limit, checked_offset = self._validate_page(limit, offset)
        checked_context = _require_integer(
            "context_lines",
            context_lines,
            minimum=0,
        )
        if checked_context > self.config.max_context_lines:
            raise InvalidRetrievalRequest(
                f"context_lines cannot exceed {self.config.max_context_lines}."
            )
        response_budget = self._validate_response_budget(max_chars)
        if topic is not None:
            self._require_topic(topic)
        if not isinstance(case_sensitive, bool):
            raise InvalidRetrievalRequest("case_sensitive must be a boolean.")

        flags = 0 if case_sensitive else re.IGNORECASE
        normalized_query = checked_query.replace("\r\n", "\n").replace("\r", "\n")
        expression = re.compile(re.escape(normalized_query), flags)
        matched_count = 0
        candidates: list[_ExactCandidate] = []
        for indexed_file in self._indexed_files(topic=topic):
            source_text = self._read_verified_source(indexed_file)
            source_lines = source_text.splitlines(keepends=True)
            normalized_source = source_text.replace("\r\n", "\n").replace("\r", "\n")
            line_starts = [0]
            line_starts.extend(
                match.end() for match in re.finditer(r"\n", normalized_source)
            )
            for match in expression.finditer(normalized_source):
                if matched_count < checked_offset:
                    matched_count += 1
                    continue
                start_line = bisect.bisect_right(line_starts, match.start())
                last_character = max(match.start(), match.end() - 1)
                end_line = bisect.bisect_right(line_starts, last_character)
                excerpt_start = max(1, start_line - checked_context)
                excerpt_end = min(len(source_lines), end_line + checked_context)
                candidates.append(
                    _ExactCandidate(
                        indexed_file=indexed_file,
                        match_start_line=start_line,
                        match_end_line=end_line,
                        excerpt_start_line=excerpt_start,
                        excerpt_end_line=excerpt_end,
                        excerpt="".join(
                            source_lines[excerpt_start - 1 : excerpt_end]
                        ),
                    )
                )
                matched_count += 1
                if len(candidates) >= checked_limit + 1:
                    break
            if len(candidates) >= checked_limit + 1:
                break

        page_candidates = candidates[:checked_limit]
        has_unreturned_candidate = len(candidates) > checked_limit
        results: list[ExactMatch] = []
        used_chars = 0
        budget_truncated = False
        connection = require_index(self.config.database_path)
        try:
            for candidate in page_candidates:
                remaining = response_budget - used_chars
                if remaining < 1:
                    budget_truncated = True
                    break
                excerpt_limit = min(self.config.max_excerpt_chars, remaining)
                excerpt, excerpt_truncated = _truncate_text(
                    candidate.excerpt,
                    excerpt_limit,
                )
                heading, environment = self._chunk_metadata(
                    connection,
                    candidate.indexed_file.path,
                    candidate.match_start_line,
                    candidate.match_end_line,
                )
                results.append(
                    ExactMatch(
                        topic=candidate.indexed_file.topic,
                        path=candidate.indexed_file.path,
                        file_type=candidate.indexed_file.file_type,
                        heading=heading,
                        environment=environment,
                        match_start_line=candidate.match_start_line,
                        match_end_line=candidate.match_end_line,
                        excerpt_start_line=candidate.excerpt_start_line,
                        excerpt_end_line=candidate.excerpt_end_line,
                        excerpt=excerpt,
                        file_hash=candidate.indexed_file.file_hash,
                    )
                )
                used_chars += len(excerpt)
                budget_truncated = budget_truncated or excerpt_truncated
                if excerpt_truncated and remaining <= excerpt_limit:
                    break
        finally:
            connection.close()

        has_more = has_unreturned_candidate or len(results) < len(page_candidates)
        next_offset = checked_offset + len(results) if has_more else None
        return ExactMatchPage(
            query=checked_query,
            topic=topic,
            case_sensitive=case_sensitive,
            offset=checked_offset,
            limit=checked_limit,
            results=tuple(results),
            has_more=has_more,
            next_offset=next_offset,
            truncated=budget_truncated,
        )

    def read_source(
        self,
        path: str,
        *,
        start_line: int = 1,
        end_line: int | None = None,
        max_chars: int | None = None,
    ) -> SourceRead:
        """Read a bounded line range from one indexed, verified source."""

        normalized_path = self._validate_source_path(path)
        checked_start = _require_integer("start_line", start_line, minimum=1)
        if end_line is not None:
            checked_end = _require_integer("end_line", end_line, minimum=1)
            if checked_end < checked_start:
                raise InvalidRetrievalRequest(
                    "end_line cannot be less than start_line."
                )
        else:
            checked_end = None
        response_budget = self._validate_response_budget(max_chars)
        indexed_file = self._indexed_file(normalized_path)
        source_text = self._read_verified_source(indexed_file)
        source_lines = source_text.splitlines(keepends=True)
        total_lines = len(source_lines)
        if total_lines and checked_start > total_lines:
            raise InvalidRetrievalRequest(
                f"start_line {checked_start} exceeds the source's "
                f"{total_lines} line(s)."
            )

        requested_end = (
            checked_end
            if checked_end is not None
            else checked_start + self.config.default_read_lines - 1
        )
        hard_end = checked_start + self.config.max_read_lines - 1
        selected_end = min(requested_end, hard_end, total_lines)
        line_limit_truncated = (
            total_lines > 0
            and selected_end < min(requested_end, total_lines)
        ) or (checked_end is None and selected_end < total_lines)

        selected_parts: list[str] = []
        returned_end: int | None = None
        used_chars = 0
        char_truncated = False
        for line_number in range(checked_start, selected_end + 1):
            line = source_lines[line_number - 1]
            remaining = response_budget - used_chars
            if remaining < 1:
                char_truncated = True
                break
            if len(line) > remaining:
                selected_parts.append(line[:remaining])
                returned_end = line_number
                used_chars += remaining
                char_truncated = True
                break
            selected_parts.append(line)
            returned_end = line_number
            used_chars += len(line)

        truncated = line_limit_truncated or char_truncated
        if returned_end is not None and returned_end < total_lines and (
            truncated or (checked_end is not None and returned_end < checked_end)
        ):
            next_start_line = returned_end + 1
        elif returned_end is None and total_lines:
            next_start_line = checked_start
        else:
            next_start_line = None

        connection = require_index(self.config.database_path)
        try:
            heading, environment = self._chunk_metadata(
                connection,
                indexed_file.path,
                checked_start,
                returned_end or checked_start,
            )
        finally:
            connection.close()
        return SourceRead(
            topic=indexed_file.topic,
            path=indexed_file.path,
            file_type=indexed_file.file_type,
            heading=heading,
            environment=environment,
            start_line=checked_start,
            end_line=returned_end,
            total_lines=total_lines,
            text="".join(selected_parts),
            truncated=truncated,
            next_start_line=next_start_line,
            file_hash=indexed_file.file_hash,
        )

    def _validate_query(self, query: str, *, lexical: bool) -> str:
        if not isinstance(query, str):
            raise InvalidRetrievalRequest("query must be a string.")
        if not query.strip():
            raise InvalidRetrievalRequest("query cannot be empty.")
        if len(query) > self.config.max_query_chars:
            raise InvalidRetrievalRequest(
                f"query cannot exceed {self.config.max_query_chars} characters."
            )
        if lexical and not re.search(r"\w", query, flags=re.UNICODE):
            raise InvalidRetrievalRequest(
                "A lexical search query must contain a word or number."
            )
        return query

    def _validate_page(self, limit: int | None, offset: int) -> tuple[int, int]:
        checked_limit = (
            self.config.default_limit
            if limit is None
            else _require_integer("limit", limit, minimum=1)
        )
        if checked_limit > self.config.max_results:
            raise InvalidRetrievalRequest(
                f"limit cannot exceed {self.config.max_results}."
            )
        checked_offset = _require_integer("offset", offset, minimum=0)
        if checked_offset > self.config.max_offset:
            raise InvalidRetrievalRequest(
                f"offset cannot exceed {self.config.max_offset}."
            )
        return checked_limit, checked_offset

    def _validate_response_budget(self, max_chars: int | None) -> int:
        if max_chars is None:
            return self.config.max_response_chars
        checked = _require_integer("max_chars", max_chars, minimum=1)
        if checked > self.config.max_response_chars:
            raise InvalidRetrievalRequest(
                f"max_chars cannot exceed {self.config.max_response_chars}."
            )
        return checked

    def _require_topic(self, topic: str) -> None:
        if not isinstance(topic, str) or not topic:
            raise InvalidRetrievalRequest("topic must be a non-empty string.")
        connection = require_index(self.config.database_path)
        try:
            exists = connection.execute(
                "SELECT 1 FROM files WHERE topic = ? LIMIT 1",
                (topic,),
            ).fetchone()
        finally:
            connection.close()
        if exists is None:
            raise TopicNotFoundError(f"Topic not found in the CRAIG index: {topic}")

    def _indexed_files(self, *, topic: str | None = None) -> list[_IndexedFile]:
        connection = require_index(self.config.database_path)
        try:
            rows = connection.execute(
                """
                SELECT path, topic, file_type, file_hash
                FROM files
                WHERE (? IS NULL OR topic = ?)
                ORDER BY path
                """,
                (topic, topic),
            ).fetchall()
        finally:
            connection.close()
        return [
            _IndexedFile(
                path=str(row[0]),
                topic=str(row[1]),
                file_type=str(row[2]),
                file_hash=str(row[3]),
            )
            for row in rows
        ]

    def _indexed_file(self, path: str) -> _IndexedFile:
        connection = require_index(self.config.database_path)
        try:
            row = connection.execute(
                """
                SELECT path, topic, file_type, file_hash
                FROM files
                WHERE path = ?
                """,
                (path,),
            ).fetchone()
        finally:
            connection.close()
        if row is None:
            raise SourceNotFoundError(
                f"Source is not present in the CRAIG index: {path}"
            )
        return _IndexedFile(
            path=str(row[0]),
            topic=str(row[1]),
            file_type=str(row[2]),
            file_hash=str(row[3]),
        )

    def _validate_source_path(self, path: str) -> str:
        if not isinstance(path, str) or not path:
            raise InvalidRetrievalRequest("path must be a non-empty string.")
        if "\x00" in path or "\\" in path or ":" in path:
            raise UnsafeSourcePathError(
                "Source paths must be normalized, relative POSIX paths."
            )
        pure_path = PurePosixPath(path)
        if (
            pure_path.is_absolute()
            or any(part in {"", ".", ".."} for part in pure_path.parts)
            or pure_path.as_posix() != path
        ):
            raise UnsafeSourcePathError(
                "Source paths must be normalized, relative POSIX paths."
            )
        return pure_path.as_posix()

    def _resolve_indexed_source(self, path: str) -> Path:
        normalized_path = self._validate_source_path(path)
        candidate = self.config.content_root
        for part in PurePosixPath(normalized_path).parts:
            candidate = candidate / part
            if candidate.is_symlink():
                raise UnsafeSourcePathError(
                    f"Symlinked source paths are not allowed: {normalized_path}"
                )
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(self.config.content_root)
        except (FileNotFoundError, ValueError, OSError) as error:
            raise SourceNotFoundError(
                f"Indexed source is unavailable inside content/: {normalized_path}"
            ) from error
        if not resolved.is_file():
            raise SourceNotFoundError(
                f"Indexed source is not a regular file: {normalized_path}"
            )
        return resolved

    def _read_verified_source(self, indexed_file: _IndexedFile) -> str:
        source_path = self._resolve_indexed_source(indexed_file.path)
        source_bytes = source_path.read_bytes()
        current_hash = hashlib.sha256(source_bytes).hexdigest()
        if current_hash != indexed_file.file_hash:
            raise IndexStaleError(
                f"Source changed after indexing: {indexed_file.path}. "
                "Run `python -m craig index` before retrieving it."
            )
        return source_bytes.decode("utf-8", errors="replace")

    @staticmethod
    def _chunk_metadata(
        connection: sqlite3.Connection,
        path: str,
        start_line: int,
        end_line: int,
    ) -> tuple[str | None, str | None]:
        row = connection.execute(
            """
            SELECT heading, environment
            FROM chunks
            WHERE path = ?
              AND start_line <= ?
              AND end_line >= ?
            ORDER BY
                CASE WHEN environment IS NULL THEN 1 ELSE 0 END,
                (end_line - start_line) ASC,
                start_line ASC
            LIMIT 1
            """,
            (path, start_line, end_line),
        ).fetchone()
        if row is None:
            return None, None
        return (
            str(row[0]) if row[0] is not None else None,
            str(row[1]) if row[1] is not None else None,
        )
