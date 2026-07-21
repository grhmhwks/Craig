# Writing Packet: qt-Catalan Middle Coefficients

This packet is for an AI writing agent rewriting
`Combinatorics/items/qt_catalan_middle_coefficients/explanation.tex`.

The goal is to explain the **flat middle coefficient theorem** and the broader
**flat-middle conjecture** without overstating what is proved.

## Files To Read First

Current item files:

- `Combinatorics/items/qt_catalan_middle_coefficients/explanation.tex`
- `Combinatorics/items/qt_catalan_middle_coefficients/README.md`
- `Combinatorics/items/qt_catalan_middle_coefficients/item.yaml`
- `Combinatorics/items/qt_catalan_middle_coefficients/code/check_flat_middle_coefficients.py`
- `Combinatorics/items/qt_catalan_middle_coefficients/code/flat_middle_coefficients_default_summary.txt`
- `Combinatorics/items/qt_catalan_middle_coefficients/code/README.md`

Primary source/provenance files:

- `Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex`
- `Dyck/paper/source_drafts/original_draft.tex`
- `Dyck/memory/proof_audits/theorem_5_30_qt_catalan_skeleton.md`
- `Dyck/memory/proof_audits/proposition_5_29_decomposition.md`
- `Dyck/memory/proof_audits/proposition_5_32_area_leq_defc.md`
- `Dyck/memory/computational_claims.md`
- `Dyck/code/code_assistant/codex_tasks/CA-0011_flat_middle_coefficients.md`
- `Dyck/code/code_assistant/reviews/CA-0011_flat_middle_coefficients_review.md`

## Executive Summary

Let

```tex
C_n(q,t)=\sum_D q^{\area(D)}t^{\dinv(D)}
```

where the sum is over Dyck area sequences of length `n`, and let

```tex
M=\binom n2,\qquad \defc(D)=M-\area(D)-\dinv(D).
```

For a fixed deficit `d`, all monomials in that deficit layer have total degree
`M-d`.  The "middle band" is

```tex
q^j t^{M-d-j},\qquad d\le j\le M-2d.
```

The proved classical skeleton result says:

> For `n >= 4` and `0 <= d <= 2n-8`, the coefficient of
> `q^j t^{M-d-j}` in `C_n(q,t)` is independent of `j` throughout
> `d <= j <= M-2d`.  The common value is the number of special Dyck skeletons
> of length `n` and deficit `d`.

The broader conjecture says:

> The same flatness should hold for every `0 <= d <= floor(M/3)`.

The broad range is **conjectural**.  The item must not imply it is proved by
the skeleton theorem or by finite code.

## Status

Use this status split:

- **Proved theorem:** flat middle coefficients in the skeleton range
  `0 <= d <= 2n-8`, for `n >= 4`, as a consequence of the skeleton-string
  decomposition and the special-skeleton formula.
- **Conjecture:** full flat-middle range
  `0 <= d <= floor(M/3)`.
- **Finite evidence:** direct coefficient checks for `n=4..8`, in the theorem
  range `0 <= d <= 2n-8`, passed.

Do not say that the finite code proves the theorem or the conjecture.

## Best Statement To Put In `explanation.tex`

Use a theorem/conjecture split like this.

```tex
\begin{theorem}[Flat middle coefficients in the skeleton range]
For \(n\ge 4\), set \(M=\binom n2\).  If \(0\le d\le 2n-8\), then the
coefficient of
\[
  q^j t^{M-d-j}
\]
in \(C_n(q,t)\) is independent of \(j\) for every integer
\[
  d\le j\le M-2d.
\]
The common coefficient is the number of special Dyck skeletons of length \(n\)
and deficit \(d\).
\end{theorem}
```

Then separately:

```tex
\begin{conjecture}[Full flat-middle range]
Let \(M=\binom n2\).  For every \(n\ge 1\) and every
\[
  0\le d\le \left\lfloor M/3\right\rfloor,
\]
the coefficient of \(q^j t^{M-d-j}\) in \(C_n(q,t)\) is independent of \(j\)
for all \(d\le j\le M-2d\).
\end{conjecture}
```

