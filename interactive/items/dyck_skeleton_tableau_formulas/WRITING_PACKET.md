# Writing Packet: Dyck Skeleton Tableau Formulas

This packet is for an AI writing agent rewriting
`Combinatorics/items/dyck_skeleton_tableau_formulas/explanation.tex`.

The item should explain the two-column skeleton/tableau formula for
`C_n(q,t)` and the checked `r=s*t+1` rational analogue.  Keep it separate from
the later low-deficit special-skeleton string formula.

## Files To Use

Item files:

- `Combinatorics/items/dyck_skeleton_tableau_formulas/README.md`
- `Combinatorics/items/dyck_skeleton_tableau_formulas/item.yaml`
- `Combinatorics/items/dyck_skeleton_tableau_formulas/explanation.tex`
- `Combinatorics/items/dyck_skeleton_tableau_formulas/code/README.md`
- `Combinatorics/items/dyck_skeleton_tableau_formulas/code/check_rational_two_column_formula.py`
- `Combinatorics/items/dyck_skeleton_tableau_formulas/html/body.html`

Source-repository files:

- `Dyck/paper/working_drafts/arxiv_submission.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/04_bijections.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/04_type4_formula.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/03_tableau_bijection_schur.tex`
- `Dyck/paper/research_notes/rational_generalizations.tex`
- `Dyck/code/codex_project/red_team_theorem_5_30_formula.py`

Important source-path caveat: `item.yaml` lists
`red_team_theorem_5_30_formula.py`, which checks the later Section 5
special-skeleton low-deficit formula.  The current item explanation and local
checker are instead about the Section 4 two-column skeleton/tableau formula
and its rational analogue.  The rewrite should not import the Section 5
Theorem 5.30 formula as if it were the main formula here.

## Executive Status

There are three status layers:

1. Classical step `tau = 1`: proved in the 2026 preprint.  This is the
   Section 4 two-column tableau formula for the ordinary `q,t`-Catalan
   polynomial.

2. Degenerate step `tau = 0`: trivial in the normalized rational sequence
   model.  A normalized nonnegative sequence starts at `0` and satisfies
   `D_{i+1} <= D_i`, so only the all-zero sequence occurs.

3. Rational step `tau > 1`, corresponding to `r=s*tau+1`: conjectural.  The
   local checker compares both sides over finite length ranges and records
   passing official checks, but this is not a proof.

The item is about `r=s*tau+1`, not arbitrary rational slopes `r/s`.

## Notation Recommendation

Use `\tau` for the rational step and reserve `t` for the second variable in
`q,t`.

The checker uses option names `--t-values` and `--n-values`.  In the
mathematical writeup:

- checker `t` = step `\tau`;
- checker `n` = sequence length `s`;
- congruence family is `r=s\tau+1`.

A good opening convention is:

```tex
The checker uses \(t\) for the rational step and \(n\) for the length.  In the
mathematical notation below, the step is \(\tau\) and the length is \(s\), so
the rational family is \(r=s\tau+1\).
```

## Direct Rational Dyck Side

For `s >= 1` and `tau >= 0`, a normalized rational Dyck sequence of length
`s` and step `tau` is a sequence

```tex
D=(D_0,\ldots,D_{s-1})
```

of nonnegative integers such that `D_0=0` and

```tex
\[
  D_{i+1}\le D_i+\tau
  \qquad(0\le i<s-1).
\]
```

For a finite integer sequence `x=(x_0,\ldots,x_{\ell-1})`,

```tex
\[
  \dinv_\tau(x)=
  \sum_{0\le i<j<\ell} d_\tau(x_i,x_j),
\]
```

where

```tex
\[
  d_\tau(a,b)=
  \begin{cases}
    \max(0,a+\tau-b),& a\le b,\\
    \max(0,b+1+\tau-a),& a>b.
  \end{cases}
\]
```

The area statistic is

```tex
\[
  \area(x)=\sum_i x_i.
\]
```

The direct rational polynomial in this model is

```tex
\[
  C_{s,\tau}(q,t)
  =
  \sum_D q^{\area(D)}t^{\dinv_\tau(D)},
\]
```

where `D` ranges over all normalized rational Dyck sequences of length `s`.

For `tau=1`, this specializes to the ordinary Dyck-sequence model for
`C_n(q,t)` in the source paper.

## Rational Extractability And Skeletons

The rational analogue uses an extractability condition adapted from the
classical `m`-skeleton definition.

For an entry `D_j=e` in a normalized rational Dyck sequence, call it
extractable if:

- `e > 0`;
- exactly one earlier entry lies in the predecessor window
  `{a >= 0 : max(0,e-\tau) <= a <= e-1}`;
- deleting `D_j` preserves the adjacent rational Dyck inequality.

The explicit deletion condition is:

- if `0 < j < s-1`, require `D_{j+1} <= D_{j-1}+\tau`;
- if `j=s-1`, there is no new adjacent pair to check.

For `tau=0`, the predecessor window is empty, so no positive entry is
extractable under this definition.

A rational `m`-skeleton is a normalized rational Dyck sequence `F` with

```tex
\[
  F_{|F|-1}=\max(F)=m,
\]
```

and with no nonfinal extractable entry.  A final extractable entry is allowed.

This "nonfinal" exemption is important.  It matches the classical Dyck
`m`-skeleton in Section 4.  Do not replace it with the later "full skeleton"
condition from Section 5, where no extractable element is allowed at all.

## Rational Dyck Tableaux

A rational Dyck tableau of step `tau` is a left-aligned tableau whose row
lengths form a partition.  In the current explanation, rows are indexed from
top to bottom.

Conditions:

- rows, read left to right, are dual rational Dyck sequences:

```tex
\[
  P_i[j+1]>P_i[j]+\tau;
\]
```

- columns, read bottom to top, satisfy the affine rational Dyck condition.
  Equivalently, if row `i` is immediately above row `i+1`, then

```tex
\[
  P_i[j]\le P_{i+1}[j]+\tau
\]
```

whenever both entries exist.

The row-reading word in the current explanation is

```tex
\[
  \operatorname{RR}(P)
  =
  P_{\text{bottom}}P_{\text{next}}\cdots P_{\text{top}},
\]
```

with each row read left to right.

For this item, only at-most-two-column tableaux appear.

## Main Formula

The checked rational two-column skeleton/tableau identity is:

```tex
\[
  C_{s,\tau}(q,t)
  =
  \sum_{(F,P)}
  q^{\area(F:\operatorname{RR}(P))}
  t^{\dinv_\tau(F:\operatorname{RR}(P))-|P|}
  s_{\lambda(P)'}(q,t).
\]
```

The sum is over all pairs `(F,P)` such that:

- `F` is a rational `m`-skeleton of step `tau` for some `m >= 0`;
- `P` is an at-most-two-column rational Dyck tableau of step `tau`;
- entries of `P` lie in `[0,m-1]`;
- `|F|+|\operatorname{RR}(P)|=s`.

Here:

- `F:\operatorname{RR}(P)` means concatenation;
- `|P|` is the number of cells of `P`;
- `\lambda(P)` is the shape of `P`;
- `\lambda(P)'` is the conjugate partition;
- `s_{\lambda(P)'}(q,t)` is the Schur function in the two variables `q,t`.

Status:

- proved for `tau=1`;
- trivial/degenerate for `tau=0`;
- conjectural for `tau>1`.

## Classical Proof Source

The classical theorem is in
`Dyck/paper/working_drafts/draft_v3_sections/04_type4_formula.tex`, theorem
`Two-column tableau formula for C_n(q,t)`, label
`thm:section4-qt-catalan-formula`.

The setup and definitions are in
`Dyck/paper/working_drafts/draft_v3_sections/04_bijections.tex`.

Classical source definitions:

- A Dyck sequence is nonempty, starts with `0`, has nonnegative entries, and
  satisfies the affine Dyck inequality.
- In Section 4, `dinv(x)=di(x)+nv(x)`, where `nv` counts equal-value pairs.
- A Dyck `m`-skeleton has maximum and final entry equal to `m`, and has no
  nonfinal extractable element.

The proof decomposes ordinary Dyck sequences by a chain of
area- and dinv-preserving bijections:

1. Family 1: a Dyck sequence `D` with maximum `m`.
2. Type 1 triples `(E,F,G)`: `F` is a Dyck `m`-skeleton, `E` is reverse
   `[1,m]` Dyck, and `G` is affine `[0,m-1]` Dyck.
3. Type 2 triples `(F,G,E^-)`: shift the reverse component down by `1`.
4. Type 3 triples `(F,G,E')`: transport a reverse `[0,m-1]` Dyck sequence to
   an affine `[0,m-1]` Dyck sequence by a multiset- and `di`-preserving normal
   form.
5. Type 4 triples `(F,P,Q)`: use the affine Dyck symmetric function
   Schur-positivity theorem in the two-factor specialization to replace
   `(G,E')` by an at-most-two-column Dyck tableau `P` and a binary reverse
   semistandard recording tableau `Q`.

