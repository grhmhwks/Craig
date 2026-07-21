# Type C Grothendieck

Status summary: Conjectural type C Grothendieck hierarchy, with basic, strong, and peakset-preserving bounded checks.

## Summary

This item curates the type C Grothendieck conjecture hierarchy from the source
repository.  For a signed permutation `w`, the type C stable Grothendieck
polynomial `GC_w` is defined by signed factorizations of Hecke words.  The
target expansion is a positive expansion in `GQ` functions:

```text
GC_w = sum_{t in T_w} GQ_shape(t),
```

where `T_w` is the set of conjectural type C unimodal Hecke tableaux for `w`.

The source note explains a stronger `GR` formulation for `GC_w^+`, where `GR`
is the shifted set-valued tableau submodel in which the first `i` or `i'` in
the left-to-right, bottom-to-top reading word is constrained.  The computational
checks are organized as three levels:

- basic: compare Hecke words with pairs `(type C unimodal tableau, standard
  shifted set-valued tableau)` of the same shape;
- strong: impose no adjacent equal Hecke letters and no consecutive entries in
  the same shifted set-valued tableau box;
- strongest: compare peaksets, which would imply the `GQ`-positivity statement.

## Provenance

Source repository: `Conjectures-and-Computations`

Source paths:

- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck.py`
- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strong.py`
- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck-strongest.py`
- `../Conjectures-and-Computations/c-grothendieck/c-grothendieck-note.tex`

Transfer type: curated writeup with adapted combined checker.

## Layers

Python layer: `code/check_type_c_grothendieck.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- Basic version: conjectural.
- Strong version: conjectural.
- Peakset-preserving version: conjectural.
- Curated code: bounded enumeration checks for all three levels.

## Code

From `Combinatorics/items/type_c_grothendieck`:

```bash
python code/check_type_c_grothendieck.py
```

The default run checks all three levels with max word length `4` and generator
indices `0..3`.  During curation, all three levels also passed with max word
length `5` and generator indices `0..3`.

The file `code/type_c_grothendieck_default_summary.txt` records the default
summary.  These checks are finite evidence, not proofs.