## What The Middle Band Means

For fixed `d`, the relevant total degree is `M-d`.

The band

```tex
d\le j\le M-2d
```

has two interpretations:

1. Lower endpoint `j=d`: this is the first "flat-middle" area predicted by the
   conjecture.
2. Upper endpoint `j=M-2d`: this is symmetric to `j=d` inside total degree
   `M-d`.

The condition that the interval is nonempty is exactly

```tex
d\le M-2d \quad\Longleftrightarrow\quad 3d\le M.
```

Thus the natural largest possible deficit range for this band is

```tex
d\le \left\lfloor M/3\right\rfloor.
```

The theorem proves only the smaller skeleton range `d <= 2n-8`.

## Proof Logic For The Theorem

The writing agent does not need to reproduce every local-map proof.  The clean
explanation should present the theorem as a consequence of three earlier
skeleton facts.

### Fact 1: Area Bound For Full Skeletons

Source:

- `Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex`
- `Dyck/memory/proof_audits/proposition_5_32_area_leq_defc.md`

Statement:

```tex
\area(S)\le \defc(S)
```

for every full Dyck skeleton `S`.

This is needed because if `S` is a special skeleton of deficit `d`, then
`area(S) <= d`.

Important proof/audit note:

- The source proof should choose the **leftmost offending position** in the
  increasing-run argument.
- The current `draft_v3_sections/05_decomposition_formula.tex` has the cleaned
  proof order: the area-bound proposition appears before the decomposition.

### Fact 2: Lower-Half String Decomposition

Source:

- `Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex`
- `Dyck/memory/proof_audits/proposition_5_29_decomposition.md`

For fixed `n`, `M=binom(n,2)`, and `d <= 2n-8`, put

```tex
\ell_d=\left\lfloor\frac{M-d}{2}\right\rfloor.
```

The Dyck sequences of length `n`, deficit `d`, and area at most `ell_d` are
partitioned into strings

```tex
\{S,\up(S),\up^2(S),\ldots,\up^{\ell_d-\area(S)}(S)\},
```

where `S` ranges over special Dyck skeletons of length `n`, deficit `d`, and
area at most `ell_d`.

Because of the area-bound fact, each special skeleton of deficit `d` starts no
later than area `d`, hence inside the desired middle range.

### Fact 3: Skeleton Formula And Symmetry

Source:

- `Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex`
- `Dyck/memory/proof_audits/theorem_5_30_qt_catalan_skeleton.md`

The low-deficit skeleton formula is

```tex
\left.C_n(q,t)\right|_{\binom n2-2n+8\le \deg_{q,t}\le \binom n2}
=
\sum_{\substack{S\text{ special Dyck skeleton of length }n\\
                \defc(S)\le 2n-8}}
\frac{q^{\dinv(S)+1}t^{\area(S)}
      -q^{\area(S)}t^{\dinv(S)+1}}{q-t}.
```

The geometric-series expansion is:

```tex
\frac{q^{\nu+1}t^a-q^a t^{\nu+1}}{q-t}
=
\sum_{j=a}^{\nu} q^j t^{a+\nu-j}.
```

For a skeleton `S` of deficit `d`,

```tex
a+\nu = M-d.
```

So the contribution is

```tex
\sum_{j=\area(S)}^{M-d-\area(S)} q^j t^{M-d-j}.
```

Since `area(S) <= d`, every special skeleton of deficit `d` contributes to
every exponent `j` in the middle band `d <= j <= M-2d`.  Therefore the
coefficient on that entire band is the number of special skeletons of deficit
`d`.

The full skeleton formula uses the known `q,t` symmetry of `C_n(q,t)`.  The
flat-middle theorem can be presented either as:

- a direct consequence of the displayed skeleton formula; or
- a consequence of the lower-half string decomposition plus symmetry.