The Type 3 to Type 4 step is nonconstructive in the paper: it uses equality of
finite coefficients from the affine Dyck symmetric function Schur expansion to
choose a bijection between fibers.  Do not describe it as an explicit new
algorithm unless the rewrite only means the earlier extraction/transport maps.

## Why The Schur Factor Appears

In the Type 4 triples, `Q` is a binary reverse semistandard Young tableau of
the same shape as `P`.  Its entries are `0` and `1`, rows are strictly
increasing left to right, and columns are weakly increasing top to bottom.

The Type 4 statistics are:

```tex
\[
\begin{aligned}
  \area(F,P,Q)&=\area(F)+\sum_{u\in P}u+\sum_{v\in Q}v,\\
  \dinv(F,P,Q)&=\dinv(F:\operatorname{RR}(P))-\sum_{v\in Q}v.
\end{aligned}
\]
```

For fixed `(F,P)`, since `Q` is binary,

```tex
\[
  \sum_{v\in Q}v=\#1(Q),
  \qquad
  \#0(Q)+\#1(Q)=|P|.
\]
```

Thus

```tex
\[
  q^{\#1(Q)}t^{-\#1(Q)}
  =
  t^{-|P|}q^{\#1(Q)}t^{\#0(Q)}.
\]
```

Transposing `Q` changes binary reverse semistandard tableaux of shape
`\lambda(P)` into ordinary semistandard tableaux of conjugate shape
`\lambda(P)'`.  With variables assigned `0 -> t` and `1 -> q`,

```tex
\[
  \sum_Q q^{\#1(Q)}t^{\#0(Q)}
  =
  s_{\lambda(P)'}(t,q)
  =
  s_{\lambda(P)'}(q,t).
\]
```

This is the source of both the `-|P|` shift and the conjugate-shape
two-variable Schur factor.

## Degenerate Step 0

For `tau=0`, the normalized condition is

```tex
D_{i+1}\le D_i.
```

Since `D_0=0` and all entries are nonnegative, the only normalized sequence of
each length is `(0,0,...,0)`.  Therefore the direct side is a single monomial
`q^0 t^0`.

On the formula side, any contributing skeleton must have `m=0`.  A nonempty
tableau would need entries in `[0,m-1]=[0,-1]`, impossible.  Hence only
`F=(0,\ldots,0)` and `P=\varnothing` contributes.  This matches the direct
side.

## Computational Evidence

The rational checker is
`Combinatorics/items/dyck_skeleton_tableau_formulas/code/check_rational_two_column_formula.py`.

Command format:

```text
python check_rational_two_column_formula.py --t-values 2,3,4 --n-values 1,2,3,4
```

Inputs:

- `--t-values`: comma-separated rational step values;
- `--n-values`: comma-separated length values, i.e. the rational `s` values in
  `r=n*t+1`.

The checker skips `t=1`, since that is the proved classical case.

For every requested non-`t=1` pair `(t,n)`, it computes two coefficient
dictionaries grouped by `(area,dinv)`:

- direct side: all normalized rational Dyck paths of length `n`;
- formula side: all pairs `(F,P)` where `F` is a rational `m`-skeleton and
  `P` is an at-most-two-column rational Dyck tableau with entries in
  `[0,m-1]`, expanded by the two-variable Schur factor.

The formula side is implemented by:

- generating skeletons while enumerating normalized rational Dyck paths;
- enumerating at-most-two-column partition shapes;
- enumerating bounded rational Dyck tableaux for each shape and endpoint
  `m`;
- aggregating tableaux by value counts, area, and dinv;
- computing cross-dinv between the skeleton and tableau row-reading word by
  value-count vectors;
- enumerating the two-variable Schur monomial expansion by SSYT enumeration on
  the conjugate shape;
- adding terms
  `(base_area + q_power, base_dinv - |P| + t_power)`.

The check passes exactly when the two dictionaries agree for every requested
case.

Official checks recorded in the item:

```text
python check_rational_two_column_formula.py --t-values 2 --n-values 1,2,3,4,5,6,7,8,9,10,11,12,13,14
python check_rational_two_column_formula.py --t-values 3 --n-values 1,2,3,4,5,6,7,8,9,10,11,12
python check_rational_two_column_formula.py --t-values 4 --n-values 1,2,3,4,5,6,7,8,9,10
```

The explanation records elapsed times:

- `tau=2`, lengths `1 <= s <= 14`, elapsed `4102.814` seconds;
- `tau=3`, lengths `1 <= s <= 12`, elapsed `25254.334` seconds;
- `tau=4`, lengths `1 <= s <= 10`, elapsed `494.131` seconds.

