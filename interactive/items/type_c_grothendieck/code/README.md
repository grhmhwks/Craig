# Code

`check_type_c_grothendieck.py` is a curated combined checker for the three
source scripts:

- `basic`: the original count comparison;
- `strong`: the count comparison with no adjacent equal Hecke letters and no
  consecutive entries in the same shifted set-valued tableau box;
- `strongest`: the peakset-preserving comparison.

Default command:

```bash
python code/check_type_c_grothendieck.py
```

The default run checks all three modes with max word length `4` and generator
indices `0..3`.

Useful options:

```bash
python code/check_type_c_grothendieck.py --mode basic --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strong --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode strongest --length 5 --largest 3
python code/check_type_c_grothendieck.py --mode all --length 4 --largest 3
```

The direct enumeration grows quickly.  The original source scripts used larger
defaults, including length `8`, largest generator `4` for the basic and strong
checks, and length `11`, largest generator `4` for the strongest check.

The file `type_c_grothendieck_default_summary.txt` records the curated default
summary.  These are bounded checks only; they do not prove the conjectures.
