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
