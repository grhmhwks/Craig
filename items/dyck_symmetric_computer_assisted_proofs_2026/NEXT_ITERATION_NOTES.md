# Next Iteration Notes

These notes record author feedback on the first attempt to build this item.

## Explanation File

The explanation file should be rewritten.

It should not record item status, transfer status, or review status. Those
belong in `README.md` and `item.yaml`.

It should give a short explanation of:

- the appendix lemmas proved in the 2026 preprint;
- what finite checks appear in Appendix A and Appendix B;
- why those finite checks are needed to complete the proofs of the lemmas.

Avoid unexplained paper-specific terminology. A reader likely does not know
what phrases such as "branch-prefix obligations" mean. Either explain the idea
plainly or avoid the phrase.

Do not put ordinary explanatory prose in italics.

## Code To Include

The code included in this item should be exactly the code that appears in
Appendix A and Appendix B of the 2026 preprint.

In addition, include code that computes the strings and returns them in a clean,
reader-friendly way.

The current copied standalone scripts are useful source references, but they
are not yet the desired final code layer for this item.
