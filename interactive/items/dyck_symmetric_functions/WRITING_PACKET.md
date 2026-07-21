# Writing Packet: Dyck Symmetric Functions

This packet is for an AI writing agent rewriting
`Combinatorics/items/dyck_symmetric_functions/explanation.tex`.

The main job is to make the exposition self-contained while keeping the
theorem/conjecture boundary exact.  The classical Dyck symmetric functions are
proved.  The `r = s*t + 1` rational analogue is conjectural for step `t > 1`,
with bounded computational evidence.

## Files To Use

Item files:

- `Combinatorics/items/dyck_symmetric_functions/README.md`
- `Combinatorics/items/dyck_symmetric_functions/item.yaml`
- `Combinatorics/items/dyck_symmetric_functions/explanation.tex`
- `Combinatorics/items/dyck_symmetric_functions/code/README.md`
- `Combinatorics/items/dyck_symmetric_functions/code/classical_insertion_demo.py`
- `Combinatorics/items/dyck_symmetric_functions/code/check_rational_dyck_generalization.py`
- `Combinatorics/items/dyck_symmetric_functions/code/random_rational_dyck_checks.py`
- `Combinatorics/items/dyck_symmetric_functions/code/paper_algorithms/row_insertion.py`
- `Combinatorics/items/dyck_symmetric_functions/code/paper_algorithms/tableau_insertion.py`
- `Combinatorics/items/dyck_symmetric_functions/code/paper_algorithms/rational_dyck.py`
- `Combinatorics/items/dyck_symmetric_functions/code/paper_algorithms/ssyt.py`
- `Combinatorics/items/dyck_symmetric_functions/html/body.html`

Source-repository files:

- `Dyck/paper/working_drafts/arxiv_submission.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/03_row_and_tableau_insertion.tex`
- `Dyck/paper/working_drafts/draft_v3_sections/03_tableau_bijection_schur.tex`
- `Dyck/paper/research_notes/rational_generalizations.tex`
- `Dyck/code/codex_project/paper_algorithms/row_insertion.py`
- `Dyck/code/codex_project/paper_algorithms/tableau_insertion.py`
- `Dyck/code/codex_project/paper_algorithms/rational_dyck.py`
- `Dyck/code/codex_project/red_team_rational_dyck_generalization.py`

The local item files are curated copies or concise writeups.  The source files
above are the authoritative provenance for the theorem and conjectural rational
extension.

## Executive Status

There are three regimes, and the rewrite should separate them.

1. Step `t = 0`: degenerate RSK/dual-RSK baseline.  In this limit the local
   dinv contribution is zero, dual factors become strictly increasing words,
   and affine factors become weakly increasing words.

2. Step `t = 1`: classical Dyck symmetric functions.  This is theorem-level
   material from the 2026 preprint *Dyck Symmetric Functions and Applications
   to q,t-Catalan Polynomials*.  The dual formula is proved by an explicit
   tableau insertion bijection.  The affine/nondual formula follows from the
   dual formula using the standard involution on symmetric functions.

3. Step `t > 1`, corresponding to `r = s*t + 1`: conjectural rational
   analogue.  The formula is supported by systematic finite checks, but there
   is no proof in the repository.

General rational `r/s` Dyck symmetric functions are not part of this item.
Only the `r = s*t + 1` family is included.

## Notation Recommendation

The current `explanation.tex` uses `t` for the rational step.  The source note
`rational_generalizations.tex` uses `\tau`.  A rewrite may keep `t`, but using
`\tau` is cleaner because the item is adjacent to q,t-Catalan material.

If switching notation, say:

```tex
Fix a nonnegative integer step parameter \(\tau\).  The rational case under
discussion corresponds to \(r=s\tau+1\).
```

Then use `\dinv_\tau`, `\DS^{(\tau)}`, and `{\DSstar}^{(\tau)}`.  Do not let
the step parameter be confused with the second variable in a q,t-Catalan
polynomial.

## Core Definitions

Let `x=(x_0,...,x_{\ell-1})` be a finite integer sequence.  For a nonnegative
integer step parameter `tau`, define

```tex
\[
  \dinv_\tau(x)
  =
  \sum_{0\le i<j<\ell} d_\tau(x_i,x_j),
\]
where
\[
  d_\tau(a,b)=
  \begin{cases}
    \max(0,a+\tau-b),& a\le b,\\
    \max(0,b+1+\tau-a),& a>b.
  \end{cases}
\]
```

This specializes to the classical Dyck statistic at `tau = 1`.

An affine rational Dyck sequence of step `tau` is a finite integer sequence
satisfying

