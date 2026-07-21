# Writing Packet: Rational qt-Catalan Formula

This packet is for an AI writing agent rewriting
`Combinatorics/items/rational_qt_catalan_formula/explanation.tex`.

The goal is to explain the conjectural rational `q,t`-Catalan formula from the
2024 paper and the curated finite checker for selected coprime parameter
pairs, without presenting the conjecture as proved and without confusing this
item with the separate computer-assisted proof item based on `qt-assisted.py`.

## Files To Read First

Current item files:

- `Combinatorics/items/rational_qt_catalan_formula/README.md`
- `Combinatorics/items/rational_qt_catalan_formula/item.yaml`
- `Combinatorics/items/rational_qt_catalan_formula/explanation.tex`
- `Combinatorics/items/rational_qt_catalan_formula/html/body.html`
- `Combinatorics/items/rational_qt_catalan_formula/code/README.md`
- `Combinatorics/items/rational_qt_catalan_formula/code/check_rational_qt_catalan_formula.py`
- `Combinatorics/items/rational_qt_catalan_formula/code/rational_qt_catalan_expected_output.txt`

Primary source/provenance file:

- `Conjectures-and-Computations/qt-catalan/qt-conjecture.py`

Related older context:

- `Conjectures-and-Computations/testing/catest.py`

Out-of-scope nearby files:

- `Conjectures-and-Computations/qt-catalan/qt-assisted.py`
- `Conjectures-and-Computations/qt-catalan/johnson.py`
- `Conjectures-and-Computations/qt-catalan/poset_decomps.txt`

The source of record for this item is `qt-conjecture.py`.  The file
`qt-assisted.py` belongs to the separate
`qt_catalan_computer_assisted_proofs_2024` item for Lemma 2 and Lemma 3 of
Section 9.  The Johnson/poset-decomposition material is not part of this item.

## Executive Summary

This item packages the conjectural rational `q,t`-Catalan formula from:

```text
Graham Hawkes, "A conjectured formula for the rational q,t-Catalan
polynomial", Annals of Combinatorics 28, 749-795 (2024).
```

The curated checker is:

```text
code/check_rational_qt_catalan_formula.py
```

It is a command-line port of
`Conjectures-and-Computations/qt-catalan/qt-conjecture.py`.  It preserves the
source script's step-coordinate generation and monomial-string comparison.

This is a conjectural formula item.  Passing finite checks for selected
coprime pairs is evidence for those cases, not a proof of the formula in
general.

The source/default example is:

```text
(r,n)=(7,12)
```

Default status:

```text
case: r=7 n=12
closest_point: (2, 5)
generated_paths: 2652
all_terms: 2652
plus_terms: 2666
minus_terms: 14
status: PASS
overall_status: PASS
```

Additional sample cases recorded in the expected-output file:

```text
(r,n)=(3,5), (5,8), (7,12)
```

all pass.

## Status Boundaries

Use this status split:

- **Conjecture:** the rational `q,t`-Catalan formula is conjectural.
- **Finite checks:** the curated script checks selected coprime parameter
  pairs by exact multiset comparison.
- **Default source example:** `(r,n)=(7,12)` is packaged and passing.
- **Additional samples:** `(3,5)` and `(5,8)` are packaged in the documented
  multi-case command and pass.
- **Not the proof-supporting Lemma 2/Lemma 3 computation:** that is the
  separate `qt_catalan_computer_assisted_proofs_2024` item based on
  `qt-assisted.py`.

The strongest safe status sentence is:

> The formula is conjectural; this item preserves and makes reproducible the
> source finite checker for selected coprime parameter pairs.

Do not say the finite checker proves the general conjecture.

## Parameters And Step Coordinates

The checker uses the source script's step-coordinate convention.  For a
coprime pair `(r,n)`, set:

```tex
\ell=r-1.
```

A generated path is:

```tex
x=(x_0,\ldots,x_{\ell-1})
```

constructed from left to right subject to:

```tex
\sum_{a=0}^{i}x_a
\le
\left\lfloor\frac{(i+1)n}{\ell+1}\right\rfloor
\qquad(0\le i<\ell).
```

The script rejects non-coprime inputs.  The source README says the conjecture
is not expected to hold for non-coprime parameters in general.

