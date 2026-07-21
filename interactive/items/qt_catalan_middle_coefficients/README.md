# qt-Catalan Middle Coefficients

Status summary: Classical flat middle coefficients are proved in the Dyck-skeleton range `0 <= d <= 2n-8`; the full flat-middle range is conjectural.

## Summary

Let `C_n(q,t)` be computed in the direct Dyck-area-sequence convention
`sum_D q^area(D)t^dinv(D)`, and let `M = binom(n,2)`.  The Dyck-skeleton
decomposition proves that, for `n >= 4` and `0 <= d <= 2n-8`, the coefficients
of

```text
q^j t^(M-d-j),   d <= j <= M-2d,
```

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

```bash
python code/check_flat_middle_coefficients.py
```

The default run checks `n=4..8`, 25 `(n,d)` bands, and 325 middle-band
coefficients.  The output is summarized in
`code/flat_middle_coefficients_default_summary.txt`.
