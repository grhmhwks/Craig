"""Command-line interface for CRAIG indexing, search, and local API."""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Sequence
from pathlib import Path

from . import __version__
from .config import load_default_environment
from .index import DEFAULT_DATABASE_PATH, index_repository
from .models import SearchResult
from .search import DEFAULT_EXPLANATION_BOOST, DEFAULT_LIMIT, search_index
from .storage import FTS5UnavailableError, IndexNotFoundError


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def _positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def _port(value: str) -> int:
    parsed = int(value)
    if not 1 <= parsed <= 65_535:
        raise argparse.ArgumentTypeError("must be between 1 and 65535")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m craig",
        description=(
            "Index, search, and serve CRAIG's protected mathematical source corpus."
        ),
    )
    parser.add_argument("--version", action="version", version=f"CRAIG {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser(
        "index", help="incrementally index supported files under content/"
    )
    index_parser.add_argument(
        "--rebuild",
        action="store_true",
        help="delete and recreate the generated SQLite index",
    )

    search_parser = subparsers.add_parser(
        "search", help="search indexed passages with SQLite FTS5"
    )
    search_parser.add_argument("query", help="natural-language or mathematical query")
    search_parser.add_argument("--topic", help="restrict results to one topic folder")
    search_parser.add_argument(
        "--limit",
        type=_positive_int,
        default=DEFAULT_LIMIT,
        help=f"maximum number of results (default: {DEFAULT_LIMIT})",
    )
    search_parser.add_argument(
        "--explanation-boost",
        type=_positive_float,
        default=os.environ.get(
            "CRAIG_EXPLANATION_BOOST", str(DEFAULT_EXPLANATION_BOOST)
        ),
        help=(
            "BM25 multiplier for explanation.tex "
            "(default: CRAIG_EXPLANATION_BOOST or 1.5)"
        ),
    )

    serve_parser = subparsers.add_parser(
        "serve",
        help="serve retrieval, conversation, and approved computation locally",
    )
    serve_parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="interface to bind (default: 127.0.0.1)",
    )
    serve_parser.add_argument(
        "--port",
        type=_port,
        default=8000,
        help="port to bind (default: 8000)",
    )

    doctor_parser = subparsers.add_parser(
        "doctor",
        help="run secret-free read-only release diagnostics",
    )
    doctor_parser.add_argument(
        "--json",
        action="store_true",
        help="emit the diagnostic report as JSON",
    )

    evaluate_parser = subparsers.add_parser(
        "evaluate-model",
        help="run the synthetic release evaluation against the configured live model",
    )
    evaluate_parser.add_argument(
        "--tier",
        choices=("strong", "small"),
        required=True,
        help="label this run for like-for-like strong/small comparison",
    )
    evaluate_parser.add_argument(
        "--confirm-live",
        action="store_true",
        help="confirm that model requests may transmit data and incur provider cost",
    )
    evaluate_parser.add_argument(
        "--output",
        type=Path,
        help="optional JSON report path outside content/",
    )
    return parser


def _print_results(results: Sequence[SearchResult]) -> None:
    if not results:
        print("No matching passages.")
        return
    for result in results:
        heading = result.heading or "(none)"
        print(
            f"{result.rank}. score={result.score:.8f} topic={result.topic}\n"
            f"   path: content/{result.path}:{result.start_line}-{result.end_line}\n"
            f"   heading: {heading}\n"
            f"   snippet: {result.snippet}"
        )


def main(argv: Sequence[str] | None = None) -> int:
    try:
        load_default_environment()
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    parser = build_parser()
    arguments = parser.parse_args(argv)
    repository_root = Path.cwd()
    content_root = Path(
        os.environ.get("CRAIG_CONTENT_ROOT", repository_root / "content")
    )
    database_path = Path(
        os.environ.get("CRAIG_INDEX_PATH", repository_root / DEFAULT_DATABASE_PATH)
    )

    try:
        if arguments.command == "index":
            stats = index_repository(
                content_root,
                database_path,
                rebuild=arguments.rebuild,
            )
            print(
                f"Discovered {stats.discovered_files} source file(s); "
                f"indexed {stats.indexed_files}, "
                f"skipped {stats.skipped_files} unchanged, "
                f"removed {stats.removed_files}; "
                f"wrote {stats.indexed_chunks} chunk(s)."
            )
            print(f"Index: {database_path}")
            return 0

        if arguments.command == "search":
            results = search_index(
                database_path,
                arguments.query,
                topic=arguments.topic,
                limit=arguments.limit,
                explanation_boost=arguments.explanation_boost,
            )
            _print_results(results)
            return 0

        if arguments.command == "doctor":
            from .doctor import run_doctor
            from .retrieval import RetrievalConfig

            frontend_dist = Path(
                os.environ.get(
                    "CRAIG_FRONTEND_DIST",
                    repository_root / "app" / "frontend" / "dist",
                )
            )
            report = run_doctor(
                RetrievalConfig(
                    content_root=content_root,
                    database_path=database_path,
                ),
                frontend_dist=frontend_dist,
            )
            if arguments.json:
                print(json.dumps(report, ensure_ascii=False, indent=2))
            else:
                print(f"CRAIG {report['craig_version']} doctor: {report['status']}")
                for check in report["checks"]:
                    print(
                        f"[{str(check['status']).upper():4}] "
                        f"{check['id']}: {check['message']}"
                    )
            return 2 if report["status"] == "fail" else 0

        if arguments.command == "evaluate-model":
            if not arguments.confirm_live:
                raise ValueError(
                    "live evaluation requires --confirm-live because it may "
                    "transmit data and incur provider cost"
                )
            from .chat.providers import provider_from_environment
            from .evaluation import evaluate_provider

            provider = provider_from_environment()
            if not provider.metadata.configured or not provider.metadata.live:
                raise ValueError("configure a live model provider first")
            report = evaluate_provider(provider, tier=arguments.tier)
            rendered = json.dumps(report, ensure_ascii=False, indent=2)
            if arguments.output:
                output = arguments.output.resolve()
                protected = content_root.resolve()
                try:
                    output.relative_to(protected)
                except ValueError:
                    pass
                else:
                    raise ValueError("evaluation output cannot be written under content/")
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(rendered + "\n", encoding="utf-8")
                print(f"Evaluation report: {output}")
            else:
                print(rendered)
            return 0 if report["all_passed"] else 1

        try:
            import uvicorn

            from .api import create_app, default_config
        except ImportError as error:
            raise RuntimeError(
                'The retrieval API dependencies are unavailable. Install with '
                '`python -m pip install -e ".[dev]"`.'
            ) from error
        uvicorn.run(
            create_app(default_config()),
            host=arguments.host,
            port=arguments.port,
        )
        return 0
    except (
        FileNotFoundError,
        FTS5UnavailableError,
        IndexNotFoundError,
        RuntimeError,
        ValueError,
    ) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