## Degree Statistic

The source statistic is generated incrementally using `beta` and `gamma`.

For:

```tex
\beta(i,j;x)=\sum_{a=i}^{j}x_a-\frac{n(j-i+1)}{\ell+1},
```

define:

```tex
\gamma(i,j;x)=
\begin{cases}
  \min(x_{i-1},\lfloor-\beta(i,j;x)\rfloor), & \beta(i,j;x)<0,\\
  \min(x_i,\lfloor\beta(i,j;x)\rfloor), & \beta(i,j;x)>0,\\
  0, & \beta(i,j;x)=0.
\end{cases}
```

When a final entry is appended, the degree increases by the relevant
`\gamma(k,j;x)` terms with the new endpoint `j`.

Implementation references:

- `beta`
- `gamma`
- `generate_paths`

## Area Statistic

The maximum area parameter is:

```tex
M=\sum_{i=0}^{\ell-1}
\left\lfloor\frac{(i+1)n}{\ell+1}\right\rfloor.
```

For a generated path `x`, the script uses:

```tex
\operatorname{area}(x)
=
M-\sum_{p=0}^{\ell-1}\sum_{a=0}^{p}x_a.
```

Implementation references:

- `max_area`
- `path_area`

## Closest Point And Distinguished Subfamily

The source formula uses the unique closest point to the diagonal.  The checker
finds an index `q` such that:

```tex
(q+1)n\equiv 1 \pmod{\ell+1},
```

and records:

```tex
\left(q,\left\lfloor\frac{(q+1)n}{\ell+1}\right\rfloor\right).
```

The distinguished subfamily `T` consists of generated paths satisfying:

```tex
\sum_{a=0}^{q}x_a
=
\left\lfloor\frac{(q+1)n}{\ell+1}\right\rfloor.
```

Implementation reference:

- `closest_point`

For the default `(r,n)=(7,12)`, the closest point is:

```text
(2, 5)
```

## Monomial-String Identity

Every generated path contributes one all-path monomial record:

```tex
(\operatorname{area}(x),\,M-d(x)),
```

where `d(x)` is the generated degree statistic.

Each path in the distinguished subfamily contributes a monomial string to the
right-side formula.  If:

```tex
a=\operatorname{area}(x),\qquad d=d(x),
```

then the positive interval is:

```tex
(j,M-d),\qquad a\le j\le M-a-d,
```

when `a <= M-a-d`.

If `M-a-d < a`, the script records the negative correction interval:

```tex
(j,M-d),\qquad M-a-d+1\le j<a.
```

The finite check is the exact multiset identity:

```text
positive interval multiset
=
all generated path monomials + negative correction multiset
```

Implementation references:

- `monomial_counts`
- `check_conjecture`

If a case fails and `--show-difference` is supplied, the script reports the
first mismatched monomial under the source ordering:

```python
key=lambda item: item[1] + item[0] / 1000
```

## Reproducibility Commands

Run the source/default example from the `Combinatorics` directory:

```text
python items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py
```

Or from the parent repository root:

```text
python Combinatorics\items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py
```

Run the documented multi-case sample:

```text
python items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py --case 3/5 --case 5/8 --case 7/12
```

Useful failure-diagnostic option:

```text
python items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py --case R/N --show-difference
```

Compile the explanation from the item directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
```

Regenerate the repository site from `Combinatorics/`:

```text
python build_site.py
```

## Expected Output

Default expected output:

```text
rational q,t-Catalan formula finite check
  case: r=7 n=12
    ell: 6
    closest_point: (2, 5)
    max_area: 33
    generated_paths: 2652
    all_terms: 2652
    plus_terms: 2666
    minus_terms: 14
    status: PASS
overall_status: PASS
```

Sample multi-case output:

```text
case: r=3 n=5
  ell: 2
  closest_point: (1, 3)
  max_area: 4
  generated_paths: 7
  all_terms: 7
  plus_terms: 7
  minus_terms: 0
  status: PASS

case: r=5 n=8
  ell: 4
  closest_point: (1, 3)
  max_area: 14
  generated_paths: 99
  all_terms: 99
  plus_terms: 99
  minus_terms: 0
  status: PASS

