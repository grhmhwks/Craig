# Code

This directory contains the code listings from Appendix A and Appendix B of the
2026 Dyck symmetric functions preprint.

## Purpose

These scripts package the finite computations used in the appendices of the
preprint. Appendix A contains reusable Dyck-sequence routines and string
generation code. Appendix B contains exhaustive finite checkers used in the
local well-definedness proofs for the skeleton string construction.

## Dependencies

Python 3 with the standard library only.

Run scripts with ordinary assertion checking enabled. Do not use Python's
optimized mode, because `assert` statements are part of the verification.

## Inputs

The checkers have no external data input. Each script enumerates its stated
finite domain internally.

## Outputs

Successful runs print count summaries and final success lines. The expected
successful-output transcripts for the Appendix B checkers are stored beside
the scripts as `.txt` files when the appendix includes such a transcript.

## Appendix A

`appendix_a/01_core_dyck_sequence_routines.py` is the core Dyck-sequence code
from Appendix A.

`appendix_a/02_make_strings.py` is the Appendix A routine that builds the
lower-half string decomposition from the core routines.

These two files are appendix listings. They are kept here because they appear
in Appendix A.

Command:

```text
python run_appendix_listing.py appendix_a/02_make_strings.py
```

The wrapper prepends the core routines before running this listing. This
routine returns the lower-half strings for requested parameters when called
from Python; it is included mainly as appendix code rather than as a command
line report.

## Appendix B

`appendix_b/01_residual_finite_check.py` is the finite checker for the small
residual range in the local well-definedness proof.

`appendix_b/03_east7_west7_seven_window_checker.py` is the finite checker for
the seven-entry East/West local move.

`appendix_b/05_lemma_525_limited_nonzero_checker.py` is the limited-nonzero
finite checker for Lemma 5.25.

`appendix_b/07_lemma_525_prefix_checker.py` is the finite checker for the two
prefix forms excluded in the proof of Lemma 5.25.

The `.txt` files in `appendix_b/` are the successful-output listings printed in
the appendix.

Some Appendix B listings rely on routines defined earlier in Appendix A. To run
the listings without editing them, use:

```text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
```

## Range Checked

`appendix_b/01_residual_finite_check.py` enumerates Dyck sequences of lengths
`4 <= n <= 7` satisfying the paper's deficit and area hypotheses for the
residual local-lemma branches.

`appendix_b/03_east7_west7_seven_window_checker.py` enumerates the finite
East7 and West7 seven-entry window domains and their bounded absolute children
after the paper's threshold reductions.

`appendix_b/05_lemma_525_limited_nonzero_checker.py` checks all Dyck sequences
with `4 <= n <= 13` and at most seven nonzero entries satisfying the fixed
deficit and area hypotheses.

`appendix_b/07_lemma_525_prefix_checker.py` checks the two excluded prefix
forms in the range `9 <= n <= 16`.

## Runtime

On the current local machine, each Appendix B checker completed in a few
seconds or less on June 13, 2026. Runtime may vary, but no external packages or
cached data are required.

## Interpretation

The computations are finite exhaustive verifications after the written proof
reduces the relevant obligations to bounded domains. They should be read as
proof-supporting appendix checks for those domains, not as broad experimental
evidence for statements outside the stated ranges.

## Limitations

The scripts verify exactly the finite obligations encoded in the appendix
listings. They do not independently reprove the symbolic reductions in the
paper, and they should be rechecked if the corresponding preprint statements,
definitions, or ranges change.
