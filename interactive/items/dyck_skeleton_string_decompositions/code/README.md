# Code

Code supporting skeleton-string decompositions.

- `check_r1mod_skeleton_strings.py` checks finite instances of the conjectural
  `r=tau*s+1`, `tau>1` rational special-skeleton formula.  It also checks the
  current East3/East5 partial lower-half string map, but only certifies a full
  map decomposition on defect layers where no `unsupported_level_7` move is
  reached.  If level 7 is reached, the map status is `PARTIAL`, not `PASS`.
  These checks are evidence only, not proof.  The checker prunes
  normalized-word generation when an exact suffix score bound proves the defect
  range is unreachable; `generated_words` remains the full normalized
  search-space size, while `searched_leaf_words` is the number of complete
  words reached after pruning.
- `run_official_r1mod_checks.py` runs the official `tau>1` finite-check grid:
  `tau=2, s<=14`; `tau=3, s<=12`; `tau=4, s<=10`; and `tau=5, s<=9`.
  Cases with `s<=4` are run in formula-only mode.
- `check_lower_root_partitions.py` checks the lower-cutoff root indexing at
  `defc <= (s-2)*tau - 1`.  It compares special skeleton roots by
  `(deficit, area)` with partitions by `(size, length)`, where the partitions
  have largest part at most `s-2`.  Equivalently, after conjugating
  partitions, this is a statement about partitions of length at most `s-2`,
  but root area then matches the largest part of the conjugate partition rather
  than its length.
- `explore_general_label1_partition_objects.py` tests the analogous
  label-1-zero question for a general coprime slope `r/s`.  It computes the
  intrinsic low-defect range where all label-1-zero paths are weakly below the
  middle area, compares the `(defect, area)` fibers with ordinary partitions
  of largest part at most `s-2`, and reports the first mismatch.  This is an
  exploratory diagnostic for finding the extra restrictions needed outside
  the `r=tau*s+1` family.
- `check_nrcm_lower_half.py` explores whether the strict NRCM gives
  lower-half decompositions for rational slopes. It checks definedness,
  defect preservation, area increase, and injectivity on low-defect layers.
- `check_nrcm_domain.py` is the narrower diagnostic for the same strict NRCM:
  it only checks that NRCM is defined on every below-midline source.  This is
  useful because the Dyck proof already establishes validity and defect
  preservation whenever strict NRCM is defined.