All three official checks passed.  These checks do not prove the formula for
all lengths.

## Neighboring Formula To Avoid Mixing In

The Section 5 formula is a different result.  It uses full/special Dyck
skeletons and a low-deficit/high-total-degree truncation of `C_n(q,t)`.

Source files:

- `Dyck/paper/working_drafts/draft_v3_sections/05_skeletons_setup.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex`
- `Dyck/code/codex_project/red_team_theorem_5_30_formula.py`

Differences:

- Section 4 uses Dyck `m`-skeletons with final extractable entries allowed.
- Section 5 uses full Dyck skeletons, then special Dyck skeletons.
- Section 4 gives a full formula for all of `C_n(q,t)` in the classical case.
- Section 5 gives a formula for a low-deficit/high-total-degree part of
  `C_n(q,t)`.
- Section 4 has a two-column tableau and Schur factor.
- Section 5 has special-skeleton strings and quotient/string contributions.

The current item's `html/body.html` placeholder says it will explain the
relation to low-deficit coefficients.  That is stale or at least incomplete
relative to the current `explanation.tex`.  A rewrite of `explanation.tex`
should follow the two-column tableau formula unless the item is deliberately
retitled or split.

## Suggested Rewrite Shape

Use this order:

1. Status and scope.
   State classical proved, rational `r=s\tau+1` conjectural, arbitrary `r/s`
   not covered, and Section 5 special-skeleton formula not the same item.

2. Direct side.
   Define normalized rational Dyck sequences, area, `\dinv_\tau`, and
   `C_{s,\tau}(q,t)`.

3. Skeleton/tableau objects.
   Define rational extractability, rational `m`-skeletons, rational Dyck
   tableaux, row-reading word, at-most-two-column condition.

4. Formula.
   Display the rational two-column skeleton/tableau identity and explain each
   symbol.

5. Classical proof context.
   Summarize the Section 4 bijection chain and the Type 4 `(F,P,Q)` story.

6. Schur-factor explanation.
   Explain the binary reverse SSYT sum, `-|P|` shift, conjugate shape, and
   two-variable Schur factor.

7. Degenerate `tau=0`.
   Show why both sides reduce to the all-zero contribution.

8. Computational evidence.
   State what the checker compares, official finite boxes, and limitation.

## Statements To Avoid

Do not say:

- "The rational two-column formula is proved for `tau>1`."  It is only checked
  computationally.
- "The code proves the conjecture."  It compares finite coefficient
  dictionaries.
- "This item covers arbitrary rational `r/s`."  It covers `r=s*tau+1`.
- "Dyck `m`-skeleton" and "full/special skeleton" interchangeably.  They are
  different notions.
- "The Type 3 to Type 4 step is an explicit insertion algorithm."  In the
  source, this step chooses a bijection using the affine Dyck symmetric
  function Schur-positivity fiber counts.
- "The Section 5 Theorem 5.30 low-deficit formula is the same as this
  two-column tableau formula."  It is not.

## Useful Commands

Run from `Combinatorics/items/dyck_skeleton_tableau_formulas/code`.

Small check:

```text
python check_rational_two_column_formula.py --t-values 2,3,4 --n-values 1,2,3,4
```

Official checks, potentially expensive:

```text
python check_rational_two_column_formula.py --t-values 2 --n-values 1,2,3,4,5,6,7,8,9,10,11,12,13,14
python check_rational_two_column_formula.py --t-values 3 --n-values 1,2,3,4,5,6,7,8,9,10,11,12
python check_rational_two_column_formula.py --t-values 4 --n-values 1,2,3,4,5,6,7,8,9,10
```

Compile the explanation from the item root:

```text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
```

## Minimum Correct Final Message For The Rewrite

A successful rewritten explanation should leave the reader with this summary:

The ordinary two-column skeleton/tableau formula expresses `C_n(q,t)` as a
sum over Dyck `m`-skeletons and at-most-two-column Dyck tableaux, with a
two-variable Schur factor from binary recording tableaux.  This classical
formula is proved by the Section 4 chain of bijections from Dyck sequences to
Type 4 triples `(F,P,Q)`.  The item records the natural `r=s\tau+1` rational
analogue using rational normalized Dyck sequences, rational `m`-skeletons, and
rational Dyck tableaux.  The rational analogue is trivial at `\tau=0`, proved
at `\tau=1`, and conjectural for `\tau>1`, with finite coefficient checks over
the stated boxes.
