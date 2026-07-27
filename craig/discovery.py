"""Read-only source-file discovery beneath ``content/``."""

from __future__ import annotations

import os
from pathlib import Path

INCLUDED_EXTENSIONS = frozenset({".md", ".tex", ".py", ".cpp", ".h", ".hpp"})
EXCLUDED_EXTENSIONS = frozenset(
    {
        ".aux",
        ".log",
        ".pdf",
        ".synctex",
        ".synctex.gz",
        ".gz",
        ".out",
        ".toc",
        ".fls",
        ".fdb_latexmk",
    }
)
EXCLUDED_DIRECTORIES = frozenset(
    {".git", ".craig", "__pycache__", "node_modules", "build", "dist"}
)


def _has_excluded_extension(path: Path) -> bool:
    name = path.name.lower()
    return any(name.endswith(extension) for extension in EXCLUDED_EXTENSIONS)


def discover_source_files(content_root: Path) -> list[Path]:
    """Return supported regular files without writing to or following links.

    Directory names and extensions are compared case-insensitively. Symlinks
    are skipped so discovery cannot escape the supplied source root.
    """

    root = content_root.resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Content directory does not exist: {root}")

    discovered: list[Path] = []
    for directory, directory_names, file_names in os.walk(root, followlinks=False):
        directory_names[:] = sorted(
            name
            for name in directory_names
            if name.lower() not in EXCLUDED_DIRECTORIES
            and not (Path(directory) / name).is_symlink()
        )
        for file_name in sorted(file_names):
            path = Path(directory) / file_name
            if (
                path.is_symlink()
                or not path.is_file()
                or _has_excluded_extension(path)
                or path.suffix.lower() not in INCLUDED_EXTENSIONS
            ):
                continue
            discovered.append(path)

    return sorted(discovered, key=lambda path: path.relative_to(root).as_posix())


def relative_source_path(path: Path, content_root: Path) -> str:
    """Return a stable POSIX path relative to ``content/``."""

    return path.resolve().relative_to(content_root.resolve()).as_posix()


def topic_for_path(relative_path: str) -> str:
    """Infer the topic from the first directory below ``content/``.

    Root-level source documents, such as ``content/README.md``, use the
    explicit ``_root`` topic.
    """

    parts = Path(relative_path).parts
    return parts[0] if len(parts) > 1 else "_root"
