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
