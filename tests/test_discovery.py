from __future__ import annotations

from pathlib import Path

from craig.discovery import discover_source_files


def _touch(path: Path, text: str = "source") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_discovers_included_extensions_and_prunes_exclusions(tmp_path: Path) -> None:
    content = tmp_path / "content"
    included = {
        "topic/notes.md",
        "topic/paper.tex",
        "topic/tool.py",
        "topic/fast.cpp",
        "topic/api.h",
        "topic/api.hpp",
    }
    for relative_path in included:
        _touch(content / relative_path)

    for relative_path in {
        "topic/paper.aux",
        "topic/paper.log",
        "topic/paper.pdf",
        "topic/paper.synctex",
        "topic/paper.synctex.gz",
        "topic/archive.gz",
        "topic/program.out",
        "topic/paper.toc",
        "topic/paper.fls",
        "topic/paper.fdb_latexmk",
        "topic/data.json",
        ".git/hidden.md",
        ".craig/hidden.tex",
        "__pycache__/hidden.py",
        "node_modules/hidden.cpp",
        "build/hidden.h",
        "dist/hidden.hpp",
    }:
        _touch(content / relative_path)

    discovered = {
        path.relative_to(content).as_posix()
        for path in discover_source_files(content)
    }
    assert discovered == included