```tex
\[
  x_{i+1}\le x_i+\tau
  \qquad\text{for all }i.
\]
```

A dual rational Dyck sequence of step `tau` is a finite integer sequence
satisfying

```tex
\[
  x_{i+1}>x_i+\tau
  \qquad\text{for all }i.
\]
```

For `tau = 1`, the dual condition is `x_{i+1} >= x_i + 2`.

A factorization of a finite multiset `S` is a sequence of finite words
`F_0,F_1,...` whose concatenation is a rearrangement of `S`.  It is affine,
respectively dual, if every factor is an affine, respectively dual, rational
Dyck sequence of the chosen step.

The rational Dyck symmetric functions are

```tex
\[
  \DS^{(\tau)}(S,d;\mathbf x)
  =
  \sum_{\substack{\mathcal F\text{ affine rational Dyck factorization of }S\\
                  \dinv_\tau(F_0F_1F_2\cdots)=d}}
  x^{\mathcal F}
\]
```

and

```tex
\[
  {\DSstar}^{(\tau)}(S,d;\mathbf x)
  =
  \sum_{\substack{\mathcal F\text{ dual rational Dyck factorization of }S\\
                  \dinv_\tau(F_0F_1F_2\cdots)=d}}
  x^{\mathcal F}.
\]
```

Here the factorization monomial is

```tex
\[
  x^{\mathcal F}=\prod_{i\ge0}x_i^{|F_i|}.
\]
```

The source preprint uses zero-indexed variables
`\mathbf{x}=(x_0,x_1,x_2,\ldots)` because factor labels are indexed by
`0,1,2,...`.

## Rational Dyck Tableaux

A rational Dyck tableau of step `tau` is a left-aligned tableau whose row
lengths form a partition shape.  The conditions are:

- each row, read left to right, is a dual rational Dyck sequence of step
  `tau`;
- each column, read bottom to top, is an affine rational Dyck sequence of step
  `tau`.

Let `\lambda(P)` be the shape.  Let `\operatorname{RR}(P)` be the row-reading
word.  In the proof-source convention, rows are processed in the
top-to-bottom convention used by the tableau insertion section, and row
reading is described there consistently with that convention.  The current
item writeup says "rows left-to-right, bottom to top"; if rewriting, verify and
state the chosen orientation once, then use it consistently.

The rational conjecture indexes Schur terms by rational Dyck tableaux with
entries exactly `S` and `\dinv_\tau(\operatorname{RR}(P))=d`.

## Classical Theorem

The theorem-level classical statements are:

```tex
\[
  \DSstar(S,d;\mathbf{x})
  =
  \sum_P s_{\lambda(P)}(\mathbf{x}),
\]
```

where `P` ranges over classical Dyck tableaux with entries `S` and
`\dinv(\operatorname{RR}(P))=d`, and

```tex
\[
  \DS(S,d;\mathbf{x})
  =
  \sum_P s_{\lambda(P)'}(\mathbf{x}),
\]
```

with the same indexing set.

The proof source is
`Dyck/paper/working_drafts/draft_v3_sections/03_tableau_bijection_schur.tex`.
The key theorem there is the tableau-factorization bijection:

- Input: a dual Dyck factorization
  `\mathcal F=(F_0,F_1,\ldots)` of `S` with
  `\di(F_0F_1\cdots)=d`.
- Output: a pair `(P,Q)`.
- `P` is a Dyck tableau with entries `S` and
  `\di(\operatorname{RR}(P))=d`.
- `Q` is a semistandard Young tableau of the same shape as `P`.
- The content of `Q` records the factorization weight:
  `m_i(Q)=|F_i|`.
- The factorization monomial becomes the SSYT monomial attached to `Q`.

Summing over all recording tableaux `Q` of shape `\lambda(P)` gives the Schur
function `s_{\lambda(P)}(\mathbf{x})`, which proves the dual formula.

The affine/nondual theorem is not proved by a separate insertion algorithm in
the source.  It is derived from the dual theorem using fundamental
quasisymmetric expansions and the usual involution `\omega`, with
`\omega(s_\lambda)=s_{\lambda'}`.  The fixed-word dual and affine allowed-cut
conditions are complementary in the classical `tau = 1` integer setting.

## Classical Insertion Proof Story

The rewrite does not need to reproduce the full insertion proof, but it should
describe the mechanism accurately.

Source file:

- `Dyck/paper/working_drafts/draft_v3_sections/03_row_and_tableau_insertion.tex`

The local operation inserts one dual Dyck row/word into another.  In the source
notation this is `\rowsert`.  It starts with a row `R`, an input dual Dyck
sequence `F`, and an initially empty evicted sequence `E`.  At each step, take
the first input letter `a=F[0]` and search for the smallest row index `i` with
`a <= R[i]+1`.

