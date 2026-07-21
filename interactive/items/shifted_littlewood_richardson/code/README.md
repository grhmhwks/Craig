# Code

`check_shifted_lr.py` is a curated combined checker for the source `GP` and
`GQ` shifted Littlewood-Richardson scripts.

Default command:

```bash
python code/check_shifted_lr.py
```

The default run checks both branches for:

```text
degree = 5
shape/skew = [3, 1]/[1]
num_vars = 3
```

The checker compares the direct homogeneous monomial expansion of the skew
function with the expansion reconstructed from the conjectural
Littlewood-Richardson rule.  For the `GQ` branch, the code follows the source
script by checking the related `GR` rule; the source README says this implies
the corresponding `GQ` expansion.

Useful options:

```bash
python code/check_shifted_lr.py --kind gp --degree 6 --shape 3,1 --skew 1 --num-vars 3
python code/check_shifted_lr.py --kind gq --degree 6 --shape 3,1 --skew 1 --num-vars 3
python code/check_shifted_lr.py --kind both --degree 5 --shape 4,2 --skew 2 --num-vars 3
```

The file `shifted_lr_default_summary.txt` records the default summary.  These
are bounded checks only; they do not prove either conjectural rule.
