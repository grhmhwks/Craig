"""Small trace for the classical dual Dyck insertion algorithm."""

from __future__ import annotations

from paper_algorithms import is_dyck_tableau, rowsert, tabsert


def main() -> None:
    row = [0, 3, 6]
    inserted = [1, 4]
    row_steps = []
    evicted, new_row = rowsert(row, inserted, trace=row_steps)

    print("rowsert example")
    print(f"  row: {row}")
    print(f"  inserted row: {inserted}")
    print(f"  evicted row: {evicted}")
    print(f"  output row: {new_row}")
    for index, step in enumerate(row_steps, 1):
        print(f"  step {index}: {step}")

    tableau = [[0, 3], [1, 4]]
    inserted_row = [2, 5]
    output, traces = tabsert(tableau, inserted_row, trace=True)

    print()
    print("tabsert example")
    print(f"  tableau: {tableau}")
    print(f"  inserted row: {inserted_row}")
    print(f"  output: {output}")
    print(f"  valid Dyck tableau: {is_dyck_tableau(output)}")
    for trace in traces:
        print(f"  row {trace.row_index}: inserted {trace.inserted_row}, evicted {trace.evicted_row}")


if __name__ == "__main__":
    main()