The cases are:

- Case 0: no such `i`; append `a` to the row and evict nothing.
- Case 1: `a <= R[i]`; replace `R[i]` by `a` and append the old value of
  `R[i]` to `E`.
- Equality branch: `a=R[i]+1`.  Compare the maximal `+2`-chain in the row
  starting at `i` with the maximal `+2`-chain at the front of the input.
- Case 2: if the row chain length is at most the input chain length, replace
  the row chain by the input chain and evict the old row chain.
- Case 3: if the row chain is longer, pass the input chain into `E` and leave
  the row unchanged.

The reverse operation is `\worsert`.  The source proves that the forward and
reverse operations are mutual inverses in the needed setting, preserve dual
Dyck validity, and preserve the dinv parameter in the sense needed by tableau
insertion.

Tableau insertion `\texttt{tabsert}(P,F)` iterates row insertion through a
tableau.  The cells added while inserting factor `F_i` are recorded with label
`i`, producing the recording tableau `Q`.  The horizontal-strip property gives
semistandardness of `Q`, and reverse insertion recovers the factorization.

For a rewritten `explanation.tex`, a compact proof sketch is enough:

1. State the dual tableau-factorization bijection.
2. Explain that summing the recording tableau over a fixed shape gives a Schur
   function.
3. Explain that affine/nondual follows by the standard involution.

Do not attempt to reprove all row-insertion cases unless the rewrite is meant
to become a full paper section.

## Degenerate Step 0

At `tau = 0`, the pair contribution is

```tex
d_0(a,b)=0
```

for all entries in the item writeup.  Therefore a fixed multiset has only the
single dinv class `d=0`.

The sequence conditions become:

- dual factors: `x_{i+1} > x_i`, hence strictly increasing;
- affine factors: `x_{i+1} <= x_i`, under the orientation conventions this is
  the weak/ordinary RSK counterpart after the same row/column convention
  translation used in the item.

The intended message is simple: step `0` is not new; it is the classical
RSK/dual-RSK baseline for Schur expansions.  Use this as motivation, not as
the main theorem.

If the rewrite includes this section, be cautious with orientation.  The item
currently says the step-0 rational tableaux are row-strict semistandard
tableaux "in our orientation."  Keep that qualifier unless the conventions are
spelled out fully.

## Rational `r = s*t + 1` Conjecture

The conjectural source is
`Dyck/paper/research_notes/rational_generalizations.tex`, subsection
"Conjectured rational Schur positivity".

For a fixed nonnegative step `tau`, the conjecture is:

```tex
\[
  \DS^{(\tau)}(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)'}(\mathbf x),
\]
```

and

```tex
\[
  {\DSstar}^{(\tau)}(S,d;\mathbf x)
  =
  \sum_P s_{\lambda(P)}(\mathbf x),
\]
```

where `P` ranges over rational Dyck tableaux of step `tau` with entries `S`
and `\dinv_\tau(\operatorname{RR}(P))=d`.

Known/conjectural status:

- `tau = 0`: classical RSK/dual-RSK baseline.
- `tau = 1`: classical Dyck theorem proved in the 2026 preprint.
- `tau > 1`: conjecture only.

The phrase "`r = s*t + 1` analogue" means the step parameter is `t` or `tau`.
It does not mean the formula is available for all coprime rational slopes
`r/s`.

## Computational Evidence

The executable finite checks are in
`Combinatorics/items/dyck_symmetric_functions/code/check_rational_dyck_generalization.py`.

The checker inputs are:

- `--t`: rational step;
- `--alphabet-size` or `-A`: alphabet size, using `{1,2,...,A}`;
- `--max-length` or `-L`: every length `1 <= l <= L`.

For each length, the exhaustive checker:

- constructs every word over `{1,...,A}` that contains `1`;
- groups words by multiset and rational dinv;
- generates every positive composition of the word length;
- groups compositions by their sorted underlying partition;
- checks that every composition with the same underlying partition gives the
  same number of valid dual Dyck factorizations;
- compares that common factorization count with the Schur-side prediction from
  rational Dyck tableaux and SSYT counts.

The implementation uses a cut-mask optimization.  Each word has a required
dual-cut mask: adjacent positions that cannot lie in the same dual factor must
be cut.  A composition is valid exactly when its cut positions contain that
required mask.  Optional NumPy/Numba support accelerates word grouping and can
split large word scans across workers.

Important interpretation:

