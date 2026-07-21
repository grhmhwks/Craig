# Writing Packet: Dyck Symmetric Computer-Assisted Proofs 2026

This packet is for an AI writing agent rewriting
`Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/explanation.tex`.

The goal is to explain the appendix computations from the 2026 Dyck symmetric
functions preprint as proof-supporting finite verifications, not as exploratory
experiments and not as standalone proofs of the surrounding symbolic
reductions.

## Files To Read First

Current item files:

- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/README.md`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/item.yaml`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/explanation.tex`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/COMPLETION_REVIEW.md`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/html/body.html`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/README.md`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/run_appendix_listing.py`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/01_core_dyck_sequence_routines.py`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_a/02_make_strings.py`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/01_residual_finite_check.py`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/02_residual_successful_output.txt`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/03_east7_west7_seven_window_checker.py`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/04_east7_west7_successful_output.txt`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/05_lemma_525_limited_nonzero_checker.py`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/06_lemma_525_limited_nonzero_successful_output.txt`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/07_lemma_525_prefix_checker.py`
- `Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code/appendix_b/08_lemma_525_prefix_successful_output.txt`

Primary source/provenance files from the source repository:

- `Dyck/paper/working_drafts/arxiv_submission.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/appendix_a_code.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/appendix_b_local_proofs.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/appendix_b_lemma_525.tex`

The local item files are curated appendix listings and explanatory wrappers.
The source files above are the provenance for the copied appendix code and the
surrounding proof statements.

## Executive Summary

This item packages the finite computations used in the appendices of Graham
Hawkes, "Dyck Symmetric Functions and Applications to q,t-Catalan Polynomials",
arXiv:2605.13003, posted May 13, 2026.

The computations support the proof of a string decomposition for Dyck
sequences in the low-deficit range. The paper defines local maps called
`\mathrm{up}` and `\mathrm{down}`. These maps change area by one while
preserving deficit, and they are built from local extraction, insertion, and
East/West window moves.

The symbolic proof reduces several local well-definedness obligations to
finite domains. Appendix B checkers exhaust those domains. Appendix A provides
the core Dyck-sequence routines and the lower-half string-generation listing.

The most important status sentence is:

> These computations are finite exhaustive proof obligations inside the
> appendix argument; they are not broad experimental evidence and they do not
> independently reprove the symbolic reductions in the paper.

## Status Boundaries

Use this status split:

- **Paper theorem context:** the surrounding string-decomposition theorem is a
  mathematical theorem in the 2026 preprint.
- **Appendix A:** code listings implementing the Dyck-sequence routines,
  skeleton tests, extraction/insertion routines, local `up` and `down` maps,
  and lower-half string generation.
- **Appendix B:** finite exhaustive checkers for bounded domains left by the
  symbolic proof.
- **Local package status:** the repository packages copied appendix listings
  and successful-output transcripts and provides a wrapper for reproducible
  local runs.

Do not present Appendix B as a general search for counterexamples. Each
checker has a bounded input domain dictated by the proof.

## Mathematical Setting

The item concerns Dyck area sequences and the statistics used in the
q,t-Catalan part of the Dyck symmetric functions preprint.

The relevant theorem range is the low-deficit range

```tex
0 \le d \le 2n-8.
```

The local maps move within a fixed deficit class and change area by one:

- `up` raises area by one;
- `down` lowers area by one.

The maps are assembled by:

- detecting special skeleton cases;
- extracting one or more entries;
- applying short East or West local moves;
- reinserting shifted entries.

The proof has symbolic parts for the infinite families and finite appendix
checks for remaining bounded cases.

## Appendix A

Appendix A is represented locally by:

- `code/appendix_a/01_core_dyck_sequence_routines.py`
- `code/appendix_a/02_make_strings.py`

The core routines include definitions and algorithms for:

- Dyck sequence validation;
- area and deficit statistics;
- full and special skeleton tests;
- extraction and insertion;
- East and West local moves;
- `up` and `down` maps.

The string-generation listing starts from special skeletons and repeatedly
applies `up` to build the lower half of each string.

The wrapper

```text
code/run_appendix_listing.py
```

loads the Appendix A files into a shared namespace before running a requested
listing. This preserves the appendix-listing style without editing the copied
files.

Command from the item `code/` directory:

```text
python run_appendix_listing.py appendix_a/02_make_strings.py
```

This listing is mainly included as appendix code. It does not produce the same
kind of terminal success transcript as the Appendix B checkers.

## Appendix B Lemmas

In the current `explanation.tex`, Appendix B is organized around Lemmas
5.22--5.25 from the arXiv version:

- Lemma 5.22: skeleton cases succeed.
- Lemma 5.23: extraction chains never fail.
- Lemma 5.24: the seven-window branches do not fail.
- Lemma 5.25: bounded extraction positions and injection nonfailure.

The rewrite may preserve this table-like organization. It is useful because it
connects each script to a specific proof obligation.

## Appendix B Checker 1: Residual Small Range

Files:

- `code/appendix_b/01_residual_finite_check.py`
- `code/appendix_b/02_residual_successful_output.txt`

Command:

```text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
```

What it checks:

- enumerates the remaining small lengths `4 <= n <= 7`;
- follows the `up` and `down` decision branches;
- confirms that each input falls into an already covered case;
- checks skeleton, extraction, and position-bound obligations in the residual
  range;
- confirms that no East7 or West7 branch is reached for `4 <= n <= 7`.

Successful transcript highlights:

```text
EverythingOkay = True
up counts   {'up skeleton': 42, 'up East3': 152,
             'up special': 2, 'up East5 case 2b': 4}
down counts {'down skeleton': 42, 'down West3': 152,
             'down special': 2, 'down West5 case 2b': 4}
No East7 or West7 branch was reached for 4 <= n <= 7.
```

Interpretation:

- This is the residual finite-domain check for the small range.
- It supports the small-range portions of Lemmas 5.22, 5.23, 5.24, and 5.25.

## Appendix B Checker 2: Seven-Entry East/West Windows

Files:

- `code/appendix_b/03_east7_west7_seven_window_checker.py`
- `code/appendix_b/04_east7_west7_successful_output.txt`

Command:

```text
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
```

What it checks:

- enumerates the finite East7 and West7 seven-entry window domains;
- includes the bounded absolute children left after threshold reductions;
- compares threshold tables against expected values;
- verifies structural constraints, finite counts, and absence of problems in
  the four Case/Side combinations.

Successful transcript highlights:

```text
|EW| = 7194, |WW| = 7194, |EW union WW| = 14388
Case 1 threshold table comparison: MATCH
Case 2 threshold table comparison: MATCH
id_mid>=10 check: PASS
SUCCESS: East7/West7 seven-window verification passed.
```

Expected finite counts:

```text
Case 1 East: children=2473, triples=9919
Case 1 West: children=2911, triples=10311
Case 2 East: children=3860, triples=715
Case 2 West: children=4827, triples=1756
```

Interpretation:

- This is the finite checker for Lemma 5.24 in the `n >= 8` part of the
  proof.
- It should be described as a finite window verification, not as a full
  enumeration of all Dyck sequences.

## Appendix B Checker 3: Lemma 5.25 Limited-Nonzero Domain

Files:

- `code/appendix_b/05_lemma_525_limited_nonzero_checker.py`
- `code/appendix_b/06_lemma_525_limited_nonzero_successful_output.txt`

Command:

```text
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
```

What it checks:

- checks all Dyck sequences with `4 <= n <= 13`;
- restricts to at most seven nonzero entries;
- applies the fixed deficit and area hypotheses used in the proof;
- verifies the required image, deficit, area-change, and position-bound
  conditions for eligible `up` and `down` calls.

Successful transcript highlights:

```text
generated by n: {4: 14, 5: 42, 6: 132, 7: 429, 8: 1430,
                 9: 3432, 10: 7072, 11: 13260,
                 12: 23256, 13: 38760}
eligible up calls: 11879
eligible down calls: 9486
position-bound or image failures: 0
status: PASS
```

Interpretation:

- This is one of the finite domains used for Lemma 5.25.
- It checks bounded extraction positions and nonfailure after the symbolic
  proof reduces to the limited-nonzero case.

## Appendix B Checker 4: Lemma 5.25 Prefix Forms

Files:

- `code/appendix_b/07_lemma_525_prefix_checker.py`
- `code/appendix_b/08_lemma_525_prefix_successful_output.txt`

Command:

```text
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
```

What it checks:

- checks the two excluded prefix forms left by the proof of Lemma 5.25;
- runs over `9 <= n <= 16`;
- covers two claims and two subcases, labeled in the code as
  `pq_lt_4` and `pq_eq_4`;
- verifies that every enumerated word gives either the required deficit
  contradiction or the required area contradiction.

Successful transcript highlights:

```text
failures: 0
status: PASS
```

Interpretation:

- This is the second finite domain for Lemma 5.25.
- It should not be merged conceptually with the limited-nonzero checker; they
  cover different leftover cases.

## Reproducibility Commands

Run from:

```text
Combinatorics/items/dyck_symmetric_computer_assisted_proofs_2026/code
```

Appendix B commands:

```text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
```

