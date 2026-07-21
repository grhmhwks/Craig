# Writing Packet: Dyck Skeleton String Decompositions

Target file for the writing agent:

```text
Combinatorics/items/dyck_skeleton_string_decompositions/explanation.tex
```

The current task is a rewrite of `explanation.tex`, not a light polish.  The
rewritten explanation should be public-facing, self-contained, and honest about
which parts are proved, conjectural, computationally checked, or draft-level.

Do not edit `explanation.tex` until the writing agent has first presented its
plan to the user.

## Item-Level Context

Item slug:

```text
dyck_skeleton_string_decompositions
```

Current item summary:

- Classical Dyck skeleton strings are proved in the 2026 Hawkes preprint in
  the low-deficit range.
- The `r = tau*s + 1`, `tau > 1` skeleton formula is conjectural.
- The item-level code gives finite checks for the conjectural formula and for
  the currently implemented East3/East5 partial lower-half map.
- The NRCM material is a separate general-rational diagnostic.  It has an
  AI-generated proof draft of deficit preservation where the map is defined,
  but the item must not present it as a fully human-verified theorem.

Primary local files for the item:

```text
Combinatorics/items/dyck_skeleton_string_decompositions/README.md
Combinatorics/items/dyck_skeleton_string_decompositions/item.yaml
Combinatorics/items/dyck_skeleton_string_decompositions/explanation.tex
Combinatorics/items/dyck_skeleton_string_decompositions/html/body.html
Combinatorics/items/dyck_skeleton_string_decompositions/code/README.md
Combinatorics/items/dyck_skeleton_string_decompositions/code/check_r1mod_skeleton_strings.py
Combinatorics/items/dyck_skeleton_string_decompositions/code/run_official_r1mod_checks.py
Combinatorics/items/dyck_skeleton_string_decompositions/code/check_nrcm_lower_half.py
Combinatorics/items/dyck_skeleton_string_decompositions/code/check_nrcm_domain.py
```

Source paths named by the item:

```text
Dyck/paper/working_drafts/arxiv_submission.tex
Dyck/paper/working_drafts/draft_v3_sections/05_skeletons_setup.tex
Dyck/paper/working_drafts/draft_v3_sections/05_up_down.tex
Dyck/paper/working_drafts/draft_v3_sections/05_east_map.tex
Dyck/paper/working_drafts/draft_v3_sections/05_east_west_inverse.tex
Dyck/paper/working_drafts/draft_v3_sections/05_decomposition_formula.tex
Dyck/paper/research_notes/rational_generalizations.tex
Dyck/paper/research_notes/naive_rational_cyclic_map_thm.tex
Dyck/paper/research_notes/naive_rational_cyclic_map_readable.tex
Dyck/docs/skeleton_string_decomposition_workflow.md
Dyck/code/experiments/skeleton_string_decompositions/current_state.md
Dyck/code/experiments/skeleton_string_decompositions/evidence_log.md
Dyck/code/experiments/skeleton_string_decompositions/failure_log.md
```

Public citation anchor:

```text
Graham Hawkes, Dyck Symmetric Functions and Applications to q,t-Catalan
Polynomials, arXiv:2605.13003, 2026.
https://arxiv.org/abs/2605.13003
```

## Writing Constraints

Follow:

```text
agents/explanation_writing_agent.md
mathematical_writing.md
pedalogical_princinples.md
explanations_initial_round.md
```

Important consequences:

- The explanation must address outside readers, not repository maintainers.
- Avoid status-ledger prose.  Put provenance and workflow history in README-like
  files, not in the explanation.
- Do not assume the reader has access to hidden `Dyck` notes or internal agent
  workflows.
- Define all nonstandard terms before use.
- Do not upgrade conjectural or AI-draft material to theorem status.
- Explain the code's role mathematically; do not turn the note into an
  implementation walkthrough.
- If the rewrite is substantial, first return a plan with:
  `Explanation goal`, `Reader assumptions`, `Definitions needed`,
  `Main structure`, `Paper connections`, `Code explanation`, and
  `Open questions before drafting`.

## Recommended Exposition Shape

A good rewrite should be shorter and more focused than the current draft.
Suggested structure:

