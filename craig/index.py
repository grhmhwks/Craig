"""Incremental, read-only indexing of the mathematical source corpus."""

from __future__ import annotations

import hashlib
from pathlib import Path

from .chunking import chunk_source
from .discovery import (
    discover_source_files,
    relative_source_path,
    topic_for_path,
)
from .models import IndexStats
from .storage import connect_database, initialize_schema

DEFAULT_DATABASE_PATH = Path(".craig") / "index.sqlite3"


def _is_within(path: Path, directory: Path) -> bool:
    try:
        path.resolve().relative_to(directory.resolve())
    except ValueError:
        return False
    return True


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def index_repository(
    content_root: Path,
    database_path: Path,
    *,
    rebuild: bool = False,
) -> IndexStats:
    """Index supported source files without modifying ``content_root``.

    Unchanged files are identified by SHA-256 and skipped. Files no longer
    present in the corpus are removed from the generated index.
    """

    content_root = content_root.resolve()
    database_path = database_path.resolve()
    if _is_within(database_path, content_root):
        raise ValueError("The generated CRAIG database cannot be stored under content/.")

    source_files = discover_source_files(content_root)
    database_path.parent.mkdir(parents=True, exist_ok=True)
    if rebuild and database_path.exists():
        database_path.unlink()

    connection = connect_database(database_path)
    try:
        initialize_schema(connection)
        existing_hashes = dict(
            connection.execute("SELECT path, file_hash FROM files").fetchall()
        )
        discovered_paths = {
            relative_source_path(source_path, content_root)
            for source_path in source_files
        }
        removed_paths = sorted(set(existing_hashes) - discovered_paths)
        indexed_files = 0
        skipped_files = 0
        indexed_chunks = 0

        with connection:
            for relative_path in removed_paths:
                connection.execute("DELETE FROM chunks WHERE path = ?", (relative_path,))
                connection.execute("DELETE FROM files WHERE path = ?", (relative_path,))

            for source_path in source_files:
                relative_path = relative_source_path(source_path, content_root)
                source_bytes = source_path.read_bytes()
                file_hash = _sha256(source_bytes)
                if existing_hashes.get(relative_path) == file_hash:
                    skipped_files += 1
                    continue

                source_text = source_bytes.decode("utf-8", errors="replace")
                topic = topic_for_path(relative_path)
                file_type = source_path.suffix.lower()
                chunks = chunk_source(source_path, source_text)

                connection.execute("DELETE FROM chunks WHERE path = ?", (relative_path,))
                connection.execute(
                    """
                    INSERT INTO files(path, topic, file_type, file_hash)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(path) DO UPDATE SET
                        topic = excluded.topic,
                        file_type = excluded.file_type,
                        file_hash = excluded.file_hash
                    """,
                    (relative_path, topic, file_type, file_hash),
                )
                connection.executemany(
                    """
                    INSERT INTO chunks(
                        topic,
                        path,
                        file_type,
                        heading,
                        environment,
                        start_line,
                        end_line,
                        text,
                        file_hash
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    [
                        (
                            topic,
                            relative_path,
                            file_type,
                            chunk.heading,
                            chunk.environment,
                            chunk.start_line,
                            chunk.end_line,
                            chunk.text,
                            file_hash,
                        )
                        for chunk in chunks
                    ],
                )
                indexed_files += 1
                indexed_chunks += len(chunks)
    finally:
        connection.close()

    return IndexStats(
        discovered_files=len(source_files),
        indexed_files=indexed_files,
        skipped_files=skipped_files,
        removed_files=len(removed_paths),
        indexed_chunks=indexed_chunks,
    )
