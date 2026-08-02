"""Small, dependency-free environment-file support for local releases."""

from __future__ import annotations

import os
import re
from pathlib import Path

_ENVIRONMENT_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
MAX_ENVIRONMENT_FILE_BYTES = 65_536


def load_environment_file(path: Path, *, override: bool = False) -> tuple[str, ...]:
    """Load a bounded dotenv-style file without expanding or executing values."""

    candidate = path.resolve()
    if not candidate.exists():
        return ()
    if not candidate.is_file():
        raise ValueError(f"environment path is not a file: {candidate}")
    raw = candidate.read_bytes()
    if len(raw) > MAX_ENVIRONMENT_FILE_BYTES:
        raise ValueError(
            f"environment file exceeds {MAX_ENVIRONMENT_FILE_BYTES} bytes"
        )
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("environment file must be UTF-8") from error

    loaded: list[str] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            raise ValueError(
                f"invalid environment assignment on line {line_number}"
            )
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not _ENVIRONMENT_KEY.fullmatch(key):
            raise ValueError(f"invalid environment key on line {line_number}")
        if value[:1] in {"'", '"'}:
            if len(value) < 2 or value[-1] != value[0]:
                raise ValueError(
                    f"unterminated quoted environment value on line {line_number}"
                )
            value = value[1:-1]
        if "\x00" in value:
            raise ValueError(
                f"environment value contains a null byte on line {line_number}"
            )
        if override or key not in os.environ:
            os.environ[key] = value
            loaded.append(key)
    return tuple(loaded)


def load_default_environment() -> tuple[str, ...]:
    """Load CRAIG_ENV_FILE or a repository-local .env with env precedence."""

    configured = os.environ.get("CRAIG_ENV_FILE", "").strip()
    path = Path(configured) if configured else Path.cwd() / ".env"
    return load_environment_file(path)