1. **Strings in a deficit layer.**
   Explain the common phenomenon first: a string is a sequence of objects with
   area increasing by one, dinv decreasing by one, and fixed deficit.  The lower
   half of a deficit layer consists of terms with area at most the midpoint.

2. **Classical theorem.**
   Define ordinary Dyck sequences, area, dinv, deficit, full skeletons, and
   special skeletons only to the degree needed to state the low-deficit string
   decomposition.  State the classical result as proved by the 2026 preprint.
   Do not reproduce the East/West local case analysis.

3. **Rational `r = tau*s + 1` conjecture.**
   Define normalized `tau`-Dyck sequences, `dinv_tau`, total degree
   `M = tau*binom(s,2)`, deficit, extractable entries, and special rational
   skeletons.  State the conjectural low-deficit formula with bound
   `defc_tau <= (s-2)(tau+1)-4`.

4. **Computational evidence.**
   Explain that the checker compares coefficient dictionaries for the formula
   and separately tests the current East3/East5 lower-half map.  Make clear
   that `formula_status: PASS` and `map_status: PASS` are different claims, and
   that `map_status: PARTIAL` means the code hit `unsupported_level_7`.

5. **NRCM diagnostic.**
   Keep this short unless the user asks for a full NRCM exposition.  Present
   NRCM as a separate general-rational diagnostic for directed chains.  It is
   not currently a human-verified theorem in the curated item.  The code checks
   finite lower-half definedness, area increase, deficit preservation, target
   membership, and injectivity.

## Classical Material To Preserve

Ordinary Dyck sequence of length `n`:

```tex
x=(x_0,\ldots,x_{n-1}),\qquad
x_0=0,\quad x_i\ge0,\quad x_{i+1}\le x_i+1.
```

Statistics:

```tex
\area(x)=\sum_i x_i,
```

```tex
\dinv(x)=\#\{(i,j):0\le i<j<n,\ x_i=x_j
  \text{ or } x_i=x_j+1\}.
```

Top degree and deficit:

```tex
M=\binom n2,\qquad
\defc(x)=M-\area(x)-\dinv(x).
```

Skeleton definitions from the 2026 preprint:

- A full Dyck skeleton is a Dyck sequence with no extractable element under the
  leftmost extraction convention.
- For `n >= 4`, the exceptional full skeleton is

```tex
\epsilon_n=(0,0,1,\underbrace{0,\ldots,0}_{n-4\text{ entries}},1).
```

- A special Dyck skeleton is a full Dyck skeleton not equal to `\epsilon_n`.
  For `n < 4`, every full skeleton is special.

The classical `up` map, when defined, changes statistics by:

```tex
\area(\mathrm{up}(x))=\area(x)+1,\qquad
\dinv(\mathrm{up}(x))=\dinv(x)-1.
```

The `down` map is inverse on the stated low-deficit lower-half domains and
changes statistics oppositely.

Classical string decomposition source statement:

For `n >= 4`, `M = binom(n,2)`, and `d <= 2n-8`, put

```tex
\ell=\left\lfloor\frac{M-d}{2}\right\rfloor.
```

The lower half of the deficit-`d` layer is partitioned by strings

```tex
\{S,\mathrm{up}(S),\ldots,\mathrm{up}^{\ell-\area(S)}(S)\},
```

where `S` ranges over special Dyck skeletons of length `n`, deficit `d`, and
area at most `ell`.

Classical formula source statement:

```tex
\left.C_n(q,t)\right|_{\binom n2-2n+8\le \deg_{q,t}\le \binom n2}
=
\sum_{\substack{S\text{ special Dyck skeleton of length }n\\
                \defc(S)\le 2n-8}}
\frac{q^{\dinv(S)+1}t^{\area(S)}
      -q^{\area(S)}t^{\dinv(S)+1}}{q-t}.
```

The current `explanation.tex` uses the equivalent convention

```tex
\frac{q^{\area(S)}t^{\dinv(S)+1}
      -q^{\dinv(S)+1}t^{\area(S)}}{t-q}.
```

Either form is acceptable if internally consistent.  The item currently says
all coefficient polynomials use `q^{area}t^{dinv}`.

The proof in the preprint uses:

- the lower-half string decomposition;
- the known `q,t` symmetry of `C_n(q,t)`;
- symmetry of each interval contribution.

Do not reproduce the local East7/West7 proof machinery unless the user asks.

