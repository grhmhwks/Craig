# Phase 5 mathematical rendering

Phase 5 renders CRAIG answers as safe Markdown, KaTeX mathematics, and a small
set of typed mathematical visualizations. It does not change the read-only
corpus boundary: every file beneath `content/` remains source material only.

## Rendering boundary

Assistant text is parsed by `react-markdown` with raw HTML disabled. Inline
mathematics uses `$...$`, display mathematics uses `$$...$$`, and KaTeX runs
with trust disabled, bounded macro expansion, and non-throwing parse errors.
No `rehype-raw` stage is installed.

A visualization is accepted only from a recognized fenced-code language and
only after its JSON object passes the corresponding strict schema. Unknown
fields are rejected. String lengths, row counts, cell counts, sequence lengths,
vertices, edges, and source size are bounded. Values are normalized to text and
React constructs all SVG and HTML nodes; JSON values are never interpreted as
markup. An invalid block displays its validation error and original text.

## Trusted block schemas

All fields other than those listed are invalid. `title` is optional everywhere.

| Fence | Required fields | Optional fields |
| --- | --- | --- |
| `tableau` | `rows` | `variant`, `shifted`, `orientation`, `title` |
| `young-diagram` | `shape` | `inner_shape`, `shifted`, `orientation`, `title` |
| `dyck-path` | `steps` | `kind`, `r`, `s`, `boundary`, `show_diagonal`, `title` |
| `reading-word` | `entries` | `direction`, `highlights`, `title` |
| `factorization` | `factors` | `separator`, `title` |
| `skeleton` | `vertices` | `edges`, `directed`, `title` |
| `string-diagram` | `strings` | `links`, `title` |

Aliases `diagram`, `dyck`, `word`, and `strings` are also recognized. Examples:

````text
```tableau
{
  "variant": "set-valued",
  "shifted": true,
  "rows": [["1'", ["1", "2'"], "3"], [["2", "3"], "4"]]
}
```

```young-diagram
{"shape": [5, 3, 2], "inner_shape": [2, 1], "shifted": true}
```

```dyck-path
{"kind": "rational", "r": 5, "s": 3, "steps": "NNEENEEE"}
```

```skeleton
{
  "directed": true,
  "vertices": [{"id": "a", "label": "A"}, {"id": "b", "label": "B"}],
  "edges": [{"from": "a", "to": "b", "label": "i"}]
}
```
````

Tableau and partition row lengths must be weakly decreasing and are strictly
decreasing when shifted. Multi-entry cells require the `set-valued` variant. A
rational Dyck path must end at `(r,s)` and remain on its declared side of the
diagonal. Graph identifiers and string endpoints must resolve. Skeleton
coordinates, when supplied, are percentages from 0 through 100 and must be
supplied for every vertex.

## Manual review and tests

Install frontend dependencies and run the checks:

```text
cd app/frontend
npm install
npm run typecheck
npm test
npm run dev
```

In the desktop interface, choose **Preview renderers** in the left sidebar to
open the built-in gallery. It exercises Markdown, inline and display TeX, every
renderer family, shifted and set-valued cases, and inspection of the trusted
source specification. Renderer SVGs have accessible titles and descriptions,
and wide diagrams scroll rather than overflowing the answer column.

The Python test suite also checks that the grounded-answer prompt exposes only
these trusted formats and forbids raw HTML and SVG.
