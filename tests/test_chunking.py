from __future__ import annotations

from craig.chunking import chunk_cpp, chunk_markdown, chunk_python, chunk_tex


def test_source_line_ranges_preserve_exact_source_text() -> None:
    text = "preamble\n# Result\nline three\nline four"

    chunks = chunk_markdown(text)

    assert [(chunk.start_line, chunk.end_line) for chunk in chunks] == [(1, 1), (2, 4)]
    assert chunks[1].text == "# Result\nline three\nline four"
    assert chunks[1].text == "".join(text.splitlines(keepends=True)[1:4])


def test_markdown_splits_at_headings() -> None:
    text = "before\n# First\nalpha\n## Second\nbeta\n"

    chunks = chunk_markdown(text)

    assert [
        (chunk.heading, chunk.environment, chunk.start_line, chunk.end_line)
        for chunk in chunks
    ] == [
        (None, None, 1, 1),
        ("First", "heading_1", 2, 3),
        ("Second", "heading_2", 4, 5),
    ]


def test_tex_splits_sections_theorems_and_proofs() -> None:
    text = (
        "\\section{Introduction}\n"
        "Opening text.\n"
        "\\begin{theorem}[Main result]\n"
        "Every widget is finite.\n"
        "\\end{theorem}\n"
        "\\begin{proof}\n"
        "Count the widgets.\n"
        "\\end{proof}\n"
        "\\subsection{Consequences}\n"
        "A final observation.\n"
    )

    chunks = chunk_tex(text)

    assert [
        (chunk.heading, chunk.environment, chunk.start_line, chunk.end_line)
        for chunk in chunks
    ] == [
        ("Introduction", "section", 1, 2),
        ("Main result", "theorem", 3, 5),
        ("Introduction", "proof", 6, 8),
        ("Consequences", "subsection", 9, 10),
    ]


def test_python_ast_chunks_module_functions_classes_and_methods() -> None:
    text = (
        '"""Module documentation."""\n'
        "\n"
        "class Counter:\n"
        "    def increment(self):\n"
        "        return 1\n"
        "\n"
        "def helper(value):\n"
        "    return value + 1\n"
    )

    chunks = chunk_python(text)
    structures = {
        (chunk.heading, chunk.environment, chunk.start_line, chunk.end_line)
        for chunk in chunks
        if chunk.environment is not None
    }

    assert ("Module docstring", "module_docstring", 1, 1) in structures
    assert ("Counter", "class", 3, 5) in structures
    assert ("Counter.increment", "method", 4, 5) in structures
    assert ("helper", "function", 7, 8) in structures


def test_cpp_heuristic_finds_class_and_function_with_fallback() -> None:
    text = (
        "#include <vector>\n"
        "\n"
        "class Box {\n"
        "public:\n"
        "    int size() const { return 1; }\n"
        "};\n"
        "\n"
        "int add(int left, int right)\n"
        "{\n"
        "    return left + right;\n"
        "}\n"
    )

    chunks = chunk_cpp(text)
    structures = {
        (chunk.heading, chunk.environment, chunk.start_line, chunk.end_line)
        for chunk in chunks
        if chunk.environment is not None
    }

    assert ("Box", "class", 3, 6) in structures
    assert ("size", "function", 5, 5) in structures
    assert ("add", "function", 8, 11) in structures
    assert any("#include <vector>" in chunk.text for chunk in chunks)
