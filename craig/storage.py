"""SQLite schema and error handling for the local index."""

from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA_VERSION = 1


class FTS5UnavailableError(RuntimeError):
    """Raised when the active Python SQLite build does not provide FTS5."""


class IndexNotFoundError(RuntimeError):
    """Raised when search is attempted before a valid index exists."""


def connect_database(database_path: Path) -> sqlite3.Connection:
    """Open a SQLite connection with the index's required safety settings."""

    connection = sqlite3.connect(database_path)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def connect_database_readonly(database_path: Path) -> sqlite3.Connection:
    """Open an existing index in SQLite's enforced read-only mode."""

    resolved_path = database_path.resolve()
    try:
        connection = sqlite3.connect(
            f"{resolved_path.as_uri()}?mode=ro",
            uri=True,
        )
    except sqlite3.OperationalError as error:
        raise IndexNotFoundError(
            f"CRAIG index not found at {resolved_path}. "
            "Run `python -m craig index` first."
        ) from error
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA query_only = ON")
    return connection


def initialize_schema(connection: sqlite3.Connection) -> None:
    """Create the metadata tables and FTS5 index."""

    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS index_metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS files (
            path TEXT PRIMARY KEY,
            topic TEXT NOT NULL,
            file_type TEXT NOT NULL,
            file_hash TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY,
            topic TEXT NOT NULL,
            path TEXT NOT NULL,
            file_type TEXT NOT NULL,
            heading TEXT,
            environment TEXT,
            start_line INTEGER NOT NULL CHECK (start_line >= 1),
            end_line INTEGER NOT NULL CHECK (end_line >= start_line),
            text TEXT NOT NULL,
            file_hash TEXT NOT NULL,
            FOREIGN KEY (path) REFERENCES files(path) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS chunks_path_index ON chunks(path);
        CREATE INDEX IF NOT EXISTS chunks_topic_index ON chunks(topic);
        """
    )
    try:
        connection.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
                text,
                heading,
                topic,
                path,
                tokenize = 'unicode61'
            )
            """
        )
    except sqlite3.OperationalError as error:
        if "fts5" in str(error).lower() or "no such module" in str(error).lower():
            raise FTS5UnavailableError(
                "SQLite FTS5 is unavailable in this Python installation. "
                "Install Python with an SQLite build that enables FTS5."
            ) from error
        raise

    connection.executescript(
        """
        CREATE TRIGGER IF NOT EXISTS chunks_after_insert
        AFTER INSERT ON chunks BEGIN
            INSERT INTO chunks_fts(rowid, text, heading, topic, path)
            VALUES (
                new.id,
                new.text,
                COALESCE(new.heading, ''),
                new.topic,
                new.path
            );
        END;

        CREATE TRIGGER IF NOT EXISTS chunks_after_delete
        AFTER DELETE ON chunks BEGIN
            DELETE FROM chunks_fts WHERE rowid = old.id;
        END;

        CREATE TRIGGER IF NOT EXISTS chunks_after_update
        AFTER UPDATE ON chunks BEGIN
            DELETE FROM chunks_fts WHERE rowid = old.id;
            INSERT INTO chunks_fts(rowid, text, heading, topic, path)
            VALUES (
                new.id,
                new.text,
                COALESCE(new.heading, ''),
                new.topic,
                new.path
            );
        END;
        """
    )
    stored_version = connection.execute(
        "SELECT value FROM index_metadata WHERE key = 'schema_version'"
    ).fetchone()
    if stored_version is not None and int(stored_version[0]) != SCHEMA_VERSION:
        raise RuntimeError(
            "The CRAIG index schema is incompatible with this version. "
            "Run `python -m craig index --rebuild`."
        )
    connection.execute(
        """
        INSERT OR IGNORE INTO index_metadata(key, value)
        VALUES ('schema_version', ?)
        """,
        (str(SCHEMA_VERSION),),
    )


def require_index(database_path: Path) -> sqlite3.Connection:
    """Open and validate an existing index without granting write access."""

    if not database_path.is_file():
        raise IndexNotFoundError(
            f"CRAIG index not found at {database_path}. "
            "Run `python -m craig index` first."
        )
    connection = connect_database_readonly(database_path)
    try:
        connection.execute("SELECT rowid FROM chunks_fts LIMIT 0")
        connection.execute("SELECT id FROM chunks LIMIT 0")
        stored_version = connection.execute(
            "SELECT value FROM index_metadata WHERE key = 'schema_version'"
        ).fetchone()
        if stored_version is None or int(stored_version[0]) != SCHEMA_VERSION:
            connection.close()
            raise IndexNotFoundError(
                f"{database_path} uses an incompatible CRAIG index schema. "
                "Run `python -m craig index --rebuild`."
            )
    except sqlite3.OperationalError as error:
        connection.close()
        if "fts5" in str(error).lower() or "no such module" in str(error).lower():
            raise FTS5UnavailableError(
                "SQLite FTS5 is unavailable in this Python installation. "
                "Install Python with an SQLite build that enables FTS5."
            ) from error
        raise IndexNotFoundError(
            f"{database_path} is not a valid CRAIG index. "
            "Run `python -m craig index --rebuild`."
        ) from error
    except (TypeError, ValueError):
        connection.close()
        raise IndexNotFoundError(
            f"{database_path} has invalid CRAIG index metadata. "
            "Run `python -m craig index --rebuild`."
        ) from None
    return connection
