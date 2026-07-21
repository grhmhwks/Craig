# Code

`check_rational_qt_catalan_formula.py` is a curated port of
`Conjectures-and-Computations/qt-catalan/qt-conjecture.py`.

Run the source example from the `Combinatorics` directory:

```powershell
python items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py
```

Or from the repository root:

```powershell
python Combinatorics\items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py
```

Check several coprime cases:

```powershell
python Combinatorics\items\rational_qt_catalan_formula\code\check_rational_qt_catalan_formula.py --case 3/5 --case 5/8 --case 7/12
```

Expected default summary:

```text
case: r=7 n=12
closest_point: (2, 5)
generated_paths: 2652
all_terms: 2652
plus_terms: 2666
minus_terms: 14
status: PASS
overall_status: PASS
```

The checker is intended for `gcd(r,n)=1` and rejects non-coprime inputs.
