"""Read-only installation diagnostics for local CRAIG deployments."""

from __future__ import annotations

import shutil
import sqlite3
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Literal

from . import __version__
from .chat.providers import provider_from_environment
from .retrieval import RetrievalConfig

CheckStatus = Literal["pass", "warn", "fail"]


@dataclass(frozen=True, slots=True)
class DoctorCheck:
    id: str
    status: CheckStatus
    message: str


def _fts5_available() -> bool:
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE VIRTUAL TABLE check_fts USING fts5(value)")
        return True
    except sqlite3.OperationalError:
        return False
    finally:
        connection.close()


def run_doctor(
    config: RetrievalConfig,
    *,
    frontend_dist: Path | None = None,
) -> dict[str, object]:
    """Return a secret-free diagnostic report without writing any files."""

    resolved_content = config.content_root.resolve()
    resolved_index = config.database_path.resolve()
    resolved_frontend = (
        frontend_dist
        or Path(__file__).resolve().parent.parent / "app" / "frontend" / "dist"
    ).resolve()
    provider = provider_from_environment().metadata
    fts5_available = _fts5_available()
    checks = [
        DoctorCheck(
            id="python",
            status="pass" if sys.version_info >= (3, 10) else "fail",
            message=(
                f"Python {sys.version_info.major}.{sys.version_info.minor}."
                f"{sys.version_info.micro}"
            ),
        ),
        DoctorCheck(
            id="sqlite_fts5",
            status="pass" if fts5_available else "fail",
            message="SQLite FTS5 is available."
            if fts5_available
            else "SQLite FTS5 is unavailable.",
        ),
        DoctorCheck(
            id="content",
            status="pass" if resolved_content.is_dir() else "fail",
            message=(
                f"Protected corpus found at {resolved_content}."
                if resolved_content.is_dir()
                else f"Protected corpus is missing at {resolved_content}."
            ),
        ),
        DoctorCheck(
            id="index",
            status="pass" if resolved_index.is_file() else "warn",
            message=(
                f"Generated index found at {resolved_index}."
                if resolved_index.is_file()
                else "Generated index is missing; run `craig index`."
            ),
        ),
        DoctorCheck(
            id="frontend",
            status="pass" if (resolved_frontend / "index.html").is_file() else "warn",
            message=(
                f"Production frontend found at {resolved_frontend}."
                if (resolved_frontend / "index.html").is_file()
                else "Production frontend is missing; build app/frontend."
            ),
        ),
        DoctorCheck(
            id="node",
            status="pass" if shutil.which("node") else "warn",
            message="Node.js is available."
            if shutil.which("node")
            else "Node.js was not found; it is needed only to build the frontend.",
        ),
        DoctorCheck(
            id="provider",
            status="pass" if provider.configured else "warn",
            message=(
                f"Provider {provider.name}/{provider.model} is configured; "
                f"data destination: {provider.data_destination}."
            ),
        ),
    ]
    status: CheckStatus = (
        "fail"
        if any(check.status == "fail" for check in checks)
        else "warn"
        if any(check.status == "warn" for check in checks)
        else "pass"
    )
    return {
        "schema_version": 1,
        "craig_version": __version__,
        "status": status,
        "checks": [asdict(check) for check in checks],
    }
