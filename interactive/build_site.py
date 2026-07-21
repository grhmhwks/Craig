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
