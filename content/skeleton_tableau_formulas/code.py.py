#!/usr/bin/env python3
"""Readable finite checks for the rational two-column skeleton/tableau formula.

This file is intended for

    contents/dyck_skeleton_tableau_formulas/code.py

It checks the conjectural r = s*tau + 1 analogue of the classical two-column
skeleton/tableau formula for the q,t-Catalan polynomial.  The classical
``tau=1`` case is theorem-level material in the 2026 Dyck symmetric functions
paper; this script is mainly for the conjectural ``tau > 1`` cases.

For each requested pair (tau, s), the script computes two coefficient
Dictionaries indexed by ``(area, dinv)``:

1. the direct side, summing over all normalized tau-Dyck sequences of length s;
2. the formula side, summing over rational m-skeletons F, at-most-two-column
   rational Dyck tableaux P with entries in [0, m-1], and the two-variable
   Schur factor s_{lambda(P)'}(q,t).

The check passes exactly when these dictionaries agree.

Large verified boxes recorded for this item were checked using more optimized
code.  They are listed in RECORDED_OPTIMIZED_CHECKS below.  This file favors
clarity over speed and runs only small examples by default.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from typing import Iterable, Sequence

Word = tuple[int, ...]
Shape = tuple[int, ...]
Tableau = tuple[tuple[int, ...], ...]
CoeffDict = Counter[tuple[int, int]]


RECORDED_OPTIMIZED_CHECKS: dict[int, tuple[int, int]] = {
    # tau: inclusive length range 1..max_s already checked for this item.
    2: (1, 14),
    3: (1, 12),
    4: (1, 10),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_int_list(text: str) -> list[int]:
    values = [int(part.strip()) for part in text.split(",") if part.strip()]
    require(bool(values), "expected a nonempty comma-separated integer list")
    return values


def area(word: Sequence[int]) -> int:
    return sum(word)


def pair_dinv(left: int, right: int, tau: int) -> int:
    """The step-tau pair contribution used throughout this item."""

    if left <= right:
        return max(0, left + tau - right)
    return max(0, right + 1 + tau - left)


@lru_cache(maxsize=None)
def dinv_tau(word: Word, tau: int) -> int:
    values = tuple(word)
    return sum(
        pair_dinv(values[i], values[j], tau)
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )


def is_normalized_tau_dyck(word: Sequence[int], tau: int) -> bool:
    values = tuple(word)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and all(values[i + 1] <= values[i] + tau for i in range(len(values) - 1))
    )


def generate_tau_dyck_sequences(length: int, tau: int) -> Iterable[Word]:
    """Generate normalized tau-Dyck sequences of a fixed length."""

    require(length > 0, "length must be positive")
    require(tau >= 0, "tau must be nonnegative")

    prefix = [0]

    def rec() -> Iterable[Word]:
        if len(prefix) == length:
            yield tuple(prefix)
            return
        for value in range(prefix[-1] + tau + 1):
            prefix.append(value)
            yield from rec()
            prefix.pop()

    yield from rec()


def direct_coefficients(length: int, tau: int) -> CoeffDict:
    """Return direct coefficients from normalized tau-Dyck sequences."""

    coeffs: CoeffDict = Counter()
    for word in generate_tau_dyck_sequences(length, tau):
        coeffs[(area(word), dinv_tau(word, tau))] += 1
    return coeffs


def find_extractable_position(
    word: Sequence[int],
    tau: int,
    *,
    include_final: bool,
) -> int | None:
    """Find the leftmost rational extractable entry, if one exists.

    An entry e>0 is extractable if exactly one earlier entry lies in
    [max(0,e-tau), e), and deleting the entry preserves the tau-Dyck adjacent
    inequality.  If include_final is False, the final entry is ignored.
    """

    values = tuple(word)
    require(is_normalized_tau_dyck(values, tau), f"not a normalized tau-Dyck word: {values}")
    for index, value in enumerate(values):
        if value == 0:
            continue
        if not include_final and index == len(values) - 1:
            continue
        lower = max(0, value - tau)
        predecessor_count = sum(1 for prior in values[:index] if lower <= prior < value)
        if predecessor_count != 1:
            continue
        if 0 < index < len(values) - 1 and values[index + 1] > values[index - 1] + tau:
            continue
        return index
    return None


def is_rational_m_skeleton(word: Sequence[int], tau: int) -> bool:
    """Check the rational m-skeleton condition used in the formula."""

    values = tuple(word)
    if not is_normalized_tau_dyck(values, tau):
        return False
    endpoint = values[-1]
    return (
        max(values) == endpoint
        and find_extractable_position(values, tau, include_final=False) is None
    )


def rational_m_skeletons(length: int, tau: int) -> Iterable[Word]:
    for word in generate_tau_dyck_sequences(length, tau):
        if is_rational_m_skeleton(word, tau):
            yield word


def is_partition_shape(shape: Sequence[int]) -> bool:
    values = tuple(shape)
    return all(isinstance(part, int) and part > 0 for part in values) and all(
        values[i] >= values[i + 1] for i in range(len(values) - 1)
    )


def conjugate_partition(shape: Sequence[int]) -> Shape:
    values = tuple(shape)
    if values == ():
        return ()
    require(is_partition_shape(values), f"not a partition shape: {values}")
    return tuple(sum(1 for part in values if part >= column) for column in range(1, values[0] + 1))


def at_most_two_column_shapes(size: int) -> list[Shape]:
    """Partition shapes of total size with all row lengths at most two."""

    require(size >= 0, "size must be nonnegative")
    if size == 0:
        return [()]
    shapes: list[Shape] = []
    for two_cell_rows in range(size // 2, -1, -1):
        one_cell_rows = size - 2 * two_cell_rows
        shapes.append((2,) * two_cell_rows + (1,) * one_cell_rows)
    return shapes


def rational_row_reading_word(tableau: Sequence[Sequence[int]]) -> Word:
    """Read rows from bottom to top, and within each row left to right."""

    rows = tuple(tuple(row) for row in tableau)
    return tuple(entry for row in reversed(rows) for entry in row)


def enumerate_bounded_rational_dyck_tableaux(
    shape: Shape,
    *,
    tau: int,
    max_entry: int,
) -> Iterable[Tableau]:
    """Enumerate step-tau rational Dyck tableaux of fixed shape.

    Rows are stored top-to-bottom.  Each row is a dual tau-Dyck sequence:
    entries increase by more than tau from left to right.  Each column, read
    bottom-to-top, is affine: an upper entry is at most tau larger than the
    entry immediately below it.
    """

    if shape == ():
        yield ()
        return
    if max_entry < 0:
        return
    require(is_partition_shape(shape), f"not a partition shape: {shape}")

    rows = [[0 for _ in range(row_length)] for row_length in shape]
    cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]

    def valid_cell(row: int, col: int, value: int) -> bool:
        # Row condition: left-to-right dual tau-Dyck.
        if col > 0 and value <= rows[row][col - 1] + tau:
            return False
        # Column condition against the already-filled lower neighbor.
        if row + 1 < len(shape) and col < shape[row + 1]:
            if value > rows[row + 1][col] + tau:
                return False
        return True

    def rec(cell_index: int) -> Iterable[Tableau]:
        if cell_index == len(cells):
            yield tuple(tuple(row) for row in rows)
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if valid_cell(row, col, value):
                rows[row][col] = value
                yield from rec(cell_index + 1)
                rows[row][col] = 0

    yield from rec(0)


def enumerate_ssyt_weights(shape: Shape, alphabet_size: int = 2) -> Counter[tuple[int, int]]:
    """Expand s_shape(q,t) by enumerating SSYT over {1,2}."""

    require(alphabet_size == 2, "this checker only needs two-variable Schur functions")
    if shape == ():
        return Counter({(0, 0): 1})
    require(is_partition_shape(shape), f"not a partition shape: {shape}")

    rows = [[0 for _ in range(row_length)] for row_length in shape]
    cells = [(row, col) for row, row_length in enumerate(shape) for col in range(row_length)]
    weights: Counter[tuple[int, int]] = Counter()

    def rec(cell_index: int, counts: list[int]) -> None:
        if cell_index == len(cells):
            weights[(counts[0], counts[1])] += 1
            return
        row, col = cells[cell_index]
        lower = 1
        # Rows weakly increase.
        if col > 0:
            lower = max(lower, rows[row][col - 1])
        # Columns strictly increase top-to-bottom.
        if row > 0 and col < shape[row - 1]:
            lower = max(lower, rows[row - 1][col] + 1)
        for value in range(lower, alphabet_size + 1):
            rows[row][col] = value
            counts[value - 1] += 1
            rec(cell_index + 1, counts)
            counts[value - 1] -= 1
            rows[row][col] = 0

    rec(0, [0, 0])
    return weights


@lru_cache(maxsize=None)
def cached_schur_weights(shape: Shape) -> tuple[tuple[tuple[int, int], int], ...]:
    return tuple(sorted(enumerate_ssyt_weights(shape).items()))


def formula_coefficients(length: int, tau: int) -> CoeffDict:
    """Return the skeleton/tableau formula-side coefficients."""

    coeffs: CoeffDict = Counter()
    skeleton_cache = {
        skeleton_length: list(rational_m_skeletons(skeleton_length, tau))
        for skeleton_length in range(1, length + 1)
    }
    tableau_cache: dict[tuple[Shape, int], list[Tableau]] = {}

    for skeleton_length in range(1, length + 1):
        tableau_size = length - skeleton_length
        for skeleton in skeleton_cache[skeleton_length]:
            m_value = skeleton[-1]
            for shape in at_most_two_column_shapes(tableau_size):
                cache_key = (shape, m_value)
                if cache_key not in tableau_cache:
                    tableau_cache[cache_key] = list(
                        enumerate_bounded_rational_dyck_tableaux(
                            shape,
                            tau=tau,
                            max_entry=m_value - 1,
                        )
                    )
                schur_shape = conjugate_partition(shape)
                schur_terms = cached_schur_weights(schur_shape)
                for tableau in tableau_cache[cache_key]:
                    row_word = rational_row_reading_word(tableau)
                    base_word = skeleton + row_word
                    base_area = area(base_word)
                    base_dinv = dinv_tau(base_word, tau)
                    for (q_power, t_power), multiplicity in schur_terms:
                        coeffs[(base_area + q_power, base_dinv - tableau_size + t_power)] += multiplicity
    return coeffs


def compare_case(length: int, tau: int) -> dict[str, int]:
    """Compare direct and formula-side coefficient dictionaries."""

    direct = direct_coefficients(length, tau)
    formula = formula_coefficients(length, tau)
    mismatches = [
        (key, direct[key], formula[key])
        for key in sorted(set(direct) | set(formula))
        if direct[key] != formula[key]
    ]
    if mismatches:
        preview = "; ".join(f"{key}: direct={a}, formula={b}" for key, a, b in mismatches[:10])
        raise AssertionError(f"coefficient mismatch for tau={tau}, s={length}: {preview}")
    return {
        "tau": tau,
        "s": length,
        "direct_paths": sum(direct.values()),
        "coefficient_keys": len(direct),
        "formula_keys": len(formula),
    }


def print_recorded_checks() -> None:
    print("recorded optimized checks for this item:")
    for tau, (start, stop) in sorted(RECORDED_OPTIMIZED_CHECKS.items()):
        print(f"  tau={tau}: lengths {start} <= s <= {stop}")
    print("  These larger boxes are recorded as verified; this readable script does not run them by default.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tau-values",
        default="2",
        help="comma-separated step values tau; tau=1 is the proved classical case",
    )
    parser.add_argument(
        "--lengths",
        default="1,2,3,4,5",
        help="comma-separated lengths s to check",
    )
    parser.add_argument(
        "--include-classical",
        action="store_true",
        help="also run tau=1 if it appears in --tau-values; otherwise it is skipped",
    )
    parser.add_argument(
        "--show-recorded",
        action="store_true",
        help="print the recorded optimized verification boxes",
    )
    args = parser.parse_args()

    taus = parse_int_list(args.tau_values)
    lengths = parse_int_list(args.lengths)
    require(all(tau >= 0 for tau in taus), "tau-values must be nonnegative")
    require(all(length > 0 for length in lengths), "lengths must be positive")

    print("rational two-column skeleton/tableau formula check")
    print("  convention: r = s*tau + 1; coefficients use q^area t^dinv")
    for tau in taus:
        if tau == 1 and not args.include_classical:
            print("  tau=1: skipped by default because this is the classical theorem")
            continue
        for length in lengths:
            result = compare_case(length, tau)
            print(
                f"  PASS tau={tau}, s={length}: "
                f"paths={result['direct_paths']}, keys={result['coefficient_keys']}"
            )

    if args.show_recorded:
        print()
        print_recorded_checks()
    print("all requested checks passed")


if __name__ == "__main__":
    main()
