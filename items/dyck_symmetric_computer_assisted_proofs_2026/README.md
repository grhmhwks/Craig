# Dyck Symmetric Computer-Assisted Proofs 2026

Status summary: Proof-supporting appendix computations for
arXiv:2605.13003; packaged checkers reproduce the successful finite
verifications.

## Summary

This item curates the finite proof-supporting computations from the 2026
preprint on Dyck symmetric functions. The code files are extracted from
Appendix A and Appendix B, with successful-output transcripts kept separately
as text files. The computations are presented as finite exhaustive steps inside
the paper's proofs, not as exploratory evidence.

## Status

Status: computation.

Verification: tied to the 2026 preprint and locally reproducible from the
packaged appendix listings.

Related paper: Graham Hawkes, "Dyck Symmetric Functions and Applications to
q,t-Catalan Polynomials", arXiv:2605.13003, posted May 13, 2026,
https://arxiv.org/abs/2605.13003.

## Provenance

Source repository: `Dyck`

Source paths:

- `../Dyck/paper/working_drafts/arxiv_submission.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/appendix_a_code.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_local_proofs.tex`
- `../Dyck/paper/working_drafts/draft_v3_sections/appendix_b_lemma_525.tex`

Transfer type: appendix listings are copied exactly from the paper source.

## Layers

Python layer: present and reproducible.

LaTeX layer: present.

HTML layer: present.

## Included Computations

- Appendix A core Dyck-sequence routines.
- Appendix A lower-half string-generation routine.
- Appendix B residual finite checker for the small local-proof range.
- Appendix B seven-window checker for the East7/West7 local move.
- Appendix B finite checkers used in the proof of Lemma 5.25.

## Reproducibility

Run the Appendix B checkers from `code/`:

```text
python run_appendix_listing.py appendix_b/01_residual_finite_check.py
python run_appendix_listing.py appendix_b/03_east7_west7_seven_window_checker.py
python run_appendix_listing.py appendix_b/05_lemma_525_limited_nonzero_checker.py
python run_appendix_listing.py appendix_b/07_lemma_525_prefix_checker.py
```

The successful runs end with `EverythingOkay = True`,
`SUCCESS: East7/West7 seven-window verification passed.`, or `status: PASS`,
as appropriate.

## Review And Routing

- Software/computation review: completed for packaging-level reproducibility;
  all packaged Appendix B checkers were run successfully on June 13, 2026.
- Mathematical accuracy review: the item mirrors finite checks from the
  preprint appendices. A future independent review should compare the curated
  explanation against the final published version if the preprint changes.
- Pedagogy/exposition review: the explanation file has been rewritten as an
  explanatory note rather than a transfer ledger. Future work should add
  examples or diagrams only if the item is expanded beyond appendix packaging.
