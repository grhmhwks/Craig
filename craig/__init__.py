"""CRAIG's local, read-only mathematical research interface."""

from .index import IndexStats, index_repository
from .retrieval import RetrievalConfig, RetrievalService
from .search import SearchResult, search_index

__all__ = [
    "IndexStats",
    "RetrievalConfig",
    "RetrievalService",
    "SearchResult",
    "index_repository",
    "search_index",
]

__version__ = "0.4.0"
