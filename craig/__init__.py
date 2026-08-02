"""CRAIG's local, read-only mathematical research interface."""

__all__ = [
    "IndexStats",
    "RetrievalConfig",
    "RetrievalService",
    "SearchResult",
    "index_repository",
    "search_index",
]

__version__ = "1.0.0"


def __getattr__(name: str):
    """Load public convenience exports lazily for isolated worker startup."""

    if name in {"IndexStats", "index_repository"}:
        from .index import IndexStats, index_repository

        return {"IndexStats": IndexStats, "index_repository": index_repository}[name]
    if name in {"RetrievalConfig", "RetrievalService"}:
        from .retrieval import RetrievalConfig, RetrievalService

        return {
            "RetrievalConfig": RetrievalConfig,
            "RetrievalService": RetrievalService,
        }[name]
    if name in {"SearchResult", "search_index"}:
        from .search import SearchResult, search_index

        return {"SearchResult": SearchResult, "search_index": search_index}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
