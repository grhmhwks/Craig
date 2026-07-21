# Writing Packet: qt-Catalan Computer-Assisted Proofs 2024

This packet is for an AI writing agent rewriting
`Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/explanation.tex`.

The goal is to explain the reproducible finite computation used for Lemma 2
and Lemma 3 of Section 9 of Graham Hawkes's 2024 rational `q,t`-Catalan
paper, without confusing it with the separate rational `q,t`-Catalan
conjecture checker.

## Files To Read First

Current item files:

- `Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/README.md`
- `Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/item.yaml`
- `Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/explanation.tex`
- `Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/html/body.html`
- `Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/code/README.md`
- `Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/code/qt_assisted_2024.py`
- `Combinatorics/items/qt_catalan_computer_assisted_proofs_2024/code/qt_assisted_2024_expected_output.txt`

Primary source/provenance file:

- `Conjectures-and-Computations/qt-catalan/qt-assisted.py`

Related older context:

- `Conjectures-and-Computations/testing/catest.py`

Out-of-scope nearby files:

- `Conjectures-and-Computations/qt-catalan/qt-conjecture.py`
- `Conjectures-and-Computations/qt-catalan/johnson.py`
- `Conjectures-and-Computations/qt-catalan/poset_decomps.txt`

The source of record for this item is `qt-assisted.py`.  The file
`qt-conjecture.py` belongs to the separate
`rational_qt_catalan_formula` item.  The Johnson/poset-decomposition files are
not part of this proof-supporting computation.

## Executive Summary

This item packages the computer-assisted verification used in:

```text
Graham Hawkes, "A conjectured formula for the rational q,t-Catalan
polynomial", Annals of Combinatorics 28, 749-795 (2024).
```

The computation is tied specifically to Lemma 2 and Lemma 3 of Section 9.  It
is not a general conjecture-testing script.  The paper reduces the relevant
remaining proof obligations to finite checks; the packaged script reproduces
those checks with stable command-line output.

The curated script is:

```text
code/qt_assisted_2024.py
```

It is a reproducibility wrapper around
`Conjectures-and-Computations/qt-catalan/qt-assisted.py`.  It preserves the
source conventions and default parameters:

```text
max_m = 20
dstar = 20
```

Default status:

```text
generated_records: 5692942
lemma2_status: PASS
lemma2_failures: 0
lemma3_status: PASS
lemma3_layers_checked: 106
lemma3_failures: 0
status: PASS
```

The measured default run time in the current workspace was about 57 seconds.
The exact elapsed time printed by the script is environment-dependent.

## Status Boundaries

Use this status split:

- **Proof-supporting finite computation:** Lemma 2 and Lemma 3 checks from
  Section 9 of the 2024 paper are packaged and passing.
- **Not exploratory evidence:** the script is not meant as a broad search for
  counterexamples.
- **Not the rational formula conjecture checker:** the separate conjectural
  formula and selected `(r,n)` checks belong to the
  `rational_qt_catalan_formula` item.
- **Not an independent paper proof:** the script verifies the finite
  obligations encoded in the source computation; it does not replace the
  surrounding mathematical reduction in the paper.

The strongest safe status sentence is:

> This is reproducible proof-supporting computation for the finite checks that
> complete Lemma 2 and Lemma 3 of Section 9 of the 2024 paper.

## Objects And Conventions

The computation uses position coordinates for `m`-Dyck paths.  A path is a
finite sequence

```tex
A=(a_0,\ldots,a_\ell),\qquad a_0=0,\qquad
0\le a_{i+1}\le a_i+m.
```

For integers `a,b`, the source uses

```tex
\alpha(a,b;m)=
\begin{cases}
  \min(b-a,m), & a\le b,\\
  \min(a-b-1,m), & a>b,
\end{cases}
\qquad
\alpha_0(a;m)=\max(0,a-m).
```

When appending a final entry `j` to a prefix
`x=(a_0,\ldots,a_{r-1})`, the generated degree increment is

```tex
\sum_{k=1}^{r-1}\alpha(a_k,j;m)-\alpha_0(j;m).
```

The finite cutoff is:

```tex
d^*=20.
```

For each `1 <= m <= 20`, the script sets

