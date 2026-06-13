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

```text
site/
  README.md
  templates/
  static/

docs/
  index.html
  items/
```

The generated site should be public-facing and navigable. It should not merely
be a file listing. It should help a reader understand the mathematical
landscape.

## Suggested Repository Layout

```text
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
```

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

```text
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
```

### `item.yaml`

The `item.yaml` file is machine-readable metadata for the site builder. It
should record the item title, slug, status labels, source paths, related paper
links, and which files should appear on the generated item page.

Suggested fields:

```text
title:
slug:
status_summary:
source_paths:
related_papers:
site_priority:
```

Only `title`, `slug`, `status_summary`, and `source_paths` should be treated as
core fields. Other metadata should be added only when it is useful.

### `README.md`

The item `README.md` is the controlling document. It should summarize what the item is, what status it has, and where it came from.

Recommended metadata:

```text
Title:
Status summary:
Source:
Source date:
Related publications:
Related external work:
```

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

```text
Purpose:
Command:
Dependencies:
Input:
Output:
Range checked:
Runtime:
Interpretation:
Limitations:
```

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

```text
shared/
  latex/
  python/
  html/
```

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

```text
bibliography.bib
```

This file should collect only BibTeX entries used by item LaTeX files, item
pages, or the generated site. It is not intended to be a complete publication
archive.

## Site Build Files

The build command should be simple and reproducible:

```text
python build_site.py
```

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

```text
Status summary: Classical case proved in the 2026 preprint; r == 1 mod s analogue conjectural.
```

The item README should then give the details:

```text
## Status

- Classical formula: theorem, proved in the 2026 preprint.
- r == 1 mod s formula: conjectural, computational evidence.
- General rational version: not yet formulated.
```

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