Do not imply that actual `up` strings themselves construct the whole high half.
The high half is obtained by symmetry in the theorem proof.

## Relationship Between `2n-8` And `floor(M/3)`

The theorem range is meaningful inside the flat-middle band because

```tex
d\le 2n-8 \quad\Longrightarrow\quad 3d\le M
```

for `n >= 4`.  Equivalently,

```tex
\binom n2 - 3(2n-8)
= \frac{n^2-13n+48}{2}.
```

The quadratic has negative discriminant and positive leading coefficient, so
it is positive for all `n`.  This is the calculation used in the proof audits
to ensure `d <= (M-d)/2`.

The broader conjecture replaces the sufficient skeleton range `2n-8` by the
maximal possible nonempty-flat-band range `floor(M/3)`.

## Code Layer

Curated checker:

```text
Combinatorics/items/qt_catalan_middle_coefficients/code/check_flat_middle_coefficients.py
```

Default command from the item directory:

```bash
python code/check_flat_middle_coefficients.py
```

Default summary:

```text
n range: 4..8
direct coefficient convention: each Dyck sequence contributes q^area t^dinv
checked theorem range: 0 <= d <= 2n-8
generated Dyck sequences: 2047
sequences by n: {4: 14, 5: 42, 6: 132, 7: 429, 8: 1430}
Dyck validation checks: 2047
formula-vs-pair deficit checks: 2047
coefficient total checks: 5
checked (n,d) bands: 25
checked coefficients in bands: 325
flat-band checks: 25
skeleton-count match checks: 325
PASS
```

What the code checks:

- generates all Dyck area sequences for `n=4..8`;
- computes `area`, `dinv`, and `defc`;
- verifies formula deficit equals explicit defect-pair count;
- builds direct coefficient counts for `C_n(q,t)=sum_D q^area(D)t^dinv(D)`;
- counts special Dyck skeletons by deficit;
- for every checked `n,d` with `0 <= d <= 2n-8`, verifies every coefficient
  in

```text
q^j t^(M-d-j), d <= j <= M-2d
```

equals the special-skeleton count.

What the code does not check:

- it does not prove the theorem;
- it does not check the full conjectural range beyond `2n-8`;
- it does not prove `q,t` symmetry;
- it does not implement a symbolic Schur expansion;
- it does not replace the skeleton decomposition proof.

## Exact Code Definitions To Preserve

Direct coefficient convention:

```python
coeffs[(area, dinv)] += 1
```

Deficit:

```python
def deficit_statistic(seq: Sequence[int]) -> int:
    n = len(seq)
    return comb(n, 2) - area_statistic(seq) - dinv_statistic(seq)
```

Middle-band loop:

```python
for d in range(0, 2 * n - 7):
    target = skeleton_counts[d]
    band: list[tuple[int, int, int]] = []
    for j in range(d, m_total - 2 * d + 1):
        coeff = coeffs[(j, m_total - d - j)]
        band.append((j, m_total - d - j, coeff))
        require(coeff == target, ...)
```

The Python range `range(0, 2*n - 7)` means exactly

```text
0 <= d <= 2n-8.
```

Special skeleton test:

```python
def is_full_dyck_skeleton(seq: Sequence[int]) -> bool:
    return is_dyck_sequence(seq) and find_extractable_position(seq, include_final=True) is None


def excluded_full_skeleton(n: int) -> tuple[int, ...]:
    if n < 4:
        return ()
    return (0, 0) + (1,) + (0,) * (n - 4) + (1,)


def is_special_dyck_skeleton(seq: Sequence[int]) -> bool:
    values = tuple(seq)
    return is_full_dyck_skeleton(values) and values != excluded_full_skeleton(len(values))
```

## Current `explanation.tex` Assessment

Current file:

```text
Combinatorics/items/qt_catalan_middle_coefficients/explanation.tex
```

It is already mostly correct and cautious:

- defines `C_n`, `M`, and `defc`;
- states the theorem in the skeleton range;
- states the broad conjecture separately;
- says the curated code checks only the theorem range;
- reports the default run counts;
- avoids claiming finite checks prove the conjecture.

