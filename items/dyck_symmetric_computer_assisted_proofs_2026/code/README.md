# Code

This directory contains the code listings from Appendix A and Appendix B of the
2026 Dyck symmetric functions preprint.

## Appendix A

`appendix_a/01_core_dyck_sequence_routines.py` is the core Dyck-sequence code
from Appendix A.

`appendix_a/02_make_strings.py` is the Appendix A routine that builds the
lower-half string decomposition from the core routines.

These two files are appendix listings. They are kept here because they appear
in Appendix A.

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
one of those listings without editing it, use:

```text
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
```
