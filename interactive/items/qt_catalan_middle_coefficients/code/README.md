# Code

`check_flat_middle_coefficients.py` is a self-contained bounded checker for
the classical flat-middle coefficient statement.

Default command:

```bash
python code/check_flat_middle_coefficients.py
```

From this item directory, the default run checks `n=4..8`.  For each checked
`n`, it builds the direct coefficient dictionary for
`C_n(q,t)=sum_D q^area(D)t^dinv(D)`, counts special Dyck skeletons by deficit,
and verifies that every coefficient in the middle band

```text
q^j t^(M-d-j),   d <= j <= M-2d,   0 <= d <= 2n-8
```

equals the corresponding special-skeleton count.

Useful options:

```bash
python code/check_flat_middle_coefficients.py --n-min 4 --n-max 8
python code/check_flat_middle_coefficients.py --representative-bands 3
```

The file `flat_middle_coefficients_default_summary.txt` records the default
summary.  The check is finite evidence and a regression guard; it is not a
proof of the theorem or of the larger flat-middle conjecture.
