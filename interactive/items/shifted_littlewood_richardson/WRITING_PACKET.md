# Writing Packet: Shifted Littlewood-Richardson

This packet is for an AI writing agent rewriting
`Combinatorics/items/shifted_littlewood_richardson/explanation.tex`.

The goal is to explain the conjectural shifted Littlewood-Richardson rules for
skew shifted stable Grothendieck functions `GP` and `GQ`, together with the
bounded direct-vs-rule monomial checks, without presenting either rule as
proved.

## Files To Read First

Current item files:

- `Combinatorics/items/shifted_littlewood_richardson/README.md`
- `Combinatorics/items/shifted_littlewood_richardson/item.yaml`
- `Combinatorics/items/shifted_littlewood_richardson/explanation.tex`
- `Combinatorics/items/shifted_littlewood_richardson/html/body.html`
- `Combinatorics/items/shifted_littlewood_richardson/code/README.md`
- `Combinatorics/items/shifted_littlewood_richardson/code/check_shifted_lr.py`
- `Combinatorics/items/shifted_littlewood_richardson/code/shifted_lr_default_summary.txt`

Primary source/provenance files:

- `Conjectures-and-Computations/shifted-LR/skew-GQ-expansion.py`
- `Conjectures-and-Computations/shifted-LR/skew-GP-expansion.py`
- `Conjectures-and-Computations/shifted-LR/skew GP_GQ.tex`

The curated checker combines the source `GP` and `GQ` scripts.  The source
`GQ` script checks the related `GR` formulation; the source README says this
implies the corresponding `GQ` expansion.

## Executive Summary

This item curates conjectural positive expansion rules for skew shifted stable
Grothendieck functions:

```tex
GP_{\lambda/\mu}=\sum_{P} GP_{\operatorname{wt}(P)}
```

and

```tex
GQ_{\lambda/\mu}=\sum_{Q} GQ_{\operatorname{wt}(Q)}.
```

For the `GP` rule, `P` ranges over shifted set-valued `P`-tableaux of shape
`\lambda/\mu` satisfying the lattice property.

For the `GQ` rule, `Q` ranges over shifted set-valued `Q`-tableaux of shape
`\lambda/\mu` satisfying both:

- the lattice property;
- the primed-starting property.

The source `GQ` computation is implemented through a related `GR` model.  In
the public writeup, say `GQ/GR` when referring to the checked branch unless the
sentence is explicitly about the conjectural `GQ` expansion.

The curated checker compares:

1. the direct homogeneous monomial expansion of the skew function;
2. the homogeneous monomial expansion reconstructed from the conjectural
   Littlewood-Richardson rule.

These are bounded checks only.  The `GP` and `GQ` rules are conjectural.

## Status Boundaries

Use this status split:

- **`GP` rule:** conjectural; bounded direct-vs-rule monomial checks pass.
- **`GQ` rule:** conjectural; checked through the source `GR` formulation.
- **Curated code:** finite evidence/regression checks, not proofs.
- **Default run:** degree `5`, shape/skew `[3,1]/[1]`, `3` variables, both
  branches pass.
- **Additional curation run:** degree `6`, same shape/skew and variables, both
  branches pass.

The strongest safe status sentence is:

> The shifted Littlewood-Richardson rules are conjectural; the curated checker
> verifies bounded monomial-expansion identities for selected finite cases.

Do not say the checks prove the conjectural rules.

## Reading Words

The writeup should preserve the two reading-word conventions.

The **backword** is read:

- by rows from top to bottom;
- within each row, from right to left;
- within each box, primed entries first in decreasing order, then unprimed
  entries in decreasing order.

The **forword** is read:

- by rows from bottom to top;
- within each row, from left to right;
- within each box, unprimed entries first in decreasing order, then primed
  entries in decreasing order.

Implementation references:

- `back`
- `forw`
- `read_w`

The source representation in the checker is:

```text
1' -> 1, 1 -> 2, 2' -> 3, 2 -> 4, ...
```

This means parity matters:

- odd entries represent primed letters;
- even entries represent unprimed letters.

## Lattice Property

The lattice property is checked for each adjacent pair `i,i+1`.

