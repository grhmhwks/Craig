# Code

`qt_assisted_2024.py` is a curated port of
`Conjectures-and-Computations/qt-catalan/qt-assisted.py`.

Run from the `Combinatorics` directory:

```powershell
python items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py
```

Or from the repository root:

```powershell
python Combinatorics\items\qt_catalan_computer_assisted_proofs_2024\code\qt_assisted_2024.py
```

The default run preserves the source parameters:

- `max_m = 20`
- `dstar = 20`

It generates all source-relevant position-coordinate `m`-Dyck path records,
checks the Lemma 2 string-bound condition, and checks the Lemma 3 monomial
multiset identity for every generated `(m, ell)` layer.

Expected default summary:

```text
generated_records: 5692942
lemma2_status: PASS
lemma2_failures: 0
lemma3_status: PASS
lemma3_layers_checked: 106
lemma3_failures: 0
status: PASS
```

The full default run took about 57 seconds in the current workspace.
