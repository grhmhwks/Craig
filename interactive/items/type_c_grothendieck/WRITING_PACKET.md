# Writing Packet: Type C Grothendieck

This packet is for an AI writing agent rewriting
`Combinatorics/items/type_c_grothendieck/explanation.tex`.

The goal is to explain the conjectural type C Grothendieck hierarchy and the
bounded finite checks at the basic, strong, and peakset-preserving levels,
without presenting any of the conjectural bijections or positivity statements
as proved.

## Files To Read First

Current item files:

- `Combinatorics/items/type_c_grothendieck/README.md`
- `Combinatorics/items/type_c_grothendieck/item.yaml`
- `Combinatorics/items/type_c_grothendieck/explanation.tex`
- `Combinatorics/items/type_c_grothendieck/html/body.html`
- `Combinatorics/items/type_c_grothendieck/code/README.md`
- `Combinatorics/items/type_c_grothendieck/code/check_type_c_grothendieck.py`
- `Combinatorics/items/type_c_grothendieck/code/type_c_grothendieck_default_summary.txt`

Primary source/provenance files:

- `Conjectures-and-Computations/c-grothendieck/c-grothendieck.py`
- `Conjectures-and-Computations/c-grothendieck/c-grothendieck-strong.py`
- `Conjectures-and-Computations/c-grothendieck/c-grothendieck-strongest.py`
- `Conjectures-and-Computations/c-grothendieck/c-grothendieck-note.tex`

The curated checker combines the three source scripts into one command-line
tool.  The source note is the provenance for the mathematical definitions and
the conjectural `GQ`/`GR` formulations.

## Executive Summary

For a signed permutation `w`, the source note defines the type C stable
Grothendieck polynomial, also called the K-theoretic Stanley symmetric function
of type C, by signed factorizations of Hecke words:

```tex
GC_w=\sum_{f\in F_w}\mathbf{x}^{\operatorname{wt}(f)}.
```

The conjectural target is a positive expansion in `GQ` functions:

```tex
GC_w=\sum_{t\in T_w}GQ_{\operatorname{shape}(t)},
```

where `T_w` is the conjectural set of type C unimodal Hecke tableaux for `w`.

The source note also gives a stronger `GR` formulation for `GC_w^+`:

```tex
GC_w^+=\sum_{t\in T_w}GR_{\operatorname{shape}(t)}.
```

The curated code checks three finite statements:

- `basic`: count Hecke words by pairs `(type C unimodal tableau, standard
  shifted set-valued tableau)` of the same shape.
- `strong`: impose no adjacent equal Hecke letters and no consecutive entries
  in the same shifted set-valued tableau box.
- `strongest`: compare peaksets; the source note says this level would imply
  the positive `GQ` expansion.

All three levels are conjectural.  The code gives bounded evidence only.

## Status Boundaries

Use this status split:

- **Basic version:** conjectural; bounded count checks pass.
- **Strong version:** conjectural; bounded restricted count checks pass.
- **Peakset-preserving version:** conjectural; bounded peakset checks pass.
- **Curated code:** finite enumeration/regression checks, not a construction
  of the conjectural bijections.
- **Expansion status:** the `GQ` and `GR` formulas should be presented as
  conjectural.

The strongest safe status sentence is:

> The type C Grothendieck hierarchy is conjectural; the curated checker
> verifies bounded instances of the three source finite comparisons.

Do not say that the positive `GQ` expansion has been proved by the code.

## Signed Hecke Words And `GC_w`

The source note uses the ordered signed alphabet:

```tex
\cdots<-3<-2<-1<-0<0<1<2<3<\cdots.
```

For `i != 0`, the letters `i` and `-i` represent the simple transposition
`s_i`.  The letters `0` and `-0` represent the type C generator `s_0`.

A signed factorization is a word in this alphabet subdivided into strictly
increasing factors.  The weight records factor sizes.

The type C stable Grothendieck polynomial is:

```tex
GC_\omega=\sum_{f\in F_\omega}\mathbf{x}^{\operatorname{wt}(f)}.
```

## `GQ` And `GR` Formulations

The `Q`-Grothendieck function is:

