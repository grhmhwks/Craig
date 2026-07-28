from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from craig.errors import (
    IndexStaleError,
    InvalidRetrievalRequest,
    SourceNotFoundError,
    TopicNotFoundError,
    UnsafeSourcePathError,
)
from craig.index import index_repository
from craig.retrieval import RetrievalConfig, RetrievalService
from craig.storage import require_index


def _write(content: Path, relative_path: str, text: str) -> Path:
    path = content / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _snapshot(directory: Path) -> dict[str, tuple[bool, int, bytes | None]]:
    return {
        path.relative_to(directory).as_posix(): (
            path.is_dir(),
            path.stat().st_mtime_ns,
            None if path.is_dir() else path.read_bytes(),
        )
        for path in sorted(directory.rglob("*"))
    }


@pytest.fixture
def retrieval(tmp_path: Path) -> tuple[RetrievalService, Path, Path]:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    _write(
        content,
        "alpha/explanation.tex",
        (
            "\\section{Alpha}\n"
            "A transversal argument proves the first claim.\n"
            "\\begin{lemma}[Literal result]\n"
            "The Exact Phrase spans\n"
            "two source lines.\n"
            "\\end{lemma}\n"
        ),
    )
    _write(
        content,
        "beta/notes.md",
        "# Beta\nA different transversal construction appears here.\n",
    )
    _write(content, "README.md", "# Corpus\nRoot-level guidance.\n")
    index_repository(content, database)
    service = RetrievalService(
        RetrievalConfig(
            content_root=content,
            database_path=database,
        )
    )
    return service, content, database


