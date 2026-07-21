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