```tex
GQ_\lambda=\sum_{q\in Q_\lambda}\mathbf{x}^{\operatorname{wt}(q)},
```

where `Q_\lambda` is the set of semistandard shifted set-valued tableaux of
`Q`-type.

The conjectural `GQ` expansion is:

```tex
GC_\omega = \sum_{t\in T_\omega} GQ_{\operatorname{shape}(t)}.
```

The stronger source formulation is:

```tex
GC_\omega^+ = \sum_{t\in T_\omega} GR_{\operatorname{shape}(t)}.
```

Here `GC_\omega^+` restricts signed factorizations by requiring a unique
minimum-absolute-value entry in each factor, with positive sign.  The `GR`
model is the shifted set-valued tableau submodel in which the first `i` or
`i'`, read left to right and bottom to top, is constrained to be `i`.

If rewriting the public explanation, keep these descriptions compact.  The
item does not need a full independent construction of `GQ`, `GR`, or
semistandard shifted set-valued tableaux unless the user asks for a deeper
expansion.

## Three Checked Levels

### Basic Count Level

For each signed permutation `w` and word length `n`, the basic conjectural
comparison counts Hecke words of length `n` for `w` against pairs `(t,r)`:

- `t` is a conjectural type C unimodal Hecke tableau for `w`;
- `r` is a standard shifted set-valued tableau with `n` entries;
- `t` and `r` have the same shape.

Implementation references:

- `run_basic_or_strong(mode="basic", ...)`
- `create_shapes(..., strong=False)`
- `children_basic`
- `hecke_tabs_for_shape`

### Strong Count Level

The strong level imposes:

- no adjacent equal Hecke letters;
- no consecutive entries in the same shifted set-valued tableau box.

Implementation references:

- `run_basic_or_strong(mode="strong", ...)`
- `words(..., no_equal_adjacent=True)`
- `create_shapes(..., strong=True)`
- `children_strong`

### Peakset-Preserving Level

The strongest level compares peaksets.  A peak in a Hecke word is an index `i`
with:

```tex
w_{i-1}<w_i>w_{i+1}.
```

The conjectural peakset-preserving correspondence sends this to a peak at `i`
in the recording shifted set-valued tableau.  The source note says this
peakset-preserving level would imply the positive `GQ` expansion.

Implementation references:

- `run_strongest`
- `add_word_peaks`
- `add_hecke_tabs`
- `standard_shifted_svts`
- `add_tableau_peaks`

## Checker Details

Curated checker:

```text
code/check_type_c_grothendieck.py
```

Default command from `Combinatorics/items/type_c_grothendieck`:

```text
python code/check_type_c_grothendieck.py
```

Default parameters:

```text
max word length: 4
largest generator index: 3
modes: basic, strong, strongest
```

The default run checks all three modes.  It groups enumerated words by the
signed permutation they produce and compares the word-side count with the
tableau-side count or peakset multiset.

The direct enumeration grows quickly.  The original source scripts used larger
defaults, including:

- length `8`, largest generator `4` for the basic and strong checks;
- length `11`, largest generator `4` for the strongest check.

The curated defaults are intentionally smaller so the item remains quick to
run.

## Expected Default Output

The default summary records:

```text
Basic type C Grothendieck count check
  grouped signed permutations: 53
  matching groups: 53
  mismatching groups: 0
  PASS: True

Strong type C Grothendieck count check
  grouped signed permutations: 53
  matching groups: 53
  mismatching groups: 0
  PASS: True

Strongest type C Grothendieck peakset check
  grouped signed permutations: 53
  matching groups: 53
  mismatching groups: 0
  PASS: True
```

The default run also prints:

- `shifted tableau shape-count terms` for the basic and strong modes;
- sample `[word, tableau_count, word_count]` records for the basic and strong
  modes;
- `bad examples` and timing data for the strongest mode.

These additional lines are useful for diagnostics, but the key status is that
all three modes have `mismatching groups: 0`.

## Additional Curation Checks

The item README says that during curation all three modes also passed with:

```text
max word length: 5
largest generator index: 3
```

Commands:

```text
python code/check_type_c_grothendieck.py --mode basic --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strong --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strongest --length 5 --largest 3
```

Recorded result:

```text
85 matching groups
0 mismatching groups
```