- These checks are finite evidence only.
- They do not prove the rational conjecture.
- The exhaustive checker uses the "contains 1" normalization in its word
  enumeration.  Do not describe it as literally traversing every word over the
  alphabet unless that qualifier is included.
- The checker no longer has the older variable-count parameter,
  affine/dual/both option, or compressed/full comparison modes.

Official bounded checks recorded in the item README:

```text
python check_rational_dyck_generalization.py --t 2 -A 10 -L 10
python check_rational_dyck_generalization.py --t 3 -A 13 -L 9
python check_rational_dyck_generalization.py --t 4 -A 16 -L 8
```

The README states that these skip `t=1` because `t=1` is proved, and that they
check all multisets and all occurring dinv values in the stated bounded boxes,
with the normalization described above.

The Monte Carlo class checker is
`Combinatorics/items/dyck_symmetric_functions/code/random_rational_dyck_checks.py`.
It samples a word uniformly from `{1,...,A}^L`, fixes the sampled multiset and
dinv value, then exhaustively checks that single class.  Unlike the exhaustive
checker, it does not restrict sampled words to contain `1`.

The current `explanation.tex` records official Monte Carlo runs of 100 sampled
classes for:

```text
(t,A,L)=(2,11,12), (3,14,11), (4,17,10)
```

If the rewrite mentions these, call them sampled class checks, not exhaustive
box checks.

## Suggested Rewrite Shape

A strong rewritten explanation should have this order:

1. Introduction and status.
   Say what the object is and immediately classify proven vs conjectural
   material.

2. Definitions.
   Define `\dinv_\tau`, affine and dual sequences, factorizations,
   `\DS^{(\tau)}`, `{\DSstar}^{(\tau)}`, rational Dyck tableaux, shape, and
   row-reading word.

3. Classical theorem.
   State dual and affine formulas.  Explain that the dual formula is proved by
   the tableau-factorization bijection and that the affine formula follows by
   `\omega`.

4. Proof sketch of the classical theorem.
   Keep it high-level: insertion produces `(P,Q)`, `Q` records factor sizes,
   summing `Q` produces Schur functions.

5. Degenerate `tau=0` baseline.
   Present it as RSK/dual-RSK motivation.

6. Rational `r=s\tau+1` conjecture.
   State the conjectural formulas and identify what is known (`tau=0,1`) and
   what is only checked computationally (`tau>1`).

7. Computational evidence.
   List the checker, what it checks, official boxes, and limitations.

The current explanation already contains most of these ingredients.  The main
rewrite improvement should be clarity and convention control, not changing the
mathematics.

## Statements To Avoid

Do not say:

- "The rational `r=s*t+1` case is proved."  It is conjectural for `t>1`.
- "The code proves the conjecture."  It provides bounded evidence.
- "The item covers arbitrary rational `r/s`."  It does not.
- "The affine rational formula is independently checked by the same direct
  insertion proof."  The classical affine formula is derived by involution;
  the rational affine formula is part of the conjectural pair.
- "The exhaustive checker traverses all words over `{1,...,A}`" without
  mentioning the contains-`1` normalization.
- "The Monte Carlo checker is exhaustive over a box."  It exhaustively checks
  the class selected by each sample, not the whole box.

## Useful Commands

Run from `Combinatorics/items/dyck_symmetric_functions`.

Compile the explanation:

```text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
```

Run the classical insertion demo:

```text
python code/classical_insertion_demo.py
```

Run a small rational check:

```text
python code/check_rational_dyck_generalization.py --t 2 -A 4 -L 4
```

Run a small random class check:

```text
python code/random_rational_dyck_checks.py --t 2 -A 5 -L 5 --iterations 5 --seed 1
```

Official exhaustive boxes, potentially expensive:

```text
python code/check_rational_dyck_generalization.py --t 2 -A 10 -L 10
python code/check_rational_dyck_generalization.py --t 3 -A 13 -L 9
python code/check_rational_dyck_generalization.py --t 4 -A 16 -L 8
```

## Minimum Correct Final Message For The Rewrite

If the rewrite is successful, a reader should come away with this summary:

Classical Dyck symmetric functions have Schur expansions indexed by Dyck
tableaux.  The dual version expands in `s_{\lambda(P)}` and is proved by an
explicit tableau insertion bijection with semistandard recording tableaux.  The
affine version expands in `s_{\lambda(P)'}` and follows by the standard
involution.  The same formulas have a natural `r=s\tau+1` rational analogue
using step-`\tau` dinv, affine/dual rational Dyck sequences, and rational Dyck
tableaux.  That analogue is known at `\tau=0` and `\tau=1`, and is conjectural
for `\tau>1`, with finite computational checks over stated boxes.
