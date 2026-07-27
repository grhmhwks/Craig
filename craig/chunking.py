"""Structure-aware source chunking with exact source line ranges."""

from __future__ import annotations

import ast
import re
from collections.abc import Iterable, Sequence
from pathlib import Path

from .models import Chunk

DEFAULT_MAX_LINES = 80
DEFAULT_OVERLAP_LINES = 10

_MARKDOWN_HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
_TEX_SECTION = re.compile(
    r"\\(?P<kind>section|subsection|subsubsection)\*?"
    r"(?:\[[^\]]*\])?\{(?P<title>.+?)\}"
)
_TEX_ENVIRONMENTS = (
    "definition",
    "theorem",
    "lemma",
    "proposition",
    "corollary",
    "conjecture",
    "proof",
    "example",
    "remark",
)
_TEX_BEGIN = re.compile(
    r"\\begin\s*\{(?P<environment>"
    + "|".join(_TEX_ENVIRONMENTS)
    + r")\}(?:\s*\[(?P<title>[^\]]+)\])?"
)

_CPP_CLASS = re.compile(
    r"\b(?P<kind>class|struct|enum)\s+(?:class\s+)?(?P<name>[A-Za-z_]\w*)"
    r"[^;{}]*\{",
    re.DOTALL,
)
_CPP_FUNCTION = re.compile(
    r"(?P<name>(?:[A-Za-z_~]\w*::)*[A-Za-z_~]\w*)\s*"
    r"\([^;{}]*\)\s*"
    r"(?:(?:const|noexcept|override|final)\b\s*|&{1,2}\s*|"
    r"->\s*[^{}]+)?\{",
    re.DOTALL,
)
_CPP_CONTROL_WORDS = frozenset(
    {"if", "for", "while", "switch", "catch", "return", "sizeof"}
)


