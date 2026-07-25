# Modulo-one decomposition and partition formula

This folder contains the proof package for the low-defect modulo-one formula
for normalized step-\(\tau\) Dyck words, with

\[
r=\tau s+1,\qquad
M=\tau\binom{s}{2},\qquad
B=\tau(s-2)-1.
\]

The goal is to decompose every defect layer \(0\le d\le B\) into strings on
which area increases by one and dinv decreases by one.  The roots are full
skeletons.  The final manuscript identifies those roots with words beginning
in two zeros and then with bounded partitions.

## Proof structure

The main dependency flow is

```text
east5_nonfailure.tex --\
                        +--> sgeq6_decomp.tex --\
west5_nonfailure.tex --/                        \
                                                  +--> mod1_formula.tex
sleq4_decomp.tex --------------------------------/
s5_decomp.tex ----------------------------------/

Hawkes's bounded-partition bijection -------------> mod1_formula.tex
known q,t symmetry -------------------------------> the full, reflected formula
```

The decomposition is split by length because the available local windows
change at small \(s\):

| Length | Decomposition file | Main issue |
|---|---|---|
| \(s=1,2\) | handled directly in `mod1_formula.tex` | \(B<0\), so the relevant defect range is empty |
| \(s=3,4\) | `sleq4_decomp.tex` | East3/West3 are automatic at \(s=3\); \(s=4\) has one boundary pair |
| \(s=5\) | `s5_decomp.tex` | failed West5 requires a saving/repacking boundary branch |
| \(s\ge6\) | `sgeq6_decomp.tex` | the uniform East5 and West5 algorithms apply |

## Files

### `mod1_formula.tex`

This is the main entry point and the only file that states the final formula
over the full range \(s\ge1\).

It does the following:

1. Treats \(s=1,2\) immediately: every word has defect zero while \(B<0\),
   so all low-defect sums are empty.
2. Proves that, in the range \(\defc_\tau\le B\), a word is a full skeleton
   exactly when it begins with \((0,0)\).
3. Uses Hawkes's bounded-partition bijection to identify the double-zero
   roots with partitions satisfying
   \[
   \lambda_1\le s-2,\qquad |\lambda|\le B,
   \]
   with root defect \(|\lambda|\) and root area \(\ell(\lambda)\).
4. Deduces the root-position estimate
   \[
   \area(S)\le\defc_\tau(S),
   \]
   which supplies the low-defect root-position input needed by the three
   decomposition manuscripts.
5. Selects the appropriate decomposition theorem according to \(s\), and
   uses \(q,t\)-symmetry to reflect the lower-half strings across the middle
   of each defect layer.
6. Gives the same answer in three equivalent forms, indexed by full
   skeletons, double-zero words, or bounded partitions.

The Hawkes bijection and the known \(q,t\)-symmetry are external inputs.
The East5 and West5 hypotheses appearing in the statement for \(s\ge6\)
are supplied by the two nonfailure manuscripts in this folder.

### `sleq4_decomp.tex`

This is the lower-half decomposition for \(s=3,4\).

- For \(s=3\), it proves directly that every East3 and West3 test reached by
  the algorithm succeeds.
- For \(s=4\), it classifies every failed level-three test by the single
  inverse boundary pair
  \[
  (0,p+1,a,c)\longleftrightarrow(0,a+1,c+1,p),
  \]
  where
  \[
  0\le p<a\le\tau-1,\qquad p+\tau<c\le a+\tau.
  \]
- It checks normalization, statistic change, totality, recognition, and
  invertibility for both the ordinary and boundary branches.

The theorem assumes that its full-skeleton roots lie in the lower half.
The required stronger estimate is proved in `mod1_formula.tex`.

### `s5_decomp.tex`

This is the standalone lower-half decomposition for \(s=5\).