case: r=7 n=12
  ell: 6
  closest_point: (2, 5)
  max_area: 33
  generated_paths: 2652
  all_terms: 2652
  plus_terms: 2666
  minus_terms: 14
  status: PASS
overall_status: PASS
```

## Current `explanation.tex` Assessment

The current explanation is already accurate and concise:

- identifies the paper and source script;
- states the conjectural status;
- defines the step-coordinate path generation;
- records the `beta`/`gamma` degree statistic;
- defines the area convention;
- explains the closest point and distinguished subfamily;
- describes the positive interval and negative correction interval;
- reports the default `(7,12)` run;
- separates this item from the Lemma 2/Lemma 3 proof-supporting computation.

Possible rewrite improvements:

1. Make the theorem/conjecture boundary visually explicit near the start.
2. Use "finite checker" or "finite evidence" rather than "proof".
3. Add a short warning that non-coprime inputs are rejected because the source
   conjecture is not expected to hold there.
4. Keep the monomial identity as a multiset identity, not only a count
   identity.
5. Add a short source/provenance paragraph if needed, but do not overload the
   public item with internal transfer details.

## Suggested Rewrite Structure

1. **Purpose and status.**
   State that the rational formula is conjectural and this item packages the
   source finite checker.

2. **Source and package.**
   Name `qt-conjecture.py` as source of record and
   `check_rational_qt_catalan_formula.py` as the curated port.

3. **Step-coordinate paths.**
   Define `ell=r-1`, the generated path, and the rational Dyck bound.

4. **Statistics.**
   Define `beta`, `gamma`, generated degree, `M`, and area.

5. **Formula check.**
   Define the closest point, distinguished subfamily, all-path monomials,
   positive intervals, negative correction intervals, and the multiset
   comparison.

6. **Reproducibility.**
   Give the default command, expected `(7,12)` output, and multi-case command.

7. **Limitations.**
   Close by saying the checks are finite evidence for selected coprime pairs
   and do not prove the general conjecture.

## Things Not To Say

Avoid these mistakes:

- Do not say the rational `q,t`-Catalan formula is proved.
- Do not say the code proves the conjecture in general.
- Do not say this item is based on `qt-assisted.py`.
- Do not merge this item with `qt_catalan_computer_assisted_proofs_2024`.
- Do not present non-coprime cases as supported by the source conjecture.
- Do not describe the checker as comparing only total counts; it compares
  exact monomial multisets.
- Do not omit the negative correction interval for cases like `(7,12)`, where
  `minus_terms=14`.
- Do not change the parameter notation silently.  The script uses `(r,n)` and
  `ell=r-1`; other rational Dyck literature may use `(r,s)`.

## Minimal Source-Backed Claims

The writing agent may safely state:

- The item curates the conjectural rational `q,t`-Catalan formula from the
  2024 paper.
- The source script is
  `Conjectures-and-Computations/qt-catalan/qt-conjecture.py`.
- The curated checker preserves the source step-coordinate path generation and
  monomial-string comparison.
- The checker requires `gcd(r,n)=1` and rejects non-coprime inputs.
- The default case `(r,n)=(7,12)` has `ell=6`, closest point `(2,5)`, maximum
  area `33`, and `2652` generated paths.
- In the default case, `plus_terms=2666`, `all_terms=2652`,
  `minus_terms=14`, and the status is `PASS`.
- The multi-case sample `(3,5)`, `(5,8)`, `(7,12)` passes.
- The computation is finite evidence for selected cases, not a proof of the
  conjecture.

## Minimum Correct Final Message For The Rewrite

If the rewrite is successful, a reader should come away with this summary:

This item records the conjectural rational `q,t`-Catalan formula and preserves
the source finite checker from `qt-conjecture.py`.  For a coprime pair `(r,n)`,
the checker generates step-coordinate rational Dyck paths, computes the source
degree and area statistics, selects the distinguished subfamily determined by
the closest point to the diagonal, and checks an exact monomial-string multiset
identity.  The default source example `(7,12)` generates 2,652 paths and
passes with 2,666 positive terms, 2,652 all-path terms, and 14 negative
correction terms.  These are finite checks of selected coprime cases; the
general formula remains conjectural.