```tex
\ell^*(m)=\left\lceil\frac{20}{m}+1.001\right\rceil
```

and generates every source-relevant path of length at most
`\ell^*(m)+1` whose generated degree is at most `20`.

The phrase "source-relevant" matters.  Do not describe the script as
generating every possible `m`-Dyck path without the length and degree cutoffs.

## Lemma 2 Check

The Lemma 2 check is a finite string-length bound.  It uses the source
operations:

- `point`;
- `pair`;
- `right`;
- `lowest`.

For a path `A`, let `b = lowest(A)` be the terminal path obtained by repeated
application of the `right` map.

The height statistic in the explanation is:

```tex
h(A)=(g-1)\ell+j-\sum_i a_i,
```

where `g` is the largest entry of `A`, and `j` is the last index at which that
largest entry occurs.

Only the boundary case needs checking: paths of length `\ell^*(m)+1` with
second entry `0`.  For each such path, the script verifies:

```tex
\operatorname{area}(b)\le
m\binom{\ell^*(m)+1}{2}-h(A)-\degr(A).
```

All shorter paths, and length-boundary paths outside this maximal class, are
automatic cases in the same sense as in the source script.

Implementation references:

- `string_okay(record, dstar=20)`
- `check_lemma2(records, dstar=20)`

Successful default summary:

```text
lemma2_status: PASS
lemma2_failures: 0
```

## Lemma 3 Check

The Lemma 3 computation is a finite monomial multiset identity checked
separately for each generated `(m, ell)` layer.

For a fixed layer, put

```tex
M=m\binom{\ell+1}{2}.
```

For every generated path `A`, with area `a` and generated degree `d`, the
left-side/all-path monomial record is:

```tex
(a, M-d).
```

The right side is built from paths whose second entry is `0`.

If

```tex
a\le M-a-d,
```

the path contributes a positive interval:

```tex
(j,M-d),\qquad a\le j\le M-a-d.
```

If

```tex
M-a-d<a,
```

the path contributes a negative correction interval:

```tex
(j,M-d),\qquad M-a-d+1\le j<a.
```

The script checks the exact multiset equality:

```text
positive interval multiset
=
all path monomials + negative correction multiset
```

The comparison uses the source ordering implemented by:

```python
sorted(values, key=lambda item: item[1] + item[0] / 1000)
```

Implementation references:

- `sort_monomials`
- `grouped_by_m_and_length`
- `check_lemma3`

Successful default summary:

```text
lemma3_status: PASS
lemma3_layers_checked: 106
lemma3_failures: 0
lemma3_last_layer: m=1 ell=22 path_count=607712
```

## Default Output

The expected-output file records:

```text
qt-Catalan 2024 computer-assisted checks
  max_m: 20
  dstar: 20
  generated_records: 5692942
  records_by_m: {1: 3893823, 2: 992623, 3: 266022, 4: 204889, 5: 120248, 6: 52429, 7: 14881, 8: 19032, 9: 23326, 10: 27779, 11: 4315, 12: 5079, 13: 5846, 14: 6616, 15: 7389, 16: 8165, 17: 8944, 18: 9726, 19: 10511, 20: 11299}
  lemma2_status: PASS
  lemma2_failures: 0
  lemma3_status: PASS
  lemma3_layers_checked: 106
  lemma3_failures: 0
  lemma3_last_layer: m=1 ell=22 path_count=607712
  status: PASS
```

The script itself also prints an `elapsed_seconds` line.  Do not require the
elapsed value to match a stored transcript exactly.

## Reproducibility Commands

Run from the `Combinatorics` directory:

```text
python items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py
```

Or from the parent repository root:

```text
python Combinatorics\items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py
```

Useful smaller or targeted runs:

```text
python items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py --lemma 2
python items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py --lemma 3
python items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py --max-m 3 --dstar 6
```

CLI options:

- `--max-m`: largest `m` to include; source default is `20`.
- `--dstar`: degree cutoff; source default is `20`.
- `--lemma`: one of `all`, `2`, or `3`.
- `--verbose`: prints per-`m` and per-layer progress.

