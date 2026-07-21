# Combinatorics Repository Packet

Generated from `Combinatorics/`. This packet lists the current file structure and expands the contents of text/source files. Binary artifacts are listed with size and SHA-256 instead of embedded bytes so the packet remains usable in chat.

## File Structure

```text
bibliography.bib
build_site.py
docs/index.html
docs/items/dyck_skeleton_string_decompositions/code/README.md
docs/items/dyck_skeleton_string_decompositions/explanation.tex
docs/items/dyck_skeleton_string_decompositions/index.html
docs/items/dyck_skeleton_tableau_formulas/code/check_rational_two_column_formula.py
docs/items/dyck_skeleton_tableau_formulas/code/README.md
docs/items/dyck_skeleton_tableau_formulas/explanation.pdf
docs/items/dyck_skeleton_tableau_formulas/explanation.tex
docs/items/dyck_skeleton_tableau_formulas/index.html
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/01_core_dyck_sequence_routines.py
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/02_make_strings.py
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/01_residual_finite_check.py
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/02_residual_successful_output.txt
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/03_east7_west7_seven_window_checker.py
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/04_east7_west7_successful_output.txt
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/05_lemma_525_limited_nonzero_checker.py
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/06_lemma_525_limited_nonzero_successful_output.txt
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/07_lemma_525_prefix_checker.py
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/08_lemma_525_prefix_successful_output.txt
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/README.md
docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/run_appendix_listing.py
docs/items/dyck_symmetric_computer_assisted_proofs_2026/explanation.pdf
docs/items/dyck_symmetric_computer_assisted_proofs_2026/explanation.tex
docs/items/dyck_symmetric_computer_assisted_proofs_2026/index.html
docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.1.nbc
docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.nbi
docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.1.nbc
docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.nbi
docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.1.nbc
docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.nbi
docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization.cpython-314.pyc
docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.1.nbc
docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.2.nbc
docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.nbi
docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.1.nbc
docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.nbi
docs/items/dyck_symmetric_functions/code/check_rational_dyck_generalization.py
docs/items/dyck_symmetric_functions/code/classical_insertion_demo.py
docs/items/dyck_symmetric_functions/code/paper_algorithms/__init__.py
docs/items/dyck_symmetric_functions/code/paper_algorithms/rational_dyck.py
docs/items/dyck_symmetric_functions/code/paper_algorithms/row_insertion.py
docs/items/dyck_symmetric_functions/code/paper_algorithms/ssyt.py
docs/items/dyck_symmetric_functions/code/paper_algorithms/tableau_insertion.py
docs/items/dyck_symmetric_functions/code/random_rational_dyck_checks.py
docs/items/dyck_symmetric_functions/code/README.md
docs/items/dyck_symmetric_functions/explanation.pdf
docs/items/dyck_symmetric_functions/explanation.tex
docs/items/dyck_symmetric_functions/index.html
docs/items/qt_catalan_computer_assisted_proofs_2024/code/README.md
docs/items/qt_catalan_computer_assisted_proofs_2024/explanation.tex
docs/items/qt_catalan_computer_assisted_proofs_2024/index.html
docs/items/qt_catalan_middle_coefficients/code/README.md
docs/items/qt_catalan_middle_coefficients/explanation.tex
docs/items/qt_catalan_middle_coefficients/index.html
docs/items/rational_qt_catalan_formula/code/README.md
docs/items/rational_qt_catalan_formula/explanation.tex
docs/items/rational_qt_catalan_formula/index.html
docs/items/shifted_littlewood_richardson/code/README.md
docs/items/shifted_littlewood_richardson/explanation.tex
docs/items/shifted_littlewood_richardson/index.html
docs/items/type_c_grothendieck/code/README.md
docs/items/type_c_grothendieck/explanation.tex
docs/items/type_c_grothendieck/index.html
docs/static/styles.css
items/dyck_skeleton_string_decompositions/assets/.gitkeep
items/dyck_skeleton_string_decompositions/code/__pycache__/check_nrcm_lower_half.cpython-314.pyc
items/dyck_skeleton_string_decompositions/code/__pycache__/check_r1mod_skeleton_strings.cpython-314.pyc
items/dyck_skeleton_string_decompositions/code/check_nrcm_domain.py
items/dyck_skeleton_string_decompositions/code/check_nrcm_lower_half.py
items/dyck_skeleton_string_decompositions/code/check_r1mod_skeleton_strings.py
items/dyck_skeleton_string_decompositions/code/README.md
items/dyck_skeleton_string_decompositions/code/run_official_r1mod_checks.py
items/dyck_skeleton_string_decompositions/explanation.aux
items/dyck_skeleton_string_decompositions/explanation.log
items/dyck_skeleton_string_decompositions/explanation.pdf
items/dyck_skeleton_string_decompositions/explanation.synctex.gz
items/dyck_skeleton_string_decompositions/explanation.tex
items/dyck_skeleton_string_decompositions/html/body.html
items/dyck_skeleton_string_decompositions/item.yaml
items/dyck_skeleton_string_decompositions/README.md
items/dyck_skeleton_string_decompositions/WRITING_PACKET.md
items/dyck_skeleton_tableau_formulas/assets/.gitkeep
items/dyck_skeleton_tableau_formulas/code/check_rational_two_column_formula.py
items/dyck_skeleton_tableau_formulas/code/README.md
items/dyck_skeleton_tableau_formulas/explanation.tex
items/dyck_skeleton_tableau_formulas/html/body.html
items/dyck_skeleton_tableau_formulas/item.yaml
items/dyck_skeleton_tableau_formulas/README.md
items/dyck_symmetric_computer_assisted_proofs_2026/assets/.gitkeep
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/01_core_dyck_sequence_routines.py
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/02_make_strings.py
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/01_residual_finite_check.py
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/02_residual_successful_output.txt
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/03_east7_west7_seven_window_checker.py
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/04_east7_west7_successful_output.txt
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/05_lemma_525_limited_nonzero_checker.py
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/06_lemma_525_limited_nonzero_successful_output.txt
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/07_lemma_525_prefix_checker.py
items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/08_lemma_525_prefix_successful_output.txt
items/dyck_symmetric_computer_assisted_proofs_2026/code/README.md
items/dyck_symmetric_computer_assisted_proofs_2026/code/run_appendix_listing.py
items/dyck_symmetric_computer_assisted_proofs_2026/COMPLETION_REVIEW.md
items/dyck_symmetric_computer_assisted_proofs_2026/explanation.pdf
items/dyck_symmetric_computer_assisted_proofs_2026/explanation.tex
items/dyck_symmetric_computer_assisted_proofs_2026/html/body.html
items/dyck_symmetric_computer_assisted_proofs_2026/item.yaml
items/dyck_symmetric_computer_assisted_proofs_2026/README.md
items/dyck_symmetric_functions/assets/.gitkeep
items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.1.nbc
items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.nbi
items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.1.nbc
items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.nbi
items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.1.nbc
items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.nbi
items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization.cpython-314.pyc
items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.1.nbc
items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.2.nbc
items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.nbi
items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.1.nbc
items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.nbi
items/dyck_symmetric_functions/code/check_rational_dyck_generalization.py
items/dyck_symmetric_functions/code/classical_insertion_demo.py
items/dyck_symmetric_functions/code/paper_algorithms/__init__.py
items/dyck_symmetric_functions/code/paper_algorithms/rational_dyck.py
items/dyck_symmetric_functions/code/paper_algorithms/row_insertion.py
items/dyck_symmetric_functions/code/paper_algorithms/ssyt.py
items/dyck_symmetric_functions/code/paper_algorithms/tableau_insertion.py
items/dyck_symmetric_functions/code/random_rational_dyck_checks.py
items/dyck_symmetric_functions/code/README.md
items/dyck_symmetric_functions/explanation.aux
items/dyck_symmetric_functions/explanation.log
items/dyck_symmetric_functions/explanation.pdf
items/dyck_symmetric_functions/explanation.synctex.gz
items/dyck_symmetric_functions/explanation.tex
items/dyck_symmetric_functions/html/body.html
items/dyck_symmetric_functions/item.yaml
items/dyck_symmetric_functions/README.md
items/qt_catalan_computer_assisted_proofs_2024/assets/.gitkeep
items/qt_catalan_computer_assisted_proofs_2024/code/qt_assisted_2024.py
items/qt_catalan_computer_assisted_proofs_2024/code/qt_assisted_2024_expected_output.txt
items/qt_catalan_computer_assisted_proofs_2024/code/README.md
items/qt_catalan_computer_assisted_proofs_2024/explanation.tex
items/qt_catalan_computer_assisted_proofs_2024/html/body.html
items/qt_catalan_computer_assisted_proofs_2024/item.yaml
items/qt_catalan_computer_assisted_proofs_2024/README.md
items/qt_catalan_middle_coefficients/assets/.gitkeep
items/qt_catalan_middle_coefficients/code/check_flat_middle_coefficients.py
items/qt_catalan_middle_coefficients/code/flat_middle_coefficients_default_summary.txt
items/qt_catalan_middle_coefficients/code/README.md
items/qt_catalan_middle_coefficients/explanation.aux
items/qt_catalan_middle_coefficients/explanation.log
items/qt_catalan_middle_coefficients/explanation.pdf
items/qt_catalan_middle_coefficients/explanation.synctex.gz
items/qt_catalan_middle_coefficients/explanation.tex
items/qt_catalan_middle_coefficients/html/body.html
items/qt_catalan_middle_coefficients/item.yaml
items/qt_catalan_middle_coefficients/README.md
items/rational_qt_catalan_formula/assets/.gitkeep
items/rational_qt_catalan_formula/code/check_rational_qt_catalan_formula.py
items/rational_qt_catalan_formula/code/rational_qt_catalan_expected_output.txt
items/rational_qt_catalan_formula/code/README.md
items/rational_qt_catalan_formula/explanation.aux
items/rational_qt_catalan_formula/explanation.log
items/rational_qt_catalan_formula/explanation.pdf
items/rational_qt_catalan_formula/explanation.synctex.gz
items/rational_qt_catalan_formula/explanation.tex
items/rational_qt_catalan_formula/html/body.html
items/rational_qt_catalan_formula/item.yaml
items/rational_qt_catalan_formula/README.md
items/README.md
items/shifted_littlewood_richardson/assets/.gitkeep
items/shifted_littlewood_richardson/code/check_shifted_lr.py
items/shifted_littlewood_richardson/code/README.md
items/shifted_littlewood_richardson/code/shifted_lr_default_summary.txt
items/shifted_littlewood_richardson/explanation.tex
items/shifted_littlewood_richardson/html/body.html
items/shifted_littlewood_richardson/item.yaml
items/shifted_littlewood_richardson/README.md
items/type_c_grothendieck/assets/.gitkeep
items/type_c_grothendieck/code/check_type_c_grothendieck.py
items/type_c_grothendieck/code/README.md
items/type_c_grothendieck/code/type_c_grothendieck_default_summary.txt
items/type_c_grothendieck/explanation.tex
items/type_c_grothendieck/html/body.html
items/type_c_grothendieck/item.yaml
items/type_c_grothendieck/README.md
README.md
requirements.txt
shared/html/.gitkeep
shared/latex/.gitkeep
shared/python/.gitkeep
shared/README.md
shared/templates/code_README.md
shared/templates/item_README.md
site/README.md
site/static/styles.css
site/templates/base.html
site/templates/home.html
site/templates/item.html
target_contents.md
target_structure.md
```

## File Contents

### `bibliography.bib`

```bibtex
% BibTeX entries used by item LaTeX files and the generated site.
% This file is not intended to be a complete publication archive.
```

### `build_site.py`

```python
"""Build the static HTML site into docs/.

This intentionally starts small and dependency-free. It reads item metadata
from items/*/item.yaml when present, injects item html/body.html content when
available, copies linked item files into docs/items/<slug>/, and writes a
static site suitable for GitHub Pages.
"""

from __future__ import annotations

import html
import os
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ITEMS_DIR = ROOT / "items"
SITE_DIR = ROOT / "site"
DOCS_DIR = ROOT / "docs"


def read_text(path: Path, default: str = "") -> str:
    return path.read_text(encoding="utf-8") if path.exists() else default


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def parse_simple_yaml(path: Path) -> dict[str, object]:
    """Parse the small YAML subset expected in item.yaml.

    Supported forms:
      key: value
      key:
        - value

    This is enough for placeholder metadata. If the metadata grows more
    complex, replace this with PyYAML.
    """

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in read_text(path).splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_list_key:
            value = stripped[2:].strip()
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(value)
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", stripped)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if value:
            data[key] = value.strip("\"'")
            current_list_key = None
        else:
            data[key] = []
            current_list_key = key
    return data


def load_template(name: str, fallback: str) -> str:
    return read_text(SITE_DIR / "templates" / name, fallback)


def render(template: str, **values: str) -> str:
    for key, value in values.items():
        template = template.replace("{{ " + key + " }}", value)
    return template


def copy_if_exists(source: Path, destination: Path) -> str | None:
    if not source.exists():
        return None
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return destination.name


def discover_items() -> list[dict[str, object]]:
    if not ITEMS_DIR.exists():
        return []

    items: list[dict[str, object]] = []
    for item_dir in sorted(path for path in ITEMS_DIR.iterdir() if path.is_dir()):
        metadata_path = item_dir / "item.yaml"
        if not metadata_path.exists():
            continue
        metadata = parse_simple_yaml(metadata_path)
        slug = str(metadata.get("slug") or item_dir.name)
        title = str(metadata.get("title") or slug.replace("_", " ").title())
        metadata["slug"] = slug
        metadata["title"] = title
        metadata["item_dir"] = item_dir
        items.append(metadata)
    return items


def build_item(metadata: dict[str, object], base_template: str, item_template: str) -> str:
    item_dir = Path(metadata["item_dir"])
    slug = str(metadata["slug"])
    title = str(metadata["title"])
    out_dir = DOCS_DIR / "items" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    copied_files: list[tuple[str, str]] = []
    for source_name, label in (
        ("explanation.pdf", "View PDF"),
        ("explanation.tex", "Download LaTeX"),
    ):
        copied_name = copy_if_exists(item_dir / source_name, out_dir / source_name)
        if copied_name:
            copied_files.append((label, copied_name))

    code_dir = item_dir / "code"
    if code_dir.exists():
        destination = out_dir / "code"
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(code_dir, destination)
        copied_files.append(("View code", "code/"))

    body = read_text(item_dir / "html" / "body.html", "<p>Educational content is planned.</p>")
    status_summary = html.escape(
        str(metadata.get("status_summary") or metadata.get("status") or "Status to be recorded.")
    )
    download_links = "\n".join(
        f'<li><a href="{html.escape(href)}">{html.escape(label)}</a></li>'
        for label, href in copied_files
    )
    if not download_links:
        download_links = "<li>Downloads are planned.</li>"

    item_html = render(
        item_template,
        title=html.escape(title),
        status_summary=status_summary,
        downloads=download_links,
        body=body,
    )
    page = render(base_template, title=html.escape(title), content=item_html)
    write_text(out_dir / "index.html", page)
    return f'<li><a href="items/{html.escape(slug)}/">{html.escape(title)}</a></li>'


def copy_static() -> None:
    static_source = SITE_DIR / "static"
    static_dest = DOCS_DIR / "static"
    if static_dest.exists():
        shutil.rmtree(static_dest)
    if static_source.exists():
        shutil.copytree(static_source, static_dest)


def build() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    copy_static()

    base_template = load_template(
        "base.html",
        "<!doctype html><html><head><title>{{ title }}</title></head><body>{{ content }}</body></html>",
    )
    home_template = load_template("home.html", "<h1>Combinatorics</h1><ul>{{ items }}</ul>")
    item_template = load_template("item.html", "<h1>{{ title }}</h1>{{ body }}")

    item_links = [
        build_item(metadata, base_template, item_template)
        for metadata in discover_items()
    ]
    if not item_links:
        item_links = ["<li>Curated items are planned.</li>"]

    home = render(home_template, items="\n".join(item_links))
    write_text(DOCS_DIR / "index.html", render(base_template, title="Combinatorics", content=home))


if __name__ == "__main__":
    build()
    print(f"Built site at {os.fspath(DOCS_DIR)}")
```

### `docs/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Combinatorics</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<section class="page-heading">
  <h1>Combinatorics</h1>
  <p>Curated mathematical results, conjectures, computations, examples, and exposition.</p>
</section>

<section>
  <h2>Items</h2>
  <ul class="item-list">
<li><a href="items/dyck_skeleton_string_decompositions/">Dyck Skeleton String Decompositions</a></li>
<li><a href="items/dyck_skeleton_tableau_formulas/">Dyck Skeleton Tableau Formulas</a></li>
<li><a href="items/dyck_symmetric_computer_assisted_proofs_2026/">Dyck Symmetric Computer-Assisted Proofs 2026</a></li>
<li><a href="items/dyck_symmetric_functions/">Dyck Symmetric Functions</a></li>
<li><a href="items/qt_catalan_computer_assisted_proofs_2024/">qt-Catalan Computer-Assisted Proofs 2024</a></li>
<li><a href="items/qt_catalan_middle_coefficients/">qt-Catalan Middle Coefficients</a></li>
<li><a href="items/rational_qt_catalan_formula/">Rational qt-Catalan Formula</a></li>
<li><a href="items/shifted_littlewood_richardson/">Shifted Littlewood-Richardson</a></li>
<li><a href="items/type_c_grothendieck/">Type C Grothendieck</a></li>
  </ul>
</section>

  </main>
</body>
</html>
```

### `docs/items/dyck_skeleton_string_decompositions/code/README.md`

```markdown
# Code

Placeholder for code supporting skeleton-string decompositions and rational
cyclic-map diagnostics.
```

### `docs/items/dyck_skeleton_string_decompositions/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{Dyck Skeleton String Decompositions}
\author{}
\date{}

\begin{document}
\maketitle

\section{Placeholder}

This file will state the classical skeleton-string decomposition, the
\(r\equiv 1 \pmod s\) conjectural analogue, and the naive rational cyclic map
status.

\end{document}
```

### `docs/items/dyck_skeleton_string_decompositions/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dyck Skeleton String Decompositions</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>Dyck Skeleton String Decompositions</h1>
    <p>Classical skeleton strings are proved in the 2026 preprint in the low-deficit range; r == 1 mod s strings are conjectural; NRCM material is not human verified.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This educational section will explain skeleton strings, East/West maps, the r == 1 mod s analogue, and the naive rational cyclic map.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/dyck_skeleton_tableau_formulas/code/check_rational_two_column_formula.py`

```python
"""Finite checks for the rational two-column skeleton/tableau formula.

Inputs are rational step values ``t`` and length values ``n``.  For each
requested pair with ``t != 1``, the checker compares:

* direct normalized rational Dyck paths of length ``n``;
* the Type 4 skeleton/tableau formula side, summed over rational
  ``m``-skeletons and at-most-two-column rational Dyck tableaux.

Both sides are grouped by ``(area, dinv)`` before comparison.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from math import comb
from typing import Iterable, Sequence


Word = tuple[int, ...]
Shape = tuple[int, ...]
Tableau = tuple[tuple[int, ...], ...]
PairTable = list[list[int]]


@dataclass(frozen=True, slots=True)
class SequenceData:
    sequence: Word
    area: int
    dinv: int
    endpoint: int
    max_value: int
    is_skeleton: bool


@dataclass(frozen=True, slots=True)
class TableauData:
    row_word: Word
    area: int
    dinv: int


@dataclass(frozen=True, slots=True)
class AggregatedTableauData:
    counts: Word
    area: int
    dinv: int
    multiplicity: int


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def pair_dinv_python(left: int, right: int, step: int) -> int:
    if left <= right:
        contribution = left + step - right
    else:
        contribution = right + 1 + step - left
    if contribution > 0:
        return contribution
    return 0


def rational_dinv_python(sequence: Word, step: int) -> int:
    total = 0
    for left_index in range(len(sequence)):
        left = sequence[left_index]
        for right in sequence[left_index + 1 :]:
            if left <= right:
                contribution = left + step - right
            else:
                contribution = right + 1 + step - left
            if contribution > 0:
                total += contribution
    return total


def has_nonfinal_rational_extractable_python(sequence: Word, step: int) -> bool:
    for index, value in enumerate(sequence[:-1]):
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = 0
        for prior in sequence[:index]:
            if lower <= prior <= value - 1:
                prior_window_count += 1
                if prior_window_count > 1:
                    break
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(sequence) and sequence[index + 1] > sequence[index - 1] + step:
            continue
        return True
    return False


def value_counts(values: Word) -> Word:
    if not values:
        return ()
    counts = [0] * (max(values) + 1)
    for value in values:
        counts[value] += 1
    return tuple(counts)


def build_pair_dinv_table(max_value: int, *, step: int) -> PairTable:
    return [
        [pair_dinv_python(left, right, step) for right in range(max_value + 1)]
        for left in range(max_value + 1)
    ]


def dinv_increment_from_table(prefix: Sequence[int], value: int, pair_table: PairTable) -> int:
    total = 0
    for left in prefix:
        total += pair_table[left][value]
    return total


def cross_dinv_counts_from_table(left_counts: Word, right_counts: Word, pair_table: PairTable) -> int:
    total = 0
    for left, left_multiplicity in enumerate(left_counts):
        if left_multiplicity == 0:
            continue
        row = pair_table[left]
        for right, right_multiplicity in enumerate(right_counts):
            if right_multiplicity:
                total += left_multiplicity * right_multiplicity * row[right]
    return total


def parse_int_list(text: str) -> list[int]:
    values: list[int] = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        values.append(int(part))
    require(values, "expected a comma-separated list of integers")
    return values


def rational_dinv(sequence: Sequence[int], *, step: int) -> int:
    return rational_dinv_python(tuple(sequence), step)


def is_rational_affine_dyck(sequence: Sequence[int], *, step: int) -> bool:
    return all(sequence[index + 1] <= sequence[index] + step for index in range(len(sequence) - 1))


def is_rational_dual_dyck(sequence: Sequence[int], *, step: int) -> bool:
    return all(sequence[index + 1] > sequence[index] + step for index in range(len(sequence) - 1))


def generate_rational_dyck_sequences(length: int, *, step: int) -> Iterable[Word]:
    require(length > 0, "length must be positive")
    require(step >= 0, "t must be non-negative")

    def rec(prefix: list[int]) -> Iterable[Word]:
        if len(prefix) == length:
            yield tuple(prefix)
            return
        previous = prefix[-1]
        for value in range(previous + step + 1):
            prefix.append(value)
            yield from rec(prefix)
            prefix.pop()

    yield from rec([0])


def is_normalized_rational_dyck_sequence(sequence: Sequence[int], *, step: int) -> bool:
    values = tuple(sequence)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and is_rational_affine_dyck(values, step=step)
    )


def find_rational_extractable_position(
    sequence: Sequence[int],
    *,
    step: int,
    include_final: bool,
) -> int | None:
    values = tuple(sequence)
    require(is_normalized_rational_dyck_sequence(values, step=step), "sequence must be normalized rational Dyck")
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = sum(1 for prior in values[:index] if lower <= prior <= value - 1)
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + step:
            continue
        return index
    return None


def is_rational_m_skeleton(sequence: Sequence[int], *, step: int, ambient: int | None = None) -> bool:
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    endpoint = values[-1] if ambient is None else ambient
    return (
        endpoint >= 0
        and max(values) == endpoint
        and values[-1] == endpoint
        and find_rational_extractable_position(values, step=step, include_final=False) is None
    )


def pair_dinv(left: int, right: int, *, step: int) -> int:
    return pair_dinv_python(left, right, step)


def has_nonfinal_rational_extractable(sequence: Word, *, step: int) -> bool:
    """Fast extractable test for already-generated normalized Dyck sequences."""

    return has_nonfinal_rational_extractable_python(sequence, step)


def is_rational_m_skeleton_generated(sequence: Word, *, step: int, max_value: int | None = None) -> bool:
    """Check skeleton status for a sequence known to be normalized rational Dyck."""

    endpoint = sequence[-1]
    if max_value is None:
        max_value = max(sequence)
    if max_value != endpoint:
        return False
    return not has_nonfinal_rational_extractable_python(sequence, step)


def generate_rational_dyck_sequence_data(
    length: int,
    *,
    step: int,
    pair_table: PairTable | None = None,
) -> list[SequenceData]:
    """Generate normalized rational Dyck paths with area/dinv cached."""

    require(length > 0, "length must be positive")
    require(step >= 0, "t must be non-negative")
    return sequence_data_by_length(length, step=step, pair_table=pair_table)[length]


def sequence_data_by_length(
    max_length: int,
    *,
    step: int,
    pair_table: PairTable | None = None,
) -> dict[int, list[SequenceData]]:
    require(max_length > 0, "max length must be positive")
    require(step >= 0, "t must be non-negative")
    if pair_table is None:
        pair_table = build_pair_dinv_table(step * (max_length - 1), step=step)

    base = SequenceData((0,), 0, 0, 0, 0, True)
    by_length: dict[int, list[SequenceData]] = {1: [base]}
    previous_level = [base]
    for length in range(2, max_length + 1):
        current_level: list[SequenceData] = []
        append_current = current_level.append
        for data in previous_level:
            prefix = data.sequence
            for value in range(data.endpoint + step + 1):
                dinv_increment_value = dinv_increment_from_table(prefix, value, pair_table)
                sequence = prefix + (value,)
                max_value = data.max_value if data.max_value >= value else value
                is_skeleton = (
                    max_value == value
                    and not has_nonfinal_rational_extractable_python(sequence, step)
                )
                append_current(
                    SequenceData(
                        sequence,
                        data.area + value,
                        data.dinv + dinv_increment_value,
                        value,
                        max_value,
                        is_skeleton,
                    )
                )
        by_length[length] = current_level
        previous_level = current_level
    return by_length


def generate_direct_coefficients_and_skeletons(
    max_length: int,
    *,
    step: int,
    pair_table: PairTable,
    requested_lengths: set[int],
) -> tuple[dict[int, Counter[tuple[int, int]]], dict[int, list[SequenceData]]]:
    require(max_length > 0, "max length must be positive")
    direct_by_length = {length: Counter() for length in requested_lengths}
    skeletons_by_length: dict[int, list[SequenceData]] = defaultdict(list)
    prefix = [0]

    def rec(area: int, dinv: int, max_value: int) -> None:
        length = len(prefix)
        endpoint = prefix[-1]
        if length in direct_by_length:
            direct_by_length[length][(area, dinv)] += 1

        if max_value == endpoint:
            sequence = tuple(prefix)
            if not has_nonfinal_rational_extractable_python(sequence, step):
                skeletons_by_length[length].append(
                    SequenceData(sequence, area, dinv, endpoint, max_value, True)
                )

        if length == max_length:
            return

        for value in range(endpoint + step + 1):
            dinv_increment_value = dinv_increment_from_table(prefix, value, pair_table)
            prefix.append(value)
            rec(area + value, dinv + dinv_increment_value, max_value if max_value >= value else value)
            prefix.pop()

    rec(0, 0, 0)
    return direct_by_length, skeletons_by_length


def is_partition_shape(shape: Sequence[int]) -> bool:
    return all(part > 0 for part in shape) and all(shape[index] >= shape[index + 1] for index in range(len(shape) - 1))


def conjugate_partition(shape: Shape) -> Shape:
    if shape == ():
        return ()
    require(is_partition_shape(shape), "shape must be a partition")
    return tuple(sum(1 for part in shape if part >= column) for column in range(1, shape[0] + 1))


def at_most_two_column_shapes(total_size: int) -> list[Shape]:
    require(total_size >= 0, "tableau size must be non-negative")
    if total_size == 0:
        return [()]
    out: list[Shape] = []
    for two_cell_rows in range(total_size // 2, -1, -1):
        one_cell_rows = total_size - 2 * two_cell_rows
        out.append((2,) * two_cell_rows + (1,) * one_cell_rows)
    return out


def rational_row_reading_word(tableau: Sequence[Sequence[int]]) -> Word:
    return tuple(value for row in reversed(tableau) for value in row)


def enumerate_bounded_rational_dyck_tableaux(
    shape: Shape,
    *,
    step: int,
    max_entry: int,
) -> Iterable[Tableau]:
    if shape == ():
        yield ()
        return
    if max_entry < 0:
        return
    require(is_partition_shape(shape), "shape must be a partition")

    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape) and col < shape[row + 1] and value > rows[row + 1][col] + step:
            return False
        if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int) -> Iterable[Tableau]:
        if cell_index == len(cells):
            yield tuple(tuple(row) for row in rows)
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            rows[row][col] = value
            yield from rec(cell_index + 1)
            rows[row][col] = 0

    yield from rec(0)


def enumerate_bounded_rational_dyck_tableau_data(
    shape: Shape,
    *,
    step: int,
    max_entry: int,
    pair_table: PairTable,
) -> Iterable[TableauData]:
    """Enumerate bounded rational Dyck tableaux with cached row-word statistics."""

    if shape == ():
        yield TableauData(row_word=(), area=0, dinv=0)
        return
    if max_entry < 0:
        return
    require(is_partition_shape(shape), "shape must be a partition")

    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
    row_word: list[int] = []

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape) and col < shape[row + 1] and value > rows[row + 1][col] + step:
            return False
        if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int, area: int, dinv: int) -> Iterable[TableauData]:
        if cell_index == len(cells):
            yield TableauData(row_word=tuple(row_word), area=area, dinv=dinv)
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            dinv_increment = dinv_increment_from_table(row_word, value, pair_table)
            rows[row][col] = value
            row_word.append(value)
            yield from rec(cell_index + 1, area + value, dinv + dinv_increment)
            row_word.pop()
            rows[row][col] = 0

    yield from rec(0, 0, 0)


def aggregate_tableau_data(tableaux: Iterable[TableauData]) -> list[AggregatedTableauData]:
    grouped: Counter[tuple[Word, int, int]] = Counter()
    for tableau in tableaux:
        grouped[(value_counts(tableau.row_word), tableau.area, tableau.dinv)] += 1
    return [
        AggregatedTableauData(counts=counts, area=area, dinv=dinv, multiplicity=multiplicity)
        for (counts, area, dinv), multiplicity in grouped.items()
    ]


def enumerate_ssyt_weights(shape: Shape, *, alphabet_size: int) -> Counter[tuple[int, ...]]:
    """Return the Schur monomial expansion by SSYT enumeration."""

    require(alphabet_size > 0, "alphabet size must be positive")
    if shape == ():
        return Counter({(0,) * alphabet_size: 1})
    require(is_partition_shape(shape), "shape must be a partition")
    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row, length in enumerate(shape) for col in range(length)]
    weights: Counter[tuple[int, ...]] = Counter()

    def rec(cell_index: int, counts: list[int]) -> None:
        if cell_index == len(cells):
            weights[tuple(counts)] += 1
            return
        row, col = cells[cell_index]
        lower = 1
        if col > 0:
            lower = max(lower, rows[row][col - 1])
        if row > 0 and col < shape[row - 1]:
            lower = max(lower, rows[row - 1][col] + 1)
        for value in range(lower, alphabet_size + 1):
            rows[row][col] = value
            counts[value - 1] += 1
            rec(cell_index + 1, counts)
            counts[value - 1] -= 1
            rows[row][col] = 0

    rec(0, [0] * alphabet_size)
    return weights


def direct_coefficients(sequence_data: list[SequenceData]) -> Counter[tuple[int, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    for data in sequence_data:
        coeffs[(data.area, data.dinv)] += 1
    return coeffs


def type4_formula_coefficients(
    length: int,
    *,
    step: int,
    skeletons_by_length: dict[int, list[SequenceData]],
    pair_table: PairTable,
) -> tuple[Counter[tuple[int, int]], dict[str, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    counts = {
        "skeletons": 0,
        "tableaux": 0,
        "skeleton_tableau_pairs": 0,
        "schur_monomial_terms": 0,
    }
    schur_cache: dict[Shape, Counter[tuple[int, int]]] = {}
    tableau_cache: dict[tuple[Shape, int], list[AggregatedTableauData]] = {}

    for skeleton_length in range(1, length + 1):
        tableau_size = length - skeleton_length
        skeletons = skeletons_by_length.get(skeleton_length, [])
        counts["skeletons"] += len(skeletons)
        if not skeletons:
            continue
        skeletons_by_endpoint: dict[int, list[SequenceData]] = defaultdict(list)
        for skeleton_data in skeletons:
            skeletons_by_endpoint[skeleton_data.endpoint].append(skeleton_data)
        skeleton_counts: dict[Word, Word] = {
            skeleton_data.sequence: value_counts(skeleton_data.sequence)
            for skeleton_data in skeletons
        }

        for shape in at_most_two_column_shapes(tableau_size):
            size = sum(shape)
            schur_shape = conjugate_partition(shape)
            if schur_shape not in schur_cache:
                schur_cache[schur_shape] = enumerate_ssyt_weights(schur_shape, alphabet_size=2)
            schur_terms = list(schur_cache[schur_shape].items())

            for ambient, skeleton_group in skeletons_by_endpoint.items():
                cache_key = (shape, ambient)
                if cache_key not in tableau_cache:
                    tableau_cache[cache_key] = aggregate_tableau_data(
                        enumerate_bounded_rational_dyck_tableau_data(
                            shape=shape,
                            step=step,
                            max_entry=ambient - 1,
                            pair_table=pair_table,
                        ),
                    )
                tableaux = tableau_cache[cache_key]
                tableau_multiplicity_total = sum(tableau.multiplicity for tableau in tableaux)
                counts["tableaux"] += tableau_multiplicity_total * len(skeleton_group)
                counts["skeleton_tableau_pairs"] += tableau_multiplicity_total * len(skeleton_group)

                for skeleton_data in skeleton_group:
                    skeleton_count_vector = skeleton_counts[skeleton_data.sequence]
                    for tableau_data in tableaux:
                        if tableau_data.counts:
                            cross_dinv_value = cross_dinv_counts_from_table(
                                skeleton_count_vector,
                                tableau_data.counts,
                                pair_table,
                            )
                        else:
                            cross_dinv_value = 0
                        base_area = skeleton_data.area + tableau_data.area
                        base_dinv = skeleton_data.dinv + tableau_data.dinv + cross_dinv_value
                        for (q_power, t_power), multiplicity in schur_terms:
                            contribution = multiplicity * tableau_data.multiplicity
                            coeffs[(base_area + q_power, base_dinv - size + t_power)] += contribution
                            counts["schur_monomial_terms"] += contribution
    return coeffs, counts


def compare_case(
    *,
    step: int,
    length: int,
    direct: Counter[tuple[int, int]],
    skeletons_by_length: dict[int, list[SequenceData]],
    pair_table: PairTable,
) -> dict[str, int | float]:
    case_start = time.perf_counter()
    formula, formula_counts = type4_formula_coefficients(
        length,
        step=step,
        skeletons_by_length=skeletons_by_length,
        pair_table=pair_table,
    )
    mismatches = [
        (key, direct[key], formula[key])
        for key in sorted(set(direct) | set(formula))
        if direct[key] != formula[key]
    ]
    require(not mismatches, f"coefficient mismatch for t={step}, n={length}: {mismatches[:10]}")
    elapsed = time.perf_counter() - case_start
    return {
        "direct_paths": sum(direct.values()),
        "direct_terms": len(direct),
        "formula_terms": len(formula),
        "coefficient_keys": len(set(direct) | set(formula)),
        "skeletons": formula_counts["skeletons"],
        "tableaux": formula_counts["tableaux"],
        "skeleton_tableau_pairs": formula_counts["skeleton_tableau_pairs"],
        "schur_monomial_terms": formula_counts["schur_monomial_terms"],
        "elapsed_seconds": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t-values", required=True, help="Comma-separated rational step values t.")
    parser.add_argument("--n-values", required=True, help="Comma-separated length values n, i.e. rational s-values.")
    args = parser.parse_args()

    steps = parse_int_list(args.t_values)
    lengths = parse_int_list(args.n_values)
    start = time.perf_counter()
    compared: dict[tuple[int, int], dict[str, int | float]] = {}
    skipped: list[tuple[int, int]] = []

    require(all(step >= 0 for step in steps), "all t-values must be non-negative")
    require(all(length > 0 for length in lengths), "all n-values must be positive")
    require(at_most_two_column_shapes(5) == [(2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)], "shape smoke check failed")
    require(is_rational_m_skeleton((0, 2), step=2, ambient=2), "skeleton smoke check failed")
    require(rational_dinv((0, 1, 0), step=2) == 5, "dinv smoke check failed")
    require(comb(3, 2) == 3, "math smoke check failed")

    for step in steps:
        if step == 1:
            for length in lengths:
                skipped.append((step, length))
            continue
        pair_table = build_pair_dinv_table(step * (max(lengths) - 1), step=step)
        direct_by_length, skeletons_by_length = generate_direct_coefficients_and_skeletons(
            max(lengths),
            step=step,
            pair_table=pair_table,
            requested_lengths=set(lengths),
        )
        for length in lengths:
            case_result = compare_case(
                step=step,
                length=length,
                direct=direct_by_length[length],
                skeletons_by_length=skeletons_by_length,
                pair_table=pair_table,
            )
            compared[(step, length)] = case_result
            print(
                f"  t={step}, n={length}: paths={case_result['direct_paths']}, "
                f"keys={case_result['coefficient_keys']}, skeletons={case_result['skeletons']}, "
                f"tableaux={case_result['tableaux']}, elapsed={case_result['elapsed_seconds']:.3f}s",
                flush=True,
            )

    require(compared, "no non-t=1 cases were checked")
    print("rational two-column skeleton/tableau formula check")
    print("  convention: r = n*t + 1; n is the rational s-value / path length")
    print(f"  compared cases: {sorted(compared)}")
    print(f"  skipped t=1 cases: {skipped}")
    print(f"  counts: {compared}")
    print(f"  elapsed: {time.perf_counter() - start:.3f}s")
    print("  all requested finite checks passed")


if __name__ == "__main__":
    main()
```

### `docs/items/dyck_skeleton_tableau_formulas/code/README.md`

```markdown
# Code

Executable checks for the Dyck skeleton tableau formula item.

## Rational Two-Column Formula

Command:

````text
python check_rational_two_column_formula.py --t-values 2,3,4 --n-values 1,2,3,4
````

Official checks:

````text
python check_rational_two_column_formula.py --t-values 2 --n-values 1,2,3,4,5,6,7,8,9,10,11,12,13,14
python check_rational_two_column_formula.py --t-values 3 --n-values 1,2,3,4,5,6,7,8,9,10,11,12
python check_rational_two_column_formula.py --t-values 4 --n-values 1,2,3,4,5,6,7,8,9,10
````

Inputs:

- `--t-values`: comma-separated rational step values.
- `--n-values`: comma-separated length values, i.e. the rational `s` values in
  `r = n*t + 1`.

The checker skips `t=1`, since that is the proved classical case.  For every
other requested `(t,n)` pair it computes two coefficient dictionaries grouped
by `(area, dinv)`:

- the direct side, generated from all normalized rational Dyck paths of length
  `n`;
- the formula side, generated from pairs `(F,P)` where `F` is a rational
  Dyck `m`-skeleton and `P` is an at-most-two-column rational Dyck tableau
  with entries in `[0,m-1]`, expanded by the corresponding two-variable Schur
  factor.

The check passes exactly when the two grouped coefficient dictionaries agree
for every requested case.
```

### `docs/items/dyck_skeleton_tableau_formulas/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 77089
sha256: 197e71b806111947ae5c2168e33d8cb474f577b6226ca7b357c9a47ba111006a
```

### `docs/items/dyck_skeleton_tableau_formulas/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\DeclareMathOperator{\area}{area}
\DeclareMathOperator{\dinv}{dinv}

\title{Dyck Skeleton Tableau Formulas}
\author{}
\date{}

\begin{document}
\maketitle

\section{What the formula says}

The purpose of this item is to compare two ways of forming the same
two-variable generating function.  The direct side sums
\(q^{\area}t^{\dinv}\) over normalized rational Dyck sequences.  The
skeleton/tableau side groups the same expected polynomial by rational
skeletons, at-most-two-column rational Dyck tableaux, and a two-variable
Schur factor.

The checker uses the option name \(t\) for the rational step and \(n\) for the
length.  In this explanation, the rational step is written \(\tau\) and the
length is written \(s\), so the congruence family is
\[
  r=s\tau+1.
\]
Thus the checker's case \(t=1\) is the case \(\tau=1\).  From this point on,
\(\tau\) denotes the rational step, while \(t\) remains the second variable in
\(q,t\).

\subsection{Rational Dyck side}

Fix \(s\geq 1\) and \(\tau\geq 0\).  A normalized rational Dyck sequence of
length \(s\) and step \(\tau\) is a sequence
\[
  D=(D_0,\ldots,D_{s-1})
\]
of nonnegative integers such that \(D_0=0\) and
\[
  D_{i+1}\leq D_i+\tau
  \qquad(0\leq i<s-1).
\]
For a finite integer sequence \(x=(x_0,\ldots,x_{\ell-1})\), define
\[
  \dinv_\tau(x)=
  \sum_{0\leq i<j<\ell} d_\tau(x_i,x_j),
\]
where
\[
  d_\tau(a,b)=
  \begin{cases}
    \max(0,a+\tau-b),& a\leq b,\\
    \max(0,b+1+\tau-a),& a>b.
  \end{cases}
\]
The area statistic is
\[
  \area(x)=\sum_i x_i.
\]
The direct rational \(q,t\)-Catalan side in this model is therefore
\[
  C_{s,\tau}(q,t)
  =
  \sum_D q^{\area(D)}t^{\dinv_\tau(D)},
\]
where \(D\) ranges over all normalized rational Dyck sequences of length
\(s\).

\subsection{Skeleton--tableau side}

The formula decomposes the same polynomial by first choosing a rational
skeleton and then filling the remaining cells by a two-column rational Dyck
tableau.

An entry \(D_j=e\) of a normalized rational Dyck sequence is called
extractable if \(e>0\), exactly one earlier entry lies in the predecessor
window
\[
  \{a\in\mathbb Z_{\geq 0}: \max(0,e-\tau)\leq a\leq e-1\},
\]
and deleting \(D_j\) preserves the adjacent rational Dyck inequality.  More
explicitly, if \(0<j<s-1\), then deletion requires
\[
  D_{j+1}\leq D_{j-1}+\tau.
\]
If \(j=s-1\), there is no new adjacent pair to check.  For \(\tau=0\), the
predecessor window is empty.  A rational \(m\)-skeleton is a normalized
rational Dyck sequence \(F\) with final entry equal to its maximum,
\[
  F_{|F|-1}=\max(F)=m,
\]
and with no nonfinal extractable entry.  A final extractable entry is allowed
in an \(m\)-skeleton.

A rational Dyck tableau \(P\) of step \(\tau\) is a left-aligned tableau whose
row lengths form a partition.  We index its rows in the source-paper
convention: \(P_0\) is the top row, \(P_1\) is the row immediately below it,
and so on.  Rows are read left to right and are dual rational Dyck sequences,
\[
  P_i[j+1]>P_i[j]+\tau,
\]
while columns, read bottom to top, satisfy the affine rational Dyck condition.
Equivalently, if row \(i\) is immediately above row \(i+1\), then
\[
  P_i[j]\leq P_{i+1}[j]+\tau
\]
whenever both entries exist.  Its row-reading word is
\[
  \operatorname{RR}(P)=P_{\text{bottom}}P_{\text{next}}\cdots P_{\text{top}},
\]
with each row read left to right, and \(\lambda(P)\) denotes its shape.

The checked conjectural rational two-column skeleton/tableau identity is
\[
  C_{s,\tau}(q,t)
  =
  \sum_{(F,P)}
  q^{\area(F:\operatorname{RR}(P))}
  t^{\dinv_\tau(F:\operatorname{RR}(P))-|P|}
  s_{\lambda(P)'}(q,t).
\]
The sum is over all pairs \((F,P)\) such that \(F\) is a rational
\(m\)-skeleton of step \(\tau\) for some \(m\geq 0\), \(P\) is an
at-most-two-column rational Dyck tableau of step \(\tau\) with entries in
\([0,m-1]\), and
\[
  |F|+|\operatorname{RR}(P)|=s.
\]
Here \(F:\operatorname{RR}(P)\) means concatenation, \(|P|\) is the number of
cells of \(P\), \(\lambda(P)'\) is the conjugate partition, and
\(s_{\lambda(P)'}(q,t)\) is the Schur function in the two variables \(q,t\).
This is the checked conjectural identity for general rational step
\(\tau\).

\section{Source context and status}

Status summary: the identity is proved for \(\tau=1\), degenerate for
\(\tau=0\), and computationally verified but not proved for the tested
values \(\tau>1\).

For \(\tau=1\), the formula is exactly the two-column tableau formula for the
ordinary \(q,t\)-Catalan polynomial proved in the source paper.  In that
proof, Dyck sequences are sent by the paper's Type 1 through Type 4
correspondences to Type 4 triples \((F,P,Q)\), where \(F\) is a Dyck
\(m\)-skeleton, \(P\) is an at-most-two-column Dyck tableau, and \(Q\) is a
binary reverse semistandard tableau of shape \(\lambda(P)\).

The \(-|P|\) shift in the displayed formula comes from summing over the
binary recording tableau \(Q\).  For fixed \((F,P)\), one has
\[
  q^{\#1(Q)}t^{-\#1(Q)}
  =
  t^{-|P|}q^{\#1(Q)}t^{\#0(Q)},
\]
since \(\#0(Q)+\#1(Q)=|P|\).  Transposing \(Q\) turns the binary reverse
semistandard condition on shape \(\lambda(P)\) into the ordinary
semistandard condition on the conjugate shape \(\lambda(P)'\), giving
\[
  \sum_Q q^{\#1(Q)}t^{\#0(Q)}
  =
  s_{\lambda(P)'}(t,q)
  =
  s_{\lambda(P)'}(q,t).
\]

The case \(\tau=0\) is degenerate.  The adjacent condition becomes
\(D_{i+1}\leq D_i\), so a normalized nonnegative sequence starts at \(0\) and
can only stay at \(0\).  Thus the direct side has only the all-zero sequence
in each length.  On the formula side, a contributing skeleton must have
\(m=0\), and a nonempty tableau would need entries in \([0,m-1]=[0,-1]\),
which is impossible.  Therefore only \(F=(0,\ldots,0)\) with \(P=\varnothing\)
contributes.

For \(\tau>1\), this item records finite evidence for the conjectural
rational analogue tested here.  The checker does not prove the formula in
these cases; it enumerates both sides and compares the resulting coefficient
dictionaries grouped by \((\area,\dinv)\).

\section{Computational verification}

The checker for the rational two-column skeleton/tableau formula is recorded
in
\[
\texttt{code/check\_rational\_two\_column\_formula.py}.
\]
It compares two coefficient dictionaries: one from the direct normalized
rational Dyck sequence generating function, and one from the formula-side
expansion described above.  The check passes exactly when the two
dictionaries agree for every \((\operatorname{area},\operatorname{dinv})\)
key in the requested finite range.

The official finite checks performed for this item are:
\begin{itemize}
\item \(\tau=2\), lengths \(1 \leq s \leq 14\), elapsed time
      \(4102.814\) seconds;
\item \(\tau=3\), lengths \(1 \leq s \leq 12\), elapsed time
      \(25254.334\) seconds;
\item \(\tau=4\), lengths \(1 \leq s \leq 10\), elapsed time
      \(494.131\) seconds.
\end{itemize}
All three official checks passed.  These finite checks do not prove the
identity for all lengths for any \(\tau>1\).

\end{document}
```

### `docs/items/dyck_skeleton_tableau_formulas/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dyck Skeleton Tableau Formulas</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>Dyck Skeleton Tableau Formulas</h1>
    <p>Classical tableau formulas are proved in the 2026 preprint; r == 1 mod s analogues need review.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.pdf">View PDF</a></li>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This educational section will explain the Dyck skeleton formula and its relation to low-deficit qt-Catalan coefficients.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/01_core_dyck_sequence_routines.py`

```python
from itertools import combinations
from math import comb

def is_Dyck(S):
    S = tuple(S)
    return (
        len(S) > 0
        and S[0] == 0
        and all(isinstance(x, int) and x >= 0 for x in S)
        and all(S[i + 1] <= S[i] + 1 for i in range(len(S) - 1))
    )

def generate_Dycks(n):
    out = []
    def rec(S):
        if len(S) == n:
            out.append(tuple(S))
            return
        for x in range(S[-1] + 2):
            rec(S + [x])
    rec([0])
    return out

def area(S):
    return sum(S)

def dinv(S):
    S = tuple(S)
    return sum(
        1
        for i in range(len(S))
        for j in range(i + 1, len(S))
        if S[i] == S[j] or S[i] == S[j] + 1
    )

def defc(S):
    return comb(len(S), 2) - area(S) - dinv(S)

def find_extractable(S):
    S = tuple(S)
    for j, x in enumerate(S):
        if x == 0:
            continue
        if sum(1 for i in range(j) if S[i] == x - 1) != 1:
            continue
        if j + 1 < len(S) and S[j + 1] > x:
            continue
        return j, x
    return None

def remove_at(S, j):
    S = tuple(S)
    return S[:j] + S[j + 1:]

def is_full_skeleton(S):
    return is_Dyck(S) and find_extractable(S) is None

def epsilon(n):
    return () if n < 4 else tuple([0, 0, 1] + [0] * (n - 4) + [1])

def omega(n):
    return tuple([0] * (n - 1) + [1])

def is_special_skeleton(S):
    S = tuple(S)
    return is_full_skeleton(S) and S != epsilon(len(S))

def inject(S, e):
    S = tuple(S)
    for i, x in enumerate(S):
        if x == e - 1:
            ans = S[:i + 1] + (e,) + S[i + 1:]
            assert is_Dyck(ans)
            return ans
    raise ValueError(f"cannot inject {e} into {S}")

def inject_right_to_left(base, entries):
    out = tuple(base)
    for e in reversed(tuple(entries)):
        out = inject(out, e)
    return out
# Local affine/reverse helpers.

def bk2(a, b):
    return (b, a) if a > b + 1 else (a, b)

def fw2(a, b):
    return (b, a) if b > a + 1 else (a, b)

def bk3(a, b, c):
    if a > b + 1:
        a, b = b, a
    if b > c + 1:
        b, c = c, b
    if a > b + 1:
        a, b = b, a
    return a, b, c
# Local East and West maps.

def East3(W):
    W = tuple(W)
    assert len(W) == 3
    return W if W[1] <= W[2] + 1 else None

def East5(W):
    W = tuple(W)
    assert len(W) == 5
    x_m2, x_m1, x_0, x_1, x_2 = W
    y_m1, y_0 = bk2(x_m1, x_0)
    if x_m1 > x_1 + 1 and y_0 <= x_2 + 1:
        return (x_m2, x_1, y_m1, y_0, x_2)
    if x_m1 <= x_1 + 1 and x_m1 <= x_2 + 1:
        return (x_m2, x_1, x_0, x_m1, x_2)
    return None
_CASE4A = {
    (3, 3, 4, 1, 2): (1, 2, 4, 3, 3),
    (3, 4, 4, 1, 2): (1, 2, 4, 3, 4),
    (4, 3, 4, 1, 2): (1, 2, 4, 4, 3),
    (2, 3, 4, 1, 2): (1, 2, 4, 3, 2),
}
_CASE4B = {
    (3, 3, 4, 2, 1): (2, 1, 4, 3, 3),
    (3, 4, 4, 2, 1): (2, 1, 4, 3, 4),
    (4, 3, 4, 2, 1): (2, 1, 4, 4, 3),
    (2, 3, 4, 2, 1): (2, 1, 4, 3, 2),
}
_CASE4C = {
    (3, 4, 4, 2, 2): (2, 2, 4, 4, 3),
    (3, 4, 5, 2, 2): (2, 2, 5, 4, 3),
}
_CASE4D = {
    (3, 3, 4): lambda o: (2, o, 4, 3, 3),
    (3, 4, 4): lambda o: (2, o, 4, 3, 4),
    (4, 3, 4): lambda o: (2, o, 4, 4, 3),
    (2, 3, 4): lambda o: (2, o, 2, 4, 3),
    (3, 4, 2): lambda o: (2, o, 4, 3, 2),
}

def East7(W):
    W = tuple(W)
    assert len(W) == 7
    x_m3, x_m2, x_m1, x_0, x_1, x_2, x_3 = W
    if x_0 <= x_1 + 1:
        return W
    y_m1, y_0 = bk2(x_m1, x_0)
    if x_m1 > x_1 + 1 and y_0 <= x_2 + 1:
        return (x_m3, x_m2, x_1, y_m1, y_0, x_2, x_3)
    if x_m1 <= x_1 + 1 and x_m1 <= x_2 + 1:
        return (x_m3, x_m2, x_1, x_0, x_m1, x_2, x_3)
    if min(x_m2, x_m1, x_0) > max(x_1, x_2) + 1:
        return (x_m3,) + fw2(x_1, x_2) + bk3(x_m2, x_m1, x_0) + (x_3,)
    shift = max(x_1, x_2) - 2
    reduced = (x_m2 - shift, x_m1 - shift, x_0 - shift,
               x_1 - shift, x_2 - shift)
    for table in (_CASE4A, _CASE4B, _CASE4C):
        if reduced in table:
            return (x_m3,) + tuple(y + shift for y in table[reduced]) + (x_3,)
    if reduced[4] == 2 and reduced[3] <= 0 and reduced[:3] in _CASE4D:
        return (x_m3,) + tuple(y + shift for y in _CASE4D[reduced[:3]](reduced[3])) + (x_3,)
    raise ValueError(f"East7 undefined on {W}")

def rev(W):
    return tuple(reversed(tuple(W)))

def West3(W):
    ans = East3(rev(W))
    return None if ans is None else rev(ans)

def West5(W):
    ans = East5(rev(W))
    return None if ans is None else rev(ans)

def West7(W):
    return rev(East7(rev(W)))

def is_far_apart_decomposable(W):
    W = tuple(W)
    assert len(W) == 7
    indices = list(range(7))
    for p1 in combinations(indices, 2):
        if abs(W[p1[0]] - W[p1[1]]) < 2:
            continue
        r1 = [i for i in indices if i not in p1]
        for p2 in combinations(r1, 2):
            if abs(W[p2[0]] - W[p2[1]]) < 2:
                continue
            r2 = [i for i in r1 if i not in p2]
            for p3 in combinations(r2, 2):
                if abs(W[p3[0]] - W[p3[1]]) >= 2:
                    return True
    return False
# Global up and down maps.

def up(S):
    S = tuple(S)
    n = len(S)
    if S == omega(n):
        return epsilon(n), 3
    if is_full_skeleton(S):
        return inject(S[:-1], S[-1] + 1), 3
    j1, e1 = find_extractable(S)
    C1 = remove_at(S, j1)
    sigma1 = C1 + (e1 - 1,)
    if East3(sigma1[-3:]) is not None:
        ans = inject_right_to_left(sigma1[:-2], (sigma1[-2] + 1, sigma1[-1] + 1))
        return ans, 3
    j2, e2 = find_extractable(C1)
    C2 = remove_at(C1, j2)
    sigma2 = C2 + (e1 - 1, e2 - 1)
    W5 = East5(sigma2[-5:])
    if W5 is not None:
        base = sigma2[:-5] + W5[:2]
        ans = inject_right_to_left(base, tuple(x + 1 for x in W5[2:]))
        return ans, 5
    j3, e3 = find_extractable(C2)
    C3 = remove_at(C2, j3)
    sigma3 = C3 + (e1 - 1, e2 - 1, e3 - 1)
    W7 = sigma3[-7:]
    assert not is_far_apart_decomposable(W7)
    E7 = East7(W7)
    new_sigma3 = sigma3[:-7] + E7
    ans = inject_right_to_left(new_sigma3[:-4], tuple(x + 1 for x in new_sigma3[-4:]))
    return ans, 7

def down(S):
    S = tuple(S)
    n = len(S)
    if S == epsilon(n):
        return omega(n), 3
    j1, f1 = find_extractable(S)
    D1 = remove_at(S, j1)
    candidate = D1 + (f1 - 1,)
    if find_extractable(candidate) is None:
        assert is_Dyck(candidate)
        return candidate, 3
    j2, f2 = find_extractable(D1)
    D2 = remove_at(D1, j2)
    tau1 = D2 + (f1 - 1, f2 - 1)
    if West3(tau1[-3:]) is not None:
        return inject(tau1[:-1], tau1[-1] + 1), 3
    j3, f3 = find_extractable(D2)
    D3 = remove_at(D2, j3)
    tau2 = D3 + (f1 - 1, f2 - 1, f3 - 1)
    W5 = West5(tau2[-5:])
    if W5 is not None:
        base = tau2[:-5] + W5[:3]
        ans = inject_right_to_left(base, tuple(x + 1 for x in W5[3:]))
        return ans, 5
    j4, f4 = find_extractable(D3)
    D4 = remove_at(D3, j4)
    tau3 = D4 + (f1 - 1, f2 - 1, f3 - 1, f4 - 1)
    W7 = tau3[-7:]
    assert not is_far_apart_decomposable(W7)
    new_tau3 = tau3[:-7] + West7(W7)
    ans = inject_right_to_left(new_tau3[:-3], tuple(x + 1 for x in new_tau3[-3:]))
    return ans, 7
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/02_make_strings.py`

```python
def make_strings(n, d):
    ell = (comb(n, 2) - d) // 2
    all_dyck = [S for S in generate_Dycks(n) if defc(S) == d]
    target = {S for S in all_dyck if area(S) <= ell}
    starts = sorted(
        [S for S in target if is_special_skeleton(S)],
        key=lambda S: (area(S), S),
    )
    strings = []
    levels = []
    for start in starts:
        chain = [start]
        current = start
        while area(current) < ell:
            nxt, level = up(current)
            assert defc(nxt) == d
            assert area(nxt) == area(current) + 1
            chain.append(nxt)
            levels.append((current, nxt, level))
            current = nxt
        strings.append(tuple(chain))
    covered = [S for chain in strings for S in chain]
    assert set(covered) == target
    assert len(covered) == len(set(covered))
    return tuple(strings), tuple(levels)
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/01_residual_finite_check.py`

```python
from collections import Counter
from math import comb

def stop(message):
    raise AssertionError(message)

def is_dyck_sequence(seq):
    return (
        bool(seq)
        and seq[0] == 0
        and all(x >= 0 for x in seq)
        and all(seq[i + 1] <= seq[i] + 1
                for i in range(len(seq) - 1))
    )

def deficit_and_area(seq):
    first_index = {}
    for i, value in enumerate(seq):
        first_index.setdefault(value, i)
    deficit = 0
    for i, left in enumerate(seq):
        for right in seq[i + 1:]:
            if left > right + 1:
                deficit += 1
            elif left < right and first_index[left] != i:
                deficit += 1
    return deficit, sum(seq)

def generate_dyck_sequences(length):
    sequences = []
    def extend(prefix):
        if len(prefix) == length:
            sequences.append(prefix)
            return
        for next_value in range(prefix[-1] + 2):
            extend(prefix + (next_value,))
    extend((0,))
    return sequences

def leftmost_extractable(seq):
    for index, value in enumerate(seq):
        has_parent = sum(x == value - 1 for x in seq[:index]) == 1
        next_ok = index == len(seq) - 1 or seq[index + 1] <= value
        if value > 0 and has_parent and next_ok:
            return index, value
    return None

def remove_index(seq, index):
    return seq[:index] + seq[index + 1:]

def is_full_skeleton(seq):
    return is_dyck_sequence(seq) and leftmost_extractable(seq) is None

def almost_zero_sequence(length):
    return (0,) * (length - 1) + (1,)

def excluded_skeleton(length):
    return (0, 0, 1) + (0,) * (length - 4) + (1,)

def is_special_skeleton(seq):
    return is_full_skeleton(seq) and seq != excluded_skeleton(len(seq))

def inject_after_first_parent(seq, value):
    for index, entry in enumerate(seq):
        if entry == value - 1:
            result = seq[:index + 1] + (value,) + seq[index + 1:]
            if is_dyck_sequence(result):
                return result
            stop(("skeleton injection produced non-Dyck",
                  seq, value, result))
    stop(("skeleton injection failed", seq, value))

def east3_applies(window3):
    _, x0, x1 = window3
    return x0 <= x1 + 1

def west3_applies(window3):
    return east3_applies(tuple(reversed(window3)))

def east5_case2b_applies(window5):
    _, x_minus1, x0, x1, x2 = window5
    return (
        x0 > x1 + 1
        and x_minus1 <= x1 + 1
        and x_minus1 <= x2 + 1
    )

def west5_case2b_applies(window5):
    return east5_case2b_applies(tuple(reversed(window5)))

def check_up_prefix(seq, length, deficit, half_area_limit):
    if seq == almost_zero_sequence(length):
        return "up special"
    if is_full_skeleton(seq):
        result = inject_after_first_parent(seq[:-1], seq[-1] + 1)
        if len(result) != length:
            stop(("up skeleton changed length", seq, result))
        return "up skeleton"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: up first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    word1 = child1 + (value1 - 1,)
    if east3_applies(word1[-3:]):
        if index1 >= length - 2:
            stop(("position lemma: up/East3 position", seq, index1))
        return "up East3"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: up second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if not (index1 < length - 3 and index2 < len(child1) - 3):
        stop(("position lemma: up/East5 position",
              seq, index1, child1, index2))
    if not east5_case2b_applies(word2[-5:]):
        stop(("seven-window lemma: up would reach East7",
              length, deficit, half_area_limit, seq, word2[-5:]))
    return "up East5 case 2b"

def check_down_prefix(seq, length, deficit, half_area_limit):
    if seq == excluded_skeleton(length):
        return "down special"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: down first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    skeleton_candidate = child1 + (value1 - 1,)
    if is_full_skeleton(skeleton_candidate):
        if len(skeleton_candidate) != length:
            stop(("down skeleton changed length", seq, skeleton_candidate))
        return "down skeleton"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: down second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if west3_applies(word2[-3:]):
        if not (index1 < length - 1 and index2 < len(child1) - 1):
            stop(("position lemma: down/West3 position",
                  seq, index1, child1, index2))
        return "down West3"
    third = leftmost_extractable(child2)
    if third is None:
        stop(("extraction lemma: down third extraction failed",
              length, deficit, half_area_limit, seq, child2))
    index3, value3 = third
    child3 = remove_index(child2, index3)
    word3 = child3 + (value1 - 1, value2 - 1, value3 - 1)
    if not (
        index1 < length - 2
        and index2 < len(child1) - 2
        and index3 < len(child2) - 2
    ):
        stop(("position lemma: down/West5 position",
              seq, index1, child1, index2, child2, index3))
    if not west5_case2b_applies(word3[-5:]):
        stop(("seven-window lemma: down would reach West7",
              length, deficit, half_area_limit, seq, word3[-5:]))
    return "down West5 case 2b"

def main():
    up_counts = Counter()
    down_counts = Counter()
    by_length = {
        length: {"up": Counter(), "down": Counter()}
        for length in range(4, 8)
    }
    for length in range(4, 8):
        for seq in generate_dyck_sequences(length):
            deficit, area = deficit_and_area(seq)
            if deficit > 2 * length - 8:
                continue
            half_area_limit = (comb(length, 2) - deficit) // 2
            if area <= half_area_limit - 1:
                label = check_up_prefix(
                    seq, length, deficit, half_area_limit)
                up_counts[label] += 1
                by_length[length]["up"][label] += 1
            if area <= half_area_limit and not is_special_skeleton(seq):
                label = check_down_prefix(
                    seq, length, deficit, half_area_limit)
                down_counts[label] += 1
                by_length[length]["down"][label] += 1
    print("EverythingOkay = True")
    print("up counts  ", dict(up_counts))
    print("down counts", dict(down_counts))
    print()
    for length in range(4, 8):
        print(f"n={length}")
        print("  up:  ", dict(by_length[length]["up"]))
        print("  down:", dict(by_length[length]["down"]))
    print()
    print("No East7 or West7 branch was reached for 4 <= n <= 7.")
if __name__ == "__main__":
    main()
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/02_residual_successful_output.txt`

```text
EverythingOkay = True
up counts   {'up skeleton': 42, 'up East3': 152,
             'up special': 2, 'up East5 case 2b': 4}
down counts {'down skeleton': 42, 'down West3': 152,
             'down special': 2, 'down West5 case 2b': 4}
n=4
  up:   {'up skeleton': 1, 'up East3': 2}
  down: {'down skeleton': 1, 'down West3': 2}
n=5
  up:   {'up skeleton': 4, 'up East3': 9}
  down: {'down skeleton': 4, 'down West3': 9}
n=6
  up:   {'up skeleton': 11, 'up special': 1, 'up East3': 32}
  down: {'down special': 1, 'down skeleton': 11, 'down West3': 32}
n=7
  up:   {'up skeleton': 26, 'up special': 1,
         'up East3': 109, 'up East5 case 2b': 4}
  down: {'down skeleton': 26, 'down special': 1,
         'down West3': 109, 'down West5 case 2b': 4}
No East7 or West7 branch was reached for 4 <= n <= 7.
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/03_east7_west7_seven_window_checker.py`

```python
from __future__ import annotations

import math
from functools import lru_cache
from itertools import combinations, permutations
from math import comb


EXPECTED_CASE1_TABLE = {
    10: (33, 23),
    11: (26, 18),
    12: (16, 11),
    13: (9, 6),
    14: (None, None),
    15: (None, None),
    16: (None, None),
    17: (None, None),
    18: (None, None),
    19: (None, None),
    20: (None, None),
    21: (None, None),
}

EXPECTED_CASE2_TABLE = {
    0: (26, 18),
    1: (23, 16),
    2: (23, 16),
    3: (20, 14),
    4: (20, 14),
    5: (19, 13),
    6: (17, 12),
    7: (16, 11),
    8: (16, 11),
    9: (13, 9),
    10: (13, 9),
    11: (12, 8),
    12: (10, 7),
    13: (9, 6),
    14: (9, 6),
    15: (None, None),
    16: (None, None),
    17: (None, None),
    18: (None, None),
    19: (None, None),
    20: (None, None),
    21: (None, None),
}

EXPECTED_FINITE_COUNTS = {
    ("Case 1", "East"): {"children": 2473, "triples": 9919},
    ("Case 1", "West"): {"children": 2911, "triples": 10311},
    ("Case 2", "East"): {"children": 3860, "triples": 715},
    ("Case 2", "West"): {"children": 4827, "triples": 1756},
}


def unique_permutations(seq: tuple[int, ...]):
    """Yield all distinct permutations of seq."""

    seen = set()
    for perm in permutations(seq):
        if perm not in seen:
            seen.add(perm)
            yield perm


def is_far_apart_decomposable(vals: tuple[int, ...]) -> bool:
    """Return True iff vals has three disjoint pairs at distance at least 2."""

    indices = list(range(7))
    for pair1 in combinations(indices, 2):
        if abs(vals[pair1[0]] - vals[pair1[1]]) < 2:
            continue
        remaining1 = [i for i in indices if i not in pair1]
        for pair2 in combinations(remaining1, 2):
            if abs(vals[pair2[0]] - vals[pair2[1]]) < 2:
                continue
            remaining2 = [i for i in remaining1 if i not in pair2]
            for pair3 in combinations(remaining2, 2):
                if abs(vals[pair3[0]] - vals[pair3[1]]) >= 2:
                    return True
    return False


def east3_fails(p: tuple[int, ...]) -> bool:
    """East3 fails iff the central pair violates the reverse condition."""

    return p[3] > p[4] + 1


def east5_fails(p: tuple[int, ...]) -> bool:
    """Return True iff neither appendix East5 Case 2a nor 2b applies."""

    x_m1, x_0, x_1, x_2 = p[2], p[3], p[4], p[5]
    y_0 = x_m1 if x_m1 > x_0 + 1 else x_0
    case2a = (x_m1 > x_1 + 1) and (y_0 <= x_2 + 1)
    case2b = (x_m1 <= x_1 + 1) and (x_m1 <= x_2 + 1)
    return not case2a and not case2b


def is_valid_l_element(p: tuple[int, ...]) -> bool:
    """Return True iff p has affine first four and reverse last three."""

    return all(p[i + 1] <= p[i] + 1 for i in range(3)) and all(
        p[i] <= p[i + 1] + 1 for i in range(4, 6)
    )


def get_ew() -> set[tuple[int, ...]]:
    """Generate normalized East seven-term patterns surviving the preliminary tests."""

    valid_windows = set()
    base_sequences: list[tuple[int, ...]] = []

    def gen_base(seq: tuple[int, ...]) -> None:
        if len(seq) == 7:
            base_sequences.append(seq)
            return
        for step in (0, 1, 2):
            gen_base(seq + (seq[-1] + step,))

    gen_base((0,))

    for base in base_sequences:
        for perm in unique_permutations(base):
            if (
                is_valid_l_element(perm)
                and east3_fails(perm)
                and east5_fails(perm)
                and is_far_apart_decomposable(perm)
            ):
                valid_windows.add(perm)

    return valid_windows


def get_ww(ew: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """West windows are ordinary reversals of East windows."""

    return {tuple(reversed(w)) for w in ew}


def window_stats(window: tuple[int, ...], m: int, suffix_len: int) -> tuple[int, int]:
    """Compute corrected local id and q0 for a window and prefix max m."""

    seen = {}
    win_first = []
    for i, value in enumerate(window):
        if value not in seen:
            seen[value] = i
            win_first.append(True)
        else:
            win_first.append(False)

    is_initial = [win_first[i] and window[i] > m for i in range(len(window))]

    pair_count = 0
    for i in range(len(window)):
        for j in range(i + 1, len(window)):
            vi, vj = window[i], window[j]
            if vi > vj + 1:
                pair_count += 1
            elif vi < vj and not is_initial[i]:
                pair_count += 1

    suffix_start = len(window) - suffix_len
    suffix_correction = 0
    for j in range(suffix_start, len(window)):
        for value in range(m + 1, window[j]):
            if value not in window[:j]:
                suffix_correction += 1

    int_defc = pair_count - suffix_correction

    q0 = sum(max(0, (m - 1) - value) for i, value in enumerate(window) if not is_initial[i])
    return int_defc, q0


def compute_id_mid(window: tuple[int, ...], suffix_len: int) -> tuple[int, int]:
    """Return id_mid(w)=id(w,max(w[0]-1,w[6]-1,mid(w)))."""

    mid_value = sorted(window, reverse=True)[3]
    m = max(window[0] - 1, window[6] - 1, mid_value)
    int_defc, _ = window_stats(window, m, suffix_len)
    return int_defc, m


def compute_id_base(window: tuple[int, ...], suffix_len: int) -> int:
    """Return id_base(w)=id(w,max(w[0]-1,w[6]-1))."""

    int_defc, _ = window_stats(window, max(window[0] - 1, window[6] - 1), suffix_len)
    return int_defc


def compute_k_from_n(n_value: int) -> int:
    """Largest K with C(K,2) <= C(n,2)/2."""

    half = comb(n_value, 2) // 2
    test = 0
    while comb(test + 1, 2) <= half:
        test += 1
    return test


def compute_nk_case1(id_val: int) -> tuple[int | None, int | None]:
    """Compute Case 1 N(id), K(id), including the -4 area penalty."""

    max_n = None
    for n_value in range(8, 300):
        m0 = math.ceil((n_value + id_val - 16) / 3)
        q_star = 3 * m0 - (n_value + id_val - 16)
        lhs_twice = 2 * (comb(m0 + 1, 2) + (m0 - 1) * (n_value - m0 - 1) - q_star)
        rhs_twice = comb(n_value, 2) - id_val - q_star - 3 * (n_value - m0 - 8) - 8
        if lhs_twice <= rhs_twice:
            max_n = n_value
    if max_n is None:
        return None, None
    return max_n, compute_k_from_n(max_n)


def compute_nk_case2(id_val: int) -> tuple[int | None, int | None]:
    """Compute Case 2 N(id), K(id), including the -4 area penalty."""

    max_n = None
    for n_value in range(8, 300):
        chi_numer = 2 * n_value + id_val - 24
        m0 = max(0, math.ceil(chi_numer / 4))
        q_star = max(0, min(4 * m0 - chi_numer, 3))
        lhs_twice = 2 * (comb(m0 + 1, 2) + (m0 - 1) * (n_value - m0 - 1) - q_star)
        rhs_twice = comb(n_value, 2) - id_val - q_star - 4 * (n_value - m0 - 8) - 8
        if lhs_twice <= rhs_twice:
            max_n = n_value
    if max_n is None:
        return None, None
    return max_n, compute_k_from_n(max_n)


def get_groups(window: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Partition sorted(window) into maximal blocks separated by gaps at least 2."""

    sorted_vals = sorted(window)
    groups: list[tuple[int, ...]] = []
    current = [sorted_vals[0]]
    for i in range(1, len(sorted_vals)):
        if sorted_vals[i] - sorted_vals[i - 1] <= 1:
            current.append(sorted_vals[i])
        else:
            groups.append(tuple(current))
            current = [sorted_vals[i]]
    groups.append(tuple(current))
    return groups


@lru_cache(maxsize=None)
def get_children_absolute(window: tuple[int, ...], k_limit: int) -> tuple[tuple[int, ...], ...]:
    """Generate absolute gap-expanded children with max value at most k_limit."""

    extra = k_limit - max(window)
    if extra < 0:
        return ()

    groups = get_groups(window)
    num_gaps = len(groups) + 1
    children = set()

    def gen_compositions(remaining: int, num_parts: int, current: tuple[int, ...] = ()):
        if num_parts == 1:
            yield current + (remaining,)
            return
        for part in range(remaining + 1):
            yield from gen_compositions(remaining - part, num_parts - 1, current + (part,))

    for composition in gen_compositions(extra, num_gaps):
        cumulative_shift = 0
        group_shifts = []
        for gap_index in range(len(groups)):
            cumulative_shift += composition[gap_index]
            group_shifts.append(cumulative_shift)

        value_map = {}
        for group_index, group in enumerate(groups):
            for value in group:
                if value not in value_map:
                    value_map[value] = value + group_shifts[group_index]

        children.add(tuple(value_map[value] for value in window))

    return tuple(sorted(children))


def gen_partitions(total: int, max_parts: int, max_val: int):
    """Yield partitions of exactly total with <= max_parts parts in [1,max_val]."""

    if total == 0:
        yield ()
        return
    if max_parts == 0 or max_val <= 0:
        return
    for first in range(min(total, max_val), 0, -1):
        for rest in gen_partitions(total - first, max_parts - 1, first):
            yield (first,) + rest


def gen_partitions_upto(max_total: int, max_parts: int, max_val: int):
    """Yield partitions with total <= max_total and bounded length/value."""

    yield ()
    if max_total <= 0 or max_parts <= 0 or max_val <= 0:
        return
    for total in range(1, max_total + 1):
        yield from gen_partitions(total, max_parts, max_val)


@lru_cache(maxsize=None)
def cached_partitions_upto(max_total: int, max_parts: int, max_val: int) -> tuple[tuple[int, ...], ...]:
    """Cached tuple form of gen_partitions_upto."""

    return tuple(gen_partitions_upto(max_total, max_parts, max_val))


def compute_defc_and_area(seq: list[int]) -> tuple[int, int]:
    """Compute defc=binom(n,2)-area-dinv and area=sum(seq)."""

    dinv = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j] or seq[i] == seq[j] + 1:
                dinv += 1
    area = sum(seq)
    return comb(len(seq), 2) - area - dinv, area


@lru_cache(maxsize=None)
def m_max_for_n(n_value: int) -> int:
    """Largest m satisfying C(m,2) <= floor(C(n,2)/2)."""

    half = comb(n_value, 2) // 2
    value = 0
    while comb(value + 1, 2) <= half:
        value += 1
    return value


@lru_cache(maxsize=None)
def first_n_with_m_allowed(m_value: int) -> int:
    """Smallest n>=8 for which m satisfies the prefix area bound."""

    n_value = 8
    while m_value > m_max_for_n(n_value):
        n_value += 1
    return n_value


def deficit_n_upper(
    coeff: int,
    m_value: int,
    int_defc: int,
    q0: int,
    n_limit: int,
) -> int:
    """Largest n that can survive the deficit lower bound with q'=0."""

    numerator = coeff * m_value + 8 * coeff - 8 - int_defc - q0
    if coeff == 2:
        return n_limit
    return min(n_limit, numerator // (coeff - 2))


def check_window_single(
    *,
    case_label: str,
    side_label: str,
    base_window: tuple[int, ...],
    child: tuple[int, ...],
    id_val: int,
    n_value: int,
    m_value: int,
    g_value: int,
    coeff: int,
    int_defc_q0: tuple[int, int],
    child_area: int,
) -> dict | None:
    """Return first counterexample for one child/n/m triple, if any."""

    target_defc = 2 * n_value - 8
    total_free = n_value - m_value - 8
    if total_free < 0:
        return None

    int_defc, q0 = int_defc_q0
    q_prime_max = target_defc - int_defc - q0 - coeff * total_free
    if q_prime_max < 0:
        return None

    max_part = max(0, m_value - 1)
    prefix = list(range(m_value + 1))
    prefix_area = comb(m_value + 1, 2)
    m_repeats = [m_value]
    window_list = list(child)
    m_choose = comb(n_value, 2)

    for repeat_count in range(total_free + 1):
        if m_value == 0 and repeat_count < total_free:
            continue

        middle_len = total_free - repeat_count
        base_area = prefix_area + repeat_count * m_value + child_area
        max_partition_sum = min(q_prime_max, middle_len * max_part)
        min_possible_area = base_area + middle_len * (m_value - 1) - max_partition_sum
        if 2 * min_possible_area > m_choose - 8:
            continue

        for partition in cached_partitions_upto(q_prime_max, middle_len, max_part):
            extended = list(partition) + [0] * (middle_len - len(partition))
            middle = [m_value - 1 - deficit for deficit in reversed(extended)]
            seq = prefix + m_repeats * repeat_count + middle + window_list
            defc, area = compute_defc_and_area(seq)

            if defc > target_defc:
                continue
            if 2 * area > m_choose - defc - 8:
                continue

            return {
                "case": case_label,
                "side": side_label,
                "base_window": base_window,
                "child": child,
                "id": id_val,
                "n": n_value,
                "m": m_value,
                "g": g_value,
                "coeff": coeff,
                "repeat_count": repeat_count,
                "middle_len": middle_len,
                "partition": partition,
                "prefix": prefix + m_repeats * repeat_count + middle,
                "seq": seq,
                "defc": defc,
                "area": area,
                "target_defc": target_defc,
            }

    return None


def compare_threshold_table(
    label: str,
    computed: dict[int, tuple[int | None, int | None]],
    expected: dict[int, tuple[int | None, int | None]],
) -> bool:
    """Print an exact threshold table comparison."""

    mismatches = []
    for id_val in sorted(expected):
        if computed.get(id_val) != expected[id_val]:
            mismatches.append((id_val, computed.get(id_val), expected[id_val]))

    if not mismatches:
        print(f"{label} threshold table comparison: MATCH")
        return True

    print(f"{label} threshold table comparison: MISMATCH")
    for id_val, got, want in mismatches:
        print(f"  id={id_val}: computed={got}, expected={want}")
    return False


def print_table(label: str, table: dict[int, tuple[int | None, int | None]]) -> None:
    """Print a threshold table."""

    print(label)
    print(f"{'id':>4} {'N':>8} {'K':>8}")
    for id_val in sorted(table):
        n_value, k_value = table[id_val]
        n_text = "--" if n_value is None else str(n_value)
        k_text = "--" if k_value is None else str(k_value)
        print(f"{id_val:>4} {n_text:>8} {k_text:>8}")
    print()


def build_threshold_table(case_num: int) -> dict[int, tuple[int | None, int | None]]:
    """Build the threshold table for one case."""

    if case_num == 1:
        return {id_val: compute_nk_case1(id_val) for id_val in range(10, 22)}
    return {id_val: compute_nk_case2(id_val) for id_val in range(0, 22)}


def verify_id_mid_bound(windows: dict[str, set[tuple[int, ...]]]) -> bool:
    """Verify id_mid(w)>=10 over EW union WW."""

    min_record = None
    distribution: dict[int, int] = {}
    for suffix_len, side_label, side_windows in (
        (3, "East", windows["East"]),
        (4, "West", windows["West"]),
    ):
        for window in side_windows:
            id_val, threshold = compute_id_mid(window, suffix_len)
            distribution[id_val] = distribution.get(id_val, 0) + 1
            if min_record is None or id_val < min_record[0]:
                min_record = (id_val, threshold, side_label, window)

    assert min_record is not None
    ok = min_record[0] >= 10
    print(
        "id_mid structural check over EW union WW: "
        f"{'PASS' if ok else 'FAIL'} (min id_mid={min_record[0]}, "
        f"threshold={min_record[1]}, side={min_record[2]}, window={min_record[3]})"
    )
    print(f"id_mid distribution: {dict(sorted(distribution.items()))}\n")
    return ok


def id_from_table(
    id_val: int,
    table: dict[int, tuple[int | None, int | None]],
    *,
    case_label: str,
    side_label: str,
    window: tuple[int, ...],
) -> tuple[int | None, int | None]:
    """Look up an id without clamping; reject unexpected values."""

    if id_val not in table:
        raise ValueError(
            f"Unexpected id in {case_label} {side_label}: id={id_val}, window={window}"
        )
    return table[id_val]


def run_case(
    *,
    case_num: int,
    side_label: str,
    windows: set[tuple[int, ...]],
    table: dict[int, tuple[int | None, int | None]],
) -> tuple[list[dict], dict[str, int]]:
    """Run one finite case."""

    case_label = f"Case {case_num}"
    problems = []
    suffix_len = 3 if side_label == "East" else 4
    windows_checked = 0
    children_generated = 0
    active_children = 0
    triples_checked = 0

    for base_window in sorted(windows):
        windows_checked += 1
        if case_num == 1:
            id_val, _ = compute_id_mid(base_window, suffix_len)
        else:
            id_val = compute_id_base(base_window, suffix_len)

        n_limit, k_limit = id_from_table(
            id_val,
            table,
            case_label=case_label,
            side_label=side_label,
            window=base_window,
        )
        if n_limit is None or k_limit is None:
            continue

        children = get_children_absolute(base_window, k_limit)
        children_generated += len(children)
        for child in children:
            child_has_checked_triple = False
            child_area = sum(child)
            fourth_largest = sorted(child, reverse=True)[3]
            if case_num == 1:
                m_start = max(0, child[0] - 1, child[6] - 1, fourth_largest)
                m_stop = m_max_for_n(n_limit)
            else:
                m_start = max(0, child[0] - 1, child[6] - 1)
                m_stop = min(m_max_for_n(n_limit), fourth_largest - 1)

            if m_start > m_stop:
                continue

            for m_value in range(m_start, m_stop + 1):
                g_value = sum(1 for value in child if value > m_value)
                if case_num == 1:
                    if g_value > 3:
                        continue
                    coeff = 3
                else:
                    if g_value < 4:
                        continue
                    coeff = g_value

                stats = window_stats(child, m_value, suffix_len)
                n_start = max(8, m_value + 8, first_n_with_m_allowed(m_value))
                n_stop = deficit_n_upper(coeff, m_value, stats[0], stats[1], n_limit)
                if n_start > n_stop:
                    continue

                for n_value in range(n_start, n_stop + 1):
                    triples_checked += 1
                    child_has_checked_triple = True
                    problem = check_window_single(
                        case_label=case_label,
                        side_label=side_label,
                        base_window=base_window,
                        child=child,
                        id_val=id_val,
                        n_value=n_value,
                        m_value=m_value,
                        g_value=g_value,
                        coeff=coeff,
                        int_defc_q0=stats,
                        child_area=child_area,
                    )
                    if problem is not None:
                        problems.append(problem)
                        print_first_failure(problem)
                        return problems, {
                            "windows": windows_checked,
                            "children": children_generated,
                            "active_children": active_children,
                            "triples": triples_checked,
                        }

            if child_has_checked_triple:
                active_children += 1

    counts = {
        "windows": windows_checked,
        "children": children_generated,
        "active_children": active_children,
        "triples": triples_checked,
    }
    print(
        f"{case_label} {side_label}: windows={windows_checked}, "
        f"children={children_generated}, active_children={active_children}, "
        f"triples={triples_checked}, problems={len(problems)}"
    )
    return problems, counts


def print_first_failure(problem: dict) -> None:
    """Print the first failed obligation."""

    print("FIRST FAILURE")
    for key in (
        "case",
        "side",
        "base_window",
        "child",
        "id",
        "n",
        "m",
        "g",
        "coeff",
        "repeat_count",
        "middle_len",
        "partition",
        "prefix",
        "seq",
        "defc",
        "area",
        "target_defc",
    ):
        print(f"  {key}: {problem[key]}")


def compare_counts(counts_by_case: dict[tuple[str, str], dict[str, float | int]]) -> bool:
    """Compare finite-search counts with the expected finite-check counts."""

    all_match = True
    print("\nExpected finite-count comparison:")
    for key, expected in EXPECTED_FINITE_COUNTS.items():
        got = counts_by_case[key]
        got_pair = {"children": int(got["children"]), "triples": int(got["triples"])}
        if got_pair == expected:
            print(f"  {key[0]} {key[1]}: MATCH {got_pair}")
        else:
            all_match = False
            print(f"  {key[0]} {key[1]}: MISMATCH got={got_pair}, expected={expected}")

    if not all_match:
        print(
            "  Count note: children are absolute generated children for finite "
            "table rows; triples are finite (child,n,m) checks after actual-g "
            "deficit pruning."
        )
    print()
    return all_match


def main() -> None:
    """Run the East7-West7 seven-window checker."""

    ew = get_ew()
    ww = get_ww(ew)
    ew_ww = ew | ww
    print(f"  |EW| = {len(ew)}, |WW| = {len(ww)}, |EW union WW| = {len(ew_ww)}\n")

    case1_table = build_threshold_table(case_num=1)
    case2_table = build_threshold_table(case_num=2)
    print_table("Case 1 threshold table", case1_table)
    print_table("Case 2 threshold table", case2_table)

    table_results = [
        compare_threshold_table("Case 1", case1_table, EXPECTED_CASE1_TABLE),
        compare_threshold_table("Case 2", case2_table, EXPECTED_CASE2_TABLE),
    ]
    print()

    id_mid_ok = verify_id_mid_bound({"East": ew, "West": ww})

    all_problems = []
    counts_by_case: dict[tuple[str, str], dict[str, float | int]] = {}

    for case_num, side_label, windows, table in (
        (1, "East", ew, case1_table),
        (1, "West", ww, case1_table),
        (2, "East", ew, case2_table),
        (2, "West", ww, case2_table),
    ):
        problems, counts = run_case(
            case_num=case_num,
            side_label=side_label,
            windows=windows,
            table=table,
        )
        all_problems.extend(problems)
        counts_by_case[(f"Case {case_num}", side_label)] = counts

    counts_match = compare_counts(counts_by_case)

    tables_ok = all(table_results)
    if tables_ok:
        print("Threshold-table checks: MATCH")
    else:
        print("Threshold-table checks: MISMATCH")

    if id_mid_ok:
        print("id_mid>=10 check: PASS")
    else:
        print("id_mid>=10 check: FAIL")

    if tables_ok and id_mid_ok and not all_problems:
        if not counts_match:
            print("Counts differ from expected finite counts; see comparison above.")
        print("SUCCESS: East7/West7 seven-window verification passed.")
        return

    print(f"FAILED: problems={len(all_problems)}, tables_ok={tables_ok}, id_mid_ok={id_mid_ok}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()

```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/04_east7_west7_successful_output.txt`

```text
  |EW| = 7194, |WW| = 7194, |EW union WW| = 14388

Case 1 threshold table
  id        N        K
  10       33       23
  11       26       18
  12       16       11
  13        9        6
  14       --       --
  15       --       --
  16       --       --
  17       --       --
  18       --       --
  19       --       --
  20       --       --
  21       --       --

Case 2 threshold table
  id        N        K
   0       26       18
   1       23       16
   2       23       16
   3       20       14
   4       20       14
   5       19       13
   6       17       12
   7       16       11
   8       16       11
   9       13        9
  10       13        9
  11       12        8
  12       10        7
  13        9        6
  14        9        6
  15       --       --
  16       --       --
  17       --       --
  18       --       --
  19       --       --
  20       --       --
  21       --       --

Case 1 threshold table comparison: MATCH
Case 2 threshold table comparison: MATCH

id_mid structural check over EW union WW: PASS (min id_mid=10, threshold=1, side=East, window=(1, 2, 3, 4, 1, 1, 0))
id_mid distribution: {10: 6, 11: 24, 12: 157, 13: 359, 14: 838, 15: 1378, 16: 1875, 17: 2670, 18: 2854, 19: 2559, 20: 1392, 21: 276}

Case 1 East: windows=7194, children=2473, active_children=1087, triples=9919, problems=0
Case 1 West: windows=7194, children=2911, active_children=1225, triples=10311, problems=0
Case 2 East: windows=7194, children=3860, active_children=456, triples=715, problems=0
Case 2 West: windows=7194, children=4827, active_children=1183, triples=1756, problems=0

Expected finite-count comparison:
  Case 1 East: MATCH {'children': 2473, 'triples': 9919}
  Case 1 West: MATCH {'children': 2911, 'triples': 10311}
  Case 2 East: MATCH {'children': 3860, 'triples': 715}
  Case 2 West: MATCH {'children': 4827, 'triples': 1756}

Threshold-table checks: MATCH
id_mid>=10 check: PASS
SUCCESS: East7/West7 seven-window verification passed.
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/05_lemma_525_limited_nonzero_checker.py`

```python
from collections import Counter
from math import comb
N_MIN, N_MAX = 4, 13
MAX_NONZERO = 7

def require(test, message):
    if not test:
        raise AssertionError(message)

def nonzero_count(S):
    return sum(1 for x in S if x != 0)

def ell_value(n, d):
    return (comb(n, 2) - d) // 2

def check_image(source, image, n, d, delta):
    require(is_Dyck(image), f"non-Dyck image: {source} -> {image}")
    require(len(image) == n, f"length changed: {source} -> {image}")
    require(defc(image) == d, f"deficit changed: {source} -> {image}")
    require(area(image) == area(source) + delta,
            f"wrong area change: {source} -> {image}")

def checked_up(S, n, d, ell):
    S = tuple(S)
    if S == omega(n):
        image = epsilon(n)
        check_image(S, image, n, d, 1)
        return "up special", 3
    if is_full_skeleton(S):
        image = inject(S[:-1], S[-1] + 1)
        check_image(S, image, n, d, 1)
        return "up skeleton", 3
    j1, e1 = find_extractable(S)
    C1 = remove_at(S, j1)
    sigma1 = C1 + (e1 - 1,)
    if East3(sigma1[-3:]) is not None:
        require(j1 < n - 2, f"up East3 position bound: {S}")
        image = inject_right_to_left(sigma1[:-2],
                                     (sigma1[-2] + 1, sigma1[-1] + 1))
        check_image(S, image, n, d, 1)
        return "up East3", 3
    j2, e2 = find_extractable(C1)
    C2 = remove_at(C1, j2)
    sigma2 = C2 + (e1 - 1, e2 - 1)
    E5 = East5(sigma2[-5:])
    if E5 is not None:
        require(j1 < n - 3 and j2 < len(C1) - 3,
                f"up East5 position bound: {S}")
        base = sigma2[:-5] + E5[:2]
        image = inject_right_to_left(base, tuple(x + 1 for x in E5[2:]))
        check_image(S, image, n, d, 1)
        return "up East5", 5
    j3, e3 = find_extractable(C2)
    C3 = remove_at(C2, j3)
    sigma3 = C3 + (e1 - 1, e2 - 1, e3 - 1)
    W7 = sigma3[-7:]
    require(not is_far_apart_decomposable(W7), f"bad East7 window: {S}")
    require(j1 < n - 3 and j2 < len(C1) - 3 and j3 < len(C2) - 3,
            f"up East7 position bound: {S}")
    E7 = East7(W7)
    image = inject_right_to_left(sigma3[:-7] + E7[:-4],
                                 tuple(x + 1 for x in E7[-4:]))
    check_image(S, image, n, d, 1)
    return "up East7", 7

def checked_down(S, n, d, ell):
    S = tuple(S)
    if S == epsilon(n):
        image = omega(n)
        check_image(S, image, n, d, -1)
        return "down special", 3
    j1, f1 = find_extractable(S)
    D1 = remove_at(S, j1)
    candidate = D1 + (f1 - 1,)
    if find_extractable(candidate) is None:
        check_image(S, candidate, n, d, -1)
        return "down skeleton", 3
    j2, f2 = find_extractable(D1)
    D2 = remove_at(D1, j2)
    tau1 = D2 + (f1 - 1, f2 - 1)
    if West3(tau1[-3:]) is not None:
        require(j1 < n - 1 and j2 < len(D1) - 1,
                f"down West3 position bound: {S}")
        image = inject(tau1[:-1], tau1[-1] + 1)
        check_image(S, image, n, d, -1)
        return "down West3", 3
    j3, f3 = find_extractable(D2)
    D3 = remove_at(D2, j3)
    tau2 = D3 + (f1 - 1, f2 - 1, f3 - 1)
    W5 = West5(tau2[-5:])
    if W5 is not None:
        require(j1 < n - 2 and j2 < len(D1) - 2 and j3 < len(D2) - 2,
                f"down West5 position bound: {S}")
        base = tau2[:-5] + W5[:3]
        image = inject_right_to_left(base, tuple(x + 1 for x in W5[3:]))
        check_image(S, image, n, d, -1)
        return "down West5", 5
    j4, f4 = find_extractable(D3)
    D4 = remove_at(D3, j4)
    tau3 = D4 + (f1 - 1, f2 - 1, f3 - 1, f4 - 1)
    W7 = tau3[-7:]
    require(not is_far_apart_decomposable(W7), f"bad West7 window: {S}")
    require(j1 < n - 2 and j2 < len(D1) - 2
            and j3 < len(D2) - 2 and j4 < len(D3) - 2,
            f"down West7 position bound: {S}")
    E7 = West7(W7)
    image = inject_right_to_left(tau3[:-7] + E7[:-3],
                                 tuple(x + 1 for x in E7[-3:]))
    check_image(S, image, n, d, -1)
    return "down West7", 7

def run_limited_nonzero_checker():
    generated = {}
    eligible = Counter()
    branches = Counter()
    levels = Counter()
    failures = []
    for n in range(N_MIN, N_MAX + 1):
        seqs = [S for S in generate_Dycks(n) if nonzero_count(S) <= MAX_NONZERO]
        generated[n] = len(seqs)
        for S in seqs:
            d = defc(S)
            if d > 2 * n - 8:
                continue
            ell = ell_value(n, d)
            try:
                if area(S) < ell:
                    branch, level = checked_up(S, n, d, ell)
                    eligible[(n, "up")] += 1
                    branches[("up", branch)] += 1
                    levels[("up", level)] += 1
                if area(S) <= ell and not is_special_skeleton(S):
                    branch, level = checked_down(S, n, d, ell)
                    eligible[(n, "down")] += 1
                    branches[("down", branch)] += 1
                    levels[("down", level)] += 1
            except Exception as exc:
                failures.append((n, S, str(exc)))
    require(not failures, f"first failure: {failures[0] if failures else None}")
    up_total = sum(v for (n, direction), v in eligible.items()
                   if direction == "up")
    down_total = sum(v for (n, direction), v in eligible.items()
                     if direction == "down")
    print("generated by n:", generated)
    print("eligible up calls:", up_total)
    print("eligible down calls:", down_total)
    print("eligible calls by n/direction:", dict(sorted(eligible.items())))
    print("branches:", dict(sorted(branches.items())))
    print("levels:", dict(sorted(levels.items())))
    print("position-bound or image failures:", len(failures))
    print("status: PASS")
run_limited_nonzero_checker()
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/06_lemma_525_limited_nonzero_successful_output.txt`

```text
generated by n: {4: 14, 5: 42, 6: 132, 7: 429, 8: 1430,
                 9: 3432, 10: 7072, 11: 13260,
                 12: 23256, 13: 38760}
eligible up calls: 11879
eligible down calls: 9486
position-bound or image failures: 0
status: PASS
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/07_lemma_525_prefix_checker.py`

```python
from collections import Counter
from itertools import product
from math import comb
N_MIN, N_MAX = 9, 16
EXPECTED = {
    (9, 1, "pq_lt_4"): 504, (9, 1, "pq_eq_4"): 3024,
    (10, 1, "pq_lt_4"): 720, (10, 1, "pq_eq_4"): 5040,
    (11, 1, "pq_lt_4"): 990, (11, 1, "pq_eq_4"): 7920,
    (12, 1, "pq_lt_4"): 1320, (12, 1, "pq_eq_4"): 11880,
    (13, 1, "pq_lt_4"): 1716, (13, 1, "pq_eq_4"): 17160,
    (14, 1, "pq_lt_4"): 2184, (14, 1, "pq_eq_4"): 24024,
    (15, 1, "pq_lt_4"): 2730, (15, 1, "pq_eq_4"): 32760,
    (16, 1, "pq_lt_4"): 3360, (16, 1, "pq_eq_4"): 43680,
    (9, 2, "pq_lt_4"): 336, (9, 2, "pq_eq_4"): 1680,
    (10, 2, "pq_lt_4"): 504, (10, 2, "pq_eq_4"): 3024,
    (11, 2, "pq_lt_4"): 720, (11, 2, "pq_eq_4"): 5040,
    (12, 2, "pq_lt_4"): 990, (12, 2, "pq_eq_4"): 7920,
    (13, 2, "pq_lt_4"): 1320, (13, 2, "pq_eq_4"): 11880,
    (14, 2, "pq_lt_4"): 1716, (14, 2, "pq_eq_4"): 17160,
    (15, 2, "pq_lt_4"): 2184, (15, 2, "pq_eq_4"): 24024,
    (16, 2, "pq_lt_4"): 2730, (16, 2, "pq_eq_4"): 32760,
}

def require(test, message):
    if not test:
        raise AssertionError(message)

def bounded_product(bounds):
    return product(*(range(bound + 1) for bound in bounds))

def defc(word):
    n = len(word)
    dinv_count = sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        if word[i] == word[j] or word[i] == word[j] + 1
    )
    return comb(n, 2) - area(word) - dinv_count

def claim_words(n, claim, subcase):
    if claim == 1 and subcase == "pq_lt_4":
        prefix = tuple(range(0, n - 3))
        bounds = (n - 3, n - 2, n - 1)
    elif claim == 1 and subcase == "pq_eq_4":
        prefix = tuple(range(0, n - 4))
        bounds = (n - 4, n - 3, n - 2, n - 1)
    elif claim == 2 and subcase == "pq_lt_4":
        prefix = (0,) + tuple(range(0, n - 4))
        bounds = (n - 4, n - 3, n - 2)
    elif claim == 2 and subcase == "pq_eq_4":
        prefix = (0,) + tuple(range(0, n - 5))
        bounds = (n - 5, n - 4, n - 3, n - 2)
    else:
        raise ValueError("unknown claim/subcase")
    for stars in bounded_product(bounds):
        yield prefix + stars

def run_prefix_checker():
    counts = Counter()
    failures = []
    for n in range(N_MIN, N_MAX + 1):
        M = comb(n, 2)
        for claim in (1, 2):
            for subcase in ("pq_lt_4", "pq_eq_4"):
                # In the p+q=4 boundary this is q+1 for up (2,2)
                # and q for down (1,3).
                adjustment = 3 if subcase == "pq_eq_4" else 0
                for word in claim_words(n, claim, subcase):
                    counts[(n, claim, subcase)] += 1
                    D = defc(word)
                    A = area(word)
                    deficit_contradiction = D > 2 * n - 8
                    area_contradiction = 2 * A > M - D - 2 * adjustment
                    if not (deficit_contradiction or area_contradiction):
                        failures.append((n, claim, subcase, word, D, A))
    require(dict(counts) == EXPECTED, "word counts do not match")
    require(not failures, f"first failure: {failures[0] if failures else None}")
    print("counts by n/claim/subcase:", dict(sorted(counts.items())))
    print("failures:", len(failures))
    print("status: PASS")
run_prefix_checker()
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/08_lemma_525_prefix_successful_output.txt`

```text
failures: 0
status: PASS
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/README.md`

```markdown
# Code

This directory contains the code listings from Appendix A and Appendix B of the
2026 Dyck symmetric functions preprint.

## Purpose

These scripts package the finite computations used in the appendices of the
preprint. Appendix A contains reusable Dyck-sequence routines and string
generation code. Appendix B contains exhaustive finite checkers used in the
local well-definedness proofs for the skeleton string construction.

## Dependencies

Python 3 with the standard library only.

Run scripts with ordinary assertion checking enabled. Do not use Python's
optimized mode, because `assert` statements are part of the verification.

## Inputs

The checkers have no external data input. Each script enumerates its stated
finite domain internally.

## Outputs

Successful runs print count summaries and final success lines. The expected
successful-output transcripts for the Appendix B checkers are stored beside
the scripts as `.txt` files when the appendix includes such a transcript.

## Appendix A

`appendix_a/01_core_dyck_sequence_routines.py` is the core Dyck-sequence code
from Appendix A.

`appendix_a/02_make_strings.py` is the Appendix A routine that builds the
lower-half string decomposition from the core routines.

These two files are appendix listings. They are kept here because they appear
in Appendix A.

Command:

````text
python run_appendix_listing.py appendix_a/02_make_strings.py
````

The wrapper prepends the core routines before running this listing. This
routine returns the lower-half strings for requested parameters when called
from Python; it is included mainly as appendix code rather than as a command
line report.

## Appendix B

`appendix_b/01_residual_finite_check.py` is the finite checker for the small
residual range in the local well-definedness proof.

`appendix_b/03_east7_west7_seven_window_checker.py` is the finite checker for
the seven-entry East/West local move.

`appendix_b/05_lemma_525_limited_nonzero_checker.py` is the limited-nonzero
finite checker for Lemma 5.25.

`appendix_b/07_lemma_525_prefix_checker.py` is the finite checker for the two
prefix forms excluded in the proof of Lemma 5.25.

The `.txt` files in `appendix_b/` are the successful-output listings printed in
the appendix.

Some Appendix B listings rely on routines defined earlier in Appendix A. To run
the listings without editing them, use:

````text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
````

## Range Checked

`appendix_b/01_residual_finite_check.py` enumerates Dyck sequences of lengths
`4 <= n <= 7` satisfying the paper's deficit and area hypotheses for the
residual local-lemma branches.

`appendix_b/03_east7_west7_seven_window_checker.py` enumerates the finite
East7 and West7 seven-entry window domains and their bounded absolute children
after the paper's threshold reductions.

`appendix_b/05_lemma_525_limited_nonzero_checker.py` checks all Dyck sequences
with `4 <= n <= 13` and at most seven nonzero entries satisfying the fixed
deficit and area hypotheses.

`appendix_b/07_lemma_525_prefix_checker.py` checks the two excluded prefix
forms in the range `9 <= n <= 16`.

## Runtime

On the current local machine, each Appendix B checker completed in a few
seconds or less on June 13, 2026. Runtime may vary, but no external packages or
cached data are required.

## Interpretation

The computations are finite exhaustive verifications after the written proof
reduces the relevant obligations to bounded domains. They should be read as
proof-supporting appendix checks for those domains, not as broad experimental
evidence for statements outside the stated ranges.

## Limitations

The scripts verify exactly the finite obligations encoded in the appendix
listings. They do not independently reprove the symbolic reductions in the
paper, and they should be rechecked if the corresponding preprint statements,
definitions, or ranges change.
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/code/run_appendix_listing.py`

```python
"""Run an extracted appendix listing with the Appendix A routines loaded.

The extracted listings are kept unchanged. This runner supplies the shared
namespace that the paper has implicitly across appendix code blocks.
"""

from pathlib import Path
import argparse


APPENDIX_A_FILES = (
    "appendix_a/01_core_dyck_sequence_routines.py",
    "appendix_a/02_make_strings.py",
)


def exec_file(path, namespace):
    source = path.read_text(encoding="ascii")
    exec(compile(source, str(path), "exec"), namespace)


def main():
    parser = argparse.ArgumentParser(description="Run an extracted appendix listing.")
    parser.add_argument("listing", help="path to the listing, relative to code/")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    namespace = {"__name__": "__main__"}
    for relative_path in APPENDIX_A_FILES:
        exec_file(here / relative_path, namespace)
    exec_file(here / args.listing, namespace)


if __name__ == "__main__":
    main()
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 92378
sha256: 931f87d4d7e62498edc0414d5a0bfaa1ba0be0ce9649c8d674a9704db7ceb7b8
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}
\usepackage{array}
\usepackage{url}

\title{Finite Computations in the Dyck Symmetric Functions Appendices}
\author{}
\date{}

\begin{document}
\emergencystretch=3em
\maketitle

\section{What the Appendix Code Supports}

The 2026 preprint proves a string decomposition for Dyck sequences in a range
of deficits. The construction uses two local operations, called
\(\mathrm{up}\) and \(\mathrm{down}\), which move a Dyck sequence one step in
area while preserving the relevant deficit. These operations are defined by
looking for a small local pattern, removing a few entries, changing a short
East or West window, and then reinserting the changed entries.

Most of the proof is symbolic: it shows that the operations preserve the Dyck
condition, preserve the deficit, and stay inside the intended range. The
appendix computations handle finite parts of this argument where the proof has
reduced the problem to checking all possible short windows or all possible
small residual inputs.

\section{Appendix A}

Appendix A gives reusable code for Dyck sequences. It defines the basic
statistics, the skeleton tests, the insertion and extraction routines, and the
local \(\mathrm{up}\) and \(\mathrm{down}\) maps. It also gives the routine
that starts from the special skeletons and repeatedly applies
\(\mathrm{up}\) to form the lower half of each string.

The Appendix A code is included here because it is the computational form of
the construction itself. It can be used to reproduce examples of the strings
and to check small cases of the decomposition.

In this repository, Appendix A is represented by the following files in
\path{code/appendix_a/}:
\begin{itemize}
\item \path{01_core_dyck_sequence_routines.py}: the
basic Dyck-sequence routines and the definitions of the local
\(\mathrm{up}\) and \(\mathrm{down}\) algorithms.
\item \path{02_make_strings.py}: the Appendix A routine
that builds the lower-half strings from the special skeletons.
\end{itemize}

\section{Appendix B}

Appendix B proves that the local operations used in Appendix A are
well-defined in the range needed by the theorem. In the arXiv version, the
four local lemmas are Lemmas 5.22--5.25:
\begin{center}
\begin{tabular}{>{\raggedright\arraybackslash}p{0.18\linewidth}
                >{\raggedright\arraybackslash}p{0.34\linewidth}
                >{\raggedright\arraybackslash}p{0.34\linewidth}}
Lemma & Title & Role \\
\hline
5.22 & Skeleton cases succeed & Checks that the skeleton branches return Dyck
sequences in the required range. \\
5.23 & Extraction chains never fail & Checks that every extraction requested
by the staged algorithms exists. \\
5.24 & The seven-window branches do not fail & Checks the final seven-entry
East and West local moves. \\
5.25 & Bounded extraction positions and injection nonfailure & Checks the
position bounds needed for later insertion steps. \\
\end{tabular}
\end{center}

These lemmas check four basic points:
\begin{itemize}
\item when the construction recognizes a skeleton case, the proposed output is
again a Dyck sequence of the required form;
\item when the construction needs to remove entries, the entries it asks for
actually exist;
\item when the construction reaches the seven-entry East or West move, every
possible short window satisfies the inequalities needed by the proof;
\item the positions used for later insertion steps stay within the allowed
bounds.
\end{itemize}

The symbolic proof handles the infinite families. The finite computations in
Appendix B close the remaining cases.

\subsection{Residual Small Range}

One checker enumerates the remaining small values \(4\le n\le 7\). For each
Dyck sequence in that finite range, it follows the decision steps used by the
\(\mathrm{up}\) and \(\mathrm{down}\) algorithms and confirms that each input
falls into one of the cases already covered by the proof. It also confirms that
the seven-entry East and West moves are not reached in this small residual
range.

This corresponds to \path{01_residual_finite_check.py} in
\path{code/appendix_b/}. It supports the small-range parts of Lemmas 5.22,
5.23, 5.24, and 5.25 at once:
\begin{itemize}
\item for Lemma 5.22, it checks the skeleton branches in the residual range;
\item for Lemma 5.23, it checks that the extractions used before each branch
stops exist;
\item for Lemma 5.24, it confirms that the seven-window branch is not reached
for \(4\le n\le 7\);
\item for Lemma 5.25, it checks the relevant position bounds before the
residual branch stops.
\end{itemize}
The successful-output transcript is
\path{02_residual_successful_output.txt}.

\subsection{Seven-Entry East and West Windows}

The largest local move changes a window of seven entries. The proof reduces
this part to a finite list of possible East and West windows together with the
short extensions that can appear next to them. The checker enumerates those
windows and verifies the threshold inequalities used in the argument. This is
needed because the local move has several boundary cases that are easier and
less error-prone to exhaust by computation than to list manually in the text.

This corresponds to \path{03_east7_west7_seven_window_checker.py} in
\path{code/appendix_b/}. It is the finite checker for Lemma 5.24 in the
\(n\ge 8\) part of the proof. The successful-output transcript is
\path{04_east7_west7_successful_output.txt}.

\subsection{Position Bounds}

Another part of the proof needs to know that certain extraction and insertion
positions remain legal. Appendix B treats the general case symbolically and
then leaves two finite domains to check. The first finite checker covers words
with at most seven nonzero entries in the required range. The second covers two
specific prefix forms that are excluded from the symbolic argument. In both
cases, the code enumerates the finite domain and verifies that every word leads
to one of the contradictions or bounds used in the written proof.

These files correspond to Lemma 5.25:
\begin{itemize}
\item \path{05_lemma_525_limited_nonzero_checker.py}
checks the enlarged finite domain with \(4\le n\le 13\) and at most seven
nonzero entries. Its successful-output transcript is
\path{06_lemma_525_limited_nonzero_successful_output.txt}.
\item \path{07_lemma_525_prefix_checker.py} checks the
two excluded prefix forms in the finite range \(9\le n\le 16\). Its
successful-output transcript is
\path{08_lemma_525_prefix_successful_output.txt}.
\end{itemize}

\section{Why These Checks Are Included}

The computations are included because they are part of the proof, not just
evidence for the theorem. Each computation corresponds to a finite exhaustive
step that appears after the main argument has reduced an infinite statement to
a bounded list of cases. The appendix code records exactly what was checked,
and the successful-output listings record the expected result of those checks.
\end{document}
```

### `docs/items/dyck_symmetric_computer_assisted_proofs_2026/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dyck Symmetric Computer-Assisted Proofs 2026</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>Dyck Symmetric Computer-Assisted Proofs 2026</h1>
    <p>Proof-supporting appendix computations for arXiv:2605.13003; packaged checkers reproduce the successful finite verifications.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.pdf">View PDF</a></li>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This item records finite computations used as proof components in the 2026 preprint on Dyck symmetric functions.</p>

<p>The code files are extracted from Appendix A and Appendix B. Appendix A contains the reusable Dyck-sequence routines and the routine that builds lower-half strings. Appendix B contains the finite checkers used in the local well-definedness proof: the small residual range, the seven-entry East/West window check, and the two finite checks used for the position-bound lemma.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 102145
sha256: 8d81d52b5b86f1b5e7de0d042a2cefc16bbd9f1e63acff14f44a849f9ef824f5
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1732
sha256: ed560e434486ee0888f9a2b03c72ef72bc54ba7c7c344393c352ca71d06c98e6
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 98466
sha256: 79442eeddd10eb9769de50767200e9645ec25922b31bb8689da5dc564d31c86c
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1738
sha256: 2e7a95962b64dda07e3ec4937ba05175b9abb3285817bec9ce46855508cd9f23
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 112565
sha256: be9ef8051f34d27b93a21c212d16263ad7780cab823c2583b4bd438ccf943167
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1738
sha256: f5738e83ec6a4759cd111fa83482e862b81e34495f3fb1183a7073b8c786d0e3
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization.cpython-314.pyc`

```text
[binary artifact not expanded]
size_bytes: 41219
sha256: ba3d6aeda90c332d70115f91c52085e6300a47e61a24b3cbb69b7a53cfc2c508
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 67829
sha256: 09b4fb597183459b543cae8482ff344a8b880e301a4b836419332ee0e99a3adc
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.2.nbc`

```text
[binary artifact not expanded]
size_bytes: 65598
sha256: 723d39ef3b4c2899381b3cccdb2e0c80eb7ff267974f7d7b8060e3a2c105aea9
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 3336
sha256: 2bb1e664d7f1a5e45b809e77cb27a637391b1b5c6fe52c490ce037e8a9125e45
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 81251
sha256: 03fee1b31b3fe09326696cff0308263e5ed3255db49aeb66507e2e4aad9ccf25
```

### `docs/items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1692
sha256: 09302bc46af31b781b8afb694d86e279680a59886532e936f50ac41cab322b50
```

### `docs/items/dyck_symmetric_functions/code/check_rational_dyck_generalization.py`

```python
"""Focused finite checks for the rational dual Dyck symmetric-function formula.

Input parameters are:

* ``t``: rational step;
* ``A``: alphabet size, using the alphabet ``{1, 2, ..., A}``;
* ``L``: maximum word length.

For every length ``1 <= l <= L`` the checker enumerates all words containing
``1``, groups them by multiset and rational dinv, verifies factor-length
symmetry across all positive compositions with the same underlying partition,
and compares the common factorization count with the Dyck-tableau Schur-side
prediction.
"""

from __future__ import annotations

import argparse
import os
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from multiprocessing import Pool
from typing import Iterable

try:
    import numpy as np
    from numba import njit, types
    from numba.typed import Dict
except ImportError:  # pragma: no cover - exercised only on minimal environments.
    np = None
    njit = None
    types = None
    Dict = None


Word = tuple[int, ...]
Composition = tuple[int, ...]
Partition = tuple[int, ...]
Shape = tuple[int, ...]
MultisetKey = int
PartitionMaskData = tuple[Partition, list[Composition], tuple[int, ...]]


@dataclass(frozen=True)
class CheckInput:
    step: int
    alphabet_size: int
    max_length: int
    workers: int = 0


@dataclass
class CheckResult:
    params: CheckInput
    words_generated: int = 0
    words_kept: int = 0
    multisets_checked: int = 0
    dinv_classes_checked: int = 0
    partition_classes_checked: int = 0
    compositions_checked: int = 0
    tableaux_checked: int = 0
    elapsed_seconds: float = 0.0


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dinv_pair(left: int, right: int, *, step: int) -> int:
    if left <= right:
        return max(0, left + step - right)
    return max(0, right + 1 + step - left)


def pair_dinv_table(params: CheckInput) -> tuple[tuple[int, ...], ...]:
    values = range(1, params.alphabet_size + 1)
    return tuple(tuple(dinv_pair(a, b, step=params.step) for b in values) for a in values)


if njit is not None:
    JIT_WORD_RECORD_KEY = types.UniTuple(types.uint64, 3)

    @njit(cache=True)
    def _jit_group_word_records(
        length: int,
        alphabet_size: int,
        pair_dinv_array: np.ndarray,
        base_powers: np.ndarray,
        dinv_limit: int,
        step: int,
        start_word: int,
        stop_word: int,
    ) -> tuple[np.ndarray, np.ndarray, int]:
        counts = np.empty(alphabet_size, dtype=np.int64)
        word = np.empty(length, dtype=np.int64)
        grouped = Dict.empty(key_type=JIT_WORD_RECORD_KEY, value_type=types.int64)
        words_kept = 0

        for encoded_word in range(start_word, stop_word):
            remaining = encoded_word
            has_one = False
            for position in range(length - 1, -1, -1):
                value_index = remaining % alphabet_size
                remaining //= alphabet_size
                word[position] = value_index
                if value_index == 0:
                    has_one = True
            if not has_one:
                continue

            for value_index in range(alphabet_size):
                counts[value_index] = 0

            dinv = 0
            required_dual_cuts = 0
            multiset_key = np.uint64(0)
            previous_index = 0
            for position in range(length):
                value_index = word[position]
                for earlier_index in range(alphabet_size):
                    dinv += counts[earlier_index] * pair_dinv_array[earlier_index, value_index]
                if position > 0:
                    if value_index <= previous_index + step:
                        required_dual_cuts |= 1 << (position - 1)
                previous_index = value_index
                counts[value_index] += 1
                multiset_key += base_powers[value_index]

            record_key = (multiset_key, np.uint64(dinv), np.uint64(required_dual_cuts))
            grouped[record_key] = grouped.get(record_key, 0) + 1
            words_kept += 1

        keys = np.empty((len(grouped), 3), dtype=np.uint64)
        values = np.empty(len(grouped), dtype=np.int64)
        index = 0
        for key, value in grouped.items():
            keys[index, 0] = key[0]
            keys[index, 1] = key[1]
            keys[index, 2] = key[2]
            values[index] = value
            index += 1
        return keys, values, words_kept

else:
    JIT_WORD_RECORD_KEY = None
    _jit_group_word_records = None


def effective_word_group_workers(params: CheckInput, *, length: int, words_generated: int) -> int:
    if _jit_group_word_records is None:
        return 1
    if params.workers < 0:
        raise AssertionError("workers must be non-negative")
    if params.workers > 0:
        return params.workers
    configured = os.environ.get("DYCK_CHECK_WORKERS")
    if configured:
        workers = int(configured)
        require(workers > 0, "DYCK_CHECK_WORKERS must be positive")
        return workers
    if words_generated < 50_000_000:
        return 1
    return min(os.cpu_count() or 1, 8)


def _jit_group_word_records_worker(
    args: tuple[int, int, tuple[tuple[int, ...], ...], int, int, int, int],
) -> tuple[np.ndarray, np.ndarray, int]:
    length, alphabet_size, pair_dinv, dinv_limit, step, start_word, stop_word = args
    base_powers = np.array([(length + 1) ** index for index in range(alphabet_size)], dtype=np.uint64)
    pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
    return _jit_group_word_records(
        length,
        alphabet_size,
        pair_dinv_array,
        base_powers,
        dinv_limit,
        step,
        start_word,
        stop_word,
    )


def partition_shapes(total_size: int) -> Iterable[Shape]:
    def rec(remaining: int, max_part: int, prefix: list[int]) -> Iterable[Shape]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for part in range(min(remaining, max_part), 0, -1):
            prefix.append(part)
            yield from rec(remaining - part, part, prefix)
            prefix.pop()

    yield from rec(total_size, total_size, [])


def positive_compositions(total: int) -> list[Composition]:
    if total <= 0:
        return []
    out: list[Composition] = []

    def rec(remaining: int, prefix: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for part in range(1, remaining + 1):
            prefix.append(part)
            rec(remaining - part, prefix)
            prefix.pop()

    rec(total, [])
    return out


def underlying_partition(composition: Composition) -> Partition:
    return tuple(sorted(composition, reverse=True))


def composition_cut_mask(composition: Composition) -> int:
    mask = 0
    position = 0
    total = sum(composition)
    for part in composition[:-1]:
        position += part
        if 0 < position < total:
            mask |= 1 << (position - 1)
    return mask


def composition_groups(length: int) -> list[PartitionMaskData]:
    grouped: defaultdict[Partition, list[tuple[Composition, int]]] = defaultdict(list)
    for composition in positive_compositions(length):
        grouped[underlying_partition(composition)].append((composition, composition_cut_mask(composition)))
    out: list[PartitionMaskData] = []
    for partition, values in grouped.items():
        compositions = [composition for composition, _cut_mask in values]
        cut_masks = tuple(cut_mask for _composition, cut_mask in values)
        out.append((partition, compositions, cut_masks))
    return out


def multiset_from_key(key: MultisetKey, *, alphabet_size: int, length: int) -> Word:
    base = length + 1
    values: list[int] = []
    for index in range(1, alphabet_size + 1):
        multiplicity = key % base
        key //= base
        values.extend([index] * multiplicity)
    return tuple(values)


def group_words_for_length(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> tuple[dict[MultisetKey, dict[int, Counter[int]]], int, int]:
    if _jit_group_word_records is not None:
        return group_words_for_length_jit(length, params=params, pair_dinv=pair_dinv)

    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
    words_generated = params.alphabet_size**length
    words_kept = 0
    base_powers = tuple((length + 1) ** index for index in range(params.alphabet_size))

    for first_one_position in range(length):
        counts = [0] * params.alphabet_size
        active_indices: list[int] = []

        def extend(
            position: int,
            previous_index: int,
            dinv: int,
            required_dual_cuts: int,
            multiset_key: int,
        ) -> None:
            nonlocal words_kept
            if position == length:
                grouped[multiset_key][dinv][required_dual_cuts] += 1
                words_kept += 1
                return

            if position < first_one_position:
                choices = range(1, params.alphabet_size)
            elif position == first_one_position:
                choices = range(1)
            else:
                choices = range(params.alphabet_size)

            for value_index in choices:
                dinv_increment = 0
                for earlier_index in active_indices:
                    dinv_increment += counts[earlier_index] * pair_dinv[earlier_index][value_index]
                next_required_dual_cuts = required_dual_cuts
                if position > 0:
                    previous_value = previous_index + 1
                    current_value = value_index + 1
                    if current_value <= previous_value + params.step:
                        next_required_dual_cuts |= 1 << (position - 1)
                first_value = counts[value_index] == 0
                if first_value:
                    active_indices.append(value_index)
                counts[value_index] += 1
                extend(
                    position + 1,
                    value_index,
                    dinv + dinv_increment,
                    next_required_dual_cuts,
                    multiset_key + base_powers[value_index],
                )
                counts[value_index] -= 1
                if first_value:
                    active_indices.pop()

        extend(0, 0, 0, 0, 0)

    expected_kept = words_generated - (params.alphabet_size - 1) ** length
    require(words_kept == expected_kept, f"internal word-count mismatch for length {length}")
    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}, words_generated, words_kept


def group_words_for_length_jit(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> tuple[dict[MultisetKey, dict[int, Counter[int]]], int, int]:
    require(np is not None, "NumPy is required for the JIT word-grouping backend")
    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
    words_generated = params.alphabet_size**length
    max_pair_dinv = max(max(row) for row in pair_dinv)
    dinv_limit = max_pair_dinv * length * (length - 1) // 2 + 1
    base_powers = np.array([(length + 1) ** index for index in range(params.alphabet_size)], dtype=np.uint64)
    pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
    workers = effective_word_group_workers(params, length=length, words_generated=words_generated)

    encoded_counts: dict[tuple[int, int, int], int] = {}
    words_kept = 0
    if workers == 1:
        record_batches = [
            _jit_group_word_records(
                length,
                params.alphabet_size,
                pair_dinv_array,
                base_powers,
                dinv_limit,
                params.step,
                0,
                words_generated,
            )
        ]
    else:
        chunk_size = (words_generated + workers - 1) // workers
        jobs = []
        for worker_index in range(workers):
            start_word = worker_index * chunk_size
            stop_word = min(words_generated, start_word + chunk_size)
            if start_word < stop_word:
                jobs.append(
                    (length, params.alphabet_size, pair_dinv, dinv_limit, params.step, start_word, stop_word)
                )
        with Pool(processes=len(jobs)) as pool:
            record_batches = pool.map(_jit_group_word_records_worker, jobs)

    for encoded_keys, multiplicities, batch_words_kept in record_batches:
        words_kept += batch_words_kept
        for index, multiplicity in enumerate(multiplicities):
            key = (int(encoded_keys[index, 0]), int(encoded_keys[index, 1]), int(encoded_keys[index, 2]))
            encoded_counts[key] = encoded_counts.get(key, 0) + int(multiplicity)

    for (multiset_key, dinv, required_dual_cuts), multiplicity in encoded_counts.items():
        grouped[multiset_key][dinv][required_dual_cuts] = multiplicity

    expected_kept = words_generated - (params.alphabet_size - 1) ** length
    require(words_kept == expected_kept, f"internal word-count mismatch for length {length}")
    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}, words_generated, words_kept


def tableau_shape_groups_for_length(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> dict[MultisetKey, dict[int, Counter[Shape]]]:
    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[Shape]]] = defaultdict(lambda: defaultdict(Counter))
    base_powers = tuple((length + 1) ** index for index in range(params.alphabet_size))

    for shape in partition_shapes(length):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(row_length)] for row_length in shape]
        for first_one_cell_index in range(length):
            counts = [0] * params.alphabet_size
            active_indices: list[int] = []

            def fill(cell_index: int, dinv: int, multiset_key: int) -> None:
                if cell_index == len(cells):
                    grouped[multiset_key][dinv][shape] += 1
                    return

                row, col = cells[cell_index]
                lower = 1
                if col > 0:
                    lower = rows[row][col - 1] + params.step + 1
                upper = params.alphabet_size
                if row + 1 < len(shape) and col < shape[row + 1]:
                    upper = min(upper, rows[row + 1][col] + params.step)

                if cell_index < first_one_cell_index:
                    lower = max(lower, 2)
                    values = range(lower, upper + 1)
                elif cell_index == first_one_cell_index:
                    if lower > 1 or upper < 1:
                        return
                    values = (1,)
                else:
                    values = range(lower, upper + 1)

                for value in values:
                    value_index = value - 1
                    dinv_increment = 0
                    for earlier_index in active_indices:
                        dinv_increment += counts[earlier_index] * pair_dinv[earlier_index][value_index]
                    rows[row][col] = value
                    first_value = counts[value_index] == 0
                    if first_value:
                        active_indices.append(value_index)
                    counts[value_index] += 1
                    fill(cell_index + 1, dinv + dinv_increment, multiset_key + base_powers[value_index])
                    counts[value_index] -= 1
                    if first_value:
                        active_indices.pop()
                    rows[row][col] = 0

            fill(0, 0, 0)

    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}


def count_ssyt_with_content(shape: Shape, content: Partition) -> int:
    """Return the Kostka number for ``shape`` and dominant content ``content``."""

    if sum(shape) != sum(content):
        return 0
    alphabet_size = len(content)
    if not shape:
        return 1 if not content else 0
    remaining = list(content)
    cells = [(row, col) for row, length in enumerate(shape) for col in range(length)]
    rows = [[-1 for _ in range(length)] for length in shape]
    total = 0

    def rec(cell_index: int) -> None:
        nonlocal total
        if cell_index == len(cells):
            total += 1
            return
        row, col = cells[cell_index]
        min_value = 0
        if col > 0:
            min_value = max(min_value, rows[row][col - 1])
        if row > 0 and col < shape[row - 1]:
            min_value = max(min_value, rows[row - 1][col] + 1)
        for value in range(min_value, alphabet_size):
            if remaining[value] == 0:
                continue
            remaining[value] -= 1
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = -1
            remaining[value] += 1

    rec(0)
    return total


def dyck_tableau_prediction(
    shape_counts: Counter[Shape],
    partition: Partition,
    *,
    ssyt_cache: dict[tuple[Shape, Partition], int],
) -> int:
    total = 0
    for shape, tableau_count in shape_counts.items():
        key = (shape, partition)
        if key not in ssyt_cache:
            ssyt_cache[key] = count_ssyt_with_content(shape, partition)
        total += tableau_count * ssyt_cache[key]
    return total


def dyck_tableau_predictions(
    shape_counts: Counter[Shape],
    partitions: list[PartitionMaskData],
    *,
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> list[int]:
    if not shape_counts:
        return [0] * len(partitions)
    cache_key = tuple(sorted(shape_counts.items()))
    if cache_key in prediction_cache:
        return prediction_cache[cache_key]
    out = [0] * len(partitions)
    for shape, tableau_count in shape_counts.items():
        for index, (partition, _compositions, _cut_masks) in enumerate(partitions):
            key = (shape, partition)
            if key not in ssyt_cache:
                ssyt_cache[key] = count_ssyt_with_content(shape, partition)
            out[index] += tableau_count * ssyt_cache[key]
    prediction_cache[cache_key] = out
    return out


def valid_factorization_count(mask_counts: Counter[int], cut_mask: int) -> int:
    total = 0
    for required_mask, multiplicity in mask_counts.items():
        if required_mask & ~cut_mask == 0:
            total += multiplicity
    return total


def valid_factorization_counts_by_cut_mask(mask_counts: Counter[int], *, length: int) -> list[int]:
    """Return counts for every cut mask by subset zeta transform."""

    mask_count = 1 << max(0, length - 1)
    counts = [0] * mask_count
    for required_mask, multiplicity in mask_counts.items():
        counts[required_mask] = multiplicity
    for bit in range(max(0, length - 1)):
        bit_mask = 1 << bit
        for mask in range(mask_count):
            if mask & bit_mask:
                counts[mask] += counts[mask ^ bit_mask]
    return counts


def cached_valid_factorization_counts_by_cut_mask(
    mask_counts: Counter[int],
    *,
    length: int,
    cache: dict[tuple[int, tuple[tuple[int, int], ...]], list[int]],
) -> list[int]:
    cache_key = (length, tuple(mask_counts.items()))
    if cache_key not in cache:
        cache[cache_key] = valid_factorization_counts_by_cut_mask(mask_counts, length=length)
    return cache[cache_key]


def check_partition_class(
    *,
    params: CheckInput,
    multiset: Word,
    dinv: int,
    partition: Partition,
    compositions: list[Composition],
    cut_masks: tuple[int, ...],
    valid_by_cut_mask: list[int],
    predicted: int,
) -> int:
    actual = valid_by_cut_mask[cut_masks[0]]
    for index in range(1, len(cut_masks)):
        if valid_by_cut_mask[cut_masks[index]] != actual:
            values = {
                composition: valid_by_cut_mask[cut_mask]
                for composition, cut_mask in zip(compositions, cut_masks)
            }
            examples = sorted(values.items())[:8]
            raise AssertionError(
                "factorization symmetry mismatch: "
                f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                f"partition={partition}, examples={examples}"
            )
    if actual != predicted:
        values = {
            composition: valid_by_cut_mask[cut_mask]
            for composition, cut_mask in zip(compositions, cut_masks)
        }
        examples = sorted(values.items())[:8]
        raise AssertionError(
            "Dyck-tableau prediction mismatch: "
            f"t={params.step}, multiset={multiset}, dinv={dinv}, "
            f"partition={partition}, factorization_count={actual}, "
            f"tableau_prediction={predicted}, examples={examples}"
        )
    return len(compositions)


def run_check(params: CheckInput) -> CheckResult:
    require(params.step >= 0, "t must be non-negative")
    require(params.alphabet_size > 0, "alphabet size A must be positive")
    require(params.max_length > 0, "max length L must be positive")

    start = time.perf_counter()
    result = CheckResult(params=params)
    pair_dinv = pair_dinv_table(params)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    valid_cut_mask_cache: dict[tuple[int, tuple[tuple[int, int], ...]], list[int]] = {}

    for length in range(1, params.max_length + 1):
        length_start = time.perf_counter()
        word_groups, words_generated, words_kept = group_words_for_length(
            length,
            params=params,
            pair_dinv=pair_dinv,
        )
        tableau_groups = tableau_shape_groups_for_length(
            length,
            params=params,
            pair_dinv=pair_dinv,
        )
        partitions = composition_groups(length)
        result.words_generated += words_generated
        result.words_kept += words_kept

        length_multisets = 0
        length_dinv_classes = 0
        length_partition_classes = 0
        for key in sorted(set(word_groups) | set(tableau_groups)):
            multiset = multiset_from_key(key, alphabet_size=params.alphabet_size, length=length)
            words_by_dinv = word_groups.get(key, {})
            tableaux_by_dinv = tableau_groups.get(key, {})
            length_multisets += 1
            for dinv in sorted(set(words_by_dinv) | set(tableaux_by_dinv)):
                length_dinv_classes += 1
                mask_counts = words_by_dinv.get(dinv, Counter())
                valid_by_cut_mask = cached_valid_factorization_counts_by_cut_mask(
                    mask_counts,
                    length=length,
                    cache=valid_cut_mask_cache,
                )
                shape_counts = tableaux_by_dinv.get(dinv, Counter())
                result.tableaux_checked += sum(shape_counts.values())
                predictions = dyck_tableau_predictions(
                    shape_counts,
                    partitions,
                    ssyt_cache=ssyt_cache,
                    prediction_cache=prediction_cache,
                )
                for partition_index, (partition, compositions, cut_masks) in enumerate(partitions):
                    actual = valid_by_cut_mask[cut_masks[0]]
                    for cut_mask in cut_masks[1:]:
                        if valid_by_cut_mask[cut_mask] != actual:
                            values = {
                                composition: valid_by_cut_mask[composition_cut_mask]
                                for composition, composition_cut_mask in zip(compositions, cut_masks)
                            }
                            examples = sorted(values.items())[:8]
                            raise AssertionError(
                                "factorization symmetry mismatch: "
                                f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                                f"partition={partition}, examples={examples}"
                            )
                    predicted = predictions[partition_index]
                    if actual != predicted:
                        values = {
                            composition: valid_by_cut_mask[composition_cut_mask]
                            for composition, composition_cut_mask in zip(compositions, cut_masks)
                        }
                        examples = sorted(values.items())[:8]
                        raise AssertionError(
                            "Dyck-tableau prediction mismatch: "
                            f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                            f"partition={partition}, factorization_count={actual}, "
                            f"tableau_prediction={predicted}, examples={examples}"
                        )
                    result.compositions_checked += len(compositions)
                    length_partition_classes += 1

        result.multisets_checked += length_multisets
        result.dinv_classes_checked += length_dinv_classes
        result.partition_classes_checked += length_partition_classes
        print(
            f"  length={length}: generated={words_generated}, kept={words_kept}, "
            f"multisets={length_multisets}, dinv classes={length_dinv_classes}, "
            f"partitions={length_partition_classes}, elapsed={time.perf_counter() - length_start:.3f}s",
            flush=True,
        )

    result.elapsed_seconds = time.perf_counter() - start
    return result


def print_result(result: CheckResult) -> None:
    params = result.params
    print(f"completed: t={params.step}, alphabet={{1,...,{params.alphabet_size}}}, lengths<= {params.max_length}")
    print(f"  words generated: {result.words_generated}")
    print(f"  1-containing words checked: {result.words_kept}")
    print(f"  multisets checked: {result.multisets_checked}")
    print(f"  dinv classes checked: {result.dinv_classes_checked}")
    print(f"  partition classes checked: {result.partition_classes_checked}")
    print(f"  positive compositions checked: {result.compositions_checked}")
    print(f"  Dyck tableaux checked: {result.tableaux_checked}")
    print(f"  elapsed: {result.elapsed_seconds:.3f}s")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, required=True, help="Rational step t.")
    parser.add_argument("--alphabet-size", "-A", type=int, required=True, help="Alphabet size A.")
    parser.add_argument("--max-length", "-L", type=int, required=True, help="Maximum word length L.")
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Word-grouping worker processes. Use 0 for automatic selection.",
    )
    args = parser.parse_args()

    result = run_check(
        CheckInput(
            step=args.t,
            alphabet_size=args.alphabet_size,
            max_length=args.max_length,
            workers=args.workers,
        )
    )
    print_result(result)
    print("all requested finite checks passed")


if __name__ == "__main__":
    main()
```

### `docs/items/dyck_symmetric_functions/code/classical_insertion_demo.py`

```python
"""Small trace for the classical dual Dyck insertion algorithm."""

from __future__ import annotations

from paper_algorithms import is_dyck_tableau, rowsert, tabsert


def main() -> None:
    row = [0, 3, 6]
    inserted = [1, 4]
    row_steps = []
    evicted, new_row = rowsert(row, inserted, trace=row_steps)

    print("rowsert example")
    print(f"  row: {row}")
    print(f"  inserted row: {inserted}")
    print(f"  evicted row: {evicted}")
    print(f"  output row: {new_row}")
    for index, step in enumerate(row_steps, 1):
        print(f"  step {index}: {step}")

    tableau = [[0, 3], [1, 4]]
    inserted_row = [2, 5]
    output, traces = tabsert(tableau, inserted_row, trace=True)

    print()
    print("tabsert example")
    print(f"  tableau: {tableau}")
    print(f"  inserted row: {inserted_row}")
    print(f"  output: {output}")
    print(f"  valid Dyck tableau: {is_dyck_tableau(output)}")
    for trace in traces:
        print(f"  row {trace.row_index}: inserted {trace.inserted_row}, evicted {trace.evicted_row}")


if __name__ == "__main__":
    main()
```

### `docs/items/dyck_symmetric_functions/code/paper_algorithms/__init__.py`

```python
"""Minimal algorithm package for the Dyck symmetric functions item."""

from .rational_dyck import (
    conjugate_partition,
    enumerate_rational_dyck_tableaux,
    is_rational_affine_dyck,
    is_rational_dual_dyck,
    is_rational_dyck_tableau,
    rational_affine_factorization_polynomial,
    rational_dual_factorization_polynomial,
    rational_dinv,
    rational_row_reading_word,
    schur_sum_from_tableau_shapes,
    shape_counts,
    unique_multiset_permutations,
)
from .row_insertion import RowsertStep, is_dual_dyck, rowsert
from .tableau_insertion import TabsertRowTrace, is_dyck_tableau, tabsert

__all__ = [
    "RowsertStep",
    "TabsertRowTrace",
    "conjugate_partition",
    "enumerate_rational_dyck_tableaux",
    "is_dual_dyck",
    "is_dyck_tableau",
    "is_rational_affine_dyck",
    "is_rational_dual_dyck",
    "is_rational_dyck_tableau",
    "rational_affine_factorization_polynomial",
    "rational_dual_factorization_polynomial",
    "rational_dinv",
    "rational_row_reading_word",
    "rowsert",
    "schur_sum_from_tableau_shapes",
    "shape_counts",
    "tabsert",
    "unique_multiset_permutations",
]
```

### `docs/items/dyck_symmetric_functions/code/paper_algorithms/rational_dyck.py`

```python
"""Finite helpers for the ``r = ms + 1`` rational Dyck generalization."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb
from typing import Iterable, Sequence

from .ssyt import Shape, SSYT, enumerate_ssyt, is_partition_shape, schur_polynomial_by_ssyt, ssyt_weight


SequenceWord = tuple[int, ...]
Tableau = tuple[tuple[int, ...], ...]
Weight = tuple[int, ...]


def _check_m(m: int) -> None:
    if not isinstance(m, int) or m < 0:
        raise ValueError("m must be a non-negative integer")


def rational_dinv(sequence: Sequence[int], *, m: int) -> int:
    """Return the rational dinv statistic for an integer sequence."""

    _check_m(m)
    values = tuple(sequence)
    total = 0
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            if left <= right:
                total += max(0, left + m - right)
            else:
                total += max(0, right + 1 + m - left)
    return total


def is_rational_affine_dyck(sequence: Sequence[int], *, m: int) -> bool:
    """Check ``x[i+1] <= x[i] + m``."""

    _check_m(m)
    values = tuple(sequence)
    return all(isinstance(value, int) for value in values) and all(
        values[index + 1] <= values[index] + m for index in range(len(values) - 1)
    )


def is_rational_dual_dyck(sequence: Sequence[int], *, m: int) -> bool:
    """Check ``x[i+1] > x[i] + m``."""

    _check_m(m)
    values = tuple(sequence)
    return all(isinstance(value, int) for value in values) and all(
        values[index + 1] > values[index] + m for index in range(len(values) - 1)
    )


def generate_rational_dyck_sequences(length: int, *, step: int) -> list[SequenceWord]:
    """Generate normalized ``step``-affine Dyck sequences of fixed length."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")

    out: list[SequenceWord] = []

    def rec(prefix: list[int]) -> None:
        if len(prefix) == length:
            out.append(tuple(prefix))
            return
        previous = prefix[-1]
        # Nonnegativity and the initial zero make this finite; the largest
        # possible next entry is obtained by taking the maximum allowed step.
        for value in range(previous + step + 1):
            prefix.append(value)
            rec(prefix)
            prefix.pop()

    rec([0])
    return out


def is_normalized_rational_dyck_sequence(sequence: Sequence[int], *, step: int) -> bool:
    """Check the normalized rational Dyck sequence convention."""

    _check_m(step)
    values = tuple(sequence)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and is_rational_affine_dyck(values, m=step)
    )


def find_rational_extractable_position(
    sequence: Sequence[int],
    *,
    step: int,
    include_final: bool = True,
) -> int | None:
    """Return the leftmost generalized extractable position, if any."""

    _check_m(step)
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        raise ValueError("sequence must be a normalized rational Dyck sequence")
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = sum(1 for prior in values[:index] if lower <= prior <= value - 1)
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + step:
            continue
        return index
    return None


def is_rational_m_skeleton(sequence: Sequence[int], *, step: int, ambient: int | None = None) -> bool:
    """Check the generalized ``[0,m]`` skeleton condition."""

    _check_m(step)
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    endpoint = values[-1] if ambient is None else ambient
    return (
        endpoint >= 0
        and max(values) == endpoint
        and values[-1] == endpoint
        and find_rational_extractable_position(values, step=step, include_final=False) is None
    )


def rational_max_total_degree(length: int, *, step: int) -> int:
    """Return the conjectural top total degree for ``r = length*step + 1``."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    return step * comb(length, 2)


def rational_deficit(sequence: Sequence[int], *, step: int) -> int:
    """Return ``M - area - dinv`` with ``M = step*binom(length, 2)``."""

    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        raise ValueError("sequence must be a normalized rational Dyck sequence")
    return rational_max_total_degree(len(values), step=step) - sum(values) - rational_dinv(values, m=step)


def excluded_rational_full_skeleton(length: int, *, step: int) -> SequenceWord:
    """Return ``(0,0,1,0,...,0,step)``."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    if length < 4:
        raise ValueError("the excluded skeleton is only defined for length at least 4")
    return (0, 0, 1) + (0,) * (length - 4) + (step,)


def is_rational_full_skeleton(sequence: Sequence[int], *, step: int) -> bool:
    """Check the generalized full skeleton condition."""

    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    return find_rational_extractable_position(values, step=step, include_final=True) is None


def is_rational_special_skeleton(sequence: Sequence[int], *, step: int) -> bool:
    """Check full skeleton status, excluding ``(0,0,1,0,...,0,1)``."""

    values = tuple(sequence)
    if not is_rational_full_skeleton(values, step=step):
        return False
    if len(values) < 4:
        return True
    return values != excluded_rational_full_skeleton(len(values), step=step)


def unique_multiset_permutations(values: Iterable[int]) -> Iterable[SequenceWord]:
    """Yield distinct permutations of a finite multiset in lexicographic order."""

    counts = Counter(values)
    if any(not isinstance(value, int) for value in counts):
        raise ValueError("values must be integers")

    def rec(prefix: list[int], remaining: int) -> Iterable[SequenceWord]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for value in sorted(counts):
            if counts[value] == 0:
                continue
            counts[value] -= 1
            prefix.append(value)
            yield from rec(prefix, remaining - 1)
            prefix.pop()
            counts[value] += 1

    yield from rec([], sum(counts.values()))


def rational_affine_factorization_polynomial(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int,
    variable_count: int,
) -> Counter[Weight]:
    """Count affine factorizations by factor lengths.

    The output coefficient of ``(a0, ..., ak)`` counts ordered factorizations
    into ``variable_count`` possibly empty consecutive factors with lengths
    ``a0, ..., ak`` whose concatenation has the requested rational dinv.
    """

    _check_m(m)
    if not isinstance(target_dinv, int) or target_dinv < 0:
        raise ValueError("target_dinv must be a non-negative integer")
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    values_tuple = tuple(values)
    polynomial: Counter[Weight] = Counter()
    length = len(values_tuple)

    def cut_rec(start: int, factors_left: int, cuts: list[int], sequence: SequenceWord) -> None:
        if factors_left == 1:
            parts = cuts + [length]
            previous = 0
            factor_lengths: list[int] = []
            for stop in parts:
                factor = sequence[previous:stop]
                if not is_rational_affine_dyck(factor, m=m):
                    return
                factor_lengths.append(len(factor))
                previous = stop
            polynomial[tuple(factor_lengths)] += 1
            return
        for stop in range(start, length + 1):
            cut_rec(stop, factors_left - 1, cuts + [stop], sequence)

    for sequence in unique_multiset_permutations(values_tuple):
        if rational_dinv(sequence, m=m) == target_dinv:
            cut_rec(0, variable_count, [], sequence)
    return polynomial


def rational_dual_factorization_polynomial(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int,
    variable_count: int,
) -> Counter[Weight]:
    """Count dual factorizations by factor lengths."""

    _check_m(m)
    if not isinstance(target_dinv, int) or target_dinv < 0:
        raise ValueError("target_dinv must be a non-negative integer")
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    values_tuple = tuple(values)
    polynomial: Counter[Weight] = Counter()
    length = len(values_tuple)

    def cut_rec(start: int, factors_left: int, cuts: list[int], sequence: SequenceWord) -> None:
        if factors_left == 1:
            parts = cuts + [length]
            previous = 0
            factor_lengths: list[int] = []
            for stop in parts:
                factor = sequence[previous:stop]
                if not is_rational_dual_dyck(factor, m=m):
                    return
                factor_lengths.append(len(factor))
                previous = stop
            polynomial[tuple(factor_lengths)] += 1
            return
        for stop in range(start, length + 1):
            cut_rec(stop, factors_left - 1, cuts + [stop], sequence)

    for sequence in unique_multiset_permutations(values_tuple):
        if rational_dinv(sequence, m=m) == target_dinv:
            cut_rec(0, variable_count, [], sequence)
    return polynomial


def rational_row_reading_word(tableau: Sequence[Sequence[int]]) -> SequenceWord:
    """Read rows left-to-right, from bottom row to top row."""

    rows = tuple(tuple(row) for row in tableau)
    return tuple(value for row in reversed(rows) for value in row)


def rational_dyck_tableau_shape(tableau: Sequence[Sequence[int]]) -> Shape:
    return tuple(len(row) for row in tableau)


def is_rational_dyck_tableau(tableau: Sequence[Sequence[int]], *, m: int) -> bool:
    """Check the rational Dyck tableau conditions in top-to-bottom row order."""

    _check_m(m)
    rows = tuple(tuple(row) for row in tableau)
    shape = rational_dyck_tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    if any(not is_rational_dual_dyck(row, m=m) for row in rows):
        return False
    for row_index in range(len(rows) - 1):
        upper = rows[row_index]
        lower = rows[row_index + 1]
        for column in range(len(lower)):
            if upper[column] > lower[column] + m:
                return False
    return True


def enumerate_rational_dyck_tableaux(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int | None = None,
) -> list[Tableau]:
    """Enumerate rational Dyck tableaux with the requested multiset entries."""

    _check_m(m)
    values_tuple = tuple(values)
    if any(not isinstance(value, int) for value in values_tuple):
        raise ValueError("values must be integers")
    if target_dinv is not None and (not isinstance(target_dinv, int) or target_dinv < 0):
        raise ValueError("target_dinv must be a non-negative integer or None")

    out: list[Tableau] = []
    total_size = len(values_tuple)

    def partition_rec(remaining: int, max_part: int, prefix: list[int]) -> Iterable[Shape]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for part in range(min(remaining, max_part), 0, -1):
            prefix.append(part)
            yield from partition_rec(remaining - part, part, prefix)
            prefix.pop()

    for shape in partition_rec(total_size, total_size, []):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(length)] for length in shape]
        remaining = Counter(values_tuple)

        def valid_cell(row: int, col: int, value: int) -> bool:
            if col > 0 and value <= rows[row][col - 1] + m:
                return False
            if row + 1 < len(shape) and col < shape[row + 1]:
                if value > rows[row + 1][col] + m:
                    return False
            if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
                if rows[row - 1][col] > value + m:
                    return False
            return True

        def fill(cell_index: int) -> None:
            if cell_index == len(cells):
                tableau = tuple(tuple(row) for row in rows)
                if target_dinv is None or rational_dinv(rational_row_reading_word(tableau), m=m) == target_dinv:
                    out.append(tableau)
                return
            row, col = cells[cell_index]
            for value in sorted(remaining):
                if remaining[value] == 0 or not valid_cell(row, col, value):
                    continue
                rows[row][col] = value
                remaining[value] -= 1
                fill(cell_index + 1)
                remaining[value] += 1
                rows[row][col] = 0

        fill(0)
    return out


def shape_counts(tableaux: Iterable[Sequence[Sequence[int]]]) -> Counter[Shape]:
    return Counter(rational_dyck_tableau_shape(tableau) for tableau in tableaux)


def conjugate_partition(shape: Sequence[int]) -> Shape:
    shape_tuple = tuple(shape)
    if shape_tuple == ():
        return ()
    if not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition")
    return tuple(sum(1 for part in shape_tuple if part >= column) for column in range(1, shape_tuple[0] + 1))


def schur_sum_from_tableau_shapes(
    tableaux: Iterable[Sequence[Sequence[int]]],
    *,
    variable_count: int,
    conjugate_shapes: bool,
) -> Counter[Weight]:
    """Expand ``sum_P s_shape(P)`` or ``sum_P s_shape(P)'`` into monomials."""

    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")
    out: Counter[Weight] = Counter()
    for tableau in tableaux:
        shape = rational_dyck_tableau_shape(tableau)
        if conjugate_shapes:
            shape = conjugate_partition(shape)
        for weight, coefficient in schur_polynomial_by_ssyt(shape, alphabet_size=variable_count).items():
            out[weight] += coefficient
    return out


def partition_weights(total: int, *, max_parts: int) -> list[Weight]:
    if not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    if not isinstance(max_parts, int) or max_parts <= 0:
        raise ValueError("max_parts must be positive")
    out: list[Weight] = []

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if len(prefix) == max_parts:
            if remaining == 0:
                out.append(tuple(prefix))
            return
        slots_left = max_parts - len(prefix) - 1
        for part in range(min(remaining, max_part), -1, -1):
            prefix.append(part)
            rec(remaining - part, part, prefix)
            prefix.pop()

    rec(total, total, [])
    return out


def schur_expansion_from_monomial_symmetric(
    monomial_coefficients: Counter[Weight] | dict[Weight, int],
    *,
    variable_count: int,
) -> Counter[Shape]:
    """Convert a symmetric monomial dictionary to Schur coefficients.

    Keys are exponent partitions padded to ``variable_count`` parts, as in the
    monomial symmetric basis in that many variables.
    """

    if not monomial_coefficients:
        return Counter()
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    normalized: Counter[Weight] = Counter()
    total: int | None = None
    for weight, coefficient in monomial_coefficients.items():
        weight_tuple = tuple(weight)
        if len(weight_tuple) != variable_count:
            raise ValueError("all weights must have length variable_count")
        if any(part < 0 for part in weight_tuple) or tuple(sorted(weight_tuple, reverse=True)) != weight_tuple:
            raise ValueError("weights must be partitions padded with zeros")
        if total is None:
            total = sum(weight_tuple)
        elif sum(weight_tuple) != total:
            raise ValueError("all weights must have the same total degree")
        normalized[weight_tuple] += coefficient

    assert total is not None
    partitions = partition_weights(total, max_parts=variable_count)
    remaining = {partition: Fraction(normalized.get(partition, 0)) for partition in partitions}
    coefficients: Counter[Shape] = Counter()

    for shape in partitions:
        shape_no_zeros = tuple(part for part in shape if part)
        if len(shape_no_zeros) > variable_count:
            continue
        schur_terms = Counter(
            ssyt_weight(tableau, alphabet_size=variable_count)
            for tableau in enumerate_ssyt(shape_no_zeros, alphabet_size=variable_count)
        )
        coefficient = remaining[shape]
        if coefficient:
            if coefficient.denominator != 1:
                raise ValueError(f"non-integral Schur coefficient for shape {shape}: {coefficient}")
            coefficients[shape_no_zeros] = int(coefficient)
        for weight, kostka in schur_terms.items():
            if weight in remaining:
                remaining[weight] -= coefficient * kostka

    if any(value != 0 for value in remaining.values()):
        raise ValueError(f"monomial coefficients were not fully converted: {remaining}")
    return coefficients


def at_most_two_column_shapes(total_size: int) -> list[Shape]:
    """Return partition shapes of ``total_size`` with at most two columns."""

    if not isinstance(total_size, int) or total_size < 0:
        raise ValueError("total_size must be a non-negative integer")
    if total_size == 0:
        return [()]
    out: list[Shape] = []
    for two_cell_rows in range(total_size // 2, -1, -1):
        one_cell_rows = total_size - 2 * two_cell_rows
        shape = (2,) * two_cell_rows + (1,) * one_cell_rows
        out.append(shape)
    return out


def enumerate_bounded_rational_dyck_tableaux(
    shape: Sequence[int],
    *,
    step: int,
    max_entry: int,
) -> list[Tableau]:
    """Enumerate rational Dyck tableaux of a fixed shape and entry interval.

    Rows are in top-to-bottom order, entries lie in ``[0,max_entry]``, rows are
    rational dual Dyck sequences, and columns read bottom-to-top are rational
    affine Dyck sequences.
    """

    _check_m(step)
    if not isinstance(max_entry, int):
        raise ValueError("max_entry must be an integer")
    shape_tuple = tuple(shape)
    if shape_tuple == ():
        return [()]
    if not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition")
    if max_entry < 0:
        return []

    rows = [[0 for _ in range(length)] for length in shape_tuple]
    cells = [(row, col) for row in range(len(shape_tuple) - 1, -1, -1) for col in range(shape_tuple[row])]
    out: list[Tableau] = []

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape_tuple) and col < shape_tuple[row + 1]:
            if value > rows[row + 1][col] + step:
                return False
        if row > 0 and col < shape_tuple[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int) -> None:
        if cell_index == len(cells):
            out.append(tuple(tuple(row) for row in rows))
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = 0

    rec(0)
    return out


def rational_qt_catalan_direct_coefficients(length: int, *, step: int) -> Counter[tuple[int, int]]:
    """Direct ``q^area t^dinv`` coefficients from normalized rational Dyck words."""

    coeffs: Counter[tuple[int, int]] = Counter()
    for sequence in generate_rational_dyck_sequences(length, step=step):
        coeffs[(sum(sequence), rational_dinv(sequence, m=step))] += 1
    return coeffs


def rational_two_column_formula_coefficients(length: int, *, step: int) -> Counter[tuple[int, int]]:
    """Formula-side coefficients using rational skeletons and two-column tabs."""

    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    _check_m(step)

    coeffs: Counter[tuple[int, int]] = Counter()
    for skeleton_length in range(1, length + 1):
        tableau_size = length - skeleton_length
        for skeleton in generate_rational_dyck_sequences(skeleton_length, step=step):
            if not is_rational_m_skeleton(skeleton, step=step):
                continue
            ambient = skeleton[-1]
            for shape in at_most_two_column_shapes(tableau_size):
                for tableau in enumerate_bounded_rational_dyck_tableaux(
                    shape,
                    step=step,
                    max_entry=ambient - 1,
                ):
                    rr = rational_row_reading_word(tableau)
                    base = skeleton + rr
                    base_area = sum(base)
                    base_dinv = rational_dinv(base, m=step)
                    size = sum(shape)
                    schur_shape = conjugate_partition(shape)
                    for weight, multiplicity in schur_polynomial_by_ssyt(schur_shape, alphabet_size=2).items():
                        q_power, t_power = weight
                        coeffs[(base_area + q_power, base_dinv - size + t_power)] += multiplicity
    return coeffs


def rational_skeleton_string_formula_coefficients(
    length: int,
    *,
    step: int,
    max_deficit: int,
) -> Counter[tuple[int, int]]:
    """Expand the special-skeleton quotient formula in the rational setting."""

    if not isinstance(max_deficit, int) or max_deficit < 0:
        raise ValueError("max_deficit must be a non-negative integer")
    total_degree = rational_max_total_degree(length, step=step)
    coeffs: Counter[tuple[int, int]] = Counter()
    for sequence in generate_rational_dyck_sequences(length, step=step):
        if not is_rational_special_skeleton(sequence, step=step):
            continue
        deficit = rational_deficit(sequence, step=step)
        if deficit > max_deficit:
            continue
        area = sum(sequence)
        dinv = rational_dinv(sequence, m=step)
        if dinv >= area:
            for q_power in range(area, dinv + 1):
                coeffs[(q_power, total_degree - deficit - q_power)] += 1
        else:
            for q_power in range(dinv + 1, area):
                coeffs[(q_power, total_degree - deficit - q_power)] -= 1
    return coeffs
```

### `docs/items/dyck_symmetric_functions/code/paper_algorithms/row_insertion.py`

```python
"""Section 3 row insertion algorithms.

The draft's "dual Dyck" rows are finite non-negative integer sequences whose
consecutive entries differ by at least +2.  The empty sequence is accepted:
the Section 3 rowsert definition explicitly allows empty input rows, and the
local gap condition is vacuous for length 0 and length 1.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal, Sequence


CaseName = Literal["case0", "case1", "case2", "case3"]


@dataclass(frozen=True)
class Chain:
    """A contiguous maximal +2-chain, using zero-based half-open indices."""

    start: int
    stop: int
    values: tuple[int, ...]

    @property
    def length(self) -> int:
        return self.stop - self.start


@dataclass(frozen=True)
class RowsertStep:
    case: CaseName
    f_chunk: tuple[int, ...]
    r_chunk: tuple[int, ...]
    index: int | None
    r_chain: Chain | None = None
    f_chain: Chain | None = None


@dataclass(frozen=True)
class WorsertStep:
    case: CaseName
    e_chunk: tuple[int, ...]
    r_chunk: tuple[int, ...]
    index: int | None
    r_chain: Chain | None = None
    e_chain: Chain | None = None


def is_dual_dyck(seq: Sequence[int]) -> bool:
    """Return whether ``seq`` satisfies the dual-Dyck step-gap condition."""

    return all(value >= 0 for value in seq) and all(
        seq[index + 1] >= seq[index] + 2 for index in range(len(seq) - 1)
    )


def _require_position(seq: Sequence[int], index: int) -> None:
    if not 0 <= index < len(seq):
        raise IndexError(f"position {index} is outside sequence of length {len(seq)}")


def maximal_plus2_chain_starting_at(seq: Sequence[int], index: int) -> Chain:
    """Return the maximal +2-chain starting at ``index``."""

    _require_position(seq, index)
    stop = index + 1
    while stop < len(seq) and seq[stop] == seq[stop - 1] + 2:
        stop += 1
    return Chain(index, stop, tuple(seq[index:stop]))


def maximal_plus2_chain_ending_at(seq: Sequence[int], index: int) -> Chain:
    """Return the maximal +2-chain ending at ``index``."""

    _require_position(seq, index)
    start = index
    while start > 0 and seq[start - 1] == seq[start] - 2:
        start -= 1
    return Chain(start, index + 1, tuple(seq[start : index + 1]))


def rowsert(
    r0: Sequence[int], f0: Sequence[int], *, trace: list[RowsertStep] | None = None
) -> tuple[list[int], list[int]]:
    """Apply the draft's row insertion operation.

    Inputs are copied on entry, so caller-owned lists are never mutated.  The
    returned pair is ``(E, R)``.
    """

    if not is_dual_dyck(r0):
        raise ValueError("r0 must be a dual Dyck sequence")
    if not is_dual_dyck(f0):
        raise ValueError("f0 must be a dual Dyck sequence")

    e: list[int] = []
    r = list(r0)
    f = list(f0)

    while f:
        first = f[0]
        index = next((idx for idx, value in enumerate(r) if first <= value + 1), None)

        if index is None:
            chunk = (first,)
            del f[:1]
            r.extend(chunk)
            if trace is not None:
                trace.append(RowsertStep("case0", chunk, (), None))
            continue

        if first <= r[index]:
            f_chunk = (first,)
            r_chunk = (r[index],)
            del f[:1]
            r[index] = first
            e.extend(r_chunk)
            if trace is not None:
                trace.append(RowsertStep("case1", f_chunk, r_chunk, index))
            continue

        r_chain = maximal_plus2_chain_starting_at(r, index)
        f_chain = maximal_plus2_chain_starting_at(f, 0)

        if r_chain.length <= f_chain.length:
            length = r_chain.length
            f_chunk = tuple(f[:length])
            r_chunk = tuple(r[index : index + length])
            del f[:length]
            r[index : index + length] = f_chunk
            e.extend(r_chunk)
            if trace is not None:
                trace.append(
                    RowsertStep("case2", f_chunk, r_chunk, index, r_chain, f_chain)
                )
        else:
            length = f_chain.length
            f_chunk = tuple(f[:length])
            del f[:length]
            e.extend(f_chunk)
            if trace is not None:
                trace.append(
                    RowsertStep("case3", f_chunk, (), index, r_chain, f_chain)
                )

    return e, r


def worsert(
    e0: Sequence[int], r0: Sequence[int], *, trace: list[WorsertStep] | None = None
) -> tuple[list[int], list[int]]:
    """Apply the corrected reverse row insertion operation.

    Inputs are copied on entry, so caller-owned lists are never mutated.  The
    returned pair is ``(R, F)``.  Case 0 follows the author clarification for
    CA-0001: the removed final element of ``E`` is prepended to ``R``, not
    ``F``.
    """

    if not is_dual_dyck(e0):
        raise ValueError("e0 must be a dual Dyck sequence")
    if not is_dual_dyck(r0):
        raise ValueError("r0 must be a dual Dyck sequence")

    e = list(e0)
    r = list(r0)
    f: list[int] = []

    while e:
        last = e[-1]
        index = next(
            (idx for idx in range(len(r) - 1, -1, -1) if last >= r[idx] - 1),
            None,
        )

        if index is None:
            chunk = (last,)
            del e[-1:]
            r[0:0] = chunk
            if trace is not None:
                trace.append(WorsertStep("case0", chunk, (), None))
            continue

        if last >= r[index]:
            e_chunk = (last,)
            r_chunk = (r[index],)
            del e[-1:]
            r[index] = last
            f[0:0] = r_chunk
            if trace is not None:
                trace.append(WorsertStep("case1", e_chunk, r_chunk, index))
            continue

        r_chain = maximal_plus2_chain_ending_at(r, index)
        e_chain = maximal_plus2_chain_ending_at(e, len(e) - 1)

        if r_chain.length <= e_chain.length:
            length = r_chain.length
            start = index - length + 1
            e_chunk = tuple(e[-length:])
            r_chunk = tuple(r[start : index + 1])
            del e[-length:]
            r[start : index + 1] = e_chunk
            f[0:0] = r_chunk
            if trace is not None:
                trace.append(
                    WorsertStep("case2", e_chunk, r_chunk, index, r_chain, e_chain)
                )
        else:
            length = e_chain.length
            e_chunk = tuple(e[-length:])
            del e[-length:]
            f[0:0] = e_chunk
            if trace is not None:
                trace.append(
                    WorsertStep("case3", e_chunk, (), index, r_chain, e_chain)
                )

    return r, f


def di_statistic(seq: Iterable[int]) -> int:
    """Count ordered pairs ``i < j`` with ``seq[i] = seq[j] + 1``."""

    values = list(seq)
    total = 0
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            if values[left] == values[right] + 1:
                total += 1
    return total
```

### `docs/items/dyck_symmetric_functions/code/paper_algorithms/ssyt.py`

```python
"""Small semistandard Young tableau enumeration utilities.

Shapes are partitions in top-to-bottom row order.  SSYT entries use the
alphabet ``1, ..., alphabet_size`` by default, with rows weakly increasing and
columns strictly increasing from top to bottom.
"""

from __future__ import annotations

from collections import Counter
from typing import Iterable, Sequence


Shape = tuple[int, ...]
SSYT = tuple[tuple[int, ...], ...]
Weight = tuple[int, ...]


def is_partition_shape(shape: Sequence[int]) -> bool:
    values = tuple(shape)
    return all(isinstance(part, int) and part > 0 for part in values) and all(
        values[index] >= values[index + 1] for index in range(len(values) - 1)
    )


def partition_shapes(max_size: int, *, max_rows: int | None = None) -> list[Shape]:
    if not isinstance(max_size, int) or max_size < 0:
        raise ValueError("max_size must be a non-negative integer")
    if max_rows is not None and (not isinstance(max_rows, int) or max_rows < 0):
        raise ValueError("max_rows must be a non-negative integer or None")

    out: list[Shape] = [()]

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if prefix and (max_rows is None or len(prefix) <= max_rows):
            out.append(tuple(prefix))
        if max_rows is not None and len(prefix) >= max_rows:
            return
        for part in range(min(remaining, max_part), 0, -1):
            rec(remaining - part, part, prefix + [part])

    rec(max_size, max_size, [])
    return out


def shape_size(shape: Sequence[int]) -> int:
    if not is_partition_shape(shape) and tuple(shape) != ():
        raise ValueError("shape must be a partition")
    return sum(shape)


def tableau_shape(tableau: Sequence[Sequence[int]]) -> Shape:
    return tuple(len(row) for row in tableau)


def is_ssyt(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> bool:
    rows = tuple(tuple(row) for row in tableau)
    shape = tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    for row in rows:
        if any(not isinstance(value, int) or value < low or value > high for value in row):
            return False
        if any(row[index] > row[index + 1] for index in range(len(row) - 1)):
            return False
    for row_index in range(len(rows) - 1):
        for column in range(len(rows[row_index + 1])):
            if rows[row_index][column] >= rows[row_index + 1][column]:
                return False
    return True


def is_reverse_ssyt(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> bool:
    rows = tuple(tuple(row) for row in tableau)
    shape = tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    for row in rows:
        if any(not isinstance(value, int) or value < low or value > high for value in row):
            return False
        if any(row[index] < row[index + 1] for index in range(len(row) - 1)):
            return False
    for row_index in range(len(rows) - 1):
        for column in range(len(rows[row_index + 1])):
            if rows[row_index][column] <= rows[row_index + 1][column]:
                return False
    return True


def enumerate_ssyt(
    shape: Sequence[int],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> list[SSYT]:
    shape_tuple = tuple(shape)
    if shape_tuple != () and not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition in top-to-bottom row order")
    if not isinstance(alphabet_size, int) or alphabet_size <= 0:
        raise ValueError("alphabet_size must be positive")

    cells = [(row, col) for row, length in enumerate(shape_tuple) for col in range(length)]
    rows = [[0 for _ in range(length)] for length in shape_tuple]
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    out: list[SSYT] = []

    def rec(cell_index: int) -> None:
        if cell_index == len(cells):
            out.append(tuple(tuple(row) for row in rows))
            return
        row, col = cells[cell_index]
        min_value = low
        if col > 0:
            min_value = max(min_value, rows[row][col - 1])
        if row > 0 and col < shape_tuple[row - 1]:
            min_value = max(min_value, rows[row - 1][col] + 1)
        for value in range(min_value, high + 1):
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = 0

    rec(0)
    return out


def enumerate_reverse_ssyt(
    shape: Sequence[int],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> list[SSYT]:
    high = alphabet_start + alphabet_size - 1
    return tuple(
        tuple(tuple(high - (value - alphabet_start) for value in row) for row in tableau)
        for tableau in enumerate_ssyt(
            shape,
            alphabet_size=alphabet_size,
            alphabet_start=alphabet_start,
        )
    )


def ssyt_weight(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> Weight:
    if not is_ssyt(tableau, alphabet_size=alphabet_size, alphabet_start=alphabet_start):
        raise ValueError("tableau must be an SSYT over the requested alphabet")
    counts = [0] * alphabet_size
    for row in tableau:
        for value in row:
            counts[value - alphabet_start] += 1
    return tuple(counts)


def reverse_ssyt_weight(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> Weight:
    if not is_reverse_ssyt(tableau, alphabet_size=alphabet_size, alphabet_start=alphabet_start):
        raise ValueError("tableau must be a reverse SSYT over the requested alphabet")
    counts = [0] * alphabet_size
    for row in tableau:
        for value in row:
            counts[value - alphabet_start] += 1
    return tuple(counts)


def weight_dictionary(tableaux: Iterable[Sequence[Sequence[int]]], *, alphabet_size: int) -> Counter[Weight]:
    weights: Counter[Weight] = Counter()
    for tableau in tableaux:
        weights[ssyt_weight(tableau, alphabet_size=alphabet_size)] += 1
    return weights


def schur_polynomial_by_ssyt(shape: Sequence[int], *, alphabet_size: int) -> Counter[Weight]:
    return weight_dictionary(enumerate_ssyt(shape, alphabet_size=alphabet_size), alphabet_size=alphabet_size)
```

### `docs/items/dyck_symmetric_functions/code/paper_algorithms/tableau_insertion.py`

```python
"""Section 3 tableau insertion helpers.

Tableaux are represented as ``list`` objects ordered bottom row to top row.
Each row is a left-to-right sequence of non-negative integers.

Shape convention used here: rows may have different lengths and no monotone
row-length condition is imposed by ``is_dyck_tableau``.  For each column index,
the cells that exist in rows having that index are read bottom-to-top and must
satisfy the affine Dyck inequality.  This is the bottom-to-top representation
requested by CA-0002; it differs from the protected draft's local prose that
sometimes indexes rows top-to-bottom.

``tabsert`` processes existing rows in the source/paper top-to-bottom order,
which is descending index order under this bottom-to-top storage.  When it
carries a non-empty evicted row past all existing rows, that row is inserted at
index 0, i.e. it becomes a new bottom row in the bottom-to-top list.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .row_insertion import RowsertStep, WorsertStep, is_dual_dyck, rowsert, worsert


Tableau = list[list[int]]


@dataclass(frozen=True)
class TabsertRowTrace:
    row_index: int
    input_row: tuple[int, ...]
    inserted_row: tuple[int, ...]
    evicted_row: tuple[int, ...]
    output_row: tuple[int, ...]
    rowsert_steps: tuple[RowsertStep, ...]


@dataclass(frozen=True)
class ReverseTabsertRowTrace:
    row_index: int
    original_length: int
    input_row: tuple[int, ...]
    kept_row: tuple[int, ...]
    peeled_row: tuple[int, ...]
    accumulated_in: tuple[int, ...]
    recovered_row: tuple[int, ...]
    accumulated_out: tuple[int, ...]
    worsert_steps: tuple[WorsertStep, ...]


def _is_row(value: object) -> bool:
    return isinstance(value, (list, tuple)) and all(
        isinstance(entry, int) and entry >= 0 for entry in value
    )


def shape(tableau: Sequence[Sequence[int]]) -> list[int]:
    """Return row lengths in bottom-to-top order."""

    _require_tableau_like(tableau)
    return [len(row) for row in tableau]


def _require_tableau_like(tableau: Sequence[Sequence[int]]) -> None:
    if not isinstance(tableau, (list, tuple)):
        raise TypeError("tableau must be a list or tuple of rows")
    for row in tableau:
        if not _is_row(row):
            raise TypeError("each tableau row must be a sequence of non-negative integers")


def _copied_tableau(tableau: Sequence[Sequence[int]]) -> Tableau:
    _require_tableau_like(tableau)
    return [list(row) for row in tableau]


def is_affine_dyck(seq: Sequence[int]) -> bool:
    """Return whether ``seq`` satisfies the affine-Dyck step condition."""

    return all(isinstance(value, int) and value >= 0 for value in seq) and all(
        seq[index + 1] <= seq[index] + 1 for index in range(len(seq) - 1)
    )


def is_dyck_tableau(tableau: Sequence[Sequence[int]]) -> bool:
    """Validate the CA-0002 bottom-to-top Dyck tableau convention.

    Empty tableaux are accepted.  Empty rows inside a non-empty tableau are
    rejected, because they create ambiguous shape data for the reverse helper.
    """

    try:
        rows = _copied_tableau(tableau)
    except TypeError:
        return False

    if any(len(row) == 0 for row in rows):
        return len(rows) == 0
    if any(not is_dual_dyck(row) for row in rows):
        return False

    max_len = max((len(row) for row in rows), default=0)
    for column in range(max_len):
        column_values = [row[column] for row in rows if column < len(row)]
        if not is_affine_dyck(column_values):
            return False
    return True


def row_reading_word(tableau: Sequence[Sequence[int]]) -> list[int]:
    """Read rows bottom-to-top, and within each row left-to-right."""

    _require_tableau_like(tableau)
    word: list[int] = []
    for row in tableau:
        word.extend(row)
    return word


def tabsert(
    tableau: Sequence[Sequence[int]],
    inserted_row: Sequence[int],
    *,
    trace: bool = False,
) -> Tableau | tuple[Tableau, list[TabsertRowTrace]]:
    """Insert ``inserted_row`` through ``tableau`` using ``rowsert``.

    Existing rows are processed in source/paper top-to-bottom order, i.e.
    descending index order under bottom-to-top storage.  Inputs are copied and
    never mutated.  If ``trace`` is true, the returned pair is
    ``(updated_tableau, row_traces)``.
    """

    rows = _copied_tableau(tableau)
    if not is_dyck_tableau(rows):
        raise ValueError("tableau must be a valid Dyck tableau")
    if not is_dual_dyck(inserted_row):
        raise ValueError("inserted_row must be a dual Dyck sequence")

    evicted = list(inserted_row)
    traces: list[TabsertRowTrace] = []
    row_index = len(rows) - 1
    while evicted and row_index >= 0:
        input_row = tuple(rows[row_index])
        inserted = tuple(evicted)
        row_trace: list[RowsertStep] = []
        next_evicted, output_row = rowsert(rows[row_index], evicted, trace=row_trace)
        rows[row_index] = output_row
        evicted = next_evicted
        traces.append(
            TabsertRowTrace(
                row_index=row_index,
                input_row=input_row,
                inserted_row=inserted,
                evicted_row=tuple(evicted),
                output_row=tuple(output_row),
                rowsert_steps=tuple(row_trace),
            )
        )
        row_index -= 1

    if evicted:
        rows.insert(0, list(evicted))
        traces.append(
            TabsertRowTrace(
                row_index=0,
                input_row=(),
                inserted_row=tuple(evicted),
                evicted_row=(),
                output_row=tuple(evicted),
                rowsert_steps=(),
            )
        )

    if not is_dyck_tableau(rows):
        raise ValueError("tabsert output is not a valid Dyck tableau under the documented convention")
    return (rows, traces) if trace else rows


def reverse_tabsert(
    updated_tableau: Sequence[Sequence[int]],
    original_shape: Sequence[int],
    *,
    trace: bool = False,
) -> tuple[Tableau, list[int]] | tuple[Tableau, list[int], list[ReverseTabsertRowTrace]]:
    """Bounded rowwise reverse helper for red-team checks.

    ``original_shape`` is the list of original row lengths in bottom-to-top
    order.  Extra updated rows are interpreted as newly added bottom rows and
    initialize the accumulated sequence.  The helper then works through the
    original rows from bottom to top, reversing the corrected top-to-bottom
    forward insertion order.  At original row ``r`` it keeps the first
    ``original_shape[r]`` cells, peels terminal cells as the horizontal-strip
    contribution, runs corrected ``worsert`` on the accumulated sequence
    through the kept row, and passes ``F_minus + F_plus`` downward.  This is an
    executable approximation of the proof's inverse construction, intended for
    finite checks.
    """

    rows = _copied_tableau(updated_tableau)
    if not is_dyck_tableau(rows):
        raise ValueError("updated_tableau must be a valid Dyck tableau")
    if not isinstance(original_shape, (list, tuple)) or any(
        not isinstance(length, int) or length < 0 for length in original_shape
    ):
        raise TypeError("original_shape must be a sequence of non-negative row lengths")
    if len(original_shape) > len(rows):
        raise ValueError("original_shape has more rows than updated_tableau")

    offset = len(rows) - len(original_shape)
    if offset < 0:
        raise ValueError("updated_tableau has fewer rows than original_shape")

    recovered: Tableau = [[] for _ in original_shape]
    accumulated: list[int] = []
    traces: list[ReverseTabsertRowTrace] = []

    for row_index in range(offset):
        current_row = rows[row_index]
        accumulated_in = tuple(accumulated)
        accumulated = accumulated + list(current_row)
        traces.append(
            ReverseTabsertRowTrace(
                row_index=row_index,
                original_length=0,
                input_row=tuple(current_row),
                kept_row=(),
                peeled_row=tuple(current_row),
                accumulated_in=accumulated_in,
                recovered_row=(),
                accumulated_out=tuple(accumulated),
                worsert_steps=(),
            )
        )

    for original_index in range(len(original_shape)):
        row_index = offset + original_index
        current_row = rows[row_index]
        keep_length = original_shape[original_index]
        if keep_length > len(current_row):
            raise ValueError("original_shape cannot exceed updated row lengths")
        kept = list(current_row[:keep_length])
        peeled = list(current_row[keep_length:])
        wor_trace: list[WorsertStep] = []
        recovered_row, f_minus = worsert(accumulated, kept, trace=wor_trace)
        accumulated_out = list(f_minus) + peeled
        recovered[original_index] = recovered_row
        traces.append(
            ReverseTabsertRowTrace(
                row_index=row_index,
                original_length=keep_length,
                input_row=tuple(current_row),
                kept_row=tuple(kept),
                peeled_row=tuple(peeled),
                accumulated_in=tuple(accumulated),
                recovered_row=tuple(recovered_row),
                accumulated_out=tuple(accumulated_out),
                worsert_steps=tuple(wor_trace),
            )
        )
        accumulated = accumulated_out

    if not is_dyck_tableau(recovered):
        raise ValueError("reverse helper recovered an invalid Dyck tableau")
    if not is_dual_dyck(accumulated):
        raise ValueError("reverse helper recovered an invalid inserted row")
    result = (recovered, accumulated)
    return (*result, traces) if trace else result
```

### `docs/items/dyck_symmetric_functions/code/random_rational_dyck_checks.py`

```python
"""Monte Carlo checks for rational dual Dyck symmetric-function classes.

Each trial samples one word uniformly from ``{1, ..., A}^L``.  The sampled word
selects a multiset and dinv value; the checker then exhaustively verifies the
usual factorization-symmetry and Dyck-tableau prediction for that single class.
"""

from __future__ import annotations

import argparse
import random
import time
from collections import Counter
from dataclasses import dataclass
from multiprocessing import Pool

try:
    import numpy as np
    from numba import njit, types
    from numba.typed import Dict
except ImportError:  # pragma: no cover - fallback path for minimal environments.
    np = None
    njit = None
    types = None
    Dict = None

from check_rational_dyck_generalization import (
    CheckInput,
    Composition,
    Partition,
    PartitionMaskData,
    Shape,
    Word,
    composition_groups,
    count_ssyt_with_content,
    dyck_tableau_predictions,
    pair_dinv_table,
    partition_shapes,
    valid_factorization_counts_by_cut_mask,
)


if njit is not None:

    @njit
    def _jit_class_word_extend(
        position: int,
        previous_index: int,
        dinv: int,
        required_dual_cuts: int,
        active_count: int,
        target_dinv: int,
        length: int,
        alphabet_size: int,
        step: int,
        pair_dinv_array: np.ndarray,
        remaining: np.ndarray,
        used_counts: np.ndarray,
        active_indices: np.ndarray,
        mask_counts: Dict,
    ) -> None:
        if dinv > target_dinv:
            return
        if position == length:
            if dinv == target_dinv:
                mask_counts[required_dual_cuts] = mask_counts.get(required_dual_cuts, 0) + 1
            return

        for value_index in range(alphabet_size):
            if remaining[value_index] == 0:
                continue
            dinv_increment = 0
            for active_position in range(active_count):
                earlier_index = active_indices[active_position]
                dinv_increment += used_counts[earlier_index] * pair_dinv_array[earlier_index, value_index]
            next_dinv = dinv + dinv_increment
            if next_dinv > target_dinv:
                continue

            next_required_dual_cuts = required_dual_cuts
            if position > 0 and value_index <= previous_index + step:
                next_required_dual_cuts |= 1 << (position - 1)

            next_active_count = active_count
            if used_counts[value_index] == 0:
                active_indices[next_active_count] = value_index
                next_active_count += 1
            remaining[value_index] -= 1
            used_counts[value_index] += 1
            _jit_class_word_extend(
                position + 1,
                value_index,
                next_dinv,
                next_required_dual_cuts,
                next_active_count,
                target_dinv,
                length,
                alphabet_size,
                step,
                pair_dinv_array,
                remaining,
                used_counts,
                active_indices,
                mask_counts,
            )
            used_counts[value_index] -= 1
            remaining[value_index] += 1


    @njit
    def _jit_class_word_mask_counts(
        counts: np.ndarray,
        target_dinv: int,
        length: int,
        alphabet_size: int,
        step: int,
        pair_dinv_array: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray]:
        remaining = counts.copy()
        used_counts = np.zeros(alphabet_size, dtype=np.int64)
        active_indices = np.empty(alphabet_size, dtype=np.int64)
        mask_counts = Dict.empty(key_type=types.int64, value_type=types.int64)
        _jit_class_word_extend(
            0,
            0,
            0,
            0,
            0,
            target_dinv,
            length,
            alphabet_size,
            step,
            pair_dinv_array,
            remaining,
            used_counts,
            active_indices,
            mask_counts,
        )
        keys = np.empty(len(mask_counts), dtype=np.int64)
        values = np.empty(len(mask_counts), dtype=np.int64)
        index = 0
        for key, value in mask_counts.items():
            keys[index] = key
            values[index] = value
            index += 1
        return keys, values

else:
    _jit_class_word_mask_counts = None


@dataclass(frozen=True)
class RandomCheckInput:
    step: int
    alphabet_size: int
    length: int
    iterations: int
    timeout_seconds: float | None
    seed: int | None
    workers: int = 1


@dataclass
class RandomCheckResult:
    params: RandomCheckInput
    iterations_completed: int = 0
    sampled_words: int = 0
    class_words_checked: int = 0
    dyck_tableaux_checked: int = 0
    partition_classes_checked: int = 0
    compositions_checked: int = 0
    elapsed_seconds: float = 0.0


@dataclass
class TrialSummary:
    iteration: int
    sample_word: Word
    target_dinv: int
    class_words: int
    tableaux: int
    partition_classes: int
    compositions: int
    elapsed_seconds: float


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def random_word(*, length: int, alphabet_size: int, rng: random.Random) -> Word:
    return tuple(rng.randint(1, alphabet_size) for _ in range(length))


def counts_from_word(word: Word, *, alphabet_size: int) -> tuple[int, ...]:
    counts = [0] * alphabet_size
    for value in word:
        counts[value - 1] += 1
    return tuple(counts)


def multiset_from_counts(counts: tuple[int, ...]) -> Word:
    values: list[int] = []
    for index, multiplicity in enumerate(counts, start=1):
        values.extend([index] * multiplicity)
    return tuple(values)


def word_dinv(word: Word, pair_dinv: tuple[tuple[int, ...], ...]) -> int:
    total = 0
    for right in range(len(word)):
        right_index = word[right] - 1
        for left in range(right):
            total += pair_dinv[word[left] - 1][right_index]
    return total


def class_word_mask_counts(
    *,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> Counter[int]:
    if _jit_class_word_mask_counts is not None:
        counts_array = np.array(counts, dtype=np.int64)
        pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
        keys, values = _jit_class_word_mask_counts(
            counts_array,
            target_dinv,
            params.length,
            params.alphabet_size,
            params.step,
            pair_dinv_array,
        )
        return Counter({int(key): int(value) for key, value in zip(keys, values)})

    remaining = list(counts)
    used_counts = [0] * params.alphabet_size
    active_indices: list[int] = []
    mask_counts: Counter[int] = Counter()

    def extend(position: int, previous_index: int, dinv: int, required_dual_cuts: int) -> None:
        if dinv > target_dinv:
            return
        if position == params.length:
            if dinv == target_dinv:
                mask_counts[required_dual_cuts] += 1
            return

        for value_index in range(params.alphabet_size):
            if remaining[value_index] == 0:
                continue
            dinv_increment = 0
            for earlier_index in active_indices:
                dinv_increment += used_counts[earlier_index] * pair_dinv[earlier_index][value_index]
            next_dinv = dinv + dinv_increment
            if next_dinv > target_dinv:
                continue

            next_required_dual_cuts = required_dual_cuts
            if position > 0 and value_index <= previous_index + params.step:
                next_required_dual_cuts |= 1 << (position - 1)

            first_value = used_counts[value_index] == 0
            if first_value:
                active_indices.append(value_index)
            remaining[value_index] -= 1
            used_counts[value_index] += 1
            extend(position + 1, value_index, next_dinv, next_required_dual_cuts)
            used_counts[value_index] -= 1
            remaining[value_index] += 1
            if first_value:
                active_indices.pop()

    extend(0, 0, 0, 0)
    return mask_counts


def class_tableau_shape_counts(
    *,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> Counter[Shape]:
    shape_counts: Counter[Shape] = Counter()

    for shape in partition_shapes(params.length):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(row_length)] for row_length in shape]
        remaining = list(counts)
        used_counts = [0] * params.alphabet_size
        active_indices: list[int] = []

        def fill(cell_index: int, dinv: int) -> None:
            if dinv > target_dinv:
                return
            if cell_index == len(cells):
                if dinv == target_dinv:
                    shape_counts[shape] += 1
                return

            row, col = cells[cell_index]
            lower = 1
            if col > 0:
                lower = rows[row][col - 1] + params.step + 1
            upper = params.alphabet_size
            if row + 1 < len(shape) and col < shape[row + 1]:
                upper = min(upper, rows[row + 1][col] + params.step)

            for value in range(lower, upper + 1):
                value_index = value - 1
                if remaining[value_index] == 0:
                    continue
                dinv_increment = 0
                for earlier_index in active_indices:
                    dinv_increment += used_counts[earlier_index] * pair_dinv[earlier_index][value_index]
                next_dinv = dinv + dinv_increment
                if next_dinv > target_dinv:
                    continue

                first_value = used_counts[value_index] == 0
                if first_value:
                    active_indices.append(value_index)
                remaining[value_index] -= 1
                used_counts[value_index] += 1
                rows[row][col] = value
                fill(cell_index + 1, next_dinv)
                rows[row][col] = 0
                used_counts[value_index] -= 1
                remaining[value_index] += 1
                if first_value:
                    active_indices.pop()

        fill(0, 0)

    return shape_counts


def verify_sampled_class(
    *,
    sample_word: Word,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
    partitions: list[PartitionMaskData],
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> tuple[int, int, int, int]:
    mask_counts = class_word_mask_counts(
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
    )
    class_word_count = sum(mask_counts.values())
    require(
        class_word_count > 0,
        f"internal error: sampled word class is empty for word={sample_word}, dinv={target_dinv}",
    )
    shape_counts = class_tableau_shape_counts(
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
    )
    valid_by_cut_mask = valid_factorization_counts_by_cut_mask(mask_counts, length=params.length)
    predictions = dyck_tableau_predictions(
        shape_counts,
        partitions,
        ssyt_cache=ssyt_cache,
        prediction_cache=prediction_cache,
    )
    multiset = multiset_from_counts(counts)
    partition_classes_checked = 0
    compositions_checked = 0

    for partition_index, (partition, compositions, cut_masks) in enumerate(partitions):
        actual = valid_by_cut_mask[cut_masks[0]]
        for cut_mask in cut_masks[1:]:
            if valid_by_cut_mask[cut_mask] != actual:
                values = {
                    composition: valid_by_cut_mask[composition_cut_mask]
                    for composition, composition_cut_mask in zip(compositions, cut_masks)
                }
                examples = sorted(values.items())[:8]
                raise AssertionError(
                    "factorization symmetry mismatch: "
                    f"t={params.step}, sample_word={sample_word}, multiset={multiset}, "
                    f"dinv={target_dinv}, partition={partition}, examples={examples}"
                )
        predicted = predictions[partition_index]
        if actual != predicted:
            values = {
                composition: valid_by_cut_mask[composition_cut_mask]
                for composition, composition_cut_mask in zip(compositions, cut_masks)
            }
            examples = sorted(values.items())[:8]
            raise AssertionError(
                "Dyck-tableau prediction mismatch: "
                f"t={params.step}, sample_word={sample_word}, multiset={multiset}, "
                f"dinv={target_dinv}, partition={partition}, factorization_count={actual}, "
                f"tableau_prediction={predicted}, examples={examples}"
            )
        partition_classes_checked += 1
        compositions_checked += len(compositions)

    return class_word_count, sum(shape_counts.values()), partition_classes_checked, compositions_checked


def run_one_trial(
    *,
    iteration: int,
    seed: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
    partitions: list[PartitionMaskData],
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> TrialSummary:
    rng = random.Random(seed)
    sample_start = time.perf_counter()
    sample_word = random_word(length=params.length, alphabet_size=params.alphabet_size, rng=rng)
    counts = counts_from_word(sample_word, alphabet_size=params.alphabet_size)
    target_dinv = word_dinv(sample_word, pair_dinv)
    class_words, tableaux, partition_classes, compositions = verify_sampled_class(
        sample_word=sample_word,
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
        partitions=partitions,
        ssyt_cache=ssyt_cache,
        prediction_cache=prediction_cache,
    )
    return TrialSummary(
        iteration=iteration,
        sample_word=sample_word,
        target_dinv=target_dinv,
        class_words=class_words,
        tableaux=tableaux,
        partition_classes=partition_classes,
        compositions=compositions,
        elapsed_seconds=time.perf_counter() - sample_start,
    )


def run_trial_batch(args: tuple[RandomCheckInput, list[tuple[int, int]]]) -> list[TrialSummary]:
    params, trials = args
    pair_dinv = pair_dinv_table(CheckInput(params.step, params.alphabet_size, params.length))
    partitions = composition_groups(params.length)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    return [
        run_one_trial(
            iteration=iteration,
            seed=seed,
            params=params,
            pair_dinv=pair_dinv,
            partitions=partitions,
            ssyt_cache=ssyt_cache,
            prediction_cache=prediction_cache,
        )
        for iteration, seed in trials
    ]


def print_trial_summary(summary: TrialSummary) -> None:
    print(
        f"  iteration={summary.iteration}: word={summary.sample_word}, dinv={summary.target_dinv}, "
        f"class words={summary.class_words}, tableaux={summary.tableaux}, "
        f"elapsed={summary.elapsed_seconds:.3f}s",
        flush=True,
    )


def run_random_checks(params: RandomCheckInput) -> RandomCheckResult:
    require(params.step >= 0, "t must be non-negative")
    require(params.alphabet_size > 0, "alphabet size A must be positive")
    require(params.length > 0, "length L must be positive")
    require(params.iterations >= 0, "iterations must be non-negative")
    require(params.timeout_seconds is None or params.timeout_seconds > 0, "timeout must be positive")
    require(params.iterations > 0 or params.timeout_seconds is not None, "use iterations, timeout, or both")
    require(params.workers > 0, "workers must be positive")

    result = RandomCheckResult(params=params)
    seed_rng = random.Random(params.seed)
    pair_dinv = pair_dinv_table(CheckInput(params.step, params.alphabet_size, params.length))
    partitions = composition_groups(params.length)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    start = time.perf_counter()

    if params.workers > 1 and params.timeout_seconds is None:
        trials = [
            (iteration, seed_rng.randrange(0, 2**63))
            for iteration in range(1, params.iterations + 1)
        ]
        batches = [[] for _ in range(min(params.workers, len(trials)))]
        for index, trial in enumerate(trials):
            batches[index % len(batches)].append(trial)
        with Pool(processes=len(batches)) as pool:
            batch_results = pool.map(run_trial_batch, [(params, batch) for batch in batches if batch])
        summaries = sorted((summary for batch in batch_results for summary in batch), key=lambda item: item.iteration)
        for summary in summaries:
            print_trial_summary(summary)
            result.iterations_completed += 1
            result.sampled_words += 1
            result.class_words_checked += summary.class_words
            result.dyck_tableaux_checked += summary.tableaux
            result.partition_classes_checked += summary.partition_classes
            result.compositions_checked += summary.compositions
        result.elapsed_seconds = time.perf_counter() - start
        return result

    while result.iterations_completed < params.iterations or params.timeout_seconds is not None:
        if params.iterations and result.iterations_completed >= params.iterations:
            break
        elapsed = time.perf_counter() - start
        if params.timeout_seconds is not None and elapsed >= params.timeout_seconds:
            break

        summary = run_one_trial(
            iteration=result.iterations_completed + 1,
            seed=seed_rng.randrange(0, 2**63),
            params=params,
            pair_dinv=pair_dinv,
            partitions=partitions,
            ssyt_cache=ssyt_cache,
            prediction_cache=prediction_cache,
        )
        result.iterations_completed += 1
        result.sampled_words += 1
        result.class_words_checked += summary.class_words
        result.dyck_tableaux_checked += summary.tableaux
        result.partition_classes_checked += summary.partition_classes
        result.compositions_checked += summary.compositions
        print_trial_summary(summary)

    result.elapsed_seconds = time.perf_counter() - start
    return result


def print_result(result: RandomCheckResult) -> None:
    params = result.params
    print(f"completed random checks: t={params.step}, alphabet={{1,...,{params.alphabet_size}}}, length={params.length}")
    print(f"  iterations completed: {result.iterations_completed}")
    print(f"  sampled words: {result.sampled_words}")
    print(f"  class words checked: {result.class_words_checked}")
    print(f"  Dyck tableaux checked: {result.dyck_tableaux_checked}")
    print(f"  partition classes checked: {result.partition_classes_checked}")
    print(f"  positive compositions checked: {result.compositions_checked}")
    print(f"  elapsed: {result.elapsed_seconds:.3f}s")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, required=True, help="Rational step t.")
    parser.add_argument("--alphabet-size", "-A", type=int, required=True, help="Alphabet size A.")
    parser.add_argument("--length", "-L", type=int, required=True, help="Sampled word length.")
    parser.add_argument("--iterations", type=int, default=100, help="Maximum sampled classes to check.")
    parser.add_argument("--timeout-seconds", type=float, default=None, help="Optional wall-clock timeout.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed.")
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Parallel worker processes for fixed-iteration runs.",
    )
    args = parser.parse_args()

    result = run_random_checks(
        RandomCheckInput(
            step=args.t,
            alphabet_size=args.alphabet_size,
            length=args.length,
            iterations=args.iterations,
            timeout_seconds=args.timeout_seconds,
            seed=args.seed,
            workers=args.workers,
        )
    )
    print_result(result)
    print("all sampled finite checks passed")


if __name__ == "__main__":
    main()
```

### `docs/items/dyck_symmetric_functions/code/README.md`

```markdown
# Code

Purpose: reproduce the executable parts curated for the Dyck symmetric
functions item.

## Classical Insertion Algorithm

Command:

````text
python classical_insertion_demo.py
````

This script traces the classical row insertion operation and a tableau
insertion example.  The implementation lives in:

- `paper_algorithms/row_insertion.py`
- `paper_algorithms/tableau_insertion.py`

These files are adapted from the 2026 preprint code.  They implement the
insertion algorithm used to prove Schur positivity for the classical dual Dyck
symmetric functions.

## Rational Dual Finite Checks

Command:

````text
python check_rational_dyck_generalization.py --t 2 --alphabet-size 4 --max-length 4
````

Official repository checks:

````text
python check_rational_dyck_generalization.py --t 2 -A 10 -L 10
python check_rational_dyck_generalization.py --t 3 -A 13 -L 9
python check_rational_dyck_generalization.py --t 4 -A 16 -L 8
````

Dependencies: Python standard library only for the portable fallback.  If
`numpy` and `numba` are installed, the checker automatically uses a compiled
word-grouping backend.  Compiled word scans with at least 50 million generated
words are split across worker processes automatically; use `--workers 1` to
force serial execution, a positive `--workers N` to force `N` workers, or
`DYCK_CHECK_WORKERS=N` to set the default from the environment.

Inputs are explicit and minimal:

- `--t`: rational step.
- `--alphabet-size` or `-A`: alphabet size, using `{1,2,...,A}`.
- `--max-length` or `-L`: checks every length `1 <= l <= L`.

For each length the checker:

- constructs every word over `{1,2,...,A}` that contains `1`;
- groups words by underlying multiset and rational dinv;
- generates every positive composition of the length and groups compositions
  by their sorted underlying partition;
- verifies that, for each multiset, dinv, and partition, every distinct
  composition in that partition gives the same number of valid dual Dyck
  factorizations;
- compares that common factorization count with the Dyck-tableau prediction
  obtained by summing, over rational Dyck tableaux with that multiset and
  dinv, the number of SSYT of the tableau shape with the given dominant
  content.

The implementation keeps the useful cut-mask optimization from the older
checker: a word contributes a bitmask of adjacent positions that must be cut
for a dual factorization, and a positive composition is valid exactly when its
cut mask contains that required mask.  With NumPy and Numba available, word
grouping is performed by a compiled exhaustive scan that aggregates compact
integer records for `(multiset, dinv, cut mask)` and then feeds the same Python
verification pipeline.  For sufficiently large word universes, that compiled
scan is partitioned across worker processes and the compact aggregate records
are merged before verification.  Without those optional dependencies, word grouping
falls back to the pure-Python first-`1` generator, which counts words with no
`1` in the reported universe size but never traverses them.  Tableau grouping
uses the same first-`1` idea, fixing the first tableau cell containing `1` and
avoiding terminal rejection of tableaux with no `1`.  Internally, multiset keys
are compact integer encodings during each fixed-length pass, Dyck-tableau
predictions are cached by shape-count profile, and factorization counts use
cached cut-mask subset sums.  The code no longer has a variable-count
parameter, affine/dual/both option, or compressed/full comparison modes.

Interpretation: these are bounded computational checks of the conjectural
`r = s*t + 1` analogue.  They are not a proof of the general conjecture.

## Random Class Checks

Command:

````text
python random_rational_dyck_checks.py --t 2 -A 10 -L 10 --iterations 100 --seed 1
````

This Monte Carlo checker samples words uniformly from `{1,2,...,A}^L`.  Each
sampled word determines a multiset and rational dinv value.  The script then
forgets the sampled order and exhaustively checks the full class with that
multiset and dinv:

- all words with the sampled multiset and dinv are enumerated;
- factorization counts are checked for symmetry across compositions with the
  same underlying partition;
- the common counts are compared with the corresponding Dyck-tableau
  prediction.

Unlike the exhaustive checker, this script does not restrict to words
containing `1`; the sampled word may use any letters in the alphabet.
When NumPy and Numba are installed, the fixed-multiset word-class enumeration
is JIT-compiled automatically; the pure-Python implementation remains as a
portable fallback.

Stopping controls:

- `--iterations N`: maximum sampled classes to check.
- `--timeout-seconds S`: optional wall-clock timeout.
- `--seed N`: optional reproducible random seed.
- `--workers N`: parallel worker processes for fixed-iteration runs.  Timeout
  driven runs currently execute serially.
```

### `docs/items/dyck_symmetric_functions/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 203874
sha256: 9520c0c81d95e594bfdc6b9616e3b6c9b2af76d3b02d5d8261f40b0d899b6275
```

### `docs/items/dyck_symmetric_functions/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\newcommand{\dinv}{\operatorname{dinv}}
\newcommand{\DS}{\operatorname{DS}}
\newcommand{\DSstar}{\operatorname{DS}^{\ast}}
\newtheorem{theorem}{Theorem}
\newtheorem{conjecture}{Conjecture}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

\title{Dyck Symmetric Functions}
\author{}
\date{}

\begin{document}
\maketitle

\section{Status}

This note records the status of Dyck symmetric functions in the curated
repository.  The degenerate step \(t=0\) case is classical RSK/dual-RSK
combinatorics.  The classical Dyck step \(t=1\) case is proved in the 2026
preprint
\emph{Dyck Symmetric Functions and Applications to \(q,t\)-Catalan
Polynomials}.  The proof first establishes the dual case by an explicit
tableau insertion algorithm and then derives the affine, or nondual, case
from the dual case using the standard involution on symmetric functions.

The \(r=s t+1\) analogue below is conjectural for \(t>1\).  The accompanying
code checks systematic finite parameter boxes for both the affine and dual
identities.

\section{The \(r=s t+1\) Setup}

Fix a nonnegative integer step parameter \(t\).  For any finite integer
sequence \(x=(x_0,\ldots,x_{\ell-1})\), set
\[
  \dinv_t(x)=
  \sum_{0\le i<j<\ell} d_t(x_i,x_j),
\]
where
\[
  d_t(a,b)=
  \begin{cases}
    \max(0,a+t-b),& a\le b,\\
    \max(0,b+1+t-a),& a>b.
  \end{cases}
\]
An \emph{affine rational Dyck sequence of step \(t\)} is a finite integer
sequence satisfying
\[
  x_{i+1}\le x_i+t
  \qquad\text{for all }i.
\]
A \emph{dual rational Dyck sequence of step \(t\)} is a finite integer
sequence satisfying
\[
  x_{i+1}>x_i+t
  \qquad\text{for all }i.
\]

Let \(S\) be a finite multiset of integers.  A factorization of \(S\) is a
sequence of finite words whose concatenation is a rearrangement of \(S\).  It
is affine, respectively dual, if each factor is an affine, respectively dual,
rational Dyck sequence of step \(t\).  Define
\[
  \DS^{(t)}(S,d;\mathbf x)
  =
  \sum_{\substack{\mathcal F\text{ affine factorization of }S\\
                  \dinv_t(F_0F_1F_2\cdots)=d}}
  x^{\mathcal F}
\]
and
\[
  {\DSstar}^{(t)}(S,d;\mathbf x)
  =
  \sum_{\substack{\mathcal F\text{ dual factorization of }S\\
                  \dinv_t(F_0F_1F_2\cdots)=d}}
  x^{\mathcal F}.
\]

A rational Dyck tableau of step \(t\) is a left-aligned tableau whose rows are
dual rational Dyck sequences of step \(t\), and whose columns, read from
bottom to top, are affine rational Dyck sequences of step \(t\).  Let
\(\lambda(P)\) be its shape and let \(\operatorname{RR}(P)\) be its
row-reading word.

\section{The Degenerate \(t=0\) Case}

When \(t=0\), one has \(d_0(a,b)=0\) for all entries \(a,b\), so every
rearrangement of a fixed multiset lies in the single dinv class \(d=0\).
The dual factors are strictly increasing words, while the affine factors are
weakly increasing words.  The rational Dyck tableaux of step \(0\) are exactly
row-strict semistandard tableaux in our orientation: rows are strictly
increasing and columns are weakly increasing.

Thus the step \(0\) dual identity is the classical dual RSK correspondence for
strict biwords.  Fix a multiset \(S\) and a composition
\(\alpha=(\alpha_1,\ldots,\alpha_k)\).  A dual factorization of weight
\(\alpha\) is encoded as a biword whose top row contains \(i\) repeated
\(\alpha_i\) times and whose bottom row is the corresponding factor.  The
strictness of each factor is precisely the strictness condition in the
dual-RSK input.  Dual RSK gives a bijection with pairs \((P,Q)\) of common
shape, where \(P\) is row-strict semistandard of content \(S\), and \(Q\) is
ordinary semistandard of content \(\alpha\).  Equivalently, after transposing
or reversing the usual row/column conventions, this is the standard
RSK/Kostka description of Schur coefficients.

The affine \(t=0\) identity is the corresponding ordinary RSK statement for
weakly increasing factors, with the recording tableau convention transposed by
the usual involution.  Consequently the \(t=0\) specialization is known by
classical RSK theory; it is the baseline that the \(t=1\) insertion theorem
and the \(t>1\) conjectures generalize.

\section{Classical Theorem}

\begin{theorem}[Classical dual Dyck symmetric functions]
For every finite multiset \(S\) and every \(d\ge0\), the classical dual Dyck
symmetric function satisfies
\[
  \DSstar(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)}(\mathbf x),
\]
where \(P\) ranges over classical Dyck tableaux with entries \(S\) and
\(\dinv(\operatorname{RR}(P))=d\).
\end{theorem}

\begin{remark}
The proof in the 2026 preprint is constructive.  It gives an explicit
insertion algorithm sending dual Dyck factorizations to Dyck tableaux together
with semistandard recording data.  The local row insertion is iterated through
the rows of a tableau, and the reverse insertion proves bijectivity.
\end{remark}

\begin{theorem}[Classical affine Dyck symmetric functions]
For every finite multiset \(S\) and every \(d\ge0\), the classical affine Dyck
symmetric function satisfies
\[
  \DS(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)'}(\mathbf x),
\]
where the indexing set \(P\) is the same set of classical Dyck tableaux.
\end{theorem}

\begin{remark}
In the preprint, this nondual statement is derived from the dual statement by
comparing the fundamental-quasisymmetric expansions and applying the standard
involution \(\omega\), which sends \(s_\lambda\) to \(s_{\lambda'}\).
\end{remark}

\section{Conjectural \(r=s t+1\) Analogue}

\begin{conjecture}[Rational Dyck symmetric functions, \(r=s t+1\)]
Let \(S\) be a finite multiset of integers, let \(d\ge0\), and fix \(t\ge0\).
Then
\[
  \DS^{(t)}(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)'}(\mathbf x),
\]
where \(P\) ranges over rational Dyck tableaux of step \(t\) whose entries
are exactly \(S\) and whose row-reading word satisfies
\[
  \dinv_t(\operatorname{RR}(P))=d.
\]
Similarly,
\[
  {\DSstar}^{(t)}(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)}(\mathbf x),
\]
with the same indexing set of rational Dyck tableaux.
\end{conjecture}

\begin{remark}
The displayed statement is known for \(t=0\) by the classical RSK and dual
RSK correspondences, and for \(t=1\) by the 2026 Dyck insertion theorem.  For
\(t>1\), it is currently treated as a conjecture.  The directory
\texttt{code/} includes systematic finite checks over bounded multisets and
all occurring dinv values for the following official parameter boxes:
\[
  (t,A,L)=(2,10,10),\qquad (3,13,9),\qquad (4,16,8),
\]
where \(A\) is the alphabet size \(\{1,\ldots,A\}\) and \(L\) is the maximum
word length.  The same directory also includes Monte Carlo class checks: each
trial samples a word uniformly from \(\{1,\ldots,A\}^L\), fixes its multiset
and dinv value, and then exhaustively checks that sampled class.  The official
Monte Carlo runs use \(100\) sampled classes for
\[
  (t,A,L)=(2,11,12),\qquad (3,14,11),\qquad (4,17,10).
\]
The directory also includes the classical insertion algorithm code used for
the theorem-level case.
\end{remark}

\end{document}
```

### `docs/items/dyck_symmetric_functions/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dyck Symmetric Functions</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>Dyck Symmetric Functions</h1>
    <p>Classical Dyck symmetric functions are proved in the 2026 preprint; the r == 1 mod s analogue is conjectural with systematic finite checks.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.pdf">View PDF</a></li>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<style>
  .dsf-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.1fr) minmax(280px, 0.9fr);
    gap: 1.25rem;
    align-items: start;
  }
  .dsf-panel {
    border: 1px solid #d7dde5;
    border-radius: 8px;
    padding: 1rem;
    background: #fff;
  }
  .dsf-toolbar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0.75rem 0;
  }
  .dsf-toolbar button,
  .dsf-toolbar select {
    border: 1px solid #a9b4c2;
    background: #f8fafc;
    border-radius: 6px;
    padding: 0.45rem 0.65rem;
    font: inherit;
  }
  .dsf-toolbar button:disabled {
    color: #8a94a3;
    background: #eef1f5;
  }
  .dsf-tableau {
    display: flex;
    flex-direction: column-reverse;
    gap: 0.35rem;
    min-height: 9rem;
    padding: 0.75rem;
    border: 1px solid #e4e8ee;
    background: #fbfcfe;
  }
  .dsf-row {
    display: flex;
    gap: 0.35rem;
    align-items: center;
  }
  .dsf-row-label {
    width: 4.25rem;
    color: #586272;
    font-size: 0.85rem;
  }
  .dsf-cell {
    min-width: 2.1rem;
    height: 2.1rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #8694a6;
    background: #ffffff;
    border-radius: 5px;
    font-weight: 600;
  }
  .dsf-active .dsf-cell {
    border-color: #1b6ca8;
    background: #eef7ff;
  }
  .dsf-insert .dsf-cell {
    border-color: #986b12;
    background: #fff7e6;
  }
  .dsf-evicted .dsf-cell {
    border-color: #7b3f98;
    background: #f8efff;
  }
  .dsf-log {
    min-height: 8rem;
    max-height: 14rem;
    overflow: auto;
    padding: 0.75rem;
    background: #101820;
    color: #e7edf3;
    border-radius: 6px;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    font-size: 0.86rem;
    white-space: pre-wrap;
  }
  .dsf-example-list {
    display: grid;
    gap: 0.75rem;
  }
  .dsf-example {
    border-left: 4px solid #1b6ca8;
    padding: 0.65rem 0.75rem;
    background: #f8fafc;
  }
  .dsf-kv {
    display: grid;
    grid-template-columns: 9rem minmax(0, 1fr);
    gap: 0.2rem 0.65rem;
    font-size: 0.92rem;
  }
  @media (max-width: 780px) {
    .dsf-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<section class="dsf-grid">
  <div class="dsf-panel">
    <h2>Insertion Walkthrough</h2>
    <p>
      The classical dual theorem is proved by inserting dual Dyck rows through
      a tableau.  Choose an example and step through the same row insertion
      logic used by the code.
    </p>
    <div class="dsf-toolbar">
      <select id="dsf-example"></select>
      <button id="dsf-reset" type="button">Reset</button>
      <button id="dsf-row-step" type="button">Apply row step</button>
      <button id="dsf-next-row" type="button">Move to next row</button>
    </div>
    <div id="dsf-tableau" class="dsf-tableau" aria-live="polite"></div>
    <div class="dsf-toolbar">
      <div id="dsf-carry" class="dsf-row dsf-insert"></div>
      <div id="dsf-evicted" class="dsf-row dsf-evicted"></div>
    </div>
    <div id="dsf-log" class="dsf-log"></div>
  </div>

  <div class="dsf-panel">
    <h2>Rational Examples</h2>
    <p>
      For \(r=s t+1\), the Schur-positive identities are conjectural for
      \(t&gt;1\).  The included checker verifies the following finite cases.
    </p>
    <div class="dsf-example-list">
      <div class="dsf-example">
        <strong>Step \(t=2\)</strong>
        <div class="dsf-kv">
          <span>Multiset</span><span>{1,2,2,3,3,4,5,7}</span>
          <span>Target dinv</span><span>17</span>
          <span>Tableaux</span><span>94</span>
          <span>Shapes</span><span>(2,2,1,1,1,1), (2,1,1,1,1,1,1), (1^8)</span>
          <span>Phenomenon</span><span>large affine side; ordinary-shape dual side vanishes in three variables because all shapes have more than three rows.</span>
        </div>
      </div>
      <div class="dsf-example">
        <strong>Step \(t=3\)</strong>
        <div class="dsf-kv">
          <span>Multiset</span><span>{0,0,0,4}</span>
          <span>Target dinv</span><span>9</span>
          <span>Tableaux</span><span>2</span>
          <span>Shapes</span><span>(2,1,1), (1,1,1,1)</span>
          <span>Phenomenon</span><span>both affine and dual Schur comparisons are nonzero in three variables.</span>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
(function () {
  const examples = [
    {
      name: "Single bump and append",
      tableau: [[0, 3, 6]],
      inserted: [1, 4],
      note: "Shows replacement followed by a terminal append."
    },
    {
      name: "Two-row propagation",
      tableau: [[0, 4], [1, 5]],
      inserted: [2, 6],
      note: "An evicted row is carried upward into the next row."
    },
    {
      name: "Chain comparison",
      tableau: [[0, 2, 4], [1, 4, 7]],
      inserted: [1, 3, 5],
      note: "Shows a maximal +2-chain interaction."
    }
  ];

  const select = document.getElementById("dsf-example");
  const resetButton = document.getElementById("dsf-reset");
  const rowStepButton = document.getElementById("dsf-row-step");
  const nextRowButton = document.getElementById("dsf-next-row");
  const tableauNode = document.getElementById("dsf-tableau");
  const carryNode = document.getElementById("dsf-carry");
  const evictedNode = document.getElementById("dsf-evicted");
  const logNode = document.getElementById("dsf-log");

  let state;

  examples.forEach((example, index) => {
    const option = document.createElement("option");
    option.value = String(index);
    option.textContent = example.name;
    select.appendChild(option);
  });

  function cloneRows(rows) {
    return rows.map(row => row.slice());
  }

  function chainStartingAt(seq, index) {
    let stop = index + 1;
    while (stop < seq.length && seq[stop] === seq[stop - 1] + 2) stop += 1;
    return seq.slice(index, stop);
  }

  function rowsertOne(row, carry) {
    const first = carry[0];
    let index = row.findIndex(value => first <= value + 1);
    if (index === -1) {
      row.push(first);
      carry.shift();
      return { caseName: "Case 0", message: `${first} appends to the row.` };
    }
    if (first <= row[index]) {
      const old = row[index];
      row[index] = first;
      carry.shift();
      return { caseName: "Case 1", evicted: [old], message: `${first} replaces ${old}.` };
    }
    const rowChain = chainStartingAt(row, index);
    const carryChain = chainStartingAt(carry, 0);
    if (rowChain.length <= carryChain.length) {
      const inserted = carry.splice(0, rowChain.length);
      const evicted = row.splice(index, rowChain.length, ...inserted);
      return {
        caseName: "Case 2",
        evicted,
        message: `The input chain [${inserted.join(", ")}] replaces row chain [${evicted.join(", ")}].`
      };
    }
    const moved = carry.splice(0, carryChain.length);
    return {
      caseName: "Case 3",
      evicted: moved,
      message: `The shorter input chain [${moved.join(", ")}] passes upward.`
    };
  }

  function renderRow(label, values, className) {
    const row = document.createElement("div");
    row.className = `dsf-row ${className || ""}`;
    const labelNode = document.createElement("span");
    labelNode.className = "dsf-row-label";
    labelNode.textContent = label;
    row.appendChild(labelNode);
    values.forEach(value => {
      const cell = document.createElement("span");
      cell.className = "dsf-cell";
      cell.textContent = String(value);
      row.appendChild(cell);
    });
    if (!values.length) {
      const empty = document.createElement("span");
      empty.textContent = "empty";
      empty.style.color = "#6b7280";
      row.appendChild(empty);
    }
    return row;
  }

  function render() {
    tableauNode.innerHTML = "";
    state.rows.forEach((row, index) => {
      const active = index === state.rowIndex && state.carry.length ? "dsf-active" : "";
      tableauNode.appendChild(renderRow(`row ${index}`, row, active));
    });
    carryNode.innerHTML = "";
    carryNode.appendChild(renderRow("carry", state.carry, "dsf-insert"));
    evictedNode.innerHTML = "";
    evictedNode.appendChild(renderRow("evicted", state.evicted, "dsf-evicted"));
    logNode.textContent = state.log.join("\n");
    rowStepButton.disabled = !(state.carry.length && state.rowIndex >= 0);
    nextRowButton.disabled = state.carry.length || state.rowIndex < 0 || !state.evicted.length;
  }

  function reset() {
    const example = examples[Number(select.value)];
    state = {
      rows: cloneRows(example.tableau),
      carry: example.inserted.slice(),
      rowIndex: example.tableau.length - 1,
      evicted: [],
      log: [`Example: ${example.name}`, example.note, `Initial inserted row: [${example.inserted.join(", ")}]`]
    };
    render();
  }

  rowStepButton.addEventListener("click", () => {
    if (!state.carry.length || state.rowIndex < 0) return;
    const result = rowsertOne(state.rows[state.rowIndex], state.carry);
    const chunk = result.evicted || [];
    state.evicted.push(...chunk);
    state.log.push(`row ${state.rowIndex}: ${result.caseName}. ${result.message}`);
    if (!state.carry.length) {
      if (state.evicted.length) {
        state.log.push(`row ${state.rowIndex}: row complete; evicted row [${state.evicted.join(", ")}] is ready to move upward.`);
      } else {
        state.log.push(`row ${state.rowIndex}: insertion stops in this row.`);
      }
    }
    render();
  });

  nextRowButton.addEventListener("click", () => {
    state.rowIndex -= 1;
    if (state.rowIndex < 0 && state.evicted.length) {
      state.rows.unshift(state.evicted.slice());
      state.rowIndex = -1;
      state.log.push(`A new bottom row [${state.evicted.join(", ")}] is created.`);
      state.evicted = [];
    } else if (state.rowIndex >= 0) {
      state.carry = state.evicted.slice();
      state.evicted = [];
      state.log.push(`Move to row ${state.rowIndex}.`);
    }
    render();
  });

  select.addEventListener("change", reset);
  resetButton.addEventListener("click", reset);
  reset();
})();
</script>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/qt_catalan_computer_assisted_proofs_2024/code/README.md`

```markdown
# Code

Placeholder for reproducible code supporting the computer-assisted proof.

Primary source to curate:

````text
../../../Conjectures-and-Computations/qt-catalan/qt-assisted.py
````
```

### `docs/items/qt_catalan_computer_assisted_proofs_2024/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{\texorpdfstring{$q,t$}{qt}-Catalan Computer-Assisted Proofs 2024}
\author{}
\date{}

\begin{document}
\maketitle

\section{Placeholder}

This file will contain the precise mathematical explanation of the
computer-assisted verification for Lemma 2 and Lemma 3 of Section 9 of the
2024 rational \(q,t\)-Catalan paper.

\end{document}
```

### `docs/items/qt_catalan_computer_assisted_proofs_2024/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>qt-Catalan Computer-Assisted Proofs 2024</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>qt-Catalan Computer-Assisted Proofs 2024</h1>
    <p>Proof-supporting computation for the 2024 rational qt-Catalan paper; computational review still needed for public packaging.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This educational section will explain what the computer-assisted verification checks and how it supports the 2024 paper.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/qt_catalan_middle_coefficients/code/README.md`

```markdown
# Code

Placeholder for code checking flat middle coefficient phenomena.
```

### `docs/items/qt_catalan_middle_coefficients/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{\texorpdfstring{$q,t$}{qt}-Catalan Middle Coefficients}
\author{}
\date{}

\begin{document}
\maketitle

\section{Placeholder}

This file will state the flat middle coefficient results and conjectures,
including the classical low-deficit theorem and rational directions.

\end{document}
```

### `docs/items/qt_catalan_middle_coefficients/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>qt-Catalan Middle Coefficients</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>qt-Catalan Middle Coefficients</h1>
    <p>Classical low-deficit case is proved in the 2026 preprint; r == 1 mod s and broader rational patterns are conjectural or experimental.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This educational section will explain flat middle coefficient patterns and the known proof statuses.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/rational_qt_catalan_formula/code/README.md`

```markdown
# Code

Placeholder for reproducible code checking the rational `qt`-Catalan
conjecture.

Primary source to curate:

````text
../../../Conjectures-and-Computations/qt-catalan/qt-conjecture.py
````
```

### `docs/items/rational_qt_catalan_formula/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{Rational \texorpdfstring{$q,t$}{qt}-Catalan Formula}
\author{}
\date{}

\begin{document}
\maketitle

\section{Placeholder}

This file will state the rational \(q,t\)-Catalan conjecture, its hypotheses,
and the current computational evidence.

\end{document}
```

### `docs/items/rational_qt_catalan_formula/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Rational qt-Catalan Formula</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>Rational qt-Catalan Formula</h1>
    <p>Conjectural formula from the 2024 rational qt-Catalan paper, supported by computational checks.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This educational section will introduce the rational qt-Catalan conjecture and show small checked examples.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/shifted_littlewood_richardson/code/README.md`

```markdown
# Code

Placeholder for reproducible code checking shifted Littlewood-Richardson
rules.
```

### `docs/items/shifted_littlewood_richardson/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{Shifted Littlewood--Richardson}
\author{}
\date{}

\begin{document}
\maketitle

\section{Placeholder}

This file will state the conjectural shifted Littlewood--Richardson rules for
skew \(GP\) and \(GQ\) functions.

\end{document}
```

### `docs/items/shifted_littlewood_richardson/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Shifted Littlewood-Richardson</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>Shifted Littlewood-Richardson</h1>
    <p>Conjectural shifted Littlewood-Richardson rules for GP and GQ functions, supported by computational checks.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This educational section will introduce the shifted Littlewood-Richardson conjectures for GP and GQ functions.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/items/type_c_grothendieck/code/README.md`

```markdown
# Code

Placeholder for reproducible code checking the type C Grothendieck
conjectures.
```

### `docs/items/type_c_grothendieck/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{Type C Grothendieck}
\author{}
\date{}

\begin{document}
\maketitle

\section{Placeholder}

This file will state the type C Grothendieck conjectures and explain the
relationship between the basic, strong, and strongest versions.

\end{document}
```

### `docs/items/type_c_grothendieck/index.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Type C Grothendieck</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
<article class="item-page">
  <header class="page-heading">
    <h1>Type C Grothendieck</h1>
    <p>Conjectural type C Grothendieck material, with basic, strong, and peakset-preserving variants.</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
<li><a href="explanation.tex">Download LaTeX</a></li>
<li><a href="code/">View code</a></li>
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
<p>This educational section will explain the type C Grothendieck conjectures and the hierarchy of checked versions.</p>

  </section>
</article>

  </main>
</body>
</html>
```

### `docs/static/styles.css`

```css
:root {
  color-scheme: light;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.5;
  color: #202124;
  background: #ffffff;
}

body {
  margin: 0;
}

a {
  color: #0b57d0;
}

.site-header {
  border-bottom: 1px solid #dadce0;
  padding: 16px 24px;
}

.site-title {
  color: #202124;
  font-weight: 700;
  text-decoration: none;
}

.site-main {
  max-width: 920px;
  margin: 0 auto;
  padding: 32px 24px 64px;
}

.page-heading {
  margin-bottom: 32px;
}

.page-heading h1 {
  margin: 0 0 8px;
}

.item-list {
  padding-left: 22px;
}
```

### `items/dyck_skeleton_string_decompositions/assets/.gitkeep`

```text

```

### `items/dyck_skeleton_string_decompositions/code/__pycache__/check_nrcm_lower_half.cpython-314.pyc`

```text
[binary artifact not expanded]
size_bytes: 21759
sha256: 949ea7548e2e773f0b057df7648a29d4cc24d4ae94df7de4ba65581b838d6c74
```

### `items/dyck_skeleton_string_decompositions/code/__pycache__/check_r1mod_skeleton_strings.cpython-314.pyc`

```text
[binary artifact not expanded]
size_bytes: 52495
sha256: bbe5991a49e0ca2730900ca341be4b014ec8acaaa3fb8310ab40cc3fc0b9ed3a
```

### `items/dyck_skeleton_string_decompositions/code/check_nrcm_domain.py`

```python
"""Check where strict NRCM is defined on lower-half sources.

This is a narrower diagnostic than ``check_nrcm_lower_half.py``.  It checks
only that strict NRCM is defined for every path of defect d and area
``a < (M-d)/2``.  The Dyck proof shows that, once strict NRCM is defined, it is
valid and preserves defect.

For slopes ``r=tau*s+1`` the script can use the optimized low-defect generator
from ``check_r1mod_skeleton_strings.py``.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import gcd

import check_nrcm_lower_half as nrcm
import check_r1mod_skeleton_strings as r1mod


def path_records_for_slope(r: int, s: int, max_defect: int) -> tuple[dict[nrcm.Path, nrcm.PathData], str]:
    records, _ = nrcm.load_path_data(r, s, max_defect)
    return records, f"ordinary_generator retained_paths={len(records)}"


def path_records_for_r1mod(tau: int, s: int, max_defect: int) -> tuple[dict[nrcm.Path, nrcm.PathData], str]:
    records, _, searched = r1mod.load_records(s, tau, max_defect)
    out = {q: nrcm.PathData(q, stats[0], stats[2]) for q, stats in records.items()}
    return (
        out,
        "r1mod_generator "
        f"generated_words={r1mod.count_normalized_words(s, tau)} "
        f"searched_leaf_words={searched} retained_paths={len(out)}",
    )


def check_domain_layer(records: dict[nrcm.Path, nrcm.PathData], r: int, s: int, defect: int) -> tuple[Counter[str], nrcm.Failure | None]:
    m_value = nrcm.total_degree(r, s)
    sources = sorted(
        (data for data in records.values() if data.defect == defect and 2 * data.area < m_value - defect),
        key=lambda data: (data.area, data.q),
    )
    counts: Counter[str] = Counter()
    counts["sources_below_midline"] = len(sources)
    for data in sources:
        move = nrcm.nrcm(data.q, r, s)
        counts["attempts"] += 1
        if move is None:
            return counts, nrcm.Failure(defect, data.area, data.q, "NRCM undefined")
        counts["defined_moves"] += 1
        counts[f"suffix_{move.k}"] += 1
    return counts, None


def scan_records(records: dict[nrcm.Path, nrcm.PathData], r: int, s: int, max_defect: int) -> tuple[int, list[str]]:
    consecutive_ok = -1
    lines: list[str] = []
    for defect in range(max_defect + 1):
        counts, failure = check_domain_layer(records, r, s, defect)
        if failure is None:
            if consecutive_ok == defect - 1:
                consecutive_ok = defect
            lines.append(f"  defc={defect}: PASS sources={counts['sources_below_midline']} defined={counts['defined_moves']}")
            continue
        lines.append(
            f"  defc={defect}: FAIL sources={counts['sources_below_midline']} "
            f"defined={counts['defined_moves']} reason={failure.reason} area={failure.area} q={failure.q}"
        )
        break
    return consecutive_ok, lines


def parse_case(text: str) -> tuple[int, int]:
    left, right = text.split("/")
    return int(left), int(right)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--case", type=parse_case, help="slope r/s")
    group.add_argument("--r1mod", nargs=2, metavar=("TAU", "S"), type=int, help="use slope r=tau*s+1")
    parser.add_argument("--max-defect", type=int, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.r1mod is not None:
        tau, s = args.r1mod
        if tau <= 0 or s <= 1:
            raise SystemExit("expected tau>0 and s>1")
        r = tau * s + 1
        records, generator_info = path_records_for_r1mod(tau, s, args.max_defect)
        label = f"tau={tau} s={s} slope={r}/{s}"
    else:
        r, s = args.case
        if r <= 0 or s <= 1 or gcd(r, s) != 1:
            raise SystemExit("expected a positive coprime slope r/s with s>1")
        records, generator_info = path_records_for_slope(r, s, args.max_defect)
        label = f"slope={r}/{s}"

    consecutive_ok, lines = scan_records(records, r, s, args.max_defect)
    print(f"NRCM domain check {label} M={nrcm.total_degree(r, s)}")
    print(f"  {generator_info}")
    for line in lines:
        print(line)
    print(f"  initial_passing_defect_range: 0..{consecutive_ok}" if consecutive_ok >= 0 else "  initial_passing_defect_range: empty")
    failed = consecutive_ok < args.max_defect
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### `items/dyck_skeleton_string_decompositions/code/check_nrcm_lower_half.py`

```python
"""Explore lower-half decompositions generated by the NRCM.

This diagnostic uses the position-coordinate rational Dyck path model from the
Dyck NRCM proof notes.  For a coprime slope r/s, it checks whether the naive
rational cyclic map gives a lower-half decomposition in each low-defect layer:

* every path of defect d and area a < (M-d)/2 has a defined NRCM image;
* the image has the same defect and area a+1;
* the image remains in the lower half;
* the map is injective on the checked lower-half sources.

The theorem in Dyck proves deficit preservation whenever NRCM is defined.  This
script is only testing whether the partial map is sufficiently defined and
injective to give lower-half strings in finite low-defect ranges.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from math import gcd
from typing import Iterable, Sequence


Path = tuple[int, ...]


@dataclass(frozen=True)
class PathData:
    q: Path
    area: int
    defect: int


@dataclass(frozen=True)
class Move:
    k: int
    after: Path


@dataclass(frozen=True)
class Failure:
    defect: int
    area: int
    q: Path
    reason: str


def ceiling_heights(r: int, s: int) -> Path:
    return tuple(r * i // s for i in range(s))


def labels(r: int, s: int) -> Path:
    return tuple((r * i) % s for i in range(s))


def increments(r: int, s: int) -> Path:
    return tuple(r * (i + 1) // s - r * i // s for i in range(s))


def total_degree(r: int, s: int) -> int:
    return sum(ceiling_heights(r, s))


def area(q_values: Sequence[int]) -> int:
    return sum(q_values)


def is_capacity_valid(q_values: Sequence[int], r: int, s: int) -> bool:
    heights = ceiling_heights(r, s)
    return len(q_values) == s and q_values[0] == 0 and all(0 <= q_values[i] <= heights[i] for i in range(s))


def path_heights(q_values: Sequence[int], r: int, s: int) -> Path:
    heights = ceiling_heights(r, s)
    return tuple(heights[i] - q_values[i] for i in range(s))


def is_path_valid(q_values: Sequence[int], r: int, s: int) -> bool:
    if not is_capacity_valid(q_values, r, s):
        return False
    p_values = path_heights(q_values, r, s)
    return all(p_values[i] <= p_values[i + 1] for i in range(s - 1))


def valid_paths(r: int, s: int) -> Iterable[Path]:
    heights = ceiling_heights(r, s)
    p_values = [0] * s

    def rec(index: int, minimum_path_height: int) -> Iterable[Path]:
        if index == s:
            yield tuple(heights[i] - p_values[i] for i in range(s))
            return
        for value in range(minimum_path_height, heights[index] + 1):
            p_values[index] = value
            yield from rec(index + 1, value)

    yield from rec(1, 0)


def suffix_cyclic_candidate(q_values: Sequence[int], r: int, s: int, suffix_start: int) -> Path:
    labs = labels(r, s)
    suffix = list(range(suffix_start, s))
    by_label = sorted(suffix, key=lambda index: labs[index])
    old = {index: q_values[index] for index in suffix}
    out = list(q_values)
    for source, destination in zip(by_label, by_label[1:]):
        out[destination] = old[source]
    out[by_label[0]] = old[by_label[-1]] + 1
    return tuple(out)


def nrcm(q_values: Sequence[int], r: int, s: int) -> Move | None:
    for suffix_start in range(1, s):
        candidate = suffix_cyclic_candidate(q_values, r, s, suffix_start)
        if not is_capacity_valid(candidate, r, s):
            continue
        if is_path_valid(candidate, r, s):
            return Move(suffix_start, candidate)
        return None
    return None


def pair_summand(q_values: Sequence[int], r: int, s: int, i: int, j: int) -> int:
    labs = labels(r, s)
    inc = increments(r, s)
    qi = q_values[i]
    qj = q_values[j]
    u = abs(qi - qj)
    if qi != qj and ((qi > qj) != (labs[i] > labs[j])):
        u -= 1
    u = max(u, 0)
    if qi > qj:
        v = inc[i] - (q_values[i + 1] - q_values[i])
    elif qj > qi:
        v = inc[i - 1] - (q_values[i] - q_values[i - 1])
    else:
        v = 0
    return min(u, v)


def defect(q_values: Sequence[int], r: int, s: int) -> int:
    return sum(pair_summand(q_values, r, s, i, j) for i in range(1, s) for j in range(i + 1, s))


def load_path_data(r: int, s: int, max_defect: int | None) -> tuple[dict[Path, PathData], Counter[int]]:
    records: dict[Path, PathData] = {}
    defect_counts: Counter[int] = Counter()
    for q_values in valid_paths(r, s):
        d = defect(q_values, r, s)
        defect_counts[d] += 1
        if max_defect is None or d <= max_defect:
            records[q_values] = PathData(q_values, area(q_values), d)
    return records, defect_counts


def check_defect_layer(records: dict[Path, PathData], r: int, s: int, d: int) -> tuple[Counter[str], Failure | None]:
    m_value = total_degree(r, s)
    middle = (m_value - d) / 2
    sources = sorted(
        (data for data in records.values() if data.defect == d and 2 * data.area < m_value - d),
        key=lambda data: (data.area, data.q),
    )
    allowed_outputs = {data.q for data in records.values() if data.defect == d and 2 * data.area <= m_value - d + 2}
    owners: dict[Path, Path] = {}
    counts: Counter[str] = Counter()
    counts["sources_below_midline"] = len(sources)
    counts["allowed_outputs"] = len(allowed_outputs)
    for data in sources:
        move = nrcm(data.q, r, s)
        counts["attempts"] += 1
        if move is None:
            return counts, Failure(d, data.area, data.q, "NRCM undefined")
        output = move.after
        output_data = records.get(output)
        if output_data is None:
            return counts, Failure(d, data.area, data.q, f"NRCM output not in retained records: {output}")
        if output_data.defect != d:
            return counts, Failure(d, data.area, data.q, f"defect changed to {output_data.defect}: {output}")
        if output_data.area != data.area + 1:
            return counts, Failure(d, data.area, data.q, f"area changed to {output_data.area}: {output}")
        if output not in allowed_outputs:
            return counts, Failure(d, data.area, data.q, f"output not in next-area target: {output}")
        previous = owners.setdefault(output, data.q)
        if previous != data.q:
            return counts, Failure(d, data.area, data.q, f"non-injective output {output}, previous source {previous}")
        counts["defined_injective_moves"] += 1
        counts[f"suffix_{move.k}"] += 1
    counts["distinct_outputs"] = len(owners)
    return counts, None


def scan_slope(r: int, s: int, max_defect: int | None) -> tuple[list[str], bool]:
    if r <= 0 or s <= 1 or gcd(r, s) != 1:
        raise ValueError("expected a positive coprime slope r/s with s>1")
    records, defect_counts = load_path_data(r, s, max_defect)
    highest = max(defect_counts) if defect_counts else -1
    limit = highest if max_defect is None else min(max_defect, highest)
    lines = [f"slope={r}/{s} M={total_degree(r, s)} retained_paths={len(records)} total_paths={sum(defect_counts.values())}"]
    consecutive_ok = -1
    all_ok = True
    for d in range(limit + 1):
        counts, failure = check_defect_layer(records, r, s, d)
        if failure is None:
            if consecutive_ok == d - 1:
                consecutive_ok = d
            lines.append(
                f"  defc={d}: PASS sources={counts['sources_below_midline']} "
                f"allowed_outputs={counts['allowed_outputs']} moves={counts['defined_injective_moves']}"
            )
            continue
        all_ok = False
        lines.append(
            f"  defc={d}: FAIL sources={counts['sources_below_midline']} "
            f"allowed_outputs={counts['allowed_outputs']} reason={failure.reason} "
            f"area={failure.area} q={failure.q}"
        )
        for later in range(d + 1, limit + 1):
            later_counts, later_failure = check_defect_layer(records, r, s, later)
            status = "PASS" if later_failure is None else "FAIL"
            detail = "" if later_failure is None else f" reason={later_failure.reason} area={later_failure.area} q={later_failure.q}"
            lines.append(
                f"  defc={later}: {status} sources={later_counts['sources_below_midline']} "
                f"allowed_outputs={later_counts['allowed_outputs']}{detail}"
            )
        break
    lines.append(f"  initial_passing_defect_range: 0..{consecutive_ok}" if consecutive_ok >= 0 else "  initial_passing_defect_range: empty")
    return lines, all_ok


def parse_cases(text: str) -> tuple[tuple[int, int], ...]:
    cases: list[tuple[int, int]] = []
    for item in text.split(","):
        item = item.strip()
        if not item:
            continue
        left, right = item.split("/")
        cases.append((int(left), int(right)))
    return tuple(cases)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=parse_cases, required=True, help="comma-separated slopes, e.g. 7/5,10/7")
    parser.add_argument("--max-defect", type=int, default=20, help="maximum defect layer to test")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ok = True
    for index, (r, s) in enumerate(args.cases):
        if index:
            print()
        lines, case_ok = scan_slope(r, s, args.max_defect)
        ok = ok and case_ok
        for line in lines:
            print(line)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### `items/dyck_skeleton_string_decompositions/code/check_r1mod_skeleton_strings.py`

```python
"""Checks for the conjectural ``r = tau*s + 1`` skeleton-string formula.

This item-level checker covers the tau>1 rational case, which remains
conjectural.  It verifies finite instances of:

1. the special-skeleton quotient formula in a defect range;
2. the current East3/East5 partial lower-half string map.

Finite checks are evidence only, not proof.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from math import comb
from typing import Iterable, Sequence


Word = tuple[int, ...]
PairTable = list[list[int]]
UNSUPPORTED_LEVEL_7 = "unsupported_level_7"
KNOWN_STATS: dict[Word, tuple[int, int, int]] = {}


@dataclass(frozen=True)
class LocalResult:
    success: bool
    output: Word | None
    case: str
    reason: str | None = None


@dataclass(frozen=True)
class StepResult:
    success: bool
    output: Word | None
    direction: str
    branch: str
    level: int | None
    reason: str | None = None
    window: Word | None = None
    local_case: str | None = None


@dataclass(frozen=True)
class Failure:
    property: str
    defect: int
    source: Word | None
    reason: str


def max_total_degree(s: int, tau: int) -> int:
    return tau * comb(s, 2)


def conjectural_defect_bound(s: int, tau: int) -> int:
    return (s - 2) * (tau + 1) - 4


def count_normalized_words(s: int, tau: int) -> int:
    counts = [1]
    for _ in range(1, s):
        next_counts = [0] * (len(counts) + tau)
        for previous, count in enumerate(counts):
            if count:
                for value in range(previous + tau + 1):
                    next_counts[value] += count
        counts = next_counts
    return sum(counts)


def area(word: Sequence[int]) -> int:
    return sum(word)


def pair_dinv(left: int, right: int, tau: int) -> int:
    if left <= right:
        contribution = left + tau - right
    else:
        contribution = right + 1 + tau - left
    return contribution if contribution > 0 else 0


def build_pair_dinv_table(max_value: int, tau: int) -> PairTable:
    return [[pair_dinv(left, right, tau) for right in range(max_value + 1)] for left in range(max_value + 1)]


def dinv_delta_append_from_table(prefix: Sequence[int], value: int, pair_table: PairTable) -> int:
    total = 0
    for left in prefix:
        total += pair_table[left][value]
    return total


def dinv_delta_append_from_counts(counts: Sequence[int], value: int, pair_columns: PairTable) -> int:
    total = 0
    column = pair_columns[value]
    for left, count in enumerate(counts):
        if count:
            total += count * column[left]
    return total


def suffix_score_bounder(s: int, tau: int, pair_table: PairTable):
    """Return an exact maximum future ``area+dinv`` scorer for a prefix state."""

    max_value = tau * (s - 1)
    pair_columns = [[pair_table[left][right] for left in range(max_value + 1)] for right in range(max_value + 1)]

    @lru_cache(maxsize=None)
    def bound(remaining: int, previous: int, counts: tuple[int, ...]) -> int:
        if remaining == 0:
            return 0
        best = -1
        limit = min(max_value, previous + tau)
        for value in range(limit + 1):
            delta = value + dinv_delta_append_from_counts(counts, value, pair_columns)
            next_counts = list(counts)
            next_counts[value] += 1
            candidate = delta + bound(remaining - 1, value, tuple(next_counts))
            if candidate > best:
                best = candidate
        return best

    return bound


def dinv_delta_append(prefix: Sequence[int], value: int, tau: int) -> int:
    total = 0
    for left in prefix:
        if left <= value:
            total += max(0, left + tau - value)
        else:
            total += max(0, value + 1 + tau - left)
    return total


@lru_cache(maxsize=None)
def rational_dinv(word: Word, tau: int) -> int:
    values = tuple(word)
    total = 0
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            if left <= right:
                total += max(0, left + tau - right)
            else:
                total += max(0, right + 1 + tau - left)
    return total


@lru_cache(maxsize=None)
def is_normalized(word: Word, tau: int) -> bool:
    values = tuple(word)
    return (
        bool(values)
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and all(values[index + 1] <= values[index] + tau for index in range(len(values) - 1))
    )


def generate_words_with_stats(s: int, tau: int) -> Iterable[tuple[Word, int, int, int]]:
    """Generate normalized tau-affine words with incremental area/dinv."""

    if s <= 0:
        raise ValueError("s must be positive")
    if tau <= 0:
        raise ValueError("tau must be positive")
    m_total = max_total_degree(s, tau)
    pair_table = build_pair_dinv_table(tau * (s - 1), tau)
    prefix = [0]

    def rec(current_area: int, current_dinv: int) -> Iterable[tuple[Word, int, int, int]]:
        if len(prefix) == s:
            word = tuple(prefix)
            yield word, current_area, current_dinv, m_total - current_area - current_dinv
            return
        previous = prefix[-1]
        for value in range(previous + tau + 1):
            delta = dinv_delta_append_from_table(prefix, value, pair_table)
            prefix.append(value)
            yield from rec(current_area + value, current_dinv + delta)
            prefix.pop()

    yield from rec(0, 0)


@lru_cache(maxsize=None)
def remove_at(word: Word, position: int) -> Word:
    values = tuple(word)
    return values[:position] + values[position + 1 :]


@lru_cache(maxsize=None)
def find_extractable(word: Word, tau: int, *, include_final: bool = True) -> int | None:
    values = tuple(word)
    if not is_normalized(values, tau):
        raise ValueError(f"not normalized: {values}")
    return find_extractable_normalized(values, tau, include_final=include_final)


def find_extractable_normalized(values: Word, tau: int, *, include_final: bool = True) -> int | None:
    max_value = tau * (len(values) - 1)
    prior_counts = [0] * (max_value + 1)
    for index, value in enumerate(values):
        if value == 0:
            prior_counts[0] += 1
            continue
        if not include_final and index == len(values) - 1:
            prior_counts[value] += 1
            continue
        lower = max(0, value - tau)
        prior_count = 0
        for prior in range(lower, value):
            prior_count += prior_counts[prior]
        if prior_count != 1:
            prior_counts[value] += 1
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + tau:
            prior_counts[value] += 1
            continue
        return index
    return None


@lru_cache(maxsize=None)
def is_full_skeleton(word: Word, tau: int) -> bool:
    values = tuple(word)
    return is_normalized(values, tau) and is_full_skeleton_normalized(values, tau)


@lru_cache(maxsize=None)
def is_full_skeleton_normalized(values: Word, tau: int) -> bool:
    return find_extractable_normalized(values, tau, include_final=True) is None


@lru_cache(maxsize=None)
def excluded_full_skeleton(s: int, tau: int) -> Word:
    if s < 4:
        raise ValueError("excluded skeleton is only defined for s >= 4")
    return (0, 0, 1) + (0,) * (s - 4) + (tau,)


@lru_cache(maxsize=None)
def is_special_skeleton(word: Word, tau: int) -> bool:
    values = tuple(word)
    if not is_normalized(values, tau) or not is_full_skeleton_normalized(values, tau):
        return False
    return is_special_skeleton_normalized(values, tau)


@lru_cache(maxsize=None)
def is_special_skeleton_normalized(values: Word, tau: int) -> bool:
    return len(values) < 4 or values != excluded_full_skeleton(len(values), tau)


@lru_cache(maxsize=None)
def special_input(s: int, tau: int) -> Word:
    return (0,) * (s - 1) + (tau,)


@lru_cache(maxsize=None)
def rational_inject(word: Word, entry: int, tau: int) -> Word:
    values = tuple(word)
    if entry <= 0:
        raise ValueError(f"cannot inject nonpositive entry {entry}")
    out = rational_inject_normalized(values, entry, tau)
    if not is_normalized(out, tau):
        raise ValueError(f"injection produced non-normalized word {out}")
    return out


def rational_inject_normalized(values: Word, entry: int, tau: int) -> Word:
    lower = max(0, entry - tau)
    anchor = next((index for index, value in enumerate(values) if lower <= value <= entry - 1), None)
    if anchor is None:
        raise ValueError(f"no injection anchor for {entry} in {values}")
    return values[: anchor + 1] + (entry,) + values[anchor + 1 :]


@lru_cache(maxsize=None)
def inject_right_to_left(base: Word, entries: Word, tau: int) -> Word:
    out = tuple(base)
    for entry in reversed(tuple(entries)):
        out = rational_inject_normalized(out, entry, tau)
    return out


def bk2(a: int, b: int, tau: int) -> tuple[int, int]:
    return (b, a) if a > b + tau else (a, b)


@lru_cache(maxsize=None)
def east3(window: Word, tau: int) -> LocalResult:
    values = tuple(window)
    if len(values) != 3:
        raise ValueError("East3 needs a 3-window")
    _, c, d = values
    if c <= d + tau:
        return LocalResult(True, values, "east3_identity")
    return LocalResult(False, None, "east3_fail", "c >> d")


@lru_cache(maxsize=None)
def east5(window: Word, tau: int) -> LocalResult:
    values = tuple(window)
    if len(values) != 5:
        raise ValueError("East5 needs a 5-window")
    a, b, c, d, e = values
    if east3((b, c, d), tau).success:
        return LocalResult(False, None, "east5_outside_domain", "East3 would pass")
    if b <= d + tau:
        if b <= e + tau:
            return LocalResult(True, (a, d, c, b, e), "east5_case2b")
        return LocalResult(False, None, "east5_case2b_fail", "b >> e")
    b_prime, c_prime = bk2(b, c, tau)
    if c_prime <= e + tau:
        return LocalResult(True, (a, d, b_prime, c_prime, e), "east5_case2a")
    return LocalResult(False, None, "east5_case2a_fail", "c' >> e")


def reverse_result(result: LocalResult) -> LocalResult:
    output = None if result.output is None else tuple(reversed(result.output))
    return LocalResult(
        result.success,
        output,
        result.case.replace("east", "west", 1),
        None if result.reason is None else result.reason.replace("East", "West"),
    )


@lru_cache(maxsize=None)
def west3(window: Word, tau: int) -> LocalResult:
    return reverse_result(east3(tuple(reversed(tuple(window))), tau))


@lru_cache(maxsize=None)
def west5(window: Word, tau: int) -> LocalResult:
    return reverse_result(east5(tuple(reversed(tuple(window))), tau))


def checked_step(
    direction: str,
    source: Word,
    output: Word,
    tau: int,
    *,
    branch: str,
    level: int,
    window: Word | None = None,
    local_case: str | None = None,
) -> StepResult:
    if len(source) != len(output):
        return StepResult(False, None, direction, "failed", None, f"{direction} changed length")
    source_stats = KNOWN_STATS.get(source)
    if source_stats is None:
        source_area = area(source)
        source_dinv = rational_dinv(source, tau)
        source_defect = max_total_degree(len(source), tau) - source_area - source_dinv
    else:
        source_area, source_dinv, source_defect = source_stats
    output_stats = KNOWN_STATS.get(output)
    if output_stats is None:
        if not is_normalized(output, tau):
            return StepResult(False, None, direction, "failed", None, f"{direction} produced non-normalized {output}")
        output_area = area(output)
        output_dinv = rational_dinv(output, tau)
        output_defect = max_total_degree(len(output), tau) - output_area - output_dinv
    else:
        output_area, output_dinv, output_defect = output_stats
    if source_defect != output_defect:
        return StepResult(False, None, direction, "failed", None, f"{direction} changed defect: {source} -> {output}")
    if direction == "up" and (output_area != source_area + 1 or output_dinv != source_dinv - 1):
        return StepResult(False, None, direction, "failed", None, f"up changed wrong statistics: {source} -> {output}")
    if direction == "down" and (output_area != source_area - 1 or output_dinv != source_dinv + 1):
        return StepResult(False, None, direction, "failed", None, f"down changed wrong statistics: {source} -> {output}")
    return StepResult(True, output, direction, branch, level, None, window, local_case)


@lru_cache(maxsize=None)
def up_step(word: Word, tau: int) -> StepResult:
    values = tuple(word)
    s = len(values)
    if not is_normalized(values, tau):
        return StepResult(False, None, "up", "failed", None, f"not normalized: {values}")
    try:
        if s >= 4 and values == special_input(s, tau):
            return checked_step("up", values, excluded_full_skeleton(s, tau), tau, branch="special", level=3)
        if is_full_skeleton_normalized(values, tau):
            result = rational_inject_normalized(values[:-1], values[-1] + 1, tau)
            return checked_step("up", values, result, tau, branch="full_skeleton", level=3)
        j1 = find_extractable(values, tau)
        if j1 is None:
            return StepResult(False, None, "up", "failed", None, f"no first extractable in {values}")
        e1 = values[j1]
        c1 = remove_at(values, j1)
        sigma1 = c1 + (e1 - 1,)
        attempt3 = east3(sigma1[-3:], tau)
        if attempt3.success:
            if j1 >= s - 2:
                return StepResult(False, None, "up", "failed", None, f"East3 position bound failed: j1={j1}")
            assert attempt3.output is not None
            result = inject_right_to_left(sigma1[:-2], (attempt3.output[-2] + 1, attempt3.output[-1] + 1), tau)
            return checked_step("up", values, result, tau, branch="local", level=3, window=sigma1[-3:], local_case=attempt3.case)
        j2 = find_extractable(c1, tau)
        if j2 is None:
            return StepResult(False, None, "up", "failed", None, f"no second extractable in {c1}")
        e2 = c1[j2]
        c2 = remove_at(c1, j2)
        sigma2 = c2 + (e1 - 1, e2 - 1)
        attempt5 = east5(sigma2[-5:], tau)
        if attempt5.success:
            if j1 >= s - 3:
                return StepResult(False, None, "up", "failed", None, f"East5 position bound failed: j1={j1}")
            if j2 > len(c1) - 3:
                return StepResult(False, None, "up", "failed", None, f"East5 position bound failed: j2={j2}")
            assert attempt5.output is not None
            base = sigma2[:-5] + attempt5.output[:2]
            result = inject_right_to_left(base, tuple(value + 1 for value in attempt5.output[2:]), tau)
            return checked_step("up", values, result, tau, branch="local", level=5, window=sigma2[-5:], local_case=attempt5.case)
        return StepResult(False, None, "up", "failed", None, UNSUPPORTED_LEVEL_7)
    except (IndexError, ValueError) as exc:
        return StepResult(False, None, "up", "failed", None, str(exc))


@lru_cache(maxsize=None)
def down_step(word: Word, tau: int) -> StepResult:
    values = tuple(word)
    s = len(values)
    if not is_normalized(values, tau):
        return StepResult(False, None, "down", "failed", None, f"not normalized: {values}")
    if is_special_skeleton_normalized(values, tau) and is_full_skeleton_normalized(values, tau):
        return StepResult(False, None, "down", "failed", None, "down undefined on special skeleton")
    try:
        if s >= 4 and values == excluded_full_skeleton(s, tau):
            return checked_step("down", values, special_input(s, tau), tau, branch="excluded_full_skeleton", level=3)
        j1 = find_extractable(values, tau)
        if j1 is None:
            return StepResult(False, None, "down", "failed", None, f"no first extractable in {values}")
        f1 = values[j1]
        d1 = remove_at(values, j1)
        candidate = d1 + (f1 - 1,)
        if is_full_skeleton_normalized(candidate, tau):
            return checked_step("down", values, candidate, tau, branch="to_full_skeleton", level=3)
        j2 = find_extractable(d1, tau)
        if j2 is None:
            return StepResult(False, None, "down", "failed", None, f"no second extractable in {d1}")
        f2 = d1[j2]
        d2 = remove_at(d1, j2)
        tau1 = d2 + (f1 - 1, f2 - 1)
        attempt3 = west3(tau1[-3:], tau)
        if attempt3.success:
            if j1 >= s - 1:
                return StepResult(False, None, "down", "failed", None, f"West3 position bound failed: j1={j1}")
            if j2 >= len(d1) - 1:
                return StepResult(False, None, "down", "failed", None, f"West3 position bound failed: j2={j2}")
            assert attempt3.output is not None
            result = rational_inject_normalized(tau1[:-1], attempt3.output[-1] + 1, tau)
            return checked_step("down", values, result, tau, branch="local", level=3, window=tau1[-3:], local_case=attempt3.case)
        j3 = find_extractable(d2, tau)
        if j3 is None:
            return StepResult(False, None, "down", "failed", None, f"no third extractable in {d2}")
        f3 = d2[j3]
        d3 = remove_at(d2, j3)
        tau2 = d3 + (f1 - 1, f2 - 1, f3 - 1)
        attempt5 = west5(tau2[-5:], tau)
        if attempt5.success:
            if j1 >= s - 2:
                return StepResult(False, None, "down", "failed", None, f"West5 position bound failed: j1={j1}")
            if j2 > len(d1) - 2:
                return StepResult(False, None, "down", "failed", None, f"West5 position bound failed: j2={j2}")
            if j3 > len(d2) - 2:
                return StepResult(False, None, "down", "failed", None, f"West5 position bound failed: j3={j3}")
            assert attempt5.output is not None
            base = tau2[:-5] + attempt5.output[:3]
            result = inject_right_to_left(base, tuple(value + 1 for value in attempt5.output[3:]), tau)
            return checked_step("down", values, result, tau, branch="local", level=5, window=tau2[-5:], local_case=attempt5.case)
        return StepResult(False, None, "down", "failed", None, UNSUPPORTED_LEVEL_7)
    except (IndexError, ValueError) as exc:
        return StepResult(False, None, "down", "failed", None, str(exc))


def load_records(s: int, tau: int, max_defect: int) -> tuple[dict[Word, tuple[int, int, int]], Counter[tuple[int, int]], int]:
    records: dict[Word, tuple[int, int, int]] = {}
    direct_coeffs: Counter[tuple[int, int]] = Counter()
    searched = 0
    total_degree = max_total_degree(s, tau)
    min_score = total_degree - max_defect
    pair_table = build_pair_dinv_table(tau * (s - 1), tau)
    suffix_bound = suffix_score_bounder(s, tau, pair_table)
    prefix = [0]
    counts = [0] * (tau * (s - 1) + 1)
    counts[0] = 1

    def rec(current_area: int, current_dinv: int) -> None:
        nonlocal searched
        remaining = s - len(prefix)
        if remaining and current_area + current_dinv + suffix_bound(remaining, prefix[-1], tuple(counts)) < min_score:
            return
        if len(prefix) == s:
            searched += 1
            word_defect = total_degree - current_area - current_dinv
            if word_defect <= max_defect:
                word = tuple(prefix)
                records[word] = (current_area, current_dinv, word_defect)
                direct_coeffs[(current_area, current_dinv)] += 1
            return
        previous = prefix[-1]
        for value in range(previous + tau + 1):
            delta = dinv_delta_append_from_table(prefix, value, pair_table)
            prefix.append(value)
            counts[value] += 1
            rec(current_area + value, current_dinv + delta)
            counts[value] -= 1
            prefix.pop()

    rec(0, 0)
    return records, direct_coeffs, searched


def formula_coefficients(records: dict[Word, tuple[int, int, int]], s: int, tau: int, max_defect: int) -> Counter[tuple[int, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    total_degree = max_total_degree(s, tau)
    for word, (word_area, word_dinv, word_defect) in records.items():
        if word_defect > max_defect or not is_full_skeleton_normalized(word, tau) or not is_special_skeleton_normalized(word, tau):
            continue
        if word_dinv >= word_area:
            for q_power in range(word_area, word_dinv + 1):
                coeffs[(q_power, total_degree - word_defect - q_power)] += 1
        else:
            for q_power in range(word_dinv + 1, word_area):
                coeffs[(q_power, total_degree - word_defect - q_power)] -= 1
    return coeffs


def check_formula(records: dict[Word, tuple[int, int, int]], direct: Counter[tuple[int, int]], s: int, tau: int, max_defect: int) -> tuple[bool, str]:
    formula = formula_coefficients(records, s, tau, max_defect)
    for key in sorted(set(direct) | set(formula)):
        if direct[key] != formula[key]:
            return False, f"formula mismatch at {key}: direct={direct[key]}, formula={formula[key]}"
    return True, "formula coefficients match"


def check_map(
    records: dict[Word, tuple[int, int, int]],
    s: int,
    tau: int,
    max_defect: int,
    *,
    report_level7: bool = False,
) -> tuple[Counter[str], Failure | None, list[Failure]]:
    global KNOWN_STATS
    KNOWN_STATS = records
    by_defect: dict[int, list[Word]] = defaultdict(list)
    for word, (_, _, word_defect) in records.items():
        if word_defect <= max_defect:
            by_defect[word_defect].append(word)
    counts: Counter[str] = Counter()
    failures: list[Failure] = []
    level7_records: dict[tuple[str, int, Word], Failure] = {}
    total_degree = max_total_degree(s, tau)

    for defect in range(max_defect + 1):
        ell = (total_degree - defect) // 2
        target = {word for word in by_defect.get(defect, ()) if records[word][0] <= ell}
        starts = sorted(
            (word for word in target if is_full_skeleton_normalized(word, tau) and is_special_skeleton_normalized(word, tau)),
            key=lambda word: (records[word][0], word),
        )
        counts["target_words"] += len(target)
        counts["special_starts"] += len(starts)
        occurrences: dict[Word, Word] = {}
        blocked_by_level7: set[Word] = set()

        for start in starts:
            current = start
            occurrences[current] = start
            while records[current][0] < ell:
                result = up_step(current, tau)
                counts["up_attempts"] += 1
                if not result.success:
                    if result.reason == UNSUPPORTED_LEVEL_7:
                        counts["unsupported_level_7"] += 1
                        blocked_by_level7.add(current)
                        if report_level7:
                            level7_records.setdefault(
                                ("up", defect, current),
                                Failure("level7_blocked_up", defect, current, result.reason),
                            )
                        break
                    failures.append(Failure("up_step_failure", defect, current, result.reason or "unknown failure"))
                    break
                assert result.output is not None
                counts[f"up_level_{result.level}"] += 1
                if result.output not in target:
                    failures.append(Failure("up_left_target", defect, current, f"output {result.output} not in target"))
                down = down_step(result.output, tau)
                counts["down_inverse_attempts"] += 1
                if not down.success:
                    if down.reason == UNSUPPORTED_LEVEL_7:
                        counts["unsupported_level_7"] += 1
                        if report_level7:
                            level7_records.setdefault(
                                ("down_inverse", defect, result.output),
                                Failure("level7_blocked_down_inverse", defect, result.output, down.reason),
                            )
                    else:
                        failures.append(Failure("down_inverse_failure", defect, result.output, down.reason or "unknown failure"))
                elif down.output != current:
                    failures.append(Failure("inverse_mismatch", defect, current, f"up={result.output}, down(up)={down.output}"))
                current = result.output
                previous_owner = occurrences.setdefault(current, start)
                if previous_owner != start:
                    failures.append(Failure("duplicate_coverage", defect, current, f"owners={previous_owner}, {start}"))

        for word in sorted(target, key=lambda item: (records[item][0], item)):
            if word in occurrences:
                continue
            current = word
            seen: set[Word] = set()
            while not (is_full_skeleton_normalized(current, tau) and is_special_skeleton_normalized(current, tau)):
                if current in seen:
                    failures.append(Failure("descent_cycle", defect, word, f"cycle at {current}"))
                    break
                seen.add(current)
                result = down_step(current, tau)
                counts["descent_attempts"] += 1
                if not result.success:
                    if result.reason == UNSUPPORTED_LEVEL_7:
                        counts["unsupported_level_7"] += 1
                        blocked_by_level7.add(word)
                        if report_level7:
                            level7_records.setdefault(
                                ("descent", defect, word),
                                Failure("level7_blocked_descent", defect, word, result.reason),
                            )
                    else:
                        failures.append(Failure("descent_failure", defect, word, result.reason or "unknown failure"))
                    break
                assert result.output is not None
                current = result.output
                if current not in target:
                    failures.append(Failure("descent_left_target", defect, word, f"down reached {current} outside target"))
                    break
            else:
                failures.append(Failure("coverage_missing_despite_descent", defect, word, f"descends to {current}"))

        missing = target - set(occurrences) - blocked_by_level7
        if missing:
            word = sorted(missing, key=lambda item: (records[item][0], item))[0]
            failures.append(Failure("coverage_missing", defect, word, "not covered"))

        counts["covered_words"] += len(occurrences)
        counts["level7_blocked_words"] += len(blocked_by_level7)

    if failures:
        first = sorted(failures, key=lambda item: (item.defect, area(item.source or ()), item.source or (), item.property))[0]
        return counts, first, sorted(level7_records.values(), key=lambda item: (item.defect, area(item.source or ()), item.source or (), item.property))
    return counts, None, sorted(level7_records.values(), key=lambda item: (item.defect, area(item.source or ()), item.source or (), item.property))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s", type=int, required=True, help="length s")
    parser.add_argument("--tau", type=int, required=True, help="tau in r=tau*s+1; intended tau>1")
    parser.add_argument(
        "--max-defect",
        default="conjectural",
        help="integer max defect, or 'conjectural' for (s-2)(tau+1)-4",
    )
    parser.add_argument("--formula-only", action="store_true", help="only check the quotient formula")
    parser.add_argument("--map-only", action="store_true", help="only check the lower-half map")
    parser.add_argument("--report-level7", action="store_true", help="print words blocked by unsupported level-7 moves")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.formula_only and args.map_only:
        raise SystemExit("choose at most one of --formula-only and --map-only")
    if args.tau <= 1:
        raise SystemExit("this checker is for the conjectural tau>1 case")
    max_defect = conjectural_defect_bound(args.s, args.tau) if args.max_defect == "conjectural" else int(args.max_defect)
    if max_defect < 0:
        print(f"empty defect range: max_defect={max_defect}")
        return 0

    start = time.perf_counter()
    records, direct, searched = load_records(args.s, args.tau, max_defect)
    load_elapsed = time.perf_counter() - start
    print("r = tau*s + 1 skeleton-string check")
    print(f"  s: {args.s}")
    print(f"  tau: {args.tau}")
    print(f"  max_defect: {max_defect}")
    print(f"  generated_words: {count_normalized_words(args.s, args.tau)}")
    print(f"  searched_leaf_words: {searched}")
    print(f"  retained_defect_range_words: {len(records)}")
    print(f"  generation_elapsed_seconds: {load_elapsed:.3f}")

    ok = True
    if not args.map_only:
        formula_start = time.perf_counter()
        formula_ok, formula_message = check_formula(records, direct, args.s, args.tau, max_defect)
        print(f"  formula_status: {'PASS' if formula_ok else 'FAIL'}")
        print(f"  formula_message: {formula_message}")
        print(f"  formula_elapsed_seconds: {time.perf_counter() - formula_start:.3f}")
        ok = ok and formula_ok

    if not args.formula_only:
        map_start = time.perf_counter()
        map_counts, failure, level7_records = check_map(
            records,
            args.s,
            args.tau,
            max_defect,
            report_level7=args.report_level7,
        )
        map_partial = failure is None and map_counts.get("unsupported_level_7", 0) > 0
        if failure is None and not map_partial:
            map_status = "PASS"
        elif map_partial:
            map_status = "PARTIAL"
        else:
            map_status = "FAIL"
        print(f"  map_status: {map_status}")
        print(f"  map_counts: {dict(sorted(map_counts.items()))}")
        if args.report_level7:
            print(f"  level7_records: {len(level7_records)}")
            for record in level7_records:
                print(
                    "  level7_record: "
                    f"property={record.property} defect={record.defect} "
                    f"area={area(record.source or ())} source={record.source} "
                    f"reason={record.reason}"
                )
        if failure is not None:
            print(f"  first_failed_property: {failure.property}")
            print(f"  first_failed_defect: {failure.defect}")
            print(f"  first_failed_source: {failure.source}")
            print(f"  first_failure_reason: {failure.reason}")
        print(f"  map_elapsed_seconds: {time.perf_counter() - map_start:.3f}")
        ok = ok and failure is None and not map_partial

    print(f"  total_elapsed_seconds: {time.perf_counter() - start:.3f}")
    print(f"  status: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### `items/dyck_skeleton_string_decompositions/code/README.md`

```markdown
# Code

Code supporting skeleton-string decompositions.

- `check_r1mod_skeleton_strings.py` checks finite instances of the conjectural
  `r=tau*s+1`, `tau>1` rational special-skeleton formula.  It also checks the
  current East3/East5 partial lower-half string map, but only certifies a full
  map decomposition on defect layers where no `unsupported_level_7` move is
  reached.  If level 7 is reached, the map status is `PARTIAL`, not `PASS`.
  These checks are evidence only, not proof.  The checker prunes
  normalized-word generation when an exact suffix score bound proves the defect
  range is unreachable; `generated_words` remains the full normalized
  search-space size, while `searched_leaf_words` is the number of complete
  words reached after pruning.
- `run_official_r1mod_checks.py` runs the official `tau>1` finite-check grid:
  `tau=2, s<=14`; `tau=3, s<=12`; `tau=4, s<=10`; and `tau=5, s<=9`.
  Cases with `s<=4` are run in formula-only mode.
- `check_nrcm_lower_half.py` explores whether the strict NRCM gives
  lower-half decompositions for rational slopes. It checks definedness,
  defect preservation, area increase, and injectivity on low-defect layers.
- `check_nrcm_domain.py` is the narrower diagnostic for the same strict NRCM:
  it only checks that NRCM is defined on every below-midline source.  This is
  useful because the Dyck proof already establishes validity and defect
  preservation whenever strict NRCM is defined.
```

### `items/dyck_skeleton_string_decompositions/code/run_official_r1mod_checks.py`

```python
"""Run the official finite checks for the ``r=tau*s+1`` string item.

The official ranges are:

* tau=2, 1 <= s <= 14;
* tau=3, 1 <= s <= 12;
* tau=4, 1 <= s <= 10;
* tau=5, 1 <= s <= 9.

For s <= 4 only the quotient formula is checked.  For s >= 5 both the
formula and the lower-half map are checked.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path


OFFICIAL_RANGES = {
    2: 14,
    3: 12,
    4: 10,
    5: 9,
}


def parse_field(output: str, field: str) -> str:
    match = re.search(rf"^\s*{re.escape(field)}:\s*(.+)$", output, re.MULTILINE)
    return match.group(1).strip() if match else ""


def run_case(checker: Path, tau: int, s: int) -> tuple[bool, str]:
    command = [sys.executable, str(checker), "--tau", str(tau), "--s", str(s)]
    if s <= 4:
        command.append("--formula-only")

    start = time.perf_counter()
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    wall = time.perf_counter() - start
    output = completed.stdout + completed.stderr
    status = parse_field(output, "status")
    if "empty defect range" in output and completed.returncode == 0:
        status = "PASS"
    ok = completed.returncode == 0 and status != "FAIL"
    mode = "formula-only" if s <= 4 else "formula+map"
    max_defect = parse_field(output, "max_defect")
    generated = parse_field(output, "generated_words")
    searched = parse_field(output, "searched_leaf_words")
    retained = parse_field(output, "retained_defect_range_words")
    total = parse_field(output, "total_elapsed_seconds")
    if not total:
        total = f"{wall:.3f}"
    summary = (
        f"tau={tau} s={s} mode={mode} status={'PASS' if ok else 'FAIL'} "
        f"max_defect={max_defect or 'empty'} generated={generated or 'n/a'} "
        f"searched={searched or 'n/a'} retained={retained or 'n/a'} "
        f"elapsed={total}s"
    )
    if not ok:
        summary += "\n" + output
    return ok, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stop-on-fail", action="store_true", help="stop after the first failed official case")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checker = Path(__file__).with_name("check_r1mod_skeleton_strings.py")
    all_ok = True
    start = time.perf_counter()
    for tau, max_s in OFFICIAL_RANGES.items():
        for s in range(1, max_s + 1):
            ok, summary = run_case(checker, tau, s)
            print(summary, flush=True)
            all_ok = all_ok and ok
            if not ok and args.stop_on_fail:
                print(f"overall_elapsed_seconds: {time.perf_counter() - start:.3f}")
                return 1
    print(f"overall_elapsed_seconds: {time.perf_counter() - start:.3f}")
    print(f"overall_status: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### `items/dyck_skeleton_string_decompositions/explanation.aux`

```text
\relax 
\@writefile{toc}{\contentsline {section}{\numberline {1}Overview}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {2}Common Vocabulary}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {3}The Classical Model}{1}{}\protected@file@percent }
\citation{Hawkes2026DyckSymmetric}
\@writefile{toc}{\contentsline {section}{\numberline {4}The \(\tau \)-Dyck Model for \(r=\tau s+1\)}{2}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {5}Rational Special Skeletons}{3}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {6}Conjectural Lower-Half Formula and Symmetry Completion}{4}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {7}Computations for the Conjecture}{4}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {8}The Naive Rational Cyclic Map}{5}{}\protected@file@percent }
\citation{Hawkes2026DyckSymmetric}
\@writefile{toc}{\contentsline {section}{\numberline {9}NRCM Lower-Half Diagnostics}{7}{}\protected@file@percent }
\bibcite{Hawkes2026DyckSymmetric}{1}
\@writefile{toc}{\contentsline {section}{\numberline {10}Status of Claims}{8}{}\protected@file@percent }
\gdef \@abspage@last{8}
```

### `items/dyck_skeleton_string_decompositions/explanation.log`

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.29 (MiKTeX 26.5) (preloaded format=pdflatex 2026.5.25)  21 JUN 2026 23:00
entering extended mode
 restricted \write18 enabled.
 %&-line parsing enabled.
**./explanation.tex
(explanation.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\size10.clo
File: size10.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
)
\c@part=\count276
\c@section=\count277
\c@subsection=\count278
\c@subsubsection=\count279
\c@paragraph=\count280
\c@subparagraph=\count281
\c@figure=\count282
\c@table=\count283
\abovecaptionskip=\skip49
\belowcaptionskip=\skip50
\bibindent=\dimen150
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsmath.sty
Package: amsmath 2025/07/09 v2.17z AMS math features
\@mathmargin=\skip51

For additional information on amsmath, use the `?' option.
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amstext.sty
Package: amstext 2024/11/17 v2.01 AMS text

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsgen.sty
File: amsgen.sty 1999/11/30 v2.0 generic functions
\@emptytoks=\toks17
\ex@=\dimen151
))
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsbsy.sty
Package: amsbsy 1999/11/29 v1.2d Bold Symbols
\pmbraise@=\dimen152
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsopn.sty
Package: amsopn 2022/04/08 v2.04 operator names
)
\inf@bad=\count284
LaTeX Info: Redefining \frac on input line 233.
\uproot@=\count285
\leftroot@=\count286
LaTeX Info: Redefining \overline on input line 398.
LaTeX Info: Redefining \colon on input line 409.
\classnum@=\count287
\DOTSCASE@=\count288
LaTeX Info: Redefining \ldots on input line 495.
LaTeX Info: Redefining \dots on input line 498.
LaTeX Info: Redefining \cdots on input line 619.
\Mathstrutbox@=\box53
\strutbox@=\box54
LaTeX Info: Redefining \big on input line 721.
LaTeX Info: Redefining \Big on input line 722.
LaTeX Info: Redefining \bigg on input line 723.
LaTeX Info: Redefining \Bigg on input line 724.
\big@size=\dimen153
LaTeX Font Info:    Redeclaring font encoding OML on input line 742.
LaTeX Font Info:    Redeclaring font encoding OMS on input line 743.
\macc@depth=\count289
LaTeX Info: Redefining \bmod on input line 904.
LaTeX Info: Redefining \pmod on input line 909.
LaTeX Info: Redefining \smash on input line 939.
LaTeX Info: Redefining \relbar on input line 969.
LaTeX Info: Redefining \Relbar on input line 970.
\c@MaxMatrixCols=\count290
\dotsspace@=\muskip17
\c@parentequation=\count291
\dspbrk@lvl=\count292
\tag@help=\toks18
\row@=\count293
\column@=\count294
\maxfields@=\count295
\andhelp@=\toks19
\eqnshift@=\dimen154
\alignsep@=\dimen155
\tagshift@=\dimen156
\tagwidth@=\dimen157
\totwidth@=\dimen158
\lineht@=\dimen159
\@envbody=\toks20
\multlinegap=\skip52
\multlinetaggap=\skip53
\mathdisplay@stack=\toks21
LaTeX Info: Redefining \[ on input line 2950.
LaTeX Info: Redefining \] on input line 2951.
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amscls\amsthm.sty
Package: amsthm 2020/05/29 v2.20.6
\thm@style=\toks22
\thm@bodyfont=\toks23
\thm@headfont=\toks24
\thm@notefont=\toks25
\thm@headpunct=\toks26
\thm@preskip=\skip54
\thm@postskip=\skip55
\thm@headsep=\skip56
\dth@everypar=\toks27
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amssymb.sty
Package: amssymb 2013/01/14 v3.01 AMS font symbols

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amsfonts.sty
Package: amsfonts 2013/01/14 v3.01 Basic AMSFonts support
\symAMSa=\mathgroup4
\symAMSb=\mathgroup5
LaTeX Font Info:    Redeclaring math symbol \hbar on input line 98.
LaTeX Font Info:    Overwriting math alphabet `\mathfrak' in version `bold'
(Font)                  U/euf/m/n --> U/euf/b/n on input line 106.
))
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/geometry\geometry.sty
Package: geometry 2026/03/07 v6.0 Page Geometry

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/graphics\keyval.sty
Package: keyval 2022/05/29 v1.15 key=value parser (DPC)
\KV@toks@=\toks28
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/generic/iftex\ifvtex.sty
Package: ifvtex 2019/10/25 v1.7 ifvtex legacy package. Use iftex instead.

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/generic/iftex\iftex.sty
Package: iftex 2024/12/12 v1.0g TeX engine tests
))
\Gm@cnth=\count296
\Gm@cntv=\count297
\c@Gm@tempcnt=\count298
\Gm@bindingoffset=\dimen160
\Gm@wd@mp=\dimen161
\Gm@odd@mp=\dimen162
\Gm@even@mp=\dimen163
\Gm@layoutwidth=\dimen164
\Gm@layoutheight=\dimen165
\Gm@layouthoffset=\dimen166
\Gm@layoutvoffset=\dimen167
\Gm@dimlist=\toks29

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/geometry\geometry.cfg))
\c@conjecture=\count299
\c@proposition=\count300

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/l3backend\l3backend-pdft
ex.def
File: l3backend-pdftex.def 2026-02-18 L3 backend support: PDF output (pdfTeX)
\l__color_backend_stack_int=\count301
) (explanation.aux)
\openout1 = `explanation.aux'.

LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 17.
LaTeX Font Info:    ... okay on input line 17.
LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 17.
LaTeX Font Info:    ... okay on input line 17.
LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 17.
LaTeX Font Info:    ... okay on input line 17.
LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 17.
LaTeX Font Info:    ... okay on input line 17.
LaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 17.
LaTeX Font Info:    ... okay on input line 17.
LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 17.
LaTeX Font Info:    ... okay on input line 17.
LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 17.
LaTeX Font Info:    ... okay on input line 17.

*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
*geometry* verbose mode - [ preamble ] result:
* driver: pdftex
* paper: <default>
* layout: <same size as paper>
* layoutoffset:(h,v)=(0.0pt,0.0pt)
* modes: 
* h-part:(L,W,R)=(72.26999pt, 469.75502pt, 72.26999pt)
* v-part:(T,H,B)=(72.26999pt, 650.43001pt, 72.26999pt)
* \paperwidth=614.295pt
* \paperheight=794.96999pt
* \textwidth=469.75502pt
* \textheight=650.43001pt
* \oddsidemargin=0.0pt
* \evensidemargin=0.0pt
* \topmargin=-37.0pt
* \headheight=12.0pt
* \headsep=25.0pt
* \topskip=10.0pt
* \footskip=30.0pt
* \marginparwidth=65.0pt
* \marginparsep=11.0pt
* \columnsep=10.0pt
* \skip\footins=9.0pt plus 4.0pt minus 2.0pt
* \hoffset=0.0pt
* \voffset=0.0pt
* \mag=1000
* \@twocolumnfalse
* \@twosidefalse
* \@mparswitchfalse
* \@reversemarginfalse
* (1in=72.27pt=25.4mm, 1cm=28.453pt)

LaTeX Font Info:    Trying to load font information for U+msa on input line 18.

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsa.fd
File: umsa.fd 2013/01/14 v3.01 AMS symbols A
)
LaTeX Font Info:    Trying to load font information for U+msb on input line 18.


(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsb.fd
File: umsb.fd 2013/01/14 v3.01 AMS symbols B
)
[1

{C:/Users/User/AppData/Local/MiKTeX/fonts/map/pdftex/pdftex.map}] [2]
[3] [4] [5] [6]
Underfull \hbox (badness 10000) in paragraph at lines 556--556
[]\OT1/cmr/m/n/10 East3/East5/West3/West5
 []

[7]
Underfull \hbox (badness 5832) in paragraph at lines 575--579
[]\OT1/cmr/m/n/10 Graham Hawkes, \OT1/cmr/m/it/10 Dyck Sym-met-ric Func-tions a
nd Ap-pli-ca-tions to $\OML/cmm/m/it/10 q; t$\OT1/cmr/m/it/10 -Catalan Poly-no-
mi-als\OT1/cmr/m/n/10 ,
 []

[8] (explanation.aux)
 ***********
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
 ***********
 ) 
Here is how much of TeX's memory you used:
 2447 strings out of 467683
 35945 string characters out of 5415205
 454356 words of memory out of 5000000
 31522 multiletter control sequences out of 15000+600000
 638407 words of font info for 82 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 57i,10n,65p,242b,231s stack positions out of 10000i,1000n,20000p,200000b,200000s
 <C:\Users\User\AppData\Local\MiKTeX\fonts/pk/ljfour/jknappen/ec/dpi600\tcrm1
000.pk><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts
/cm/cmbx10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/
amsfonts/cm/cmbx12.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1
/public/amsfonts/cm/cmex10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fon
ts/type1/public/amsfonts/cm/cmmi10.pfb><C:/Users/User/AppData/Local/Programs/Mi
KTeX/fonts/type1/public/amsfonts/cm/cmmi12.pfb><C:/Users/User/AppData/Local/Pro
grams/MiKTeX/fonts/type1/public/amsfonts/cm/cmmi5.pfb><C:/Users/User/AppData/Lo
cal/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmmi7.pfb><C:/Users/User/App
Data/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr10.pfb><C:/Users/U
ser/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr12.pfb><C:/
Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr17.p
fb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/
cmr5.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfon
ts/cm/cmr7.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/
amsfonts/cm/cmsy10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1
/public/amsfonts/cm/cmsy7.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/font
s/type1/public/amsfonts/cm/cmti10.pfb><C:/Users/User/AppData/Local/Programs/MiK
TeX/fonts/type1/public/amsfonts/cm/cmti7.pfb><C:/Users/User/AppData/Local/Progr
ams/MiKTeX/fonts/type1/public/amsfonts/cm/cmtt10.pfb>
Output written on explanation.pdf (8 pages, 255366 bytes).
PDF statistics:
 119 PDF objects out of 1000 (max. 8388607)
 0 named destinations out of 1000 (max. 500000)
 1 words of extra memory for PDF output out of 10000 (max. 10000000)

```

### `items/dyck_skeleton_string_decompositions/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 255366
sha256: 3b17f0236b2baedcda8226853a60b9f072877e80c596610c9d1c8e960bf5de19
```

### `items/dyck_skeleton_string_decompositions/explanation.synctex.gz`

```text
[binary artifact not expanded]
size_bytes: 69530
sha256: 12fc768cbc096c95188463acfb659da6978a675fb1434e9828fd2c1a63ea82a4
```

### `items/dyck_skeleton_string_decompositions/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}
\usepackage[margin=1in]{geometry}

\newcommand{\defc}{\operatorname{defc}}
\newcommand{\dinv}{\operatorname{dinv}}
\newcommand{\area}{\operatorname{area}}
\newcommand{\NRCM}{\operatorname{NRCM}}

\newtheorem{conjecture}{Conjecture}
\newtheorem{proposition}{Proposition}

\title{Dyck Skeleton String Decompositions}
\author{}
\date{}

\begin{document}
\maketitle

\section{Overview}

This note studies string decompositions inside fixed deficit layers.  A string
is a sequence of paths along which area increases by \(1\), dinv decreases by
\(1\), and deficit remains fixed.  The guiding example is Hawkes's
low-deficit Dyck skeleton formula, where special skeletons start strings whose
lower halves cover the corresponding deficit layers.

The main conjectural extension considered here is the case \(r=\tau s+1\).
For this family we define \(\tau\)-Dyck sequences, a \(\tau\)-analogue of
dinv, special skeletons, and a conjectural lower-half string formula.  A full
coefficient formula requires either deficit-layer \(q,t\)-symmetry or a direct
full coefficient-dictionary identity.

The final sections describe finite computational checks.  These checks support
the conjectural formula in selected ranges and also test a separate
general-slope diagnostic called NRCM.

All coefficient polynomials in this note use the convention
\(q^{\area}t^{\dinv}\).  Thus the lower half of a fixed deficit layer is the
part with \(\area\le\dinv\).

The rest of the note first introduces the mathematical sequences, paths, and
claims and then describes the finite checks attached to them.

\section{Common Vocabulary}

For a fixed total degree \(M\), the deficit of a sequence or path \(X\) is
\[
  \defc(X)=M-\area(X)-\dinv(X).
\]
A string of fixed deficit \(e\) is a sequence
\[
  X_0,X_1,\ldots,X_m
\]
such that \(\area(X_{i+1})=\area(X_i)+1\),
\(\dinv(X_{i+1})=\dinv(X_i)-1\), and \(\defc(X_i)=e\) for every \(i\).
Thus every term of the string has total degree \(M-e\).

The lower half of deficit \(e\) means the paths with
\[
  \area\le \left\lfloor\frac{M-e}{2}\right\rfloor.
\]
A lower-half decomposition is a disjoint cover of this lower-half set by the
initial segments of strings.

The remaining sections use this vocabulary in three settings: the classical
Dyck setting, the \(r=\tau s+1\) rational setting, and the NRCM diagnostic.
The mathematical definitions are stated first.  The scripts and finite checks
are described separately afterward.

\section{The Classical Model}

An ordinary Dyck sequence of length \(n\) is an integer sequence
\[
  x=(x_0,\ldots,x_{n-1})
\]
with
\[
  x_0=0,\qquad x_i\ge0,\qquad x_{i+1}\le x_i+1.
\]
Its area is
\[
  \area(x)=\sum_{i=0}^{n-1}x_i,
\]
and the classical dinv statistic in this notation is
\[
  \dinv(x)=\#\{(i,j):0\le i<j<n,\ x_i=x_j\text{ or }x_i=x_j+1\}.
\]
Here \(M=\binom n2\), so
\[
  \defc(x)=\binom n2-\area(x)-\dinv(x).
\]

The skeleton terminology in this section is imported from Section 5
of~\cite{Hawkes2026DyckSymmetric}.  In Hawkes's setup, extractable entries are
the entries removed by the recursive down move, full Dyck skeletons are the
terminal Dyck sequences with no extractable entry, and special Dyck skeletons
are the permitted string starts after Hawkes's special attachment convention.
The \(\mathrm{up}\) and \(\mathrm{down}\) moves then generate the strings.

The classical theorem used as the template here is Hawkes's low-deficit
skeleton formula.  All formulas in this note use the convention
\(q^{\area}t^{\dinv}\):
\[
  \left.C_n(q,t)\right|_{\binom n2-2n+8\le \deg_{q,t}\le \binom n2}
  =
  \sum_{\substack{S\text{ special Dyck skeleton of length }n\\
                  \defc(S)\le 2n-8}}
  \frac{q^{\area(S)}t^{\dinv(S)+1}
        -q^{\dinv(S)+1}t^{\area(S)}}{t-q}.
\]
The rational expression is a finite interval contribution: if
\(a=\area(S)\), \(\nu=\dinv(S)\), and \(e=\defc(S)\), then in the low-deficit
range of the theorem one has \(a\le\nu\), and
\[
  \frac{q^a t^{\nu+1}-q^{\nu+1}t^a}{t-q}
  =
  \sum_{i=a}^{\nu}q^i t^{M-e-i}.
\]
Hawkes proves that these strings cover the lower half of every deficit layer
with \(\defc\le2n-8\).  Equivalently, their lower-half contributions are
truncated at the midpoint:
\[
  \sum_{i=a}^{\left\lfloor(M-e)/2\right\rfloor} q^i t^{M-e-i}.
\]
The upper half is then supplied by the symmetry \(C_n(q,t)=C_n(t,q)\).

\section{The \(\tau\)-Dyck Model for \(r=\tau s+1\)}

Fix integers \(s\ge1\) and \(\tau>1\), and put \(r=\tau s+1\).  For the
conjectural model in this note, the ordinary Dyck growth bound \(+1\) is
replaced by \(+\tau\).

A \(\tau\)-Dyck sequence of length \(s\) is an integer sequence
\[
  x=(x_1,\ldots,x_s),\qquad
  x_1=0,\qquad x_i\ge0,\qquad x_{i+1}\le x_i+\tau.
\]
These inequalities imply
\[
  0\le x_i\le \tau(i-1).
\]
Thus there are only finitely many \(\tau\)-Dyck sequences of each length.

The area statistic is
\[
  \area(x)=\sum_{i=1}^s x_i.
\]
The dinv statistic used in this note is the following \(\tau\)-analogue:
\[
  \dinv(x)=\sum_{1\le i<j\le s}
  \begin{cases}
    \max(0,x_i+\tau-x_j), & x_i\le x_j,\\
    \max(0,x_j+1+\tau-x_i), & x_i>x_j.
  \end{cases}
\]
The total degree is
\[
  M=\tau\binom{s}{2},
\]
and
\[
  \defc(x)=M-\area(x)-\dinv(x).
\]

For a deficit cutoff \(B\), define the aggregate polynomial
\[
  \mathcal C_{\tau,s}^{\le B}(q,t)
  =
  \sum_{\substack{x\text{ is a }\tau\text{-Dyck sequence}\\
                  0\le \defc(x)\le B}}
      q^{\area(x)}t^{\dinv(x)}.
\]
The conjectural bound is
\[
  B=(s-2)(\tau+1)-4.
\]

For comparison with the position-coordinate notation used later in the NRCM
diagnostic, when \(r=\tau s+1\) one has
\(\lfloor ri/s\rfloor=\tau i\) for \(0\le i<s\), so
\(\Delta_i=\tau\) for \(0\le i<s-1\).  In \(Q\)-coordinates, path-validity
gives
\[
  Q_{i+1}\le Q_i+\tau\qquad(0\le i<s-1).
\]
Identifying \(x_{i+1}=Q_i\) gives exactly the \(\tau\)-Dyck growth bound
\(x_{i+2}\le x_{i+1}+\tau\).

\section{Rational Special Skeletons}

For this conjectural model, all skeletons are \(\tau\)-Dyck sequences
of the fixed length \(s\).  Deletion is used only to define extractability and
the recursive map operations.

Let \(x=(x_1,\ldots,x_s)\) be a \(\tau\)-Dyck sequence.  An entry \(x_j\) is extractable if:
\[
\begin{gathered}
  x_j>0,\\
  \#\{i<j:\max(0,x_j-\tau)\le x_i<x_j\}=1,
\end{gathered}
\]
and deleting \(x_j\) leaves a \(\tau\)-Dyck sequence.  The endpoint
conventions are explicit:
\begin{itemize}
  \item \(j=1\) cannot occur because \(x_1=0\);
  \item if \(1<j<s\), deletion is equivalent to the splice inequality
  \[
    x_{j+1}\le x_{j-1}+\tau;
  \]
  \item if \(j=s\), there is no extra splice inequality.
\end{itemize}
The sequence after deletion is
\[
  (x_1,\ldots,x_{j-1},x_{j+1},\ldots,x_s).
\]
The recursive moves use left-to-right extraction order: the first extractable
entry is the one removed.

A full skeleton is a \(\tau\)-Dyck sequence of length \(s\) with no extractable entry.
For \(s\ge4\), one full skeleton is excluded from the starting set:
\[
  (0,0,1,\underbrace{0,\ldots,0}_{s-4\text{ zeros}},\tau).
\]
For \(s=4\) this is \((0,0,1,\tau)\).  For \(s<4\), there is no excluded full
skeleton and no special upward attachment.  A special skeleton is a full
skeleton other than this excluded sequence.

The excluded full skeleton is not removed from the strings.  It is attached to
the string beginning at
\[
  (0,\ldots,0,\tau)
\]
by the special upward move
\[
  (0,\ldots,0,\tau)
  \longmapsto
  (0,0,1,\underbrace{0,\ldots,0}_{s-4\text{ zeros}},\tau)
  \qquad(s\ge4).
\]

\section{Conjectural Lower-Half Formula and Symmetry Completion}

\begin{conjecture}[Special-skeleton lower-half formula for \(r=\tau s+1\)]
Fix \(s\ge1\) and \(\tau>1\), and set \(M=\tau\binom{s}{2}\) and
\[
  B=(s-2)(\tau+1)-4.
\]
For \(0\le d\le B\), put
\[
  L_d=\left\lfloor\frac{M-d}{2}\right\rfloor.
\]
If \(B\ge0\), the lower-area part of each deficit layer \(d\le B\) is obtained
by summing over all special skeletons \(z\) of length \(s\) with
\(\defc(z)=d\).  These skeletons are lower-half starts.  Write
\[
  a=\area(z),\qquad \nu=\dinv(z),\qquad d=\defc(z).
\]
Then \(z\) contributes the lower-half interval ending at the cutoff \(L_d\):
\[
  \sum_{i=a}^{L_d} q^i t^{M-d-i}.
\]
The asserted identity is
\[
  \sum_{\substack{x\text{ is a }\tau\text{-Dyck sequence}\\
                  \defc(x)=d,\ \area(x)\le L_d}}
      q^{\area(x)}t^{\dinv(x)}
  =
  \sum_{\substack{z\text{ special skeleton}\\ \defc(z)=d}}
      \sum_{i=\area(z)}^{L_d} q^i t^{M-d-i}.
\]
\end{conjecture}

The full aggregate polynomial \(\mathcal C_{\tau,s}^{\le B}(q,t)\) follows
from this lower-half statement only with an additional symmetry input.  The
needed symmetry is deficit-layer symmetry: for each \(0\le d\le B\),
\[
  \sum_{\defc(x)=d}q^{\area(x)}t^{\dinv(x)}
  =
  \sum_{\defc(x)=d}q^{\dinv(x)}t^{\area(x)},
\]
where the sums run over \(\tau\)-Dyck sequences of length \(s\).
Equivalently, one may prove the full coefficient dictionary directly.  Without
one of these two inputs, the displayed conjecture is only a lower-half
string-start formula.

A useful algebraic packaging of a full string interval is the rational
expression
\[
  \frac{q^a t^{\nu+1}-q^{\nu+1}t^a}{t-q}.
\]
When \(a\le\nu\), this expands as the full interval
\[
  \sum_{i=a}^{\nu}q^i t^{M-d-i}.
\]
If \(a>\nu\), the same expression expands with the opposite sign over the open
interval between \(\nu\) and \(a\).  That signed expansion is algebraic
bookkeeping, not the lower-half string interpretation above.

\section{Computations for the Conjecture}

The relevant scripts are
\[
  \texttt{code/check\_r1mod\_skeleton\_strings.py}
  \qquad\text{and}\qquad
  \texttt{code/run\_official\_r1mod\_checks.py}.
\]
Some script options and output fields use the legacy name \texttt{defect}.  The
relevant names here are
\[
  \texttt{--max-defect}
  \qquad\text{and}\qquad
  \texttt{initial\_passing\_defect\_range}.
\]
In the mathematical exposition these refer to deficit.

The single-case command
\[
  \texttt{python code/check\_r1mod\_skeleton\_strings.py --tau T --s S}
\]
uses \(B=(S-2)(T+1)-4\) unless \(\texttt{--max-defect}\) is supplied.  It
performs a finite formula check by comparing two coefficient dictionaries.  The
direct dictionary is obtained by exhaustive \(\tau\)-Dyck sequence enumeration in the
retained deficit range, with pruning only when an exact suffix bound proves that
the remaining suffix cannot reach the required total \(\area+\dinv\).  The
predicted dictionary in the script is obtained from the signed rational
expressions above, so this check is a direct full-dictionary identity rather
than only a lower-half comparison.  In the exposition here, the signed terms
should be read as algebraic bookkeeping; the string picture is the lower-half
formula plus deficit-layer symmetry or direct full-dictionary agreement.  The
formula status is \(\texttt{PASS}\) iff the two dictionaries are identical.  If
the requested bound is negative, there is no nonnegative deficit layer to test.

For \(S\ge5\), the same script also attempts a lower-half map check.  The
implemented local cases are named East3, East5, West3, and West5 in the code.
This note treats those labels as implementation-defined local moves.  The
special-skeleton map check tests the implemented up and down moves:
preservation of deficit, area change by \(1\), inverse behavior on checked
steps, and disjoint coverage of the lower-half target.  A map status of
\(\texttt{PASS}\) means that the checked lower-half strings cover the target
through the supported local cases.  A status of \(\texttt{PARTIAL}\) means
that no contradiction was found before the implemented moves reached the code
label \(\texttt{unsupported\_level\_7}\).  For \(s\ge4\), this map check also
includes the special upward attachment from \((0,\ldots,0,\tau)\) to the
excluded full skeleton.

The batch runner is configured to run the following finite grid.  Since no run
log is included here, this table records the intended finite test range, not
independent evidence that each listed command has been freshly run.
\[
\begin{array}{c|c|c}
\tau & \text{formula cases} & \text{formula+map cases}\\
\hline
2 & 1\le s\le14 & 5\le s\le14\\
3 & 1\le s\le12 & 5\le s\le12\\
4 & 1\le s\le10 & 5\le s\le10\\
5 & 1\le s\le9  & 5\le s\le9
\end{array}
\]
The reproducible command is
\[
  \texttt{python code/run\_official\_r1mod\_checks.py}.
\]

For example, at \((\tau,s)=(2,15)\) the conjectural bound is exactly
\[
  (15-2)(2+1)-4=35.
\]
The command
\[
  \texttt{python code/check\_r1mod\_skeleton\_strings.py --tau 2 --s 15 --report-level7}
\]
is designed to test the formula through precisely the conjectural bound
\(\defc\le35\) and reports any level-7 obstructions encountered by the partial
map.

\section{The Naive Rational Cyclic Map}

The NRCM diagnostic applies to coprime positive integers \(r\) and \(s\) with
\(s>1\).  Let
\[
  H_i=\left\lfloor\frac{ri}{s}\right\rfloor,\qquad
  L_i\in\{0,\ldots,s-1\},\quad L_i\equiv ri\pmod s,\qquad
  \Delta_i=H_{i+1}-H_i
\]
for \(0\le i<s\), where \(\Delta_i\) is used only for \(0\le i<s-1\).
A position-coordinate path is an integer sequence
\[
  Q=(Q_0,\ldots,Q_{s-1})
\]
with
\[
  Q_0=0,\qquad 0\le Q_i\le H_i.
\]
It is path-valid when the path heights
\[
  P_i=H_i-Q_i
\]
satisfy
\[
  P_0\le P_1\le\cdots\le P_{s-1}.
\]

The diagnostic area is
\[
  \area(Q)=\sum_{i=0}^{s-1}Q_i,
\]
and \(M=\sum_i H_i\).  The diagnostic deficit is defined by
\[
  \defc(Q)=\sum_{1\le i<j<s}\delta_{ij}(Q),
\]
where the summand is as follows.  Put
\[
  u_{ij}=|Q_i-Q_j|.
\]
If \(Q_i\ne Q_j\) and the comparisons \(Q_i>Q_j\) and \(L_i>L_j\) have
opposite truth values, replace \(u_{ij}\) by \(u_{ij}-1\); then replace it by
\(\max(u_{ij},0)\).  Define
\[
  v_{ij}=
  \begin{cases}
    \Delta_i-(Q_{i+1}-Q_i), & Q_i>Q_j,\\
    \Delta_{i-1}-(Q_i-Q_{i-1}), & Q_j>Q_i,\\
    0, & Q_i=Q_j.
  \end{cases}
\]
Then
\[
  \delta_{ij}(Q)=\min(u_{ij},v_{ij}).
\]
The second quantity \(v_{ij}\) is not separately clamped in this diagnostic
definition.  On path-valid inputs it is nevertheless nonnegative: the two
nonzero cases are exactly the adjacent inequalities
\(Q_{i+1}-Q_i\le\Delta_i\) and \(Q_i-Q_{i-1}\le\Delta_{i-1}\).  No replacement
by \(\max(v_{ij},0)\) is part of the implemented statistic.
Finally,
\[
  \dinv(Q)=M-\area(Q)-\defc(Q).
\]
These are the statistics used by the NRCM scripts.

For a suffix \(I_k=\{k,k+1,\ldots,s-1\}\), list its columns in increasing
label order \(L_i\).  The candidate \(T_k(Q)\) cyclically moves the \(Q\)-value
from each listed column to the next listed column and moves the last listed
value to the first listed column after adding \(1\).  Columns outside \(I_k\)
are unchanged.  The strict NRCM tries \(k=1,2,\ldots,s-1\), stops at the first
\(k\) for which \(T_k(Q)\) satisfies the capacity inequalities
\[
  0\le T_k(Q)_i\le H_i,
\]
and defines
\[
  \NRCM(Q)=T_k(Q)
\]
only if this first capacity-valid candidate is also path-valid.  If no suffix
is capacity-valid, or if the first capacity-valid suffix is not path-valid,
then \(\NRCM(Q)\) is undefined.

Here is a small successful move.  For slope \(5/3\),
\[
  H=(0,1,3),\qquad L=(0,2,1).
\]
Let \(Q=(0,1,1)\).  For \(k=1\), the suffix columns \(\{1,2\}\) appear in
label order \(2,1\).  Thus \(Q_2=1\) moves to column \(1\), and \(Q_1=1\)
wraps to column \(2\) as \(2\), giving
\[
  T_1(Q)=(0,1,2).
\]
This candidate is capacity-valid and path-valid.

The failure mode in the definition is also important.  For slope \(4/3\),
\[
  H=(0,1,2),\qquad L=(0,1,2),
\]
and \(Q=(0,0,1)\).  The first capacity-valid suffix is \(k=2\), giving
\[
  T_2(Q)=(0,0,2).
\]
Its path heights are \((0,1,0)\), which are not nondecreasing.  Strict NRCM is
therefore undefined on this \(Q\).  In this example \(k=2\) is already the
final suffix, so there is no valid NRCM value.

\section{NRCM Lower-Half Diagnostics}

The NRCM scripts are
\[
  \texttt{code/check\_nrcm\_lower\_half.py}
  \qquad\text{and}\qquad
  \texttt{code/check\_nrcm\_domain.py}.
\]
The lower-half script checks, in finite deficit layers, whether every
below-midline source has a defined NRCM image, whether the image has the same
diagnostic deficit and area one larger, whether the image remains in the
allowed target, and whether the map is injective on the checked sources.  The
domain script is narrower: it checks only definedness on below-midline
sources.

By definition, every defined strict NRCM move raises area by \(1\): the suffix
values are cyclically permuted and the wrapped value is increased by \(1\).
The proof-status issue concerns deficit preservation.  A proof that defined
strict NRCM preserves the diagnostic deficit exists outside this note and has
been partially human-verified, but it is not part of the present argument.  The
finite diagnostics below locate the deficit layers where the directed-chain
picture can be checked directly.

\begin{proposition}[Conditional NRCM chain consequence]
Fix a slope \(r/s\), a deficit \(e\), and \(M=\sum_iH_i\).  Let
\[
  \mathcal L_e=\{Q:\ Q\text{ is valid},\ \defc(Q)=e,\ 
    \area(Q)\le \lfloor(M-e)/2\rfloor\}
\]
be the checked lower-half target, including midpoint targets when
\((M-e)/2\) is an integer.  Suppose strict NRCM is defined on every valid path
of deficit \(e\) with
\[
  \area(Q)<\frac{M-e}{2},
\]
so no move is required from a midpoint target.  Suppose the checked moves
preserve deficit, raise area by \(1\), land in \(\mathcal L_e\), and are
injective on those sources.  Suppose also that every path in \(\mathcal L_e\)
which is not declared NRCM-minimal has a checked predecessor in the same
deficit layer.  Then \(\mathcal L_e\) is covered by directed NRCM chains.  The
chain starts are the NRCM-minimal paths, meaning valid paths of deficit \(e\)
that are not the NRCM image of any lower-area path in the same checked layer.
\end{proposition}

To turn such lower-half strings into a full coefficient formula, one
additionally needs equality of the predicted interval dictionary with the full
direct coefficient dictionary, or a separately proved \(q,t\)-symmetry for the
homogeneous deficit layer being considered.

The output field
\[
  \texttt{initial\_passing\_defect\_range: 0..D}
\]
means that every deficit layer \(0,1,\ldots,D\), inclusive, passed the specific
diagnostic run.  For the lower-half script this includes definedness, deficit
preservation, area increase, target membership, and injectivity.  For the
domain script it includes only definedness.  The notes accompanying these
values record tentative patterns; claims that use those patterns should include
the corresponding command and run output.

\section{Status of Claims}

\begin{center}
\begin{tabular}{p{0.31\linewidth}|p{0.54\linewidth}}
claim & status\\
\hline
classical Dyck skeleton formula &
proved by Hawkes, Theorem 5.35 of~\cite{Hawkes2026DyckSymmetric}, for
\(n\ge4\) and \(\defc\le 2n-8\)\\
\(r=\tau s+1\) special-skeleton lower-half formula &
conjectural; finite exhaustive coefficient checks are implemented for selected
\((\tau,s)\), and full recovery also needs deficit-layer symmetry or direct
full-dictionary agreement\\
East3/East5/West3/West5 lower-half map &
finite computational diagnostic using the local moves named in the code; the
implemented map stops when an unsupported level-7 case is reached\\
NRCM deficit preservation &
conditional in this note outside the finite runs; defined NRCM moves raise area
by \(1\) by construction, while preservation of diagnostic deficit is the
separate proof-status claim
\end{tabular}
\end{center}

The NRCM material is diagnostic rather than a complete theorem in this note.
The definitions, examples, and finite checks are included because they test the
same directed-chain picture for general coprime slopes.  Claims depending on
NRCM deficit preservation should be read as conditional unless accompanied by a
separate proof or by the relevant finite run output.

\begin{thebibliography}{9}

\bibitem{Hawkes2026DyckSymmetric}
Graham Hawkes,
\emph{Dyck Symmetric Functions and Applications to \(q,t\)-Catalan
Polynomials},
arXiv:2605.13003, 2026.
\[
  \texttt{https://arxiv.org/abs/2605.13003}
\]

\end{thebibliography}

\end{document}
```

### `items/dyck_skeleton_string_decompositions/html/body.html`

```html
<p>
  This item separates three layers: the proved classical Dyck skeleton-string
  theorem, the conjectural <code>r = tau*s + 1</code> special-skeleton formula,
  and the stronger lower-half string decomposition supplied by the currently
  implemented East3/East5 partial map.
</p>

<p>
  In the <code>r == 1 mod s</code> case, the formula in terms of special
  skeletons remains conjectural. The East3/East5 partial up/down map is not
  claimed to give the full lower-half decomposition for every
  <code>(tau,s,defc)</code> where the formula is expected to hold. It gives a
  checked decomposition only through defect layers where no unsupported level-7
  move appears.
</p>

<p>
  In the recorded checks, this partial map reaches all conjectural formula
  defect layers for <code>tau=2, 5&lt;=s&lt;=14</code>,
  <code>tau=3, 5&lt;=s&lt;=12</code>, and
  <code>tau=4, 5&lt;=s&lt;=10</code>. A later diagnostic at
  <code>tau=2, s=15</code> still passed the formula check through
  <code>defc&lt;=35</code>, but the partial map hit 14 unsupported level-7
  records at defect 35.
</p>

<p>
  The naive rational cyclic map (NRCM) is a separate general-rational
  construction. In position coordinates, it tries right suffixes in order,
  cyclically moves the suffix values in rational label order, and stops at the
  first capacity-valid candidate. The strict NRCM is defined only if that first
  capacity-valid candidate is also path-valid.
</p>

<p>
  There is an AI-generated proof in the Dyck research notes that the strict
  NRCM preserves deficit whenever it is defined. Thus, once defined, it gives a
  valid rational path move with unchanged deficit. Only after this independent
  NRCM fact do we compare it to the <code>r = tau*s + 1</code> setting: finite
  checks indicate that NRCM agrees with the special-skeleton lower-half map
  where both are defined.
</p>
```

### `items/dyck_skeleton_string_decompositions/item.yaml`

```yaml
title: Dyck Skeleton String Decompositions
slug: dyck_skeleton_string_decompositions
status_summary: Classical skeleton strings are proved in the 2026 preprint in the low-deficit range; r=tau*s+1, tau>1 strings and formula are conjectural and checked finitely here.
source_paths:
  - ../Dyck/paper/working_drafts/arxiv_submission.tex
  - ../Dyck/code/codex_project/red_team_up_string_decomposition.py
  - ../Dyck/code/codex_project/red_team_rational_skeleton_string_formula.py
  - ../Dyck/code/experiments/skeleton_string_decompositions/ssd_r1_001.py
  - code/check_r1mod_skeleton_strings.py
downloads:
  - explanation.tex
```

### `items/dyck_skeleton_string_decompositions/README.md`

```markdown
# Dyck Skeleton String Decompositions

Status summary: Classical skeleton strings are proved in the 2026 preprint in
the low-deficit range.  The `r=tau*s+1`, `tau>1` skeleton formula is
conjectural and supported here by finite checks.  The East3/East5 partial
up/down map gives finite checked lower-half decompositions only through the
defect layers where no unsupported level-7 move appears.  The NRCM has an
AI-generated proof of deficit preservation wherever it is defined, but this
material is not human verified.

## Summary

This item will combine the classical Dyck skeleton string decomposition and
the `r=tau*s+1`, `tau>1` rational analogue.  The rational code checks the
conjectural skeleton formula separately from the stronger lower-half string
decomposition supplied by the currently implemented East3/East5 partial map.

## Provenance

Source repository: `Dyck`

Source paths:

- `../Dyck/paper/working_drafts/arxiv_submission.tex`
- `../Dyck/code/codex_project/red_team_up_string_decomposition.py`
- `code/check_r1mod_skeleton_strings.py`
- `../Dyck/code/codex_project/red_team_rational_skeleton_string_formula.py`
- `../Dyck/code/experiments/skeleton_string_decompositions/ssd_r1_001.py`
- `../Dyck/paper/research_notes/naive_rational_cyclic_map_thm.tex`

Transfer type: planned curated writeup with adapted code as needed.

## Layers

Python layer: `code/check_r1mod_skeleton_strings.py` is the current item-level
checker for the `r=tau*s+1`, `tau>1` conjectural case.

LaTeX layer: planned.

HTML layer: planned.

## Status

- Classical skeleton strings: theorem in the 2026 preprint, in the low-deficit range.
- `r=tau*s+1`, `tau>1` skeleton formula: conjectural; finite checks only.
- East3/East5 partial map: finite lower-half decomposition evidence only up to
  the defect level where unsupported level-7 moves first appear.
- NRCM material: AI proof of deficit preservation where defined, with
  computational support for lower-half definedness/injectivity ranges; not
  human verified.

## Review Needs

- Record formula checks separately from partial-map decomposition checks.
- Keep the largest no-level-7 defect layer visible for each checked
  `(tau,s)`.
```

### `items/dyck_skeleton_string_decompositions/WRITING_PACKET.md`

```markdown
# Writing Packet: Dyck Skeleton String Decompositions

Target file for the writing agent:

````text
Combinatorics/items/dyck_skeleton_string_decompositions/explanation.tex
````

The current task is a rewrite of `explanation.tex`, not a light polish.  The
rewritten explanation should be public-facing, self-contained, and honest about
which parts are proved, conjectural, computationally checked, or draft-level.

Do not edit `explanation.tex` until the writing agent has first presented its
plan to the user.

## Item-Level Context

Item slug:

````text
dyck_skeleton_string_decompositions
````

Current item summary:

- Classical Dyck skeleton strings are proved in the 2026 Hawkes preprint in
  the low-deficit range.
- The `r = tau*s + 1`, `tau > 1` skeleton formula is conjectural.
- The item-level code gives finite checks for the conjectural formula and for
  the currently implemented East3/East5 partial lower-half map.
- The NRCM material is a separate general-rational diagnostic.  It has an
  AI-generated proof draft of deficit preservation where the map is defined,
  but the item must not present it as a fully human-verified theorem.

Primary local files for the item:

````text
Combinatorics/items/dyck_skeleton_string_decompositions/README.md
Combinatorics/items/dyck_skeleton_string_decompositions/item.yaml
Combinatorics/items/dyck_skeleton_string_decompositions/explanation.tex
Combinatorics/items/dyck_skeleton_string_decompositions/html/body.html
Combinatorics/items/dyck_skeleton_string_decompositions/code/README.md
Combinatorics/items/dyck_skeleton_string_decompositions/code/check_r1mod_skeleton_strings.py
Combinatorics/items/dyck_skeleton_string_decompositions/code/run_official_r1mod_checks.py
Combinatorics/items/dyck_skeleton_string_decompositions/code/check_nrcm_lower_half.py
Combinatorics/items/dyck_skeleton_string_decompositions/code/check_nrcm_domain.py
````

Source paths named by the item:

````text
Dyck/paper/working_drafts/arxiv_submission.tex
Dyck/paper/working_drafts/draft_v3_sections/05_skeletons_setup.tex
Dyck/paper/working_drafts/draft_v3_sections/05_up_down.tex
Dyck/paper/working_drafts/draft_v3_sections/05_east_map.tex
Dyck/paper/working_drafts/draft_v3_sections/05_east_west_inverse.tex
Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex
Dyck/paper/research_notes/rational_generalizations.tex
Dyck/paper/research_notes/naive_rational_cyclic_map_thm.tex
Dyck/paper/research_notes/naive_rational_cyclic_map_readable.tex
Dyck/docs/skeleton_string_decomposition_workflow.md
Dyck/code/experiments/skeleton_string_decompositions/current_state.md
Dyck/code/experiments/skeleton_string_decompositions/evidence_log.md
Dyck/code/experiments/skeleton_string_decompositions/failure_log.md
````

Public citation anchor:

````text
Graham Hawkes, Dyck Symmetric Functions and Applications to q,t-Catalan
Polynomials, arXiv:2605.13003, 2026.
https://arxiv.org/abs/2605.13003
````

## Writing Constraints

Follow:

````text
agents/explanation_writing_agent.md
mathematical_writing.md
pedalogical_princinples.md
explanations_initial_round.md
````

Important consequences:

- The explanation must address outside readers, not repository maintainers.
- Avoid status-ledger prose.  Put provenance and workflow history in README-like
  files, not in the explanation.
- Do not assume the reader has access to hidden `Dyck` notes or internal agent
  workflows.
- Define all nonstandard terms before use.
- Do not upgrade conjectural or AI-draft material to theorem status.
- Explain the code's role mathematically; do not turn the note into an
  implementation walkthrough.
- If the rewrite is substantial, first return a plan with:
  `Explanation goal`, `Reader assumptions`, `Definitions needed`,
  `Main structure`, `Paper connections`, `Code explanation`, and
  `Open questions before drafting`.

## Recommended Exposition Shape

A good rewrite should be shorter and more focused than the current draft.
Suggested structure:

1. **Strings in a deficit layer.**
   Explain the common phenomenon first: a string is a sequence of objects with
   area increasing by one, dinv decreasing by one, and fixed deficit.  The lower
   half of a deficit layer consists of terms with area at most the midpoint.

2. **Classical theorem.**
   Define ordinary Dyck sequences, area, dinv, deficit, full skeletons, and
   special skeletons only to the degree needed to state the low-deficit string
   decomposition.  State the classical result as proved by the 2026 preprint.
   Do not reproduce the East/West local case analysis.

3. **Rational `r = tau*s + 1` conjecture.**
   Define normalized `tau`-Dyck sequences, `dinv_tau`, total degree
   `M = tau*binom(s,2)`, deficit, extractable entries, and special rational
   skeletons.  State the conjectural low-deficit formula with bound
   `defc_tau <= (s-2)(tau+1)-4`.

4. **Computational evidence.**
   Explain that the checker compares coefficient dictionaries for the formula
   and separately tests the current East3/East5 lower-half map.  Make clear
   that `formula_status: PASS` and `map_status: PASS` are different claims, and
   that `map_status: PARTIAL` means the code hit `unsupported_level_7`.

5. **NRCM diagnostic.**
   Keep this short unless the user asks for a full NRCM exposition.  Present
   NRCM as a separate general-rational diagnostic for directed chains.  It is
   not currently a human-verified theorem in the curated item.  The code checks
   finite lower-half definedness, area increase, deficit preservation, target
   membership, and injectivity.

## Classical Material To Preserve

Ordinary Dyck sequence of length `n`:

````tex
x=(x_0,\ldots,x_{n-1}),\qquad
x_0=0,\quad x_i\ge0,\quad x_{i+1}\le x_i+1.
````

Statistics:

````tex
\area(x)=\sum_i x_i,
````

````tex
\dinv(x)=\#\{(i,j):0\le i<j<n,\ x_i=x_j
  \text{ or } x_i=x_j+1\}.
````

Top degree and deficit:

````tex
M=\binom n2,\qquad
\defc(x)=M-\area(x)-\dinv(x).
````

Skeleton definitions from the 2026 preprint:

- A full Dyck skeleton is a Dyck sequence with no extractable element under the
  leftmost extraction convention.
- For `n >= 4`, the exceptional full skeleton is

````tex
\epsilon_n=(0,0,1,\underbrace{0,\ldots,0}_{n-4\text{ entries}},1).
````

- A special Dyck skeleton is a full Dyck skeleton not equal to `\epsilon_n`.
  For `n < 4`, every full skeleton is special.

The classical `up` map, when defined, changes statistics by:

````tex
\area(\mathrm{up}(x))=\area(x)+1,\qquad
\dinv(\mathrm{up}(x))=\dinv(x)-1.
````

The `down` map is inverse on the stated low-deficit lower-half domains and
changes statistics oppositely.

Classical string decomposition source statement:

For `n >= 4`, `M = binom(n,2)`, and `d <= 2n-8`, put

````tex
\ell=\left\lfloor\frac{M-d}{2}\right\rfloor.
````

The lower half of the deficit-`d` layer is partitioned by strings

````tex
\{S,\mathrm{up}(S),\ldots,\mathrm{up}^{\ell-\area(S)}(S)\},
````

where `S` ranges over special Dyck skeletons of length `n`, deficit `d`, and
area at most `ell`.

Classical formula source statement:

````tex
\left.C_n(q,t)\right|_{\binom n2-2n+8\le \deg_{q,t}\le \binom n2}
=
\sum_{\substack{S\text{ special Dyck skeleton of length }n\\
                \defc(S)\le 2n-8}}
\frac{q^{\dinv(S)+1}t^{\area(S)}
      -q^{\area(S)}t^{\dinv(S)+1}}{q-t}.
````

The current `explanation.tex` uses the equivalent convention

````tex
\frac{q^{\area(S)}t^{\dinv(S)+1}
      -q^{\dinv(S)+1}t^{\area(S)}}{t-q}.
````

Either form is acceptable if internally consistent.  The item currently says
all coefficient polynomials use `q^{area}t^{dinv}`.

The proof in the preprint uses:

- the lower-half string decomposition;
- the known `q,t` symmetry of `C_n(q,t)`;
- symmetry of each interval contribution.

Do not reproduce the local East7/West7 proof machinery unless the user asks.

## Rational `r = tau*s + 1` Material To Preserve

Use `tau` for the step parameter and reserve `t` for the `q,t` variable.
Assume `s >= 1` and `tau > 1`, and set:

````tex
r=\tau s+1.
````

Normalized `tau`-Dyck sequence of length `s`:

````tex
x=(x_1,\ldots,x_s),\qquad
x_1=0,\quad x_i\ge0,\quad x_{i+1}\le x_i+\tau.
````

The code uses zero-based tuples `(x_0,...,x_{s-1})`; the current explanation
uses one-based notation in the rational section.  Pick one convention and use
it consistently.  Zero-based notation matches the code and nearby item
`dyck_skeleton_tableau_formulas`.

Statistics:

````tex
\area(x)=\sum_i x_i,
````

````tex
\dinv_\tau(x)=\sum_{i<j}
\begin{cases}
\max(0,x_i+\tau-x_j), & x_i\le x_j,\\
\max(0,x_j+1+\tau-x_i), & x_i>x_j.
\end{cases}
````

Top degree and deficit:

````tex
M_{s,\tau}=\tau\binom{s}{2},\qquad
\defc_\tau(x)=M_{s,\tau}-\area(x)-\dinv_\tau(x).
````

Rational extractability in the current item-level checker:

An entry `x_j` with value `e > 0` is extractable if exactly one earlier entry
lies in the predecessor interval

````tex
[\max(0,e-\tau),e)
````

and deleting the entry preserves the `tau`-Dyck adjacent condition.  If
`0 < j < s-1`, the splice condition is

````tex
x_{j+1}\le x_{j-1}+\tau.
````

If `j=s-1`, there is no new adjacent pair to check.  The leftmost extractable
entry is used.

Full and special rational skeletons:

- A full rational skeleton is a normalized `tau`-Dyck sequence with no
  extractable entry.
- For `s >= 4`, the excluded full skeleton is

````tex
\epsilon_{s,\tau}=(0,0,1,\underbrace{0,\ldots,0}_{s-4\text{ entries}},\tau).
````

- A special rational skeleton is a full rational skeleton other than
  `\epsilon_{s,\tau}`.  For `s < 4`, every full rational skeleton is special.
- The excluded full skeleton is not discarded from the strings; it is attached
  to the string beginning at `(0,\ldots,0,\tau)` by a special upward move.

Conjectural range:

````tex
B=(s-2)(\tau+1)-4.
````

If `B < 0`, there is no nonnegative deficit layer in the stated range.

Conjectural low-deficit formula from `rational_generalizations.tex`:

````tex
\sum_{\substack{
    S\text{ special rational Dyck skeleton of length }s\\
    \defc_\tau(S)\le B}}
\frac{
  q^{\dinv_\tau(S)+1}t^{\area(S)}
  -
  q^{\area(S)}t^{\dinv_\tau(S)+1}
}{q-t}.
````

Equivalent interval form for a fixed skeleton `S` of deficit `d`:

````tex
\sum_{j=\area(S)}^{M_{s,\tau}-d-\area(S)}
q^j t^{M_{s,\tau}-d-j}.
````

The current `explanation.tex` is more cautious and states a lower-half version:
for `L_d = floor((M-d)/2)`,

````tex
\sum_{\substack{x:\ \defc_\tau(x)=d,\ \area(x)\le L_d}}
q^{\area(x)}t^{\dinv_\tau(x)}
=
\sum_{\substack{z\text{ special skeleton}\\ \defc_\tau(z)=d}}
\sum_{i=\area(z)}^{L_d} q^i t^{M-d-i}.
````

The full formula needs either:

- deficit-layer `q,t` symmetry, or
- a direct full coefficient-dictionary identity.

The checker currently performs the second kind of check by comparing full
coefficient dictionaries, using signed rational-expression bookkeeping.  The
explanation should not imply that the East3/East5 lower-half map alone proves
the full rational formula.

## Code Evidence To Explain

`check_r1mod_skeleton_strings.py`:

- intended for `tau > 1`;
- default bound is `B=(s-2)(tau+1)-4`;
- prints `empty defect range` and exits successfully if `B < 0`;
- enumerates normalized `tau`-Dyck sequences in the retained deficit range;
- compares direct coefficients with formula-side coefficients;
- separately tests the implemented lower-half map.

Important output fields:

````text
formula_status: PASS|FAIL
map_status: PASS|PARTIAL|FAIL
status: PASS|FAIL
generated_words
searched_leaf_words
retained_defect_range_words
unsupported_level_7
````

Interpretation:

- `formula_status: PASS` means the full coefficient dictionaries matched in
  the checked finite case.
- `map_status: PASS` means the current implemented East3/East5 up/down map
  gave lower-half coverage with the checked inverse/statistic properties.
- `map_status: PARTIAL` means no contradiction was found before the map hit an
  unsupported level-7 branch.  It is not a full lower-half decomposition
  certificate.
- The script's command-line option says `--max-defect`; in the exposition,
  call this deficit.
- `generated_words` is the full normalized search-space size; the checker may
  prune the search, so `searched_leaf_words` can be smaller.

`run_official_r1mod_checks.py` configured ranges:

````text
tau=2, 1 <= s <= 14
tau=3, 1 <= s <= 12
tau=4, 1 <= s <= 10
tau=5, 1 <= s <= 9
````

For `s <= 4`, it runs formula-only.  For `s >= 5`, it runs both formula and
map checks.

No compact expected-output file or durable complete run log was found in the
item directory.  The existing HTML page states that recorded checks have the
partial map reaching all conjectural formula defect layers for:

````text
tau=2, 5 <= s <= 14
tau=3, 5 <= s <= 12
tau=4, 5 <= s <= 10
````

and that at `(tau,s)=(2,15)` the formula check passed through `defc <= 35`,
while the partial map hit `14` unsupported level-7 records at defect `35`.
If the rewrite wants to use these exact claims, state them as recorded item
evidence unless a fresh reproducibility run is provided.

## NRCM Material To Preserve Carefully

The NRCM is not the same as the `r=tau*s+1` special-skeleton map.  It is a
separate general-rational diagnostic for coprime positive `r,s`.

Definitions used in the item-level code:

````tex
H_i=\left\lfloor\frac{ri}{s}\right\rfloor,\qquad
L_i\equiv ri\pmod s,\quad 0\le L_i<s.
````

Position-coordinate path:

````tex
Q=(Q_0,\ldots,Q_{s-1}),\qquad
Q_0=0,\quad 0\le Q_i\le H_i.
````

Path heights:

````tex
P_i=H_i-Q_i.
````

The path is valid when:

````tex
P_0\le P_1\le\cdots\le P_{s-1}.
````

The item-level code defines diagnostic deficit by pair summands.  For
`1 <= i < j < s`, put `u = |Q_i-Q_j|`; if `Q_i != Q_j` and the comparisons
`Q_i > Q_j` and `L_i > L_j` have opposite truth values, replace `u` by
`u-1`, then clamp to `max(u,0)`.  Define

````tex
v_{ij}=
\begin{cases}
\Delta_i-(Q_{i+1}-Q_i), & Q_i>Q_j,\\
\Delta_{i-1}-(Q_i-Q_{i-1}), & Q_j>Q_i,\\
0, & Q_i=Q_j,
\end{cases}
````

where `Delta_i = H_{i+1}-H_i`.  The summand is

````tex
\delta_{ij}(Q)=\min(u_{ij},v_{ij}),
````

and

````tex
\defc(Q)=\sum_{1\le i<j<s}\delta_{ij}(Q),\qquad
\dinv(Q)=M-\area(Q)-\defc(Q),\quad M=\sum_iH_i.
````

Do not silently add a clamp to `v_{ij}`; the current item explicitly says this
is not part of the implemented statistic.

Strict NRCM:

For `I_k={k,k+1,...,s-1}`, list the suffix columns in increasing label order.
The candidate `T_k(Q)` moves each suffix value to the next suffix column in
that label order, and wraps the last value to the first suffix column after
adding `1`.  Columns outside the suffix are unchanged.

Starting with `k=1`, strict NRCM chooses the first `k` for which `T_k(Q)`
satisfies capacity.  It defines `NRCM(Q)=T_k(Q)` only if that first
capacity-valid candidate is also path-valid.  Otherwise NRCM is undefined.

Important status:

- By construction, a defined NRCM move raises area by one.
- The Dyck research notes contain an AI-generated and AI-checked proof draft
  that defined strict NRCM preserves deficit.
- The item should not call this a fully human-verified theorem unless the user
  supplies that decision.
- `check_nrcm_lower_half.py` is a finite diagnostic: it checks definedness,
  same deficit, area increase, target membership, and injectivity on checked
  lower-half sources.
- `check_nrcm_domain.py` checks only definedness on lower-half sources.

If including examples, the current explanation has two small ones:

- Slope `5/3`: `H=(0,1,3)`, `L=(0,2,1)`, `Q=(0,1,1)`.  For `k=1`,
  the suffix columns `{1,2}` in label order are `2,1`, and the move gives
  `T_1(Q)=(0,1,2)`, which is capacity-valid and path-valid.
- Slope `4/3`: `H=(0,1,2)`, `L=(0,1,2)`, `Q=(0,0,1)`.  The first
  capacity-valid suffix is `k=2`, giving `T_2(Q)=(0,0,2)`, whose path heights
  are `(0,1,0)`, not nondecreasing.  Strict NRCM is undefined.

## Current Explanation Problems To Fix

The current `explanation.tex` has useful material, but it is too ledger-like
and overlong for a public explanation.  Specific issues:

- It opens with status and computational caveats before giving a compact
  mental model of strings.
- It includes a long NRCM definition and diagnostic proposition; this may
  overwhelm the main skeleton-string story.
- It mixes lower-half string interpretation with full signed rational
  expression checks.  The rewrite should explicitly separate these.
- It uses both classical and rational skeleton definitions; the rewrite should
  introduce them in parallel only where that helps.
- It says the batch grid records intended finite tests, not independent fresh
  evidence.  That caution should be preserved unless a durable run log is
  added.
- It should avoid implying that the current East3/East5 partial map proves the
  conjectural rational formula.
- It should avoid implying that NRCM deficit preservation is a public theorem
  in the curated item.

## Suggested Main Statements

Use theorem/conjecture environments sparingly.

Possible theorem statement:

````tex
\begin{theorem}[Hawkes, low-deficit skeleton strings]
For \(n\ge4\) and \(d\le2n-8\), the lower half of the
deficit-\(d\) layer of ordinary Dyck sequences of length \(n\) is partitioned
by strings beginning at special Dyck skeletons.
\end{theorem}
````

Then either include the formula immediately after, or make it a corollary:

````tex
\left.C_n(q,t)\right|_{\binom n2-2n+8\le \deg_{q,t}\le \binom n2}
=
\sum_{\substack{S\text{ special Dyck skeleton}\\ \defc(S)\le 2n-8}}
\frac{q^{\dinv(S)+1}t^{\area(S)}
      -q^{\area(S)}t^{\dinv(S)+1}}{q-t}.
````

Possible conjecture statement:

````tex
\begin{conjecture}[Rational special-skeleton formula for \(r=\tau s+1\)]
Let \(\tau>1\), \(s\ge1\), and \(B=(s-2)(\tau+1)-4\).
In the normalized \(\tau\)-Dyck model, the low-deficit part
\(\defc_\tau\le B\) is given by the same interval formula, with special
rational skeletons replacing special Dyck skeletons.
\end{conjecture}
````

Then explain the lower-half version before the full interval version, because
the string interpretation is naturally lower-half.  Say that the full interval
formula is supported in the finite checker by direct coefficient-dictionary
comparison.

## What To Omit Or Relegate

Avoid including:

- detailed East3/East5/East7 case tables;
- current `SSD-R1-002` East7 tie-breaker research;
- superseded failures from exploratory logs, except as an internal caution;
- the full NRCM proof architecture;
- workflow/agent/provenance commentary inside `explanation.tex`;
- claims that require hidden source notes to understand.

The explanation may point to code files by name, but should not cite internal
workspace paths as mathematical authority.  Use the 2026 preprint as the
authority for the classical theorem.

## Verification After Writing

After the writing agent edits `explanation.tex`, run a LaTeX compile from:

````text
Combinatorics/items/dyck_skeleton_string_decompositions
````

Recommended command:

````text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
````

If the rewrite changes computational claims, either:

- include only claims already recorded in item files, with cautious wording; or
- run the relevant finite command and record the output before strengthening
  the claim.
```

### `items/dyck_skeleton_tableau_formulas/assets/.gitkeep`

```text

```

### `items/dyck_skeleton_tableau_formulas/code/check_rational_two_column_formula.py`

```python
"""Finite checks for the rational two-column skeleton/tableau formula.

Inputs are rational step values ``t`` and length values ``n``.  For each
requested pair with ``t != 1``, the checker compares:

* direct normalized rational Dyck paths of length ``n``;
* the Type 4 skeleton/tableau formula side, summed over rational
  ``m``-skeletons and at-most-two-column rational Dyck tableaux.

Both sides are grouped by ``(area, dinv)`` before comparison.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from math import comb
from typing import Iterable, Sequence


Word = tuple[int, ...]
Shape = tuple[int, ...]
Tableau = tuple[tuple[int, ...], ...]
PairTable = list[list[int]]


@dataclass(frozen=True, slots=True)
class SequenceData:
    sequence: Word
    area: int
    dinv: int
    endpoint: int
    max_value: int
    is_skeleton: bool


@dataclass(frozen=True, slots=True)
class TableauData:
    row_word: Word
    area: int
    dinv: int


@dataclass(frozen=True, slots=True)
class AggregatedTableauData:
    counts: Word
    area: int
    dinv: int
    multiplicity: int


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def pair_dinv_python(left: int, right: int, step: int) -> int:
    if left <= right:
        contribution = left + step - right
    else:
        contribution = right + 1 + step - left
    if contribution > 0:
        return contribution
    return 0


def rational_dinv_python(sequence: Word, step: int) -> int:
    total = 0
    for left_index in range(len(sequence)):
        left = sequence[left_index]
        for right in sequence[left_index + 1 :]:
            if left <= right:
                contribution = left + step - right
            else:
                contribution = right + 1 + step - left
            if contribution > 0:
                total += contribution
    return total


def has_nonfinal_rational_extractable_python(sequence: Word, step: int) -> bool:
    for index, value in enumerate(sequence[:-1]):
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = 0
        for prior in sequence[:index]:
            if lower <= prior <= value - 1:
                prior_window_count += 1
                if prior_window_count > 1:
                    break
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(sequence) and sequence[index + 1] > sequence[index - 1] + step:
            continue
        return True
    return False


def value_counts(values: Word) -> Word:
    if not values:
        return ()
    counts = [0] * (max(values) + 1)
    for value in values:
        counts[value] += 1
    return tuple(counts)


def build_pair_dinv_table(max_value: int, *, step: int) -> PairTable:
    return [
        [pair_dinv_python(left, right, step) for right in range(max_value + 1)]
        for left in range(max_value + 1)
    ]


def dinv_increment_from_table(prefix: Sequence[int], value: int, pair_table: PairTable) -> int:
    total = 0
    for left in prefix:
        total += pair_table[left][value]
    return total


def cross_dinv_counts_from_table(left_counts: Word, right_counts: Word, pair_table: PairTable) -> int:
    total = 0
    for left, left_multiplicity in enumerate(left_counts):
        if left_multiplicity == 0:
            continue
        row = pair_table[left]
        for right, right_multiplicity in enumerate(right_counts):
            if right_multiplicity:
                total += left_multiplicity * right_multiplicity * row[right]
    return total


def parse_int_list(text: str) -> list[int]:
    values: list[int] = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        values.append(int(part))
    require(values, "expected a comma-separated list of integers")
    return values


def rational_dinv(sequence: Sequence[int], *, step: int) -> int:
    return rational_dinv_python(tuple(sequence), step)


def is_rational_affine_dyck(sequence: Sequence[int], *, step: int) -> bool:
    return all(sequence[index + 1] <= sequence[index] + step for index in range(len(sequence) - 1))


def is_rational_dual_dyck(sequence: Sequence[int], *, step: int) -> bool:
    return all(sequence[index + 1] > sequence[index] + step for index in range(len(sequence) - 1))


def generate_rational_dyck_sequences(length: int, *, step: int) -> Iterable[Word]:
    require(length > 0, "length must be positive")
    require(step >= 0, "t must be non-negative")

    def rec(prefix: list[int]) -> Iterable[Word]:
        if len(prefix) == length:
            yield tuple(prefix)
            return
        previous = prefix[-1]
        for value in range(previous + step + 1):
            prefix.append(value)
            yield from rec(prefix)
            prefix.pop()

    yield from rec([0])


def is_normalized_rational_dyck_sequence(sequence: Sequence[int], *, step: int) -> bool:
    values = tuple(sequence)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and is_rational_affine_dyck(values, step=step)
    )


def find_rational_extractable_position(
    sequence: Sequence[int],
    *,
    step: int,
    include_final: bool,
) -> int | None:
    values = tuple(sequence)
    require(is_normalized_rational_dyck_sequence(values, step=step), "sequence must be normalized rational Dyck")
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = sum(1 for prior in values[:index] if lower <= prior <= value - 1)
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + step:
            continue
        return index
    return None


def is_rational_m_skeleton(sequence: Sequence[int], *, step: int, ambient: int | None = None) -> bool:
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    endpoint = values[-1] if ambient is None else ambient
    return (
        endpoint >= 0
        and max(values) == endpoint
        and values[-1] == endpoint
        and find_rational_extractable_position(values, step=step, include_final=False) is None
    )


def pair_dinv(left: int, right: int, *, step: int) -> int:
    return pair_dinv_python(left, right, step)


def has_nonfinal_rational_extractable(sequence: Word, *, step: int) -> bool:
    """Fast extractable test for already-generated normalized Dyck sequences."""

    return has_nonfinal_rational_extractable_python(sequence, step)


def is_rational_m_skeleton_generated(sequence: Word, *, step: int, max_value: int | None = None) -> bool:
    """Check skeleton status for a sequence known to be normalized rational Dyck."""

    endpoint = sequence[-1]
    if max_value is None:
        max_value = max(sequence)
    if max_value != endpoint:
        return False
    return not has_nonfinal_rational_extractable_python(sequence, step)


def generate_rational_dyck_sequence_data(
    length: int,
    *,
    step: int,
    pair_table: PairTable | None = None,
) -> list[SequenceData]:
    """Generate normalized rational Dyck paths with area/dinv cached."""

    require(length > 0, "length must be positive")
    require(step >= 0, "t must be non-negative")
    return sequence_data_by_length(length, step=step, pair_table=pair_table)[length]


def sequence_data_by_length(
    max_length: int,
    *,
    step: int,
    pair_table: PairTable | None = None,
) -> dict[int, list[SequenceData]]:
    require(max_length > 0, "max length must be positive")
    require(step >= 0, "t must be non-negative")
    if pair_table is None:
        pair_table = build_pair_dinv_table(step * (max_length - 1), step=step)

    base = SequenceData((0,), 0, 0, 0, 0, True)
    by_length: dict[int, list[SequenceData]] = {1: [base]}
    previous_level = [base]
    for length in range(2, max_length + 1):
        current_level: list[SequenceData] = []
        append_current = current_level.append
        for data in previous_level:
            prefix = data.sequence
            for value in range(data.endpoint + step + 1):
                dinv_increment_value = dinv_increment_from_table(prefix, value, pair_table)
                sequence = prefix + (value,)
                max_value = data.max_value if data.max_value >= value else value
                is_skeleton = (
                    max_value == value
                    and not has_nonfinal_rational_extractable_python(sequence, step)
                )
                append_current(
                    SequenceData(
                        sequence,
                        data.area + value,
                        data.dinv + dinv_increment_value,
                        value,
                        max_value,
                        is_skeleton,
                    )
                )
        by_length[length] = current_level
        previous_level = current_level
    return by_length


def generate_direct_coefficients_and_skeletons(
    max_length: int,
    *,
    step: int,
    pair_table: PairTable,
    requested_lengths: set[int],
) -> tuple[dict[int, Counter[tuple[int, int]]], dict[int, list[SequenceData]]]:
    require(max_length > 0, "max length must be positive")
    direct_by_length = {length: Counter() for length in requested_lengths}
    skeletons_by_length: dict[int, list[SequenceData]] = defaultdict(list)
    prefix = [0]

    def rec(area: int, dinv: int, max_value: int) -> None:
        length = len(prefix)
        endpoint = prefix[-1]
        if length in direct_by_length:
            direct_by_length[length][(area, dinv)] += 1

        if max_value == endpoint:
            sequence = tuple(prefix)
            if not has_nonfinal_rational_extractable_python(sequence, step):
                skeletons_by_length[length].append(
                    SequenceData(sequence, area, dinv, endpoint, max_value, True)
                )

        if length == max_length:
            return

        for value in range(endpoint + step + 1):
            dinv_increment_value = dinv_increment_from_table(prefix, value, pair_table)
            prefix.append(value)
            rec(area + value, dinv + dinv_increment_value, max_value if max_value >= value else value)
            prefix.pop()

    rec(0, 0, 0)
    return direct_by_length, skeletons_by_length


def is_partition_shape(shape: Sequence[int]) -> bool:
    return all(part > 0 for part in shape) and all(shape[index] >= shape[index + 1] for index in range(len(shape) - 1))


def conjugate_partition(shape: Shape) -> Shape:
    if shape == ():
        return ()
    require(is_partition_shape(shape), "shape must be a partition")
    return tuple(sum(1 for part in shape if part >= column) for column in range(1, shape[0] + 1))


def at_most_two_column_shapes(total_size: int) -> list[Shape]:
    require(total_size >= 0, "tableau size must be non-negative")
    if total_size == 0:
        return [()]
    out: list[Shape] = []
    for two_cell_rows in range(total_size // 2, -1, -1):
        one_cell_rows = total_size - 2 * two_cell_rows
        out.append((2,) * two_cell_rows + (1,) * one_cell_rows)
    return out


def rational_row_reading_word(tableau: Sequence[Sequence[int]]) -> Word:
    return tuple(value for row in reversed(tableau) for value in row)


def enumerate_bounded_rational_dyck_tableaux(
    shape: Shape,
    *,
    step: int,
    max_entry: int,
) -> Iterable[Tableau]:
    if shape == ():
        yield ()
        return
    if max_entry < 0:
        return
    require(is_partition_shape(shape), "shape must be a partition")

    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape) and col < shape[row + 1] and value > rows[row + 1][col] + step:
            return False
        if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int) -> Iterable[Tableau]:
        if cell_index == len(cells):
            yield tuple(tuple(row) for row in rows)
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            rows[row][col] = value
            yield from rec(cell_index + 1)
            rows[row][col] = 0

    yield from rec(0)


def enumerate_bounded_rational_dyck_tableau_data(
    shape: Shape,
    *,
    step: int,
    max_entry: int,
    pair_table: PairTable,
) -> Iterable[TableauData]:
    """Enumerate bounded rational Dyck tableaux with cached row-word statistics."""

    if shape == ():
        yield TableauData(row_word=(), area=0, dinv=0)
        return
    if max_entry < 0:
        return
    require(is_partition_shape(shape), "shape must be a partition")

    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
    row_word: list[int] = []

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape) and col < shape[row + 1] and value > rows[row + 1][col] + step:
            return False
        if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int, area: int, dinv: int) -> Iterable[TableauData]:
        if cell_index == len(cells):
            yield TableauData(row_word=tuple(row_word), area=area, dinv=dinv)
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            dinv_increment = dinv_increment_from_table(row_word, value, pair_table)
            rows[row][col] = value
            row_word.append(value)
            yield from rec(cell_index + 1, area + value, dinv + dinv_increment)
            row_word.pop()
            rows[row][col] = 0

    yield from rec(0, 0, 0)


def aggregate_tableau_data(tableaux: Iterable[TableauData]) -> list[AggregatedTableauData]:
    grouped: Counter[tuple[Word, int, int]] = Counter()
    for tableau in tableaux:
        grouped[(value_counts(tableau.row_word), tableau.area, tableau.dinv)] += 1
    return [
        AggregatedTableauData(counts=counts, area=area, dinv=dinv, multiplicity=multiplicity)
        for (counts, area, dinv), multiplicity in grouped.items()
    ]


def enumerate_ssyt_weights(shape: Shape, *, alphabet_size: int) -> Counter[tuple[int, ...]]:
    """Return the Schur monomial expansion by SSYT enumeration."""

    require(alphabet_size > 0, "alphabet size must be positive")
    if shape == ():
        return Counter({(0,) * alphabet_size: 1})
    require(is_partition_shape(shape), "shape must be a partition")
    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row, length in enumerate(shape) for col in range(length)]
    weights: Counter[tuple[int, ...]] = Counter()

    def rec(cell_index: int, counts: list[int]) -> None:
        if cell_index == len(cells):
            weights[tuple(counts)] += 1
            return
        row, col = cells[cell_index]
        lower = 1
        if col > 0:
            lower = max(lower, rows[row][col - 1])
        if row > 0 and col < shape[row - 1]:
            lower = max(lower, rows[row - 1][col] + 1)
        for value in range(lower, alphabet_size + 1):
            rows[row][col] = value
            counts[value - 1] += 1
            rec(cell_index + 1, counts)
            counts[value - 1] -= 1
            rows[row][col] = 0

    rec(0, [0] * alphabet_size)
    return weights


def direct_coefficients(sequence_data: list[SequenceData]) -> Counter[tuple[int, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    for data in sequence_data:
        coeffs[(data.area, data.dinv)] += 1
    return coeffs


def type4_formula_coefficients(
    length: int,
    *,
    step: int,
    skeletons_by_length: dict[int, list[SequenceData]],
    pair_table: PairTable,
) -> tuple[Counter[tuple[int, int]], dict[str, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    counts = {
        "skeletons": 0,
        "tableaux": 0,
        "skeleton_tableau_pairs": 0,
        "schur_monomial_terms": 0,
    }
    schur_cache: dict[Shape, Counter[tuple[int, int]]] = {}
    tableau_cache: dict[tuple[Shape, int], list[AggregatedTableauData]] = {}

    for skeleton_length in range(1, length + 1):
        tableau_size = length - skeleton_length
        skeletons = skeletons_by_length.get(skeleton_length, [])
        counts["skeletons"] += len(skeletons)
        if not skeletons:
            continue
        skeletons_by_endpoint: dict[int, list[SequenceData]] = defaultdict(list)
        for skeleton_data in skeletons:
            skeletons_by_endpoint[skeleton_data.endpoint].append(skeleton_data)
        skeleton_counts: dict[Word, Word] = {
            skeleton_data.sequence: value_counts(skeleton_data.sequence)
            for skeleton_data in skeletons
        }

        for shape in at_most_two_column_shapes(tableau_size):
            size = sum(shape)
            schur_shape = conjugate_partition(shape)
            if schur_shape not in schur_cache:
                schur_cache[schur_shape] = enumerate_ssyt_weights(schur_shape, alphabet_size=2)
            schur_terms = list(schur_cache[schur_shape].items())

            for ambient, skeleton_group in skeletons_by_endpoint.items():
                cache_key = (shape, ambient)
                if cache_key not in tableau_cache:
                    tableau_cache[cache_key] = aggregate_tableau_data(
                        enumerate_bounded_rational_dyck_tableau_data(
                            shape=shape,
                            step=step,
                            max_entry=ambient - 1,
                            pair_table=pair_table,
                        ),
                    )
                tableaux = tableau_cache[cache_key]
                tableau_multiplicity_total = sum(tableau.multiplicity for tableau in tableaux)
                counts["tableaux"] += tableau_multiplicity_total * len(skeleton_group)
                counts["skeleton_tableau_pairs"] += tableau_multiplicity_total * len(skeleton_group)

                for skeleton_data in skeleton_group:
                    skeleton_count_vector = skeleton_counts[skeleton_data.sequence]
                    for tableau_data in tableaux:
                        if tableau_data.counts:
                            cross_dinv_value = cross_dinv_counts_from_table(
                                skeleton_count_vector,
                                tableau_data.counts,
                                pair_table,
                            )
                        else:
                            cross_dinv_value = 0
                        base_area = skeleton_data.area + tableau_data.area
                        base_dinv = skeleton_data.dinv + tableau_data.dinv + cross_dinv_value
                        for (q_power, t_power), multiplicity in schur_terms:
                            contribution = multiplicity * tableau_data.multiplicity
                            coeffs[(base_area + q_power, base_dinv - size + t_power)] += contribution
                            counts["schur_monomial_terms"] += contribution
    return coeffs, counts


def compare_case(
    *,
    step: int,
    length: int,
    direct: Counter[tuple[int, int]],
    skeletons_by_length: dict[int, list[SequenceData]],
    pair_table: PairTable,
) -> dict[str, int | float]:
    case_start = time.perf_counter()
    formula, formula_counts = type4_formula_coefficients(
        length,
        step=step,
        skeletons_by_length=skeletons_by_length,
        pair_table=pair_table,
    )
    mismatches = [
        (key, direct[key], formula[key])
        for key in sorted(set(direct) | set(formula))
        if direct[key] != formula[key]
    ]
    require(not mismatches, f"coefficient mismatch for t={step}, n={length}: {mismatches[:10]}")
    elapsed = time.perf_counter() - case_start
    return {
        "direct_paths": sum(direct.values()),
        "direct_terms": len(direct),
        "formula_terms": len(formula),
        "coefficient_keys": len(set(direct) | set(formula)),
        "skeletons": formula_counts["skeletons"],
        "tableaux": formula_counts["tableaux"],
        "skeleton_tableau_pairs": formula_counts["skeleton_tableau_pairs"],
        "schur_monomial_terms": formula_counts["schur_monomial_terms"],
        "elapsed_seconds": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t-values", required=True, help="Comma-separated rational step values t.")
    parser.add_argument("--n-values", required=True, help="Comma-separated length values n, i.e. rational s-values.")
    args = parser.parse_args()

    steps = parse_int_list(args.t_values)
    lengths = parse_int_list(args.n_values)
    start = time.perf_counter()
    compared: dict[tuple[int, int], dict[str, int | float]] = {}
    skipped: list[tuple[int, int]] = []

    require(all(step >= 0 for step in steps), "all t-values must be non-negative")
    require(all(length > 0 for length in lengths), "all n-values must be positive")
    require(at_most_two_column_shapes(5) == [(2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)], "shape smoke check failed")
    require(is_rational_m_skeleton((0, 2), step=2, ambient=2), "skeleton smoke check failed")
    require(rational_dinv((0, 1, 0), step=2) == 5, "dinv smoke check failed")
    require(comb(3, 2) == 3, "math smoke check failed")

    for step in steps:
        if step == 1:
            for length in lengths:
                skipped.append((step, length))
            continue
        pair_table = build_pair_dinv_table(step * (max(lengths) - 1), step=step)
        direct_by_length, skeletons_by_length = generate_direct_coefficients_and_skeletons(
            max(lengths),
            step=step,
            pair_table=pair_table,
            requested_lengths=set(lengths),
        )
        for length in lengths:
            case_result = compare_case(
                step=step,
                length=length,
                direct=direct_by_length[length],
                skeletons_by_length=skeletons_by_length,
                pair_table=pair_table,
            )
            compared[(step, length)] = case_result
            print(
                f"  t={step}, n={length}: paths={case_result['direct_paths']}, "
                f"keys={case_result['coefficient_keys']}, skeletons={case_result['skeletons']}, "
                f"tableaux={case_result['tableaux']}, elapsed={case_result['elapsed_seconds']:.3f}s",
                flush=True,
            )

    require(compared, "no non-t=1 cases were checked")
    print("rational two-column skeleton/tableau formula check")
    print("  convention: r = n*t + 1; n is the rational s-value / path length")
    print(f"  compared cases: {sorted(compared)}")
    print(f"  skipped t=1 cases: {skipped}")
    print(f"  counts: {compared}")
    print(f"  elapsed: {time.perf_counter() - start:.3f}s")
    print("  all requested finite checks passed")


if __name__ == "__main__":
    main()
```

### `items/dyck_skeleton_tableau_formulas/code/README.md`

```markdown
# Code

Executable checks for the Dyck skeleton tableau formula item.

## Rational Two-Column Formula

Command:

````text
python check_rational_two_column_formula.py --t-values 2,3,4 --n-values 1,2,3,4
````

Official checks:

````text
python check_rational_two_column_formula.py --t-values 2 --n-values 1,2,3,4,5,6,7,8,9,10,11,12,13,14
python check_rational_two_column_formula.py --t-values 3 --n-values 1,2,3,4,5,6,7,8,9,10,11,12
python check_rational_two_column_formula.py --t-values 4 --n-values 1,2,3,4,5,6,7,8,9,10
````

Inputs:

- `--t-values`: comma-separated rational step values.
- `--n-values`: comma-separated length values, i.e. the rational `s` values in
  `r = n*t + 1`.

The checker skips `t=1`, since that is the proved classical case.  For every
other requested `(t,n)` pair it computes two coefficient dictionaries grouped
by `(area, dinv)`:

- the direct side, generated from all normalized rational Dyck paths of length
  `n`;
- the formula side, generated from pairs `(F,P)` where `F` is a rational
  Dyck `m`-skeleton and `P` is an at-most-two-column rational Dyck tableau
  with entries in `[0,m-1]`, expanded by the corresponding two-variable Schur
  factor.

The check passes exactly when the two grouped coefficient dictionaries agree
for every requested case.
```

### `items/dyck_skeleton_tableau_formulas/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\DeclareMathOperator{\area}{area}
\DeclareMathOperator{\dinv}{dinv}

\title{Dyck Skeleton Tableau Formulas}
\author{}
\date{}

\begin{document}
\maketitle

\section{What the formula says}

The purpose of this item is to compare two ways of forming the same
two-variable generating function.  The direct side sums
\(q^{\area}t^{\dinv}\) over normalized rational Dyck sequences.  The
skeleton/tableau side groups the same expected polynomial by rational
skeletons, at-most-two-column rational Dyck tableaux, and a two-variable
Schur factor.

The checker uses the option name \(t\) for the rational step and \(n\) for the
length.  In this explanation, the rational step is written \(\tau\) and the
length is written \(s\), so the congruence family is
\[
  r=s\tau+1.
\]
Thus the checker's case \(t=1\) is the case \(\tau=1\).  From this point on,
\(\tau\) denotes the rational step, while \(t\) remains the second variable in
\(q,t\).

\subsection{Rational Dyck side}

Fix \(s\geq 1\) and \(\tau\geq 0\).  A normalized rational Dyck sequence of
length \(s\) and step \(\tau\) is a sequence
\[
  D=(D_0,\ldots,D_{s-1})
\]
of nonnegative integers such that \(D_0=0\) and
\[
  D_{i+1}\leq D_i+\tau
  \qquad(0\leq i<s-1).
\]
For a finite integer sequence \(x=(x_0,\ldots,x_{\ell-1})\), define
\[
  \dinv_\tau(x)=
  \sum_{0\leq i<j<\ell} d_\tau(x_i,x_j),
\]
where
\[
  d_\tau(a,b)=
  \begin{cases}
    \max(0,a+\tau-b),& a\leq b,\\
    \max(0,b+1+\tau-a),& a>b.
  \end{cases}
\]
The area statistic is
\[
  \area(x)=\sum_i x_i.
\]
The direct rational \(q,t\)-Catalan side in this model is therefore
\[
  C_{s,\tau}(q,t)
  =
  \sum_D q^{\area(D)}t^{\dinv_\tau(D)},
\]
where \(D\) ranges over all normalized rational Dyck sequences of length
\(s\).

\subsection{Skeleton--tableau side}

The formula decomposes the same polynomial by first choosing a rational
skeleton and then filling the remaining cells by a two-column rational Dyck
tableau.

An entry \(D_j=e\) of a normalized rational Dyck sequence is called
extractable if \(e>0\), exactly one earlier entry lies in the predecessor
window
\[
  \{a\in\mathbb Z_{\geq 0}: \max(0,e-\tau)\leq a\leq e-1\},
\]
and deleting \(D_j\) preserves the adjacent rational Dyck inequality.  More
explicitly, if \(0<j<s-1\), then deletion requires
\[
  D_{j+1}\leq D_{j-1}+\tau.
\]
If \(j=s-1\), there is no new adjacent pair to check.  For \(\tau=0\), the
predecessor window is empty.  A rational \(m\)-skeleton is a normalized
rational Dyck sequence \(F\) with final entry equal to its maximum,
\[
  F_{|F|-1}=\max(F)=m,
\]
and with no nonfinal extractable entry.  A final extractable entry is allowed
in an \(m\)-skeleton.

A rational Dyck tableau \(P\) of step \(\tau\) is a left-aligned tableau whose
row lengths form a partition.  We index its rows in the source-paper
convention: \(P_0\) is the top row, \(P_1\) is the row immediately below it,
and so on.  Rows are read left to right and are dual rational Dyck sequences,
\[
  P_i[j+1]>P_i[j]+\tau,
\]
while columns, read bottom to top, satisfy the affine rational Dyck condition.
Equivalently, if row \(i\) is immediately above row \(i+1\), then
\[
  P_i[j]\leq P_{i+1}[j]+\tau
\]
whenever both entries exist.  Its row-reading word is
\[
  \operatorname{RR}(P)=P_{\text{bottom}}P_{\text{next}}\cdots P_{\text{top}},
\]
with each row read left to right, and \(\lambda(P)\) denotes its shape.

The checked conjectural rational two-column skeleton/tableau identity is
\[
  C_{s,\tau}(q,t)
  =
  \sum_{(F,P)}
  q^{\area(F:\operatorname{RR}(P))}
  t^{\dinv_\tau(F:\operatorname{RR}(P))-|P|}
  s_{\lambda(P)'}(q,t).
\]
The sum is over all pairs \((F,P)\) such that \(F\) is a rational
\(m\)-skeleton of step \(\tau\) for some \(m\geq 0\), \(P\) is an
at-most-two-column rational Dyck tableau of step \(\tau\) with entries in
\([0,m-1]\), and
\[
  |F|+|\operatorname{RR}(P)|=s.
\]
Here \(F:\operatorname{RR}(P)\) means concatenation, \(|P|\) is the number of
cells of \(P\), \(\lambda(P)'\) is the conjugate partition, and
\(s_{\lambda(P)'}(q,t)\) is the Schur function in the two variables \(q,t\).
This is the checked conjectural identity for general rational step
\(\tau\).

\section{Source context and status}

Status summary: the identity is proved for \(\tau=1\), degenerate for
\(\tau=0\), and computationally verified but not proved for the tested
values \(\tau>1\).

For \(\tau=1\), the formula is exactly the two-column tableau formula for the
ordinary \(q,t\)-Catalan polynomial proved in the source paper.  In that
proof, Dyck sequences are sent by the paper's Type 1 through Type 4
correspondences to Type 4 triples \((F,P,Q)\), where \(F\) is a Dyck
\(m\)-skeleton, \(P\) is an at-most-two-column Dyck tableau, and \(Q\) is a
binary reverse semistandard tableau of shape \(\lambda(P)\).

The \(-|P|\) shift in the displayed formula comes from summing over the
binary recording tableau \(Q\).  For fixed \((F,P)\), one has
\[
  q^{\#1(Q)}t^{-\#1(Q)}
  =
  t^{-|P|}q^{\#1(Q)}t^{\#0(Q)},
\]
since \(\#0(Q)+\#1(Q)=|P|\).  Transposing \(Q\) turns the binary reverse
semistandard condition on shape \(\lambda(P)\) into the ordinary
semistandard condition on the conjugate shape \(\lambda(P)'\), giving
\[
  \sum_Q q^{\#1(Q)}t^{\#0(Q)}
  =
  s_{\lambda(P)'}(t,q)
  =
  s_{\lambda(P)'}(q,t).
\]

The case \(\tau=0\) is degenerate.  The adjacent condition becomes
\(D_{i+1}\leq D_i\), so a normalized nonnegative sequence starts at \(0\) and
can only stay at \(0\).  Thus the direct side has only the all-zero sequence
in each length.  On the formula side, a contributing skeleton must have
\(m=0\), and a nonempty tableau would need entries in \([0,m-1]=[0,-1]\),
which is impossible.  Therefore only \(F=(0,\ldots,0)\) with \(P=\varnothing\)
contributes.

For \(\tau>1\), this item records finite evidence for the conjectural
rational analogue tested here.  The checker does not prove the formula in
these cases; it enumerates both sides and compares the resulting coefficient
dictionaries grouped by \((\area,\dinv)\).

\section{Computational verification}

The checker for the rational two-column skeleton/tableau formula is recorded
in
\[
\texttt{code/check\_rational\_two\_column\_formula.py}.
\]
It compares two coefficient dictionaries: one from the direct normalized
rational Dyck sequence generating function, and one from the formula-side
expansion described above.  The check passes exactly when the two
dictionaries agree for every \((\operatorname{area},\operatorname{dinv})\)
key in the requested finite range.

The official finite checks performed for this item are:
\begin{itemize}
\item \(\tau=2\), lengths \(1 \leq s \leq 14\), elapsed time
      \(4102.814\) seconds;
\item \(\tau=3\), lengths \(1 \leq s \leq 12\), elapsed time
      \(25254.334\) seconds;
\item \(\tau=4\), lengths \(1 \leq s \leq 10\), elapsed time
      \(494.131\) seconds.
\end{itemize}
All three official checks passed.  These finite checks do not prove the
identity for all lengths for any \(\tau>1\).

\end{document}
```

### `items/dyck_skeleton_tableau_formulas/html/body.html`

```html
<p>This educational section will explain the Dyck skeleton formula and its relation to low-deficit qt-Catalan coefficients.</p>
```

### `items/dyck_skeleton_tableau_formulas/item.yaml`

```yaml
title: Dyck Skeleton Tableau Formulas
slug: dyck_skeleton_tableau_formulas
status_summary: Classical tableau formulas are proved in the 2026 preprint; r == 1 mod s analogues need review.
source_paths:
  - ../Dyck/paper/working_drafts/arxiv_submission.tex
  - ../Dyck/code/codex_project/red_team_theorem_5_30_formula.py
downloads:
  - explanation.tex
```

### `items/dyck_skeleton_tableau_formulas/README.md`

```markdown
# Dyck Skeleton Tableau Formulas

Status summary: Classical tableau formulas are proved in the 2026 preprint; `r == 1 mod s` analogues have supporting finite computational checks.

## Summary

This item records the classical Dyck skeleton formula and the corresponding
`r == 1 mod s` conjectural analogue.

## Provenance

Source repository: `Dyck`

Source paths:

- `../Dyck/paper/working_drafts/arxiv_submission.tex`
- `../Dyck/code/codex_project/red_team_theorem_5_30_formula.py`

Transfer type: explanatory writeup with adapted verification code as needed.

## Layers

Python layer: checker present in `code/check_rational_two_column_formula.py`.

LaTeX layer: explanation present.

HTML layer: planned.

## Status

- Classical formula: theorem in the 2026 preprint.
- `r == 1 mod s` analogue: conjectural identity with official finite checks recorded in the explanation.

## Review Needs

- Review the explanation against the final source-paper theorem numbering.
- Add an HTML rendering if this item is published as a web page.
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/assets/.gitkeep`

```text

```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/01_core_dyck_sequence_routines.py`

```python
from itertools import combinations
from math import comb

def is_Dyck(S):
    S = tuple(S)
    return (
        len(S) > 0
        and S[0] == 0
        and all(isinstance(x, int) and x >= 0 for x in S)
        and all(S[i + 1] <= S[i] + 1 for i in range(len(S) - 1))
    )

def generate_Dycks(n):
    out = []
    def rec(S):
        if len(S) == n:
            out.append(tuple(S))
            return
        for x in range(S[-1] + 2):
            rec(S + [x])
    rec([0])
    return out

def area(S):
    return sum(S)

def dinv(S):
    S = tuple(S)
    return sum(
        1
        for i in range(len(S))
        for j in range(i + 1, len(S))
        if S[i] == S[j] or S[i] == S[j] + 1
    )

def defc(S):
    return comb(len(S), 2) - area(S) - dinv(S)

def find_extractable(S):
    S = tuple(S)
    for j, x in enumerate(S):
        if x == 0:
            continue
        if sum(1 for i in range(j) if S[i] == x - 1) != 1:
            continue
        if j + 1 < len(S) and S[j + 1] > x:
            continue
        return j, x
    return None

def remove_at(S, j):
    S = tuple(S)
    return S[:j] + S[j + 1:]

def is_full_skeleton(S):
    return is_Dyck(S) and find_extractable(S) is None

def epsilon(n):
    return () if n < 4 else tuple([0, 0, 1] + [0] * (n - 4) + [1])

def omega(n):
    return tuple([0] * (n - 1) + [1])

def is_special_skeleton(S):
    S = tuple(S)
    return is_full_skeleton(S) and S != epsilon(len(S))

def inject(S, e):
    S = tuple(S)
    for i, x in enumerate(S):
        if x == e - 1:
            ans = S[:i + 1] + (e,) + S[i + 1:]
            assert is_Dyck(ans)
            return ans
    raise ValueError(f"cannot inject {e} into {S}")

def inject_right_to_left(base, entries):
    out = tuple(base)
    for e in reversed(tuple(entries)):
        out = inject(out, e)
    return out
# Local affine/reverse helpers.

def bk2(a, b):
    return (b, a) if a > b + 1 else (a, b)

def fw2(a, b):
    return (b, a) if b > a + 1 else (a, b)

def bk3(a, b, c):
    if a > b + 1:
        a, b = b, a
    if b > c + 1:
        b, c = c, b
    if a > b + 1:
        a, b = b, a
    return a, b, c
# Local East and West maps.

def East3(W):
    W = tuple(W)
    assert len(W) == 3
    return W if W[1] <= W[2] + 1 else None

def East5(W):
    W = tuple(W)
    assert len(W) == 5
    x_m2, x_m1, x_0, x_1, x_2 = W
    y_m1, y_0 = bk2(x_m1, x_0)
    if x_m1 > x_1 + 1 and y_0 <= x_2 + 1:
        return (x_m2, x_1, y_m1, y_0, x_2)
    if x_m1 <= x_1 + 1 and x_m1 <= x_2 + 1:
        return (x_m2, x_1, x_0, x_m1, x_2)
    return None
_CASE4A = {
    (3, 3, 4, 1, 2): (1, 2, 4, 3, 3),
    (3, 4, 4, 1, 2): (1, 2, 4, 3, 4),
    (4, 3, 4, 1, 2): (1, 2, 4, 4, 3),
    (2, 3, 4, 1, 2): (1, 2, 4, 3, 2),
}
_CASE4B = {
    (3, 3, 4, 2, 1): (2, 1, 4, 3, 3),
    (3, 4, 4, 2, 1): (2, 1, 4, 3, 4),
    (4, 3, 4, 2, 1): (2, 1, 4, 4, 3),
    (2, 3, 4, 2, 1): (2, 1, 4, 3, 2),
}
_CASE4C = {
    (3, 4, 4, 2, 2): (2, 2, 4, 4, 3),
    (3, 4, 5, 2, 2): (2, 2, 5, 4, 3),
}
_CASE4D = {
    (3, 3, 4): lambda o: (2, o, 4, 3, 3),
    (3, 4, 4): lambda o: (2, o, 4, 3, 4),
    (4, 3, 4): lambda o: (2, o, 4, 4, 3),
    (2, 3, 4): lambda o: (2, o, 2, 4, 3),
    (3, 4, 2): lambda o: (2, o, 4, 3, 2),
}

def East7(W):
    W = tuple(W)
    assert len(W) == 7
    x_m3, x_m2, x_m1, x_0, x_1, x_2, x_3 = W
    if x_0 <= x_1 + 1:
        return W
    y_m1, y_0 = bk2(x_m1, x_0)
    if x_m1 > x_1 + 1 and y_0 <= x_2 + 1:
        return (x_m3, x_m2, x_1, y_m1, y_0, x_2, x_3)
    if x_m1 <= x_1 + 1 and x_m1 <= x_2 + 1:
        return (x_m3, x_m2, x_1, x_0, x_m1, x_2, x_3)
    if min(x_m2, x_m1, x_0) > max(x_1, x_2) + 1:
        return (x_m3,) + fw2(x_1, x_2) + bk3(x_m2, x_m1, x_0) + (x_3,)
    shift = max(x_1, x_2) - 2
    reduced = (x_m2 - shift, x_m1 - shift, x_0 - shift,
               x_1 - shift, x_2 - shift)
    for table in (_CASE4A, _CASE4B, _CASE4C):
        if reduced in table:
            return (x_m3,) + tuple(y + shift for y in table[reduced]) + (x_3,)
    if reduced[4] == 2 and reduced[3] <= 0 and reduced[:3] in _CASE4D:
        return (x_m3,) + tuple(y + shift for y in _CASE4D[reduced[:3]](reduced[3])) + (x_3,)
    raise ValueError(f"East7 undefined on {W}")

def rev(W):
    return tuple(reversed(tuple(W)))

def West3(W):
    ans = East3(rev(W))
    return None if ans is None else rev(ans)

def West5(W):
    ans = East5(rev(W))
    return None if ans is None else rev(ans)

def West7(W):
    return rev(East7(rev(W)))

def is_far_apart_decomposable(W):
    W = tuple(W)
    assert len(W) == 7
    indices = list(range(7))
    for p1 in combinations(indices, 2):
        if abs(W[p1[0]] - W[p1[1]]) < 2:
            continue
        r1 = [i for i in indices if i not in p1]
        for p2 in combinations(r1, 2):
            if abs(W[p2[0]] - W[p2[1]]) < 2:
                continue
            r2 = [i for i in r1 if i not in p2]
            for p3 in combinations(r2, 2):
                if abs(W[p3[0]] - W[p3[1]]) >= 2:
                    return True
    return False
# Global up and down maps.

def up(S):
    S = tuple(S)
    n = len(S)
    if S == omega(n):
        return epsilon(n), 3
    if is_full_skeleton(S):
        return inject(S[:-1], S[-1] + 1), 3
    j1, e1 = find_extractable(S)
    C1 = remove_at(S, j1)
    sigma1 = C1 + (e1 - 1,)
    if East3(sigma1[-3:]) is not None:
        ans = inject_right_to_left(sigma1[:-2], (sigma1[-2] + 1, sigma1[-1] + 1))
        return ans, 3
    j2, e2 = find_extractable(C1)
    C2 = remove_at(C1, j2)
    sigma2 = C2 + (e1 - 1, e2 - 1)
    W5 = East5(sigma2[-5:])
    if W5 is not None:
        base = sigma2[:-5] + W5[:2]
        ans = inject_right_to_left(base, tuple(x + 1 for x in W5[2:]))
        return ans, 5
    j3, e3 = find_extractable(C2)
    C3 = remove_at(C2, j3)
    sigma3 = C3 + (e1 - 1, e2 - 1, e3 - 1)
    W7 = sigma3[-7:]
    assert not is_far_apart_decomposable(W7)
    E7 = East7(W7)
    new_sigma3 = sigma3[:-7] + E7
    ans = inject_right_to_left(new_sigma3[:-4], tuple(x + 1 for x in new_sigma3[-4:]))
    return ans, 7

def down(S):
    S = tuple(S)
    n = len(S)
    if S == epsilon(n):
        return omega(n), 3
    j1, f1 = find_extractable(S)
    D1 = remove_at(S, j1)
    candidate = D1 + (f1 - 1,)
    if find_extractable(candidate) is None:
        assert is_Dyck(candidate)
        return candidate, 3
    j2, f2 = find_extractable(D1)
    D2 = remove_at(D1, j2)
    tau1 = D2 + (f1 - 1, f2 - 1)
    if West3(tau1[-3:]) is not None:
        return inject(tau1[:-1], tau1[-1] + 1), 3
    j3, f3 = find_extractable(D2)
    D3 = remove_at(D2, j3)
    tau2 = D3 + (f1 - 1, f2 - 1, f3 - 1)
    W5 = West5(tau2[-5:])
    if W5 is not None:
        base = tau2[:-5] + W5[:3]
        ans = inject_right_to_left(base, tuple(x + 1 for x in W5[3:]))
        return ans, 5
    j4, f4 = find_extractable(D3)
    D4 = remove_at(D3, j4)
    tau3 = D4 + (f1 - 1, f2 - 1, f3 - 1, f4 - 1)
    W7 = tau3[-7:]
    assert not is_far_apart_decomposable(W7)
    new_tau3 = tau3[:-7] + West7(W7)
    ans = inject_right_to_left(new_tau3[:-3], tuple(x + 1 for x in new_tau3[-3:]))
    return ans, 7
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/02_make_strings.py`

```python
def make_strings(n, d):
    ell = (comb(n, 2) - d) // 2
    all_dyck = [S for S in generate_Dycks(n) if defc(S) == d]
    target = {S for S in all_dyck if area(S) <= ell}
    starts = sorted(
        [S for S in target if is_special_skeleton(S)],
        key=lambda S: (area(S), S),
    )
    strings = []
    levels = []
    for start in starts:
        chain = [start]
        current = start
        while area(current) < ell:
            nxt, level = up(current)
            assert defc(nxt) == d
            assert area(nxt) == area(current) + 1
            chain.append(nxt)
            levels.append((current, nxt, level))
            current = nxt
        strings.append(tuple(chain))
    covered = [S for chain in strings for S in chain]
    assert set(covered) == target
    assert len(covered) == len(set(covered))
    return tuple(strings), tuple(levels)
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/01_residual_finite_check.py`

```python
from collections import Counter
from math import comb

def stop(message):
    raise AssertionError(message)

def is_dyck_sequence(seq):
    return (
        bool(seq)
        and seq[0] == 0
        and all(x >= 0 for x in seq)
        and all(seq[i + 1] <= seq[i] + 1
                for i in range(len(seq) - 1))
    )

def deficit_and_area(seq):
    first_index = {}
    for i, value in enumerate(seq):
        first_index.setdefault(value, i)
    deficit = 0
    for i, left in enumerate(seq):
        for right in seq[i + 1:]:
            if left > right + 1:
                deficit += 1
            elif left < right and first_index[left] != i:
                deficit += 1
    return deficit, sum(seq)

def generate_dyck_sequences(length):
    sequences = []
    def extend(prefix):
        if len(prefix) == length:
            sequences.append(prefix)
            return
        for next_value in range(prefix[-1] + 2):
            extend(prefix + (next_value,))
    extend((0,))
    return sequences

def leftmost_extractable(seq):
    for index, value in enumerate(seq):
        has_parent = sum(x == value - 1 for x in seq[:index]) == 1
        next_ok = index == len(seq) - 1 or seq[index + 1] <= value
        if value > 0 and has_parent and next_ok:
            return index, value
    return None

def remove_index(seq, index):
    return seq[:index] + seq[index + 1:]

def is_full_skeleton(seq):
    return is_dyck_sequence(seq) and leftmost_extractable(seq) is None

def almost_zero_sequence(length):
    return (0,) * (length - 1) + (1,)

def excluded_skeleton(length):
    return (0, 0, 1) + (0,) * (length - 4) + (1,)

def is_special_skeleton(seq):
    return is_full_skeleton(seq) and seq != excluded_skeleton(len(seq))

def inject_after_first_parent(seq, value):
    for index, entry in enumerate(seq):
        if entry == value - 1:
            result = seq[:index + 1] + (value,) + seq[index + 1:]
            if is_dyck_sequence(result):
                return result
            stop(("skeleton injection produced non-Dyck",
                  seq, value, result))
    stop(("skeleton injection failed", seq, value))

def east3_applies(window3):
    _, x0, x1 = window3
    return x0 <= x1 + 1

def west3_applies(window3):
    return east3_applies(tuple(reversed(window3)))

def east5_case2b_applies(window5):
    _, x_minus1, x0, x1, x2 = window5
    return (
        x0 > x1 + 1
        and x_minus1 <= x1 + 1
        and x_minus1 <= x2 + 1
    )

def west5_case2b_applies(window5):
    return east5_case2b_applies(tuple(reversed(window5)))

def check_up_prefix(seq, length, deficit, half_area_limit):
    if seq == almost_zero_sequence(length):
        return "up special"
    if is_full_skeleton(seq):
        result = inject_after_first_parent(seq[:-1], seq[-1] + 1)
        if len(result) != length:
            stop(("up skeleton changed length", seq, result))
        return "up skeleton"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: up first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    word1 = child1 + (value1 - 1,)
    if east3_applies(word1[-3:]):
        if index1 >= length - 2:
            stop(("position lemma: up/East3 position", seq, index1))
        return "up East3"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: up second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if not (index1 < length - 3 and index2 < len(child1) - 3):
        stop(("position lemma: up/East5 position",
              seq, index1, child1, index2))
    if not east5_case2b_applies(word2[-5:]):
        stop(("seven-window lemma: up would reach East7",
              length, deficit, half_area_limit, seq, word2[-5:]))
    return "up East5 case 2b"

def check_down_prefix(seq, length, deficit, half_area_limit):
    if seq == excluded_skeleton(length):
        return "down special"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: down first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    skeleton_candidate = child1 + (value1 - 1,)
    if is_full_skeleton(skeleton_candidate):
        if len(skeleton_candidate) != length:
            stop(("down skeleton changed length", seq, skeleton_candidate))
        return "down skeleton"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: down second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if west3_applies(word2[-3:]):
        if not (index1 < length - 1 and index2 < len(child1) - 1):
            stop(("position lemma: down/West3 position",
                  seq, index1, child1, index2))
        return "down West3"
    third = leftmost_extractable(child2)
    if third is None:
        stop(("extraction lemma: down third extraction failed",
              length, deficit, half_area_limit, seq, child2))
    index3, value3 = third
    child3 = remove_index(child2, index3)
    word3 = child3 + (value1 - 1, value2 - 1, value3 - 1)
    if not (
        index1 < length - 2
        and index2 < len(child1) - 2
        and index3 < len(child2) - 2
    ):
        stop(("position lemma: down/West5 position",
              seq, index1, child1, index2, child2, index3))
    if not west5_case2b_applies(word3[-5:]):
        stop(("seven-window lemma: down would reach West7",
              length, deficit, half_area_limit, seq, word3[-5:]))
    return "down West5 case 2b"

def main():
    up_counts = Counter()
    down_counts = Counter()
    by_length = {
        length: {"up": Counter(), "down": Counter()}
        for length in range(4, 8)
    }
    for length in range(4, 8):
        for seq in generate_dyck_sequences(length):
            deficit, area = deficit_and_area(seq)
            if deficit > 2 * length - 8:
                continue
            half_area_limit = (comb(length, 2) - deficit) // 2
            if area <= half_area_limit - 1:
                label = check_up_prefix(
                    seq, length, deficit, half_area_limit)
                up_counts[label] += 1
                by_length[length]["up"][label] += 1
            if area <= half_area_limit and not is_special_skeleton(seq):
                label = check_down_prefix(
                    seq, length, deficit, half_area_limit)
                down_counts[label] += 1
                by_length[length]["down"][label] += 1
    print("EverythingOkay = True")
    print("up counts  ", dict(up_counts))
    print("down counts", dict(down_counts))
    print()
    for length in range(4, 8):
        print(f"n={length}")
        print("  up:  ", dict(by_length[length]["up"]))
        print("  down:", dict(by_length[length]["down"]))
    print()
    print("No East7 or West7 branch was reached for 4 <= n <= 7.")
if __name__ == "__main__":
    main()
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/02_residual_successful_output.txt`

```text
EverythingOkay = True
up counts   {'up skeleton': 42, 'up East3': 152,
             'up special': 2, 'up East5 case 2b': 4}
down counts {'down skeleton': 42, 'down West3': 152,
             'down special': 2, 'down West5 case 2b': 4}
n=4
  up:   {'up skeleton': 1, 'up East3': 2}
  down: {'down skeleton': 1, 'down West3': 2}
n=5
  up:   {'up skeleton': 4, 'up East3': 9}
  down: {'down skeleton': 4, 'down West3': 9}
n=6
  up:   {'up skeleton': 11, 'up special': 1, 'up East3': 32}
  down: {'down special': 1, 'down skeleton': 11, 'down West3': 32}
n=7
  up:   {'up skeleton': 26, 'up special': 1,
         'up East3': 109, 'up East5 case 2b': 4}
  down: {'down skeleton': 26, 'down special': 1,
         'down West3': 109, 'down West5 case 2b': 4}
No East7 or West7 branch was reached for 4 <= n <= 7.
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/03_east7_west7_seven_window_checker.py`

```python
from __future__ import annotations

import math
from functools import lru_cache
from itertools import combinations, permutations
from math import comb


EXPECTED_CASE1_TABLE = {
    10: (33, 23),
    11: (26, 18),
    12: (16, 11),
    13: (9, 6),
    14: (None, None),
    15: (None, None),
    16: (None, None),
    17: (None, None),
    18: (None, None),
    19: (None, None),
    20: (None, None),
    21: (None, None),
}

EXPECTED_CASE2_TABLE = {
    0: (26, 18),
    1: (23, 16),
    2: (23, 16),
    3: (20, 14),
    4: (20, 14),
    5: (19, 13),
    6: (17, 12),
    7: (16, 11),
    8: (16, 11),
    9: (13, 9),
    10: (13, 9),
    11: (12, 8),
    12: (10, 7),
    13: (9, 6),
    14: (9, 6),
    15: (None, None),
    16: (None, None),
    17: (None, None),
    18: (None, None),
    19: (None, None),
    20: (None, None),
    21: (None, None),
}

EXPECTED_FINITE_COUNTS = {
    ("Case 1", "East"): {"children": 2473, "triples": 9919},
    ("Case 1", "West"): {"children": 2911, "triples": 10311},
    ("Case 2", "East"): {"children": 3860, "triples": 715},
    ("Case 2", "West"): {"children": 4827, "triples": 1756},
}


def unique_permutations(seq: tuple[int, ...]):
    """Yield all distinct permutations of seq."""

    seen = set()
    for perm in permutations(seq):
        if perm not in seen:
            seen.add(perm)
            yield perm


def is_far_apart_decomposable(vals: tuple[int, ...]) -> bool:
    """Return True iff vals has three disjoint pairs at distance at least 2."""

    indices = list(range(7))
    for pair1 in combinations(indices, 2):
        if abs(vals[pair1[0]] - vals[pair1[1]]) < 2:
            continue
        remaining1 = [i for i in indices if i not in pair1]
        for pair2 in combinations(remaining1, 2):
            if abs(vals[pair2[0]] - vals[pair2[1]]) < 2:
                continue
            remaining2 = [i for i in remaining1 if i not in pair2]
            for pair3 in combinations(remaining2, 2):
                if abs(vals[pair3[0]] - vals[pair3[1]]) >= 2:
                    return True
    return False


def east3_fails(p: tuple[int, ...]) -> bool:
    """East3 fails iff the central pair violates the reverse condition."""

    return p[3] > p[4] + 1


def east5_fails(p: tuple[int, ...]) -> bool:
    """Return True iff neither appendix East5 Case 2a nor 2b applies."""

    x_m1, x_0, x_1, x_2 = p[2], p[3], p[4], p[5]
    y_0 = x_m1 if x_m1 > x_0 + 1 else x_0
    case2a = (x_m1 > x_1 + 1) and (y_0 <= x_2 + 1)
    case2b = (x_m1 <= x_1 + 1) and (x_m1 <= x_2 + 1)
    return not case2a and not case2b


def is_valid_l_element(p: tuple[int, ...]) -> bool:
    """Return True iff p has affine first four and reverse last three."""

    return all(p[i + 1] <= p[i] + 1 for i in range(3)) and all(
        p[i] <= p[i + 1] + 1 for i in range(4, 6)
    )


def get_ew() -> set[tuple[int, ...]]:
    """Generate normalized East seven-term patterns surviving the preliminary tests."""

    valid_windows = set()
    base_sequences: list[tuple[int, ...]] = []

    def gen_base(seq: tuple[int, ...]) -> None:
        if len(seq) == 7:
            base_sequences.append(seq)
            return
        for step in (0, 1, 2):
            gen_base(seq + (seq[-1] + step,))

    gen_base((0,))

    for base in base_sequences:
        for perm in unique_permutations(base):
            if (
                is_valid_l_element(perm)
                and east3_fails(perm)
                and east5_fails(perm)
                and is_far_apart_decomposable(perm)
            ):
                valid_windows.add(perm)

    return valid_windows


def get_ww(ew: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """West windows are ordinary reversals of East windows."""

    return {tuple(reversed(w)) for w in ew}


def window_stats(window: tuple[int, ...], m: int, suffix_len: int) -> tuple[int, int]:
    """Compute corrected local id and q0 for a window and prefix max m."""

    seen = {}
    win_first = []
    for i, value in enumerate(window):
        if value not in seen:
            seen[value] = i
            win_first.append(True)
        else:
            win_first.append(False)

    is_initial = [win_first[i] and window[i] > m for i in range(len(window))]

    pair_count = 0
    for i in range(len(window)):
        for j in range(i + 1, len(window)):
            vi, vj = window[i], window[j]
            if vi > vj + 1:
                pair_count += 1
            elif vi < vj and not is_initial[i]:
                pair_count += 1

    suffix_start = len(window) - suffix_len
    suffix_correction = 0
    for j in range(suffix_start, len(window)):
        for value in range(m + 1, window[j]):
            if value not in window[:j]:
                suffix_correction += 1

    int_defc = pair_count - suffix_correction

    q0 = sum(max(0, (m - 1) - value) for i, value in enumerate(window) if not is_initial[i])
    return int_defc, q0


def compute_id_mid(window: tuple[int, ...], suffix_len: int) -> tuple[int, int]:
    """Return id_mid(w)=id(w,max(w[0]-1,w[6]-1,mid(w)))."""

    mid_value = sorted(window, reverse=True)[3]
    m = max(window[0] - 1, window[6] - 1, mid_value)
    int_defc, _ = window_stats(window, m, suffix_len)
    return int_defc, m


def compute_id_base(window: tuple[int, ...], suffix_len: int) -> int:
    """Return id_base(w)=id(w,max(w[0]-1,w[6]-1))."""

    int_defc, _ = window_stats(window, max(window[0] - 1, window[6] - 1), suffix_len)
    return int_defc


def compute_k_from_n(n_value: int) -> int:
    """Largest K with C(K,2) <= C(n,2)/2."""

    half = comb(n_value, 2) // 2
    test = 0
    while comb(test + 1, 2) <= half:
        test += 1
    return test


def compute_nk_case1(id_val: int) -> tuple[int | None, int | None]:
    """Compute Case 1 N(id), K(id), including the -4 area penalty."""

    max_n = None
    for n_value in range(8, 300):
        m0 = math.ceil((n_value + id_val - 16) / 3)
        q_star = 3 * m0 - (n_value + id_val - 16)
        lhs_twice = 2 * (comb(m0 + 1, 2) + (m0 - 1) * (n_value - m0 - 1) - q_star)
        rhs_twice = comb(n_value, 2) - id_val - q_star - 3 * (n_value - m0 - 8) - 8
        if lhs_twice <= rhs_twice:
            max_n = n_value
    if max_n is None:
        return None, None
    return max_n, compute_k_from_n(max_n)


def compute_nk_case2(id_val: int) -> tuple[int | None, int | None]:
    """Compute Case 2 N(id), K(id), including the -4 area penalty."""

    max_n = None
    for n_value in range(8, 300):
        chi_numer = 2 * n_value + id_val - 24
        m0 = max(0, math.ceil(chi_numer / 4))
        q_star = max(0, min(4 * m0 - chi_numer, 3))
        lhs_twice = 2 * (comb(m0 + 1, 2) + (m0 - 1) * (n_value - m0 - 1) - q_star)
        rhs_twice = comb(n_value, 2) - id_val - q_star - 4 * (n_value - m0 - 8) - 8
        if lhs_twice <= rhs_twice:
            max_n = n_value
    if max_n is None:
        return None, None
    return max_n, compute_k_from_n(max_n)


def get_groups(window: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Partition sorted(window) into maximal blocks separated by gaps at least 2."""

    sorted_vals = sorted(window)
    groups: list[tuple[int, ...]] = []
    current = [sorted_vals[0]]
    for i in range(1, len(sorted_vals)):
        if sorted_vals[i] - sorted_vals[i - 1] <= 1:
            current.append(sorted_vals[i])
        else:
            groups.append(tuple(current))
            current = [sorted_vals[i]]
    groups.append(tuple(current))
    return groups


@lru_cache(maxsize=None)
def get_children_absolute(window: tuple[int, ...], k_limit: int) -> tuple[tuple[int, ...], ...]:
    """Generate absolute gap-expanded children with max value at most k_limit."""

    extra = k_limit - max(window)
    if extra < 0:
        return ()

    groups = get_groups(window)
    num_gaps = len(groups) + 1
    children = set()

    def gen_compositions(remaining: int, num_parts: int, current: tuple[int, ...] = ()):
        if num_parts == 1:
            yield current + (remaining,)
            return
        for part in range(remaining + 1):
            yield from gen_compositions(remaining - part, num_parts - 1, current + (part,))

    for composition in gen_compositions(extra, num_gaps):
        cumulative_shift = 0
        group_shifts = []
        for gap_index in range(len(groups)):
            cumulative_shift += composition[gap_index]
            group_shifts.append(cumulative_shift)

        value_map = {}
        for group_index, group in enumerate(groups):
            for value in group:
                if value not in value_map:
                    value_map[value] = value + group_shifts[group_index]

        children.add(tuple(value_map[value] for value in window))

    return tuple(sorted(children))


def gen_partitions(total: int, max_parts: int, max_val: int):
    """Yield partitions of exactly total with <= max_parts parts in [1,max_val]."""

    if total == 0:
        yield ()
        return
    if max_parts == 0 or max_val <= 0:
        return
    for first in range(min(total, max_val), 0, -1):
        for rest in gen_partitions(total - first, max_parts - 1, first):
            yield (first,) + rest


def gen_partitions_upto(max_total: int, max_parts: int, max_val: int):
    """Yield partitions with total <= max_total and bounded length/value."""

    yield ()
    if max_total <= 0 or max_parts <= 0 or max_val <= 0:
        return
    for total in range(1, max_total + 1):
        yield from gen_partitions(total, max_parts, max_val)


@lru_cache(maxsize=None)
def cached_partitions_upto(max_total: int, max_parts: int, max_val: int) -> tuple[tuple[int, ...], ...]:
    """Cached tuple form of gen_partitions_upto."""

    return tuple(gen_partitions_upto(max_total, max_parts, max_val))


def compute_defc_and_area(seq: list[int]) -> tuple[int, int]:
    """Compute defc=binom(n,2)-area-dinv and area=sum(seq)."""

    dinv = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j] or seq[i] == seq[j] + 1:
                dinv += 1
    area = sum(seq)
    return comb(len(seq), 2) - area - dinv, area


@lru_cache(maxsize=None)
def m_max_for_n(n_value: int) -> int:
    """Largest m satisfying C(m,2) <= floor(C(n,2)/2)."""

    half = comb(n_value, 2) // 2
    value = 0
    while comb(value + 1, 2) <= half:
        value += 1
    return value


@lru_cache(maxsize=None)
def first_n_with_m_allowed(m_value: int) -> int:
    """Smallest n>=8 for which m satisfies the prefix area bound."""

    n_value = 8
    while m_value > m_max_for_n(n_value):
        n_value += 1
    return n_value


def deficit_n_upper(
    coeff: int,
    m_value: int,
    int_defc: int,
    q0: int,
    n_limit: int,
) -> int:
    """Largest n that can survive the deficit lower bound with q'=0."""

    numerator = coeff * m_value + 8 * coeff - 8 - int_defc - q0
    if coeff == 2:
        return n_limit
    return min(n_limit, numerator // (coeff - 2))


def check_window_single(
    *,
    case_label: str,
    side_label: str,
    base_window: tuple[int, ...],
    child: tuple[int, ...],
    id_val: int,
    n_value: int,
    m_value: int,
    g_value: int,
    coeff: int,
    int_defc_q0: tuple[int, int],
    child_area: int,
) -> dict | None:
    """Return first counterexample for one child/n/m triple, if any."""

    target_defc = 2 * n_value - 8
    total_free = n_value - m_value - 8
    if total_free < 0:
        return None

    int_defc, q0 = int_defc_q0
    q_prime_max = target_defc - int_defc - q0 - coeff * total_free
    if q_prime_max < 0:
        return None

    max_part = max(0, m_value - 1)
    prefix = list(range(m_value + 1))
    prefix_area = comb(m_value + 1, 2)
    m_repeats = [m_value]
    window_list = list(child)
    m_choose = comb(n_value, 2)

    for repeat_count in range(total_free + 1):
        if m_value == 0 and repeat_count < total_free:
            continue

        middle_len = total_free - repeat_count
        base_area = prefix_area + repeat_count * m_value + child_area
        max_partition_sum = min(q_prime_max, middle_len * max_part)
        min_possible_area = base_area + middle_len * (m_value - 1) - max_partition_sum
        if 2 * min_possible_area > m_choose - 8:
            continue

        for partition in cached_partitions_upto(q_prime_max, middle_len, max_part):
            extended = list(partition) + [0] * (middle_len - len(partition))
            middle = [m_value - 1 - deficit for deficit in reversed(extended)]
            seq = prefix + m_repeats * repeat_count + middle + window_list
            defc, area = compute_defc_and_area(seq)

            if defc > target_defc:
                continue
            if 2 * area > m_choose - defc - 8:
                continue

            return {
                "case": case_label,
                "side": side_label,
                "base_window": base_window,
                "child": child,
                "id": id_val,
                "n": n_value,
                "m": m_value,
                "g": g_value,
                "coeff": coeff,
                "repeat_count": repeat_count,
                "middle_len": middle_len,
                "partition": partition,
                "prefix": prefix + m_repeats * repeat_count + middle,
                "seq": seq,
                "defc": defc,
                "area": area,
                "target_defc": target_defc,
            }

    return None


def compare_threshold_table(
    label: str,
    computed: dict[int, tuple[int | None, int | None]],
    expected: dict[int, tuple[int | None, int | None]],
) -> bool:
    """Print an exact threshold table comparison."""

    mismatches = []
    for id_val in sorted(expected):
        if computed.get(id_val) != expected[id_val]:
            mismatches.append((id_val, computed.get(id_val), expected[id_val]))

    if not mismatches:
        print(f"{label} threshold table comparison: MATCH")
        return True

    print(f"{label} threshold table comparison: MISMATCH")
    for id_val, got, want in mismatches:
        print(f"  id={id_val}: computed={got}, expected={want}")
    return False


def print_table(label: str, table: dict[int, tuple[int | None, int | None]]) -> None:
    """Print a threshold table."""

    print(label)
    print(f"{'id':>4} {'N':>8} {'K':>8}")
    for id_val in sorted(table):
        n_value, k_value = table[id_val]
        n_text = "--" if n_value is None else str(n_value)
        k_text = "--" if k_value is None else str(k_value)
        print(f"{id_val:>4} {n_text:>8} {k_text:>8}")
    print()


def build_threshold_table(case_num: int) -> dict[int, tuple[int | None, int | None]]:
    """Build the threshold table for one case."""

    if case_num == 1:
        return {id_val: compute_nk_case1(id_val) for id_val in range(10, 22)}
    return {id_val: compute_nk_case2(id_val) for id_val in range(0, 22)}


def verify_id_mid_bound(windows: dict[str, set[tuple[int, ...]]]) -> bool:
    """Verify id_mid(w)>=10 over EW union WW."""

    min_record = None
    distribution: dict[int, int] = {}
    for suffix_len, side_label, side_windows in (
        (3, "East", windows["East"]),
        (4, "West", windows["West"]),
    ):
        for window in side_windows:
            id_val, threshold = compute_id_mid(window, suffix_len)
            distribution[id_val] = distribution.get(id_val, 0) + 1
            if min_record is None or id_val < min_record[0]:
                min_record = (id_val, threshold, side_label, window)

    assert min_record is not None
    ok = min_record[0] >= 10
    print(
        "id_mid structural check over EW union WW: "
        f"{'PASS' if ok else 'FAIL'} (min id_mid={min_record[0]}, "
        f"threshold={min_record[1]}, side={min_record[2]}, window={min_record[3]})"
    )
    print(f"id_mid distribution: {dict(sorted(distribution.items()))}\n")
    return ok


def id_from_table(
    id_val: int,
    table: dict[int, tuple[int | None, int | None]],
    *,
    case_label: str,
    side_label: str,
    window: tuple[int, ...],
) -> tuple[int | None, int | None]:
    """Look up an id without clamping; reject unexpected values."""

    if id_val not in table:
        raise ValueError(
            f"Unexpected id in {case_label} {side_label}: id={id_val}, window={window}"
        )
    return table[id_val]


def run_case(
    *,
    case_num: int,
    side_label: str,
    windows: set[tuple[int, ...]],
    table: dict[int, tuple[int | None, int | None]],
) -> tuple[list[dict], dict[str, int]]:
    """Run one finite case."""

    case_label = f"Case {case_num}"
    problems = []
    suffix_len = 3 if side_label == "East" else 4
    windows_checked = 0
    children_generated = 0
    active_children = 0
    triples_checked = 0

    for base_window in sorted(windows):
        windows_checked += 1
        if case_num == 1:
            id_val, _ = compute_id_mid(base_window, suffix_len)
        else:
            id_val = compute_id_base(base_window, suffix_len)

        n_limit, k_limit = id_from_table(
            id_val,
            table,
            case_label=case_label,
            side_label=side_label,
            window=base_window,
        )
        if n_limit is None or k_limit is None:
            continue

        children = get_children_absolute(base_window, k_limit)
        children_generated += len(children)
        for child in children:
            child_has_checked_triple = False
            child_area = sum(child)
            fourth_largest = sorted(child, reverse=True)[3]
            if case_num == 1:
                m_start = max(0, child[0] - 1, child[6] - 1, fourth_largest)
                m_stop = m_max_for_n(n_limit)
            else:
                m_start = max(0, child[0] - 1, child[6] - 1)
                m_stop = min(m_max_for_n(n_limit), fourth_largest - 1)

            if m_start > m_stop:
                continue

            for m_value in range(m_start, m_stop + 1):
                g_value = sum(1 for value in child if value > m_value)
                if case_num == 1:
                    if g_value > 3:
                        continue
                    coeff = 3
                else:
                    if g_value < 4:
                        continue
                    coeff = g_value

                stats = window_stats(child, m_value, suffix_len)
                n_start = max(8, m_value + 8, first_n_with_m_allowed(m_value))
                n_stop = deficit_n_upper(coeff, m_value, stats[0], stats[1], n_limit)
                if n_start > n_stop:
                    continue

                for n_value in range(n_start, n_stop + 1):
                    triples_checked += 1
                    child_has_checked_triple = True
                    problem = check_window_single(
                        case_label=case_label,
                        side_label=side_label,
                        base_window=base_window,
                        child=child,
                        id_val=id_val,
                        n_value=n_value,
                        m_value=m_value,
                        g_value=g_value,
                        coeff=coeff,
                        int_defc_q0=stats,
                        child_area=child_area,
                    )
                    if problem is not None:
                        problems.append(problem)
                        print_first_failure(problem)
                        return problems, {
                            "windows": windows_checked,
                            "children": children_generated,
                            "active_children": active_children,
                            "triples": triples_checked,
                        }

            if child_has_checked_triple:
                active_children += 1

    counts = {
        "windows": windows_checked,
        "children": children_generated,
        "active_children": active_children,
        "triples": triples_checked,
    }
    print(
        f"{case_label} {side_label}: windows={windows_checked}, "
        f"children={children_generated}, active_children={active_children}, "
        f"triples={triples_checked}, problems={len(problems)}"
    )
    return problems, counts


def print_first_failure(problem: dict) -> None:
    """Print the first failed obligation."""

    print("FIRST FAILURE")
    for key in (
        "case",
        "side",
        "base_window",
        "child",
        "id",
        "n",
        "m",
        "g",
        "coeff",
        "repeat_count",
        "middle_len",
        "partition",
        "prefix",
        "seq",
        "defc",
        "area",
        "target_defc",
    ):
        print(f"  {key}: {problem[key]}")


def compare_counts(counts_by_case: dict[tuple[str, str], dict[str, float | int]]) -> bool:
    """Compare finite-search counts with the expected finite-check counts."""

    all_match = True
    print("\nExpected finite-count comparison:")
    for key, expected in EXPECTED_FINITE_COUNTS.items():
        got = counts_by_case[key]
        got_pair = {"children": int(got["children"]), "triples": int(got["triples"])}
        if got_pair == expected:
            print(f"  {key[0]} {key[1]}: MATCH {got_pair}")
        else:
            all_match = False
            print(f"  {key[0]} {key[1]}: MISMATCH got={got_pair}, expected={expected}")

    if not all_match:
        print(
            "  Count note: children are absolute generated children for finite "
            "table rows; triples are finite (child,n,m) checks after actual-g "
            "deficit pruning."
        )
    print()
    return all_match


def main() -> None:
    """Run the East7-West7 seven-window checker."""

    ew = get_ew()
    ww = get_ww(ew)
    ew_ww = ew | ww
    print(f"  |EW| = {len(ew)}, |WW| = {len(ww)}, |EW union WW| = {len(ew_ww)}\n")

    case1_table = build_threshold_table(case_num=1)
    case2_table = build_threshold_table(case_num=2)
    print_table("Case 1 threshold table", case1_table)
    print_table("Case 2 threshold table", case2_table)

    table_results = [
        compare_threshold_table("Case 1", case1_table, EXPECTED_CASE1_TABLE),
        compare_threshold_table("Case 2", case2_table, EXPECTED_CASE2_TABLE),
    ]
    print()

    id_mid_ok = verify_id_mid_bound({"East": ew, "West": ww})

    all_problems = []
    counts_by_case: dict[tuple[str, str], dict[str, float | int]] = {}

    for case_num, side_label, windows, table in (
        (1, "East", ew, case1_table),
        (1, "West", ww, case1_table),
        (2, "East", ew, case2_table),
        (2, "West", ww, case2_table),
    ):
        problems, counts = run_case(
            case_num=case_num,
            side_label=side_label,
            windows=windows,
            table=table,
        )
        all_problems.extend(problems)
        counts_by_case[(f"Case {case_num}", side_label)] = counts

    counts_match = compare_counts(counts_by_case)

    tables_ok = all(table_results)
    if tables_ok:
        print("Threshold-table checks: MATCH")
    else:
        print("Threshold-table checks: MISMATCH")

    if id_mid_ok:
        print("id_mid>=10 check: PASS")
    else:
        print("id_mid>=10 check: FAIL")

    if tables_ok and id_mid_ok and not all_problems:
        if not counts_match:
            print("Counts differ from expected finite counts; see comparison above.")
        print("SUCCESS: East7/West7 seven-window verification passed.")
        return

    print(f"FAILED: problems={len(all_problems)}, tables_ok={tables_ok}, id_mid_ok={id_mid_ok}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()

```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/04_east7_west7_successful_output.txt`

```text
  |EW| = 7194, |WW| = 7194, |EW union WW| = 14388

Case 1 threshold table
  id        N        K
  10       33       23
  11       26       18
  12       16       11
  13        9        6
  14       --       --
  15       --       --
  16       --       --
  17       --       --
  18       --       --
  19       --       --
  20       --       --
  21       --       --

Case 2 threshold table
  id        N        K
   0       26       18
   1       23       16
   2       23       16
   3       20       14
   4       20       14
   5       19       13
   6       17       12
   7       16       11
   8       16       11
   9       13        9
  10       13        9
  11       12        8
  12       10        7
  13        9        6
  14        9        6
  15       --       --
  16       --       --
  17       --       --
  18       --       --
  19       --       --
  20       --       --
  21       --       --

Case 1 threshold table comparison: MATCH
Case 2 threshold table comparison: MATCH

id_mid structural check over EW union WW: PASS (min id_mid=10, threshold=1, side=East, window=(1, 2, 3, 4, 1, 1, 0))
id_mid distribution: {10: 6, 11: 24, 12: 157, 13: 359, 14: 838, 15: 1378, 16: 1875, 17: 2670, 18: 2854, 19: 2559, 20: 1392, 21: 276}

Case 1 East: windows=7194, children=2473, active_children=1087, triples=9919, problems=0
Case 1 West: windows=7194, children=2911, active_children=1225, triples=10311, problems=0
Case 2 East: windows=7194, children=3860, active_children=456, triples=715, problems=0
Case 2 West: windows=7194, children=4827, active_children=1183, triples=1756, problems=0

Expected finite-count comparison:
  Case 1 East: MATCH {'children': 2473, 'triples': 9919}
  Case 1 West: MATCH {'children': 2911, 'triples': 10311}
  Case 2 East: MATCH {'children': 3860, 'triples': 715}
  Case 2 West: MATCH {'children': 4827, 'triples': 1756}

Threshold-table checks: MATCH
id_mid>=10 check: PASS
SUCCESS: East7/West7 seven-window verification passed.
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/05_lemma_525_limited_nonzero_checker.py`

```python
from collections import Counter
from math import comb
N_MIN, N_MAX = 4, 13
MAX_NONZERO = 7

def require(test, message):
    if not test:
        raise AssertionError(message)

def nonzero_count(S):
    return sum(1 for x in S if x != 0)

def ell_value(n, d):
    return (comb(n, 2) - d) // 2

def check_image(source, image, n, d, delta):
    require(is_Dyck(image), f"non-Dyck image: {source} -> {image}")
    require(len(image) == n, f"length changed: {source} -> {image}")
    require(defc(image) == d, f"deficit changed: {source} -> {image}")
    require(area(image) == area(source) + delta,
            f"wrong area change: {source} -> {image}")

def checked_up(S, n, d, ell):
    S = tuple(S)
    if S == omega(n):
        image = epsilon(n)
        check_image(S, image, n, d, 1)
        return "up special", 3
    if is_full_skeleton(S):
        image = inject(S[:-1], S[-1] + 1)
        check_image(S, image, n, d, 1)
        return "up skeleton", 3
    j1, e1 = find_extractable(S)
    C1 = remove_at(S, j1)
    sigma1 = C1 + (e1 - 1,)
    if East3(sigma1[-3:]) is not None:
        require(j1 < n - 2, f"up East3 position bound: {S}")
        image = inject_right_to_left(sigma1[:-2],
                                     (sigma1[-2] + 1, sigma1[-1] + 1))
        check_image(S, image, n, d, 1)
        return "up East3", 3
    j2, e2 = find_extractable(C1)
    C2 = remove_at(C1, j2)
    sigma2 = C2 + (e1 - 1, e2 - 1)
    E5 = East5(sigma2[-5:])
    if E5 is not None:
        require(j1 < n - 3 and j2 < len(C1) - 3,
                f"up East5 position bound: {S}")
        base = sigma2[:-5] + E5[:2]
        image = inject_right_to_left(base, tuple(x + 1 for x in E5[2:]))
        check_image(S, image, n, d, 1)
        return "up East5", 5
    j3, e3 = find_extractable(C2)
    C3 = remove_at(C2, j3)
    sigma3 = C3 + (e1 - 1, e2 - 1, e3 - 1)
    W7 = sigma3[-7:]
    require(not is_far_apart_decomposable(W7), f"bad East7 window: {S}")
    require(j1 < n - 3 and j2 < len(C1) - 3 and j3 < len(C2) - 3,
            f"up East7 position bound: {S}")
    E7 = East7(W7)
    image = inject_right_to_left(sigma3[:-7] + E7[:-4],
                                 tuple(x + 1 for x in E7[-4:]))
    check_image(S, image, n, d, 1)
    return "up East7", 7

def checked_down(S, n, d, ell):
    S = tuple(S)
    if S == epsilon(n):
        image = omega(n)
        check_image(S, image, n, d, -1)
        return "down special", 3
    j1, f1 = find_extractable(S)
    D1 = remove_at(S, j1)
    candidate = D1 + (f1 - 1,)
    if find_extractable(candidate) is None:
        check_image(S, candidate, n, d, -1)
        return "down skeleton", 3
    j2, f2 = find_extractable(D1)
    D2 = remove_at(D1, j2)
    tau1 = D2 + (f1 - 1, f2 - 1)
    if West3(tau1[-3:]) is not None:
        require(j1 < n - 1 and j2 < len(D1) - 1,
                f"down West3 position bound: {S}")
        image = inject(tau1[:-1], tau1[-1] + 1)
        check_image(S, image, n, d, -1)
        return "down West3", 3
    j3, f3 = find_extractable(D2)
    D3 = remove_at(D2, j3)
    tau2 = D3 + (f1 - 1, f2 - 1, f3 - 1)
    W5 = West5(tau2[-5:])
    if W5 is not None:
        require(j1 < n - 2 and j2 < len(D1) - 2 and j3 < len(D2) - 2,
                f"down West5 position bound: {S}")
        base = tau2[:-5] + W5[:3]
        image = inject_right_to_left(base, tuple(x + 1 for x in W5[3:]))
        check_image(S, image, n, d, -1)
        return "down West5", 5
    j4, f4 = find_extractable(D3)
    D4 = remove_at(D3, j4)
    tau3 = D4 + (f1 - 1, f2 - 1, f3 - 1, f4 - 1)
    W7 = tau3[-7:]
    require(not is_far_apart_decomposable(W7), f"bad West7 window: {S}")
    require(j1 < n - 2 and j2 < len(D1) - 2
            and j3 < len(D2) - 2 and j4 < len(D3) - 2,
            f"down West7 position bound: {S}")
    E7 = West7(W7)
    image = inject_right_to_left(tau3[:-7] + E7[:-3],
                                 tuple(x + 1 for x in E7[-3:]))
    check_image(S, image, n, d, -1)
    return "down West7", 7

def run_limited_nonzero_checker():
    generated = {}
    eligible = Counter()
    branches = Counter()
    levels = Counter()
    failures = []
    for n in range(N_MIN, N_MAX + 1):
        seqs = [S for S in generate_Dycks(n) if nonzero_count(S) <= MAX_NONZERO]
        generated[n] = len(seqs)
        for S in seqs:
            d = defc(S)
            if d > 2 * n - 8:
                continue
            ell = ell_value(n, d)
            try:
                if area(S) < ell:
                    branch, level = checked_up(S, n, d, ell)
                    eligible[(n, "up")] += 1
                    branches[("up", branch)] += 1
                    levels[("up", level)] += 1
                if area(S) <= ell and not is_special_skeleton(S):
                    branch, level = checked_down(S, n, d, ell)
                    eligible[(n, "down")] += 1
                    branches[("down", branch)] += 1
                    levels[("down", level)] += 1
            except Exception as exc:
                failures.append((n, S, str(exc)))
    require(not failures, f"first failure: {failures[0] if failures else None}")
    up_total = sum(v for (n, direction), v in eligible.items()
                   if direction == "up")
    down_total = sum(v for (n, direction), v in eligible.items()
                     if direction == "down")
    print("generated by n:", generated)
    print("eligible up calls:", up_total)
    print("eligible down calls:", down_total)
    print("eligible calls by n/direction:", dict(sorted(eligible.items())))
    print("branches:", dict(sorted(branches.items())))
    print("levels:", dict(sorted(levels.items())))
    print("position-bound or image failures:", len(failures))
    print("status: PASS")
run_limited_nonzero_checker()
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/06_lemma_525_limited_nonzero_successful_output.txt`

```text
generated by n: {4: 14, 5: 42, 6: 132, 7: 429, 8: 1430,
                 9: 3432, 10: 7072, 11: 13260,
                 12: 23256, 13: 38760}
eligible up calls: 11879
eligible down calls: 9486
position-bound or image failures: 0
status: PASS
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/07_lemma_525_prefix_checker.py`

```python
from collections import Counter
from itertools import product
from math import comb
N_MIN, N_MAX = 9, 16
EXPECTED = {
    (9, 1, "pq_lt_4"): 504, (9, 1, "pq_eq_4"): 3024,
    (10, 1, "pq_lt_4"): 720, (10, 1, "pq_eq_4"): 5040,
    (11, 1, "pq_lt_4"): 990, (11, 1, "pq_eq_4"): 7920,
    (12, 1, "pq_lt_4"): 1320, (12, 1, "pq_eq_4"): 11880,
    (13, 1, "pq_lt_4"): 1716, (13, 1, "pq_eq_4"): 17160,
    (14, 1, "pq_lt_4"): 2184, (14, 1, "pq_eq_4"): 24024,
    (15, 1, "pq_lt_4"): 2730, (15, 1, "pq_eq_4"): 32760,
    (16, 1, "pq_lt_4"): 3360, (16, 1, "pq_eq_4"): 43680,
    (9, 2, "pq_lt_4"): 336, (9, 2, "pq_eq_4"): 1680,
    (10, 2, "pq_lt_4"): 504, (10, 2, "pq_eq_4"): 3024,
    (11, 2, "pq_lt_4"): 720, (11, 2, "pq_eq_4"): 5040,
    (12, 2, "pq_lt_4"): 990, (12, 2, "pq_eq_4"): 7920,
    (13, 2, "pq_lt_4"): 1320, (13, 2, "pq_eq_4"): 11880,
    (14, 2, "pq_lt_4"): 1716, (14, 2, "pq_eq_4"): 17160,
    (15, 2, "pq_lt_4"): 2184, (15, 2, "pq_eq_4"): 24024,
    (16, 2, "pq_lt_4"): 2730, (16, 2, "pq_eq_4"): 32760,
}

def require(test, message):
    if not test:
        raise AssertionError(message)

def bounded_product(bounds):
    return product(*(range(bound + 1) for bound in bounds))

def defc(word):
    n = len(word)
    dinv_count = sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        if word[i] == word[j] or word[i] == word[j] + 1
    )
    return comb(n, 2) - area(word) - dinv_count

def claim_words(n, claim, subcase):
    if claim == 1 and subcase == "pq_lt_4":
        prefix = tuple(range(0, n - 3))
        bounds = (n - 3, n - 2, n - 1)
    elif claim == 1 and subcase == "pq_eq_4":
        prefix = tuple(range(0, n - 4))
        bounds = (n - 4, n - 3, n - 2, n - 1)
    elif claim == 2 and subcase == "pq_lt_4":
        prefix = (0,) + tuple(range(0, n - 4))
        bounds = (n - 4, n - 3, n - 2)
    elif claim == 2 and subcase == "pq_eq_4":
        prefix = (0,) + tuple(range(0, n - 5))
        bounds = (n - 5, n - 4, n - 3, n - 2)
    else:
        raise ValueError("unknown claim/subcase")
    for stars in bounded_product(bounds):
        yield prefix + stars

def run_prefix_checker():
    counts = Counter()
    failures = []
    for n in range(N_MIN, N_MAX + 1):
        M = comb(n, 2)
        for claim in (1, 2):
            for subcase in ("pq_lt_4", "pq_eq_4"):
                # In the p+q=4 boundary this is q+1 for up (2,2)
                # and q for down (1,3).
                adjustment = 3 if subcase == "pq_eq_4" else 0
                for word in claim_words(n, claim, subcase):
                    counts[(n, claim, subcase)] += 1
                    D = defc(word)
                    A = area(word)
                    deficit_contradiction = D > 2 * n - 8
                    area_contradiction = 2 * A > M - D - 2 * adjustment
                    if not (deficit_contradiction or area_contradiction):
                        failures.append((n, claim, subcase, word, D, A))
    require(dict(counts) == EXPECTED, "word counts do not match")
    require(not failures, f"first failure: {failures[0] if failures else None}")
    print("counts by n/claim/subcase:", dict(sorted(counts.items())))
    print("failures:", len(failures))
    print("status: PASS")
run_prefix_checker()
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/08_lemma_525_prefix_successful_output.txt`

```text
failures: 0
status: PASS
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/README.md`

```markdown
# Code

This directory contains the code listings from Appendix A and Appendix B of the
2026 Dyck symmetric functions preprint.

## Purpose

These scripts package the finite computations used in the appendices of the
preprint. Appendix A contains reusable Dyck-sequence routines and string
generation code. Appendix B contains exhaustive finite checkers used in the
local well-definedness proofs for the skeleton string construction.

## Dependencies

Python 3 with the standard library only.

Run scripts with ordinary assertion checking enabled. Do not use Python's
optimized mode, because `assert` statements are part of the verification.

## Inputs

The checkers have no external data input. Each script enumerates its stated
finite domain internally.

## Outputs

Successful runs print count summaries and final success lines. The expected
successful-output transcripts for the Appendix B checkers are stored beside
the scripts as `.txt` files when the appendix includes such a transcript.

## Appendix A

`appendix_a/01_core_dyck_sequence_routines.py` is the core Dyck-sequence code
from Appendix A.

`appendix_a/02_make_strings.py` is the Appendix A routine that builds the
lower-half string decomposition from the core routines.

These two files are appendix listings. They are kept here because they appear
in Appendix A.

Command:

````text
python run_appendix_listing.py appendix_a/02_make_strings.py
````

The wrapper prepends the core routines before running this listing. This
routine returns the lower-half strings for requested parameters when called
from Python; it is included mainly as appendix code rather than as a command
line report.

## Appendix B

`appendix_b/01_residual_finite_check.py` is the finite checker for the small
residual range in the local well-definedness proof.

`appendix_b/03_east7_west7_seven_window_checker.py` is the finite checker for
the seven-entry East/West local move.

`appendix_b/05_lemma_525_limited_nonzero_checker.py` is the limited-nonzero
finite checker for Lemma 5.25.

`appendix_b/07_lemma_525_prefix_checker.py` is the finite checker for the two
prefix forms excluded in the proof of Lemma 5.25.

The `.txt` files in `appendix_b/` are the successful-output listings printed in
the appendix.

Some Appendix B listings rely on routines defined earlier in Appendix A. To run
the listings without editing them, use:

````text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
````

## Range Checked

`appendix_b/01_residual_finite_check.py` enumerates Dyck sequences of lengths
`4 <= n <= 7` satisfying the paper's deficit and area hypotheses for the
residual local-lemma branches.

`appendix_b/03_east7_west7_seven_window_checker.py` enumerates the finite
East7 and West7 seven-entry window domains and their bounded absolute children
after the paper's threshold reductions.

`appendix_b/05_lemma_525_limited_nonzero_checker.py` checks all Dyck sequences
with `4 <= n <= 13` and at most seven nonzero entries satisfying the fixed
deficit and area hypotheses.

`appendix_b/07_lemma_525_prefix_checker.py` checks the two excluded prefix
forms in the range `9 <= n <= 16`.

## Runtime

On the current local machine, each Appendix B checker completed in a few
seconds or less on June 13, 2026. Runtime may vary, but no external packages or
cached data are required.

## Interpretation

The computations are finite exhaustive verifications after the written proof
reduces the relevant obligations to bounded domains. They should be read as
proof-supporting appendix checks for those domains, not as broad experimental
evidence for statements outside the stated ranges.

## Limitations

The scripts verify exactly the finite obligations encoded in the appendix
listings. They do not independently reprove the symbolic reductions in the
paper, and they should be rechecked if the corresponding preprint statements,
definitions, or ranges change.
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/code/run_appendix_listing.py`

```python
"""Run an extracted appendix listing with the Appendix A routines loaded.

The extracted listings are kept unchanged. This runner supplies the shared
namespace that the paper has implicitly across appendix code blocks.
"""

from pathlib import Path
import argparse


APPENDIX_A_FILES = (
    "appendix_a/01_core_dyck_sequence_routines.py",
    "appendix_a/02_make_strings.py",
)


def exec_file(path, namespace):
    source = path.read_text(encoding="ascii")
    exec(compile(source, str(path), "exec"), namespace)


def main():
    parser = argparse.ArgumentParser(description="Run an extracted appendix listing.")
    parser.add_argument("listing", help="path to the listing, relative to code/")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    namespace = {"__name__": "__main__"}
    for relative_path in APPENDIX_A_FILES:
        exec_file(here / relative_path, namespace)
    exec_file(here / args.listing, namespace)


if __name__ == "__main__":
    main()
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/COMPLETION_REVIEW.md`

```markdown
# Completion Review

This file records the completion pass for the first population of this item.

## Resolved Feedback

- The explanation file was rewritten as explanatory prose rather than a status,
  transfer, or review ledger.
- The explanation now summarizes the appendix lemmas, the finite checks in
  Appendix A and Appendix B, and why those checks are used in the proofs.
- Ordinary explanatory prose is not italicized.
- The code layer contains the Appendix A and Appendix B listings, including the
  lower-half string generation routine and the successful-output transcripts
  for the proof-critical Appendix B checks.
- Public arXiv metadata was added for arXiv:2605.13003.

## Verification Run

The following commands were run successfully on June 13, 2026 from this item's
`code/` directory:

````text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
````

The repository site was also regenerated successfully with:

````text
python build_site.py
````

## Agent Routing

Software/computation agent: packaging-level reproducibility is complete. The
remaining software work is only needed if the appendix listings change or if a
more automated transcript comparison is desired.

Mathematical accuracy agent: no immediate blocker for this curated item. A
future independent review should compare the explanation and status language
against the final published paper if arXiv:2605.13003 is revised or published.

Pedagogy/exposition agent: no immediate blocker. Future exposition work should
focus on optional examples or diagrams, not on changing the proof status.
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 92378
sha256: 931f87d4d7e62498edc0414d5a0bfaa1ba0be0ce9649c8d674a9704db7ceb7b8
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}
\usepackage{array}
\usepackage{url}

\title{Finite Computations in the Dyck Symmetric Functions Appendices}
\author{}
\date{}

\begin{document}
\emergencystretch=3em
\maketitle

\section{What the Appendix Code Supports}

The 2026 preprint proves a string decomposition for Dyck sequences in a range
of deficits. The construction uses two local operations, called
\(\mathrm{up}\) and \(\mathrm{down}\), which move a Dyck sequence one step in
area while preserving the relevant deficit. These operations are defined by
looking for a small local pattern, removing a few entries, changing a short
East or West window, and then reinserting the changed entries.

Most of the proof is symbolic: it shows that the operations preserve the Dyck
condition, preserve the deficit, and stay inside the intended range. The
appendix computations handle finite parts of this argument where the proof has
reduced the problem to checking all possible short windows or all possible
small residual inputs.

\section{Appendix A}

Appendix A gives reusable code for Dyck sequences. It defines the basic
statistics, the skeleton tests, the insertion and extraction routines, and the
local \(\mathrm{up}\) and \(\mathrm{down}\) maps. It also gives the routine
that starts from the special skeletons and repeatedly applies
\(\mathrm{up}\) to form the lower half of each string.

The Appendix A code is included here because it is the computational form of
the construction itself. It can be used to reproduce examples of the strings
and to check small cases of the decomposition.

In this repository, Appendix A is represented by the following files in
\path{code/appendix_a/}:
\begin{itemize}
\item \path{01_core_dyck_sequence_routines.py}: the
basic Dyck-sequence routines and the definitions of the local
\(\mathrm{up}\) and \(\mathrm{down}\) algorithms.
\item \path{02_make_strings.py}: the Appendix A routine
that builds the lower-half strings from the special skeletons.
\end{itemize}

\section{Appendix B}

Appendix B proves that the local operations used in Appendix A are
well-defined in the range needed by the theorem. In the arXiv version, the
four local lemmas are Lemmas 5.22--5.25:
\begin{center}
\begin{tabular}{>{\raggedright\arraybackslash}p{0.18\linewidth}
                >{\raggedright\arraybackslash}p{0.34\linewidth}
                >{\raggedright\arraybackslash}p{0.34\linewidth}}
Lemma & Title & Role \\
\hline
5.22 & Skeleton cases succeed & Checks that the skeleton branches return Dyck
sequences in the required range. \\
5.23 & Extraction chains never fail & Checks that every extraction requested
by the staged algorithms exists. \\
5.24 & The seven-window branches do not fail & Checks the final seven-entry
East and West local moves. \\
5.25 & Bounded extraction positions and injection nonfailure & Checks the
position bounds needed for later insertion steps. \\
\end{tabular}
\end{center}

These lemmas check four basic points:
\begin{itemize}
\item when the construction recognizes a skeleton case, the proposed output is
again a Dyck sequence of the required form;
\item when the construction needs to remove entries, the entries it asks for
actually exist;
\item when the construction reaches the seven-entry East or West move, every
possible short window satisfies the inequalities needed by the proof;
\item the positions used for later insertion steps stay within the allowed
bounds.
\end{itemize}

The symbolic proof handles the infinite families. The finite computations in
Appendix B close the remaining cases.

\subsection{Residual Small Range}

One checker enumerates the remaining small values \(4\le n\le 7\). For each
Dyck sequence in that finite range, it follows the decision steps used by the
\(\mathrm{up}\) and \(\mathrm{down}\) algorithms and confirms that each input
falls into one of the cases already covered by the proof. It also confirms that
the seven-entry East and West moves are not reached in this small residual
range.

This corresponds to \path{01_residual_finite_check.py} in
\path{code/appendix_b/}. It supports the small-range parts of Lemmas 5.22,
5.23, 5.24, and 5.25 at once:
\begin{itemize}
\item for Lemma 5.22, it checks the skeleton branches in the residual range;
\item for Lemma 5.23, it checks that the extractions used before each branch
stops exist;
\item for Lemma 5.24, it confirms that the seven-window branch is not reached
for \(4\le n\le 7\);
\item for Lemma 5.25, it checks the relevant position bounds before the
residual branch stops.
\end{itemize}
The successful-output transcript is
\path{02_residual_successful_output.txt}.

\subsection{Seven-Entry East and West Windows}

The largest local move changes a window of seven entries. The proof reduces
this part to a finite list of possible East and West windows together with the
short extensions that can appear next to them. The checker enumerates those
windows and verifies the threshold inequalities used in the argument. This is
needed because the local move has several boundary cases that are easier and
less error-prone to exhaust by computation than to list manually in the text.

This corresponds to \path{03_east7_west7_seven_window_checker.py} in
\path{code/appendix_b/}. It is the finite checker for Lemma 5.24 in the
\(n\ge 8\) part of the proof. The successful-output transcript is
\path{04_east7_west7_successful_output.txt}.

\subsection{Position Bounds}

Another part of the proof needs to know that certain extraction and insertion
positions remain legal. Appendix B treats the general case symbolically and
then leaves two finite domains to check. The first finite checker covers words
with at most seven nonzero entries in the required range. The second covers two
specific prefix forms that are excluded from the symbolic argument. In both
cases, the code enumerates the finite domain and verifies that every word leads
to one of the contradictions or bounds used in the written proof.

These files correspond to Lemma 5.25:
\begin{itemize}
\item \path{05_lemma_525_limited_nonzero_checker.py}
checks the enlarged finite domain with \(4\le n\le 13\) and at most seven
nonzero entries. Its successful-output transcript is
\path{06_lemma_525_limited_nonzero_successful_output.txt}.
\item \path{07_lemma_525_prefix_checker.py} checks the
two excluded prefix forms in the finite range \(9\le n\le 16\). Its
successful-output transcript is
\path{08_lemma_525_prefix_successful_output.txt}.
\end{itemize}

\section{Why These Checks Are Included}

The computations are included because they are part of the proof, not just
evidence for the theorem. Each computation corresponds to a finite exhaustive
step that appears after the main argument has reduced an infinite statement to
a bounded list of cases. The appendix code records exactly what was checked,
and the successful-output listings record the expected result of those checks.
\end{document}
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/html/body.html`

```html
<p>This item records finite computations used as proof components in the 2026 preprint on Dyck symmetric functions.</p>

<p>The code files are extracted from Appendix A and Appendix B. Appendix A contains the reusable Dyck-sequence routines and the routine that builds lower-half strings. Appendix B contains the finite checkers used in the local well-definedness proof: the small residual range, the seven-entry East/West window check, and the two finite checks used for the position-bound lemma.</p>
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/item.yaml`

```yaml
title: Dyck Symmetric Computer-Assisted Proofs 2026
slug: dyck_symmetric_computer_assisted_proofs_2026
status_summary: Proof-supporting appendix computations for arXiv:2605.13003; packaged checkers reproduce the successful finite verifications.
source_paths:
  - ../Dyck/paper/working_drafts/arxiv_submission.tex
  - ../Dyck/paper/working_drafts/draft_v3_sections/appendix_a_code.tex
  - ../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_local_proofs.tex
  - ../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_lemma_525.tex
related_papers:
  - arXiv:2605.13003
  - https://arxiv.org/abs/2605.13003
downloads:
  - explanation.tex
```

### `items/dyck_symmetric_computer_assisted_proofs_2026/README.md`

```markdown
# Dyck Symmetric Computer-Assisted Proofs 2026

Status summary: Proof-supporting appendix computations for
arXiv:2605.13003; packaged checkers reproduce the successful finite
verifications.

## Summary

This item curates the finite proof-supporting computations from the 2026
preprint on Dyck symmetric functions. The code files are extracted from
Appendix A and Appendix B, with successful-output transcripts kept separately
as text files. The computations are presented as finite exhaustive steps inside
the paper's proofs, not as exploratory evidence.

## Status

Status: computation.

Verification: tied to the 2026 preprint and locally reproducible from the
packaged appendix listings.

Related paper: Graham Hawkes, "Dyck Symmetric Functions and Applications to
q,t-Catalan Polynomials", arXiv:2605.13003, posted May 13, 2026,
https://arxiv.org/abs/2605.13003.

## Provenance

Source repository: `Dyck`

Source paths:

- `../Dyck/paper/working_drafts/arxiv_submission.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/appendix_a_code.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_local_proofs.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_lemma_525.tex`

Transfer type: appendix listings are copied exactly from the paper source.

## Layers

Python layer: present and reproducible.

LaTeX layer: present.

HTML layer: present.

## Included Computations

- Appendix A core Dyck-sequence routines.
- Appendix A lower-half string-generation routine.
- Appendix B residual finite checker for the small local-proof range.
- Appendix B seven-window checker for the East7/West7 local move.
- Appendix B finite checkers used in the proof of Lemma 5.25.

## Reproducibility

Run the Appendix B checkers from `code/`:

````text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
````

The successful runs end with `EverythingOkay = True`,
`SUCCESS: East7/West7 seven-window verification passed.`, or `status: PASS`,
as appropriate.

## Review And Routing

- Software/computation review: completed for packaging-level reproducibility;
  all packaged Appendix B checkers were run successfully on June 13, 2026.
- Mathematical accuracy review: the item mirrors finite checks from the
  preprint appendices. A future independent review should compare the curated
  explanation against the final published version if the preprint changes.
- Pedagogy/exposition review: the explanation file has been rewritten as an
  explanatory note rather than a transfer ledger. Future work should add
  examples or diagrams only if the item is expanded beyond appendix packaging.
```

### `items/dyck_symmetric_functions/assets/.gitkeep`

```text

```

### `items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 102145
sha256: 8d81d52b5b86f1b5e7de0d042a2cefc16bbd9f1e63acff14f44a849f9ef824f5
```

### `items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-81.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1732
sha256: ed560e434486ee0888f9a2b03c72ef72bc54ba7c7c344393c352ca71d06c98e6
```

### `items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 98466
sha256: 79442eeddd10eb9769de50767200e9645ec25922b31bb8689da5dc564d31c86c
```

### `items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-84.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1738
sha256: 2e7a95962b64dda07e3ec4937ba05175b9abb3285817bec9ce46855508cd9f23
```

### `items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 112565
sha256: be9ef8051f34d27b93a21c212d16263ad7780cab823c2583b4bd438ccf943167
```

### `items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization._jit_group_word_records-85.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1738
sha256: f5738e83ec6a4759cd111fa83482e862b81e34495f3fb1183a7073b8c786d0e3
```

### `items/dyck_symmetric_functions/code/__pycache__/check_rational_dyck_generalization.cpython-314.pyc`

```text
[binary artifact not expanded]
size_bytes: 41219
sha256: ba3d6aeda90c332d70115f91c52085e6300a47e61a24b3cbb69b7a53cfc2c508
```

### `items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 67829
sha256: 09b4fb597183459b543cae8482ff344a8b880e301a4b836419332ee0e99a3adc
```

### `items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.2.nbc`

```text
[binary artifact not expanded]
size_bytes: 65598
sha256: 723d39ef3b4c2899381b3cccdb2e0c80eb7ff267974f7d7b8060e3a2c105aea9
```

### `items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_extend-44.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 3336
sha256: 2bb1e664d7f1a5e45b809e77cb27a637391b1b5c6fe52c490ce037e8a9125e45
```

### `items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.1.nbc`

```text
[binary artifact not expanded]
size_bytes: 81251
sha256: 03fee1b31b3fe09326696cff0308263e5ed3255db49aeb66507e2e4aad9ccf25
```

### `items/dyck_symmetric_functions/code/__pycache__/random_rational_dyck_checks._jit_class_word_mask_counts-109.py314.nbi`

```text
[binary artifact not expanded]
size_bytes: 1692
sha256: 09302bc46af31b781b8afb694d86e279680a59886532e936f50ac41cab322b50
```

### `items/dyck_symmetric_functions/code/check_rational_dyck_generalization.py`

```python
"""Focused finite checks for the rational dual Dyck symmetric-function formula.

Input parameters are:

* ``t``: rational step;
* ``A``: alphabet size, using the alphabet ``{1, 2, ..., A}``;
* ``L``: maximum word length.

For every length ``1 <= l <= L`` the checker enumerates all words containing
``1``, groups them by multiset and rational dinv, verifies factor-length
symmetry across all positive compositions with the same underlying partition,
and compares the common factorization count with the Dyck-tableau Schur-side
prediction.
"""

from __future__ import annotations

import argparse
import os
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from multiprocessing import Pool
from typing import Iterable

try:
    import numpy as np
    from numba import njit, types
    from numba.typed import Dict
except ImportError:  # pragma: no cover - exercised only on minimal environments.
    np = None
    njit = None
    types = None
    Dict = None


Word = tuple[int, ...]
Composition = tuple[int, ...]
Partition = tuple[int, ...]
Shape = tuple[int, ...]
MultisetKey = int
PartitionMaskData = tuple[Partition, list[Composition], tuple[int, ...]]


@dataclass(frozen=True)
class CheckInput:
    step: int
    alphabet_size: int
    max_length: int
    workers: int = 0


@dataclass
class CheckResult:
    params: CheckInput
    words_generated: int = 0
    words_kept: int = 0
    multisets_checked: int = 0
    dinv_classes_checked: int = 0
    partition_classes_checked: int = 0
    compositions_checked: int = 0
    tableaux_checked: int = 0
    elapsed_seconds: float = 0.0


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dinv_pair(left: int, right: int, *, step: int) -> int:
    if left <= right:
        return max(0, left + step - right)
    return max(0, right + 1 + step - left)


def pair_dinv_table(params: CheckInput) -> tuple[tuple[int, ...], ...]:
    values = range(1, params.alphabet_size + 1)
    return tuple(tuple(dinv_pair(a, b, step=params.step) for b in values) for a in values)


if njit is not None:
    JIT_WORD_RECORD_KEY = types.UniTuple(types.uint64, 3)

    @njit(cache=True)
    def _jit_group_word_records(
        length: int,
        alphabet_size: int,
        pair_dinv_array: np.ndarray,
        base_powers: np.ndarray,
        dinv_limit: int,
        step: int,
        start_word: int,
        stop_word: int,
    ) -> tuple[np.ndarray, np.ndarray, int]:
        counts = np.empty(alphabet_size, dtype=np.int64)
        word = np.empty(length, dtype=np.int64)
        grouped = Dict.empty(key_type=JIT_WORD_RECORD_KEY, value_type=types.int64)
        words_kept = 0

        for encoded_word in range(start_word, stop_word):
            remaining = encoded_word
            has_one = False
            for position in range(length - 1, -1, -1):
                value_index = remaining % alphabet_size
                remaining //= alphabet_size
                word[position] = value_index
                if value_index == 0:
                    has_one = True
            if not has_one:
                continue

            for value_index in range(alphabet_size):
                counts[value_index] = 0

            dinv = 0
            required_dual_cuts = 0
            multiset_key = np.uint64(0)
            previous_index = 0
            for position in range(length):
                value_index = word[position]
                for earlier_index in range(alphabet_size):
                    dinv += counts[earlier_index] * pair_dinv_array[earlier_index, value_index]
                if position > 0:
                    if value_index <= previous_index + step:
                        required_dual_cuts |= 1 << (position - 1)
                previous_index = value_index
                counts[value_index] += 1
                multiset_key += base_powers[value_index]

            record_key = (multiset_key, np.uint64(dinv), np.uint64(required_dual_cuts))
            grouped[record_key] = grouped.get(record_key, 0) + 1
            words_kept += 1

        keys = np.empty((len(grouped), 3), dtype=np.uint64)
        values = np.empty(len(grouped), dtype=np.int64)
        index = 0
        for key, value in grouped.items():
            keys[index, 0] = key[0]
            keys[index, 1] = key[1]
            keys[index, 2] = key[2]
            values[index] = value
            index += 1
        return keys, values, words_kept

else:
    JIT_WORD_RECORD_KEY = None
    _jit_group_word_records = None


def effective_word_group_workers(params: CheckInput, *, length: int, words_generated: int) -> int:
    if _jit_group_word_records is None:
        return 1
    if params.workers < 0:
        raise AssertionError("workers must be non-negative")
    if params.workers > 0:
        return params.workers
    configured = os.environ.get("DYCK_CHECK_WORKERS")
    if configured:
        workers = int(configured)
        require(workers > 0, "DYCK_CHECK_WORKERS must be positive")
        return workers
    if words_generated < 50_000_000:
        return 1
    return min(os.cpu_count() or 1, 8)


def _jit_group_word_records_worker(
    args: tuple[int, int, tuple[tuple[int, ...], ...], int, int, int, int],
) -> tuple[np.ndarray, np.ndarray, int]:
    length, alphabet_size, pair_dinv, dinv_limit, step, start_word, stop_word = args
    base_powers = np.array([(length + 1) ** index for index in range(alphabet_size)], dtype=np.uint64)
    pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
    return _jit_group_word_records(
        length,
        alphabet_size,
        pair_dinv_array,
        base_powers,
        dinv_limit,
        step,
        start_word,
        stop_word,
    )


def partition_shapes(total_size: int) -> Iterable[Shape]:
    def rec(remaining: int, max_part: int, prefix: list[int]) -> Iterable[Shape]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for part in range(min(remaining, max_part), 0, -1):
            prefix.append(part)
            yield from rec(remaining - part, part, prefix)
            prefix.pop()

    yield from rec(total_size, total_size, [])


def positive_compositions(total: int) -> list[Composition]:
    if total <= 0:
        return []
    out: list[Composition] = []

    def rec(remaining: int, prefix: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for part in range(1, remaining + 1):
            prefix.append(part)
            rec(remaining - part, prefix)
            prefix.pop()

    rec(total, [])
    return out


def underlying_partition(composition: Composition) -> Partition:
    return tuple(sorted(composition, reverse=True))


def composition_cut_mask(composition: Composition) -> int:
    mask = 0
    position = 0
    total = sum(composition)
    for part in composition[:-1]:
        position += part
        if 0 < position < total:
            mask |= 1 << (position - 1)
    return mask


def composition_groups(length: int) -> list[PartitionMaskData]:
    grouped: defaultdict[Partition, list[tuple[Composition, int]]] = defaultdict(list)
    for composition in positive_compositions(length):
        grouped[underlying_partition(composition)].append((composition, composition_cut_mask(composition)))
    out: list[PartitionMaskData] = []
    for partition, values in grouped.items():
        compositions = [composition for composition, _cut_mask in values]
        cut_masks = tuple(cut_mask for _composition, cut_mask in values)
        out.append((partition, compositions, cut_masks))
    return out


def multiset_from_key(key: MultisetKey, *, alphabet_size: int, length: int) -> Word:
    base = length + 1
    values: list[int] = []
    for index in range(1, alphabet_size + 1):
        multiplicity = key % base
        key //= base
        values.extend([index] * multiplicity)
    return tuple(values)


def group_words_for_length(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> tuple[dict[MultisetKey, dict[int, Counter[int]]], int, int]:
    if _jit_group_word_records is not None:
        return group_words_for_length_jit(length, params=params, pair_dinv=pair_dinv)

    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
    words_generated = params.alphabet_size**length
    words_kept = 0
    base_powers = tuple((length + 1) ** index for index in range(params.alphabet_size))

    for first_one_position in range(length):
        counts = [0] * params.alphabet_size
        active_indices: list[int] = []

        def extend(
            position: int,
            previous_index: int,
            dinv: int,
            required_dual_cuts: int,
            multiset_key: int,
        ) -> None:
            nonlocal words_kept
            if position == length:
                grouped[multiset_key][dinv][required_dual_cuts] += 1
                words_kept += 1
                return

            if position < first_one_position:
                choices = range(1, params.alphabet_size)
            elif position == first_one_position:
                choices = range(1)
            else:
                choices = range(params.alphabet_size)

            for value_index in choices:
                dinv_increment = 0
                for earlier_index in active_indices:
                    dinv_increment += counts[earlier_index] * pair_dinv[earlier_index][value_index]
                next_required_dual_cuts = required_dual_cuts
                if position > 0:
                    previous_value = previous_index + 1
                    current_value = value_index + 1
                    if current_value <= previous_value + params.step:
                        next_required_dual_cuts |= 1 << (position - 1)
                first_value = counts[value_index] == 0
                if first_value:
                    active_indices.append(value_index)
                counts[value_index] += 1
                extend(
                    position + 1,
                    value_index,
                    dinv + dinv_increment,
                    next_required_dual_cuts,
                    multiset_key + base_powers[value_index],
                )
                counts[value_index] -= 1
                if first_value:
                    active_indices.pop()

        extend(0, 0, 0, 0, 0)

    expected_kept = words_generated - (params.alphabet_size - 1) ** length
    require(words_kept == expected_kept, f"internal word-count mismatch for length {length}")
    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}, words_generated, words_kept


def group_words_for_length_jit(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> tuple[dict[MultisetKey, dict[int, Counter[int]]], int, int]:
    require(np is not None, "NumPy is required for the JIT word-grouping backend")
    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
    words_generated = params.alphabet_size**length
    max_pair_dinv = max(max(row) for row in pair_dinv)
    dinv_limit = max_pair_dinv * length * (length - 1) // 2 + 1
    base_powers = np.array([(length + 1) ** index for index in range(params.alphabet_size)], dtype=np.uint64)
    pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
    workers = effective_word_group_workers(params, length=length, words_generated=words_generated)

    encoded_counts: dict[tuple[int, int, int], int] = {}
    words_kept = 0
    if workers == 1:
        record_batches = [
            _jit_group_word_records(
                length,
                params.alphabet_size,
                pair_dinv_array,
                base_powers,
                dinv_limit,
                params.step,
                0,
                words_generated,
            )
        ]
    else:
        chunk_size = (words_generated + workers - 1) // workers
        jobs = []
        for worker_index in range(workers):
            start_word = worker_index * chunk_size
            stop_word = min(words_generated, start_word + chunk_size)
            if start_word < stop_word:
                jobs.append(
                    (length, params.alphabet_size, pair_dinv, dinv_limit, params.step, start_word, stop_word)
                )
        with Pool(processes=len(jobs)) as pool:
            record_batches = pool.map(_jit_group_word_records_worker, jobs)

    for encoded_keys, multiplicities, batch_words_kept in record_batches:
        words_kept += batch_words_kept
        for index, multiplicity in enumerate(multiplicities):
            key = (int(encoded_keys[index, 0]), int(encoded_keys[index, 1]), int(encoded_keys[index, 2]))
            encoded_counts[key] = encoded_counts.get(key, 0) + int(multiplicity)

    for (multiset_key, dinv, required_dual_cuts), multiplicity in encoded_counts.items():
        grouped[multiset_key][dinv][required_dual_cuts] = multiplicity

    expected_kept = words_generated - (params.alphabet_size - 1) ** length
    require(words_kept == expected_kept, f"internal word-count mismatch for length {length}")
    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}, words_generated, words_kept


def tableau_shape_groups_for_length(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> dict[MultisetKey, dict[int, Counter[Shape]]]:
    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[Shape]]] = defaultdict(lambda: defaultdict(Counter))
    base_powers = tuple((length + 1) ** index for index in range(params.alphabet_size))

    for shape in partition_shapes(length):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(row_length)] for row_length in shape]
        for first_one_cell_index in range(length):
            counts = [0] * params.alphabet_size
            active_indices: list[int] = []

            def fill(cell_index: int, dinv: int, multiset_key: int) -> None:
                if cell_index == len(cells):
                    grouped[multiset_key][dinv][shape] += 1
                    return

                row, col = cells[cell_index]
                lower = 1
                if col > 0:
                    lower = rows[row][col - 1] + params.step + 1
                upper = params.alphabet_size
                if row + 1 < len(shape) and col < shape[row + 1]:
                    upper = min(upper, rows[row + 1][col] + params.step)

                if cell_index < first_one_cell_index:
                    lower = max(lower, 2)
                    values = range(lower, upper + 1)
                elif cell_index == first_one_cell_index:
                    if lower > 1 or upper < 1:
                        return
                    values = (1,)
                else:
                    values = range(lower, upper + 1)

                for value in values:
                    value_index = value - 1
                    dinv_increment = 0
                    for earlier_index in active_indices:
                        dinv_increment += counts[earlier_index] * pair_dinv[earlier_index][value_index]
                    rows[row][col] = value
                    first_value = counts[value_index] == 0
                    if first_value:
                        active_indices.append(value_index)
                    counts[value_index] += 1
                    fill(cell_index + 1, dinv + dinv_increment, multiset_key + base_powers[value_index])
                    counts[value_index] -= 1
                    if first_value:
                        active_indices.pop()
                    rows[row][col] = 0

            fill(0, 0, 0)

    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}


def count_ssyt_with_content(shape: Shape, content: Partition) -> int:
    """Return the Kostka number for ``shape`` and dominant content ``content``."""

    if sum(shape) != sum(content):
        return 0
    alphabet_size = len(content)
    if not shape:
        return 1 if not content else 0
    remaining = list(content)
    cells = [(row, col) for row, length in enumerate(shape) for col in range(length)]
    rows = [[-1 for _ in range(length)] for length in shape]
    total = 0

    def rec(cell_index: int) -> None:
        nonlocal total
        if cell_index == len(cells):
            total += 1
            return
        row, col = cells[cell_index]
        min_value = 0
        if col > 0:
            min_value = max(min_value, rows[row][col - 1])
        if row > 0 and col < shape[row - 1]:
            min_value = max(min_value, rows[row - 1][col] + 1)
        for value in range(min_value, alphabet_size):
            if remaining[value] == 0:
                continue
            remaining[value] -= 1
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = -1
            remaining[value] += 1

    rec(0)
    return total


def dyck_tableau_prediction(
    shape_counts: Counter[Shape],
    partition: Partition,
    *,
    ssyt_cache: dict[tuple[Shape, Partition], int],
) -> int:
    total = 0
    for shape, tableau_count in shape_counts.items():
        key = (shape, partition)
        if key not in ssyt_cache:
            ssyt_cache[key] = count_ssyt_with_content(shape, partition)
        total += tableau_count * ssyt_cache[key]
    return total


def dyck_tableau_predictions(
    shape_counts: Counter[Shape],
    partitions: list[PartitionMaskData],
    *,
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> list[int]:
    if not shape_counts:
        return [0] * len(partitions)
    cache_key = tuple(sorted(shape_counts.items()))
    if cache_key in prediction_cache:
        return prediction_cache[cache_key]
    out = [0] * len(partitions)
    for shape, tableau_count in shape_counts.items():
        for index, (partition, _compositions, _cut_masks) in enumerate(partitions):
            key = (shape, partition)
            if key not in ssyt_cache:
                ssyt_cache[key] = count_ssyt_with_content(shape, partition)
            out[index] += tableau_count * ssyt_cache[key]
    prediction_cache[cache_key] = out
    return out


def valid_factorization_count(mask_counts: Counter[int], cut_mask: int) -> int:
    total = 0
    for required_mask, multiplicity in mask_counts.items():
        if required_mask & ~cut_mask == 0:
            total += multiplicity
    return total


def valid_factorization_counts_by_cut_mask(mask_counts: Counter[int], *, length: int) -> list[int]:
    """Return counts for every cut mask by subset zeta transform."""

    mask_count = 1 << max(0, length - 1)
    counts = [0] * mask_count
    for required_mask, multiplicity in mask_counts.items():
        counts[required_mask] = multiplicity
    for bit in range(max(0, length - 1)):
        bit_mask = 1 << bit
        for mask in range(mask_count):
            if mask & bit_mask:
                counts[mask] += counts[mask ^ bit_mask]
    return counts


def cached_valid_factorization_counts_by_cut_mask(
    mask_counts: Counter[int],
    *,
    length: int,
    cache: dict[tuple[int, tuple[tuple[int, int], ...]], list[int]],
) -> list[int]:
    cache_key = (length, tuple(mask_counts.items()))
    if cache_key not in cache:
        cache[cache_key] = valid_factorization_counts_by_cut_mask(mask_counts, length=length)
    return cache[cache_key]


def check_partition_class(
    *,
    params: CheckInput,
    multiset: Word,
    dinv: int,
    partition: Partition,
    compositions: list[Composition],
    cut_masks: tuple[int, ...],
    valid_by_cut_mask: list[int],
    predicted: int,
) -> int:
    actual = valid_by_cut_mask[cut_masks[0]]
    for index in range(1, len(cut_masks)):
        if valid_by_cut_mask[cut_masks[index]] != actual:
            values = {
                composition: valid_by_cut_mask[cut_mask]
                for composition, cut_mask in zip(compositions, cut_masks)
            }
            examples = sorted(values.items())[:8]
            raise AssertionError(
                "factorization symmetry mismatch: "
                f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                f"partition={partition}, examples={examples}"
            )
    if actual != predicted:
        values = {
            composition: valid_by_cut_mask[cut_mask]
            for composition, cut_mask in zip(compositions, cut_masks)
        }
        examples = sorted(values.items())[:8]
        raise AssertionError(
            "Dyck-tableau prediction mismatch: "
            f"t={params.step}, multiset={multiset}, dinv={dinv}, "
            f"partition={partition}, factorization_count={actual}, "
            f"tableau_prediction={predicted}, examples={examples}"
        )
    return len(compositions)


def run_check(params: CheckInput) -> CheckResult:
    require(params.step >= 0, "t must be non-negative")
    require(params.alphabet_size > 0, "alphabet size A must be positive")
    require(params.max_length > 0, "max length L must be positive")

    start = time.perf_counter()
    result = CheckResult(params=params)
    pair_dinv = pair_dinv_table(params)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    valid_cut_mask_cache: dict[tuple[int, tuple[tuple[int, int], ...]], list[int]] = {}

    for length in range(1, params.max_length + 1):
        length_start = time.perf_counter()
        word_groups, words_generated, words_kept = group_words_for_length(
            length,
            params=params,
            pair_dinv=pair_dinv,
        )
        tableau_groups = tableau_shape_groups_for_length(
            length,
            params=params,
            pair_dinv=pair_dinv,
        )
        partitions = composition_groups(length)
        result.words_generated += words_generated
        result.words_kept += words_kept

        length_multisets = 0
        length_dinv_classes = 0
        length_partition_classes = 0
        for key in sorted(set(word_groups) | set(tableau_groups)):
            multiset = multiset_from_key(key, alphabet_size=params.alphabet_size, length=length)
            words_by_dinv = word_groups.get(key, {})
            tableaux_by_dinv = tableau_groups.get(key, {})
            length_multisets += 1
            for dinv in sorted(set(words_by_dinv) | set(tableaux_by_dinv)):
                length_dinv_classes += 1
                mask_counts = words_by_dinv.get(dinv, Counter())
                valid_by_cut_mask = cached_valid_factorization_counts_by_cut_mask(
                    mask_counts,
                    length=length,
                    cache=valid_cut_mask_cache,
                )
                shape_counts = tableaux_by_dinv.get(dinv, Counter())
                result.tableaux_checked += sum(shape_counts.values())
                predictions = dyck_tableau_predictions(
                    shape_counts,
                    partitions,
                    ssyt_cache=ssyt_cache,
                    prediction_cache=prediction_cache,
                )
                for partition_index, (partition, compositions, cut_masks) in enumerate(partitions):
                    actual = valid_by_cut_mask[cut_masks[0]]
                    for cut_mask in cut_masks[1:]:
                        if valid_by_cut_mask[cut_mask] != actual:
                            values = {
                                composition: valid_by_cut_mask[composition_cut_mask]
                                for composition, composition_cut_mask in zip(compositions, cut_masks)
                            }
                            examples = sorted(values.items())[:8]
                            raise AssertionError(
                                "factorization symmetry mismatch: "
                                f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                                f"partition={partition}, examples={examples}"
                            )
                    predicted = predictions[partition_index]
                    if actual != predicted:
                        values = {
                            composition: valid_by_cut_mask[composition_cut_mask]
                            for composition, composition_cut_mask in zip(compositions, cut_masks)
                        }
                        examples = sorted(values.items())[:8]
                        raise AssertionError(
                            "Dyck-tableau prediction mismatch: "
                            f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                            f"partition={partition}, factorization_count={actual}, "
                            f"tableau_prediction={predicted}, examples={examples}"
                        )
                    result.compositions_checked += len(compositions)
                    length_partition_classes += 1

        result.multisets_checked += length_multisets
        result.dinv_classes_checked += length_dinv_classes
        result.partition_classes_checked += length_partition_classes
        print(
            f"  length={length}: generated={words_generated}, kept={words_kept}, "
            f"multisets={length_multisets}, dinv classes={length_dinv_classes}, "
            f"partitions={length_partition_classes}, elapsed={time.perf_counter() - length_start:.3f}s",
            flush=True,
        )

    result.elapsed_seconds = time.perf_counter() - start
    return result


def print_result(result: CheckResult) -> None:
    params = result.params
    print(f"completed: t={params.step}, alphabet={{1,...,{params.alphabet_size}}}, lengths<= {params.max_length}")
    print(f"  words generated: {result.words_generated}")
    print(f"  1-containing words checked: {result.words_kept}")
    print(f"  multisets checked: {result.multisets_checked}")
    print(f"  dinv classes checked: {result.dinv_classes_checked}")
    print(f"  partition classes checked: {result.partition_classes_checked}")
    print(f"  positive compositions checked: {result.compositions_checked}")
    print(f"  Dyck tableaux checked: {result.tableaux_checked}")
    print(f"  elapsed: {result.elapsed_seconds:.3f}s")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, required=True, help="Rational step t.")
    parser.add_argument("--alphabet-size", "-A", type=int, required=True, help="Alphabet size A.")
    parser.add_argument("--max-length", "-L", type=int, required=True, help="Maximum word length L.")
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Word-grouping worker processes. Use 0 for automatic selection.",
    )
    args = parser.parse_args()

    result = run_check(
        CheckInput(
            step=args.t,
            alphabet_size=args.alphabet_size,
            max_length=args.max_length,
            workers=args.workers,
        )
    )
    print_result(result)
    print("all requested finite checks passed")


if __name__ == "__main__":
    main()
```

### `items/dyck_symmetric_functions/code/classical_insertion_demo.py`

```python
"""Small trace for the classical dual Dyck insertion algorithm."""

from __future__ import annotations

from paper_algorithms import is_dyck_tableau, rowsert, tabsert


def main() -> None:
    row = [0, 3, 6]
    inserted = [1, 4]
    row_steps = []
    evicted, new_row = rowsert(row, inserted, trace=row_steps)

    print("rowsert example")
    print(f"  row: {row}")
    print(f"  inserted row: {inserted}")
    print(f"  evicted row: {evicted}")
    print(f"  output row: {new_row}")
    for index, step in enumerate(row_steps, 1):
        print(f"  step {index}: {step}")

    tableau = [[0, 3], [1, 4]]
    inserted_row = [2, 5]
    output, traces = tabsert(tableau, inserted_row, trace=True)

    print()
    print("tabsert example")
    print(f"  tableau: {tableau}")
    print(f"  inserted row: {inserted_row}")
    print(f"  output: {output}")
    print(f"  valid Dyck tableau: {is_dyck_tableau(output)}")
    for trace in traces:
        print(f"  row {trace.row_index}: inserted {trace.inserted_row}, evicted {trace.evicted_row}")


if __name__ == "__main__":
    main()
```

### `items/dyck_symmetric_functions/code/paper_algorithms/__init__.py`

```python
"""Minimal algorithm package for the Dyck symmetric functions item."""

from .rational_dyck import (
    conjugate_partition,
    enumerate_rational_dyck_tableaux,
    is_rational_affine_dyck,
    is_rational_dual_dyck,
    is_rational_dyck_tableau,
    rational_affine_factorization_polynomial,
    rational_dual_factorization_polynomial,
    rational_dinv,
    rational_row_reading_word,
    schur_sum_from_tableau_shapes,
    shape_counts,
    unique_multiset_permutations,
)
from .row_insertion import RowsertStep, is_dual_dyck, rowsert
from .tableau_insertion import TabsertRowTrace, is_dyck_tableau, tabsert

__all__ = [
    "RowsertStep",
    "TabsertRowTrace",
    "conjugate_partition",
    "enumerate_rational_dyck_tableaux",
    "is_dual_dyck",
    "is_dyck_tableau",
    "is_rational_affine_dyck",
    "is_rational_dual_dyck",
    "is_rational_dyck_tableau",
    "rational_affine_factorization_polynomial",
    "rational_dual_factorization_polynomial",
    "rational_dinv",
    "rational_row_reading_word",
    "rowsert",
    "schur_sum_from_tableau_shapes",
    "shape_counts",
    "tabsert",
    "unique_multiset_permutations",
]
```

### `items/dyck_symmetric_functions/code/paper_algorithms/rational_dyck.py`

```python
"""Finite helpers for the ``r = ms + 1`` rational Dyck generalization."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb
from typing import Iterable, Sequence

from .ssyt import Shape, SSYT, enumerate_ssyt, is_partition_shape, schur_polynomial_by_ssyt, ssyt_weight


SequenceWord = tuple[int, ...]
Tableau = tuple[tuple[int, ...], ...]
Weight = tuple[int, ...]


def _check_m(m: int) -> None:
    if not isinstance(m, int) or m < 0:
        raise ValueError("m must be a non-negative integer")


def rational_dinv(sequence: Sequence[int], *, m: int) -> int:
    """Return the rational dinv statistic for an integer sequence."""

    _check_m(m)
    values = tuple(sequence)
    total = 0
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            if left <= right:
                total += max(0, left + m - right)
            else:
                total += max(0, right + 1 + m - left)
    return total


def is_rational_affine_dyck(sequence: Sequence[int], *, m: int) -> bool:
    """Check ``x[i+1] <= x[i] + m``."""

    _check_m(m)
    values = tuple(sequence)
    return all(isinstance(value, int) for value in values) and all(
        values[index + 1] <= values[index] + m for index in range(len(values) - 1)
    )


def is_rational_dual_dyck(sequence: Sequence[int], *, m: int) -> bool:
    """Check ``x[i+1] > x[i] + m``."""

    _check_m(m)
    values = tuple(sequence)
    return all(isinstance(value, int) for value in values) and all(
        values[index + 1] > values[index] + m for index in range(len(values) - 1)
    )


def generate_rational_dyck_sequences(length: int, *, step: int) -> list[SequenceWord]:
    """Generate normalized ``step``-affine Dyck sequences of fixed length."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")

    out: list[SequenceWord] = []

    def rec(prefix: list[int]) -> None:
        if len(prefix) == length:
            out.append(tuple(prefix))
            return
        previous = prefix[-1]
        # Nonnegativity and the initial zero make this finite; the largest
        # possible next entry is obtained by taking the maximum allowed step.
        for value in range(previous + step + 1):
            prefix.append(value)
            rec(prefix)
            prefix.pop()

    rec([0])
    return out


def is_normalized_rational_dyck_sequence(sequence: Sequence[int], *, step: int) -> bool:
    """Check the normalized rational Dyck sequence convention."""

    _check_m(step)
    values = tuple(sequence)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and is_rational_affine_dyck(values, m=step)
    )


def find_rational_extractable_position(
    sequence: Sequence[int],
    *,
    step: int,
    include_final: bool = True,
) -> int | None:
    """Return the leftmost generalized extractable position, if any."""

    _check_m(step)
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        raise ValueError("sequence must be a normalized rational Dyck sequence")
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = sum(1 for prior in values[:index] if lower <= prior <= value - 1)
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + step:
            continue
        return index
    return None


def is_rational_m_skeleton(sequence: Sequence[int], *, step: int, ambient: int | None = None) -> bool:
    """Check the generalized ``[0,m]`` skeleton condition."""

    _check_m(step)
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    endpoint = values[-1] if ambient is None else ambient
    return (
        endpoint >= 0
        and max(values) == endpoint
        and values[-1] == endpoint
        and find_rational_extractable_position(values, step=step, include_final=False) is None
    )


def rational_max_total_degree(length: int, *, step: int) -> int:
    """Return the conjectural top total degree for ``r = length*step + 1``."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    return step * comb(length, 2)


def rational_deficit(sequence: Sequence[int], *, step: int) -> int:
    """Return ``M - area - dinv`` with ``M = step*binom(length, 2)``."""

    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        raise ValueError("sequence must be a normalized rational Dyck sequence")
    return rational_max_total_degree(len(values), step=step) - sum(values) - rational_dinv(values, m=step)


def excluded_rational_full_skeleton(length: int, *, step: int) -> SequenceWord:
    """Return ``(0,0,1,0,...,0,step)``."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    if length < 4:
        raise ValueError("the excluded skeleton is only defined for length at least 4")
    return (0, 0, 1) + (0,) * (length - 4) + (step,)


def is_rational_full_skeleton(sequence: Sequence[int], *, step: int) -> bool:
    """Check the generalized full skeleton condition."""

    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    return find_rational_extractable_position(values, step=step, include_final=True) is None


def is_rational_special_skeleton(sequence: Sequence[int], *, step: int) -> bool:
    """Check full skeleton status, excluding ``(0,0,1,0,...,0,1)``."""

    values = tuple(sequence)
    if not is_rational_full_skeleton(values, step=step):
        return False
    if len(values) < 4:
        return True
    return values != excluded_rational_full_skeleton(len(values), step=step)


def unique_multiset_permutations(values: Iterable[int]) -> Iterable[SequenceWord]:
    """Yield distinct permutations of a finite multiset in lexicographic order."""

    counts = Counter(values)
    if any(not isinstance(value, int) for value in counts):
        raise ValueError("values must be integers")

    def rec(prefix: list[int], remaining: int) -> Iterable[SequenceWord]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for value in sorted(counts):
            if counts[value] == 0:
                continue
            counts[value] -= 1
            prefix.append(value)
            yield from rec(prefix, remaining - 1)
            prefix.pop()
            counts[value] += 1

    yield from rec([], sum(counts.values()))


def rational_affine_factorization_polynomial(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int,
    variable_count: int,
) -> Counter[Weight]:
    """Count affine factorizations by factor lengths.

    The output coefficient of ``(a0, ..., ak)`` counts ordered factorizations
    into ``variable_count`` possibly empty consecutive factors with lengths
    ``a0, ..., ak`` whose concatenation has the requested rational dinv.
    """

    _check_m(m)
    if not isinstance(target_dinv, int) or target_dinv < 0:
        raise ValueError("target_dinv must be a non-negative integer")
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    values_tuple = tuple(values)
    polynomial: Counter[Weight] = Counter()
    length = len(values_tuple)

    def cut_rec(start: int, factors_left: int, cuts: list[int], sequence: SequenceWord) -> None:
        if factors_left == 1:
            parts = cuts + [length]
            previous = 0
            factor_lengths: list[int] = []
            for stop in parts:
                factor = sequence[previous:stop]
                if not is_rational_affine_dyck(factor, m=m):
                    return
                factor_lengths.append(len(factor))
                previous = stop
            polynomial[tuple(factor_lengths)] += 1
            return
        for stop in range(start, length + 1):
            cut_rec(stop, factors_left - 1, cuts + [stop], sequence)

    for sequence in unique_multiset_permutations(values_tuple):
        if rational_dinv(sequence, m=m) == target_dinv:
            cut_rec(0, variable_count, [], sequence)
    return polynomial


def rational_dual_factorization_polynomial(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int,
    variable_count: int,
) -> Counter[Weight]:
    """Count dual factorizations by factor lengths."""

    _check_m(m)
    if not isinstance(target_dinv, int) or target_dinv < 0:
        raise ValueError("target_dinv must be a non-negative integer")
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    values_tuple = tuple(values)
    polynomial: Counter[Weight] = Counter()
    length = len(values_tuple)

    def cut_rec(start: int, factors_left: int, cuts: list[int], sequence: SequenceWord) -> None:
        if factors_left == 1:
            parts = cuts + [length]
            previous = 0
            factor_lengths: list[int] = []
            for stop in parts:
                factor = sequence[previous:stop]
                if not is_rational_dual_dyck(factor, m=m):
                    return
                factor_lengths.append(len(factor))
                previous = stop
            polynomial[tuple(factor_lengths)] += 1
            return
        for stop in range(start, length + 1):
            cut_rec(stop, factors_left - 1, cuts + [stop], sequence)

    for sequence in unique_multiset_permutations(values_tuple):
        if rational_dinv(sequence, m=m) == target_dinv:
            cut_rec(0, variable_count, [], sequence)
    return polynomial


def rational_row_reading_word(tableau: Sequence[Sequence[int]]) -> SequenceWord:
    """Read rows left-to-right, from bottom row to top row."""

    rows = tuple(tuple(row) for row in tableau)
    return tuple(value for row in reversed(rows) for value in row)


def rational_dyck_tableau_shape(tableau: Sequence[Sequence[int]]) -> Shape:
    return tuple(len(row) for row in tableau)


def is_rational_dyck_tableau(tableau: Sequence[Sequence[int]], *, m: int) -> bool:
    """Check the rational Dyck tableau conditions in top-to-bottom row order."""

    _check_m(m)
    rows = tuple(tuple(row) for row in tableau)
    shape = rational_dyck_tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    if any(not is_rational_dual_dyck(row, m=m) for row in rows):
        return False
    for row_index in range(len(rows) - 1):
        upper = rows[row_index]
        lower = rows[row_index + 1]
        for column in range(len(lower)):
            if upper[column] > lower[column] + m:
                return False
    return True


def enumerate_rational_dyck_tableaux(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int | None = None,
) -> list[Tableau]:
    """Enumerate rational Dyck tableaux with the requested multiset entries."""

    _check_m(m)
    values_tuple = tuple(values)
    if any(not isinstance(value, int) for value in values_tuple):
        raise ValueError("values must be integers")
    if target_dinv is not None and (not isinstance(target_dinv, int) or target_dinv < 0):
        raise ValueError("target_dinv must be a non-negative integer or None")

    out: list[Tableau] = []
    total_size = len(values_tuple)

    def partition_rec(remaining: int, max_part: int, prefix: list[int]) -> Iterable[Shape]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for part in range(min(remaining, max_part), 0, -1):
            prefix.append(part)
            yield from partition_rec(remaining - part, part, prefix)
            prefix.pop()

    for shape in partition_rec(total_size, total_size, []):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(length)] for length in shape]
        remaining = Counter(values_tuple)

        def valid_cell(row: int, col: int, value: int) -> bool:
            if col > 0 and value <= rows[row][col - 1] + m:
                return False
            if row + 1 < len(shape) and col < shape[row + 1]:
                if value > rows[row + 1][col] + m:
                    return False
            if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
                if rows[row - 1][col] > value + m:
                    return False
            return True

        def fill(cell_index: int) -> None:
            if cell_index == len(cells):
                tableau = tuple(tuple(row) for row in rows)
                if target_dinv is None or rational_dinv(rational_row_reading_word(tableau), m=m) == target_dinv:
                    out.append(tableau)
                return
            row, col = cells[cell_index]
            for value in sorted(remaining):
                if remaining[value] == 0 or not valid_cell(row, col, value):
                    continue
                rows[row][col] = value
                remaining[value] -= 1
                fill(cell_index + 1)
                remaining[value] += 1
                rows[row][col] = 0

        fill(0)
    return out


def shape_counts(tableaux: Iterable[Sequence[Sequence[int]]]) -> Counter[Shape]:
    return Counter(rational_dyck_tableau_shape(tableau) for tableau in tableaux)


def conjugate_partition(shape: Sequence[int]) -> Shape:
    shape_tuple = tuple(shape)
    if shape_tuple == ():
        return ()
    if not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition")
    return tuple(sum(1 for part in shape_tuple if part >= column) for column in range(1, shape_tuple[0] + 1))


def schur_sum_from_tableau_shapes(
    tableaux: Iterable[Sequence[Sequence[int]]],
    *,
    variable_count: int,
    conjugate_shapes: bool,
) -> Counter[Weight]:
    """Expand ``sum_P s_shape(P)`` or ``sum_P s_shape(P)'`` into monomials."""

    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")
    out: Counter[Weight] = Counter()
    for tableau in tableaux:
        shape = rational_dyck_tableau_shape(tableau)
        if conjugate_shapes:
            shape = conjugate_partition(shape)
        for weight, coefficient in schur_polynomial_by_ssyt(shape, alphabet_size=variable_count).items():
            out[weight] += coefficient
    return out


def partition_weights(total: int, *, max_parts: int) -> list[Weight]:
    if not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    if not isinstance(max_parts, int) or max_parts <= 0:
        raise ValueError("max_parts must be positive")
    out: list[Weight] = []

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if len(prefix) == max_parts:
            if remaining == 0:
                out.append(tuple(prefix))
            return
        slots_left = max_parts - len(prefix) - 1
        for part in range(min(remaining, max_part), -1, -1):
            prefix.append(part)
            rec(remaining - part, part, prefix)
            prefix.pop()

    rec(total, total, [])
    return out


def schur_expansion_from_monomial_symmetric(
    monomial_coefficients: Counter[Weight] | dict[Weight, int],
    *,
    variable_count: int,
) -> Counter[Shape]:
    """Convert a symmetric monomial dictionary to Schur coefficients.

    Keys are exponent partitions padded to ``variable_count`` parts, as in the
    monomial symmetric basis in that many variables.
    """

    if not monomial_coefficients:
        return Counter()
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    normalized: Counter[Weight] = Counter()
    total: int | None = None
    for weight, coefficient in monomial_coefficients.items():
        weight_tuple = tuple(weight)
        if len(weight_tuple) != variable_count:
            raise ValueError("all weights must have length variable_count")
        if any(part < 0 for part in weight_tuple) or tuple(sorted(weight_tuple, reverse=True)) != weight_tuple:
            raise ValueError("weights must be partitions padded with zeros")
        if total is None:
            total = sum(weight_tuple)
        elif sum(weight_tuple) != total:
            raise ValueError("all weights must have the same total degree")
        normalized[weight_tuple] += coefficient

    assert total is not None
    partitions = partition_weights(total, max_parts=variable_count)
    remaining = {partition: Fraction(normalized.get(partition, 0)) for partition in partitions}
    coefficients: Counter[Shape] = Counter()

    for shape in partitions:
        shape_no_zeros = tuple(part for part in shape if part)
        if len(shape_no_zeros) > variable_count:
            continue
        schur_terms = Counter(
            ssyt_weight(tableau, alphabet_size=variable_count)
            for tableau in enumerate_ssyt(shape_no_zeros, alphabet_size=variable_count)
        )
        coefficient = remaining[shape]
        if coefficient:
            if coefficient.denominator != 1:
                raise ValueError(f"non-integral Schur coefficient for shape {shape}: {coefficient}")
            coefficients[shape_no_zeros] = int(coefficient)
        for weight, kostka in schur_terms.items():
            if weight in remaining:
                remaining[weight] -= coefficient * kostka

    if any(value != 0 for value in remaining.values()):
        raise ValueError(f"monomial coefficients were not fully converted: {remaining}")
    return coefficients


def at_most_two_column_shapes(total_size: int) -> list[Shape]:
    """Return partition shapes of ``total_size`` with at most two columns."""

    if not isinstance(total_size, int) or total_size < 0:
        raise ValueError("total_size must be a non-negative integer")
    if total_size == 0:
        return [()]
    out: list[Shape] = []
    for two_cell_rows in range(total_size // 2, -1, -1):
        one_cell_rows = total_size - 2 * two_cell_rows
        shape = (2,) * two_cell_rows + (1,) * one_cell_rows
        out.append(shape)
    return out


def enumerate_bounded_rational_dyck_tableaux(
    shape: Sequence[int],
    *,
    step: int,
    max_entry: int,
) -> list[Tableau]:
    """Enumerate rational Dyck tableaux of a fixed shape and entry interval.

    Rows are in top-to-bottom order, entries lie in ``[0,max_entry]``, rows are
    rational dual Dyck sequences, and columns read bottom-to-top are rational
    affine Dyck sequences.
    """

    _check_m(step)
    if not isinstance(max_entry, int):
        raise ValueError("max_entry must be an integer")
    shape_tuple = tuple(shape)
    if shape_tuple == ():
        return [()]
    if not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition")
    if max_entry < 0:
        return []

    rows = [[0 for _ in range(length)] for length in shape_tuple]
    cells = [(row, col) for row in range(len(shape_tuple) - 1, -1, -1) for col in range(shape_tuple[row])]
    out: list[Tableau] = []

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape_tuple) and col < shape_tuple[row + 1]:
            if value > rows[row + 1][col] + step:
                return False
        if row > 0 and col < shape_tuple[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int) -> None:
        if cell_index == len(cells):
            out.append(tuple(tuple(row) for row in rows))
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = 0

    rec(0)
    return out


def rational_qt_catalan_direct_coefficients(length: int, *, step: int) -> Counter[tuple[int, int]]:
    """Direct ``q^area t^dinv`` coefficients from normalized rational Dyck words."""

    coeffs: Counter[tuple[int, int]] = Counter()
    for sequence in generate_rational_dyck_sequences(length, step=step):
        coeffs[(sum(sequence), rational_dinv(sequence, m=step))] += 1
    return coeffs


def rational_two_column_formula_coefficients(length: int, *, step: int) -> Counter[tuple[int, int]]:
    """Formula-side coefficients using rational skeletons and two-column tabs."""

    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    _check_m(step)

    coeffs: Counter[tuple[int, int]] = Counter()
    for skeleton_length in range(1, length + 1):
        tableau_size = length - skeleton_length
        for skeleton in generate_rational_dyck_sequences(skeleton_length, step=step):
            if not is_rational_m_skeleton(skeleton, step=step):
                continue
            ambient = skeleton[-1]
            for shape in at_most_two_column_shapes(tableau_size):
                for tableau in enumerate_bounded_rational_dyck_tableaux(
                    shape,
                    step=step,
                    max_entry=ambient - 1,
                ):
                    rr = rational_row_reading_word(tableau)
                    base = skeleton + rr
                    base_area = sum(base)
                    base_dinv = rational_dinv(base, m=step)
                    size = sum(shape)
                    schur_shape = conjugate_partition(shape)
                    for weight, multiplicity in schur_polynomial_by_ssyt(schur_shape, alphabet_size=2).items():
                        q_power, t_power = weight
                        coeffs[(base_area + q_power, base_dinv - size + t_power)] += multiplicity
    return coeffs


def rational_skeleton_string_formula_coefficients(
    length: int,
    *,
    step: int,
    max_deficit: int,
) -> Counter[tuple[int, int]]:
    """Expand the special-skeleton quotient formula in the rational setting."""

    if not isinstance(max_deficit, int) or max_deficit < 0:
        raise ValueError("max_deficit must be a non-negative integer")
    total_degree = rational_max_total_degree(length, step=step)
    coeffs: Counter[tuple[int, int]] = Counter()
    for sequence in generate_rational_dyck_sequences(length, step=step):
        if not is_rational_special_skeleton(sequence, step=step):
            continue
        deficit = rational_deficit(sequence, step=step)
        if deficit > max_deficit:
            continue
        area = sum(sequence)
        dinv = rational_dinv(sequence, m=step)
        if dinv >= area:
            for q_power in range(area, dinv + 1):
                coeffs[(q_power, total_degree - deficit - q_power)] += 1
        else:
            for q_power in range(dinv + 1, area):
                coeffs[(q_power, total_degree - deficit - q_power)] -= 1
    return coeffs
```

### `items/dyck_symmetric_functions/code/paper_algorithms/row_insertion.py`

```python
"""Section 3 row insertion algorithms.

The draft's "dual Dyck" rows are finite non-negative integer sequences whose
consecutive entries differ by at least +2.  The empty sequence is accepted:
the Section 3 rowsert definition explicitly allows empty input rows, and the
local gap condition is vacuous for length 0 and length 1.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal, Sequence


CaseName = Literal["case0", "case1", "case2", "case3"]


@dataclass(frozen=True)
class Chain:
    """A contiguous maximal +2-chain, using zero-based half-open indices."""

    start: int
    stop: int
    values: tuple[int, ...]

    @property
    def length(self) -> int:
        return self.stop - self.start


@dataclass(frozen=True)
class RowsertStep:
    case: CaseName
    f_chunk: tuple[int, ...]
    r_chunk: tuple[int, ...]
    index: int | None
    r_chain: Chain | None = None
    f_chain: Chain | None = None


@dataclass(frozen=True)
class WorsertStep:
    case: CaseName
    e_chunk: tuple[int, ...]
    r_chunk: tuple[int, ...]
    index: int | None
    r_chain: Chain | None = None
    e_chain: Chain | None = None


def is_dual_dyck(seq: Sequence[int]) -> bool:
    """Return whether ``seq`` satisfies the dual-Dyck step-gap condition."""

    return all(value >= 0 for value in seq) and all(
        seq[index + 1] >= seq[index] + 2 for index in range(len(seq) - 1)
    )


def _require_position(seq: Sequence[int], index: int) -> None:
    if not 0 <= index < len(seq):
        raise IndexError(f"position {index} is outside sequence of length {len(seq)}")


def maximal_plus2_chain_starting_at(seq: Sequence[int], index: int) -> Chain:
    """Return the maximal +2-chain starting at ``index``."""

    _require_position(seq, index)
    stop = index + 1
    while stop < len(seq) and seq[stop] == seq[stop - 1] + 2:
        stop += 1
    return Chain(index, stop, tuple(seq[index:stop]))


def maximal_plus2_chain_ending_at(seq: Sequence[int], index: int) -> Chain:
    """Return the maximal +2-chain ending at ``index``."""

    _require_position(seq, index)
    start = index
    while start > 0 and seq[start - 1] == seq[start] - 2:
        start -= 1
    return Chain(start, index + 1, tuple(seq[start : index + 1]))


def rowsert(
    r0: Sequence[int], f0: Sequence[int], *, trace: list[RowsertStep] | None = None
) -> tuple[list[int], list[int]]:
    """Apply the draft's row insertion operation.

    Inputs are copied on entry, so caller-owned lists are never mutated.  The
    returned pair is ``(E, R)``.
    """

    if not is_dual_dyck(r0):
        raise ValueError("r0 must be a dual Dyck sequence")
    if not is_dual_dyck(f0):
        raise ValueError("f0 must be a dual Dyck sequence")

    e: list[int] = []
    r = list(r0)
    f = list(f0)

    while f:
        first = f[0]
        index = next((idx for idx, value in enumerate(r) if first <= value + 1), None)

        if index is None:
            chunk = (first,)
            del f[:1]
            r.extend(chunk)
            if trace is not None:
                trace.append(RowsertStep("case0", chunk, (), None))
            continue

        if first <= r[index]:
            f_chunk = (first,)
            r_chunk = (r[index],)
            del f[:1]
            r[index] = first
            e.extend(r_chunk)
            if trace is not None:
                trace.append(RowsertStep("case1", f_chunk, r_chunk, index))
            continue

        r_chain = maximal_plus2_chain_starting_at(r, index)
        f_chain = maximal_plus2_chain_starting_at(f, 0)

        if r_chain.length <= f_chain.length:
            length = r_chain.length
            f_chunk = tuple(f[:length])
            r_chunk = tuple(r[index : index + length])
            del f[:length]
            r[index : index + length] = f_chunk
            e.extend(r_chunk)
            if trace is not None:
                trace.append(
                    RowsertStep("case2", f_chunk, r_chunk, index, r_chain, f_chain)
                )
        else:
            length = f_chain.length
            f_chunk = tuple(f[:length])
            del f[:length]
            e.extend(f_chunk)
            if trace is not None:
                trace.append(
                    RowsertStep("case3", f_chunk, (), index, r_chain, f_chain)
                )

    return e, r


def worsert(
    e0: Sequence[int], r0: Sequence[int], *, trace: list[WorsertStep] | None = None
) -> tuple[list[int], list[int]]:
    """Apply the corrected reverse row insertion operation.

    Inputs are copied on entry, so caller-owned lists are never mutated.  The
    returned pair is ``(R, F)``.  Case 0 follows the author clarification for
    CA-0001: the removed final element of ``E`` is prepended to ``R``, not
    ``F``.
    """

    if not is_dual_dyck(e0):
        raise ValueError("e0 must be a dual Dyck sequence")
    if not is_dual_dyck(r0):
        raise ValueError("r0 must be a dual Dyck sequence")

    e = list(e0)
    r = list(r0)
    f: list[int] = []

    while e:
        last = e[-1]
        index = next(
            (idx for idx in range(len(r) - 1, -1, -1) if last >= r[idx] - 1),
            None,
        )

        if index is None:
            chunk = (last,)
            del e[-1:]
            r[0:0] = chunk
            if trace is not None:
                trace.append(WorsertStep("case0", chunk, (), None))
            continue

        if last >= r[index]:
            e_chunk = (last,)
            r_chunk = (r[index],)
            del e[-1:]
            r[index] = last
            f[0:0] = r_chunk
            if trace is not None:
                trace.append(WorsertStep("case1", e_chunk, r_chunk, index))
            continue

        r_chain = maximal_plus2_chain_ending_at(r, index)
        e_chain = maximal_plus2_chain_ending_at(e, len(e) - 1)

        if r_chain.length <= e_chain.length:
            length = r_chain.length
            start = index - length + 1
            e_chunk = tuple(e[-length:])
            r_chunk = tuple(r[start : index + 1])
            del e[-length:]
            r[start : index + 1] = e_chunk
            f[0:0] = r_chunk
            if trace is not None:
                trace.append(
                    WorsertStep("case2", e_chunk, r_chunk, index, r_chain, e_chain)
                )
        else:
            length = e_chain.length
            e_chunk = tuple(e[-length:])
            del e[-length:]
            f[0:0] = e_chunk
            if trace is not None:
                trace.append(
                    WorsertStep("case3", e_chunk, (), index, r_chain, e_chain)
                )

    return r, f


def di_statistic(seq: Iterable[int]) -> int:
    """Count ordered pairs ``i < j`` with ``seq[i] = seq[j] + 1``."""

    values = list(seq)
    total = 0
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            if values[left] == values[right] + 1:
                total += 1
    return total
```

### `items/dyck_symmetric_functions/code/paper_algorithms/ssyt.py`

```python
"""Small semistandard Young tableau enumeration utilities.

Shapes are partitions in top-to-bottom row order.  SSYT entries use the
alphabet ``1, ..., alphabet_size`` by default, with rows weakly increasing and
columns strictly increasing from top to bottom.
"""

from __future__ import annotations

from collections import Counter
from typing import Iterable, Sequence


Shape = tuple[int, ...]
SSYT = tuple[tuple[int, ...], ...]
Weight = tuple[int, ...]


def is_partition_shape(shape: Sequence[int]) -> bool:
    values = tuple(shape)
    return all(isinstance(part, int) and part > 0 for part in values) and all(
        values[index] >= values[index + 1] for index in range(len(values) - 1)
    )


def partition_shapes(max_size: int, *, max_rows: int | None = None) -> list[Shape]:
    if not isinstance(max_size, int) or max_size < 0:
        raise ValueError("max_size must be a non-negative integer")
    if max_rows is not None and (not isinstance(max_rows, int) or max_rows < 0):
        raise ValueError("max_rows must be a non-negative integer or None")

    out: list[Shape] = [()]

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if prefix and (max_rows is None or len(prefix) <= max_rows):
            out.append(tuple(prefix))
        if max_rows is not None and len(prefix) >= max_rows:
            return
        for part in range(min(remaining, max_part), 0, -1):
            rec(remaining - part, part, prefix + [part])

    rec(max_size, max_size, [])
    return out


def shape_size(shape: Sequence[int]) -> int:
    if not is_partition_shape(shape) and tuple(shape) != ():
        raise ValueError("shape must be a partition")
    return sum(shape)


def tableau_shape(tableau: Sequence[Sequence[int]]) -> Shape:
    return tuple(len(row) for row in tableau)


def is_ssyt(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> bool:
    rows = tuple(tuple(row) for row in tableau)
    shape = tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    for row in rows:
        if any(not isinstance(value, int) or value < low or value > high for value in row):
            return False
        if any(row[index] > row[index + 1] for index in range(len(row) - 1)):
            return False
    for row_index in range(len(rows) - 1):
        for column in range(len(rows[row_index + 1])):
            if rows[row_index][column] >= rows[row_index + 1][column]:
                return False
    return True


def is_reverse_ssyt(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> bool:
    rows = tuple(tuple(row) for row in tableau)
    shape = tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    for row in rows:
        if any(not isinstance(value, int) or value < low or value > high for value in row):
            return False
        if any(row[index] < row[index + 1] for index in range(len(row) - 1)):
            return False
    for row_index in range(len(rows) - 1):
        for column in range(len(rows[row_index + 1])):
            if rows[row_index][column] <= rows[row_index + 1][column]:
                return False
    return True


def enumerate_ssyt(
    shape: Sequence[int],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> list[SSYT]:
    shape_tuple = tuple(shape)
    if shape_tuple != () and not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition in top-to-bottom row order")
    if not isinstance(alphabet_size, int) or alphabet_size <= 0:
        raise ValueError("alphabet_size must be positive")

    cells = [(row, col) for row, length in enumerate(shape_tuple) for col in range(length)]
    rows = [[0 for _ in range(length)] for length in shape_tuple]
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    out: list[SSYT] = []

    def rec(cell_index: int) -> None:
        if cell_index == len(cells):
            out.append(tuple(tuple(row) for row in rows))
            return
        row, col = cells[cell_index]
        min_value = low
        if col > 0:
            min_value = max(min_value, rows[row][col - 1])
        if row > 0 and col < shape_tuple[row - 1]:
            min_value = max(min_value, rows[row - 1][col] + 1)
        for value in range(min_value, high + 1):
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = 0

    rec(0)
    return out


def enumerate_reverse_ssyt(
    shape: Sequence[int],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> list[SSYT]:
    high = alphabet_start + alphabet_size - 1
    return tuple(
        tuple(tuple(high - (value - alphabet_start) for value in row) for row in tableau)
        for tableau in enumerate_ssyt(
            shape,
            alphabet_size=alphabet_size,
            alphabet_start=alphabet_start,
        )
    )


def ssyt_weight(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> Weight:
    if not is_ssyt(tableau, alphabet_size=alphabet_size, alphabet_start=alphabet_start):
        raise ValueError("tableau must be an SSYT over the requested alphabet")
    counts = [0] * alphabet_size
    for row in tableau:
        for value in row:
            counts[value - alphabet_start] += 1
    return tuple(counts)


def reverse_ssyt_weight(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> Weight:
    if not is_reverse_ssyt(tableau, alphabet_size=alphabet_size, alphabet_start=alphabet_start):
        raise ValueError("tableau must be a reverse SSYT over the requested alphabet")
    counts = [0] * alphabet_size
    for row in tableau:
        for value in row:
            counts[value - alphabet_start] += 1
    return tuple(counts)


def weight_dictionary(tableaux: Iterable[Sequence[Sequence[int]]], *, alphabet_size: int) -> Counter[Weight]:
    weights: Counter[Weight] = Counter()
    for tableau in tableaux:
        weights[ssyt_weight(tableau, alphabet_size=alphabet_size)] += 1
    return weights


def schur_polynomial_by_ssyt(shape: Sequence[int], *, alphabet_size: int) -> Counter[Weight]:
    return weight_dictionary(enumerate_ssyt(shape, alphabet_size=alphabet_size), alphabet_size=alphabet_size)
```

### `items/dyck_symmetric_functions/code/paper_algorithms/tableau_insertion.py`

```python
"""Section 3 tableau insertion helpers.

Tableaux are represented as ``list`` objects ordered bottom row to top row.
Each row is a left-to-right sequence of non-negative integers.

Shape convention used here: rows may have different lengths and no monotone
row-length condition is imposed by ``is_dyck_tableau``.  For each column index,
the cells that exist in rows having that index are read bottom-to-top and must
satisfy the affine Dyck inequality.  This is the bottom-to-top representation
requested by CA-0002; it differs from the protected draft's local prose that
sometimes indexes rows top-to-bottom.

``tabsert`` processes existing rows in the source/paper top-to-bottom order,
which is descending index order under this bottom-to-top storage.  When it
carries a non-empty evicted row past all existing rows, that row is inserted at
index 0, i.e. it becomes a new bottom row in the bottom-to-top list.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .row_insertion import RowsertStep, WorsertStep, is_dual_dyck, rowsert, worsert


Tableau = list[list[int]]


@dataclass(frozen=True)
class TabsertRowTrace:
    row_index: int
    input_row: tuple[int, ...]
    inserted_row: tuple[int, ...]
    evicted_row: tuple[int, ...]
    output_row: tuple[int, ...]
    rowsert_steps: tuple[RowsertStep, ...]


@dataclass(frozen=True)
class ReverseTabsertRowTrace:
    row_index: int
    original_length: int
    input_row: tuple[int, ...]
    kept_row: tuple[int, ...]
    peeled_row: tuple[int, ...]
    accumulated_in: tuple[int, ...]
    recovered_row: tuple[int, ...]
    accumulated_out: tuple[int, ...]
    worsert_steps: tuple[WorsertStep, ...]


def _is_row(value: object) -> bool:
    return isinstance(value, (list, tuple)) and all(
        isinstance(entry, int) and entry >= 0 for entry in value
    )


def shape(tableau: Sequence[Sequence[int]]) -> list[int]:
    """Return row lengths in bottom-to-top order."""

    _require_tableau_like(tableau)
    return [len(row) for row in tableau]


def _require_tableau_like(tableau: Sequence[Sequence[int]]) -> None:
    if not isinstance(tableau, (list, tuple)):
        raise TypeError("tableau must be a list or tuple of rows")
    for row in tableau:
        if not _is_row(row):
            raise TypeError("each tableau row must be a sequence of non-negative integers")


def _copied_tableau(tableau: Sequence[Sequence[int]]) -> Tableau:
    _require_tableau_like(tableau)
    return [list(row) for row in tableau]


def is_affine_dyck(seq: Sequence[int]) -> bool:
    """Return whether ``seq`` satisfies the affine-Dyck step condition."""

    return all(isinstance(value, int) and value >= 0 for value in seq) and all(
        seq[index + 1] <= seq[index] + 1 for index in range(len(seq) - 1)
    )


def is_dyck_tableau(tableau: Sequence[Sequence[int]]) -> bool:
    """Validate the CA-0002 bottom-to-top Dyck tableau convention.

    Empty tableaux are accepted.  Empty rows inside a non-empty tableau are
    rejected, because they create ambiguous shape data for the reverse helper.
    """

    try:
        rows = _copied_tableau(tableau)
    except TypeError:
        return False

    if any(len(row) == 0 for row in rows):
        return len(rows) == 0
    if any(not is_dual_dyck(row) for row in rows):
        return False

    max_len = max((len(row) for row in rows), default=0)
    for column in range(max_len):
        column_values = [row[column] for row in rows if column < len(row)]
        if not is_affine_dyck(column_values):
            return False
    return True


def row_reading_word(tableau: Sequence[Sequence[int]]) -> list[int]:
    """Read rows bottom-to-top, and within each row left-to-right."""

    _require_tableau_like(tableau)
    word: list[int] = []
    for row in tableau:
        word.extend(row)
    return word


def tabsert(
    tableau: Sequence[Sequence[int]],
    inserted_row: Sequence[int],
    *,
    trace: bool = False,
) -> Tableau | tuple[Tableau, list[TabsertRowTrace]]:
    """Insert ``inserted_row`` through ``tableau`` using ``rowsert``.

    Existing rows are processed in source/paper top-to-bottom order, i.e.
    descending index order under bottom-to-top storage.  Inputs are copied and
    never mutated.  If ``trace`` is true, the returned pair is
    ``(updated_tableau, row_traces)``.
    """

    rows = _copied_tableau(tableau)
    if not is_dyck_tableau(rows):
        raise ValueError("tableau must be a valid Dyck tableau")
    if not is_dual_dyck(inserted_row):
        raise ValueError("inserted_row must be a dual Dyck sequence")

    evicted = list(inserted_row)
    traces: list[TabsertRowTrace] = []
    row_index = len(rows) - 1
    while evicted and row_index >= 0:
        input_row = tuple(rows[row_index])
        inserted = tuple(evicted)
        row_trace: list[RowsertStep] = []
        next_evicted, output_row = rowsert(rows[row_index], evicted, trace=row_trace)
        rows[row_index] = output_row
        evicted = next_evicted
        traces.append(
            TabsertRowTrace(
                row_index=row_index,
                input_row=input_row,
                inserted_row=inserted,
                evicted_row=tuple(evicted),
                output_row=tuple(output_row),
                rowsert_steps=tuple(row_trace),
            )
        )
        row_index -= 1

    if evicted:
        rows.insert(0, list(evicted))
        traces.append(
            TabsertRowTrace(
                row_index=0,
                input_row=(),
                inserted_row=tuple(evicted),
                evicted_row=(),
                output_row=tuple(evicted),
                rowsert_steps=(),
            )
        )

    if not is_dyck_tableau(rows):
        raise ValueError("tabsert output is not a valid Dyck tableau under the documented convention")
    return (rows, traces) if trace else rows


def reverse_tabsert(
    updated_tableau: Sequence[Sequence[int]],
    original_shape: Sequence[int],
    *,
    trace: bool = False,
) -> tuple[Tableau, list[int]] | tuple[Tableau, list[int], list[ReverseTabsertRowTrace]]:
    """Bounded rowwise reverse helper for red-team checks.

    ``original_shape`` is the list of original row lengths in bottom-to-top
    order.  Extra updated rows are interpreted as newly added bottom rows and
    initialize the accumulated sequence.  The helper then works through the
    original rows from bottom to top, reversing the corrected top-to-bottom
    forward insertion order.  At original row ``r`` it keeps the first
    ``original_shape[r]`` cells, peels terminal cells as the horizontal-strip
    contribution, runs corrected ``worsert`` on the accumulated sequence
    through the kept row, and passes ``F_minus + F_plus`` downward.  This is an
    executable approximation of the proof's inverse construction, intended for
    finite checks.
    """

    rows = _copied_tableau(updated_tableau)
    if not is_dyck_tableau(rows):
        raise ValueError("updated_tableau must be a valid Dyck tableau")
    if not isinstance(original_shape, (list, tuple)) or any(
        not isinstance(length, int) or length < 0 for length in original_shape
    ):
        raise TypeError("original_shape must be a sequence of non-negative row lengths")
    if len(original_shape) > len(rows):
        raise ValueError("original_shape has more rows than updated_tableau")

    offset = len(rows) - len(original_shape)
    if offset < 0:
        raise ValueError("updated_tableau has fewer rows than original_shape")

    recovered: Tableau = [[] for _ in original_shape]
    accumulated: list[int] = []
    traces: list[ReverseTabsertRowTrace] = []

    for row_index in range(offset):
        current_row = rows[row_index]
        accumulated_in = tuple(accumulated)
        accumulated = accumulated + list(current_row)
        traces.append(
            ReverseTabsertRowTrace(
                row_index=row_index,
                original_length=0,
                input_row=tuple(current_row),
                kept_row=(),
                peeled_row=tuple(current_row),
                accumulated_in=accumulated_in,
                recovered_row=(),
                accumulated_out=tuple(accumulated),
                worsert_steps=(),
            )
        )

    for original_index in range(len(original_shape)):
        row_index = offset + original_index
        current_row = rows[row_index]
        keep_length = original_shape[original_index]
        if keep_length > len(current_row):
            raise ValueError("original_shape cannot exceed updated row lengths")
        kept = list(current_row[:keep_length])
        peeled = list(current_row[keep_length:])
        wor_trace: list[WorsertStep] = []
        recovered_row, f_minus = worsert(accumulated, kept, trace=wor_trace)
        accumulated_out = list(f_minus) + peeled
        recovered[original_index] = recovered_row
        traces.append(
            ReverseTabsertRowTrace(
                row_index=row_index,
                original_length=keep_length,
                input_row=tuple(current_row),
                kept_row=tuple(kept),
                peeled_row=tuple(peeled),
                accumulated_in=tuple(accumulated),
                recovered_row=tuple(recovered_row),
                accumulated_out=tuple(accumulated_out),
                worsert_steps=tuple(wor_trace),
            )
        )
        accumulated = accumulated_out

    if not is_dyck_tableau(recovered):
        raise ValueError("reverse helper recovered an invalid Dyck tableau")
    if not is_dual_dyck(accumulated):
        raise ValueError("reverse helper recovered an invalid inserted row")
    result = (recovered, accumulated)
    return (*result, traces) if trace else result
```

### `items/dyck_symmetric_functions/code/random_rational_dyck_checks.py`

```python
"""Monte Carlo checks for rational dual Dyck symmetric-function classes.

Each trial samples one word uniformly from ``{1, ..., A}^L``.  The sampled word
selects a multiset and dinv value; the checker then exhaustively verifies the
usual factorization-symmetry and Dyck-tableau prediction for that single class.
"""

from __future__ import annotations

import argparse
import random
import time
from collections import Counter
from dataclasses import dataclass
from multiprocessing import Pool

try:
    import numpy as np
    from numba import njit, types
    from numba.typed import Dict
except ImportError:  # pragma: no cover - fallback path for minimal environments.
    np = None
    njit = None
    types = None
    Dict = None

from check_rational_dyck_generalization import (
    CheckInput,
    Composition,
    Partition,
    PartitionMaskData,
    Shape,
    Word,
    composition_groups,
    count_ssyt_with_content,
    dyck_tableau_predictions,
    pair_dinv_table,
    partition_shapes,
    valid_factorization_counts_by_cut_mask,
)


if njit is not None:

    @njit
    def _jit_class_word_extend(
        position: int,
        previous_index: int,
        dinv: int,
        required_dual_cuts: int,
        active_count: int,
        target_dinv: int,
        length: int,
        alphabet_size: int,
        step: int,
        pair_dinv_array: np.ndarray,
        remaining: np.ndarray,
        used_counts: np.ndarray,
        active_indices: np.ndarray,
        mask_counts: Dict,
    ) -> None:
        if dinv > target_dinv:
            return
        if position == length:
            if dinv == target_dinv:
                mask_counts[required_dual_cuts] = mask_counts.get(required_dual_cuts, 0) + 1
            return

        for value_index in range(alphabet_size):
            if remaining[value_index] == 0:
                continue
            dinv_increment = 0
            for active_position in range(active_count):
                earlier_index = active_indices[active_position]
                dinv_increment += used_counts[earlier_index] * pair_dinv_array[earlier_index, value_index]
            next_dinv = dinv + dinv_increment
            if next_dinv > target_dinv:
                continue

            next_required_dual_cuts = required_dual_cuts
            if position > 0 and value_index <= previous_index + step:
                next_required_dual_cuts |= 1 << (position - 1)

            next_active_count = active_count
            if used_counts[value_index] == 0:
                active_indices[next_active_count] = value_index
                next_active_count += 1
            remaining[value_index] -= 1
            used_counts[value_index] += 1
            _jit_class_word_extend(
                position + 1,
                value_index,
                next_dinv,
                next_required_dual_cuts,
                next_active_count,
                target_dinv,
                length,
                alphabet_size,
                step,
                pair_dinv_array,
                remaining,
                used_counts,
                active_indices,
                mask_counts,
            )
            used_counts[value_index] -= 1
            remaining[value_index] += 1


    @njit
    def _jit_class_word_mask_counts(
        counts: np.ndarray,
        target_dinv: int,
        length: int,
        alphabet_size: int,
        step: int,
        pair_dinv_array: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray]:
        remaining = counts.copy()
        used_counts = np.zeros(alphabet_size, dtype=np.int64)
        active_indices = np.empty(alphabet_size, dtype=np.int64)
        mask_counts = Dict.empty(key_type=types.int64, value_type=types.int64)
        _jit_class_word_extend(
            0,
            0,
            0,
            0,
            0,
            target_dinv,
            length,
            alphabet_size,
            step,
            pair_dinv_array,
            remaining,
            used_counts,
            active_indices,
            mask_counts,
        )
        keys = np.empty(len(mask_counts), dtype=np.int64)
        values = np.empty(len(mask_counts), dtype=np.int64)
        index = 0
        for key, value in mask_counts.items():
            keys[index] = key
            values[index] = value
            index += 1
        return keys, values

else:
    _jit_class_word_mask_counts = None


@dataclass(frozen=True)
class RandomCheckInput:
    step: int
    alphabet_size: int
    length: int
    iterations: int
    timeout_seconds: float | None
    seed: int | None
    workers: int = 1


@dataclass
class RandomCheckResult:
    params: RandomCheckInput
    iterations_completed: int = 0
    sampled_words: int = 0
    class_words_checked: int = 0
    dyck_tableaux_checked: int = 0
    partition_classes_checked: int = 0
    compositions_checked: int = 0
    elapsed_seconds: float = 0.0


@dataclass
class TrialSummary:
    iteration: int
    sample_word: Word
    target_dinv: int
    class_words: int
    tableaux: int
    partition_classes: int
    compositions: int
    elapsed_seconds: float


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def random_word(*, length: int, alphabet_size: int, rng: random.Random) -> Word:
    return tuple(rng.randint(1, alphabet_size) for _ in range(length))


def counts_from_word(word: Word, *, alphabet_size: int) -> tuple[int, ...]:
    counts = [0] * alphabet_size
    for value in word:
        counts[value - 1] += 1
    return tuple(counts)


def multiset_from_counts(counts: tuple[int, ...]) -> Word:
    values: list[int] = []
    for index, multiplicity in enumerate(counts, start=1):
        values.extend([index] * multiplicity)
    return tuple(values)


def word_dinv(word: Word, pair_dinv: tuple[tuple[int, ...], ...]) -> int:
    total = 0
    for right in range(len(word)):
        right_index = word[right] - 1
        for left in range(right):
            total += pair_dinv[word[left] - 1][right_index]
    return total


def class_word_mask_counts(
    *,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> Counter[int]:
    if _jit_class_word_mask_counts is not None:
        counts_array = np.array(counts, dtype=np.int64)
        pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
        keys, values = _jit_class_word_mask_counts(
            counts_array,
            target_dinv,
            params.length,
            params.alphabet_size,
            params.step,
            pair_dinv_array,
        )
        return Counter({int(key): int(value) for key, value in zip(keys, values)})

    remaining = list(counts)
    used_counts = [0] * params.alphabet_size
    active_indices: list[int] = []
    mask_counts: Counter[int] = Counter()

    def extend(position: int, previous_index: int, dinv: int, required_dual_cuts: int) -> None:
        if dinv > target_dinv:
            return
        if position == params.length:
            if dinv == target_dinv:
                mask_counts[required_dual_cuts] += 1
            return

        for value_index in range(params.alphabet_size):
            if remaining[value_index] == 0:
                continue
            dinv_increment = 0
            for earlier_index in active_indices:
                dinv_increment += used_counts[earlier_index] * pair_dinv[earlier_index][value_index]
            next_dinv = dinv + dinv_increment
            if next_dinv > target_dinv:
                continue

            next_required_dual_cuts = required_dual_cuts
            if position > 0 and value_index <= previous_index + params.step:
                next_required_dual_cuts |= 1 << (position - 1)

            first_value = used_counts[value_index] == 0
            if first_value:
                active_indices.append(value_index)
            remaining[value_index] -= 1
            used_counts[value_index] += 1
            extend(position + 1, value_index, next_dinv, next_required_dual_cuts)
            used_counts[value_index] -= 1
            remaining[value_index] += 1
            if first_value:
                active_indices.pop()

    extend(0, 0, 0, 0)
    return mask_counts


def class_tableau_shape_counts(
    *,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> Counter[Shape]:
    shape_counts: Counter[Shape] = Counter()

    for shape in partition_shapes(params.length):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(row_length)] for row_length in shape]
        remaining = list(counts)
        used_counts = [0] * params.alphabet_size
        active_indices: list[int] = []

        def fill(cell_index: int, dinv: int) -> None:
            if dinv > target_dinv:
                return
            if cell_index == len(cells):
                if dinv == target_dinv:
                    shape_counts[shape] += 1
                return

            row, col = cells[cell_index]
            lower = 1
            if col > 0:
                lower = rows[row][col - 1] + params.step + 1
            upper = params.alphabet_size
            if row + 1 < len(shape) and col < shape[row + 1]:
                upper = min(upper, rows[row + 1][col] + params.step)

            for value in range(lower, upper + 1):
                value_index = value - 1
                if remaining[value_index] == 0:
                    continue
                dinv_increment = 0
                for earlier_index in active_indices:
                    dinv_increment += used_counts[earlier_index] * pair_dinv[earlier_index][value_index]
                next_dinv = dinv + dinv_increment
                if next_dinv > target_dinv:
                    continue

                first_value = used_counts[value_index] == 0
                if first_value:
                    active_indices.append(value_index)
                remaining[value_index] -= 1
                used_counts[value_index] += 1
                rows[row][col] = value
                fill(cell_index + 1, next_dinv)
                rows[row][col] = 0
                used_counts[value_index] -= 1
                remaining[value_index] += 1
                if first_value:
                    active_indices.pop()

        fill(0, 0)

    return shape_counts


def verify_sampled_class(
    *,
    sample_word: Word,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
    partitions: list[PartitionMaskData],
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> tuple[int, int, int, int]:
    mask_counts = class_word_mask_counts(
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
    )
    class_word_count = sum(mask_counts.values())
    require(
        class_word_count > 0,
        f"internal error: sampled word class is empty for word={sample_word}, dinv={target_dinv}",
    )
    shape_counts = class_tableau_shape_counts(
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
    )
    valid_by_cut_mask = valid_factorization_counts_by_cut_mask(mask_counts, length=params.length)
    predictions = dyck_tableau_predictions(
        shape_counts,
        partitions,
        ssyt_cache=ssyt_cache,
        prediction_cache=prediction_cache,
    )
    multiset = multiset_from_counts(counts)
    partition_classes_checked = 0
    compositions_checked = 0

    for partition_index, (partition, compositions, cut_masks) in enumerate(partitions):
        actual = valid_by_cut_mask[cut_masks[0]]
        for cut_mask in cut_masks[1:]:
            if valid_by_cut_mask[cut_mask] != actual:
                values = {
                    composition: valid_by_cut_mask[composition_cut_mask]
                    for composition, composition_cut_mask in zip(compositions, cut_masks)
                }
                examples = sorted(values.items())[:8]
                raise AssertionError(
                    "factorization symmetry mismatch: "
                    f"t={params.step}, sample_word={sample_word}, multiset={multiset}, "
                    f"dinv={target_dinv}, partition={partition}, examples={examples}"
                )
        predicted = predictions[partition_index]
        if actual != predicted:
            values = {
                composition: valid_by_cut_mask[composition_cut_mask]
                for composition, composition_cut_mask in zip(compositions, cut_masks)
            }
            examples = sorted(values.items())[:8]
            raise AssertionError(
                "Dyck-tableau prediction mismatch: "
                f"t={params.step}, sample_word={sample_word}, multiset={multiset}, "
                f"dinv={target_dinv}, partition={partition}, factorization_count={actual}, "
                f"tableau_prediction={predicted}, examples={examples}"
            )
        partition_classes_checked += 1
        compositions_checked += len(compositions)

    return class_word_count, sum(shape_counts.values()), partition_classes_checked, compositions_checked


def run_one_trial(
    *,
    iteration: int,
    seed: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
    partitions: list[PartitionMaskData],
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> TrialSummary:
    rng = random.Random(seed)
    sample_start = time.perf_counter()
    sample_word = random_word(length=params.length, alphabet_size=params.alphabet_size, rng=rng)
    counts = counts_from_word(sample_word, alphabet_size=params.alphabet_size)
    target_dinv = word_dinv(sample_word, pair_dinv)
    class_words, tableaux, partition_classes, compositions = verify_sampled_class(
        sample_word=sample_word,
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
        partitions=partitions,
        ssyt_cache=ssyt_cache,
        prediction_cache=prediction_cache,
    )
    return TrialSummary(
        iteration=iteration,
        sample_word=sample_word,
        target_dinv=target_dinv,
        class_words=class_words,
        tableaux=tableaux,
        partition_classes=partition_classes,
        compositions=compositions,
        elapsed_seconds=time.perf_counter() - sample_start,
    )


def run_trial_batch(args: tuple[RandomCheckInput, list[tuple[int, int]]]) -> list[TrialSummary]:
    params, trials = args
    pair_dinv = pair_dinv_table(CheckInput(params.step, params.alphabet_size, params.length))
    partitions = composition_groups(params.length)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    return [
        run_one_trial(
            iteration=iteration,
            seed=seed,
            params=params,
            pair_dinv=pair_dinv,
            partitions=partitions,
            ssyt_cache=ssyt_cache,
            prediction_cache=prediction_cache,
        )
        for iteration, seed in trials
    ]


def print_trial_summary(summary: TrialSummary) -> None:
    print(
        f"  iteration={summary.iteration}: word={summary.sample_word}, dinv={summary.target_dinv}, "
        f"class words={summary.class_words}, tableaux={summary.tableaux}, "
        f"elapsed={summary.elapsed_seconds:.3f}s",
        flush=True,
    )


def run_random_checks(params: RandomCheckInput) -> RandomCheckResult:
    require(params.step >= 0, "t must be non-negative")
    require(params.alphabet_size > 0, "alphabet size A must be positive")
    require(params.length > 0, "length L must be positive")
    require(params.iterations >= 0, "iterations must be non-negative")
    require(params.timeout_seconds is None or params.timeout_seconds > 0, "timeout must be positive")
    require(params.iterations > 0 or params.timeout_seconds is not None, "use iterations, timeout, or both")
    require(params.workers > 0, "workers must be positive")

    result = RandomCheckResult(params=params)
    seed_rng = random.Random(params.seed)
    pair_dinv = pair_dinv_table(CheckInput(params.step, params.alphabet_size, params.length))
    partitions = composition_groups(params.length)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    start = time.perf_counter()

    if params.workers > 1 and params.timeout_seconds is None:
        trials = [
            (iteration, seed_rng.randrange(0, 2**63))
            for iteration in range(1, params.iterations + 1)
        ]
        batches = [[] for _ in range(min(params.workers, len(trials)))]
        for index, trial in enumerate(trials):
            batches[index % len(batches)].append(trial)
        with Pool(processes=len(batches)) as pool:
            batch_results = pool.map(run_trial_batch, [(params, batch) for batch in batches if batch])
        summaries = sorted((summary for batch in batch_results for summary in batch), key=lambda item: item.iteration)
        for summary in summaries:
            print_trial_summary(summary)
            result.iterations_completed += 1
            result.sampled_words += 1
            result.class_words_checked += summary.class_words
            result.dyck_tableaux_checked += summary.tableaux
            result.partition_classes_checked += summary.partition_classes
            result.compositions_checked += summary.compositions
        result.elapsed_seconds = time.perf_counter() - start
        return result

    while result.iterations_completed < params.iterations or params.timeout_seconds is not None:
        if params.iterations and result.iterations_completed >= params.iterations:
            break
        elapsed = time.perf_counter() - start
        if params.timeout_seconds is not None and elapsed >= params.timeout_seconds:
            break

        summary = run_one_trial(
            iteration=result.iterations_completed + 1,
            seed=seed_rng.randrange(0, 2**63),
            params=params,
            pair_dinv=pair_dinv,
            partitions=partitions,
            ssyt_cache=ssyt_cache,
            prediction_cache=prediction_cache,
        )
        result.iterations_completed += 1
        result.sampled_words += 1
        result.class_words_checked += summary.class_words
        result.dyck_tableaux_checked += summary.tableaux
        result.partition_classes_checked += summary.partition_classes
        result.compositions_checked += summary.compositions
        print_trial_summary(summary)

    result.elapsed_seconds = time.perf_counter() - start
    return result


def print_result(result: RandomCheckResult) -> None:
    params = result.params
    print(f"completed random checks: t={params.step}, alphabet={{1,...,{params.alphabet_size}}}, length={params.length}")
    print(f"  iterations completed: {result.iterations_completed}")
    print(f"  sampled words: {result.sampled_words}")
    print(f"  class words checked: {result.class_words_checked}")
    print(f"  Dyck tableaux checked: {result.dyck_tableaux_checked}")
    print(f"  partition classes checked: {result.partition_classes_checked}")
    print(f"  positive compositions checked: {result.compositions_checked}")
    print(f"  elapsed: {result.elapsed_seconds:.3f}s")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, required=True, help="Rational step t.")
    parser.add_argument("--alphabet-size", "-A", type=int, required=True, help="Alphabet size A.")
    parser.add_argument("--length", "-L", type=int, required=True, help="Sampled word length.")
    parser.add_argument("--iterations", type=int, default=100, help="Maximum sampled classes to check.")
    parser.add_argument("--timeout-seconds", type=float, default=None, help="Optional wall-clock timeout.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed.")
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Parallel worker processes for fixed-iteration runs.",
    )
    args = parser.parse_args()

    result = run_random_checks(
        RandomCheckInput(
            step=args.t,
            alphabet_size=args.alphabet_size,
            length=args.length,
            iterations=args.iterations,
            timeout_seconds=args.timeout_seconds,
            seed=args.seed,
            workers=args.workers,
        )
    )
    print_result(result)
    print("all sampled finite checks passed")


if __name__ == "__main__":
    main()
```

### `items/dyck_symmetric_functions/code/README.md`

```markdown
# Code

Purpose: reproduce the executable parts curated for the Dyck symmetric
functions item.

## Classical Insertion Algorithm

Command:

````text
python classical_insertion_demo.py
````

This script traces the classical row insertion operation and a tableau
insertion example.  The implementation lives in:

- `paper_algorithms/row_insertion.py`
- `paper_algorithms/tableau_insertion.py`

These files are adapted from the 2026 preprint code.  They implement the
insertion algorithm used to prove Schur positivity for the classical dual Dyck
symmetric functions.

## Rational Dual Finite Checks

Command:

````text
python check_rational_dyck_generalization.py --t 2 --alphabet-size 4 --max-length 4
````

Official repository checks:

````text
python check_rational_dyck_generalization.py --t 2 -A 10 -L 10
python check_rational_dyck_generalization.py --t 3 -A 13 -L 9
python check_rational_dyck_generalization.py --t 4 -A 16 -L 8
````

Dependencies: Python standard library only for the portable fallback.  If
`numpy` and `numba` are installed, the checker automatically uses a compiled
word-grouping backend.  Compiled word scans with at least 50 million generated
words are split across worker processes automatically; use `--workers 1` to
force serial execution, a positive `--workers N` to force `N` workers, or
`DYCK_CHECK_WORKERS=N` to set the default from the environment.

Inputs are explicit and minimal:

- `--t`: rational step.
- `--alphabet-size` or `-A`: alphabet size, using `{1,2,...,A}`.
- `--max-length` or `-L`: checks every length `1 <= l <= L`.

For each length the checker:

- constructs every word over `{1,2,...,A}` that contains `1`;
- groups words by underlying multiset and rational dinv;
- generates every positive composition of the length and groups compositions
  by their sorted underlying partition;
- verifies that, for each multiset, dinv, and partition, every distinct
  composition in that partition gives the same number of valid dual Dyck
  factorizations;
- compares that common factorization count with the Dyck-tableau prediction
  obtained by summing, over rational Dyck tableaux with that multiset and
  dinv, the number of SSYT of the tableau shape with the given dominant
  content.

The implementation keeps the useful cut-mask optimization from the older
checker: a word contributes a bitmask of adjacent positions that must be cut
for a dual factorization, and a positive composition is valid exactly when its
cut mask contains that required mask.  With NumPy and Numba available, word
grouping is performed by a compiled exhaustive scan that aggregates compact
integer records for `(multiset, dinv, cut mask)` and then feeds the same Python
verification pipeline.  For sufficiently large word universes, that compiled
scan is partitioned across worker processes and the compact aggregate records
are merged before verification.  Without those optional dependencies, word grouping
falls back to the pure-Python first-`1` generator, which counts words with no
`1` in the reported universe size but never traverses them.  Tableau grouping
uses the same first-`1` idea, fixing the first tableau cell containing `1` and
avoiding terminal rejection of tableaux with no `1`.  Internally, multiset keys
are compact integer encodings during each fixed-length pass, Dyck-tableau
predictions are cached by shape-count profile, and factorization counts use
cached cut-mask subset sums.  The code no longer has a variable-count
parameter, affine/dual/both option, or compressed/full comparison modes.

Interpretation: these are bounded computational checks of the conjectural
`r = s*t + 1` analogue.  They are not a proof of the general conjecture.

## Random Class Checks

Command:

````text
python random_rational_dyck_checks.py --t 2 -A 10 -L 10 --iterations 100 --seed 1
````

This Monte Carlo checker samples words uniformly from `{1,2,...,A}^L`.  Each
sampled word determines a multiset and rational dinv value.  The script then
forgets the sampled order and exhaustively checks the full class with that
multiset and dinv:

- all words with the sampled multiset and dinv are enumerated;
- factorization counts are checked for symmetry across compositions with the
  same underlying partition;
- the common counts are compared with the corresponding Dyck-tableau
  prediction.

Unlike the exhaustive checker, this script does not restrict to words
containing `1`; the sampled word may use any letters in the alphabet.
When NumPy and Numba are installed, the fixed-multiset word-class enumeration
is JIT-compiled automatically; the pure-Python implementation remains as a
portable fallback.

Stopping controls:

- `--iterations N`: maximum sampled classes to check.
- `--timeout-seconds S`: optional wall-clock timeout.
- `--seed N`: optional reproducible random seed.
- `--workers N`: parallel worker processes for fixed-iteration runs.  Timeout
  driven runs currently execute serially.
```

### `items/dyck_symmetric_functions/explanation.aux`

```text
\relax 
\@writefile{toc}{\contentsline {section}{\numberline {1}Status}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {2}The \(r=s t+1\) Setup}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {3}The Degenerate \(t=0\) Case}{2}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {4}Classical Theorem}{2}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {5}Conjectural \(r=s t+1\) Analogue}{3}{}\protected@file@percent }
\gdef \@abspage@last{3}
```

### `items/dyck_symmetric_functions/explanation.log`

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.29 (MiKTeX 26.5) (preloaded format=pdflatex 2026.5.25)  16 JUN 2026 10:32
entering extended mode
 restricted \write18 enabled.
 %&-line parsing enabled.
**./explanation.tex
(explanation.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\size10.clo
File: size10.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
)
\c@part=\count276
\c@section=\count277
\c@subsection=\count278
\c@subsubsection=\count279
\c@paragraph=\count280
\c@subparagraph=\count281
\c@figure=\count282
\c@table=\count283
\abovecaptionskip=\skip49
\belowcaptionskip=\skip50
\bibindent=\dimen150
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsmath.sty
Package: amsmath 2025/07/09 v2.17z AMS math features
\@mathmargin=\skip51

For additional information on amsmath, use the `?' option.
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amstext.sty
Package: amstext 2024/11/17 v2.01 AMS text

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsgen.sty
File: amsgen.sty 1999/11/30 v2.0 generic functions
\@emptytoks=\toks17
\ex@=\dimen151
))
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsbsy.sty
Package: amsbsy 1999/11/29 v1.2d Bold Symbols
\pmbraise@=\dimen152
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsopn.sty
Package: amsopn 2022/04/08 v2.04 operator names
)
\inf@bad=\count284
LaTeX Info: Redefining \frac on input line 233.
\uproot@=\count285
\leftroot@=\count286
LaTeX Info: Redefining \overline on input line 398.
LaTeX Info: Redefining \colon on input line 409.
\classnum@=\count287
\DOTSCASE@=\count288
LaTeX Info: Redefining \ldots on input line 495.
LaTeX Info: Redefining \dots on input line 498.
LaTeX Info: Redefining \cdots on input line 619.
\Mathstrutbox@=\box53
\strutbox@=\box54
LaTeX Info: Redefining \big on input line 721.
LaTeX Info: Redefining \Big on input line 722.
LaTeX Info: Redefining \bigg on input line 723.
LaTeX Info: Redefining \Bigg on input line 724.
\big@size=\dimen153
LaTeX Font Info:    Redeclaring font encoding OML on input line 742.
LaTeX Font Info:    Redeclaring font encoding OMS on input line 743.
\macc@depth=\count289
LaTeX Info: Redefining \bmod on input line 904.
LaTeX Info: Redefining \pmod on input line 909.
LaTeX Info: Redefining \smash on input line 939.
LaTeX Info: Redefining \relbar on input line 969.
LaTeX Info: Redefining \Relbar on input line 970.
\c@MaxMatrixCols=\count290
\dotsspace@=\muskip17
\c@parentequation=\count291
\dspbrk@lvl=\count292
\tag@help=\toks18
\row@=\count293
\column@=\count294
\maxfields@=\count295
\andhelp@=\toks19
\eqnshift@=\dimen154
\alignsep@=\dimen155
\tagshift@=\dimen156
\tagwidth@=\dimen157
\totwidth@=\dimen158
\lineht@=\dimen159
\@envbody=\toks20
\multlinegap=\skip52
\multlinetaggap=\skip53
\mathdisplay@stack=\toks21
LaTeX Info: Redefining \[ on input line 2950.
LaTeX Info: Redefining \] on input line 2951.
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amscls\amsthm.sty
Package: amsthm 2020/05/29 v2.20.6
\thm@style=\toks22
\thm@bodyfont=\toks23
\thm@headfont=\toks24
\thm@notefont=\toks25
\thm@headpunct=\toks26
\thm@preskip=\skip54
\thm@postskip=\skip55
\thm@headsep=\skip56
\dth@everypar=\toks27
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amssymb.sty
Package: amssymb 2013/01/14 v3.01 AMS font symbols

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amsfonts.sty
Package: amsfonts 2013/01/14 v3.01 Basic AMSFonts support
\symAMSa=\mathgroup4
\symAMSb=\mathgroup5
LaTeX Font Info:    Redeclaring math symbol \hbar on input line 98.
LaTeX Font Info:    Overwriting math alphabet `\mathfrak' in version `bold'
(Font)                  U/euf/m/n --> U/euf/b/n on input line 106.
))
\c@theorem=\count296
\c@conjecture=\count297
\c@definition=\count298
\c@remark=\count299

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/l3backend\l3backend-pdft
ex.def
File: l3backend-pdftex.def 2026-02-18 L3 backend support: PDF output (pdfTeX)
\l__color_backend_stack_int=\count300
) (explanation.aux)
\openout1 = `explanation.aux'.

LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 16.
LaTeX Font Info:    ... okay on input line 16.
LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 16.
LaTeX Font Info:    ... okay on input line 16.
LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 16.
LaTeX Font Info:    ... okay on input line 16.
LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 16.
LaTeX Font Info:    ... okay on input line 16.
LaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 16.
LaTeX Font Info:    ... okay on input line 16.
LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 16.
LaTeX Font Info:    ... okay on input line 16.
LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 16.
LaTeX Font Info:    ... okay on input line 16.
LaTeX Font Info:    Trying to load font information for U+msa on input line 17.


(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsa.fd
File: umsa.fd 2013/01/14 v3.01 AMS symbols A
)
LaTeX Font Info:    Trying to load font information for U+msb on input line 17.


(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsb.fd
File: umsb.fd 2013/01/14 v3.01 AMS symbols B
)
[1

{C:/Users/User/AppData/Local/MiKTeX/fonts/map/pdftex/pdftex.map}] [2]
[3] (explanation.aux)
 ***********
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
 ***********
 ) 
Here is how much of TeX's memory you used:
 1845 strings out of 467683
 26182 string characters out of 5415205
 444244 words of memory out of 5000000
 30938 multiletter control sequences out of 15000+600000
 637657 words of font info for 79 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 56i,9n,65p,209b,220s stack positions out of 10000i,1000n,20000p,200000b,200000s
<C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/c
mbx10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfo
nts/cm/cmbx12.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/publ
ic/amsfonts/cm/cmex10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/ty
pe1/public/amsfonts/cm/cmitt10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX
/fonts/type1/public/amsfonts/cm/cmmi10.pfb><C:/Users/User/AppData/Local/Program
s/MiKTeX/fonts/type1/public/amsfonts/cm/cmmi12.pfb><C:/Users/User/AppData/Local
/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmmi5.pfb><C:/Users/User/AppDat
a/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmmi7.pfb><C:/Users/User
/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr10.pfb><C:/Use
rs/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr12.pfb>
<C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr
17.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts
/cm/cmr5.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/am
sfonts/cm/cmr7.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/pub
lic/amsfonts/cm/cmsy10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/t
ype1/public/amsfonts/cm/cmsy5.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/
fonts/type1/public/amsfonts/cm/cmsy7.pfb><C:/Users/User/AppData/Local/Programs/
MiKTeX/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on explanation.pdf (3 pages, 203874 bytes).
PDF statistics:
 97 PDF objects out of 1000 (max. 8388607)
 0 named destinations out of 1000 (max. 500000)
 1 words of extra memory for PDF output out of 10000 (max. 10000000)

```

### `items/dyck_symmetric_functions/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 203874
sha256: 9520c0c81d95e594bfdc6b9616e3b6c9b2af76d3b02d5d8261f40b0d899b6275
```

### `items/dyck_symmetric_functions/explanation.synctex.gz`

```text
[binary artifact not expanded]
size_bytes: 22715
sha256: b29a51eac38cc49b9985ad228ed8f9176766a0e4e8806b1d699bed918cb744d7
```

### `items/dyck_symmetric_functions/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\newcommand{\dinv}{\operatorname{dinv}}
\newcommand{\DS}{\operatorname{DS}}
\newcommand{\DSstar}{\operatorname{DS}^{\ast}}
\newtheorem{theorem}{Theorem}
\newtheorem{conjecture}{Conjecture}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

\title{Dyck Symmetric Functions}
\author{}
\date{}

\begin{document}
\maketitle

\section{Status}

This note records the status of Dyck symmetric functions in the curated
repository.  The degenerate step \(t=0\) case is classical RSK/dual-RSK
combinatorics.  The classical Dyck step \(t=1\) case is proved in the 2026
preprint
\emph{Dyck Symmetric Functions and Applications to \(q,t\)-Catalan
Polynomials}.  The proof first establishes the dual case by an explicit
tableau insertion algorithm and then derives the affine, or nondual, case
from the dual case using the standard involution on symmetric functions.

The \(r=s t+1\) analogue below is conjectural for \(t>1\).  The accompanying
code checks systematic finite parameter boxes for both the affine and dual
identities.

\section{The \(r=s t+1\) Setup}

Fix a nonnegative integer step parameter \(t\).  For any finite integer
sequence \(x=(x_0,\ldots,x_{\ell-1})\), set
\[
  \dinv_t(x)=
  \sum_{0\le i<j<\ell} d_t(x_i,x_j),
\]
where
\[
  d_t(a,b)=
  \begin{cases}
    \max(0,a+t-b),& a\le b,\\
    \max(0,b+1+t-a),& a>b.
  \end{cases}
\]
An \emph{affine rational Dyck sequence of step \(t\)} is a finite integer
sequence satisfying
\[
  x_{i+1}\le x_i+t
  \qquad\text{for all }i.
\]
A \emph{dual rational Dyck sequence of step \(t\)} is a finite integer
sequence satisfying
\[
  x_{i+1}>x_i+t
  \qquad\text{for all }i.
\]

Let \(S\) be a finite multiset of integers.  A factorization of \(S\) is a
sequence of finite words whose concatenation is a rearrangement of \(S\).  It
is affine, respectively dual, if each factor is an affine, respectively dual,
rational Dyck sequence of step \(t\).  Define
\[
  \DS^{(t)}(S,d;\mathbf x)
  =
  \sum_{\substack{\mathcal F\text{ affine factorization of }S\\
                  \dinv_t(F_0F_1F_2\cdots)=d}}
  x^{\mathcal F}
\]
and
\[
  {\DSstar}^{(t)}(S,d;\mathbf x)
  =
  \sum_{\substack{\mathcal F\text{ dual factorization of }S\\
                  \dinv_t(F_0F_1F_2\cdots)=d}}
  x^{\mathcal F}.
\]

A rational Dyck tableau of step \(t\) is a left-aligned tableau whose rows are
dual rational Dyck sequences of step \(t\), and whose columns, read from
bottom to top, are affine rational Dyck sequences of step \(t\).  Let
\(\lambda(P)\) be its shape and let \(\operatorname{RR}(P)\) be its
row-reading word.

\section{The Degenerate \(t=0\) Case}

When \(t=0\), one has \(d_0(a,b)=0\) for all entries \(a,b\), so every
rearrangement of a fixed multiset lies in the single dinv class \(d=0\).
The dual factors are strictly increasing words, while the affine factors are
weakly increasing words.  The rational Dyck tableaux of step \(0\) are exactly
row-strict semistandard tableaux in our orientation: rows are strictly
increasing and columns are weakly increasing.

Thus the step \(0\) dual identity is the classical dual RSK correspondence for
strict biwords.  Fix a multiset \(S\) and a composition
\(\alpha=(\alpha_1,\ldots,\alpha_k)\).  A dual factorization of weight
\(\alpha\) is encoded as a biword whose top row contains \(i\) repeated
\(\alpha_i\) times and whose bottom row is the corresponding factor.  The
strictness of each factor is precisely the strictness condition in the
dual-RSK input.  Dual RSK gives a bijection with pairs \((P,Q)\) of common
shape, where \(P\) is row-strict semistandard of content \(S\), and \(Q\) is
ordinary semistandard of content \(\alpha\).  Equivalently, after transposing
or reversing the usual row/column conventions, this is the standard
RSK/Kostka description of Schur coefficients.

The affine \(t=0\) identity is the corresponding ordinary RSK statement for
weakly increasing factors, with the recording tableau convention transposed by
the usual involution.  Consequently the \(t=0\) specialization is known by
classical RSK theory; it is the baseline that the \(t=1\) insertion theorem
and the \(t>1\) conjectures generalize.

\section{Classical Theorem}

\begin{theorem}[Classical dual Dyck symmetric functions]
For every finite multiset \(S\) and every \(d\ge0\), the classical dual Dyck
symmetric function satisfies
\[
  \DSstar(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)}(\mathbf x),
\]
where \(P\) ranges over classical Dyck tableaux with entries \(S\) and
\(\dinv(\operatorname{RR}(P))=d\).
\end{theorem}

\begin{remark}
The proof in the 2026 preprint is constructive.  It gives an explicit
insertion algorithm sending dual Dyck factorizations to Dyck tableaux together
with semistandard recording data.  The local row insertion is iterated through
the rows of a tableau, and the reverse insertion proves bijectivity.
\end{remark}

\begin{theorem}[Classical affine Dyck symmetric functions]
For every finite multiset \(S\) and every \(d\ge0\), the classical affine Dyck
symmetric function satisfies
\[
  \DS(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)'}(\mathbf x),
\]
where the indexing set \(P\) is the same set of classical Dyck tableaux.
\end{theorem}

\begin{remark}
In the preprint, this nondual statement is derived from the dual statement by
comparing the fundamental-quasisymmetric expansions and applying the standard
involution \(\omega\), which sends \(s_\lambda\) to \(s_{\lambda'}\).
\end{remark}

\section{Conjectural \(r=s t+1\) Analogue}

\begin{conjecture}[Rational Dyck symmetric functions, \(r=s t+1\)]
Let \(S\) be a finite multiset of integers, let \(d\ge0\), and fix \(t\ge0\).
Then
\[
  \DS^{(t)}(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)'}(\mathbf x),
\]
where \(P\) ranges over rational Dyck tableaux of step \(t\) whose entries
are exactly \(S\) and whose row-reading word satisfies
\[
  \dinv_t(\operatorname{RR}(P))=d.
\]
Similarly,
\[
  {\DSstar}^{(t)}(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)}(\mathbf x),
\]
with the same indexing set of rational Dyck tableaux.
\end{conjecture}

\begin{remark}
The displayed statement is known for \(t=0\) by the classical RSK and dual
RSK correspondences, and for \(t=1\) by the 2026 Dyck insertion theorem.  For
\(t>1\), it is currently treated as a conjecture.  The directory
\texttt{code/} includes systematic finite checks over bounded multisets and
all occurring dinv values for the following official parameter boxes:
\[
  (t,A,L)=(2,10,10),\qquad (3,13,9),\qquad (4,16,8),
\]
where \(A\) is the alphabet size \(\{1,\ldots,A\}\) and \(L\) is the maximum
word length.  The same directory also includes Monte Carlo class checks: each
trial samples a word uniformly from \(\{1,\ldots,A\}^L\), fixes its multiset
and dinv value, and then exhaustively checks that sampled class.  The official
Monte Carlo runs use \(100\) sampled classes for
\[
  (t,A,L)=(2,11,12),\qquad (3,14,11),\qquad (4,17,10).
\]
The directory also includes the classical insertion algorithm code used for
the theorem-level case.
\end{remark}

\end{document}
```

### `items/dyck_symmetric_functions/html/body.html`

```html
<style>
  .dsf-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.1fr) minmax(280px, 0.9fr);
    gap: 1.25rem;
    align-items: start;
  }
  .dsf-panel {
    border: 1px solid #d7dde5;
    border-radius: 8px;
    padding: 1rem;
    background: #fff;
  }
  .dsf-toolbar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0.75rem 0;
  }
  .dsf-toolbar button,
  .dsf-toolbar select {
    border: 1px solid #a9b4c2;
    background: #f8fafc;
    border-radius: 6px;
    padding: 0.45rem 0.65rem;
    font: inherit;
  }
  .dsf-toolbar button:disabled {
    color: #8a94a3;
    background: #eef1f5;
  }
  .dsf-tableau {
    display: flex;
    flex-direction: column-reverse;
    gap: 0.35rem;
    min-height: 9rem;
    padding: 0.75rem;
    border: 1px solid #e4e8ee;
    background: #fbfcfe;
  }
  .dsf-row {
    display: flex;
    gap: 0.35rem;
    align-items: center;
  }
  .dsf-row-label {
    width: 4.25rem;
    color: #586272;
    font-size: 0.85rem;
  }
  .dsf-cell {
    min-width: 2.1rem;
    height: 2.1rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #8694a6;
    background: #ffffff;
    border-radius: 5px;
    font-weight: 600;
  }
  .dsf-active .dsf-cell {
    border-color: #1b6ca8;
    background: #eef7ff;
  }
  .dsf-insert .dsf-cell {
    border-color: #986b12;
    background: #fff7e6;
  }
  .dsf-evicted .dsf-cell {
    border-color: #7b3f98;
    background: #f8efff;
  }
  .dsf-log {
    min-height: 8rem;
    max-height: 14rem;
    overflow: auto;
    padding: 0.75rem;
    background: #101820;
    color: #e7edf3;
    border-radius: 6px;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    font-size: 0.86rem;
    white-space: pre-wrap;
  }
  .dsf-example-list {
    display: grid;
    gap: 0.75rem;
  }
  .dsf-example {
    border-left: 4px solid #1b6ca8;
    padding: 0.65rem 0.75rem;
    background: #f8fafc;
  }
  .dsf-kv {
    display: grid;
    grid-template-columns: 9rem minmax(0, 1fr);
    gap: 0.2rem 0.65rem;
    font-size: 0.92rem;
  }
  @media (max-width: 780px) {
    .dsf-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<section class="dsf-grid">
  <div class="dsf-panel">
    <h2>Insertion Walkthrough</h2>
    <p>
      The classical dual theorem is proved by inserting dual Dyck rows through
      a tableau.  Choose an example and step through the same row insertion
      logic used by the code.
    </p>
    <div class="dsf-toolbar">
      <select id="dsf-example"></select>
      <button id="dsf-reset" type="button">Reset</button>
      <button id="dsf-row-step" type="button">Apply row step</button>
      <button id="dsf-next-row" type="button">Move to next row</button>
    </div>
    <div id="dsf-tableau" class="dsf-tableau" aria-live="polite"></div>
    <div class="dsf-toolbar">
      <div id="dsf-carry" class="dsf-row dsf-insert"></div>
      <div id="dsf-evicted" class="dsf-row dsf-evicted"></div>
    </div>
    <div id="dsf-log" class="dsf-log"></div>
  </div>

  <div class="dsf-panel">
    <h2>Rational Examples</h2>
    <p>
      For \(r=s t+1\), the Schur-positive identities are conjectural for
      \(t&gt;1\).  The included checker verifies the following finite cases.
    </p>
    <div class="dsf-example-list">
      <div class="dsf-example">
        <strong>Step \(t=2\)</strong>
        <div class="dsf-kv">
          <span>Multiset</span><span>{1,2,2,3,3,4,5,7}</span>
          <span>Target dinv</span><span>17</span>
          <span>Tableaux</span><span>94</span>
          <span>Shapes</span><span>(2,2,1,1,1,1), (2,1,1,1,1,1,1), (1^8)</span>
          <span>Phenomenon</span><span>large affine side; ordinary-shape dual side vanishes in three variables because all shapes have more than three rows.</span>
        </div>
      </div>
      <div class="dsf-example">
        <strong>Step \(t=3\)</strong>
        <div class="dsf-kv">
          <span>Multiset</span><span>{0,0,0,4}</span>
          <span>Target dinv</span><span>9</span>
          <span>Tableaux</span><span>2</span>
          <span>Shapes</span><span>(2,1,1), (1,1,1,1)</span>
          <span>Phenomenon</span><span>both affine and dual Schur comparisons are nonzero in three variables.</span>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
(function () {
  const examples = [
    {
      name: "Single bump and append",
      tableau: [[0, 3, 6]],
      inserted: [1, 4],
      note: "Shows replacement followed by a terminal append."
    },
    {
      name: "Two-row propagation",
      tableau: [[0, 4], [1, 5]],
      inserted: [2, 6],
      note: "An evicted row is carried upward into the next row."
    },
    {
      name: "Chain comparison",
      tableau: [[0, 2, 4], [1, 4, 7]],
      inserted: [1, 3, 5],
      note: "Shows a maximal +2-chain interaction."
    }
  ];

  const select = document.getElementById("dsf-example");
  const resetButton = document.getElementById("dsf-reset");
  const rowStepButton = document.getElementById("dsf-row-step");
  const nextRowButton = document.getElementById("dsf-next-row");
  const tableauNode = document.getElementById("dsf-tableau");
  const carryNode = document.getElementById("dsf-carry");
  const evictedNode = document.getElementById("dsf-evicted");
  const logNode = document.getElementById("dsf-log");

  let state;

  examples.forEach((example, index) => {
    const option = document.createElement("option");
    option.value = String(index);
    option.textContent = example.name;
    select.appendChild(option);
  });

  function cloneRows(rows) {
    return rows.map(row => row.slice());
  }

  function chainStartingAt(seq, index) {
    let stop = index + 1;
    while (stop < seq.length && seq[stop] === seq[stop - 1] + 2) stop += 1;
    return seq.slice(index, stop);
  }

  function rowsertOne(row, carry) {
    const first = carry[0];
    let index = row.findIndex(value => first <= value + 1);
    if (index === -1) {
      row.push(first);
      carry.shift();
      return { caseName: "Case 0", message: `${first} appends to the row.` };
    }
    if (first <= row[index]) {
      const old = row[index];
      row[index] = first;
      carry.shift();
      return { caseName: "Case 1", evicted: [old], message: `${first} replaces ${old}.` };
    }
    const rowChain = chainStartingAt(row, index);
    const carryChain = chainStartingAt(carry, 0);
    if (rowChain.length <= carryChain.length) {
      const inserted = carry.splice(0, rowChain.length);
      const evicted = row.splice(index, rowChain.length, ...inserted);
      return {
        caseName: "Case 2",
        evicted,
        message: `The input chain [${inserted.join(", ")}] replaces row chain [${evicted.join(", ")}].`
      };
    }
    const moved = carry.splice(0, carryChain.length);
    return {
      caseName: "Case 3",
      evicted: moved,
      message: `The shorter input chain [${moved.join(", ")}] passes upward.`
    };
  }

  function renderRow(label, values, className) {
    const row = document.createElement("div");
    row.className = `dsf-row ${className || ""}`;
    const labelNode = document.createElement("span");
    labelNode.className = "dsf-row-label";
    labelNode.textContent = label;
    row.appendChild(labelNode);
    values.forEach(value => {
      const cell = document.createElement("span");
      cell.className = "dsf-cell";
      cell.textContent = String(value);
      row.appendChild(cell);
    });
    if (!values.length) {
      const empty = document.createElement("span");
      empty.textContent = "empty";
      empty.style.color = "#6b7280";
      row.appendChild(empty);
    }
    return row;
  }

  function render() {
    tableauNode.innerHTML = "";
    state.rows.forEach((row, index) => {
      const active = index === state.rowIndex && state.carry.length ? "dsf-active" : "";
      tableauNode.appendChild(renderRow(`row ${index}`, row, active));
    });
    carryNode.innerHTML = "";
    carryNode.appendChild(renderRow("carry", state.carry, "dsf-insert"));
    evictedNode.innerHTML = "";
    evictedNode.appendChild(renderRow("evicted", state.evicted, "dsf-evicted"));
    logNode.textContent = state.log.join("\n");
    rowStepButton.disabled = !(state.carry.length && state.rowIndex >= 0);
    nextRowButton.disabled = state.carry.length || state.rowIndex < 0 || !state.evicted.length;
  }

  function reset() {
    const example = examples[Number(select.value)];
    state = {
      rows: cloneRows(example.tableau),
      carry: example.inserted.slice(),
      rowIndex: example.tableau.length - 1,
      evicted: [],
      log: [`Example: ${example.name}`, example.note, `Initial inserted row: [${example.inserted.join(", ")}]`]
    };
    render();
  }

  rowStepButton.addEventListener("click", () => {
    if (!state.carry.length || state.rowIndex < 0) return;
    const result = rowsertOne(state.rows[state.rowIndex], state.carry);
    const chunk = result.evicted || [];
    state.evicted.push(...chunk);
    state.log.push(`row ${state.rowIndex}: ${result.caseName}. ${result.message}`);
    if (!state.carry.length) {
      if (state.evicted.length) {
        state.log.push(`row ${state.rowIndex}: row complete; evicted row [${state.evicted.join(", ")}] is ready to move upward.`);
      } else {
        state.log.push(`row ${state.rowIndex}: insertion stops in this row.`);
      }
    }
    render();
  });

  nextRowButton.addEventListener("click", () => {
    state.rowIndex -= 1;
    if (state.rowIndex < 0 && state.evicted.length) {
      state.rows.unshift(state.evicted.slice());
      state.rowIndex = -1;
      state.log.push(`A new bottom row [${state.evicted.join(", ")}] is created.`);
      state.evicted = [];
    } else if (state.rowIndex >= 0) {
      state.carry = state.evicted.slice();
      state.evicted = [];
      state.log.push(`Move to row ${state.rowIndex}.`);
    }
    render();
  });

  select.addEventListener("change", reset);
  resetButton.addEventListener("click", reset);
  reset();
})();
</script>
```

### `items/dyck_symmetric_functions/item.yaml`

```yaml
title: Dyck Symmetric Functions
slug: dyck_symmetric_functions
status_summary: Classical Dyck symmetric functions are proved in the 2026 preprint; the r == 1 mod s analogue is conjectural with systematic finite checks.
source_paths:
  - ../Dyck/paper/working_drafts/arxiv_submission.tex
  - ../Dyck/paper/research_notes/rational_generalizations.tex
  - ../Dyck/code/codex_project/red_team_rational_dyck_generalization.py
downloads:
  - explanation.tex
```

### `items/dyck_symmetric_functions/README.md`

```markdown
# Dyck Symmetric Functions

Status summary: Classical Dyck symmetric functions are proved in the 2026
preprint; the `r = s*t + 1` analogue is conjectural and supported here by
systematic finite checks over stated parameter boxes.

## Summary

This item curates Dyck symmetric functions and dual Dyck symmetric functions.
The classical case is theorem-level material from the 2026 preprint
*Dyck Symmetric Functions and Applications to q,t-Catalan Polynomials*.

The general `r = s*t + 1` version is included as a conjectural extension.  The
curated code checks systematic finite parameter boxes for both the
affine/nondual and dual versions of the conjecture.

## Provenance

Source repository: `Dyck`

Source paths:

- `../Dyck/paper/working_drafts/arxiv_submission.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/03_row_and_tableau_insertion.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/03_tableau_bijection_schur.tex`
- `../Dyck/paper/research_notes/rational_generalizations.tex`
- `../Dyck/code/codex_project/paper_algorithms/row_insertion.py`
- `../Dyck/code/codex_project/paper_algorithms/tableau_insertion.py`
- `../Dyck/code/codex_project/paper_algorithms/rational_dyck.py`
- `../Dyck/code/codex_project/red_team_rational_dyck_generalization.py`

Transfer type: curated writeup with adapted code.

## Layers

Python layer: present.  It includes the classical row/tableau insertion
algorithm and systematic finite checks for bounded `r = s*t + 1` cases.

LaTeX layer: present as a concise statement/status note.

HTML layer: present with an interactive insertion walkthrough and rational
examples.

## Status

- Classical dual Dyck symmetric functions: theorem, proved in the 2026
  preprint by an explicit tableau insertion algorithm.
- Classical affine/nondual Dyck symmetric functions: theorem, derived from
  the dual case using the standard involution on symmetric functions.
- `r = s*t + 1` affine/nondual and dual analogues: conjectures, with
  systematic finite checks included in
  `code/check_rational_dyck_generalization.py`.  The official bounded checks
  skip `t=1` because it is proved; check all multisets and all occurring dinv
  values for `t=2`, alphabet size `A=10`, length at most `L=10`; `t=3`,
  alphabet size `A=13`, length at most `L=9`; and `t=4`, alphabet size `A=16`,
  length at most `L=8`.
- General rational `r/s` Dyck symmetric functions: not part of this item.

## Review Needs

- Add a full bibliographic reference once publication metadata is added to the
  repository.
- Expand the LaTeX note into a complete self-contained exposition.
- Investigate further optimizations if larger length or alphabet boxes are
  needed.
```

### `items/qt_catalan_computer_assisted_proofs_2024/assets/.gitkeep`

```text

```

### `items/qt_catalan_computer_assisted_proofs_2024/code/qt_assisted_2024.py`

```python
"""Computer-assisted checks for Lemma 2 and Lemma 3 of Section 9.

This is a curated port of
``Conjectures-and-Computations/qt-catalan/qt-assisted.py``.  It keeps the
source computation's position-coordinate conventions and finite cutoff
``dstar = 20`` while wrapping the script in a reproducible command-line entry
point.
"""

from __future__ import annotations

import argparse
import math
import time
from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Sequence


Path = tuple[int, ...]
Monomial = tuple[int, int]


@dataclass(frozen=True)
class DyckPathRecord:
    m: int
    degree: int
    path: Path


@dataclass(frozen=True)
class Lemma3LayerResult:
    m: int
    ell: int
    path_count: int
    plus_count: int
    minus_count: int
    all_count: int
    ok: bool


def alpha(a: int, b: int, m: int) -> int:
    if a <= b:
        return min(b - a, m)
    return min(a - b - 1, m)


def alpha0(a: int, m: int) -> int:
    return max(0, a - m)


def point(path: Sequence[int], m: int) -> int:
    pt = 0
    for i in range(len(path) - 1, -1, -1):
        if path[i] - path[-1] > -m:
            pt = i
    return pt


def pair(path: Sequence[int], m: int) -> int:
    pr = len(path) - 2
    for i in range(len(path) - 3, -1, -1):
        if path[i] - path[i + 2] >= -m:
            pr = i
    return pr


def right(path: Sequence[int], m: int) -> Path:
    values = tuple(path)
    pt = point(values, m)
    pr = pair(values, m)
    if pt <= pr + 1 and pt < len(values) - 1:
        return values[: pt + 1] + (values[-1] + 1,) + values[pt + 1 : -1]
    return values


def left(path: Sequence[int], m: int) -> Path:
    values = tuple(path)
    pr = pair(values, m)
    if values[-1] - values[pr + 1] >= -m - 1:
        return values[: pr + 1] + values[pr + 2 :] + (values[pr + 1] - 1,)
    return values


def lowest(path: Sequence[int], m: int) -> Path:
    current = tuple(path)
    previous: Path | None = None
    while current != previous:
        previous = current
        current = right(current, m)
    return current


def height(path: Sequence[int]) -> int:
    greatest = 0
    j = 0
    for i, value in enumerate(path):
        if value >= greatest:
            greatest = value
            j = i
    return (greatest - 1) * (len(path) - 1) + j - sum(path)


def lstar(dstar: int, m: int) -> int:
    return int(math.ceil(dstar / m + 1.001))


def extend_degree(prefix: Sequence[int], value: int, m: int, current_degree: int) -> int:
    degree = current_degree
    for k in range(1, len(prefix)):
        degree += alpha(prefix[k], value, m)
    degree -= alpha0(value, m)
    return degree


def generate_records(*, max_m: int = 20, dstar: int = 20, verbose: bool = False) -> list[DyckPathRecord]:
    """Generate all records used by the source computation.

    The source script uses records ``[m, d, [a_0,...,a_l]]``.  This port stores
    them as ``DyckPathRecord`` values with tuple paths.
    """

    records: list[DyckPathRecord] = []
    for m in range(max_m, 0, -1):
        if verbose:
            print(f"generating Dyck paths with m={m}", flush=True)
        max_length = lstar(dstar, m) + 1
        all_for_m = [DyckPathRecord(m, 0, (0,))]
        frontier = [DyckPathRecord(m, 0, (0,))]
        while len(frontier[0].path) < max_length:
            next_frontier: list[DyckPathRecord] = []
            for record in frontier:
                prefix = record.path
                for value in range(prefix[-1] + m + 1):
                    degree = extend_degree(prefix, value, m, record.degree)
                    if degree <= dstar:
                        child = DyckPathRecord(m, degree, prefix + (value,))
                        next_frontier.append(child)
                        all_for_m.append(child)
            frontier = next_frontier
        records.extend(all_for_m)
    return records


def string_okay(record: DyckPathRecord, *, dstar: int = 20) -> bool:
    m = record.m
    path = record.path
    target_length = lstar(dstar, m) + 1
    if len(path) < target_length:
        return True
    if len(path) != target_length:
        return True
    if path[1] > 0:
        return True
    m_total = m * len(path) * (len(path) - 1) // 2
    bound = m_total - height(path) - record.degree
    return sum(lowest(path, m)) <= bound


def check_lemma2(records: Sequence[DyckPathRecord], *, dstar: int = 20) -> tuple[bool, list[DyckPathRecord]]:
    failures = [record for record in records if not string_okay(record, dstar=dstar)]
    return not failures, failures


def sort_monomials(values: Iterable[Monomial]) -> list[Monomial]:
    return sorted(values, key=lambda item: item[1] + item[0] / 1000)


def grouped_by_m_and_length(records: Sequence[DyckPathRecord]) -> Iterable[list[DyckPathRecord]]:
    start = 0
    ordered = list(records)
    while start < len(ordered):
        end = start
        while (
            end < len(ordered) - 1
            and ordered[end].m == ordered[end + 1].m
            and len(ordered[end].path) == len(ordered[end + 1].path)
        ):
            end += 1
        end += 1
        yield ordered[start:end]
        start = end


def check_lemma3(records: Sequence[DyckPathRecord], *, verbose: bool = False) -> tuple[bool, list[Lemma3LayerResult]]:
    results: list[Lemma3LayerResult] = []
    all_ok = True
    for layer in grouped_by_m_and_length(records):
        ell = len(layer[0].path) - 1
        if ell == 0:
            continue
        m = layer[0].m
        m_total = m * (ell + 1) * ell // 2
        plus: list[Monomial] = []
        minus: list[Monomial] = []
        all_monomials: list[Monomial] = []

        for record in layer:
            path = record.path
            degree = record.degree
            path_area = sum(path)
            all_monomials.append((path_area, m_total - degree))
            if path[1] != 0:
                continue
            if path_area <= m_total - path_area - degree:
                for q_degree in range(path_area, int(m_total - path_area - degree + 1)):
                    plus.append((q_degree, m_total - degree))
            else:
                for q_degree in range(int(m_total - path_area - degree + 1), path_area):
                    minus.append((q_degree, m_total - degree))

        ok = sort_monomials(plus) == sort_monomials(all_monomials + minus)
        all_ok = all_ok and ok
        result = Lemma3LayerResult(
            m=m,
            ell=ell,
            path_count=len(layer),
            plus_count=len(plus),
            minus_count=len(minus),
            all_count=len(all_monomials),
            ok=ok,
        )
        results.append(result)
        if verbose:
            status = "PASS" if ok else "FAIL"
            print(f"lemma3 m={m} ell={ell}: {status}", flush=True)
    return all_ok, results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=20, help="largest m to include; source value is 20")
    parser.add_argument("--dstar", type=int, default=20, help="degree cutoff; source value is 20")
    parser.add_argument("--lemma", choices=("all", "2", "3"), default="all", help="which check to run")
    parser.add_argument("--verbose", action="store_true", help="print per-m and per-layer progress")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    start = time.perf_counter()
    records = generate_records(max_m=args.max_m, dstar=args.dstar, verbose=args.verbose)
    print("qt-Catalan 2024 computer-assisted checks")
    print(f"  max_m: {args.max_m}")
    print(f"  dstar: {args.dstar}")
    print(f"  generated_records: {len(records)}")
    by_m = Counter(record.m for record in records)
    print(f"  records_by_m: {dict(sorted(by_m.items()))}")

    ok = True
    if args.lemma in ("all", "2"):
        lemma2_ok, failures = check_lemma2(records, dstar=args.dstar)
        print(f"  lemma2_status: {'PASS' if lemma2_ok else 'FAIL'}")
        print(f"  lemma2_failures: {len(failures)}")
        for failure in failures[:5]:
            print(f"  lemma2_failure: m={failure.m} degree={failure.degree} path={failure.path}")
        ok = ok and lemma2_ok

    if args.lemma in ("all", "3"):
        lemma3_ok, layer_results = check_lemma3(records, verbose=args.verbose)
        print(f"  lemma3_status: {'PASS' if lemma3_ok else 'FAIL'}")
        print(f"  lemma3_layers_checked: {len(layer_results)}")
        failures = [result for result in layer_results if not result.ok]
        print(f"  lemma3_failures: {len(failures)}")
        if layer_results:
            print(
                "  lemma3_last_layer: "
                f"m={layer_results[-1].m} ell={layer_results[-1].ell} "
                f"path_count={layer_results[-1].path_count}"
            )
        for failure in failures[:5]:
            print(f"  lemma3_failure: m={failure.m} ell={failure.ell}")
        ok = ok and lemma3_ok

    print(f"  elapsed_seconds: {time.perf_counter() - start:.3f}")
    print(f"  status: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### `items/qt_catalan_computer_assisted_proofs_2024/code/qt_assisted_2024_expected_output.txt`

```text
qt-Catalan 2024 computer-assisted checks
  max_m: 20
  dstar: 20
  generated_records: 5692942
  records_by_m: {1: 3893823, 2: 992623, 3: 266022, 4: 204889, 5: 120248, 6: 52429, 7: 14881, 8: 19032, 9: 23326, 10: 27779, 11: 4315, 12: 5079, 13: 5846, 14: 6616, 15: 7389, 16: 8165, 17: 8944, 18: 9726, 19: 10511, 20: 11299}
  lemma2_status: PASS
  lemma2_failures: 0
  lemma3_status: PASS
  lemma3_layers_checked: 106
  lemma3_failures: 0
  lemma3_last_layer: m=1 ell=22 path_count=607712
  status: PASS
```

### `items/qt_catalan_computer_assisted_proofs_2024/code/README.md`

```markdown
# Code

`qt_assisted_2024.py` is a curated port of
`Conjectures-and-Computations/qt-catalan/qt-assisted.py`.

Run from the `Combinatorics` directory:

````powershell
python items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py
````

Or from the repository root:

````powershell
python Combinatorics\items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py
````

The default run preserves the source parameters:

- `max_m = 20`
- `dstar = 20`

It generates all source-relevant position-coordinate `m`-Dyck path records,
checks the Lemma 2 string-bound condition, and checks the Lemma 3 monomial
multiset identity for every generated `(m, ell)` layer.

Expected default summary:

````text
generated_records: 5692942
lemma2_status: PASS
lemma2_failures: 0
lemma3_status: PASS
lemma3_layers_checked: 106
lemma3_failures: 0
status: PASS
````

The full default run took about 57 seconds in the current workspace.
```

### `items/qt_catalan_computer_assisted_proofs_2024/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}
\usepackage[margin=1in]{geometry}

\newcommand{\degr}{\operatorname{degr}}

\title{\(q,t\)-Catalan Computer-Assisted Proofs 2024}
\author{}
\date{}

\begin{document}
\maketitle

\section{Purpose}

This item records the computer-assisted verification used for Lemma 2 and
Lemma 3 of Section 9 of Graham Hawkes's paper
\emph{A conjectured formula for the rational \(q,t\)-Catalan polynomial}
(Annals of Combinatorics 28, 749--795, 2024; arXiv:2208.00577).

The source computation is
\[
  \texttt{Conjectures-and-Computations/qt-catalan/qt-assisted.py}.
\]
The curated script
\[
  \texttt{code/qt\_assisted\_2024.py}
\]
is a reproducibility wrapper around the same finite checks.  It keeps the
source conventions and default cutoff \(d^*=20\), but replaces top-level script
side effects by a command-line entry point and stable summary output.

\section{Objects}

The computation uses position coordinates for \(m\)-Dyck paths.  A path is a
finite sequence
\[
  A=(a_0,\ldots,a_\ell),\qquad a_0=0,\qquad
  0\le a_{i+1}\le a_i+m.
\]
For integers \(a,b\), define
\[
  \alpha(a,b;m)=
  \begin{cases}
    \min(b-a,m), & a\le b,\\
    \min(a-b-1,m), & a>b,
  \end{cases}
  \qquad
  \alpha_0(a;m)=\max(0,a-m).
\]
The script generates paths together with the degree statistic obtained
incrementally from these \(\alpha\)-terms.  When appending a new final entry
\(j\) to a prefix \(x=(a_0,\ldots,a_{r-1})\), the degree increment is
\[
  \sum_{k=1}^{r-1}\alpha(a_k,j;m)-\alpha_0(j;m).
\]

The finite cutoff is \(d^*=20\).  For each \(1\le m\le20\), the script sets
\[
  \ell^*(m)=\left\lceil\frac{20}{m}+1.001\right\rceil
\]
and generates every path of length at most \(\ell^*(m)+1\) whose generated
degree is at most \(20\).  These are exactly the paths needed by the source
computation for the two Section 9 lemmas.

\section{Lemma 2 Check}

The source code's Lemma 2 check is a finite string-length bound.  It uses the
paper's point, pair, right, and lowest operations on position-coordinate paths.
For a path \(A\), let \(b=\operatorname{lowest}(A)\) be the terminal path
obtained by repeatedly applying the right map.  The computation also uses the
height
\[
  h(A)=(g-1)\ell+j-\sum_i a_i,
\]
where \(g\) is the largest entry of \(A\) and \(j\) is the last index at which
that largest entry is attained.

Only the boundary case needs checking: paths of length \(\ell^*(m)+1\) with
second entry \(0\).  For each such path, the script verifies
\[
  \operatorname{area}(b)\le
  m\binom{\ell^*(m)+1}{2}-h(A)-\degr(A).
\]
All shorter paths, and the length-boundary paths outside this maximal class,
are treated as automatic cases just as in the source script.

\section{Lemma 3 Check}

The Lemma 3 computation is a finite monomial identity checked separately for
each pair \((m,\ell)\) appearing in the generated records.  Put
\[
  M=m\binom{\ell+1}{2}.
\]
For every generated path \(A\) of fixed \(m\) and length \(\ell+1\), the left
side contributes the monomial record
\[
  (\operatorname{area}(A),\,M-\degr(A)).
\]
The right side is built from the subfamily with second entry \(0\).  If
\(a=\operatorname{area}(A)\) and \(d=\degr(A)\), this subfamily contributes a
positive interval
\[
  (j,M-d),\qquad a\le j\le M-a-d,
\]
when \(a\le M-a-d\), and a negative correction interval
\[
  (j,M-d),\qquad M-a-d+1\le j<a,
\]
when \(M-a-d<a\).  The check is
\[
  \text{positive interval multiset}
  =
  \text{all path monomials}+\text{negative correction multiset}.
\]
The script sorts both multisets by the source ordering and compares them
exactly.

\section{Reproducible Run}

Run the curated checker from the repository root by executing
\[
  \texttt{python items/qt\_catalan\_computer\_assisted\_proofs\_2024/code/qt\_assisted\_2024.py}
\]
from inside the \(\texttt{Combinatorics}\) directory, or equivalently by giving
the full path to the script.

The default run performed for this item generated \(5{,}692{,}942\) records.
Both checks passed:
\[
  \texttt{lemma2\_status: PASS},\qquad
  \texttt{lemma3\_status: PASS}.
\]
The Lemma 3 comparison checked 106 nontrivial \((m,\ell)\)-layers.  The final
layer in the default source ordering was \(m=1\), \(\ell=22\), with 607,712
records.  The measured run time in this environment was about 57 seconds.

\section{Status}

This is proof-supporting computation, not experimental evidence for a new
conjecture.  The mathematical proof in the 2024 paper reduces the remaining
parts of Lemma 2 and Lemma 3 to the finite checks above.  The curated code is
intended to make those checks reproducible from the archived source script.

\end{document}
```

### `items/qt_catalan_computer_assisted_proofs_2024/html/body.html`

```html
<p>
  This item packages the finite computation used to complete Lemma 2 and
  Lemma 3 of Section 9 of Graham Hawkes's 2024 rational
  <code>q,t</code>-Catalan paper.
</p>

<p>
  The source script is
  <code>Conjectures-and-Computations/qt-catalan/qt-assisted.py</code>. The
  curated script <code>code/qt_assisted_2024.py</code> preserves the source
  cutoff <code>dstar=20</code> and the same position-coordinate
  <code>m</code>-Dyck path conventions, but gives a reproducible command-line
  summary.
</p>

<p>
  The Lemma 2 check verifies a finite string-bound condition for the boundary
  paths selected by the source proof. The Lemma 3 check verifies, for every
  generated <code>(m, ell)</code> layer, that the positive monomial-string
  multiset equals the multiset of all generated path monomials together with
  the negative correction multiset.
</p>

<p>
  The default run generated 5,692,942 records, checked 106 nontrivial Lemma 3
  layers, and returned <code>PASS</code> for both Lemma 2 and Lemma 3.
</p>
```

### `items/qt_catalan_computer_assisted_proofs_2024/item.yaml`

```yaml
title: qt-Catalan Computer-Assisted Proofs 2024
slug: qt_catalan_computer_assisted_proofs_2024
status_summary: Reproducible proof-supporting computation for Lemma 2 and Lemma 3 of the 2024 rational q,t-Catalan paper.
source_paths:
  - ../Conjectures-and-Computations/qt-catalan/qt-assisted.py
  - ../Conjectures-and-Computations/testing/catest.py
downloads:
  - explanation.tex
  - code/qt_assisted_2024.py
  - code/qt_assisted_2024_expected_output.txt
```

### `items/qt_catalan_computer_assisted_proofs_2024/README.md`

```markdown
# qt-Catalan Computer-Assisted Proofs 2024

Status summary: Reproducible proof-supporting computation for Lemma 2 and
Lemma 3 of Section 9 of the 2024 rational `q,t`-Catalan paper.

## Summary

This item curates the computer-assisted verification used in Graham Hawkes,
*A conjectured formula for the rational q,t-Catalan polynomial*, Annals of
Combinatorics 28, 749-795 (2024).  The computation is not a general
conjecture-testing script; it is the finite verification needed to complete
Lemma 2 and Lemma 3 of Section 9.

## Provenance

Source repository: `Conjectures-and-Computations`

Primary source path:

- `../Conjectures-and-Computations/qt-catalan/qt-assisted.py`

Related older context:

- `../Conjectures-and-Computations/testing/catest.py`

Transfer type: adapted reproducibility wrapper preserving the source
computation.

## Layers

Python layer: `code/qt_assisted_2024.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- Lemma 2 finite string-bound check: packaged and passing.
- Lemma 3 finite monomial multiset check: packaged and passing.
- Default run: 5,692,942 generated records; 106 Lemma 3 layers; status `PASS`.

## Review Notes

- `qt-assisted.py` is the source of record for this item.
- `qt-conjecture.py` belongs to the separate rational `q,t`-Catalan formula
  item.
- `johnson.py` and `poset_decomps.txt` concern Armstrong/Johnson poset
  decomposition material and are not part of this proof-supporting computation.
```

### `items/qt_catalan_middle_coefficients/assets/.gitkeep`

```text

```

### `items/qt_catalan_middle_coefficients/code/check_flat_middle_coefficients.py`

```python
"""Bounded checks for flat middle coefficients of classical q,t-Catalan.

The checked statement is the finite version of the flat-middle consequence of
the Dyck-skeleton decomposition formula.  For each checked n and each
0 <= d <= 2n-8, this script computes direct coefficients of

    C_n(q,t) = sum_D q^area(D) t^dinv(D)

over all Dyck area sequences D of length n, then verifies that the coefficients
of q^j t^(M-d-j), d <= j <= M-2d, are all equal to the number of special Dyck
skeletons of length n and deficit d.

These are bounded computational checks.  They are not a proof of the
flat-middle theorem or of the larger flat-middle conjecture.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import comb
from typing import Sequence


def is_dyck_sequence(seq: Sequence[int]) -> bool:
    """Return whether seq is a Dyck area sequence in the source convention."""

    return (
        len(seq) > 0
        and seq[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in seq)
        and all(seq[index + 1] <= seq[index] + 1 for index in range(len(seq) - 1))
    )


def generate_dyck_sequences(n: int) -> list[tuple[int, ...]]:
    """Generate all Dyck area sequences of length n."""

    if n <= 0:
        raise ValueError("n must be positive")

    out: list[tuple[int, ...]] = []

    def rec(seq: list[int]) -> None:
        if len(seq) == n:
            out.append(tuple(seq))
            return
        for value in range(seq[-1] + 2):
            rec(seq + [value])

    rec([0])
    return out


def area_statistic(seq: Sequence[int]) -> int:
    return sum(seq)


def di_statistic(seq: Sequence[int]) -> int:
    """Count pairs i<j with seq[i] = seq[j]+1."""

    values = tuple(seq)
    return sum(
        1
        for left in range(len(values))
        for right in range(left + 1, len(values))
        if values[left] == values[right] + 1
    )


def nv_statistic(seq: Sequence[int]) -> int:
    """Count pairs i<j with seq[i] = seq[j]."""

    values = tuple(seq)
    return sum(
        1
        for left in range(len(values))
        for right in range(left + 1, len(values))
        if values[left] == values[right]
    )


def dinv_statistic(seq: Sequence[int]) -> int:
    return di_statistic(seq) + nv_statistic(seq)


def deficit_pair_count(seq: Sequence[int]) -> int:
    """Count the source paper's two explicit deficit-pair types."""

    values = tuple(seq)
    total = 0
    first_seen: set[int] = set()
    for left, left_value in enumerate(values):
        left_is_first = left_value not in first_seen
        first_seen.add(left_value)
        for right in range(left + 1, len(values)):
            right_value = values[right]
            type_a = left_value > right_value + 1
            type_b = left_value < right_value and not left_is_first
            if type_a or type_b:
                total += 1
    return total


def deficit_statistic(seq: Sequence[int]) -> int:
    n = len(seq)
    return comb(n, 2) - area_statistic(seq) - dinv_statistic(seq)


def find_extractable_position(seq: Sequence[int], *, include_final: bool = True) -> int | None:
    """Return the leftmost extractable position, if any."""

    values = tuple(seq)
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        if sum(1 for prior in values[:index] if prior == value - 1) != 1:
            continue
        if index + 1 < len(values) and values[index + 1] > value:
            continue
        return index
    return None


def is_full_dyck_skeleton(seq: Sequence[int]) -> bool:
    return is_dyck_sequence(seq) and find_extractable_position(seq, include_final=True) is None


def excluded_full_skeleton(n: int) -> tuple[int, ...]:
    """Return the exceptional full skeleton excluded from the special count."""

    if n < 4:
        return ()
    return (0, 0) + (1,) + (0,) * (n - 4) + (1,)


def is_special_dyck_skeleton(seq: Sequence[int]) -> bool:
    values = tuple(seq)
    return is_full_dyck_skeleton(values) and values != excluded_full_skeleton(len(values))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_check(n_min: int, n_max: int, max_representative_bands: int) -> dict[str, object]:
    total_sequences = 0
    dyck_validation_checks = 0
    formula_pair_deficit_checks = 0
    coefficient_total_checks = 0
    checked_bands = 0
    checked_coefficients = 0
    flat_band_checks = 0
    skeleton_match_checks = 0
    sequences_by_n: dict[int, int] = {}
    special_skeleton_counts: dict[int, dict[int, int]] = {}
    representative_bands: list[dict[str, object]] = []

    for n in range(n_min, n_max + 1):
        m_total = comb(n, 2)
        coeffs: Counter[tuple[int, int]] = Counter()
        skeleton_counts: Counter[int] = Counter()
        sequences = generate_dyck_sequences(n)
        sequences_by_n[n] = len(sequences)
        total_sequences += len(sequences)

        for seq in sequences:
            require(is_dyck_sequence(seq), f"generator produced non-Dyck sequence: {seq}")
            dyck_validation_checks += 1

            area = area_statistic(seq)
            dinv = dinv_statistic(seq)
            formula_defc = deficit_statistic(seq)
            pair_defc = deficit_pair_count(seq)
            require(
                formula_defc == pair_defc,
                "formula/pair deficit mismatch: "
                f"n={n}, seq={seq}, formula={formula_defc}, pairs={pair_defc}",
            )
            require(
                formula_defc == m_total - area - dinv,
                f"deficit formula mismatch: n={n}, seq={seq}",
            )
            formula_pair_deficit_checks += 1
            coeffs[(area, dinv)] += 1

            if is_special_dyck_skeleton(seq):
                require(
                    area <= formula_defc,
                    f"special skeleton violates area <= deficit: n={n}, seq={seq}",
                )
                skeleton_counts[formula_defc] += 1

        require(
            sum(coeffs.values()) == len(sequences),
            f"coefficient dictionary total mismatch for n={n}",
        )
        coefficient_total_checks += 1
        special_skeleton_counts[n] = dict(sorted(skeleton_counts.items()))

        for d in range(0, 2 * n - 7):
            target = skeleton_counts[d]
            band: list[tuple[int, int, int]] = []
            for j in range(d, m_total - 2 * d + 1):
                coeff = coeffs[(j, m_total - d - j)]
                band.append((j, m_total - d - j, coeff))
                require(
                    coeff == target,
                    "flat middle coefficient mismatch: "
                    f"n={n}, d={d}, target_special_skeletons={target}, "
                    f"at q^{j} t^{m_total - d - j} coefficient={coeff}, band={band}",
                )
                checked_coefficients += 1
                skeleton_match_checks += 1

            require(
                len({coeff for _, _, coeff in band}) <= 1,
                f"band is not flat: n={n}, d={d}, band={band}",
            )
            flat_band_checks += 1
            checked_bands += 1

            if len(representative_bands) < max_representative_bands and (
                d > 0 or not representative_bands
            ):
                representative_bands.append(
                    {
                        "n": n,
                        "d": d,
                        "special_skeleton_count": target,
                        "band": band,
                    }
                )

    require(
        any(item["d"] > 0 for item in representative_bands),
        "representative bands did not include a nonzero deficit",
    )

    return {
        "n_min": n_min,
        "n_max": n_max,
        "total_sequences": total_sequences,
        "sequences_by_n": sequences_by_n,
        "special_skeleton_counts": special_skeleton_counts,
        "dyck_validation_checks": dyck_validation_checks,
        "formula_pair_deficit_checks": formula_pair_deficit_checks,
        "coefficient_total_checks": coefficient_total_checks,
        "checked_bands": checked_bands,
        "checked_coefficients": checked_coefficients,
        "flat_band_checks": flat_band_checks,
        "skeleton_match_checks": skeleton_match_checks,
        "representative_bands": representative_bands,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-min", type=int, default=4, help="smallest n to check")
    parser.add_argument("--n-max", type=int, default=8, help="largest n to check")
    parser.add_argument(
        "--representative-bands",
        type=int,
        default=10,
        help="maximum number of representative bands to print",
    )
    args = parser.parse_args()

    if args.n_min < 4 or args.n_max < args.n_min:
        raise SystemExit("require 4 <= n-min <= n-max")
    if args.representative_bands < 1:
        raise SystemExit("representative-bands must be positive")

    summary = run_check(args.n_min, args.n_max, args.representative_bands)

    print("Flat middle coefficient bounded check")
    print(f"  n range: {summary['n_min']}..{summary['n_max']}")
    print("  direct coefficient convention: each Dyck sequence contributes q^area t^dinv")
    print(f"  checked theorem range: 0 <= d <= 2n-8")
    print(f"  generated Dyck sequences: {summary['total_sequences']}")
    print(f"  sequences by n: {summary['sequences_by_n']}")
    print(f"  special skeleton counts by n,d: {summary['special_skeleton_counts']}")
    print(f"  Dyck validation checks: {summary['dyck_validation_checks']}")
    print(f"  formula-vs-pair deficit checks: {summary['formula_pair_deficit_checks']}")
    print(f"  coefficient total checks: {summary['coefficient_total_checks']}")
    print(f"  checked (n,d) bands: {summary['checked_bands']}")
    print(f"  checked coefficients in bands: {summary['checked_coefficients']}")
    print(f"  flat-band checks: {summary['flat_band_checks']}")
    print(f"  skeleton-count match checks: {summary['skeleton_match_checks']}")
    print(f"  representative bands: {summary['representative_bands']}")
    print("  PASS")


if __name__ == "__main__":
    main()
```

### `items/qt_catalan_middle_coefficients/code/flat_middle_coefficients_default_summary.txt`

```text
Flat middle coefficient bounded check, default run summary

Command:

  python code/check_flat_middle_coefficients.py

Key output:

  n range: 4..8
  direct coefficient convention: each Dyck sequence contributes q^area t^dinv
  checked theorem range: 0 <= d <= 2n-8
  generated Dyck sequences: 2047
  sequences by n: {4: 14, 5: 42, 6: 132, 7: 429, 8: 1430}
  Dyck validation checks: 2047
  formula-vs-pair deficit checks: 2047
  coefficient total checks: 5
  checked (n,d) bands: 25
  checked coefficients in bands: 325
  flat-band checks: 25
  skeleton-count match checks: 325
  PASS

The full command output also prints special skeleton counts by n,d and a list
of representative flat bands.
```

### `items/qt_catalan_middle_coefficients/code/README.md`

```markdown
# Code

`check_flat_middle_coefficients.py` is a self-contained bounded checker for
the classical flat-middle coefficient statement.

Default command:

````bash
python code/check_flat_middle_coefficients.py
````

From this item directory, the default run checks `n=4..8`.  For each checked
`n`, it builds the direct coefficient dictionary for
`C_n(q,t)=sum_D q^area(D)t^dinv(D)`, counts special Dyck skeletons by deficit,
and verifies that every coefficient in the middle band

````text
q^j t^(M-d-j),   d <= j <= M-2d,   0 <= d <= 2n-8
````

equals the corresponding special-skeleton count.

Useful options:

````bash
python code/check_flat_middle_coefficients.py --n-min 4 --n-max 8
python code/check_flat_middle_coefficients.py --representative-bands 3
````

The file `flat_middle_coefficients_default_summary.txt` records the default
summary.  The check is finite evidence and a regression guard; it is not a
proof of the theorem or of the larger flat-middle conjecture.
```

### `items/qt_catalan_middle_coefficients/explanation.aux`

```text
\relax 
\@writefile{toc}{\contentsline {section}{\numberline {1}Classical flat middle coefficients}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {2}Broader conjecture}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {3}Computer check}{2}{}\protected@file@percent }
\gdef \@abspage@last{2}
```

### `items/qt_catalan_middle_coefficients/explanation.log`

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.29 (MiKTeX 26.5) (preloaded format=pdflatex 2026.5.25)  21 JUN 2026 18:18
entering extended mode
 restricted \write18 enabled.
 %&-line parsing enabled.
**./explanation.tex
(explanation.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\size10.clo
File: size10.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
)
\c@part=\count276
\c@section=\count277
\c@subsection=\count278
\c@subsubsection=\count279
\c@paragraph=\count280
\c@subparagraph=\count281
\c@figure=\count282
\c@table=\count283
\abovecaptionskip=\skip49
\belowcaptionskip=\skip50
\bibindent=\dimen150
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsmath.sty
Package: amsmath 2025/07/09 v2.17z AMS math features
\@mathmargin=\skip51

For additional information on amsmath, use the `?' option.
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amstext.sty
Package: amstext 2024/11/17 v2.01 AMS text

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsgen.sty
File: amsgen.sty 1999/11/30 v2.0 generic functions
\@emptytoks=\toks17
\ex@=\dimen151
))
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsbsy.sty
Package: amsbsy 1999/11/29 v1.2d Bold Symbols
\pmbraise@=\dimen152
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsopn.sty
Package: amsopn 2022/04/08 v2.04 operator names
)
\inf@bad=\count284
LaTeX Info: Redefining \frac on input line 233.
\uproot@=\count285
\leftroot@=\count286
LaTeX Info: Redefining \overline on input line 398.
LaTeX Info: Redefining \colon on input line 409.
\classnum@=\count287
\DOTSCASE@=\count288
LaTeX Info: Redefining \ldots on input line 495.
LaTeX Info: Redefining \dots on input line 498.
LaTeX Info: Redefining \cdots on input line 619.
\Mathstrutbox@=\box53
\strutbox@=\box54
LaTeX Info: Redefining \big on input line 721.
LaTeX Info: Redefining \Big on input line 722.
LaTeX Info: Redefining \bigg on input line 723.
LaTeX Info: Redefining \Bigg on input line 724.
\big@size=\dimen153
LaTeX Font Info:    Redeclaring font encoding OML on input line 742.
LaTeX Font Info:    Redeclaring font encoding OMS on input line 743.
\macc@depth=\count289
LaTeX Info: Redefining \bmod on input line 904.
LaTeX Info: Redefining \pmod on input line 909.
LaTeX Info: Redefining \smash on input line 939.
LaTeX Info: Redefining \relbar on input line 969.
LaTeX Info: Redefining \Relbar on input line 970.
\c@MaxMatrixCols=\count290
\dotsspace@=\muskip17
\c@parentequation=\count291
\dspbrk@lvl=\count292
\tag@help=\toks18
\row@=\count293
\column@=\count294
\maxfields@=\count295
\andhelp@=\toks19
\eqnshift@=\dimen154
\alignsep@=\dimen155
\tagshift@=\dimen156
\tagwidth@=\dimen157
\totwidth@=\dimen158
\lineht@=\dimen159
\@envbody=\toks20
\multlinegap=\skip52
\multlinetaggap=\skip53
\mathdisplay@stack=\toks21
LaTeX Info: Redefining \[ on input line 2950.
LaTeX Info: Redefining \] on input line 2951.
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amscls\amsthm.sty
Package: amsthm 2020/05/29 v2.20.6
\thm@style=\toks22
\thm@bodyfont=\toks23
\thm@headfont=\toks24
\thm@notefont=\toks25
\thm@headpunct=\toks26
\thm@preskip=\skip54
\thm@postskip=\skip55
\thm@headsep=\skip56
\dth@everypar=\toks27
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amssymb.sty
Package: amssymb 2013/01/14 v3.01 AMS font symbols

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amsfonts.sty
Package: amsfonts 2013/01/14 v3.01 Basic AMSFonts support
\symAMSa=\mathgroup4
\symAMSb=\mathgroup5
LaTeX Font Info:    Redeclaring math symbol \hbar on input line 98.
LaTeX Font Info:    Overwriting math alphabet `\mathfrak' in version `bold'
(Font)                  U/euf/m/n --> U/euf/b/n on input line 106.
))
\c@theorem=\count296
\c@conjecture=\count297

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/l3backend\l3backend-pdft
ex.def
File: l3backend-pdftex.def 2026-02-18 L3 backend support: PDF output (pdfTeX)
\l__color_backend_stack_int=\count298
) (explanation.aux)
\openout1 = `explanation.aux'.

LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 11.
LaTeX Font Info:    ... okay on input line 11.
LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 11.
LaTeX Font Info:    ... okay on input line 11.
LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 11.
LaTeX Font Info:    ... okay on input line 11.
LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 11.
LaTeX Font Info:    ... okay on input line 11.
LaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 11.
LaTeX Font Info:    ... okay on input line 11.
LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 11.
LaTeX Font Info:    ... okay on input line 11.
LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 11.
LaTeX Font Info:    ... okay on input line 11.
LaTeX Font Info:    Trying to load font information for U+msa on input line 12.


(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsa.fd
File: umsa.fd 2013/01/14 v3.01 AMS symbols A
)
LaTeX Font Info:    Trying to load font information for U+msb on input line 12.


(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsb.fd
File: umsb.fd 2013/01/14 v3.01 AMS symbols B
)
[1

{C:/Users/User/AppData/Local/MiKTeX/fonts/map/pdftex/pdftex.map}] [2]
(explanation.aux)
 ***********
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
 ***********
 ) 
Here is how much of TeX's memory you used:
 1821 strings out of 467683
 25921 string characters out of 5415205
 442244 words of memory out of 5000000
 30916 multiletter control sequences out of 15000+600000
 637038 words of font info for 77 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 56i,5n,65p,209b,228s stack positions out of 10000i,1000n,20000p,200000b,200000s
<C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/c
mbx10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfo
nts/cm/cmbx12.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/publ
ic/amsfonts/cm/cmex10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/
fonts/type1/public/amsfonts/cm/cmmi12.pfb><C:/Users/User/AppData/Local/Programs
/MiKTeX/fonts/type1/public/amsfonts/cm/cmmi7.pfb><C:/Users/User/AppData/Local/P
rograms/MiKTeX/fonts/type1/public/amsfonts/cm/cmr10.pfb><C:/Users/User/AppData/
Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr17.pfb><C:/Users/User/A
ppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr7.pfb><C:/Users/
User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmsy10.pfb><C
:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmsy7
.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/c
m/cmti10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/am
sfonts/cm/cmtt10.pfb>
Output written on explanation.pdf (2 pages, 159871 bytes).
PDF statistics:
 74 PDF objects out of 1000 (max. 8388607)
 0 named destinations out of 1000 (max. 500000)
 1 words of extra memory for PDF output out of 10000 (max. 10000000)

```

### `items/qt_catalan_middle_coefficients/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 159871
sha256: cf0afbe530a867a3653501009e640e266944fc487c3193732cc1901c292efc08
```

### `items/qt_catalan_middle_coefficients/explanation.synctex.gz`

```text
[binary artifact not expanded]
size_bytes: 10099
sha256: 676934838fdd699d36561f69a912782992643b9ebaaf44064d858ad408688766
```

### `items/qt_catalan_middle_coefficients/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{$q,t$-Catalan Middle Coefficients}
\author{}
\date{}

\newtheorem{theorem}{Theorem}
\newtheorem{conjecture}{Conjecture}

\begin{document}
\maketitle

\section{Classical flat middle coefficients}

Let
\[
  C_n(q,t)=\sum_D q^{\operatorname{area}(D)}t^{\operatorname{dinv}(D)}
\]
where the sum is over Dyck area sequences \(D\) of length \(n\).  Put
\[
  M=\binom{n}{2}, \qquad
  \operatorname{defc}(D)=M-\operatorname{area}(D)-\operatorname{dinv}(D).
\]

The Dyck-skeleton decomposition formula has the following flat-middle
consequence.

\begin{theorem}[Flat middle coefficients in the skeleton range]
For \(n\ge 4\), \(M=\binom{n}{2}\), and \(0\le d\le 2n-8\), the coefficient of
\[
  q^j t^{M-d-j}
\]
in \(C_n(q,t)\) is independent of \(j\) for all integers
\[
  d\le j\le M-2d.
\]
The common value is the number of special Dyck skeletons of length \(n\) and
deficit \(d\).
\end{theorem}

Here a special Dyck skeleton is a full Dyck skeleton other than the exceptional
full skeleton
\[
  (0,0,1,0,\ldots,0,1)
\]
when that exceptional sequence exists.  The input from the skeleton
decomposition is that every special skeleton \(S\) of deficit \(d\) satisfies
\(\operatorname{area}(S)\le d\), and the skeleton contribution therefore fills
the displayed middle band with the same coefficient.

\section{Broader conjecture}

The proved statement above is restricted to \(0\le d\le 2n-8\).  The broader
flat-middle prediction is the following.

\begin{conjecture}[Full flat-middle range]
Let \(M=\binom{n}{2}\).  For any \(n\ge 1\) and
\[
  0\le d\le \left\lfloor \frac{M}{3}\right\rfloor,
\]
the coefficient of \(q^j t^{M-d-j}\) in \(C_n(q,t)\) is independent of \(j\)
for all integers \(d\le j\le M-2d\).
\end{conjecture}

This conjecture is not a theorem in this item.  The curated code gives bounded
checks of the theorem range only.

\section{Computer check}

The script \texttt{code/check\_flat\_middle\_coefficients.py} is a
self-contained port of the bounded check from the Dyck repository.  It
generates all Dyck area sequences for \(4\le n\le 8\), computes direct
coefficients in the convention \(q^{\operatorname{area}}t^{\operatorname{dinv}}\),
counts special skeletons by deficit, and verifies the flat band equality for
all \(0\le d\le 2n-8\).

The default run checks 2047 Dyck sequences, 25 \((n,d)\)-bands, and 325
individual middle-band coefficients.  It also checks that the formula
\[
  \operatorname{defc}(D)
  =\binom{n}{2}-\operatorname{area}(D)-\operatorname{dinv}(D)
\]
agrees with the explicit deficit-pair count on every generated sequence.

These computations are regression evidence for the implementation and finite
evidence for the displayed statements; they do not replace the skeleton
decomposition proof and they do not prove the full flat-middle conjecture.

\end{document}
```

### `items/qt_catalan_middle_coefficients/html/body.html`

```html
<p>Let <span class="math">C_n(q,t)=\sum_D q^{area(D)}t^{dinv(D)}</span>, with the sum over Dyck area sequences of length <span class="math">n</span>, and put <span class="math">M=\binom n2</span>.</p>

<h2>Classical skeleton range</h2>

<p>The Dyck-skeleton decomposition proves the following flat-middle statement. For <span class="math">n\ge 4</span> and <span class="math">0\le d\le 2n-8</span>, the coefficient of</p>

<pre>q^j t^(M-d-j)</pre>

<p>in <span class="math">C_n(q,t)</span> is independent of <span class="math">j</span> for every <span class="math">d\le j\le M-2d</span>. The common value is the number of special Dyck skeletons of length <span class="math">n</span> and deficit <span class="math">d</span>.</p>

<p>The full flat-middle conjecture asks for the same independence throughout <span class="math">0\le d\le \lfloor M/3\rfloor</span>. That broader range is conjectural here.</p>

<h2>Computer check</h2>

<p>The script <code>code/check_flat_middle_coefficients.py</code> is a self-contained bounded checker ported from the Dyck repository. The default run checks <span class="math">n=4,\ldots,8</span>, generating 2047 Dyck sequences, 25 <span class="math">(n,d)</span> bands, and 325 middle-band coefficients.</p>

<pre><code>python code/check_flat_middle_coefficients.py</code></pre>

<p>The code is finite evidence and a regression guard. It does not prove the theorem or the full flat-middle conjecture.</p>
```

### `items/qt_catalan_middle_coefficients/item.yaml`

```yaml
title: qt-Catalan Middle Coefficients
slug: qt_catalan_middle_coefficients
status_summary: Classical flat middle coefficients are proved for 0 <= d <= 2n-8; the full flat-middle range is conjectural.
source_paths:
  - ../Dyck/paper/working_drafts/arxiv_submission.tex
  - ../Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex
  - ../Dyck/code/codex_project/red_team_flat_middle_coefficients.py
  - ../Dyck/code/code_assistant/codex_tasks/CA-0011_flat_middle_coefficients.md
  - ../Dyck/code/code_assistant/reviews/CA-0011_flat_middle_coefficients_review.md
downloads:
  - explanation.tex
  - code/check_flat_middle_coefficients.py
  - code/flat_middle_coefficients_default_summary.txt
```

### `items/qt_catalan_middle_coefficients/README.md`

```markdown
# qt-Catalan Middle Coefficients

Status summary: Classical flat middle coefficients are proved in the Dyck-skeleton range `0 <= d <= 2n-8`; the full flat-middle range is conjectural.

## Summary

Let `C_n(q,t)` be computed in the direct Dyck-area-sequence convention
`sum_D q^area(D)t^dinv(D)`, and let `M = binom(n,2)`.  The Dyck-skeleton
decomposition proves that, for `n >= 4` and `0 <= d <= 2n-8`, the coefficients
of

````text
q^j t^(M-d-j),   d <= j <= M-2d,
````

are independent of `j`.  Their common value is the number of special Dyck
skeletons of length `n` and deficit `d`.

The broader flat-middle conjecture asks for the same independence throughout
`0 <= d <= floor(M/3)`.  That broader range is not claimed here as proved.

## Provenance

Source repository: `Dyck`

Source paths:

- `../Dyck/paper/working_drafts/arxiv_submission.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex`
- `../Dyck/code/codex_project/red_team_flat_middle_coefficients.py`
- `../Dyck/code/code_assistant/codex_tasks/CA-0011_flat_middle_coefficients.md`
- `../Dyck/code/code_assistant/reviews/CA-0011_flat_middle_coefficients_review.md`

Transfer type: curated writeup with self-contained adapted code.

## Layers

Python layer: `code/check_flat_middle_coefficients.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- Classical range `0 <= d <= 2n-8`: theorem, via the special Dyck-skeleton
  decomposition.
- Full flat-middle range `0 <= d <= floor(M/3)`: conjecture.
- Curated code: bounded direct-coefficient red-team check for `n=4..8`.

## Code

From `Combinatorics/items/qt_catalan_middle_coefficients`:

````bash
python code/check_flat_middle_coefficients.py
````

The default run checks `n=4..8`, 25 `(n,d)` bands, and 325 middle-band
coefficients.  The output is summarized in
`code/flat_middle_coefficients_default_summary.txt`.
```

### `items/rational_qt_catalan_formula/assets/.gitkeep`

```text

```

### `items/rational_qt_catalan_formula/code/check_rational_qt_catalan_formula.py`

```python
"""Finite checks for the rational q,t-Catalan formula.

This is a curated port of
``Conjectures-and-Computations/qt-catalan/qt-conjecture.py``.  It keeps the
source script's step-coordinate convention and the same monomial comparison,
but exposes a reproducible command-line interface.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter
from dataclasses import dataclass
from math import gcd
from typing import Sequence


StepPath = tuple[int, ...]
Monomial = tuple[int, int]


@dataclass(frozen=True)
class PathRecord:
    degree: int
    path: StepPath


@dataclass(frozen=True)
class CheckResult:
    r: int
    n: int
    ell: int
    closest_index: int
    closest_height: int
    max_area: int
    path_count: int
    all_count: int
    plus_count: int
    minus_count: int
    ok: bool
    first_difference: Monomial | None


def beta(n: int, ell: int, i: int, j: int, path: Sequence[int]) -> float:
    return sum(path[i : j + 1]) - n * (j - i + 1) / (ell + 1)


def gamma(n: int, ell: int, i: int, j: int, path: Sequence[int]) -> int:
    value = beta(n, ell, i, j, path)
    if value < 0:
        return min(path[i - 1], math.floor(-value))
    if value > 0:
        return min(path[i], math.floor(value))
    return 0


def generate_paths(ell: int, n: int) -> list[PathRecord]:
    """Generate the source script's step-coordinate Dyck paths."""

    frontier = [PathRecord(0, ())]
    while len(frontier[0].path) < ell:
        next_frontier: list[PathRecord] = []
        for record in frontier:
            prefix = record.path
            room = math.floor((len(prefix) + 1) * n / (ell + 1) - sum(prefix))
            for value in range(int(room) + 1):
                child_path = prefix + (value,)
                degree = record.degree
                for k in range(1, len(child_path)):
                    degree += gamma(n, ell, k, len(child_path) - 1, child_path)
                next_frontier.append(PathRecord(degree, child_path))
        frontier = next_frontier
    return frontier


def max_area(ell: int, n: int) -> int:
    return sum(int(math.floor((i + 1) * n / (ell + 1))) for i in range(ell))


def closest_point(r: int, n: int) -> tuple[int, int]:
    """Return the source script's closest point [q, floor((q+1)n/r)]."""

    ell = r - 1
    closest: tuple[int, int] | None = None
    for q in range(ell):
        fractional_scaled = round((ell + 1) * ((q + 1) * n / (ell + 1) - math.floor((q + 1) * n / (ell + 1))))
        if fractional_scaled == 1:
            closest = (q, math.floor((q + 1) * n / (ell + 1)))
    if closest is None:
        raise ValueError(f"no closest point found for r={r}, n={n}; expected gcd(r,n)=1")
    return closest


def path_area(record: PathRecord, ell: int, n: int) -> int:
    area = max_area(ell, n)
    for p in range(len(record.path)):
        area -= sum(record.path[: p + 1])
    return area


def monomial_counts(r: int, n: int) -> tuple[Counter[Monomial], Counter[Monomial], Counter[Monomial], list[PathRecord], int, tuple[int, int]]:
    ell = r - 1
    paths = generate_paths(ell, n)
    total_area = max_area(ell, n)
    closest = closest_point(r, n)
    all_terms: Counter[Monomial] = Counter()
    plus_terms: Counter[Monomial] = Counter()
    minus_terms: Counter[Monomial] = Counter()

    for record in paths:
        area = path_area(record, ell, n)
        all_terms[(area, total_area - record.degree)] += 1
        if sum(record.path[: closest[0] + 1]) != closest[1]:
            continue
        if area <= total_area - area - record.degree:
            for q_degree in range(area, int(total_area - area - record.degree + 1)):
                plus_terms[(q_degree, total_area - record.degree)] += 1
        else:
            for q_degree in range(int(total_area - area - record.degree + 1), area):
                minus_terms[(q_degree, total_area - record.degree)] += 1

    return all_terms, plus_terms, minus_terms, paths, total_area, closest


def check_conjecture(r: int, n: int) -> CheckResult:
    if r <= 1 or n <= 0:
        raise ValueError("expected r>1 and n>0")
    if gcd(r, n) != 1:
        raise ValueError("the source conjecture check is intended for gcd(r,n)=1")

    all_terms, plus_terms, minus_terms, paths, total_area, closest = monomial_counts(r, n)
    right_side = all_terms + minus_terms
    ok = plus_terms == right_side
    first_difference = None
    if not ok:
        for key in sorted(set(plus_terms) | set(right_side), key=lambda item: item[1] + item[0] / 1000):
            if plus_terms[key] != right_side[key]:
                first_difference = key
                break
    return CheckResult(
        r=r,
        n=n,
        ell=r - 1,
        closest_index=closest[0],
        closest_height=closest[1],
        max_area=total_area,
        path_count=len(paths),
        all_count=sum(all_terms.values()),
        plus_count=sum(plus_terms.values()),
        minus_count=sum(minus_terms.values()),
        ok=ok,
        first_difference=first_difference,
    )


def parse_case(text: str) -> tuple[int, int]:
    if "/" in text:
        left, right = text.split("/", 1)
    elif "," in text:
        left, right = text.split(",", 1)
    else:
        raise argparse.ArgumentTypeError("expected a case in the form r/n")
    return int(left), int(right)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        type=parse_case,
        dest="cases",
        help="case r/n to check; may be supplied multiple times; default is 7/12",
    )
    parser.add_argument("--show-difference", action="store_true", help="print the first mismatched monomial if a case fails")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cases = args.cases or [(7, 12)]
    all_ok = True
    print("rational q,t-Catalan formula finite check")
    for r, n in cases:
        result = check_conjecture(r, n)
        all_ok = all_ok and result.ok
        print(f"  case: r={r} n={n}")
        print(f"    ell: {result.ell}")
        print(f"    closest_point: ({result.closest_index}, {result.closest_height})")
        print(f"    max_area: {result.max_area}")
        print(f"    generated_paths: {result.path_count}")
        print(f"    all_terms: {result.all_count}")
        print(f"    plus_terms: {result.plus_count}")
        print(f"    minus_terms: {result.minus_count}")
        print(f"    status: {'PASS' if result.ok else 'FAIL'}")
        if args.show_difference and result.first_difference is not None:
            print(f"    first_difference: {result.first_difference}")
    print(f"overall_status: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

### `items/rational_qt_catalan_formula/code/rational_qt_catalan_expected_output.txt`

```text
rational q,t-Catalan formula finite check
  case: r=7 n=12
    ell: 6
    closest_point: (2, 5)
    max_area: 33
    generated_paths: 2652
    all_terms: 2652
    plus_terms: 2666
    minus_terms: 14
    status: PASS
overall_status: PASS

Sample multi-case run:

rational q,t-Catalan formula finite check
  case: r=3 n=5
    ell: 2
    closest_point: (1, 3)
    max_area: 4
    generated_paths: 7
    all_terms: 7
    plus_terms: 7
    minus_terms: 0
    status: PASS
  case: r=5 n=8
    ell: 4
    closest_point: (1, 3)
    max_area: 14
    generated_paths: 99
    all_terms: 99
    plus_terms: 99
    minus_terms: 0
    status: PASS
  case: r=7 n=12
    ell: 6
    closest_point: (2, 5)
    max_area: 33
    generated_paths: 2652
    all_terms: 2652
    plus_terms: 2666
    minus_terms: 14
    status: PASS
overall_status: PASS
```

### `items/rational_qt_catalan_formula/code/README.md`

```markdown
# Code

`check_rational_qt_catalan_formula.py` is a curated port of
`Conjectures-and-Computations/qt-catalan/qt-conjecture.py`.

Run the source example from the `Combinatorics` directory:

````powershell
python items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py
````

Or from the repository root:

````powershell
python Combinatorics\items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py
````

Check several coprime cases:

````powershell
python Combinatorics\items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py --case 3/5 --case 5/8 --case 7/12
````

Expected default summary:

````text
case: r=7 n=12
closest_point: (2, 5)
generated_paths: 2652
all_terms: 2652
plus_terms: 2666
minus_terms: 14
status: PASS
overall_status: PASS
````

The checker is intended for `gcd(r,n)=1` and rejects non-coprime inputs.
```

### `items/rational_qt_catalan_formula/explanation.aux`

```text
\relax 
\@writefile{toc}{\contentsline {section}{\numberline {1}Purpose}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {2}Step Coordinates}{1}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {3}Conjectural Formula Check}{2}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {4}Reproducible Runs}{2}{}\protected@file@percent }
\@writefile{toc}{\contentsline {section}{\numberline {5}Status}{2}{}\protected@file@percent }
\gdef \@abspage@last{2}
```

### `items/rational_qt_catalan_formula/explanation.log`

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.29 (MiKTeX 26.5) (preloaded format=pdflatex 2026.5.25)  21 JUN 2026 18:16
entering extended mode
 restricted \write18 enabled.
 %&-line parsing enabled.
**./explanation.tex
(explanation.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/base\size10.clo
File: size10.clo 2025/01/22 v1.4n Standard LaTeX file (size option)
)
\c@part=\count276
\c@section=\count277
\c@subsection=\count278
\c@subsubsection=\count279
\c@paragraph=\count280
\c@subparagraph=\count281
\c@figure=\count282
\c@table=\count283
\abovecaptionskip=\skip49
\belowcaptionskip=\skip50
\bibindent=\dimen150
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsmath.sty
Package: amsmath 2025/07/09 v2.17z AMS math features
\@mathmargin=\skip51

For additional information on amsmath, use the `?' option.
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amstext.sty
Package: amstext 2024/11/17 v2.01 AMS text

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsgen.sty
File: amsgen.sty 1999/11/30 v2.0 generic functions
\@emptytoks=\toks17
\ex@=\dimen151
))
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsbsy.sty
Package: amsbsy 1999/11/29 v1.2d Bold Symbols
\pmbraise@=\dimen152
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsmath\amsopn.sty
Package: amsopn 2022/04/08 v2.04 operator names
)
\inf@bad=\count284
LaTeX Info: Redefining \frac on input line 233.
\uproot@=\count285
\leftroot@=\count286
LaTeX Info: Redefining \overline on input line 398.
LaTeX Info: Redefining \colon on input line 409.
\classnum@=\count287
\DOTSCASE@=\count288
LaTeX Info: Redefining \ldots on input line 495.
LaTeX Info: Redefining \dots on input line 498.
LaTeX Info: Redefining \cdots on input line 619.
\Mathstrutbox@=\box53
\strutbox@=\box54
LaTeX Info: Redefining \big on input line 721.
LaTeX Info: Redefining \Big on input line 722.
LaTeX Info: Redefining \bigg on input line 723.
LaTeX Info: Redefining \Bigg on input line 724.
\big@size=\dimen153
LaTeX Font Info:    Redeclaring font encoding OML on input line 742.
LaTeX Font Info:    Redeclaring font encoding OMS on input line 743.
\macc@depth=\count289
LaTeX Info: Redefining \bmod on input line 904.
LaTeX Info: Redefining \pmod on input line 909.
LaTeX Info: Redefining \smash on input line 939.
LaTeX Info: Redefining \relbar on input line 969.
LaTeX Info: Redefining \Relbar on input line 970.
\c@MaxMatrixCols=\count290
\dotsspace@=\muskip17
\c@parentequation=\count291
\dspbrk@lvl=\count292
\tag@help=\toks18
\row@=\count293
\column@=\count294
\maxfields@=\count295
\andhelp@=\toks19
\eqnshift@=\dimen154
\alignsep@=\dimen155
\tagshift@=\dimen156
\tagwidth@=\dimen157
\totwidth@=\dimen158
\lineht@=\dimen159
\@envbody=\toks20
\multlinegap=\skip52
\multlinetaggap=\skip53
\mathdisplay@stack=\toks21
LaTeX Info: Redefining \[ on input line 2950.
LaTeX Info: Redefining \] on input line 2951.
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amscls\amsthm.sty
Package: amsthm 2020/05/29 v2.20.6
\thm@style=\toks22
\thm@bodyfont=\toks23
\thm@headfont=\toks24
\thm@notefont=\toks25
\thm@headpunct=\toks26
\thm@preskip=\skip54
\thm@postskip=\skip55
\thm@headsep=\skip56
\dth@everypar=\toks27
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amssymb.sty
Package: amssymb 2013/01/14 v3.01 AMS font symbols

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\amsfonts.sty
Package: amsfonts 2013/01/14 v3.01 Basic AMSFonts support
\symAMSa=\mathgroup4
\symAMSb=\mathgroup5
LaTeX Font Info:    Redeclaring math symbol \hbar on input line 98.
LaTeX Font Info:    Overwriting math alphabet `\mathfrak' in version `bold'
(Font)                  U/euf/m/n --> U/euf/b/n on input line 106.
))
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/geometry\geometry.sty
Package: geometry 2026/03/07 v6.0 Page Geometry

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/graphics\keyval.sty
Package: keyval 2022/05/29 v1.15 key=value parser (DPC)
\KV@toks@=\toks28
)
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/generic/iftex\ifvtex.sty
Package: ifvtex 2019/10/25 v1.7 ifvtex legacy package. Use iftex instead.

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/generic/iftex\iftex.sty
Package: iftex 2024/12/12 v1.0g TeX engine tests
))
\Gm@cnth=\count296
\Gm@cntv=\count297
\c@Gm@tempcnt=\count298
\Gm@bindingoffset=\dimen160
\Gm@wd@mp=\dimen161
\Gm@odd@mp=\dimen162
\Gm@even@mp=\dimen163
\Gm@layoutwidth=\dimen164
\Gm@layoutheight=\dimen165
\Gm@layouthoffset=\dimen166
\Gm@layoutvoffset=\dimen167
\Gm@dimlist=\toks29

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/geometry\geometry.cfg))
(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/l3backend\l3backend-pdft
ex.def
File: l3backend-pdftex.def 2026-02-18 L3 backend support: PDF output (pdfTeX)
\l__color_backend_stack_int=\count299
)
No file explanation.aux.
\openout1 = `explanation.aux'.

LaTeX Font Info:    Checking defaults for OML/cmm/m/it on input line 12.
LaTeX Font Info:    ... okay on input line 12.
LaTeX Font Info:    Checking defaults for OMS/cmsy/m/n on input line 12.
LaTeX Font Info:    ... okay on input line 12.
LaTeX Font Info:    Checking defaults for OT1/cmr/m/n on input line 12.
LaTeX Font Info:    ... okay on input line 12.
LaTeX Font Info:    Checking defaults for T1/cmr/m/n on input line 12.
LaTeX Font Info:    ... okay on input line 12.
LaTeX Font Info:    Checking defaults for TS1/cmr/m/n on input line 12.
LaTeX Font Info:    ... okay on input line 12.
LaTeX Font Info:    Checking defaults for OMX/cmex/m/n on input line 12.
LaTeX Font Info:    ... okay on input line 12.
LaTeX Font Info:    Checking defaults for U/cmr/m/n on input line 12.
LaTeX Font Info:    ... okay on input line 12.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
*geometry* verbose mode - [ preamble ] result:
* driver: pdftex
* paper: <default>
* layout: <same size as paper>
* layoutoffset:(h,v)=(0.0pt,0.0pt)
* modes: 
* h-part:(L,W,R)=(72.26999pt, 469.75502pt, 72.26999pt)
* v-part:(T,H,B)=(72.26999pt, 650.43001pt, 72.26999pt)
* \paperwidth=614.295pt
* \paperheight=794.96999pt
* \textwidth=469.75502pt
* \textheight=650.43001pt
* \oddsidemargin=0.0pt
* \evensidemargin=0.0pt
* \topmargin=-37.0pt
* \headheight=12.0pt
* \headsep=25.0pt
* \topskip=10.0pt
* \footskip=30.0pt
* \marginparwidth=65.0pt
* \marginparsep=11.0pt
* \columnsep=10.0pt
* \skip\footins=9.0pt plus 4.0pt minus 2.0pt
* \hoffset=0.0pt
* \voffset=0.0pt
* \mag=1000
* \@twocolumnfalse
* \@twosidefalse
* \@mparswitchfalse
* \@reversemarginfalse
* (1in=72.27pt=25.4mm, 1cm=28.453pt)

LaTeX Font Info:    Trying to load font information for U+msa on input line 13.

(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsa.fd
File: umsa.fd 2013/01/14 v3.01 AMS symbols A
)
LaTeX Font Info:    Trying to load font information for U+msb on input line 13.


(C:\Users\User\AppData\Local\Programs\MiKTeX\tex/latex/amsfonts\umsb.fd
File: umsb.fd 2013/01/14 v3.01 AMS symbols B
)
[1

{C:/Users/User/AppData/Local/MiKTeX/fonts/map/pdftex/pdftex.map}] [2]
(explanation.aux)
 ***********
LaTeX2e <2025-11-01>
L3 programming layer <2026-04-28>
 ***********
 ) 
Here is how much of TeX's memory you used:
 2406 strings out of 467683
 35093 string characters out of 5415205
 450182 words of memory out of 5000000
 31486 multiletter control sequences out of 15000+600000
 637066 words of font info for 78 fonts, out of 8000000 for 9000
 1141 hyphenation exceptions out of 8191
 57i,7n,65p,242b,200s stack positions out of 10000i,1000n,20000p,200000b,200000s
<C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/c
mbx12.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfo
nts/cm/cmex10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/publ
ic/amsfonts/cm/cmmi10.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/ty
pe1/public/amsfonts/cm/cmmi12.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/
fonts/type1/public/amsfonts/cm/cmmi7.pfb><C:/Users/User/AppData/Local/Programs/
MiKTeX/fonts/type1/public/amsfonts/cm/cmr10.pfb><C:/Users/User/AppData/Local/Pr
ograms/MiKTeX/fonts/type1/public/amsfonts/cm/cmr17.pfb><C:/Users/User/AppData/L
ocal/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmr7.pfb><C:/Users/User/App
Data/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmsy10.pfb><C:/Users/
User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmsy7.pfb><C:
/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/cm/cmti10
.pfb><C:/Users/User/AppData/Local/Programs/MiKTeX/fonts/type1/public/amsfonts/c
m/cmtt10.pfb>
Output written on explanation.pdf (2 pages, 151506 bytes).
PDF statistics:
 69 PDF objects out of 1000 (max. 8388607)
 0 named destinations out of 1000 (max. 500000)
 1 words of extra memory for PDF output out of 10000 (max. 10000000)

```

### `items/rational_qt_catalan_formula/explanation.pdf`

```text
[binary artifact not expanded]
size_bytes: 151506
sha256: 4cffda0e4230f2d2ebd25636f3f9f16c2ba4dcd28b816f371d2ac9f69f0ad8ea
```

### `items/rational_qt_catalan_formula/explanation.synctex.gz`

```text
[binary artifact not expanded]
size_bytes: 13210
sha256: 6f1b3160ea7e6bbb36063763fc3f052ee8c4713cad6df9edd9e6bc459c545897
```

### `items/rational_qt_catalan_formula/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}
\usepackage[margin=1in]{geometry}

\newcommand{\Cat}{\mathcal C}
\newcommand{\dinv}{\operatorname{dinv}}

\title{Rational \(q,t\)-Catalan Formula}
\author{}
\date{}

\begin{document}
\maketitle

\section{Purpose}

This item records the conjectural formula and finite checker from Graham
Hawkes's paper \emph{A conjectured formula for the rational
\(q,t\)-Catalan polynomial} (Annals of Combinatorics 28, 749--795, 2024;
arXiv:2208.00577).

The source script is
\[
  \texttt{Conjectures-and-Computations/qt-catalan/qt-conjecture.py}.
\]
The curated script
\[
  \texttt{code/check\_rational\_qt\_catalan\_formula.py}
\]
ports the same finite check into a command-line tool with compact output.

\section{Step Coordinates}

The checker uses the source script's step-coordinate convention.  For a
coprime pair \((r,n)\), put
\[
  \ell=r-1.
\]
A generated path is a sequence
\[
  x=(x_0,\ldots,x_{\ell-1})
\]
constructed from left to right subject to the rational Dyck bound
\[
  \sum_{a=0}^{i} x_a
  \le
  \left\lfloor\frac{(i+1)n}{\ell+1}\right\rfloor
  \qquad(0\le i<\ell).
\]
The script computes a degree statistic incrementally.  For
\[
  \beta(i,j;x)=\sum_{a=i}^{j}x_a-\frac{n(j-i+1)}{\ell+1},
\]
define
\[
  \gamma(i,j;x)=
  \begin{cases}
    \min(x_{i-1},\lfloor-\beta(i,j;x)\rfloor), & \beta(i,j;x)<0,\\
    \min(x_i,\lfloor\beta(i,j;x)\rfloor), & \beta(i,j;x)>0,\\
    0, & \beta(i,j;x)=0.
  \end{cases}
\]
When a new final entry is appended, the degree is increased by the corresponding
\(\gamma(k,j;x)\) terms with the new endpoint \(j\).  This is the source
script's statistic used in the monomial comparison.

The maximum area parameter is
\[
  M=\sum_{i=0}^{\ell-1}
  \left\lfloor\frac{(i+1)n}{\ell+1}\right\rfloor .
\]
For a generated path \(x\), the script uses
\[
  \operatorname{area}(x)
  =
  M-\sum_{p=0}^{\ell-1}\sum_{a=0}^{p}x_a.
\]

\section{Conjectural Formula Check}

The formula is expressed as a monomial-string identity.  The source script
first finds the unique closest point to the diagonal used by the conjecture:
an index \(q\) such that
\[
  (q+1)n\equiv 1 \pmod{\ell+1},
\]
recorded as
\[
  \left(q,\left\lfloor\frac{(q+1)n}{\ell+1}\right\rfloor\right).
\]
The distinguished subfamily \(T\) consists of the generated paths satisfying
\[
  \sum_{a=0}^{q}x_a
  =
  \left\lfloor\frac{(q+1)n}{\ell+1}\right\rfloor .
\]

Every generated path contributes one left-side monomial record
\[
  (\operatorname{area}(x),\,M-d(x)),
\]
where \(d(x)\) is the generated degree statistic.  Each path in \(T\) contributes
a monomial string to the right side.  If \(a=\operatorname{area}(x)\) and
\(d=d(x)\), then the positive interval is
\[
  (j,M-d),\qquad a\le j\le M-a-d,
\]
when \(a\le M-a-d\).  If \(M-a-d<a\), the script records the negative correction
interval
\[
  (j,M-d),\qquad M-a-d+1\le j<a.
\]
The finite check is the exact multiset identity
\[
  \text{positive interval multiset}
  =
  \text{all path monomials}+\text{negative correction multiset}.
\]

\section{Reproducible Runs}

The source script's built-in example is \((r,n)=(7,12)\).  Running
\[
  \texttt{python code/check\_rational\_qt\_catalan\_formula.py}
\]
checks that case.  In the curated run it generated 2,652 paths, found closest
point \((2,5)\), and verified
\[
  2666\text{ positive terms}
  =
  2652\text{ all-path terms}
  +
  14\text{ negative correction terms}.
\]
The status was \(\texttt{PASS}\).

The script also accepts multiple cases, for example
\[
  \texttt{python code/check\_rational\_qt\_catalan\_formula.py
  --case 3/5 --case 5/8 --case 7/12}.
\]
All listed cases must be coprime.  The source README explicitly warns that the
conjecture is not expected to hold for non-coprime parameters in general, and
the curated checker rejects non-coprime inputs.

\section{Status}

This item is conjectural.  It packages the finite checks for selected
relatively prime parameter pairs; it is separate from the computer-assisted
proof item for Lemma 2 and Lemma 3 of Section 9.

\end{document}
```

### `items/rational_qt_catalan_formula/html/body.html`

```html
<p>
  This item packages the finite checker for the conjectural rational
  <code>q,t</code>-Catalan formula from Graham Hawkes's 2024 paper.
</p>

<p>
  The source script is
  <code>Conjectures-and-Computations/qt-catalan/qt-conjecture.py</code>. The
  curated script <code>code/check_rational_qt_catalan_formula.py</code>
  preserves the source step-coordinate generation and monomial-string
  comparison, while giving compact command-line output.
</p>

<p>
  For a coprime pair <code>(r,n)</code>, the checker generates the relevant
  rational Dyck paths, forms the distinguished subfamily determined by the
  closest point to the diagonal, and compares the positive monomial-string
  multiset with all generated path monomials plus the negative correction
  multiset.
</p>

<p>
  The source example <code>(r,n)=(7,12)</code> generated 2,652 paths and
  returned <code>PASS</code>. The curated checker rejects non-coprime inputs,
  since the source conjecture is not expected to hold for non-coprime pairs in
  general.
</p>
```

### `items/rational_qt_catalan_formula/item.yaml`

```yaml
title: Rational qt-Catalan Formula
slug: rational_qt_catalan_formula
status_summary: Conjectural formula from the 2024 rational q,t-Catalan paper, with reproducible finite checks for selected coprime pairs.
source_paths:
  - ../Conjectures-and-Computations/qt-catalan/qt-conjecture.py
  - ../Conjectures-and-Computations/testing/catest.py
downloads:
  - explanation.tex
  - code/check_rational_qt_catalan_formula.py
  - code/rational_qt_catalan_expected_output.txt
```

### `items/rational_qt_catalan_formula/README.md`

```markdown
# Rational qt-Catalan Formula

Status summary: Conjectural formula from the 2024 rational `q,t`-Catalan
paper, with reproducible finite checks for selected coprime parameter pairs.

## Summary

This item curates the rational `q,t`-Catalan conjecture from Graham Hawkes,
*A conjectured formula for the rational q,t-Catalan polynomial*, Annals of
Combinatorics 28, 749-795 (2024).  It packages the source checker for the
monomial-string identity associated to a relatively prime pair `(r,n)`.

## Provenance

Source repository: `Conjectures-and-Computations`

Primary source path:

- `../Conjectures-and-Computations/qt-catalan/qt-conjecture.py`

Related older context:

- `../Conjectures-and-Computations/testing/catest.py`

Transfer type: adapted reproducibility wrapper preserving the source
computation.

## Layers

Python layer: `code/check_rational_qt_catalan_formula.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- Rational `q,t`-Catalan formula: conjectural.
- Default source example `(r,n)=(7,12)`: packaged and passing.
- Additional sample cases `(3,5)` and `(5,8)`: packaged and passing.

## Review Notes

- `qt-conjecture.py` is the source of record for this item.
- The checker rejects non-coprime inputs; the source README notes that the
  conjecture is not expected to hold for non-coprime pairs in general.
- `qt-assisted.py` belongs to the separate computer-assisted proof item for
  Lemma 2 and Lemma 3 of Section 9.
```

### `items/README.md`

```markdown
# Items

Each subdirectory of `items/` should contain one curated mathematical item.

Use the structure documented in `../target_structure.md`.
```

### `items/shifted_littlewood_richardson/assets/.gitkeep`

```text

```

### `items/shifted_littlewood_richardson/code/check_shifted_lr.py`

```python
"""Bounded checks for shifted Littlewood-Richardson conjectures.

This is a curated port of the two source scripts
``skew-GP-expansion.py`` and ``skew-GQ-expansion.py``.  It compares two
homogeneous-degree monomial expansions:

1. the direct skew expansion for a shifted skew shape ``shape/skew``;
2. the expansion obtained from the conjectural shifted Littlewood-Richardson
   rule into non-skew GP or GR functions.

The source GQ script checks the rule for GR functions; the source README notes
that this implies the same expansion for GQ functions.  The default examples
are intentionally small so the checker is quick.  Larger degrees and shapes can
be supplied from the command line.
"""

from __future__ import annotations

import argparse
import copy
import math
from typing import Literal


Kind = Literal["gp", "gq"]
Tableau = list[list[list[int]]]


def parse_shape(text: str) -> list[int]:
    if text.strip() == "":
        return []
    values = [int(part.strip()) for part in text.split(",") if part.strip()]
    if any(value < 0 for value in values):
        raise argparse.ArgumentTypeError("shape parts must be nonnegative")
    if any(values[i] < values[i + 1] for i in range(len(values) - 1)):
        raise argparse.ArgumentTypeError("shape parts must be weakly decreasing")
    return values


def normalized_skew(skew: list[int], shape: list[int]) -> list[int]:
    mu = list(skew)
    lam = list(shape)
    while len(mu) < len(lam):
        mu.append(0)
    if len(mu) > len(lam):
        raise ValueError("skew must have no more parts than shape")
    if any(mu[i] > lam[i] for i in range(len(lam))):
        raise ValueError("skew must be contained in shape")
    return mu


def standard_tabs(kind: Kind, alph: int, skew: list[int], shape: list[int]) -> list[list]:
    """Generate source-standard tableaux and their peak/repeat data."""

    mu = normalized_skew(skew, shape)
    empty_tab: Tableau = [[] for _ in shape]
    tab_list: list[list] = [[empty_tab, []]]

    for n in range(alph):
        new_list: list[list] = []
        for tab, positions in tab_list:
            for row_index in range(len(tab)):
                if len(tab[row_index]) > 0:
                    can_append_to_box = (
                        row_index == len(tab) - 1
                        or len(tab[row_index + 1]) == 0
                        or (
                            mu[row_index] + len(tab[row_index])
                            > mu[row_index + 1] + len(tab[row_index + 1]) + 1
                        )
                    )
                    if can_append_to_box:
                        t_cop = copy.deepcopy(tab)
                        t_cop[row_index][-1] += [n]
                        new_position = [row_index, mu[row_index] + len(t_cop[row_index]) + row_index]
                        new_list.append([t_cop, positions + [new_position]])

                if len(tab[row_index]) < shape[row_index] - mu[row_index]:
                    can_add_box = (
                        row_index == 0
                        or mu[row_index] + len(tab[row_index]) + 1
                        < mu[row_index - 1] + len(tab[row_index - 1])
                    )
                    if can_add_box:
                        t_cop = copy.deepcopy(tab)
                        t_cop[row_index] += [[n]]
                        new_position = [row_index, mu[row_index] + len(t_cop[row_index]) + row_index]
                        new_list.append([t_cop, positions + [new_position]])
        tab_list = new_list

    out: list[list] = []
    for tab, positions in tab_list:
        if any(len(tab[row]) != shape[row] - mu[row] for row in range(len(shape))):
            continue

        peak_set: list[int] = []
        repeat_set: list[int] = []
        diags = 0
        for i in range(0, len(positions) - 2):
            j = i + 1
            k = i + 2
            if positions[j][1] > positions[i][1] and positions[k][0] > positions[j][0]:
                peak_set.append(j)
            if kind == "gp":
                if positions[i] == positions[j] and positions[k][0] > positions[j][0]:
                    peak_set.append(j)
                if positions[j][1] > positions[i][1] and positions[j] == positions[k]:
                    peak_set.append(j)
                if positions[i] == positions[j] and positions[j] == positions[k]:
                    peak_set.append(j)

        for i in range(0, len(positions) - 1):
            if positions[i] == positions[i + 1]:
                if kind == "gp":
                    repeat_set.append(-(i + 1) if positions[i][0] == positions[i][1] - 1 else i + 1)
                else:
                    repeat_set.append(i)

        if kind == "gp":
            for row, col in positions:
                if row == col - 1:
                    diags += 1
            out.append([tab, peak_set, repeat_set, diags])
        else:
            out.append([tab, peak_set, repeat_set])
    return out


def partitions(n: int, k: int) -> list[list[int]]:
    if n <= 0:
        return [[]]
    par_list = [[1]]
    while sum(par_list[0]) < n:
        new_list: list[list[int]] = []
        for par in par_list:
            if len(par) == 1 or (len(par) > 1 and par[-1] < par[-2]):
                p_cop = copy.copy(par)
                p_cop[-1] += 1
                new_list.append(p_cop)
            if len(par) < k:
                p_cop = copy.copy(par)
                p_cop.append(1)
                new_list.append(p_cop)
        par_list = new_list
    return par_list


def polynomial(kind: Kind, tab_data: list, num_vars: int) -> list[list[int]]:
    values: list[list[int]] = []
    tab = tab_data[0]
    peak_set = tab_data[1]
    repeat_set = tab_data[2]
    diags = tab_data[3] if kind == "gp" else 0
    degree = sum(len(box) for row in tab for box in row)

    for par in partitions(degree, num_vars):
        weak_seq: list[int] = []
        for index, part in enumerate(par):
            weak_seq += [index + 1] * part

        good = True
        power_of_two = len(par) - diags
        for i in range(0, len(weak_seq) - 2):
            if weak_seq[i] == weak_seq[i + 1] == weak_seq[i + 2] and i + 1 in peak_set:
                good = False
        for i in range(0, len(weak_seq) - 1):
            if weak_seq[i] == weak_seq[i + 1]:
                if kind == "gp":
                    if -(i + 1) in repeat_set:
                        good = False
                    if i + 1 in repeat_set:
                        power_of_two -= 1
                elif i in repeat_set:
                    good = False
        if good:
            multiplicity = int(math.pow(2, power_of_two)) if kind == "gp" else 1
            values += [par] * multiplicity
    return values


def distinct_elements(values: list[list[int]]) -> list[list]:
    if not values:
        return []
    values = sorted(values, key=lambda x: str(x))
    out = [[1, values[0]]]
    for value in values[1:]:
        if value == out[-1][1]:
            out[-1][0] += 1
        else:
            out.append([1, value])
    out.reverse()
    return out


def monomial_exp(kind: Kind, degree: int, skew: list[int], shape: list[int], num_vars: int) -> list[list]:
    values: list[list[int]] = []
    for tab_data in standard_tabs(kind, degree, list(skew), list(shape)):
        values += polynomial(kind, tab_data, num_vars)
    return distinct_elements(values)


def sequences(length: int, maxi: int) -> list[list[int]]:
    seq_list = [[]]
    while len(seq_list[0]) < length:
        seq_list = [seq + [value] for seq in seq_list for value in range(maxi + 1)]
    return seq_list


def row(m: int, n: int) -> list[list[list[int]]]:
    """Create one-row shifted set-valued tableaux of length m and max entry n.

    The source representation is 1' -> 1, 1 -> 2, 2' -> 3, 2 -> 4, and so on.
    """

    row_tabs: list[list[list[int]]] = [[]]
    while len(row_tabs[0]) < m:
        new_tabs: list[list[list[int]]] = []
        for row_tab in row_tabs:
            previous = row_tab[-1][-1] if row_tab else 1
            for bit_string in sequences(2 * n + 1 - previous, 1):
                subset = [index + previous for index, bit in enumerate(bit_string) if bit == 0]
                if subset and (previous % 2 == 0 or previous < subset[0] or not row_tab):
                    new_tabs.append(row_tab + [subset])
        row_tabs = new_tabs
    return row_tabs


def over(top_row: list[list[int]], bottom_row: list[list[int]], offset: int) -> bool:
    for i, top in enumerate(top_row):
        bot = [float("inf")]
        if 0 <= i + offset < len(bottom_row):
            bot = bottom_row[i + offset]
        if max(top) > min(bot):
            return False
        if max(top) == min(bot) and max(top) % 2 == 0:
            return False
    return True


def flag(skew: list[int], shape: list[int]) -> list[Tableau]:
    mu = normalized_skew(skew, shape)
    if not shape:
        return []

    flag_tabs: list[Tableau] = [[one_row] for one_row in row(shape[0] - mu[0], 1)]
    for row_number in range(2, len(shape) + 1):
        new_tabs: list[Tableau] = []
        row_tabs = row(shape[row_number - 1] - mu[row_number - 1], row_number)
        for partial in flag_tabs:
            for new_row in row_tabs:
                if over(partial[-1], new_row, mu[row_number - 2] - 1 - mu[row_number - 1]):
                    new_tabs.append(partial + [new_row])
        flag_tabs = new_tabs
    return flag_tabs


def read_w(tableau: Tableau) -> list[int]:
    word: list[int] = []
    for row_index in range(len(tableau) - 1, -1, -1):
        for box in tableau[row_index]:
            word += list(box)
    return word


def no_prime_diag(tableau: Tableau, diag_rows: list[int]) -> bool:
    for row_index in diag_rows:
        if row_index < len(tableau) and tableau[row_index]:
            if any(entry % 2 == 1 for entry in tableau[row_index][0]):
                return False
    return True


def first_unprimed(word: list[int]) -> bool:
    if not word:
        return True
    maxi = max(word)
    if maxi % 2 == 1:
        return False
    starts = [0] * int(maxi / 2)
    for entry in word:
        base = math.ceil(entry / 2)
        if starts[base - 1] == 0:
            starts[base - 1] = 1 if entry % 2 == 0 else -1
    return all(value != -1 for value in starts)


def primed_start(tableau: Tableau) -> Tableau:
    result = copy.deepcopy(tableau)
    word = read_w(result)
    if not word or max(word) % 2 == 1:
        return result
    for n in range(1, int(max(word) / 2) + 1):
        changed = False
        for row_index in range(len(result) - 1, -1, -1):
            for box in result[row_index]:
                for entry_index, entry in enumerate(box):
                    if not changed and entry == 2 * n:
                        changed = True
                        box[entry_index] -= 1
    return result


def back(tableau: Tableau) -> list[int]:
    backword: list[int] = []
    for row in tableau:
        for box_index in range(len(row) - 1, -1, -1):
            box = copy.copy(row[box_index])
            box.sort(key=lambda x: -(x % 2) + 1 / x)
            backword += box
    return backword


def forw(tableau: Tableau) -> list[int]:
    forword: list[int] = []
    for row_index in range(len(tableau) - 1, -1, -1):
        for box in tableau[row_index]:
            copied = copy.copy(box)
            copied.sort(key=lambda x: (x % 2) + 1 / x)
            forword += copied
    return forword


def lattice(tableau: Tableau) -> bool:
    word_max = max(read_w(tableau), default=0)
    counts = [0] * (math.ceil(word_max / 2) + 3)

    for entry in back(tableau):
        base = math.ceil(entry / 2)
        if entry % 2 == 0:
            counts[base] += 1
            if base > 1 and counts[base] > counts[base - 1]:
                return False
        elif base > 1 and counts[base] == counts[base - 1]:
            return False

    for entry in forw(tableau):
        base = math.ceil(entry / 2)
        if entry % 2 == 1:
            counts[base] += 1
            if base > 1 and counts[base] > counts[base - 1]:
                return False
        elif counts[base + 1] == counts[base]:
            return False
    return True


def weights(word: list[int]) -> list[int]:
    max_base = max((math.ceil(entry / 2) for entry in word), default=0)
    counts = [0] * max(9, max_base)
    for entry in word:
        counts[math.ceil(entry / 2) - 1] += 1
    return counts


def rule_expand(kind: Kind, skew: list[int], shape: list[int]) -> list[list]:
    mu = normalized_skew(skew, shape)
    tableaux = flag(mu, shape)
    weights_seen: list[list[int]] = []

    if kind == "gp":
        diag_rows = [row_index for row_index in range(len(shape)) if mu[row_index] == 0]
        for tableau in tableaux:
            if no_prime_diag(tableau, diag_rows) and lattice(tableau):
                weights_seen.append(weights(read_w(tableau)))
    else:
        for tableau in tableaux:
            if first_unprimed(read_w(tableau)) and lattice(primed_start(tableau)):
                weights_seen.append(weights(read_w(tableau)))

    expanded = distinct_elements(weights_seen)
    expanded.sort(key=lambda x: str(x[1]))
    expanded.reverse()
    return expanded


def list_expand(kind: Kind, expansion: list[list], degree: int, num_vars: int) -> list[list]:
    values: list[list[int]] = []
    for multiplicity, shape in expansion:
        if sum(shape) <= degree:
            for monomial_multiplicity, partition in monomial_exp(kind, degree, [], shape, num_vars):
                values += [partition] * (monomial_multiplicity * multiplicity)
    return distinct_elements(values)


def compare(kind: Kind, degree: int, skew: list[int], shape: list[int], num_vars: int) -> dict[str, object]:
    direct = monomial_exp(kind, degree, list(skew), list(shape), num_vars)
    rule = rule_expand(kind, list(skew), list(shape))
    reconstructed = list_expand(kind, rule, degree, num_vars)
    return {
        "kind": kind,
        "degree": degree,
        "skew": list(skew),
        "shape": list(shape),
        "num_vars": num_vars,
        "direct": direct,
        "rule": rule,
        "reconstructed": reconstructed,
        "pass": direct == reconstructed,
    }


def run_case(kind: Kind, degree: int, skew: list[int], shape: list[int], num_vars: int) -> bool:
    result = compare(kind, degree, skew, shape, num_vars)
    label = "GP" if kind == "gp" else "GQ/GR"
    print(f"{label} shifted LR bounded check")
    print(f"  degree: {degree}")
    print(f"  shape/skew: {shape}/{skew}")
    print(f"  variables: {num_vars}")
    print(f"  direct monomial terms: {len(result['direct'])}")
    print(f"  conjectural rule terms: {len(result['rule'])}")
    print(f"  reconstructed monomial terms: {len(result['reconstructed'])}")
    print(f"  rule expansion: {result['rule']}")
    print(f"  PASS: {result['pass']}")
    return bool(result["pass"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["gp", "gq", "both"], default="both")
    parser.add_argument("--degree", type=int, default=5)
    parser.add_argument("--skew", type=parse_shape, default=parse_shape("1"))
    parser.add_argument("--shape", type=parse_shape, default=parse_shape("3,1"))
    parser.add_argument("--num-vars", type=int, default=3)
    args = parser.parse_args()

    if args.degree < 0:
        raise SystemExit("degree must be nonnegative")
    if args.num_vars <= 0:
        raise SystemExit("num-vars must be positive")
    normalized_skew(args.skew, args.shape)

    kinds: list[Kind] = ["gp", "gq"] if args.kind == "both" else [args.kind]  # type: ignore[list-item]
    passes = [run_case(kind, args.degree, args.skew, args.shape, args.num_vars) for kind in kinds]
    if not all(passes):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
```

### `items/shifted_littlewood_richardson/code/README.md`

```markdown
# Code

`check_shifted_lr.py` is a curated combined checker for the source `GP` and
`GQ` shifted Littlewood-Richardson scripts.

Default command:

````bash
python code/check_shifted_lr.py
````

The default run checks both branches for:

````text
degree = 5
shape/skew = [3, 1]/[1]
num_vars = 3
````

The checker compares the direct homogeneous monomial expansion of the skew
function with the expansion reconstructed from the conjectural
Littlewood-Richardson rule.  For the `GQ` branch, the code follows the source
script by checking the related `GR` rule; the source README says this implies
the corresponding `GQ` expansion.

Useful options:

````bash
python code/check_shifted_lr.py --kind gp --degree 6 --shape 3,1 --skew 1 --num-vars 3
python code/check_shifted_lr.py --kind gq --degree 6 --shape 3,1 --skew 1 --num-vars 3
python code/check_shifted_lr.py --kind both --degree 5 --shape 4,2 --skew 2 --num-vars 3
````

The file `shifted_lr_default_summary.txt` records the default summary.  These
are bounded checks only; they do not prove either conjectural rule.
```

### `items/shifted_littlewood_richardson/code/shifted_lr_default_summary.txt`

```text
Shifted Littlewood-Richardson bounded check, default run summary

Command:

  python code/check_shifted_lr.py

Default parameters:

  degree: 5
  shape/skew: [3, 1]/[1]
  variables: 3

Key output:

  GP shifted LR bounded check
    direct monomial terms: 3
    conjectural rule terms: 3
    reconstructed monomial terms: 3
    PASS: True

  GQ/GR shifted LR bounded check
    direct monomial terms: 3
    conjectural rule terms: 3
    reconstructed monomial terms: 3
    PASS: True

Additional sanity check run during curation:

  python code/check_shifted_lr.py --degree 6 --shape 3,1 --skew 1 --num-vars 3

Both GP and GQ/GR checks passed for that degree-6 case as well.
```

### `items/shifted_littlewood_richardson/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{Shifted Littlewood--Richardson}
\author{}
\date{}

\newtheorem{conjecture}{Conjecture}
\newtheorem{remark}{Remark}

\begin{document}
\maketitle

\section{Reading words}

This item records the shifted Littlewood--Richardson conjectures from the
source note on skewing \(GP\) and \(GQ\) functions.  The objects are shifted
set-valued tableaux, in either the \(P\)-version or the \(Q\)-version.

The \emph{backword} of such a tableau is read by rows from top to bottom; within
each row, from right to left; and within each box, primed entries first in
decreasing order, followed by unprimed entries in decreasing order.  The
\emph{forword} is read by rows from bottom to top; within each row, from left
to right; and within each box, unprimed entries first in decreasing order,
followed by primed entries in decreasing order.

\section{Lattice and primed-starting conditions}

The lattice property is defined by testing each adjacent pair \(i,i+1\).  In
the backword, count unprimed \(i\)'s and unprimed \((i+1)\)'s; the latter count
must never exceed the former, and an \((i+1)'\) may not occur when the two
counts are equal.  In the forword, count primed \(i'\)'s and primed
\((i+1)'\)'s; again the latter count must never exceed the former, and an
unprimed \(i\) may not occur when the two counts are equal.

The primed-starting property is used for the \(Q\)-rule.  Read boxes by rows
from bottom to top and left to right within each row.  For each \(i\), the first
box containing \(i\) or \(i'\) must contain \(i'\) but not \(i\).

\section{Conjectural rules}

Let \(\mathcal{P}_{\lambda/\mu}\) be the set of shifted set-valued
\(P\)-tableaux of shape \(\lambda/\mu\) satisfying the lattice property.  Let
\(\mathcal{Q}_{\lambda/\mu}\) be the set of shifted set-valued \(Q\)-tableaux of
shape \(\lambda/\mu\) satisfying both the lattice and primed-starting
properties.

\begin{conjecture}[Skew \(GP\) expansion]
\[
  GP_{\lambda/\mu}
  =
  \sum_{P\in\mathcal{P}_{\lambda/\mu}} GP_{\operatorname{wt}(P)}.
\]
\end{conjecture}

\begin{conjecture}[Skew \(GQ\) expansion]
\[
  GQ_{\lambda/\mu}
  =
  \sum_{Q\in\mathcal{Q}_{\lambda/\mu}} GQ_{\operatorname{wt}(Q)}.
\]
\end{conjecture}

\begin{remark}
The source \(GQ\) script checks an equivalent-looking rule in a related \(GR\)
model.  In the source README, \(GR\) is described as the submodel in which, for
each \(i\), the first \(i\) or \(i'\) in the left-to-right, bottom-to-top
reading word is constrained.  The source notes that the \(GR\) check implies
the corresponding \(GQ\) expansion.
\end{remark}

\section{Computer check}

The script \texttt{code/check\_shifted\_lr.py} is a combined curated port of
the source \(GP\) and \(GQ\) scripts.  It compares the direct homogeneous
monomial expansion of a skew shifted Grothendieck function with the homogeneous
monomial expansion reconstructed from the conjectural rule.

The default run checks both the \(GP\) and \(GQ/GR\) branches for degree \(5\),
shape/skew \([3,1]/[1]\), and \(3\) variables.  During curation the same shape
was also checked in degree \(6\).  These computations are finite evidence and
regression checks; they are not proofs of the conjectures.

\end{document}
```

### `items/shifted_littlewood_richardson/html/body.html`

```html
<p>This item records conjectural shifted Littlewood-Richardson rules for skew shifted stable Grothendieck functions <span class="math">GP_{\lambda/\mu}</span> and <span class="math">GQ_{\lambda/\mu}</span>.</p>

<h2>Rules</h2>

<p>For the <span class="math">GP</span> rule, sum over shifted set-valued <span class="math">P</span>-tableaux of shape <span class="math">\lambda/\mu</span> satisfying the lattice property:</p>

<pre>GP_{lambda/mu} = sum_P GP_{wt(P)}</pre>

<p>For the <span class="math">GQ</span> rule, sum over shifted set-valued <span class="math">Q</span>-tableaux satisfying both the lattice property and the primed-starting property:</p>

<pre>GQ_{lambda/mu} = sum_Q GQ_{wt(Q)}</pre>

<p>The source <span class="math">GQ</span> script checks the related <span class="math">GR</span> formulation, which the source README says implies the same <span class="math">GQ</span> expansion.</p>

<h2>Computer check</h2>

<p>The script <code>code/check_shifted_lr.py</code> compares direct homogeneous monomial expansions with the expansions reconstructed from the conjectural rule.</p>

<pre><code>python code/check_shifted_lr.py</code></pre>

<p>The default run checks both <span class="math">GP</span> and <span class="math">GQ/GR</span> for degree 5, shape/skew <code>[3,1]/[1]</code>, and 3 variables. These are bounded checks, not proofs.</p>
```

### `items/shifted_littlewood_richardson/item.yaml`

```yaml
title: Shifted Littlewood-Richardson
slug: shifted_littlewood_richardson
status_summary: Conjectural shifted Littlewood-Richardson rules for skew GP and GQ functions, with bounded computational checks.
source_paths:
  - ../Conjectures-and-Computations/shifted-LR/skew-GQ-expansion.py
  - ../Conjectures-and-Computations/shifted-LR/skew-GP-expansion.py
  - ../Conjectures-and-Computations/shifted-LR/skew GP_GQ.tex
downloads:
  - explanation.tex
  - code/check_shifted_lr.py
  - code/shifted_lr_default_summary.txt
```

### `items/shifted_littlewood_richardson/README.md`

```markdown
# Shifted Littlewood-Richardson

Status summary: Conjectural shifted Littlewood-Richardson rules for skew `GP` and `GQ` functions, with bounded computational checks.

## Summary

This item curates conjectural positive expansion rules for skew shifted stable
Grothendieck functions:

````text
GP_{lambda/mu} = sum_P GP_{wt(P)}
GQ_{lambda/mu} = sum_Q GQ_{wt(Q)}
````

Here `P` runs over shifted set-valued `P`-tableaux of shape `lambda/mu` with
the lattice property.  The `Q` rule uses shifted set-valued `Q`-tableaux with
both the lattice property and the primed-starting property.

The source `GQ` code performs the comparison in the related `GR` model.  The
source README states that the checked `GR` rule implies the same expansion for
`GQ`.

## Provenance

Source repository: `Conjectures-and-Computations`

Source paths:

- `../Conjectures-and-Computations/shifted-LR/skew-GQ-expansion.py`
- `../Conjectures-and-Computations/shifted-LR/skew-GP-expansion.py`
- `../Conjectures-and-Computations/shifted-LR/skew GP_GQ.tex`

Transfer type: curated writeup with adapted combined checker.

## Layers

Python layer: `code/check_shifted_lr.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- `GP` rule: conjectural.
- `GQ` rule: conjectural; checked through the source `GR` formulation.
- Curated code: bounded direct-vs-rule monomial expansion checks.

## Code

From `Combinatorics/items/shifted_littlewood_richardson`:

````bash
python code/check_shifted_lr.py
````

The default run checks both variants for degree `5`, shape/skew `[3,1]/[1]`,
and `3` variables.  Larger cases can be supplied with:

````bash
python code/check_shifted_lr.py --kind gp --degree 6 --shape 3,1 --skew 1 --num-vars 3
python code/check_shifted_lr.py --kind gq --degree 6 --shape 3,1 --skew 1 --num-vars 3
````

The file `code/shifted_lr_default_summary.txt` records the default summary.
These checks are finite evidence, not proofs.
```

### `items/type_c_grothendieck/assets/.gitkeep`

```text

```

### `items/type_c_grothendieck/code/check_type_c_grothendieck.py`

```python
"""Bounded checks for the type C Grothendieck conjecture hierarchy.

This is a curated port of the three source scripts:

* ``c-grothendieck.py``: basic counting version;
* ``c-grothendieck-strong.py``: no repeated adjacent Hecke letters and no
  consecutive entries in the same shifted set-valued tableau box;
* ``c-grothendieck-strongest.py``: peakset-preserving version.

The checks are finite evidence only.  They do not construct the conjectural
bijections and they do not prove the resulting GQ-positivity statement.
"""

from __future__ import annotations

import argparse
import copy
import time
from typing import Literal


Mode = Literal["basic", "strong", "strongest"]


def hecke(index: int, permutation: list[int]) -> list[int]:
    result = copy.copy(permutation)
    if index == 0 and result[0] > 0:
        result[0] = -result[0]
    if index > 0 and result[index - 1] < result[index]:
        result[index - 1], result[index] = result[index], result[index - 1]
    return result


def identity(largest: int) -> list[int]:
    return list(range(1, largest + 2))


def permute(word: list[int], largest: int) -> list[int]:
    result = identity(largest)
    for index in word:
        result = hecke(index, result)
    return result


def words(length: int, largest: int, *, no_equal_adjacent: bool) -> list[list[int]]:
    word_list = [[]]
    while len(word_list[0]) < length:
        next_words: list[list[int]] = []
        for word in word_list:
            for value in range(largest + 1):
                if not no_equal_adjacent or not word or word[-1] != value:
                    next_words.append(word + [value])
        word_list = next_words
    return word_list


def all_words(max_length: int, largest: int, *, no_equal_adjacent: bool) -> list[list[list[int]]]:
    return [words(length, largest, no_equal_adjacent=no_equal_adjacent) for length in range(1, max_length + 1)]


def create_word_perm_pairs(max_length: int, largest: int, *, no_equal_adjacent: bool) -> list[list]:
    pairs: list[list] = []
    for word_group in all_words(max_length, largest, no_equal_adjacent=no_equal_adjacent):
        for word in word_group:
            pairs.append([word, permute(word, largest)])
    pairs.sort(key=lambda item: str(item[1]))
    return pairs


def colreq(bottom: list[int], top: list[int]) -> bool:
    """Source row-adjacency condition for type C unimodal Hecke tableaux."""

    if len(bottom) == 0:
        return True
    if len(top) <= len(bottom):
        return False

    b_row = copy.copy(bottom)
    a_row = copy.copy(top)
    bindex = max(index for index, value in enumerate(b_row) if value == min(b_row))
    for index in range(0, bindex + 1):
        b_row[index] = -b_row[index]
    aindex = max(index for index, value in enumerate(a_row) if value == min(a_row))
    for index in range(0, aindex):
        a_row[index] = -a_row[index]

    if abs(b_row[-1]) >= abs(a_row[0]):
        return False
    if abs(b_row[0]) >= abs(a_row[0]):
        return False

    for index in range(len(b_row)):
        if a_row[index + 1] > b_row[index]:
            for j in range(index + 1, len(b_row)):
                if b_row[index] < b_row[j] < a_row[index + 1]:
                    return False
                if b_row[index] < -b_row[j] < a_row[index + 1]:
                    return False
                if b_row[j] == a_row[index + 1] or b_row[j] == -a_row[index + 1]:
                    return False
            for k in range(0, index + 1):
                if b_row[index] < a_row[k] < a_row[index + 1]:
                    return False
                if b_row[index] < -a_row[k] < a_row[index + 1]:
                    return False
                if a_row[k] == -a_row[index + 1] or a_row[k] == a_row[index + 1]:
                    return False
    return True


def hook(row: list[int]) -> bool:
    if not row:
        return False
    min_index = max(index for index, value in enumerate(row) if value == min(row))
    for index in range(0, min_index):
        if row[index] <= row[index + 1]:
            return False
    for index in range(min_index, len(row) - 1):
        if row[index] >= row[index + 1]:
            return False
    return True


def hecke_tabs_for_shape(words_for_size: list[list[int]], shape: list[int]) -> list[list[int]]:
    valid: list[list[int]] = []
    offsets = [sum(shape[:index]) for index in range(len(shape) + 1)]
    for word in words_for_size:
        good = True
        for row_index in range(len(shape)):
            bottom = word[offsets[row_index] : offsets[row_index + 1]]
            if not hook(bottom):
                good = False
                break
            if row_index < len(shape) - 1:
                top = word[offsets[row_index + 1] : offsets[row_index + 2]]
                if not hook(top) or not colreq(bottom, top):
                    good = False
                    break
        if good:
            valid.append(word)
    return valid


def children_basic(partition: list[int]) -> list[list[int]]:
    children: list[list[int]] = []
    for index in range(len(partition)):
        if index == 0 or partition[index] < partition[index - 1] - 1:
            child = copy.copy(partition)
            child[index] += 1
            children.append(child)
    if partition[-1] > 1:
        children.append(copy.copy(partition) + [1])
    for index in range(len(partition)):
        if index == len(partition) - 1 or partition[index] > partition[index + 1] + 1:
            children.append(copy.copy(partition))
    return children


def positive_parts(partition: list[int]) -> list[int]:
    return [abs(value) for value in partition]


def children_strong(partition: list[int]) -> list[list[int]]:
    children: list[list[int]] = []
    positive = positive_parts(partition)
    for index in range(len(partition)):
        if index == 0 or positive[index] < positive[index - 1] - 1:
            child = copy.copy(positive)
            child[index] = -child[index] - 1
            children.append(child)
    if positive[-1] > 1:
        children.append(copy.copy(positive) + [-1])
    for index in range(len(partition)):
        if (index == len(partition) - 1 or positive[index] > positive[index + 1] + 1) and partition[index] > 0:
            child = copy.copy(positive)
            child[index] = -child[index]
            children.append(child)
    return children


def create_shapes(length: int, *, strong: bool) -> list[list[list[int]]]:
    if strong:
        sizes = [[], [[-1]]]
        child_func = children_strong
    else:
        sizes = [[], [[1]]]
        child_func = children_basic
    for _ in range(2, length + 1):
        next_sizes: list[list[int]] = []
        for partition in sizes[-1]:
            next_sizes += child_func(partition)
        sizes.append(next_sizes)
    if strong:
        for group in sizes:
            for partition in group:
                for index in range(len(partition)):
                    partition[index] = abs(partition[index])
    return sizes


def distinct_with_multiplicity(values: list[list[int]]) -> list[list]:
    if not values:
        return []
    out = [[1, values[0]]]
    for value in values[1:]:
        spot = -1
        for index, item in enumerate(out):
            if item[1] == value:
                spot = index
                break
        if spot >= 0:
            out[spot][0] += 1
        else:
            out.append([1, value])
        out.sort(key=lambda item: item[0])
    return out


def count_for_perm(length_words: list[list[list[int]]], shape_counts: list[list]) -> list:
    total = 0
    representative: list[int] = []
    if length_words[-1]:
        representative = length_words[-1][0]
    else:
        for group in reversed(length_words):
            if group:
                representative = group[0]
                break
    for multiplicity, shape in shape_counts:
        size = sum(shape)
        reversed_shape = copy.copy(shape)
        reversed_shape.reverse()
        valid_tabs = hecke_tabs_for_shape(length_words[size], reversed_shape)
        total += len(valid_tabs) * multiplicity
    return [representative, total, len(length_words[-1])]


def run_basic_or_strong(mode: Literal["basic", "strong"], length: int, largest: int) -> dict[str, object]:
    strong = mode == "strong"
    shape_counts = distinct_with_multiplicity(copy.deepcopy(create_shapes(length, strong=strong)[length]))
    pairs = create_word_perm_pairs(length, largest, no_equal_adjacent=strong)
    grouped_results: list[list] = []

    index = 0
    while index < len(pairs):
        current_perm = pairs[index][1]
        length_words = [[] for _ in range(length + 1)]
        while index < len(pairs) and pairs[index][1] == current_perm:
            word = pairs[index][0]
            length_words[len(word)].append(word)
            index += 1
        grouped_results.append(count_for_perm(length_words, shape_counts))

    same = sum(1 for result in grouped_results if result[1] == result[2])
    different = len(grouped_results) - same
    return {
        "mode": mode,
        "length": length,
        "largest": largest,
        "permutations": len(grouped_results),
        "same": same,
        "different": different,
        "shape_count_terms": len(shape_counts),
        "sample_results": grouped_results[: min(8, len(grouped_results))],
    }


def word_list(max_length: int, largest: int) -> list[list[list]]:
    base = identity(largest)
    all_by_length = [[[base, []]]]
    while len(all_by_length[-1][0][1]) < max_length:
        next_group: list[list] = []
        for perm, word in all_by_length[-1]:
            for value in range(largest + 1):
                if not word or word[-1] != value:
                    next_group.append([hecke(value, perm), word + [value]])
        all_by_length.append(next_group)
    return all_by_length


def create_perm_dict(max_length: int, largest: int) -> dict[str, dict[str, list]]:
    pairs: list[list] = []
    for group in word_list(max_length, largest)[1:]:
        pairs += group
    pairs.sort(key=lambda item: str(item[0]))
    result: dict[str, dict[str, list]] = {}
    for perm, word in pairs:
        result.setdefault(str(perm), {"words": []})["words"].append(word)
    return result


def add_word_peaks(perm_data: dict[str, dict[str, list]]) -> dict[str, dict[str, list]]:
    for perm in perm_data:
        peaksets: list[list[int]] = []
        for word in perm_data[perm]["words"]:
            peaks = [len(word)]
            for index in range(1, len(word) - 1):
                if word[index - 1] < word[index] and word[index] > word[index + 1]:
                    peaks.append(index)
            peaksets.append(peaks)
        peaksets.sort(key=lambda item: str(item))
        perm_data[perm]["peaksets"] = peaksets
    return perm_data


def hecke_tab(word: list[int]) -> list[list[int]]:
    tableau: list[list[int]] = []
    remainder = copy.copy(word)
    while not hook(remainder):
        index = 1
        while index <= len(remainder) and not hook(remainder[index:]):
            index += 1
        if index > len(remainder) or max(remainder[:index]) >= max(remainder[index:]):
            return []
        tableau.append(remainder[index:])
        remainder = remainder[:index]
        if len(tableau) > 1 and not colreq(tableau[-1], tableau[-2]):
            return []
    tableau.append(remainder)
    if len(tableau) > 1 and not colreq(tableau[-1], tableau[-2]):
        return []
    return tableau


def add_hecke_tabs(perm_data: dict[str, dict[str, list]]) -> dict[str, dict[str, list]]:
    for perm in perm_data:
        tabs: list[list[list[int]]] = []
        for word in perm_data[perm]["words"]:
            tab = hecke_tab(word)
            if tab:
                tabs.append(tab)
        perm_data[perm]["tabs"] = tabs
    return perm_data


def standard_shifted_svts(max_length: int) -> list[list[list]]:
    tabs: list[list[list]] = [[ [[], [], [], []] ]]
    for entry in range(max_length):
        big_tabs: list[list] = []
        for tab, positions, peakset, shape in tabs[-1]:
            for row_index in range(len(tab)):
                if entry - 1 not in tab[row_index][-1] and (
                    row_index == len(tab) - 1 or len(tab[row_index]) > 1 + len(tab[row_index + 1])
                ):
                    t_cop = copy.deepcopy(tab)
                    p_cop = copy.copy(positions)
                    k_cop = copy.copy(peakset)
                    t_cop[row_index][-1] += [entry]
                    new_position = [row_index, len(t_cop[row_index]) - 1 + row_index]
                    p_cop += [new_position]
                    if len(positions) > 1 and positions[-2][1] < positions[-1][1] and positions[-1][0] < new_position[0]:
                        k_cop += [entry - 1]
                    big_tabs.append([t_cop, p_cop, k_cop, shape])

                if row_index == 0 or 1 + len(tab[row_index]) < len(tab[row_index - 1]):
                    t_cop = copy.deepcopy(tab)
                    p_cop = copy.copy(positions)
                    k_cop = copy.copy(peakset)
                    s_cop = copy.deepcopy(shape)
                    t_cop[row_index] += [[entry]]
                    new_position = [row_index, len(t_cop[row_index]) - 1 + row_index]
                    p_cop += [new_position]
                    if len(positions) > 1 and positions[-2][1] < positions[-1][1] and positions[-1][0] < new_position[0]:
                        k_cop += [entry - 1]
                    s_cop[row_index] += 1
                    big_tabs.append([t_cop, p_cop, k_cop, s_cop])

            if len(tab) == 0 or len(tab[-1]) > 1:
                t_cop = copy.deepcopy(tab)
                p_cop = copy.copy(positions)
                k_cop = copy.copy(peakset)
                s_cop = copy.deepcopy(shape)
                t_cop += [[[entry]]]
                new_position = [len(t_cop) - 1, len(t_cop) - 1]
                p_cop += [new_position]
                if len(positions) > 1 and positions[-2][1] < positions[-1][1] and positions[-1][0] < new_position[0]:
                    k_cop += [entry - 1]
                s_cop += [1]
                big_tabs.append([t_cop, p_cop, k_cop, s_cop])
        tabs.append(big_tabs)
    return tabs


def create_q_peak_dict(tabs: list[list[list]]) -> dict[str, dict[str, list]]:
    rows: list[list] = []
    for size, group in enumerate(tabs):
        for tab in group:
            rows.append([tab[3], [size] + tab[2]])
    rows.sort(key=lambda item: str(item[0]))
    result: dict[str, dict[str, list]] = {}
    for shape, peakset in rows:
        result.setdefault(str(shape), {"peaksets": []})["peaksets"].append(peakset)
    return result


def add_tableau_peaks(max_length: int, perm_data: dict[str, dict[str, list]]) -> dict[str, dict[str, list]]:
    qdict = create_q_peak_dict(standard_shifted_svts(max_length))
    for perm in perm_data:
        tabpeaks: list[list[int]] = []
        for tab in perm_data[perm]["tabs"]:
            shape = [len(row) for row in tab]
            tabpeaks += qdict[str(shape)]["peaksets"]
        tabpeaks.sort(key=lambda item: str(item))
        perm_data[perm]["tabpeaks"] = tabpeaks
    return perm_data


def run_strongest(length: int, largest: int) -> dict[str, object]:
    timings: list[float] = []
    start = time.time()
    data = create_perm_dict(length, largest)
    timings.append(time.time() - start)
    start = time.time()
    add_word_peaks(data)
    timings.append(time.time() - start)
    start = time.time()
    add_hecke_tabs(data)
    timings.append(time.time() - start)
    start = time.time()
    add_tableau_peaks(length, data)
    timings.append(time.time() - start)

    good = 0
    bad = 0
    bad_examples: list[str] = []
    for perm in data:
        if data[perm]["peaksets"] == data[perm]["tabpeaks"]:
            good += 1
        else:
            bad += 1
            if len(bad_examples) < 5:
                bad_examples.append(perm)
    return {
        "mode": "strongest",
        "length": length,
        "largest": largest,
        "permutations": len(data),
        "same": good,
        "different": bad,
        "bad_examples": bad_examples,
        "timings_seconds": [round(value, 4) for value in timings],
    }


def print_summary(summary: dict[str, object]) -> None:
    mode = str(summary["mode"])
    label = {
        "basic": "Basic type C Grothendieck count check",
        "strong": "Strong type C Grothendieck count check",
        "strongest": "Strongest type C Grothendieck peakset check",
    }[mode]
    print(label)
    print(f"  max word length: {summary['length']}")
    print(f"  largest generator index: {summary['largest']}")
    print(f"  grouped signed permutations: {summary['permutations']}")
    print(f"  matching groups: {summary['same']}")
    print(f"  mismatching groups: {summary['different']}")
    if "shape_count_terms" in summary:
        print(f"  shifted tableau shape-count terms: {summary['shape_count_terms']}")
        print(f"  sample [word, tableau_count, word_count] records: {summary['sample_results']}")
    if "bad_examples" in summary:
        print(f"  bad examples: {summary['bad_examples']}")
        print(f"  timings seconds: {summary['timings_seconds']}")
    print(f"  PASS: {summary['different'] == 0}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["basic", "strong", "strongest", "all"], default="all")
    parser.add_argument("--length", type=int, default=4)
    parser.add_argument("--largest", type=int, default=3)
    args = parser.parse_args()

    if args.length <= 0:
        raise SystemExit("length must be positive")
    if args.largest < 0:
        raise SystemExit("largest must be nonnegative")
    if args.length > 8 or args.largest > 4:
        print("warning: this direct enumerator can grow quickly; source defaults include length=8, largest=4")

    modes: list[Mode] = ["basic", "strong", "strongest"] if args.mode == "all" else [args.mode]  # type: ignore[list-item]
    summaries: list[dict[str, object]] = []
    for mode in modes:
        if mode in ("basic", "strong"):
            summaries.append(run_basic_or_strong(mode, args.length, args.largest))
        else:
            summaries.append(run_strongest(args.length, args.largest))
        print_summary(summaries[-1])

    if any(summary["different"] != 0 for summary in summaries):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
```

### `items/type_c_grothendieck/code/README.md`

```markdown
# Code

`check_type_c_grothendieck.py` is a curated combined checker for the three
source scripts:

- `basic`: the original count comparison;
- `strong`: the count comparison with no adjacent equal Hecke letters and no
  consecutive entries in the same shifted set-valued tableau box;
- `strongest`: the peakset-preserving comparison.

Default command:

````bash
python code/check_type_c_grothendieck.py
````

The default run checks all three modes with max word length `4` and generator
indices `0..3`.

Useful options:

````bash
python code/check_type_c_grothendieck.py --mode basic --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strong --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strongest --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode all --length 4 --largest 3
````

The direct enumeration grows quickly.  The original source scripts used larger
defaults, including length `8`, largest generator `4` for the basic and strong
checks, and length `11`, largest generator `4` for the strongest check.

The file `type_c_grothendieck_default_summary.txt` records the curated default
summary.  These are bounded checks only; they do not prove the conjectures.
```

### `items/type_c_grothendieck/code/type_c_grothendieck_default_summary.txt`

```text
Type C Grothendieck bounded check, default run summary

Command:

  python code/check_type_c_grothendieck.py

Default parameters:

  max word length: 4
  largest generator index: 3
  modes: basic, strong, strongest

Key output:

  Basic type C Grothendieck count check
    grouped signed permutations: 53
    matching groups: 53
    mismatching groups: 0
    PASS: True

  Strong type C Grothendieck count check
    grouped signed permutations: 53
    matching groups: 53
    mismatching groups: 0
    PASS: True

  Strongest type C Grothendieck peakset check
    grouped signed permutations: 53
    matching groups: 53
    mismatching groups: 0
    PASS: True

Additional curation checks:

  python code/check_type_c_grothendieck.py --mode basic --length 5 --largest 3
  python code/check_type_c_grothendieck.py --mode strong --length 5 --largest 3
  python code/check_type_c_grothendieck.py --mode strongest --length 5 --largest 3

All three length-5 checks passed with 85 matching groups and 0 mismatching
groups.
```

### `items/type_c_grothendieck/explanation.tex`

```tex
\documentclass{article}
\usepackage{amsmath,amsthm,amssymb}

\title{Type C Grothendieck}
\author{}
\date{}

\newtheorem{conjecture}{Conjecture}
\newtheorem{remark}{Remark}

\begin{document}
\maketitle

\section{Objects}

For a signed permutation \(\omega\), the type \(C\) stable Grothendieck
polynomial, or \(K\)-theoretic Stanley symmetric function of type \(C\), is
defined in the source note as
\[
  GC_\omega=\sum_{f\in F_\omega} \mathbf{x}^{\operatorname{wt}(f)}.
\]
Here \(F_\omega\) is the set of signed factorizations for \(\omega\).  Such a
factorization begins with a word in the ordered alphabet
\[
  \cdots < -3 < -2 < -1 < -0 < 0 < 1 < 2 < 3 < \cdots,
\]
where \(i\) and \(-i\), for \(i\ne 0\), represent the simple transposition
\(s_i\), while \(0\) and \(-0\) represent the type \(C\) generator \(s_0\).  The
word is subdivided into strictly increasing factors, and the weight records the
factor sizes.

The \(Q\)-Grothendieck function is
\[
  GQ_\lambda=\sum_{q\in Q_\lambda}\mathbf{x}^{\operatorname{wt}(q)},
\]
where \(Q_\lambda\) is the set of semistandard shifted set-valued tableaux of
\(Q\)-type.

\section{Conjectural expansion}

The source conjecture predicts a positive \(GQ\)-expansion
\[
  GC_\omega = \sum_{t\in T_\omega} GQ_{\operatorname{shape}(t)},
\]
where \(T_\omega\) is the set of conjectural type \(C\) unimodal Hecke tableaux
for \(\omega\).

The source note also states a stronger \(GR\)-model formulation
\[
  GC_\omega^+ = \sum_{t\in T_\omega} GR_{\operatorname{shape}(t)}.
\]
Here \(GC_\omega^+\) restricts the signed factorizations by requiring a unique
minimum-absolute-value entry in each factor, with positive sign.  The \(GR\)
model is the shifted set-valued tableau submodel in which the first \(i\) or
\(i'\), read left to right and bottom to top, is constrained to be \(i\).

\section{Three checked levels}

The source code tests three increasingly strong finite statements.

\begin{conjecture}[Basic count level]
For each signed permutation \(\omega\) and word length \(n\), Hecke words of
length \(n\) for \(\omega\) are counted by pairs \((t,r)\), where
\(t\in T_\omega\), \(r\) is a standard shifted set-valued tableau with \(n\)
entries, and \(t\) and \(r\) have the same shape.
\end{conjecture}

\begin{conjecture}[Strong count level]
The same count holds after restricting to Hecke words with no adjacent equal
letters and to standard shifted set-valued tableaux with no consecutive entries
in the same box.
\end{conjecture}

\begin{conjecture}[Peakset-preserving level]
The correspondence can also be made peakset-preserving: a peak
\(w_{i-1}<w_i>w_{i+1}\) in the Hecke word corresponds to a peak at \(i\) in the
recording shifted set-valued tableau.
\end{conjecture}

\begin{remark}
The source note explains that the peakset-preserving level would imply the
positive \(GQ\)-expansion for \(GC_\omega\), with coefficients counted by type
\(C\) unimodal tableaux of the corresponding shape.
\end{remark}

\section{Computer check}

The script \texttt{code/check\_type\_c\_grothendieck.py} is a curated combined
port of the three source scripts.  Its default run checks all three levels with
max word length \(4\) and generator indices \(0,\ldots,3\).  During curation,
all three levels were also checked with max word length \(5\) and generator
indices \(0,\ldots,3\).

The original source scripts use larger default parameters, including length
\(8\), largest generator \(4\) for the basic and strong checks, and length
\(11\), largest generator \(4\) for the strongest check.  The curated defaults
are smaller so that the item remains quick to run.

These computations are finite evidence and regression checks.  They do not
construct the conjectural bijections and they do not prove the conjectures.

\end{document}
```

### `items/type_c_grothendieck/html/body.html`

```html
<p>This item records a conjectural hierarchy for type C stable Grothendieck polynomials <span class="math">GC_\omega</span>.</p>

<h2>Expansion</h2>

<p>For a signed permutation <span class="math">\omega</span>, the predicted positive expansion is</p>

<pre>GC_w = sum_{t in T_w} GQ_shape(t)</pre>

<p>where <span class="math">T_w</span> is the conjectural set of type C unimodal Hecke tableaux for <span class="math">w</span>. The source note also gives a stronger <span class="math">GR</span>-model formulation for <span class="math">GC_w^+</span>.</p>

<h2>Checked levels</h2>

<p>The basic check compares Hecke words with pairs consisting of a type C unimodal tableau and a standard shifted set-valued tableau of the same shape.</p>

<p>The strong check imposes no adjacent equal Hecke letters and no consecutive entries in the same shifted set-valued tableau box.</p>

<p>The strongest check compares peaksets. The source note explains that this peakset-preserving level would imply the positive <span class="math">GQ</span>-expansion.</p>

<h2>Computer check</h2>

<p>The script <code>code/check_type_c_grothendieck.py</code> is a combined curated checker for all three source scripts.</p>

<pre><code>python code/check_type_c_grothendieck.py</code></pre>

<p>The default run checks all three modes with max word length 4 and generator indices <code>0..3</code>. These are bounded checks, not proofs.</p>
```

### `items/type_c_grothendieck/item.yaml`

```yaml
title: Type C Grothendieck
slug: type_c_grothendieck
status_summary: Conjectural type C Grothendieck hierarchy, with basic, strong, and peakset-preserving bounded checks.
source_paths:
  - ../Conjectures-and-Computations/c-grothendieck/c-grothendieck.py
  - ../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strong.py
  - ../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strongest.py
  - ../Conjectures-and-Computations/c-grothendieck/c-grothendieck-note.tex
downloads:
  - explanation.tex
  - code/check_type_c_grothendieck.py
  - code/type_c_grothendieck_default_summary.txt
```

### `items/type_c_grothendieck/README.md`

```markdown
# Type C Grothendieck

Status summary: Conjectural type C Grothendieck hierarchy, with basic, strong, and peakset-preserving bounded checks.

## Summary

This item curates the type C Grothendieck conjecture hierarchy from the source
repository.  For a signed permutation `w`, the type C stable Grothendieck
polynomial `GC_w` is defined by signed factorizations of Hecke words.  The
target expansion is a positive expansion in `GQ` functions:

````text
GC_w = sum_{t in T_w} GQ_shape(t),
````

where `T_w` is the set of conjectural type C unimodal Hecke tableaux for `w`.

The source note explains a stronger `GR` formulation for `GC_w^+`, where `GR`
is the shifted set-valued tableau submodel in which the first `i` or `i'` in
the left-to-right, bottom-to-top reading word is constrained.  The computational
checks are organized as three levels:

- basic: compare Hecke words with pairs `(type C unimodal tableau, standard
  shifted set-valued tableau)` of the same shape;
- strong: impose no adjacent equal Hecke letters and no consecutive entries in
  the same shifted set-valued tableau box;
- strongest: compare peaksets, which would imply the `GQ`-positivity statement.

## Provenance

Source repository: `Conjectures-and-Computations`

Source paths:

- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck.py`
- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strong.py`
- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strongest.py`
- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck-note.tex`

Transfer type: curated writeup with adapted combined checker.

## Layers

Python layer: `code/check_type_c_grothendieck.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- Basic version: conjectural.
- Strong version: conjectural.
- Peakset-preserving version: conjectural.
- Curated code: bounded enumeration checks for all three levels.

## Code

From `Combinatorics/items/type_c_grothendieck`:

````bash
python code/check_type_c_grothendieck.py
````

The default run checks all three levels with max word length `4` and generator
indices `0..3`.  During curation, all three levels also passed with max word
length `5` and generator indices `0..3`.

The file `code/type_c_grothendieck_default_summary.txt` records the default
summary.  These checks are finite evidence, not proofs.
```

### `README.md`

```markdown
# Combinatorics

Curated mathematical results, conjectures, computations, examples, and
expository material.

This repository is organized around items. Each item should have clear
provenance, honest status labels, reproducible code when relevant, a precise
LaTeX explanation, and optional educational HTML content.

See `target_structure.md` for the intended repository architecture and
`target_contents.md` for the planned initial contents.

See `docs/source_policy.md` for provenance and code-transfer conventions.
Reusable item and code README templates are in `shared/templates/`.
```

### `requirements.txt`

```text
# The placeholder site builder uses only the Python standard library.
```

### `shared/html/.gitkeep`

```text

```

### `shared/latex/.gitkeep`

```text

```

### `shared/python/.gitkeep`

```text

```

### `shared/README.md`

```markdown
# Shared Support Files

Reusable support files used by more than one item belong here.

- `latex/`: shared LaTeX macros and preamble fragments.
- `python/`: shared Python utilities.
- `html/`: shared HTML, CSS, JavaScript, or interactive helpers.
```

### `shared/templates/code_README.md`

```markdown
# Code

Purpose:

Command:

Dependencies:

Input:

Output:

Range checked:

Runtime:

Expected success message:

Interpretation:

Limitations:

Source provenance:

Transfer type: verbatim copy | adapted from source | new implementation
```

### `shared/templates/item_README.md`

```markdown
# Item Title

Status summary:

## Summary

Briefly explain what this item is and why it belongs in `Combinatorics`.

## Provenance

Source repository:

Source paths:

Source date or commit:

Transfer type: verbatim copy | adapted code | rewritten exposition | new curated writeup

## Layers

Python layer: present | planned | not applicable

LaTeX layer: present | planned | not applicable

HTML layer: present | planned | not applicable

## Status

State exactly what is proved, conjectural, computationally checked, or still
draft. If different parts of the item have different statuses, list them
separately.

## Review Needs

List remaining mathematical, computational, or exposition review needs.
```

### `site/README.md`

```markdown
# Site Source

This directory contains templates and static files used by `../build_site.py`.

The generated site is written to `../docs/`.
```

### `site/static/styles.css`

```css
:root {
  color-scheme: light;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.5;
  color: #202124;
  background: #ffffff;
}

body {
  margin: 0;
}

a {
  color: #0b57d0;
}

.site-header {
  border-bottom: 1px solid #dadce0;
  padding: 16px 24px;
}

.site-title {
  color: #202124;
  font-weight: 700;
  text-decoration: none;
}

.site-main {
  max-width: 920px;
  margin: 0 auto;
  padding: 32px 24px 64px;
}

.page-heading {
  margin-bottom: 32px;
}

.page-heading h1 {
  margin: 0 0 8px;
}

.item-list {
  padding-left: 22px;
}
```

### `site/templates/base.html`

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ title }}</title>
  <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="/">Combinatorics</a>
  </header>
  <main class="site-main">
{{ content }}
  </main>
</body>
</html>
```

### `site/templates/home.html`

```html
<section class="page-heading">
  <h1>Combinatorics</h1>
  <p>Curated mathematical results, conjectures, computations, examples, and exposition.</p>
</section>

<section>
  <h2>Items</h2>
  <ul class="item-list">
{{ items }}
  </ul>
</section>
```

### `site/templates/item.html`

```html
<article class="item-page">
  <header class="page-heading">
    <h1>{{ title }}</h1>
    <p>{{ status_summary }}</p>
  </header>

  <section>
    <h2>Files</h2>
    <ul>
{{ downloads }}
    </ul>
  </section>

  <section>
    <h2>Educational Content</h2>
{{ body }}
  </section>
</article>
```

### `target_contents.md`

```markdown
# Target Contents For `Combinatorics`

This document records the first planned transfer targets from
`../Conjectures-and-Computations` into the curated public-facing
`Combinatorics` repository.

The goal is not to copy raw files directly. Each item should be selected,
given accurate mathematical status labels, supplied with provenance, and
eventually organized into the repository structure described in
`target_structure.md`.

## Source Repository

Primary source:

````text
../Conjectures-and-Computations/
````

The source repository contains exploratory and verification code for several
conjectures and computations in algebraic combinatorics. The material selected
below should be curated into explanatory items suitable for outside readers.

## Primary Items To Include

### 1. Computer-Assisted `qt`-Catalan Proof For The 2024 Paper

Suggested item slug:

````text
items/qt_catalan_computer_assisted_proofs_2024/
````

Source location:

````text
../Conjectures-and-Computations/qt-catalan/qt-assisted.py
../Conjectures-and-Computations/testing/catest.py
````

Description:

This item records the computer-assisted verification used to complete Lemma 2
and Lemma 3 of Section 9 of the 2024 rational `qt`-Catalan paper,
*A conjectured formula for the rational qt-Catalan polynomial*.

This is not merely a conjectural experiment. It should be presented as a
specific computational component supporting a proof, with a clear statement of
what the script verifies, what inputs or parameters are fixed, and what the
reader should run to reproduce the check.

Initial status:

````text
Status: computation
Verification: needs computational review
Python layer: present
LaTeX layer: planned
HTML layer: planned
````

Roadmap:

- Identify the exact mathematical statements of Lemma 2 and Lemma 3 in the
  paper.
- Explain precisely what finite checks the script performs.
- Treat `qt-assisted.py` as the primary source. Check `testing/catest.py` only
  as older related code if better/current code cannot be generated from the
  paper or recovered from the primary source files.
- Add a reproducibility-oriented `code/README.md`.
- Add a short LaTeX note connecting the computation to the proof.
- Add an educational HTML page explaining the role of the computation in the
  paper.

### 2. `qt`-Catalan Conjecture For The 2024 Paper

Suggested item slug:

````text
items/rational_qt_catalan_formula/
````

Source location:

````text
../Conjectures-and-Computations/qt-catalan/qt-conjecture.py
../Conjectures-and-Computations/testing/catest.py
````

Description:

This item presents the conjectural formula for the rational `qt`-Catalan
polynomial from the 2024 paper, together with the associated code for checking
the conjecture for relatively prime pairs `(r,n)`.

The item should clearly distinguish the proved parts of the paper from the
conjectural formula being tested. The code currently supplies evidence by
checking fixed relatively prime parameter pairs and reporting relevant data.

Initial status:

````text
Status: conjecture
Verification: needs mathematical review and computational review
Python layer: present
LaTeX layer: planned
HTML layer: planned
````

Roadmap:

- State the conjecture in a self-contained LaTeX layer.
- Record the exact range of computational evidence already checked.
- Explain why the relatively prime condition is required.
- Treat `qt-conjecture.py` as the primary source. Check `testing/catest.py`
  only as older related code if better/current code cannot be generated from
  the paper or recovered from the primary source files.
- Add a code README describing the `conjecture(r,n)` function and expected
  output.
- Add examples suitable for a public-facing HTML explanation.

### 3. Type C Grothendieck Material

Suggested item slug:

````text
items/type_c_grothendieck/
````

Source locations:

````text
../Conjectures-and-Computations/c-grothendieck/c-grothendieck.py
../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strong.py
../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strongest.py
../Conjectures-and-Computations/c-grothendieck/c-grothendieck-note.tex
````

Description:

This item collects the type C Grothendieck conjectures. The basic conjecture
compares Hecke words for signed permutations with pairs consisting of a type C
unimodal tableau and a shifted set-valued tableau of the same shape. The
stronger variants impose additional restrictions and, in the strongest version,
test peakset preservation.

The strongest version would imply a positivity statement for type C
Grothendieck functions in the `GQ` basis, with coefficients counted by
unimodal tableaux of a given shape.

Initial status:

````text
Status: conjecture
Verification: needs mathematical review and computational review
Python layer: present
LaTeX layer: present as source draft
HTML layer: planned
````

Roadmap:

- Decide whether the basic, strong, and strongest versions should be presented
  as one item with subclaims or split into separate subitems.
- Review `c-grothendieck-note.tex` for suitability as the starting LaTeX
  explanation.
- Clarify definitions: signed permutations, Hecke words, type C unimodal
  tableaux, shifted set-valued tableaux, peaksets, and `GQ` positivity.
- Record checked parameter ranges for each script.
- Add examples comparing the three conjectural levels.

### 4. Shifted Littlewood-Richardson Material

Suggested item slug:

````text
items/shifted_littlewood_richardson/
````

Source locations:

````text
../Conjectures-and-Computations/shifted-LR/skew-GQ-expansion.py
../Conjectures-and-Computations/shifted-LR/skew-GP-expansion.py
../Conjectures-and-Computations/shifted-LR/skew GP_GQ.tex
````

Description:

This item collects conjectural shifted Littlewood-Richardson rules for skew
stable Grothendieck functions in the shifted setting.

The `GQ` script tests a conjectural rule for coefficients in the expansion of
a skew `GQ` function into ordinary `GQ` functions, using the related `GR`
formulation described in the source README. The `GP` script tests a similar,
slightly simpler conjectural rule for the expansion of skew `GP` functions
into ordinary `GP` functions.

Initial status:

````text
Status: conjecture
Verification: needs mathematical review and computational review
Python layer: present
LaTeX layer: present as source draft
HTML layer: planned
````

Roadmap:

- Decide whether the `GQ` and `GP` rules should be one item with two branches
  or two closely linked items.
- Review `skew GP_GQ.tex` as a possible source for the LaTeX explanation.
- State the conjectural coefficient rules precisely.
- Explain the relation among `GP`, `GQ`, and `GR`.
- Record checked degrees, shapes, skew shapes, and number of variables.
- Add small examples suitable for an HTML layer.

## Possible Low-Emphasis Item

### Armstrong/Johnson Poset Decomposition Material

Source locations:

````text
../Conjectures-and-Computations/qt-catalan/johnson.py
../Conjectures-and-Computations/qt-catalan/poset_decomps.txt
````

Description:

This material concerns a conjecture due to Armstrong, based on work of
Johnson, related to decompositions for `B_a(m,n)`. It is relevant background
and may be useful to preserve, but it should not be emphasized as a primary
author item in the first public-facing version of `Combinatorics`.

Recommended treatment:

````text
Status: possible related-work or appendix item
Priority: low
````

If included, it should be clearly marked as external conjectural material and
connected to the appropriate outside reference.

## Initial Curation Priorities

1. Start with the computer-assisted `qt`-Catalan proof because it has the
   clearest proof-support role.
2. Add the rational `qt`-Catalan conjecture as a separate but linked item.
3. Curate the type C Grothendieck material as a family of related conjectures.
4. Curate the shifted Littlewood-Richardson material as a second conjectural
   family.
5. Mention Armstrong/Johnson material only if it helps explain context or
   related work.

## Additional Items From `Dyck`

The following items should be curated from the neighboring `../Dyck`
repository. The main 2026 paper anchor is:

````text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/arxiv_submission.pdf
````

The title in that source is:

````text
Dyck Symmetric Functions and Applications to q,t-Catalan Polynomials
````

The sectioned draft source is also available at:

````text
../Dyck/paper/working_drafts/draft_v3.tex
../Dyck/paper/working_drafts/draft_v3_sections/
````

### 5. Computer-Assisted Material From The 2026 Preprint

Suggested item slug:

````text
items/dyck_symmetric_computer_assisted_proofs_2026/
````

Source locations:

````text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/appendix_a_code.tex
../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_local_proofs.tex
../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_lemma_525.tex
../Dyck/code/codex_project/verify_east7_west7_corrected.py
../Dyck/code/codex_project/verify_reduced_residual_local_lemmas.py
../Dyck/code/codex_project/verify_finite_local_lemmas.py
../Dyck/code/code_assistant/reviews/CA-0026_lemma_5_24_corrected_east7_west7_checker_review.md
````

Description:

This item records the computer-assisted parts of the 2026 preprint
*Dyck Symmetric Functions and Applications to q,t-Catalan Polynomials*.
The most important computational artifacts concern the finite local checks
behind the Section 5 skeleton decomposition, especially the corrected
East7/West7 verification and the reduced residual local lemma checks.

This item should be presented as proof-supporting computation for specific
lemmas and appendices, not as exploratory evidence.

Initial status:

````text
Status: computation
Verification: tied to 2026 preprint; needs independent computational packaging
Python layer: present
LaTeX layer: present in source paper
HTML layer: planned
````

Roadmap:

- Identify every theorem or lemma in the 2026 preprint that depends on a
  finite computation.
- Separate proof-critical scripts from historical or superseded scripts.
- Treat `verify_east7_west7_corrected.py` as the durable East7/West7 checker.
- Add a public `code/README.md` explaining commands, expected output, ranges,
  runtime, and interpretation.
- Add a concise LaTeX explanation of how the computations enter the proof.

### 6. Flat Middle Coefficients

Suggested item slug:

````text
items/qt_catalan_middle_coefficients/
````

Source locations:

````text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex
../Dyck/code/codex_project/red_team_flat_middle_coefficients.py
../Dyck/code/code_assistant/codex_tasks/CA-0011_flat_middle_coefficients.md
../Dyck/code/code_assistant/reviews/CA-0011_flat_middle_coefficients_review.md
````

Description:

This item should collect flat-middle-coefficient phenomena for classical and
rational `q,t`-Catalan polynomials.

The 2026 preprint gives the weakest currently proved version: in the classical
case, the result is proved only in the low-deficit range
`\defc <= 2n-8`. There is also a conjectural `r == 1 mod s` version somewhere
in the `Dyck` project, and the general rational `r/s` case remains an open
experimental target.

Initial status:

````text
Status: mixed theorem / conjecture / computation
Verification: needs mathematical review and computational review
Python layer: present for classical checks; rational code may need extension
LaTeX layer: present for classical case in source paper
HTML layer: planned
````

Known status distinctions:

- Classical case: proved in the 2026 preprint in the range
  `\defc <= 2n-8`.
- `r == 1 mod s` case: conjectural; source and exact bound should be located
  in `Dyck`.
- General rational `r/s` case: needs new testing to determine where the middle
  flat region begins and whether a clean general statement exists.

Roadmap:

- Extract the exact flat-middle statement from the 2026 paper.
- Locate the `r == 1 mod s` conjectural statement and its tested bound.
- Write or adapt code to test the general `r/s` case.
- State the most general version supported by evidence.
- Explicitly say that the 2026 preprint proves only the classical low-deficit
  version.

### 7. Dyck Symmetric Functions

Suggested item slug:

````text
items/dyck_symmetric_functions/
````

Source locations:

````text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/03_row_and_tableau_insertion.tex
../Dyck/paper/working_drafts/draft_v3_sections/03_tableau_bijection_schur.tex
../Dyck/paper/working_drafts/draft_v3_sections/04_bijections.tex
../Dyck/paper/working_drafts/draft_v3_sections/04_type4_formula.tex
../Dyck/paper/research_notes/rational_generalizations.tex
../Dyck/code/codex_project/paper_algorithms/
../Dyck/code/codex_project/red_team_rational_dyck_generalization.py
../Dyck/code/codex_project/red_team_rational_qt_catalan_formula.py
````

Description:

This item presents Dyck symmetric functions and dual Dyck symmetric functions.
The classical construction and Schur-positivity results should be treated as
proved by reference to the 2026 preprint.

There is also an `r == 1 mod s`, equivalently `r = s*t + 1`, analogue in
`Dyck`, with code-checked evidence. This should be included only as a
conjectural/computational extension after the relevant source files and exact
statements are isolated. This item should not be presented as a general
rational Dyck symmetric-function theory.

Initial status:

````text
Status: mixed theorem / conjecture
Verification: classical proved by 2026 preprint; r == 1 mod s analogue needs review
Python layer: present
LaTeX layer: present for classical case in source paper
HTML layer: planned
````

Roadmap:

- Curate the classical definitions and theorems from the 2026 preprint.
- Add source references for Schur positivity and affine/dual variants.
- Locate the `r == 1 mod s` analogue and code checks.
- Keep the `r == 1 mod s` analogue visibly separate from the classical
  theorem statements.

### 8. Dyck Skeleton Formula

Suggested item slug:

````text
items/dyck_skeleton_tableau_formulas/
````

Source locations:

````text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_skeletons_setup.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex
../Dyck/code/codex_project/red_team_theorem_5_30_formula.py
../Dyck/code/code_assistant/reviews/CA-0015_theorem_5_30_formula_comparison_review.md
../Dyck/memory/proof_audits/theorem_5_30_qt_catalan_skeleton.md
````

Description:

This item presents the Dyck skeleton formula for the high-total-degree /
low-deficit part of the classical `q,t`-Catalan polynomial. It is built from
the Dyck skeleton machinery but requires additional arguments beyond the
definition of Dyck symmetric functions.

The classical formula is proved in the 2026 preprint in the range
`\defc <= 2n-8`. The corresponding `r == 1 mod s` formula should be treated as
conjectural until its exact statement, bound, and evidence are curated.

Initial status:

````text
Status: mixed theorem / conjecture / computation
Verification: classical theorem in 2026 preprint; r == 1 mod s analogue needs review
Python layer: present
LaTeX layer: present for classical case in source paper
HTML layer: planned
````

Roadmap:

- Extract the precise Theorem 5.30 statement from the 2026 preprint.
- Separate the skeleton formula from the underlying Dyck symmetric function
  definitions.
- Add the bounded coefficient comparison code as supporting material.
- Locate and state the `r == 1 mod s` analogue, including the correct bound.
- Explain how this item relates to flat middle coefficients.

### 9. Dyck Skeleton String Decomposition And Rational Cyclic Maps

Suggested item slug:

````text
items/dyck_skeleton_string_decompositions/
````

Source locations:

````text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_up_down.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_east_map.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_east_west_inverse.tex
../Dyck/code/codex_project/paper_algorithms/up_down.py
../Dyck/code/codex_project/paper_algorithms/east_west_local.py
../Dyck/code/codex_project/red_team_up_string_decomposition.py
../Dyck/code/codex_project/red_team_rational_skeleton_string_formula.py
../Dyck/code/codex_project/red_team_rational_cyclic_summands.py
../Dyck/code/codex_project/red_team_rational_cyclic_missing_lemmas.py
../Dyck/code/codex_project/red_team_rational_cyclic_endpoint_tokens.py
../Dyck/code/codex_project/red_team_nrct_candidate_statements.py
../Dyck/code/codex_project/red_team_nrct_endpoint_obligations.py
../Dyck/paper/research_notes/naive_rational_cyclic_map.tex
../Dyck/paper/research_notes/naive_rational_cyclic_map_thm.tex
../Dyck/docs/rational_cyclic_defc_readability_draft.md
../Dyck/docs/rational_cyclic_defc_proof_plan.md
../Dyck/docs/research_progress.md
````

Description:

This item should combine the classical Dyck skeleton string decomposition, its
`r == 1 mod s` rational analogue, and the naive rational cyclic map material.

In the classical case, the 2026 preprint proves the skeleton string
decomposition in the range `\defc <= 2n-8`, using local East/West maps up to
East7/West7. In the `r == 1 mod s` case, the corresponding skeleton-string
formula is conjectural and should be sourced from `Dyck`; the proper bound is
expected to be
`\defc_\tau <= (s-2)(\tau+1)-4`. In the general rational case, the naive
rational cyclic map appears to be the East3/West3-level analogue and can be
used to explore what rational skeletons should be.

The naive rational cyclic map theorem should not yet be labeled as a fully
human-verified theorem. The current honest status is that there is computational
support together with an AI-generated and AI-checked proof draft that has not
yet been human verified.

Initial status:

````text
Status: mixed theorem / conjecture / draft
Verification: classical proved in 2026 preprint; rational material not human verified
Python layer: present
LaTeX layer: present as source paper and research notes
HTML layer: planned
````

Known status distinctions:

- Classical Dyck skeleton strings: proved in the 2026 preprint for
  `\defc <= 2n-8`, with local maps up to East7/West7.
- `r == 1 mod s` skeleton strings: conjectural; current expected bound is
  `\defc_\tau <= (s-2)(\tau+1)-4`.
- General rational / NRCM: computationally supported; proof draft is
  AI-generated and AI-checked but not human verified.
- NRCM relation: tentatively treat the naive rational cyclic map as the
  rational analogue of the East3/West3-and-below cases.

Roadmap:

- Extract the classical up/down string-decomposition theorem and supporting
  East/West local maps from the 2026 preprint.
- Locate the precise `r == 1 mod s` skeleton-string conjecture statement
  underlying the bound `\defc_\tau <= (s-2)(\tau+1)-4`.
- Derive and test explicit East5/West5 definitions for the `r == 1 mod s`
  case as a possible route toward a smaller-deficit proof.
- Use the NRCM to investigate what rational skeletons should mean in the
  general `r/s` case.
- Keep the NRCM proof status visibly distinct from human-verified theorem
  status.

## Updated Curation Priorities

1. Keep the `Conjectures-and-Computations` items as the first source-family
   transfer.
2. Add the 2026 preprint metadata to `publications/` early, since several
   Dyck-derived items should cite it.
3. Package the 2026 computer-assisted proof artifacts before presenting them
   publicly.
4. Curate the classical Dyck symmetric function, skeleton formula, and
   skeleton-string results as proved 2026-paper material.
5. Treat `r == 1 mod s` and general rational extensions as conjectural or
   draft material until their statements, bounds, and evidence are isolated.
```

### `target_structure.md`

```markdown
# Target Structure For `Combinatorics`

## Purpose

`Combinatorics` is a public-facing curated repository for selected mathematical results, conjectures, computations, examples, and expository material.

Much of the material will originate, or have earlier versions, in neighboring repositories such as `Conjectures_and_Computations` and `Dyck`. Material should not be copied into `Combinatorics` as raw notes. It should be selected, labeled, contextualized, and made useful to outside readers.

The intended audience includes mathematicians, researchers interested in the author's work, and technically sophisticated readers who want to understand both the results and some of the methods behind them.

## Guiding Principle

Each substantial item should ideally have three connected layers:

1. Python code for computation, examples, verification, or data generation.
2. LaTeX explanation for precise mathematical statements, definitions, conjectures, proofs, or evidence.
3. HTML educational material for examples, visualization, exposition, and possible interactive exploration.

Not every item needs all three layers immediately. The repository should allow partial development, provided the current status is clear.

## Buildable HTML Site

The repository should contain a buildable static HTML site. The site should
have a homepage that describes the curated contents and links to one page for
each item.

The homepage should explain:

- the main conjectures, computations, and results in the repository;
- how they relate to one another;
- how they relate to the author's published papers and preprints;
- how they relate to work by other authors;
- which topics are proved, conjectural, computational, experimental, or expository;
- where a reader should start depending on their background and interests.

Each item page should contain:

- a short introduction;
- status, provenance, and verification labels;
- links to view or download the Python code;
- links to view or download the compiled LaTeX PDF;
- a link to download the LaTeX source;
- embedded educational HTML content for examples, explanation, visualization, or interaction.

The source for the site should live in `site/`. The generated static site
should live in `docs/`, so it can be served directly by GitHub Pages if desired.

Suggested site locations:

````text
site/
  README.md
  templates/
  static/

docs/
  index.html
  items/
````

The generated site should be public-facing and navigable. It should not merely
be a file listing. It should help a reader understand the mathematical
landscape.

## Suggested Repository Layout

````text
Combinatorics/
  README.md
  target_structure.md
  target_contents.md
  bibliography.bib
  build_site.py
  requirements.txt

  items/
    item_slug/
      item.yaml
      README.md
      explanation.tex
      explanation.pdf
      code/
        README.md
        verify.py
      html/
        body.html
      assets/

  shared/
    latex/
    python/
    html/

  site/
    README.md
    templates/
    static/

  docs/
    index.html
    items/
````

The exact names can evolve, but the repository should keep a clear distinction
between curated mathematical items, shared support files, site source files, and
generated site output.

The repository should not store copies of papers by default. Instead, item
metadata and item pages should link to arXiv, journal pages, DOI pages, or
other stable external locations as needed. The top-level `bibliography.bib`
should contain only BibTeX entries actually used by item LaTeX files or the
site.

## Per-Item Structure

Each item should live in its own directory under `items/`.

Suggested form:

````text
items/
  rational_qt_catalan_candidate/
    item.yaml
    README.md
    explanation.tex
    explanation.pdf
    code/
      README.md
      verify.py
    html/
      body.html
    assets/
````

### `item.yaml`

The `item.yaml` file is machine-readable metadata for the site builder. It
should record the item title, slug, status labels, source paths, related paper
links, and which files should appear on the generated item page.

Suggested fields:

````text
title:
slug:
status_summary:
source_paths:
related_papers:
site_priority:
````

Only `title`, `slug`, `status_summary`, and `source_paths` should be treated as
core fields. Other metadata should be added only when it is useful.

### `README.md`

The item `README.md` is the controlling document. It should summarize what the item is, what status it has, and where it came from.

Recommended metadata:

````text
Title:
Status summary:
Source:
Source date:
Related publications:
Related external work:
````

If an item contains several claims or constructions with different statuses,
the README should explain those internal statuses in prose or a short table.

### `explanation.tex`

The LaTeX file should contain the precise mathematical material:

- definitions;
- theorem, proposition, lemma, conjecture, or question statements;
- proofs when available;
- computational evidence when relevant;
- remarks connecting the item to the literature.

The LaTeX should be mathematically honest. It should not present a conjecture or computation as a theorem.

### `explanation.pdf`

The PDF should be the compiled version of `explanation.tex`. The generated
site should link to it for viewing and downloading. If the LaTeX layer is not
yet present, the item metadata should mark the PDF as planned rather than
pretending it exists.

### `code/`

The code directory should contain reproducible scripts, not unexplained exploratory code.

The local `code/README.md` should state:

````text
Purpose:
Command:
Dependencies:
Input:
Output:
Range checked:
Runtime:
Interpretation:
Limitations:
````

When the code supports a mathematical statement, the exact scope of the computation should be clear.

### `html/`

The HTML directory should contain educational or example-driven material for the item.

This may include:

- interactive examples;
- diagrams;
- generated data visualizations;
- simplified explanations;
- guided examples of definitions or conjectures.

The preferred file is `html/body.html`, which the site builder inserts into the
generated item page. The HTML layer should serve the mathematics. It should not
replace the precise LaTeX statement.

### `assets/`

The item `assets/` directory should contain item-specific files such as images,
generated tables, data files, diagrams, or downloadable artifacts. Files used
by more than one item should go in `shared/` instead.

## Shared Support Files

The `shared/` directory is for reusable support files used by more than one
item. It should not contain item-specific mathematical content.

````text
shared/
  latex/
  python/
  html/
````

### `shared/latex/`

Reusable LaTeX infrastructure:

- common macros;
- theorem styles;
- shared preamble fragments;
- bibliography helpers if needed.

### `shared/python/`

Reusable Python helpers used by multiple item scripts:

- Dyck path utilities;
- rational path generators;
- coefficient dictionary helpers;
- shared test utilities.

### `shared/html/`

Reusable web assets or helpers used by multiple item pages:

- CSS;
- JavaScript;
- shared images or icons;
- shared interactive helpers.

Files that belong to a single item should remain in that item's directory.
Files that are part of the site template or build machinery should live in
`site/`, not `shared/`.

## Bibliography

The repository should maintain a single top-level bibliography file:

````text
bibliography.bib
````

This file should collect only BibTeX entries used by item LaTeX files, item
pages, or the generated site. It is not intended to be a complete publication
archive.

## Site Build Files

The build command should be simple and reproducible:

````text
python build_site.py
````

The builder should read item metadata from `items/*/item.yaml`, combine it with
templates from `site/templates/`, copy needed assets, and write the generated
static site to `docs/`.

The `docs/` directory is generated output. It may be committed so that GitHub
Pages can publish directly from it.

## Status Conventions

Use a simple item-level status summary rather than many rigid status fields.
Different contents inside the same item may have different statuses, so the
item-level summary should be brief and honest.

Example:

````text
Status summary: Classical case proved in the 2026 preprint; r == 1 mod s analogue conjectural.
````

The item README should then give the details:

````text
## Status

- Classical formula: theorem, proved in the 2026 preprint.
- r == 1 mod s formula: conjectural, computational evidence.
- General rational version: not yet formulated.
````

For computation items, the status section should state what the computation
checks, whether it is proof-supporting or exploratory, and what review remains.

## Agent Workflow

Workspace-level agents in `../agents/` help shape this repository.

- The advisor agent controls curation, provenance, repo boundaries, and routing.
- The mathematical accuracy agent checks statements, proofs, definitions, and status labels.
- The pedagogy and exposition agent improves readability and public-facing explanation.
- The software and computation agent checks code, reproducibility, and computational interpretation.

Before substantial material enters `Combinatorics`, it should be reviewed by the relevant agents.

## Transfer Standard

When transferring material from another repository:

1. Identify the source repo and path.
2. Determine whether the material belongs in `Combinatorics`.
3. Determine its mathematical status.
4. Create a curated item directory under `items/`.
5. Add provenance and status metadata to the item `README.md`.
6. Add or adapt the LaTeX layer.
7. Add or adapt the Python layer if computation is relevant.
8. Add or plan the HTML educational layer.
9. Add item metadata so the generated site can link to code, PDF, LaTeX, and
   educational content.
10. Mark any remaining review needs.

## Public-Facing Standard

`Combinatorics` should be legible, honest, and useful.

It should make interesting mathematics visible without overstating what is known. It should help readers see individual ideas, computational evidence, and the larger research picture.
```