## Rational `r = tau*s + 1` Material To Preserve

Use `tau` for the step parameter and reserve `t` for the `q,t` variable.
Assume `s >= 1` and `tau > 1`, and set:

```tex
r=\tau s+1.
```

Normalized `tau`-Dyck sequence of length `s`:

```tex
x=(x_1,\ldots,x_s),\qquad
x_1=0,\quad x_i\ge0,\quad x_{i+1}\le x_i+\tau.
```

The code uses zero-based tuples `(x_0,...,x_{s-1})`; the current explanation
uses one-based notation in the rational section.  Pick one convention and use
it consistently.  Zero-based notation matches the code and nearby item
`dyck_skeleton_tableau_formulas`.

Statistics:

```tex
\area(x)=\sum_i x_i,
```

```tex
\dinv_\tau(x)=\sum_{i<j}
\begin{cases}
\max(0,x_i+\tau-x_j), & x_i\le x_j,\\
\max(0,x_j+1+\tau-x_i), & x_i>x_j.
\end{cases}
```

Top degree and deficit:

```tex
M_{s,\tau}=\tau\binom{s}{2},\qquad
\defc_\tau(x)=M_{s,\tau}-\area(x)-\dinv_\tau(x).
```

Rational extractability in the current item-level checker:

An entry `x_j` with value `e > 0` is extractable if exactly one earlier entry
lies in the predecessor interval

```tex
[\max(0,e-\tau),e)
```

and deleting the entry preserves the `tau`-Dyck adjacent condition.  If
`0 < j < s-1`, the splice condition is

```tex
x_{j+1}\le x_{j-1}+\tau.
```

If `j=s-1`, there is no new adjacent pair to check.  The leftmost extractable
entry is used.

Full and special rational skeletons:

- A full rational skeleton is a normalized `tau`-Dyck sequence with no
  extractable entry.
- For `s >= 4`, the excluded full skeleton is

```tex
\epsilon_{s,\tau}=(0,0,1,\underbrace{0,\ldots,0}_{s-4\text{ entries}},\tau).
```

- A special rational skeleton is a full rational skeleton other than
  `\epsilon_{s,\tau}`.  For `s < 4`, every full rational skeleton is special.
- The excluded full skeleton is not discarded from the strings; it is attached
  to the string beginning at `(0,\ldots,0,\tau)` by a special upward move.

Conjectural range:

```tex
B=(s-2)(\tau+1)-4.
```

If `B < 0`, there is no nonnegative deficit layer in the stated range.

Conjectural low-deficit formula from `rational_generalizations.tex`:

```tex
\sum_{\substack{
    S\text{ special rational Dyck skeleton of length }s\\
    \defc_\tau(S)\le B}}
\frac{
  q^{\dinv_\tau(S)+1}t^{\area(S)}
  -
  q^{\area(S)}t^{\dinv_\tau(S)+1}
}{q-t}.
```

Equivalent interval form for a fixed skeleton `S` of deficit `d`:

```tex
\sum_{j=\area(S)}^{M_{s,\tau}-d-\area(S)}
q^j t^{M_{s,\tau}-d-j}.
```

The current `explanation.tex` is more cautious and states a lower-half version:
for `L_d = floor((M-d)/2)`,

```tex
\sum_{\substack{x:\ \defc_\tau(x)=d,\ \area(x)\le L_d}}
q^{\area(x)}t^{\dinv_\tau(x)}
=
\sum_{\substack{z\text{ special skeleton}\\ \defc_\tau(z)=d}}
\sum_{i=\area(z)}^{L_d} q^i t^{M-d-i}.
```

The full formula needs either:

- deficit-layer `q,t` symmetry, or
- a direct full coefficient-dictionary identity.

The checker currently performs the second kind of check by comparing full
coefficient dictionaries, using signed rational-expression bookkeeping.  The
explanation should not imply that the East3/East5 lower-half map alone proves
the full rational formula.

## Code Evidence To Explain

`check_r1mod_skeleton_strings.py`:

- intended for `tau > 1`;
- default bound is `B=(s-2)(tau+1)-4`;
- prints `empty defect range` and exits successfully if `B < 0`;
- enumerates normalized `tau`-Dyck sequences in the retained deficit range;
- compares direct coefficients with formula-side coefficients;
- separately tests the implemented lower-half map.

