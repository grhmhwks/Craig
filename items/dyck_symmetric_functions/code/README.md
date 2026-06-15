# Code

Purpose: reproduce the executable parts curated for the Dyck symmetric
functions item.

## Classical Insertion Algorithm

Command:

```text
python classical_insertion_demo.py
```

This script traces the classical row insertion operation and a tableau
insertion example.  The implementation lives in:

- `paper_algorithms/row_insertion.py`
- `paper_algorithms/tableau_insertion.py`

These files are adapted from the 2026 preprint code.  They implement the
insertion algorithm used to prove Schur positivity for the classical dual Dyck
symmetric functions.

## Rational Dual Finite Checks

Command:

```text
python check_rational_dyck_generalization.py --t 2 --alphabet-size 4 --max-length 4
```

Official repository checks:

```text
python check_rational_dyck_generalization.py --t 2 -A 10 -L 10
python check_rational_dyck_generalization.py --t 3 -A 13 -L 9
python check_rational_dyck_generalization.py --t 4 -A 16 -L 8
```

Dependencies: Python standard library only for the portable fallback.  If
`numpy` and `numba` are installed, the checker automatically uses a compiled
word-grouping backend.  Compiled word scans with at least 50 million generated
words are split across worker processes automatically; use `--workers 1` to
force serial execution, a positive `--workers N` to force `N` workers, or
`DYCK_CHECK_WORKERS=N` to set the default from the environment.

Inputs are explicit and minimal:

- `--t`: rational step.
- `--alphabet-size` or `-A`: alphabet size, using `{1,2,...,A}`.
- `--max-length` or `-L`: checks every length `1 <= l <= L`.

For each length the checker:

- constructs every word over `{1,2,...,A}` that contains `1`;
- groups words by underlying multiset and rational dinv;
- generates every positive composition of the length and groups compositions
  by their sorted underlying partition;
- verifies that, for each multiset, dinv, and partition, every distinct
  composition in that partition gives the same number of valid dual Dyck
  factorizations;
- compares that common factorization count with the Dyck-tableau prediction
  obtained by summing, over rational Dyck tableaux with that multiset and
  dinv, the number of SSYT of the tableau shape with the given dominant
  content.

The implementation keeps the useful cut-mask optimization from the older
checker: a word contributes a bitmask of adjacent positions that must be cut
for a dual factorization, and a positive composition is valid exactly when its
cut mask contains that required mask.  With NumPy and Numba available, word
grouping is performed by a compiled exhaustive scan that aggregates compact
integer records for `(multiset, dinv, cut mask)` and then feeds the same Python
verification pipeline.  For sufficiently large word universes, that compiled
scan is partitioned across worker processes and the compact aggregate records
are merged before verification.  Without those optional dependencies, word grouping
falls back to the pure-Python first-`1` generator, which counts words with no
`1` in the reported universe size but never traverses them.  Tableau grouping
uses the same first-`1` idea, fixing the first tableau cell containing `1` and
avoiding terminal rejection of tableaux with no `1`.  Internally, multiset keys
are compact integer encodings during each fixed-length pass, Dyck-tableau
predictions are cached by shape-count profile, and factorization counts use
cached cut-mask subset sums.  The code no longer has a variable-count
parameter, affine/dual/both option, or compressed/full comparison modes.

Interpretation: these are bounded computational checks of the conjectural
`r = s*t + 1` analogue.  They are not a proof of the general conjecture.

## Random Class Checks

Command:

```text
python random_rational_dyck_checks.py --t 2 -A 10 -L 10 --iterations 100 --seed 1
```

This Monte Carlo checker samples words uniformly from `{1,2,...,A}^L`.  Each
sampled word determines a multiset and rational dinv value.  The script then
forgets the sampled order and exhaustively checks the full class with that
multiset and dinv:

- all words with the sampled multiset and dinv are enumerated;
- factorization counts are checked for symmetry across compositions with the
  same underlying partition;
- the common counts are compared with the corresponding Dyck-tableau
  prediction.

Unlike the exhaustive checker, this script does not restrict to words
containing `1`; the sampled word may use any letters in the alphabet.
When NumPy and Numba are installed, the fixed-multiset word-class enumeration
is JIT-compiled automatically; the pure-Python implementation remains as a
portable fallback.

Stopping controls:

- `--iterations N`: maximum sampled classes to check.
- `--timeout-seconds S`: optional wall-clock timeout.
- `--seed N`: optional reproducible random seed.
- `--workers N`: parallel worker processes for fixed-iteration runs.  Timeout
  driven runs currently execute serially.
