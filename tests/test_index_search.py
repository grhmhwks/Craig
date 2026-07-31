from __future__ import annotations

import sqlite3
from contextlib import closing
from pathlib import Path

from craig.index import index_repository
from craig.search import search_index


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


def test_topic_scoped_search(tmp_path: Path) -> None:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    _write(
        content,
        "alpha/explanation.tex",
        "\\section{Alpha}\nA transversal argument proves the claim.\n",
    )
    _write(
        content,
        "beta/notes.md",
        "# Beta\nA different transversal construction appears here.\n",
    )
    index_repository(content, database)

    results = search_index(database, "transversal construction argument", topic="beta")

    assert results
    assert {result.topic for result in results} == {"beta"}
    assert all(result.path.startswith("beta/") for result in results)


def test_explanation_tex_receives_configurable_ranking_preference(
    tmp_path: Path,
) -> None:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    source = "\\section{Shared}\nThe crystalline bijection preserves weight.\n"
    _write(content, "topic/explanation.tex", source)
    _write(content, "topic/notes.tex", source)
    index_repository(content, database)

    boosted = search_index(
        database,
        "crystalline bijection",
        limit=2,
        explanation_boost=2.0,
    )

    assert [result.path for result in boosted] == [
        "topic/explanation.tex",
        "topic/notes.tex",
    ]
    assert boosted[0].score > boosted[1].score


def test_incremental_indexing_skips_unchanged_files(tmp_path: Path) -> None:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    source = _write(content, "topic/notes.md", "# First\ninitial text\n")

    first = index_repository(content, database)
    second = index_repository(content, database)
    source.write_text("# First\nchanged text\n", encoding="utf-8")
    third = index_repository(content, database)

    assert (first.indexed_files, first.skipped_files) == (1, 0)
    assert (second.indexed_files, second.skipped_files) == (0, 1)
    assert (third.indexed_files, third.skipped_files) == (1, 0)
    with closing(sqlite3.connect(database)) as connection:
        assert connection.execute("SELECT COUNT(*) FROM files").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] == 1
        stored_text = connection.execute("SELECT text FROM chunks").fetchone()[0]
    assert "changed text" in stored_text


def test_index_stores_required_chunk_metadata(tmp_path: Path) -> None:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    _write(
        content,
        "topic/explanation.tex",
        "\\section{Setup}\n\\begin{lemma}\nA useful fact.\n\\end{lemma}\n",
    )
    index_repository(content, database)

    with closing(sqlite3.connect(database)) as connection:
        row = connection.execute(
            """
            SELECT
                topic,
                path,
                file_type,
                heading,
                environment,
                start_line,
                end_line,
                text,
                file_hash
            FROM chunks
            WHERE environment = 'lemma'
            """
        ).fetchone()

    assert row is not None
    assert row[:7] == (
        "topic",
        "topic/explanation.tex",
        ".tex",
        "Setup",
        "lemma",
        2,
        4,
    )
    assert "A useful fact." in row[7]
    assert len(row[8]) == 64


def test_indexing_does_not_write_under_content(tmp_path: Path) -> None:
    content = tmp_path / "content"
    database = tmp_path / "generated" / "index.sqlite3"
    _write(content, "topic/explanation.tex", "\\section{Safe}\nRead only.\n")
    _write(content, "topic/code.py", "def value():\n    return 7\n")
    before = _snapshot(content)

    index_repository(content, database)

    assert _snapshot(content) == before
    assert database.is_file()
    assert not database.is_relative_to(content)


def test_database_path_under_content_is_rejected(tmp_path: Path) -> None:
    content = tmp_path / "content"
    _write(content, "topic/notes.md", "# Protected\n")

    try:
        index_repository(content, content / ".craig" / "index.sqlite3")
    except ValueError as error:
        assert "cannot be stored under content" in str(error)
    else:
        raise AssertionError("an index path under content/ must be rejected")