for each of the three modes.

## Reproducibility Commands

Run all curated default checks:

```text
python code/check_type_c_grothendieck.py
```

Run a single mode:

```text
python code/check_type_c_grothendieck.py --mode basic --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strong --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strongest --length 5 --largest 3
```

Run all modes with explicit default parameters:

```text
python code/check_type_c_grothendieck.py --mode all --length 4 --largest 3
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

The current explanation is accurate and appropriately cautious:

- defines `GC_\omega` by signed factorizations;
- gives the ordered signed alphabet and the role of `s_0`;
- states the conjectural `GQ` expansion;
- states the stronger `GR` model formulation for `GC_\omega^+`;
- separates the basic, strong, and peakset-preserving checked levels;
- says the peakset-preserving level would imply the positive `GQ` expansion;
- says the computations are finite evidence and regression checks, not proofs.

Possible rewrite improvements:

1. Put the conjectural status in the first paragraph.
2. Keep the three checked levels visually separate.
3. Explain that the strongest check compares peakset multisets, not an
   explicit bijection.
4. Keep the curation/default-parameter explanation: source defaults were
   larger, curated defaults are smaller for quick reproducibility.
5. Avoid expanding the entire source-code machinery unless the rewrite is
   intended as a code guide.

## Suggested Rewrite Structure

1. **Purpose and status.**
   State that this is a conjectural type C Grothendieck hierarchy with bounded
   checks.

2. **Objects.**
   Define signed permutations, signed factorizations, `GC_\omega`, `GQ`, and
   the conjectural type C unimodal Hecke tableaux `T_\omega`.

3. **Conjectural expansions.**
   State the `GQ` expansion and the stronger `GR` formulation.

4. **Three finite comparisons.**
   Present basic, strong, and peakset-preserving levels separately.

5. **Checker.**
   Identify the combined curated checker, source scripts, default parameters,
   and expected output.

6. **Limitations.**
   Say the computations are bounded evidence, do not construct bijections, and
   do not prove the conjectures.

## Things Not To Say

Avoid these mistakes:

- Do not say the `GQ` expansion is proved.
- Do not say the `GR` formulation is proved.
- Do not say the code constructs the conjectural bijections.
- Do not treat finite matching counts as a proof.
- Do not merge the three checked levels into one statement; they have
  different restrictions and implications.
- Do not omit that the peakset-preserving level is stronger and would imply
  the `GQ` positivity statement.
- Do not imply the curated default parameters are the original source
  defaults.
- Do not describe the strongest mode as a count-only check; it compares
  peakset data.

## Minimal Source-Backed Claims

The writing agent may safely state:

- The item curates a conjectural type C Grothendieck hierarchy from the source
  repository.
- The source files are `c-grothendieck.py`, `c-grothendieck-strong.py`,
  `c-grothendieck-strongest.py`, and `c-grothendieck-note.tex`.
- `GC_\omega` is defined by signed factorizations of Hecke words.
- The target is a positive `GQ` expansion indexed by conjectural type C
  unimodal Hecke tableaux.
- The source note also states a stronger `GR` formulation for `GC_\omega^+`.
- The basic, strong, and peakset-preserving versions are all conjectural.
- The default checker uses max word length `4` and generator indices `0..3`.
- In the default run, all three modes have `53` matching grouped signed
  permutations and `0` mismatching groups.
- Length-`5`, largest-`3` checks passed for all three modes during curation
  with `85` matching groups and `0` mismatching groups.

## Minimum Correct Final Message For The Rewrite

If the rewrite is successful, a reader should come away with this summary:

This item records a conjectural hierarchy for type C stable Grothendieck
polynomials.  The predicted formula expands `GC_w` positively in `GQ`
functions indexed by conjectural type C unimodal Hecke tableaux, and the source
note gives a stronger `GR` formulation for `GC_w^+`.  The code packages three
bounded finite comparisons: the basic count, the strong count with adjacent
and box restrictions, and the peakset-preserving comparison that would imply
the `GQ` positivity statement.  The default run checks length at most `4` and
generators `0..3`; all three modes pass with `53` matching groups and no
mismatches.  These checks are finite evidence, not proofs of the conjectures.