Possible rewrite improvements:

1. Make the "middle band" motivation explicit: the range `d <= j <= M-2d` is
   nonempty exactly when `d <= floor(M/3)`.
2. Explain why the skeleton theorem gives flatness: every special skeleton of
   deficit `d` has `area <= d`, so every skeleton interval covers the whole
   middle band.
3. Mention the lower-half string decomposition and symmetry at a high level,
   but do not reprove all local up/down lemmas.
4. Keep direct coefficient convention `q^area t^dinv` visible.
5. Keep the conjecture visually separate from the theorem.
6. Add source/provenance paragraph if desired, but do not overload the public
   item with internal file paths unless the site style wants that.

## Suggested Rewrite Structure

1. **Definitions.**
   Define Dyck area sequences, `area`, `dinv`, `M`, and `defc`.

2. **Middle Bands.**
   Explain fixed-deficit layer total degree `M-d` and the band
   `d <= j <= M-2d`.  Note the maximal possible range `d <= floor(M/3)`.

3. **Skeleton-Range Theorem.**
   State theorem for `0 <= d <= 2n-8`; common value is special-skeleton count.

4. **Why Skeletons Imply Flatness.**
   Summarize:
   - special skeleton `S` of deficit `d` contributes interval
     `j=area(S)..M-d-area(S)`;
   - area bound gives `area(S) <= d`;
   - hence every such interval contains the whole middle band;
   - summing over special skeletons gives constant coefficient.

5. **Full Flat-Middle Conjecture.**
   State separately for `0 <= d <= floor(M/3)`.

6. **Finite Check.**
   Describe `check_flat_middle_coefficients.py` and default counts.  Say it is
   a regression/finite evidence check, not proof.

7. **Status.**
   Close with a short status paragraph:
   theorem proved in skeleton range; full flat-middle range conjectural.

## Things Not To Say

Avoid these mistakes:

- Do not say "the full flat-middle conjecture is proved."
- Do not say the code proves the conjecture.
- Do not say the theorem holds for `d <= floor(M/3)`.
- Do not blur the theorem range `2n-8` with the conjectural range
  `floor(M/3)`.
- Do not claim the lower-half up strings alone construct the whole symmetric
  interval.  The upper half is supplied by `q,t` symmetry in the skeleton
  formula proof.
- Do not change the coefficient convention to `q^dinv t^area`; this item uses
  direct `q^area t^dinv`.
- Do not forget the excluded full skeleton
  `(0,0,1,0,\ldots,0,1)` in the definition of special skeleton.

## Minimal Source-Backed Claims

The writing agent may safely state:

- `C_n(q,t)` is computed in the direct Dyck area sequence convention
  `sum_D q^area(D)t^dinv(D)`.
- `defc(D)=binom(n,2)-area(D)-dinv(D)`.
- In the skeleton range `0 <= d <= 2n-8`, flatness follows from the
  special-skeleton formula.
- The common coefficient in the flat band is the number of special Dyck
  skeletons of length `n` and deficit `d`.
- The broad conjectural range is `0 <= d <= floor(binomial(n,2)/3)`.
- The default curated finite check covers `n=4..8`, 25 `(n,d)` bands, and 325
  coefficients, and it passes.

## Optional Example

If the rewrite needs an example, generate one from the code output rather than
inventing it.  The script prints representative bands when run:

```bash
python code/check_flat_middle_coefficients.py --representative-bands 10
```

Use the printed `representative bands` data verbatim or paraphrase it.  Do not
guess special-skeleton counts by hand.

## Build/Verification

After rewriting `explanation.tex`, run from
`Combinatorics/items/qt_catalan_middle_coefficients`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
python code/check_flat_middle_coefficients.py
```

The LaTeX should compile, and the Python script should end with:

```text
PASS
```

If code output changes, update

```text
code/flat_middle_coefficients_default_summary.txt
```

only if the changed output is expected and reviewed.