def test_list_topics_returns_file_and_chunk_counts(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, _, _ = retrieval

    result = service.list_topics()

    assert result.total_topics == 3
    summaries = {topic.topic: topic for topic in result.topics}
    assert summaries["alpha"].file_count == 1
    assert summaries["alpha"].chunk_count >= 2
    assert summaries["_root"].file_count == 1


def test_search_content_supports_scope_metadata_and_iteration(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, _, _ = retrieval

    first = service.search_content("transversal", limit=1)
    second = service.search_content(
        "transversal",
        limit=1,
        offset=first.next_offset or 0,
    )
    scoped = service.search_content("transversal", topic="beta")

    assert len(first.results) == 1
    assert first.has_more is True
    assert first.next_offset == 1
    assert second.results[0].rank == 2
    assert second.results[0].path != first.results[0].path
    assert scoped.results[0].topic == "beta"
    assert scoped.results[0].file_type == ".md"
    assert scoped.results[0].environment == "heading_1"
    assert len(scoped.results[0].file_hash or "") == 64


def test_find_exact_handles_multiline_literals_without_chunk_duplicates(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, _, _ = retrieval

    result = service.find_exact(
        "Exact Phrase spans\ntwo",
        context_lines=1,
    )
    insensitive = service.find_exact(
        "exact phrase",
        case_sensitive=False,
        context_lines=0,
    )

    assert len(result.results) == 1
    match = result.results[0]
    assert (match.match_start_line, match.match_end_line) == (4, 5)
    assert match.heading == "Literal result"
    assert match.environment == "lemma"
    assert match.excerpt_start_line == 3
    assert match.excerpt_end_line == 6
    assert len(insensitive.results) == 1


def test_find_exact_supports_bounded_iteration(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, _, _ = retrieval

    first = service.find_exact("transversal", limit=1)
    second = service.find_exact(
        "transversal",
        limit=1,
        offset=first.next_offset or 0,
    )

    assert first.has_more is True
    assert first.next_offset == 1
    assert len(second.results) == 1
    assert second.results[0].path != first.results[0].path
    assert second.has_more is False


def test_read_source_returns_bounded_lines_and_structural_metadata(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, _, database = retrieval
    bounded_service = RetrievalService(
        RetrievalConfig(
            content_root=service.config.content_root,
            database_path=database,
            default_read_lines=2,
            max_read_lines=2,
        )
    )

    result = bounded_service.read_source(
        "alpha/explanation.tex",
        start_line=3,
    )

    assert result.start_line == 3
    assert result.end_line == 4
    assert result.total_lines == 6
    assert result.heading == "Literal result"
    assert result.environment == "lemma"
    assert result.text.startswith("\\begin{lemma}")
    assert result.truncated is True
    assert result.next_start_line == 5


def test_character_and_request_budgets_are_enforced(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, _, _ = retrieval

    search = service.search_content("transversal", max_chars=10)
    exact = service.find_exact("transversal", max_chars=10)
    source = service.read_source("alpha/explanation.tex", max_chars=10)

    assert sum(len(result.snippet) for result in search.results) <= 10
    assert search.truncated is True
    assert sum(len(result.excerpt) for result in exact.results) <= 10
    assert exact.truncated is True
    assert len(source.text) <= 10
    assert source.truncated is True
    with pytest.raises(InvalidRetrievalRequest):
        service.search_content("x", limit=service.config.max_results + 1)
    with pytest.raises(InvalidRetrievalRequest):
        service.find_exact(
            "x" * (service.config.max_query_chars + 1),
        )
    with pytest.raises(InvalidRetrievalRequest):
        service.read_source("alpha/explanation.tex", start_line=0)


@pytest.mark.parametrize(
    "path",
    [
        "../outside.md",
        "/absolute.md",
        "alpha\\explanation.tex",
        "C:/outside.md",
        "./alpha/explanation.tex",
        "alpha//explanation.tex",
    ],
)
def test_read_source_rejects_unsafe_or_unnormalized_paths(
    retrieval: tuple[RetrievalService, Path, Path],
    path: str,
) -> None:
    service, _, _ = retrieval

    with pytest.raises(UnsafeSourcePathError):
        service.read_source(path)


def test_read_source_rejects_files_absent_from_index(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, content, _ = retrieval
    _write(content, "alpha/not-indexed.txt", "not approved")

    with pytest.raises(SourceNotFoundError):
        service.read_source("alpha/not-indexed.txt")


def test_read_source_detects_stale_index(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, content, _ = retrieval
    (content / "alpha" / "explanation.tex").write_text(
        "\\section{Changed}\nChanged after indexing.\n",
        encoding="utf-8",
    )

    with pytest.raises(IndexStaleError):
        service.read_source("alpha/explanation.tex")


def test_read_source_rejects_symlink_after_indexing(
    retrieval: tuple[RetrievalService, Path, Path],
    tmp_path: Path,
) -> None:
    service, content, _ = retrieval
    indexed = content / "alpha" / "explanation.tex"
    outside = tmp_path / "outside.tex"
    outside.write_text("\\section{Outside}\n", encoding="utf-8")
    indexed.unlink()
    try:
        indexed.symlink_to(outside)
    except OSError:
        pytest.skip("Creating symlinks is unavailable in this environment.")

    with pytest.raises(UnsafeSourcePathError):
        service.read_source("alpha/explanation.tex")


def test_unknown_topics_are_reported(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, _, _ = retrieval

    with pytest.raises(TopicNotFoundError):
        service.search_content("transversal", topic="missing")
    with pytest.raises(TopicNotFoundError):
        service.find_exact("transversal", topic="missing")


def test_retrieval_connections_are_sqlite_enforced_read_only(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    _, _, database = retrieval
    connection = require_index(database)
    try:
        assert connection.execute("PRAGMA query_only").fetchone()[0] == 1
        with pytest.raises(sqlite3.OperationalError):
            connection.execute(
                "INSERT INTO index_metadata(key, value) VALUES ('write', 'denied')"
            )
    finally:
        connection.close()


def test_all_retrieval_operations_leave_content_unchanged(
    retrieval: tuple[RetrievalService, Path, Path],
) -> None:
    service, content, _ = retrieval
    before = _snapshot(content)

    service.list_topics()
    service.search_content("transversal")
    service.find_exact("Exact Phrase")
    service.read_source("alpha/explanation.tex", start_line=1, end_line=3)

    assert _snapshot(content) == before
