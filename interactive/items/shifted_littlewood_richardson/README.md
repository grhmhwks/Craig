# Shifted Littlewood-Richardson

Status summary: Conjectural shifted Littlewood-Richardson rules for skew `GP` and `GQ` functions, with bounded computational checks.

## Summary

This item curates conjectural positive expansion rules for skew shifted stable
Grothendieck functions:

```text
GP_{lambda/mu} = sum_P GP_{wt(P)}
GQ_{lambda/mu} = sum_Q GQ_{wt(Q)}
```

Here `P` runs over shifted set-valued `P`-tableaux of shape `lambda/mu` with
the lattice property.  The `Q` rule uses shifted set-valued `Q`-tableaux with
both the lattice property and the primed-starting property.

The source `GQ` code performs the comparison in the related `GR` model.  The
source README states that the checked `GR` rule implies the same expansion for
`GQ`.

## Provenance

Source repository: `Conjectures-and-Computations`

Source paths:

- `../Conjectures-and-Computations/shifted-LR/skew-GQ-expansion.py`
- `../Conjectures-and-Computations/shifted-LR/skew-GP-expansion.py`
- `../Conjectures-and-Computations/shifted-LR/skew GP_GQ.tex`

Transfer type: curated writeup with adapted combined checker.

## Layers

Python layer: `code/check_shifted_lr.py`

LaTeX layer: `explanation.tex`

HTML layer: `html/body.html`

## Status

- `GP` rule: conjectural.
- `GQ` rule: conjectural; checked through the source `GR` formulation.
- Curated code: bounded direct-vs-rule monomial expansion checks.

## Code

From `Combinatorics/items/shifted_littlewood_richardson`:

```bash
python code/check_shifted_lr.py
```

The default run checks both variants for degree `5`, shape/skew `[3,1]/[1]`,
and `3` variables.  Larger cases can be supplied with:

```bash
python code/check_shifted_lr.py --kind gp --degree 6 --shape 3,1 --skew 1 --num-vars 3
python code/check_shifted_lr.py --kind gq --degree 6 --shape 3,1 --skew 1 --num-vars 3
```

The file `code/shifted_lr_default_summary.txt` records the default summary.
These checks are finite evidence, not proofs.
