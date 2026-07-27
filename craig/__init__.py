"""CRAIG's local, read-only repository index."""

from .index import IndexStats, index_repository
from .search import SearchResult, search_index

__all__ = [
    "IndexStats",
    "SearchResult",
    "index_repository",
    "search_index",
]

__version__ = "0.1.0"