In the backword:

- count unprimed `i` and unprimed `i+1`;
- the count of unprimed `i+1` must never exceed the count of unprimed `i`;
- an `(i+1)'` may not occur when those two counts are equal.

In the forword:

- count primed `i'` and primed `(i+1)'`;
- the count of primed `(i+1)'` must never exceed the count of primed `i'`;
- an unprimed `i` may not occur when those two counts are equal.

Implementation reference:

- `lattice`

## Primed-Starting Property

The primed-starting property is used for the `Q` rule.

Read boxes:

- by rows from bottom to top;
- left to right within each row.

For each `i`, the first box containing `i` or `i'` must contain `i'` but not
`i`.

The checker implements the `GQ/GR` branch using:

- `first_unprimed`
- `primed_start`

This is easy to confuse: the source `GQ` script checks a related `GR` rule,
and the source README says that `GR` check implies the `GQ` expansion.

## Conjectural Rules

Let `\mathcal P_{\lambda/\mu}` be the set of shifted set-valued `P`-tableaux
of shape `\lambda/\mu` satisfying the lattice property.  The conjectural `GP`
rule is:

```tex
GP_{\lambda/\mu}
=
\sum_{P\in\mathcal P_{\lambda/\mu}} GP_{\operatorname{wt}(P)}.
```

Let `\mathcal Q_{\lambda/\mu}` be the set of shifted set-valued `Q`-tableaux
of shape `\lambda/\mu` satisfying the lattice and primed-starting properties.
The conjectural `GQ` rule is:

```tex
GQ_{\lambda/\mu}
=
\sum_{Q\in\mathcal Q_{\lambda/\mu}} GQ_{\operatorname{wt}(Q)}.
```

For `GQ`, include the caveat:

> The source `GQ` code checks an equivalent-looking rule in the related `GR`
> model; the source README says the checked `GR` rule implies the corresponding
> `GQ` expansion.

## Checker Details

Curated checker:

```text
code/check_shifted_lr.py
```

Default command from `Combinatorics/items/shifted_littlewood_richardson`:

```text
python code/check_shifted_lr.py
```

Default parameters:

```text
degree = 5
shape/skew = [3, 1]/[1]
num_vars = 3
kind = both
```

The checker computes:

- `direct`: direct homogeneous monomial expansion of the skew function;
- `rule`: conjectural shifted LR expansion by weights;
- `reconstructed`: monomial expansion reconstructed from `rule`.

The check passes when:

```python
direct == reconstructed
```

Implementation references:

- `monomial_exp`
- `rule_expand`
- `list_expand`
- `compare`

## Expected Default Output

The default run records:

```text
GP shifted LR bounded check
  degree: 5
  shape/skew: [3, 1]/[1]
  variables: 3
  direct monomial terms: 3
  conjectural rule terms: 3
  reconstructed monomial terms: 3
  PASS: True

GQ/GR shifted LR bounded check
  degree: 5
  shape/skew: [3, 1]/[1]
  variables: 3
  direct monomial terms: 3
  conjectural rule terms: 3
  reconstructed monomial terms: 3
  PASS: True
```

The actual script also prints the rule expansions:

```text
GP rule expansion:
[[2, [3, 1, 0, 0, 0, 0, 0, 0, 0]],
 [1, [3, 0, 0, 0, 0, 0, 0, 0, 0]],
 [2, [2, 1, 0, 0, 0, 0, 0, 0, 0]]]

GQ/GR rule expansion:
[[1, [3, 1, 0, 0, 0, 0, 0, 0, 0]],
 [1, [3, 0, 0, 0, 0, 0, 0, 0, 0]],
 [1, [2, 1, 0, 0, 0, 0, 0, 0, 0]]]
```

These expansions are useful diagnostics but should not be oversold as proof.

## Additional Curation Check

The default summary says the same shape/skew and variables were also checked
at degree `6`:

```text
python code/check_shifted_lr.py --degree 6 --shape 3,1 --skew 1 --num-vars 3
```

Both `GP` and `GQ/GR` checks passed for that degree-`6` case.

## Reproducibility Commands

Run both branches with default parameters:

