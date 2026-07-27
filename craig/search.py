"""Ranked lexical search over the local SQLite FTS5 index."""

from __future__ import annotations

import re
from pathlib import Path

from .models import SearchResult
from .storage import require_index

DEFAULT_EXPLANATION_BOOST = 1.5
DEFAULT_LIMIT = 5
MAX_QUERY_TERMS = 32


def _fts_query(query: str) -> str:
    """Convert free-form input into a safe, disjunctive FTS5 expression."""

    terms: list[str] = []
    seen: set[str] = set()
    for term in re.findall(r"\w+", query, flags=re.UNICODE):
        normalized = term.casefold()
        if normalized in seen:
            continue
        seen.add(normalized)
        terms.append(term.replace('"', '""'))
        if len(terms) >= MAX_QUERY_TERMS:
            break
    if not terms:
        raise ValueError("Search query must contain at least one word or number.")
    return " OR ".join(f'"{term}"' for term in terms)


def search_index(
    database_path: Path,
    query: str,
    *,
    topic: str | None = None,
    limit: int = DEFAULT_LIMIT,
    explanation_boost: float = DEFAULT_EXPLANATION_BOOST,
) -> list[SearchResult]:
    """Return passages ordered by boosted FTS5 BM25 relevance."""

    if limit < 1:
        raise ValueError("Search limit must be at least 1.")
    if explanation_boost <= 0:
        raise ValueError("explanation_boost must be greater than zero.")

    match_query = _fts_query(query)
    connection = require_index(database_path.resolve())
    try:
        rows = connection.execute(
            """
            SELECT
                c.topic,
                c.path,
                c.heading,
                c.start_line,
                c.end_line,
                snippet(chunks_fts, 0, '[', ']', ' … ', 28) AS snippet,
                (
                    -bm25(chunks_fts, 1.0, 4.0, 0.5, 0.25)
                    * CASE
                        WHEN c.path = 'explanation.tex'
                             OR c.path LIKE '%/explanation.tex'
                        THEN ?
                        ELSE 1.0
                      END
                ) AS score
            FROM chunks_fts
            JOIN chunks AS c ON c.id = chunks_fts.rowid
            WHERE chunks_fts MATCH ?
              AND (? IS NULL OR c.topic = ?)
            ORDER BY score DESC, c.path ASC, c.start_line ASC
            LIMIT ?
            """,
            (explanation_boost, match_query, topic, topic, limit),
        ).fetchall()
    finally:
        connection.close()

    return [
        SearchResult(
            rank=rank,
            score=float(row[6]),
            topic=str(row[0]),
            path=str(row[1]),
            heading=str(row[2]) if row[2] is not None else None,
            start_line=int(row[3]),
            end_line=int(row[4]),
            snippet=re.sub(r"\s+", " ", str(row[5])).strip(),
        )
        for rank, row in enumerate(rows, start=1)
    ]
