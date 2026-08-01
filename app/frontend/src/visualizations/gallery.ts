const FENCE = "```";

export const RENDERER_GALLERY_MARKDOWN = String.raw`
## Trusted mathematical renderer gallery

Inline mathematics such as $s_\lambda = \sum_T x^{\mathrm{wt}(T)}$ and display
mathematics render through the same safe Markdown pipeline:

$$
\sum_{k=0}^{n} \binom{n}{k} = 2^n.
$$

### Ordinary and set-valued tableaux

${FENCE}tableau
{
  "title": "Ordinary tableau of shape (4, 3, 1)",
  "rows": [[1, 1, 2, 4], [2, 3, 4], [5]]
}
${FENCE}

${FENCE}tableau
{
  "title": "Shifted set-valued tableau",
  "variant": "set-valued",
  "shifted": true,
  "rows": [["1'", ["1", "2'"], "3"], [["2", "3"], "4"]]
}
${FENCE}

### Young and skew diagrams

${FENCE}young-diagram
{
  "title": "Shifted skew shape (5, 3, 2) / (2, 1)",
  "shape": [5, 3, 2],
  "inner_shape": [2, 1],
  "shifted": true
}
${FENCE}

### Ordinary and rational Dyck paths

${FENCE}dyck-path
{
  "title": "Dyck path of semilength 4",
  "kind": "ordinary",
  "steps": "NNEENNEE"
}
${FENCE}

${FENCE}dyck-path
{
  "title": "A rational (5, 3)-Dyck path",
  "kind": "rational",
  "r": 5,
  "s": 3,
  "steps": "NNEENEEE"
}
${FENCE}

### Reading words and factorizations

${FENCE}reading-word
{
  "title": "Highlighted reading word",
  "entries": ["4", "2'", "3", "1", "1'"],
  "direction": "right-to-left",
  "highlights": [1, 3]
}
${FENCE}

${FENCE}factorization
{
  "title": "Three-factor decomposition",
  "factors": [["s₁", "s₂"], ["s₃"], ["s₂", "s₁"]],
  "separator": "·"
}
${FENCE}

### Skeleton and string diagrams

${FENCE}skeleton
{
  "title": "Directed local-move skeleton",
  "directed": true,
  "vertices": [
    {"id": "a", "label": "A"},
    {"id": "b", "label": "B"},
    {"id": "c", "label": "C"},
    {"id": "d", "label": "D"}
  ],
  "edges": [
    {"from": "a", "to": "b", "label": "i"},
    {"from": "b", "to": "c", "label": "j"},
    {"from": "c", "to": "d"},
    {"from": "d", "to": "a"}
  ]
}
${FENCE}

${FENCE}string-diagram
{
  "title": "Linked string decomposition",
  "strings": [
    {"id": "top", "label": "top string", "entries": ["1", "2", "4"]},
    {"id": "bottom", "label": "bottom string", "entries": ["1'", "3", "5"]}
  ],
  "links": [
    {
      "from": {"string": "top", "index": 1},
      "to": {"string": "bottom", "index": 1},
      "label": "match"
    }
  ]
}
${FENCE}

Invalid or oversized JSON never becomes HTML or SVG; CRAIG shows a readable text
fallback with the validation error instead.
`;