```text
python code/check_shifted_lr.py
```

Run individual degree-`6` branches:

```text
python code/check_shifted_lr.py --kind gp --degree 6 --shape 3,1 --skew 1 --num-vars 3
python code/check_shifted_lr.py --kind gq --degree 6 --shape 3,1 --skew 1 --num-vars 3
```

Run another sample shape:

```text
python code/check_shifted_lr.py --kind both --degree 5 --shape 4,2 --skew 2 --num-vars 3
```

Compile the explanation from the item directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error explanation.tex
```

Regenerate the repository site from `Combinatorics/`:

```text
python build_site.py
```

## Current `explanation.tex` Assessment

The current explanation is accurate and compact:

- defines backword and forword;
- explains the lattice property;
- explains the primed-starting property;
- states separate conjectural `GP` and `GQ` rules;
- includes the `GR` caveat for the source `GQ` checker;
- describes the direct-vs-rule monomial comparison;
- reports default parameters and finite-evidence status.

Possible rewrite improvements:

1. State the conjectural status in the opening paragraph.
2. Keep `GP`, `GQ`, and checked `GQ/GR` terminology visually distinct.
3. Add the exact default output counts if useful.
4. Make clear that `degree` is a homogeneous-degree truncation/check
   parameter, not a full infinite expansion.
5. Avoid expanding the full source-code representation unless writing a code
   guide.

## Suggested Rewrite Structure

1. **Purpose and status.**
   State that the rules are conjectural and the code gives bounded checks.

2. **Reading words.**
   Define backword and forword precisely.

3. **Conditions.**
   Define the lattice property and primed-starting property.

4. **Rules.**
   State the `GP` rule and the `GQ` rule separately, with the `GR` caveat.

5. **Checker.**
   Explain direct expansion, rule expansion, reconstruction, default
   parameters, and expected output.

6. **Limitations.**
   Say the checks are finite evidence, not proofs.

## Things Not To Say

Avoid these mistakes:

- Do not say the shifted Littlewood-Richardson rules are proved.
- Do not say the finite checker proves either conjecture.
- Do not conflate the source `GR` check with a direct `GQ` implementation
  without the caveat.
- Do not omit the primed-starting property from the `Q` rule.
- Do not change the backword/forword reading order.
- Do not describe the checker as comparing only term counts; it compares the
  actual monomial expansions.
- Do not imply the default run covers all shapes, all degrees, or all numbers
  of variables.

## Minimal Source-Backed Claims

The writing agent may safely state:

- The item curates conjectural shifted Littlewood-Richardson rules for skew
  `GP` and `GQ` functions.
- The source files are `skew-GP-expansion.py`, `skew-GQ-expansion.py`, and
  `skew GP_GQ.tex`.
- The `GP` rule sums over shifted set-valued `P`-tableaux with the lattice
  property.
- The `GQ` rule sums over shifted set-valued `Q`-tableaux with the lattice and
  primed-starting properties.
- The source `GQ` script checks the related `GR` formulation, which the source
  README says implies the `GQ` expansion.
- The default checker uses degree `5`, shape/skew `[3,1]/[1]`, and `3`
  variables.
- In the default run, both `GP` and `GQ/GR` branches have `3` direct monomial
  terms, `3` conjectural rule terms, `3` reconstructed monomial terms, and
  `PASS: True`.
- A degree-`6` check for the same shape/skew and variables passed during
  curation.

## Minimum Correct Final Message For The Rewrite

If the rewrite is successful, a reader should come away with this summary:

This item records conjectural shifted Littlewood-Richardson rules for skew
shifted stable Grothendieck functions.  The `GP` rule uses shifted set-valued
`P`-tableaux satisfying the lattice property.  The `GQ` rule uses shifted
set-valued `Q`-tableaux satisfying both the lattice and primed-starting
properties, with the source computation checking the related `GR` formulation.
The curated checker compares direct homogeneous monomial expansions with
expansions reconstructed from the conjectural rules.  The default degree-`5`
case for shape/skew `[3,1]/[1]` and `3` variables passes for both `GP` and
`GQ/GR`.  These are bounded checks, not proofs of the conjectures.
