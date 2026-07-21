# Code

Executable checks for the Dyck skeleton tableau formula item.

## Rational Two-Column Formula

Command:

```text
python check_rational_two_column_formula.py --t-values 2,3,4 --n-values 1,2,3,4
```

Official checks:

```text
python check_rational_two_column_formula.py --t-values 2 --n-values 1,2,3,4,5,6,7,8,9,10,11,12,13,14
python check_rational_two_column_formula.py --t-values 3 --n-values 1,2,3,4,5,6,7,8,9,10,11,12
python check_rational_two_column_formula.py --t-values 4 --n-values 1,2,3,4,5,6,7,8,9,10
```

Inputs:

- `--t-values`: comma-separated rational step values.
- `--n-values`: comma-separated length values, i.e. the rational `s` values in
  `r = n*t + 1`.

The checker skips `t=1`, since that is the proved classical case.  For every
other requested `(t,n)` pair it computes two coefficient dictionaries grouped
by `(area, dinv)`:

- the direct side, generated from all normalized rational Dyck paths of length
  `n`;
- the formula side, generated from pairs `(F,P)` where `F` is a rational
  Dyck `m`-skeleton and `P` is an at-most-two-column rational Dyck tableau
  with entries in `[0,m-1]`, expanded by the corresponding two-variable Schur
  factor.

The check passes exactly when the two grouped coefficient dictionaries agree
for every requested case.