Compile the explanation from the item directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
```

Regenerate the repository site from `Combinatorics/`:

```text
python build_site.py
```

## Current `explanation.tex` Assessment

The current explanation is already accurate and concise:

- identifies the paper and Section 9 Lemmas 2 and 3;
- identifies `qt-assisted.py` as the source computation;
- defines the position-coordinate path convention;
- explains the degree generation formula;
- separates the Lemma 2 string-bound check from the Lemma 3 monomial multiset
  check;
- reports the default record count, layer count, and pass statuses;
- says the computation is proof-supporting rather than experimental evidence.

Possible rewrite improvements:

1. Add a short "out of scope" note distinguishing this item from the rational
   formula checker based on `qt-conjecture.py`.
2. Make "finite cutoff" and "source-relevant generated records" more explicit
   so readers do not infer an unbounded enumeration.
3. Include the exact expected summary lines or refer clearly to
   `qt_assisted_2024_expected_output.txt`.
4. Say that elapsed time is not mathematically meaningful and may vary by
   machine.
5. If adding implementation detail, keep it tied to Lemma 2 and Lemma 3; do
   not turn the note into a general manual for rational Catalan computations.

## Suggested Rewrite Structure

1. **Purpose.**
   State that the item records the finite computation for Lemma 2 and Lemma 3
   of Section 9 of the 2024 paper.

2. **Source and package.**
   Name `qt-assisted.py` as source of record and
   `code/qt_assisted_2024.py` as the curated reproducibility wrapper.

3. **Generated objects.**
   Define position-coordinate `m`-Dyck paths, `alpha`, `alpha_0`, generated
   degree increments, `dstar=20`, and `ell^*(m)`.

4. **Lemma 2 finite check.**
   Explain the boundary path condition and the inequality checked.

5. **Lemma 3 finite check.**
   Explain the layer-by-layer monomial multiset identity.

6. **Reproducible run.**
   Give the command and expected summary counts/statuses.

7. **Status and limitations.**
   Close by saying this reproduces the finite proof obligations from the
   source computation and is not a general conjecture checker.

## Things Not To Say

Avoid these mistakes:

- Do not say this script proves the full rational `q,t`-Catalan conjecture.
- Do not say this is the `qt-conjecture.py` computation.
- Do not merge this item with the `rational_qt_catalan_formula` item.
- Do not imply the script enumerates all `m`-Dyck paths without the `dstar`
  and `ell^*(m)` cutoffs.
- Do not treat `dstar=20` as an arbitrary local testing choice; it is the
  source cutoff preserved from `qt-assisted.py`.
- Do not report elapsed seconds as an invariant expected-output value.
- Do not describe Lemma 3 as a numeric coefficient comparison only; it is an
  exact sorted multiset comparison of monomial records.
- Do not describe the code as experimental evidence for a new conjecture.

## Minimal Source-Backed Claims

The writing agent may safely state:

- The item curates the computation for Lemma 2 and Lemma 3 of Section 9 of
  the 2024 paper.
- The source script is
  `Conjectures-and-Computations/qt-catalan/qt-assisted.py`.
- The curated script preserves `max_m=20` and `dstar=20` by default.
- The default run generated `5,692,942` records.
- Lemma 2 passed with `0` failures.
- Lemma 3 checked `106` layers and passed with `0` failures.
- The final Lemma 3 layer in source ordering was
  `m=1`, `ell=22`, with `607,712` records.
- The computation is proof-supporting and finite; it is not the separate
  rational formula conjecture checker.

## Minimum Correct Final Message For The Rewrite

If the rewrite is successful, a reader should come away with this summary:

This item makes reproducible the finite computer-assisted checks used for
Lemma 2 and Lemma 3 of Section 9 of Hawkes's 2024 rational `q,t`-Catalan
paper.  The curated script preserves the source `qt-assisted.py` conventions,
including `max_m=20` and `dstar=20`.  It generates the source-relevant
position-coordinate `m`-Dyck path records, verifies the Lemma 2 boundary
string-length inequality, and checks the Lemma 3 monomial multiset identity on
each generated `(m, ell)` layer.  The default run generates 5,692,942 records,
checks 106 Lemma 3 layers, and passes both lemmas.  The computation supports
the finite obligations left by the paper's proof and should not be confused
with the separate conjectural rational formula checker.