Important output fields:

```text
formula_status: PASS|FAIL
map_status: PASS|PARTIAL|FAIL
status: PASS|FAIL
generated_words
searched_leaf_words
retained_defect_range_words
unsupported_level_7
```

Interpretation:

- `formula_status: PASS` means the full coefficient dictionaries matched in
  the checked finite case.
- `map_status: PASS` means the current implemented East3/East5 up/down map
  gave lower-half coverage with the checked inverse/statistic properties.
- `map_status: PARTIAL` means no contradiction was found before the map hit an
  unsupported level-7 branch.  It is not a full lower-half decomposition
  certificate.
- The script's command-line option says `--max-defect`; in the exposition,
  call this deficit.
- `generated_words` is the full normalized search-space size; the checker may
  prune the search, so `searched_leaf_words` can be smaller.

`run_official_r1mod_checks.py` configured ranges:

```text
tau=2, 1 <= s <= 14
tau=3, 1 <= s <= 12
tau=4, 1 <= s <= 10
tau=5, 1 <= s <= 9
```

For `s <= 4`, it runs formula-only.  For `s >= 5`, it runs both formula and
map checks.

No compact expected-output file or durable complete run log was found in the
item directory.  The existing HTML page states that recorded checks have the
partial map reaching all conjectural formula defect layers for:

```text
tau=2, 5 <= s <= 14
tau=3, 5 <= s <= 12
tau=4, 5 <= s <= 10
```

and that at `(tau,s)=(2,15)` the formula check passed through `defc <= 35`,
while the partial map hit `14` unsupported level-7 records at defect `35`.
If the rewrite wants to use these exact claims, state them as recorded item
evidence unless a fresh reproducibility run is provided.

## NRCM Material To Preserve Carefully

The NRCM is not the same as the `r=tau*s+1` special-skeleton map.  It is a
separate general-rational diagnostic for coprime positive `r,s`.

Definitions used in the item-level code:

```tex
H_i=\left\lfloor\frac{ri}{s}\right\rfloor,\qquad
L_i\equiv ri\pmod s,\quad 0\le L_i<s.
```

Position-coordinate path:

```tex
Q=(Q_0,\ldots,Q_{s-1}),\qquad
Q_0=0,\quad 0\le Q_i\le H_i.
```

Path heights:

```tex
P_i=H_i-Q_i.
```

The path is valid when:

```tex
P_0\le P_1\le\cdots\le P_{s-1}.
```

The item-level code defines diagnostic deficit by pair summands.  For
`1 <= i < j < s`, put `u = |Q_i-Q_j|`; if `Q_i != Q_j` and the comparisons
`Q_i > Q_j` and `L_i > L_j` have opposite truth values, replace `u` by
`u-1`, then clamp to `max(u,0)`.  Define

```tex
v_{ij}=
\begin{cases}
\Delta_i-(Q_{i+1}-Q_i), & Q_i>Q_j,\\
\Delta_{i-1}-(Q_i-Q_{i-1}), & Q_j>Q_i,\\
0, & Q_i=Q_j,
\end{cases}
```

where `Delta_i = H_{i+1}-H_i`.  The summand is

```tex
\delta_{ij}(Q)=\min(u_{ij},v_{ij}),
```

and

```tex
\defc(Q)=\sum_{1\le i<j<s}\delta_{ij}(Q),\qquad
\dinv(Q)=M-\area(Q)-\defc(Q),\quad M=\sum_iH_i.
```

Do not silently add a clamp to `v_{ij}`; the current item explicitly says this
is not part of the implemented statistic.

Strict NRCM:

For `I_k={k,k+1,...,s-1}`, list the suffix columns in increasing label order.
The candidate `T_k(Q)` moves each suffix value to the next suffix column in
that label order, and wraps the last value to the first suffix column after
adding `1`.  Columns outside the suffix are unchanged.

Starting with `k=1`, strict NRCM chooses the first `k` for which `T_k(Q)`
satisfies capacity.  It defines `NRCM(Q)=T_k(Q)` only if that first
capacity-valid candidate is also path-valid.  Otherwise NRCM is undefined.

Important status:

