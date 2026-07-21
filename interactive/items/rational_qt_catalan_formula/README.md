# Rational qt-Catalan Formula

Status summary: Conjectural formula from the 2024 rational `q,t`-Catalan
paper, with reproducible finite checks for selected coprime parameter pairs.

## Summary

This item curates the rational `q,t`-Catalan conjecture from Graham Hawkes,
*A conjectured formula for the rational q,t-Catalan polynomial*, Annals of
Combinatorics 28, 749-795 (2024).  It packages the source checker for the
monomial-string identity associated to a relatively prime pair `(r,n)`.

## Provenance

Source repository: `Conjectures-and-Computations`

Primary source path:

- `../Conjectures-and-Computations/qt-catalan/qt-conjecture.py`

Related older context:

- `../Conjectures-and-Computations/testing/catest.py`

Transfer type: adapted reproducibility wrapper preserving the source
computation.

## Layers

Python layer: `code/check_rational_qt_catalan_formula.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- Rational `q,t`-Catalan formula: conjectural.
- Default source example `(r,n)=(7,12)`: packaged and passing.
- Additional sample cases `(3,5)` and `(5,8)`: packaged and passing.

## Review Notes

- `qt-conjecture.py` is the source of record for this item.
- The checker rejects non-coprime inputs; the source README notes that the
  conjecture is not expected to hold for non-coprime pairs in general.
- `qt-assisted.py` belongs to the separate computer-assisted proof item for
  Lemma 2 and Lemma 3 of Section 9.
