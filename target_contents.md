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

```text
../Conjectures-and-Computations/
```

The source repository contains exploratory and verification code for several
conjectures and computations in algebraic combinatorics. The material selected
below should be curated into explanatory items suitable for outside readers.

## Primary Items To Include

### 1. Computer-Assisted `qt`-Catalan Proof For The 2024 Paper

Suggested item slug:

```text
items/qt_catalan_computer_assisted_proofs_2024/
```

Source location:

```text
../Conjectures-and-Computations/qt-catalan/qt-assisted.py
../Conjectures-and-Computations/testing/catest.py
```

Description:

This item records the computer-assisted verification used to complete Lemma 2
and Lemma 3 of Section 9 of the 2024 rational `qt`-Catalan paper,
*A conjectured formula for the rational qt-Catalan polynomial*.

This is not merely a conjectural experiment. It should be presented as a
specific computational component supporting a proof, with a clear statement of
what the script verifies, what inputs or parameters are fixed, and what the
reader should run to reproduce the check.

Initial status:

```text
Status: computation
Verification: needs computational review
Python layer: present
LaTeX layer: planned
HTML layer: planned
```

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

```text
items/rational_qt_catalan_formula/
```

Source location:

```text
../Conjectures-and-Computations/qt-catalan/qt-conjecture.py
../Conjectures-and-Computations/testing/catest.py
```

Description:

This item presents the conjectural formula for the rational `qt`-Catalan
polynomial from the 2024 paper, together with the associated code for checking
the conjecture for relatively prime pairs `(r,n)`.

The item should clearly distinguish the proved parts of the paper from the
conjectural formula being tested. The code currently supplies evidence by
checking fixed relatively prime parameter pairs and reporting relevant data.

Initial status:

```text
Status: conjecture
Verification: needs mathematical review and computational review
Python layer: present
LaTeX layer: planned
HTML layer: planned
```

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

```text
items/type_c_grothendieck/
```

Source locations:

```text
../Conjectures-and-Computations/c-grothendieck/c-grothendieck.py
../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strong.py
../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strongest.py
../Conjectures-and-Computations/c-grothendieck/c-grothendieck-note.tex
```

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

```text
Status: conjecture
Verification: needs mathematical review and computational review
Python layer: present
LaTeX layer: present as source draft
HTML layer: planned
```

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

```text
items/shifted_littlewood_richardson/
```

Source locations:

```text
../Conjectures-and-Computations/shifted-LR/skew-GQ-expansion.py
../Conjectures-and-Computations/shifted-LR/skew-GP-expansion.py
../Conjectures-and-Computations/shifted-LR/skew GP_GQ.tex
```

Description:

This item collects conjectural shifted Littlewood-Richardson rules for skew
stable Grothendieck functions in the shifted setting.

The `GQ` script tests a conjectural rule for coefficients in the expansion of
a skew `GQ` function into ordinary `GQ` functions, using the related `GR`
formulation described in the source README. The `GP` script tests a similar,
slightly simpler conjectural rule for the expansion of skew `GP` functions
into ordinary `GP` functions.

Initial status:

```text
Status: conjecture
Verification: needs mathematical review and computational review
Python layer: present
LaTeX layer: present as source draft
HTML layer: planned
```

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

```text
../Conjectures-and-Computations/qt-catalan/johnson.py
../Conjectures-and-Computations/qt-catalan/poset_decomps.txt
```

Description:

This material concerns a conjecture due to Armstrong, based on work of
Johnson, related to decompositions for `B_a(m,n)`. It is relevant background
and may be useful to preserve, but it should not be emphasized as a primary
author item in the first public-facing version of `Combinatorics`.

Recommended treatment:

```text
Status: possible related-work or appendix item
Priority: low
```

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

```text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/arxiv_submission.pdf
```

The title in that source is:

```text
Dyck Symmetric Functions and Applications to q,t-Catalan Polynomials
```

The sectioned draft source is also available at:

```text
../Dyck/paper/working_drafts/draft_v3.tex
../Dyck/paper/working_drafts/draft_v3_sections/
```

### 5. Computer-Assisted Material From The 2026 Preprint

Suggested item slug:

```text
items/dyck_symmetric_computer_assisted_proofs_2026/
```

Source locations:

```text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/appendix_a_code.tex
../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_local_proofs.tex
../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_lemma_525.tex
../Dyck/code/codex_project/verify_east7_west7_corrected.py
../Dyck/code/codex_project/verify_reduced_residual_local_lemmas.py
../Dyck/code/codex_project/verify_finite_local_lemmas.py
../Dyck/code/code_assistant/reviews/CA-0026_lemma_5_24_corrected_east7_west7_checker_review.md
```

Description:

This item records the computer-assisted parts of the 2026 preprint
*Dyck Symmetric Functions and Applications to q,t-Catalan Polynomials*.
The most important computational artifacts concern the finite local checks
behind the Section 5 skeleton decomposition, especially the corrected
East7/West7 verification and the reduced residual local lemma checks.

This item should be presented as proof-supporting computation for specific
lemmas and appendices, not as exploratory evidence.

Initial status:

```text
Status: computation
Verification: tied to 2026 preprint; needs independent computational packaging
Python layer: present
LaTeX layer: present in source paper
HTML layer: planned
```

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

```text
items/qt_catalan_middle_coefficients/
```

Source locations:

```text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex
../Dyck/code/codex_project/red_team_flat_middle_coefficients.py
../Dyck/code/code_assistant/codex_tasks/CA-0011_flat_middle_coefficients.md
../Dyck/code/code_assistant/reviews/CA-0011_flat_middle_coefficients_review.md
```

Description:

This item should collect flat-middle-coefficient phenomena for classical and
rational `q,t`-Catalan polynomials.

The 2026 preprint gives the weakest currently proved version: in the classical
case, the result is proved only in the low-deficit range
`\defc <= 2n-8`. There is also a conjectural `r == 1 mod s` version somewhere
in the `Dyck` project, and the general rational `r/s` case remains an open
experimental target.

Initial status:

```text
Status: mixed theorem / conjecture / computation
Verification: needs mathematical review and computational review
Python layer: present for classical checks; rational code may need extension
LaTeX layer: present for classical case in source paper
HTML layer: planned
```

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

```text
items/dyck_symmetric_functions/
```

Source locations:

```text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/03_row_and_tableau_insertion.tex
../Dyck/paper/working_drafts/draft_v3_sections/03_tableau_bijection_schur.tex
../Dyck/paper/working_drafts/draft_v3_sections/04_bijections.tex
../Dyck/paper/working_drafts/draft_v3_sections/04_type4_formula.tex
../Dyck/paper/research_notes/rational_generalizations.tex
../Dyck/code/codex_project/paper_algorithms/
../Dyck/code/codex_project/red_team_rational_dyck_generalization.py
../Dyck/code/codex_project/red_team_rational_qt_catalan_formula.py
```

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

```text
Status: mixed theorem / conjecture
Verification: classical proved by 2026 preprint; r == 1 mod s analogue needs review
Python layer: present
LaTeX layer: present for classical case in source paper
HTML layer: planned
```

Roadmap:

- Curate the classical definitions and theorems from the 2026 preprint.
- Add source references for Schur positivity and affine/dual variants.
- Locate the `r == 1 mod s` analogue and code checks.
- Keep the `r == 1 mod s` analogue visibly separate from the classical
  theorem statements.

### 8. Dyck Skeleton Formula

Suggested item slug:

```text
items/dyck_skeleton_tableau_formulas/
```

Source locations:

```text
../Dyck/paper/working_drafts/arxiv_submission.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_skeletons_setup.tex
../Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex
../Dyck/code/codex_project/red_team_theorem_5_30_formula.py
../Dyck/code/code_assistant/reviews/CA-0015_theorem_5_30_formula_comparison_review.md
../Dyck/memory/proof_audits/theorem_5_30_qt_catalan_skeleton.md
```

Description:

This item presents the Dyck skeleton formula for the high-total-degree /
low-deficit part of the classical `q,t`-Catalan polynomial. It is built from
the Dyck skeleton machinery but requires additional arguments beyond the
definition of Dyck symmetric functions.

The classical formula is proved in the 2026 preprint in the range
`\defc <= 2n-8`. The corresponding `r == 1 mod s` formula should be treated as
conjectural until its exact statement, bound, and evidence are curated.

Initial status:

```text
Status: mixed theorem / conjecture / computation
Verification: classical theorem in 2026 preprint; r == 1 mod s analogue needs review
Python layer: present
LaTeX layer: present for classical case in source paper
HTML layer: planned
```

Roadmap:

- Extract the precise Theorem 5.30 statement from the 2026 preprint.
- Separate the skeleton formula from the underlying Dyck symmetric function
  definitions.
- Add the bounded coefficient comparison code as supporting material.
- Locate and state the `r == 1 mod s` analogue, including the correct bound.
- Explain how this item relates to flat middle coefficients.

### 9. Dyck Skeleton String Decomposition And Rational Cyclic Maps

Suggested item slug:

```text
items/dyck_skeleton_string_decompositions/
```

Source locations:

```text
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
```

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

```text
Status: mixed theorem / conjecture / draft
Verification: classical proved in 2026 preprint; rational material not human verified
Python layer: present
LaTeX layer: present as source paper and research notes
HTML layer: planned
```

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