- By construction, a defined NRCM move raises area by one.
- The Dyck research notes contain an AI-generated and AI-checked proof draft
  that defined strict NRCM preserves deficit.
- The item should not call this a fully human-verified theorem unless the user
  supplies that decision.
- `check_nrcm_lower_half.py` is a finite diagnostic: it checks definedness,
  same deficit, area increase, target membership, and injectivity on checked
  lower-half sources.
- `check_nrcm_domain.py` checks only definedness on lower-half sources.

If including examples, the current explanation has two small ones:

- Slope `5/3`: `H=(0,1,3)`, `L=(0,2,1)`, `Q=(0,1,1)`.  For `k=1`,
  the suffix columns `{1,2}` in label order are `2,1`, and the move gives
  `T_1(Q)=(0,1,2)`, which is capacity-valid and path-valid.
- Slope `4/3`: `H=(0,1,2)`, `L=(0,1,2)`, `Q=(0,0,1)`.  The first
  capacity-valid suffix is `k=2`, giving `T_2(Q)=(0,0,2)`, whose path heights
  are `(0,1,0)`, not nondecreasing.  Strict NRCM is undefined.

## Current Explanation Problems To Fix

The current `explanation.tex` has useful material, but it is too ledger-like
and overlong for a public explanation.  Specific issues:

- It opens with status and computational caveats before giving a compact
  mental model of strings.
- It includes a long NRCM definition and diagnostic proposition; this may
  overwhelm the main skeleton-string story.
- It mixes lower-half string interpretation with full signed rational
  expression checks.  The rewrite should explicitly separate these.
- It uses both classical and rational skeleton definitions; the rewrite should
  introduce them in parallel only where that helps.
- It says the batch grid records intended finite tests, not independent fresh
  evidence.  That caution should be preserved unless a durable run log is
  added.
- It should avoid implying that the current East3/East5 partial map proves the
  conjectural rational formula.
- It should avoid implying that NRCM deficit preservation is a public theorem
  in the curated item.

## Suggested Main Statements

Use theorem/conjecture environments sparingly.

Possible theorem statement:

```tex
\begin{theorem}[Hawkes, low-deficit skeleton strings]
For \(n\ge4\) and \(d\le2n-8\), the lower half of the
deficit-\(d\) layer of ordinary Dyck sequences of length \(n\) is partitioned
by strings beginning at special Dyck skeletons.
\end{theorem}
```

Then either include the formula immediately after, or make it a corollary:

```tex
\left.C_n(q,t)\right|_{\binom n2-2n+8\le \deg_{q,t}\le \binom n2}
=
\sum_{\substack{S\text{ special Dyck skeleton}\\ \defc(S)\le 2n-8}}
\frac{q^{\dinv(S)+1}t^{\area(S)}
      -q^{\area(S)}t^{\dinv(S)+1}}{q-t}.
```

Possible conjecture statement:

```tex
\begin{conjecture}[Rational special-skeleton formula for \(r=\tau s+1\)]
Let \(\tau>1\), \(s\ge1\), and \(B=(s-2)(\tau+1)-4\).
In the normalized \(\tau\)-Dyck model, the low-deficit part
\(\defc_\tau\le B\) is given by the same interval formula, with special
rational skeletons replacing special Dyck skeletons.
\end{conjecture}
```

Then explain the lower-half version before the full interval version, because
the string interpretation is naturally lower-half.  Say that the full interval
formula is supported in the finite checker by direct coefficient-dictionary
comparison.

## What To Omit Or Relegate

Avoid including:

- detailed East3/East5/East7 case tables;
- current `SSD-R1-002` East7 tie-breaker research;
- superseded failures from exploratory logs, except as an internal caution;
- the full NRCM proof architecture;
- workflow/agent/provenance commentary inside `explanation.tex`;
- claims that require hidden source notes to understand.

The explanation may point to code files by name, but should not cite internal
workspace paths as mathematical authority.  Use the 2026 preprint as the
authority for the classical theorem.

## Verification After Writing

After the writing agent edits `explanation.tex`, run a LaTeX compile from:

```text
Combinatorics/items/dyck_skeleton_string_decompositions
```

Recommended command:

```text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
```

If the rewrite changes computational claims, either:

- include only claims already recorded in item files, with cautious wording; or
- run the relevant finite command and record the output before strengthening
  the claim.
