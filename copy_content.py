#!/usr/bin/env python3
"""Combine a file or directory tree into one labeled text document."""

from __future__ import annotations

import argparse
import base64
import os
import re
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent
OUTPUT_DIRECTORY = REPOSITORY_ROOT / "copied"


def output_name(raw_source: str, source: Path) -> str:
    """Convert an input such as ``path/to`` to ``path_to.txt``."""

    raw_path = Path(raw_source).expanduser()
    if raw_path.is_absolute():
        try:
            name_source = str(source.relative_to(REPOSITORY_ROOT))
        except ValueError:
            name_source = str(source)
    else:
        name_source = os.path.normpath(raw_source)

    name_source = name_source.lstrip("./\\")
    safe_name = re.sub(r'[<>:"/\\|?*]+', "_", name_source).strip(" ._")
    if not safe_name:
        safe_name = source.name or "copied"
    return f"{safe_name}.txt"


def files_to_copy(source: Path, output_path: Path) -> list[tuple[Path, Path]]:
    """Return ``(display_path, absolute_path)`` pairs in stable order."""

    if source.is_file():
        return [(Path(source.name), source)]

    files: list[tuple[Path, Path]] = []
    for candidate in source.rglob("*"):
        if not candidate.is_file():
            continue
        resolved_candidate = candidate.resolve()
        if resolved_candidate == output_path:
            continue
        files.append((candidate.relative_to(source), resolved_candidate))
    return sorted(files, key=lambda pair: pair[0].as_posix().casefold())


def rendered_content(path: Path) -> str:
    """Read text as UTF-8 and represent other byte sequences as base64."""

    data = path.read_bytes()
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        encoded = base64.b64encode(data).decode("ascii")
        return "[Binary content encoded as base64]\n" + encoded


def copy_to_text(raw_source: str) -> Path:
    source = Path(raw_source).expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(f"Input path does not exist: {raw_source}")
    if not source.is_file() and not source.is_dir():
        raise ValueError(f"Input path is neither a file nor a directory: {raw_source}")

    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    output_path = (OUTPUT_DIRECTORY / output_name(raw_source, source)).resolve()
    entries = files_to_copy(source, output_path)

    with output_path.open("w", encoding="utf-8", newline="\n") as output:
        for index, (display_path, file_path) in enumerate(entries):
            if index:
                output.write("\n")
            output.write(f"===== {display_path.as_posix()} =====\n")
            try:
                content = rendered_content(file_path)
            except OSError as error:
                content = f"[Unable to read file: {error}]"
            output.write(content)
            if not content.endswith("\n"):
                output.write("\n")

    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy a file or every file in a directory tree into one labeled "
            "text document under the repository's copied directory."
        )
    )
    parser.add_argument("path", help="file or directory to copy")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output_path = copy_to_text(args.path)
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"copy.py: {error}", file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