The checkers require only Python 3 and the standard library. Run with ordinary
assertions enabled. Do not use optimized mode such as:

```text
python -O ...
```

because `assert` statements are part of the verification in the appendix code.

Compile the explanation from the item directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
```

Regenerate the repository site from `Combinatorics/`:

```text
python build_site.py
```

The completion review says the four Appendix B commands and `python
build_site.py` were run successfully on June 13, 2026.

## Current `explanation.tex` Assessment

The current explanation is already in a good public-facing shape:

- it explains what the appendix code supports;
- it separates Appendix A from Appendix B;
- it connects Appendix B scripts to Lemmas 5.22--5.25;
- it describes the residual, seven-window, and Lemma 5.25 finite checks;
- it states that the computations are part of the proof after finite
  reduction, not just evidence.

Possible rewrite improvements:

1. Add a short status paragraph near the start saying exactly what is proved
   symbolically and what is checked computationally.
2. Make the dependency on ordinary Python assertions visible in the
   reproducibility section.
3. Include the exact success lines from the transcripts so readers know what
   a passing run looks like.
4. Clarify that Appendix A is mostly construction/listing code, while Appendix
   B contains the proof-critical finite exhaustive checkers.
5. Mention that the local package mirrors arXiv appendix listings and should
   be compared again if the preprint changes.

## Suggested Rewrite Structure

1. **Status and role of the computations.**
   State that the paper supplies symbolic reductions and the appendices supply
   finite exhaustive checks for bounded cases.

2. **Dyck sequence construction layer.**
   Briefly describe area, deficit, skeletons, extraction/insertion, and local
   `up`/`down` maps without reproducing the full algorithms.

3. **Appendix A.**
   Explain the core routines and lower-half string-generation listing.

4. **Appendix B overview.**
   State Lemmas 5.22--5.25 and their proof obligations.

5. **Finite checkers.**
   Give one compact subsection per checker:
   residual small range, seven-entry windows, limited-nonzero Lemma 5.25
   domain, prefix-form Lemma 5.25 domain.

6. **Reproducibility.**
   List exact commands, dependencies, and expected success lines.

7. **Limitations.**
   Say the scripts verify the encoded finite obligations and do not replace
   the surrounding symbolic proof or cover statements outside the stated
   bounded domains.

## Things Not To Say

Avoid these mistakes:

- Do not say the appendix code proves the whole theorem by itself.
- Do not say the computations are merely experimental evidence.
- Do not imply the checkers cover arbitrary `n`; they cover the finite domains
  stated in the appendices.
- Do not describe the East7/West7 checker as enumerating all Dyck sequences.
  It enumerates local seven-entry window domains and bounded children.
- Do not merge the two Lemma 5.25 checks into one domain; one is the
  limited-nonzero domain and the other is the prefix-form domain.
- Do not claim Appendix A has the same success-transcript role as Appendix B.
  Appendix A contains construction/listing code.
- Do not omit the warning about Python optimized mode disabling assertions.
- Do not update the successful-output transcripts unless the corresponding
  appendix listing or expected output has intentionally changed.

## Minimal Source-Backed Claims

The writing agent may safely state:

- The item curates appendix computations from arXiv:2605.13003.
- Appendix A contains core Dyck-sequence routines and lower-half string
  generation code.
- Appendix B contains finite exhaustive checkers for local well-definedness
  obligations in the skeleton string construction.
- The residual checker covers `4 <= n <= 7` and reports
  `EverythingOkay = True`.
- The seven-window checker covers East7/West7 local windows, compares expected
  threshold tables and finite counts, and reports
  `SUCCESS: East7/West7 seven-window verification passed.`
- The limited-nonzero Lemma 5.25 checker covers `4 <= n <= 13` with at most
  seven nonzero entries and reports `status: PASS`.
- The prefix-form Lemma 5.25 checker covers `9 <= n <= 16` and reports
  `status: PASS`.
- The scripts use only the Python standard library and require assertions to
  remain enabled.

## Minimum Correct Final Message For The Rewrite

If the rewrite is successful, a reader should come away with this summary:

The 2026 Dyck symmetric functions preprint proves a skeleton string
decomposition using local `up` and `down` maps on Dyck sequences. Most of the
argument is symbolic. The appendix code records the finite exhaustive checks
needed after the proof reduces certain local well-definedness questions to
bounded cases. Appendix A gives the construction routines and string
generation listing. Appendix B supplies four reproducible checkers: the
residual small range, the East7/West7 seven-window verification, and two
finite domains used in Lemma 5.25. Passing these scripts reproduces the
appendix's finite proof obligations, but does not replace the surrounding
symbolic reductions or assert anything outside the stated finite domains.