At length five, ordinary East5 is available, but an ordinary West5 failure
can occur at the boundary.  The manuscript classifies that failure and adds
the saving/repacking pair needed to make UP and DOWN total and inverse.  In
particular, the inverse boundary operation is a special repacking operation,
not an otherwise invalid ordinary extraction.

The file proves:

- ordinary East5 totality in the relevant length-five UP branch;
- the complete failed-West5 boundary classification;
- normalization and the area/dinv ledger for saving and repacking;
- totality, statistic change, and branchwise invertibility;
- the resulting lower-half string decomposition.

As in the \(s=3,4\) file, the root-position assumption is discharged by
`mod1_formula.tex`.

### `sgeq6_decomp.tex`

This is the general modulo-one string decomposition for \(s\ge6\).

It develops the common structural lemmas, defines the UP and DOWN maps using
the full-skeleton, level-three, and level-five branches, and proves their
statistic change and invertibility.  It then obtains the root-indexed
generating function, using \(q,t\)-symmetry to reflect the lower half.

The proof isolates three inputs:

1. the special-skeleton position bound;
2. East5 nonfailure for strictly lower-half words;
3. West5 nonfailure for weakly lower-half nonskeletons.

For the defect range used in the final formula, the needed position bound is
proved in `mod1_formula.tex`.  The two nonfailure inputs are proved in
`east5_nonfailure.tex` and `west5_nonfailure.tex`.

### `east5_nonfailure.tex`

This proves a uniform obstruction to East5 failure for every \(\tau\ge2\)
and \(s\ge5\).  A failed East5 stage satisfying the normalization and defect
conditions must obey

\[
2\area+d>\tau\binom{s}{2},
\]

so it lies strictly above the fixed-defect midpoint.  Therefore an East5
stage reached from the strictly lower half in the required defect range
cannot fail.  In particular, this supplies the East5 input used by
`sgeq6_decomp.tex`.

### `west5_nonfailure.tex`

This proves West5 nonfailure for every \(\tau\ge2\) and \(s\ge6\).  Starting
from a weakly lower-half word of defect at most \(B\), if the successive
leftmost-extraction procedure reaches its level-five DOWN stage, the West5
test succeeds.

The proof separates the double-zero and positive-second-entry cases and
supplies the West5 input used by `sgeq6_decomp.tex`.

## Logical status of the final result

Within this folder, the local decomposition and nonfailure work is divided
into standalone manuscripts rather than combined with `mod1_formula.tex`.
Taken together, they establish the required string decompositions for every
nonempty range \(s\ge3\).  The final conversion to the bounded-partition
formula additionally uses:

- the known \(q,t\)-symmetry of
  \(\operatorname{Cat}_{\tau s+1,s}(q,t)\);
- Hawkes's partition--matrix--maximal-path bijection, cited in
  `mod1_formula.tex`.

Thus `mod1_formula.tex` should be read as the assembly theorem, while the
other five files supply its range-specific decomposition and local
nonfailure components.

## Recommended reading order

For the shortest route to the final statement:

1. `mod1_formula.tex`;
2. the decomposition file for the desired length range;
3. for \(s\ge6\), `east5_nonfailure.tex` and
   `west5_nonfailure.tex`.

For the local-map development in increasing order of complexity:

1. `sleq4_decomp.tex`;
2. `s5_decomp.tex`;
3. `sgeq6_decomp.tex`;
4. `east5_nonfailure.tex`;
5. `west5_nonfailure.tex`;
6. `mod1_formula.tex`.

## Compilation

Each TeX file is standalone; the files refer to one another by manuscript
name rather than by `\input` or cross-document labels.  From this directory,
compile any manuscript with two LaTeX passes, for example:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error mod1_formula.tex
pdflatex -interaction=nonstopmode -halt-on-error mod1_formula.tex
```

Because definitions of the statistics, extraction convention, and local
moves are repeated in the standalone manuscripts, any future change to those
definitions should be checked consistently across all six TeX files.