def _source_lines(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def _bounded_chunks(
    lines: Sequence[str],
    start_line: int,
    end_line: int,
    *,
    heading: str | None,
    environment: str | None,
    max_lines: int,
    overlap_lines: int,
) -> list[Chunk]:
    """Split an inclusive source range into bounded, overlapping windows."""

    if start_line > end_line or not lines:
        return []
    if max_lines < 1:
        raise ValueError("max_lines must be at least 1")
    if overlap_lines < 0 or overlap_lines >= max_lines:
        raise ValueError("overlap_lines must satisfy 0 <= overlap_lines < max_lines")

    chunks: list[Chunk] = []
    window_start = start_line
    while window_start <= end_line:
        window_end = min(window_start + max_lines - 1, end_line)
        chunk_text = "".join(lines[window_start - 1 : window_end])
        if chunk_text.strip():
            chunks.append(
                Chunk(
                    heading=heading,
                    environment=environment,
                    start_line=window_start,
                    end_line=window_end,
                    text=chunk_text,
                )
            )
        if window_end == end_line:
            break
        window_start = window_end - overlap_lines + 1
    return chunks


def chunk_markdown(
    text: str,
    *,
    max_lines: int = DEFAULT_MAX_LINES,
    overlap_lines: int = DEFAULT_OVERLAP_LINES,
) -> list[Chunk]:
    """Split Markdown at ATX headings, bounding unusually long sections."""

    lines = _source_lines(text)
    if not lines:
        return []

    headings: list[tuple[int, int, str]] = []
    for line_number, line in enumerate(lines, start=1):
        match = _MARKDOWN_HEADING.match(line.rstrip("\r\n"))
        if match:
            headings.append((line_number, len(match.group(1)), match.group(2).strip()))

    if not headings:
        return _bounded_chunks(
            lines,
            1,
            len(lines),
            heading=None,
            environment=None,
            max_lines=max_lines,
            overlap_lines=overlap_lines,
        )

    chunks: list[Chunk] = []
    if headings[0][0] > 1:
        chunks.extend(
            _bounded_chunks(
                lines,
                1,
                headings[0][0] - 1,
                heading=None,
                environment=None,
                max_lines=max_lines,
                overlap_lines=overlap_lines,
            )
        )

    for index, (start_line, level, heading) in enumerate(headings):
        end_line = (
            headings[index + 1][0] - 1 if index + 1 < len(headings) else len(lines)
        )
        chunks.extend(
            _bounded_chunks(
                lines,
                start_line,
                end_line,
                heading=heading,
                environment=f"heading_{level}",
                max_lines=max_lines,
                overlap_lines=overlap_lines,
            )
        )
    return chunks


def _find_tex_environment_end(
    lines: Sequence[str], start_index: int, environment: str
) -> int:
    begin_marker = re.compile(rf"\\begin\s*\{{{re.escape(environment)}\}}")
    end_marker = re.compile(rf"\\end\s*\{{{re.escape(environment)}\}}")
    depth = 0
    for index in range(start_index, len(lines)):
        depth += len(begin_marker.findall(lines[index]))
        depth -= len(end_marker.findall(lines[index]))
        if depth <= 0:
            return index
    return len(lines) - 1


def chunk_tex(
    text: str,
    *,
    max_lines: int = DEFAULT_MAX_LINES,
    overlap_lines: int = DEFAULT_OVERLAP_LINES,
) -> list[Chunk]:
    """Split TeX around section commands and selected theorem-like environments."""

    lines = _source_lines(text)
    if not lines:
        return []

    chunks: list[Chunk] = []
    current_heading: str | None = None
    current_section_kind: str | None = None
    segment_start = 0
    index = 0

    def flush_plain(end_index: int) -> None:
        nonlocal segment_start
        if segment_start <= end_index:
            chunks.extend(
                _bounded_chunks(
                    lines,
                    segment_start + 1,
                    end_index + 1,
                    heading=current_heading,
                    environment=current_section_kind,
                    max_lines=max_lines,
                    overlap_lines=overlap_lines,
                )
            )

    while index < len(lines):
        section_match = _TEX_SECTION.search(lines[index])
        if section_match:
            flush_plain(index - 1)
            current_heading = section_match.group("title").strip()
            current_section_kind = section_match.group("kind")
            segment_start = index
            index += 1
            continue

        environment_match = _TEX_BEGIN.search(lines[index])
        if environment_match:
            flush_plain(index - 1)
            environment = environment_match.group("environment")
            environment_end = _find_tex_environment_end(lines, index, environment)
            environment_heading = environment_match.group("title")
            chunks.extend(
                _bounded_chunks(
                    lines,
                    index + 1,
                    environment_end + 1,
                    heading=(
                        environment_heading.strip()
                        if environment_heading
                        else current_heading
                    ),
                    environment=environment,
                    max_lines=max_lines,
                    overlap_lines=overlap_lines,
                )
            )
            segment_start = environment_end + 1
            index = environment_end + 1
            continue
        index += 1

    flush_plain(len(lines) - 1)
    return chunks


def _node_start_line(node: ast.AST) -> int:
    decorator_lines = [
        decorator.lineno
        for decorator in getattr(node, "decorator_list", [])
        if hasattr(decorator, "lineno")
    ]
    return min([getattr(node, "lineno", 1), *decorator_lines])


def _qualified_python_name(node: ast.AST, parents: dict[ast.AST, ast.AST]) -> str:
    names = [getattr(node, "name", "<anonymous>")]
    parent = parents.get(node)
    while parent is not None and not isinstance(parent, ast.Module):
        if isinstance(
            parent, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            names.append(parent.name)
        parent = parents.get(parent)
    return ".".join(reversed(names))


def _covered_fallback_chunks(
    lines: Sequence[str],
    covered_ranges: Iterable[tuple[int, int]],
    *,
    max_lines: int,
    overlap_lines: int,
) -> list[Chunk]:
    covered = [False] * (len(lines) + 1)
    for start_line, end_line in covered_ranges:
        for line_number in range(max(1, start_line), min(len(lines), end_line) + 1):
            covered[line_number] = True

    chunks: list[Chunk] = []
    line_number = 1
    while line_number <= len(lines):
        if covered[line_number]:
            line_number += 1
            continue
        start_line = line_number
        while line_number <= len(lines) and not covered[line_number]:
            line_number += 1
        chunks.extend(
            _bounded_chunks(
                lines,
                start_line,
                line_number - 1,
                heading=None,
                environment=None,
                max_lines=max_lines,
                overlap_lines=overlap_lines,
            )
        )
    return chunks


def chunk_python(
    text: str,
    *,
    max_lines: int = DEFAULT_MAX_LINES,
    overlap_lines: int = DEFAULT_OVERLAP_LINES,
) -> list[Chunk]:
    """Chunk Python with the standard-library AST, falling back on syntax errors."""

    lines = _source_lines(text)
    if not lines:
        return []
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return _bounded_chunks(
            lines,
            1,
            len(lines),
            heading=None,
            environment=None,
            max_lines=max_lines,
            overlap_lines=overlap_lines,
        )

    parents = {
        child: parent
        for parent in ast.walk(tree)
        for child in ast.iter_child_nodes(parent)
    }
    structural_chunks: list[Chunk] = []
    top_level_ranges: list[tuple[int, int]] = []

    module_docstring_node: ast.Expr | None = None
    if (
        tree.body
        and isinstance(tree.body[0], ast.Expr)
        and isinstance(tree.body[0].value, ast.Constant)
        and isinstance(getattr(tree.body[0].value, "value", None), str)
    ):
        module_docstring_node = tree.body[0]
        doc_end = getattr(module_docstring_node, "end_lineno", module_docstring_node.lineno)
        structural_chunks.extend(
            _bounded_chunks(
                lines,
                module_docstring_node.lineno,
                doc_end,
                heading="Module docstring",
                environment="module_docstring",
                max_lines=max_lines,
                overlap_lines=overlap_lines,
            )
        )
        top_level_ranges.append((module_docstring_node.lineno, doc_end))

    structural_nodes = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    ]
    structural_nodes.sort(
        key=lambda node: (_node_start_line(node), getattr(node, "end_lineno", 0))
    )
    for node in structural_nodes:
        start_line = _node_start_line(node)
        end_line = getattr(node, "end_lineno", getattr(node, "lineno", start_line))
        if isinstance(node, ast.ClassDef):
            environment = "class"
        elif isinstance(parents.get(node), ast.ClassDef):
            environment = (
                "async_method" if isinstance(node, ast.AsyncFunctionDef) else "method"
            )
        else:
            environment = (
                "async_function"
                if isinstance(node, ast.AsyncFunctionDef)
                else "function"
            )
        structural_chunks.extend(
            _bounded_chunks(
                lines,
                start_line,
                end_line,
                heading=_qualified_python_name(node, parents),
                environment=environment,
                max_lines=max_lines,
                overlap_lines=overlap_lines,
            )
        )
        if isinstance(parents.get(node), ast.Module):
            top_level_ranges.append((start_line, end_line))

    structural_chunks.extend(
        _covered_fallback_chunks(
            lines,
            top_level_ranges,
            max_lines=max_lines,
            overlap_lines=overlap_lines,
        )
    )
    return sorted(
        structural_chunks,
        key=lambda chunk: (
            chunk.start_line,
            chunk.end_line,
            chunk.environment or "",
            chunk.heading or "",
        ),
    )


def _matching_brace_line(
    lines: Sequence[str], open_line_index: int, open_column: int
) -> int:
    """Find a closing brace with a deliberately lightweight character count."""

    depth = 0
    for line_index in range(open_line_index, len(lines)):
        start_column = open_column if line_index == open_line_index else 0
        for character in lines[line_index][start_column:]:
            if character == "{":
                depth += 1
            elif character == "}":
                depth -= 1
                if depth == 0:
                    return line_index
    return len(lines) - 1


def _cpp_candidates(lines: Sequence[str]) -> list[tuple[int, int, str, str]]:
    """Recognize common C/C++ definitions without a compiler-grade parser.

    The heuristic joins at most six signature lines, rejects declarations and
    control statements, then uses balanced-brace character counts. It can be
    confused by braces in comments or string literals; bounded fallback chunks
    ensure that unrecognized source remains searchable.
    """

    candidates: list[tuple[int, int, str, str]] = []
    seen: set[tuple[str, str, int]] = set()
    for start_index in range(len(lines)):
        stripped_start = lines[start_index].strip()
        if (
            not stripped_start
            or lines[start_index].lstrip().startswith("#")
            or re.fullmatch(r"(?:public|private|protected)\s*:", stripped_start)
        ):
            continue
        header_parts: list[str] = []
        for header_end in range(start_index, min(start_index + 6, len(lines))):
            header_parts.append(lines[header_end])
            header = "".join(header_parts)
            brace_offset = header.find("{")
            semicolon_offset = header.find(";")
            if semicolon_offset >= 0 and (
                brace_offset < 0 or semicolon_offset < brace_offset
            ):
                break
            if brace_offset < 0:
                continue

            class_match = _CPP_CLASS.search(header)
            function_match = _CPP_FUNCTION.search(header)
            if class_match and (
                function_match is None or class_match.start() <= function_match.start()
            ):
                heading = class_match.group("name")
                environment = class_match.group("kind")
                match = class_match
            elif function_match:
                heading = function_match.group("name")
                if heading.split("::")[-1] in _CPP_CONTROL_WORDS:
                    break
                environment = "function"
                match = function_match
            else:
                break

            match_open_offset = match.end() - 1
            prefix = header[:match_open_offset]
            open_line_delta = prefix.count("\n")
            open_line_index = start_index + open_line_delta
            last_newline = prefix.rfind("\n")
            open_column = (
                match_open_offset
                if last_newline < 0
                else match_open_offset - last_newline - 1
            )
            end_index = _matching_brace_line(lines, open_line_index, open_column)
            key = (environment, heading, end_index)
            if key not in seen:
                candidates.append(
                    (start_index + 1, end_index + 1, heading, environment)
                )
                seen.add(key)
            break
    return candidates


def chunk_cpp(
    text: str,
    *,
    max_lines: int = DEFAULT_MAX_LINES,
    overlap_lines: int = DEFAULT_OVERLAP_LINES,
) -> list[Chunk]:
    """Chunk C/C++ definitions using a small heuristic plus full fallback coverage."""

    lines = _source_lines(text)
    if not lines:
        return []

    candidates = _cpp_candidates(lines)
    chunks: list[Chunk] = []
    for start_line, end_line, heading, environment in candidates:
        chunks.extend(
            _bounded_chunks(
                lines,
                start_line,
                end_line,
                heading=heading,
                environment=environment,
                max_lines=max_lines,
                overlap_lines=overlap_lines,
            )
        )
    chunks.extend(
        _covered_fallback_chunks(
            lines,
            ((start, end) for start, end, _, _ in candidates),
            max_lines=max_lines,
            overlap_lines=overlap_lines,
        )
    )
    return sorted(
        chunks,
        key=lambda chunk: (
            chunk.start_line,
            chunk.end_line,
            chunk.environment or "",
            chunk.heading or "",
        ),
    )


def chunk_source(path: Path, text: str) -> list[Chunk]:
    """Dispatch source text to the chunker for its extension."""

    extension = path.suffix.lower()
    if extension == ".md":
        return chunk_markdown(text)
    if extension == ".tex":
        return chunk_tex(text)
    if extension == ".py":
        return chunk_python(text)
    if extension in {".cpp", ".h", ".hpp"}:
        return chunk_cpp(text)
    raise ValueError(f"Unsupported source type: {extension}")
