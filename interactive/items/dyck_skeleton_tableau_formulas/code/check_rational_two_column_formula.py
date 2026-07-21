"""Finite checks for the rational two-column skeleton/tableau formula.

Inputs are rational step values ``t`` and length values ``n``.  For each
requested pair with ``t != 1``, the checker compares:

* direct normalized rational Dyck paths of length ``n``;
* the Type 4 skeleton/tableau formula side, summed over rational
  ``m``-skeletons and at-most-two-column rational Dyck tableaux.

Both sides are grouped by ``(area, dinv)`` before comparison.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from math import comb
from typing import Iterable, Sequence


Word = tuple[int, ...]
Shape = tuple[int, ...]
Tableau = tuple[tuple[int, ...], ...]
PairTable = list[list[int]]


@dataclass(frozen=True, slots=True)
class SequenceData:
    sequence: Word
    area: int
    dinv: int
    endpoint: int
    max_value: int
    is_skeleton: bool


@dataclass(frozen=True, slots=True)
class TableauData:
    row_word: Word
    area: int
    dinv: int


@dataclass(frozen=True, slots=True)
class AggregatedTableauData:
    counts: Word
    area: int
    dinv: int
    multiplicity: int


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def pair_dinv_python(left: int, right: int, step: int) -> int:
    if left <= right:
        contribution = left + step - right
    else:
        contribution = right + 1 + step - left
    if contribution > 0:
        return contribution
    return 0


def rational_dinv_python(sequence: Word, step: int) -> int:
    total = 0
    for left_index in range(len(sequence)):
        left = sequence[left_index]
        for right in sequence[left_index + 1 :]:
            if left <= right:
                contribution = left + step - right
            else:
                contribution = right + 1 + step - left
            if contribution > 0:
                total += contribution
    return total


def has_nonfinal_rational_extractable_python(sequence: Word, step: int) -> bool:
    for index, value in enumerate(sequence[:-1]):
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = 0
        for prior in sequence[:index]:
            if lower <= prior <= value - 1:
                prior_window_count += 1
                if prior_window_count > 1:
                    break
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(sequence) and sequence[index + 1] > sequence[index - 1] + step:
            continue
        return True
    return False


def value_counts(values: Word) -> Word:
    if not values:
        return ()
    counts = [0] * (max(values) + 1)
    for value in values:
        counts[value] += 1
    return tuple(counts)


def build_pair_dinv_table(max_value: int, *, step: int) -> PairTable:
    return [
        [pair_dinv_python(left, right, step) for right in range(max_value + 1)]
        for left in range(max_value + 1)
    ]


def dinv_increment_from_table(prefix: Sequence[int], value: int, pair_table: PairTable) -> int:
    total = 0
    for left in prefix:
        total += pair_table[left][value]
    return total


def cross_dinv_counts_from_table(left_counts: Word, right_counts: Word, pair_table: PairTable) -> int:
    total = 0
    for left, left_multiplicity in enumerate(left_counts):
        if left_multiplicity == 0:
            continue
        row = pair_table[left]
        for right, right_multiplicity in enumerate(right_counts):
            if right_multiplicity:
                total += left_multiplicity * right_multiplicity * row[right]
    return total


def parse_int_list(text: str) -> list[int]:
    values: list[int] = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        values.append(int(part))
    require(values, "expected a comma-separated list of integers")
    return values


def rational_dinv(sequence: Sequence[int], *, step: int) -> int:
    return rational_dinv_python(tuple(sequence), step)


def is_rational_affine_dyck(sequence: Sequence[int], *, step: int) -> bool:
    return all(sequence[index + 1] <= sequence[index] + step for index in range(len(sequence) - 1))


def is_rational_dual_dyck(sequence: Sequence[int], *, step: int) -> bool:
    return all(sequence[index + 1] > sequence[index] + step for index in range(len(sequence) - 1))


def generate_rational_dyck_sequences(length: int, *, step: int) -> Iterable[Word]:
    require(length > 0, "length must be positive")
    require(step >= 0, "t must be non-negative")

    def rec(prefix: list[int]) -> Iterable[Word]:
        if len(prefix) == length:
            yield tuple(prefix)
            return
        previous = prefix[-1]
        for value in range(previous + step + 1):
            prefix.append(value)
            yield from rec(prefix)
            prefix.pop()

    yield from rec([0])


def is_normalized_rational_dyck_sequence(sequence: Sequence[int], *, step: int) -> bool:
    values = tuple(sequence)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and is_rational_affine_dyck(values, step=step)
    )


def find_rational_extractable_position(
    sequence: Sequence[int],
    *,
    step: int,
    include_final: bool,
) -> int | None:
    values = tuple(sequence)
    require(is_normalized_rational_dyck_sequence(values, step=step), "sequence must be normalized rational Dyck")
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        lower = max(0, value - step)
        prior_window_count = sum(1 for prior in values[:index] if lower <= prior <= value - 1)
        if prior_window_count != 1:
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + step:
            continue
        return index
    return None


def is_rational_m_skeleton(sequence: Sequence[int], *, step: int, ambient: int | None = None) -> bool:
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    endpoint = values[-1] if ambient is None else ambient
    return (
        endpoint >= 0
        and max(values) == endpoint
        and values[-1] == endpoint
        and find_rational_extractable_position(values, step=step, include_final=False) is None
    )


def pair_dinv(left: int, right: int, *, step: int) -> int:
    return pair_dinv_python(left, right, step)


def has_nonfinal_rational_extractable(sequence: Word, *, step: int) -> bool:
    """Fast extractable test for already-generated normalized Dyck sequences."""

    return has_nonfinal_rational_extractable_python(sequence, step)


def is_rational_m_skeleton_generated(sequence: Word, *, step: int, max_value: int | None = None) -> bool:
    """Check skeleton status for a sequence known to be normalized rational Dyck."""

    endpoint = sequence[-1]
    if max_value is None:
        max_value = max(sequence)
    if max_value != endpoint:
        return False
    return not has_nonfinal_rational_extractable_python(sequence, step)


def generate_rational_dyck_sequence_data(
    length: int,
    *,
    step: int,
    pair_table: PairTable | None = None,
) -> list[SequenceData]:
    """Generate normalized rational Dyck paths with area/dinv cached."""

    require(length > 0, "length must be positive")
    require(step >= 0, "t must be non-negative")
    return sequence_data_by_length(length, step=step, pair_table=pair_table)[length]


def sequence_data_by_length(
    max_length: int,
    *,
    step: int,
    pair_table: PairTable | None = None,
) -> dict[int, list[SequenceData]]:
    require(max_length > 0, "max length must be positive")
    require(step >= 0, "t must be non-negative")
    if pair_table is None:
        pair_table = build_pair_dinv_table(step * (max_length - 1), step=step)

    base = SequenceData((0,), 0, 0, 0, 0, True)
    by_length: dict[int, list[SequenceData]] = {1: [base]}
    previous_level = [base]
    for length in range(2, max_length + 1):
        current_level: list[SequenceData] = []
        append_current = current_level.append
        for data in previous_level:
            prefix = data.sequence
            for value in range(data.endpoint + step + 1):
                dinv_increment_value = dinv_increment_from_table(prefix, value, pair_table)
                sequence = prefix + (value,)
                max_value = data.max_value if data.max_value >= value else value
                is_skeleton = (
                    max_value == value
                    and not has_nonfinal_rational_extractable_python(sequence, step)
                )
                append_current(
                    SequenceData(
                        sequence,
                        data.area + value,
                        data.dinv + dinv_increment_value,
                        value,
                        max_value,
                        is_skeleton,
                    )
                )
        by_length[length] = current_level
        previous_level = current_level
    return by_length


def generate_direct_coefficients_and_skeletons(
    max_length: int,
    *,
    step: int,
    pair_table: PairTable,
    requested_lengths: set[int],
) -> tuple[dict[int, Counter[tuple[int, int]]], dict[int, list[SequenceData]]]:
    require(max_length > 0, "max length must be positive")
    direct_by_length = {length: Counter() for length in requested_lengths}
    skeletons_by_length: dict[int, list[SequenceData]] = defaultdict(list)
    prefix = [0]

    def rec(area: int, dinv: int, max_value: int) -> None:
        length = len(prefix)
        endpoint = prefix[-1]
        if length in direct_by_length:
            direct_by_length[length][(area, dinv)] += 1

        if max_value == endpoint:
            sequence = tuple(prefix)
            if not has_nonfinal_rational_extractable_python(sequence, step):
                skeletons_by_length[length].append(
                    SequenceData(sequence, area, dinv, endpoint, max_value, True)
                )

        if length == max_length:
            return

        for value in range(endpoint + step + 1):
            dinv_increment_value = dinv_increment_from_table(prefix, value, pair_table)
            prefix.append(value)
            rec(area + value, dinv + dinv_increment_value, max_value if max_value >= value else value)
            prefix.pop()

    rec(0, 0, 0)
    return direct_by_length, skeletons_by_length


def is_partition_shape(shape: Sequence[int]) -> bool:
    return all(part > 0 for part in shape) and all(shape[index] >= shape[index + 1] for index in range(len(shape) - 1))


def conjugate_partition(shape: Shape) -> Shape:
    if shape == ():
        return ()
    require(is_partition_shape(shape), "shape must be a partition")
    return tuple(sum(1 for part in shape if part >= column) for column in range(1, shape[0] + 1))


def at_most_two_column_shapes(total_size: int) -> list[Shape]:
    require(total_size >= 0, "tableau size must be non-negative")
    if total_size == 0:
        return [()]
    out: list[Shape] = []
    for two_cell_rows in range(total_size // 2, -1, -1):
        one_cell_rows = total_size - 2 * two_cell_rows
        out.append((2,) * two_cell_rows + (1,) * one_cell_rows)
    return out


def rational_row_reading_word(tableau: Sequence[Sequence[int]]) -> Word:
    return tuple(value for row in reversed(tableau) for value in row)


def enumerate_bounded_rational_dyck_tableaux(
    shape: Shape,
    *,
    step: int,
    max_entry: int,
) -> Iterable[Tableau]:
    if shape == ():
        yield ()
        return
    if max_entry < 0:
        return
    require(is_partition_shape(shape), "shape must be a partition")

    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape) and col < shape[row + 1] and value > rows[row + 1][col] + step:
            return False
        if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int) -> Iterable[Tableau]:
        if cell_index == len(cells):
            yield tuple(tuple(row) for row in rows)
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            rows[row][col] = value
            yield from rec(cell_index + 1)
            rows[row][col] = 0

    yield from rec(0)


def enumerate_bounded_rational_dyck_tableau_data(
    shape: Shape,
    *,
    step: int,
    max_entry: int,
    pair_table: PairTable,
) -> Iterable[TableauData]:
    """Enumerate bounded rational Dyck tableaux with cached row-word statistics."""

    if shape == ():
        yield TableauData(row_word=(), area=0, dinv=0)
        return
    if max_entry < 0:
        return
    require(is_partition_shape(shape), "shape must be a partition")

    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
    row_word: list[int] = []

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape) and col < shape[row + 1] and value > rows[row + 1][col] + step:
            return False
        if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int, area: int, dinv: int) -> Iterable[TableauData]:
        if cell_index == len(cells):
            yield TableauData(row_word=tuple(row_word), area=area, dinv=dinv)
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            dinv_increment = dinv_increment_from_table(row_word, value, pair_table)
            rows[row][col] = value
            row_word.append(value)
            yield from rec(cell_index + 1, area + value, dinv + dinv_increment)
            row_word.pop()
            rows[row][col] = 0

    yield from rec(0, 0, 0)


def aggregate_tableau_data(tableaux: Iterable[TableauData]) -> list[AggregatedTableauData]:
    grouped: Counter[tuple[Word, int, int]] = Counter()
    for tableau in tableaux:
        grouped[(value_counts(tableau.row_word), tableau.area, tableau.dinv)] += 1
    return [
        AggregatedTableauData(counts=counts, area=area, dinv=dinv, multiplicity=multiplicity)
        for (counts, area, dinv), multiplicity in grouped.items()
    ]


def enumerate_ssyt_weights(shape: Shape, *, alphabet_size: int) -> Counter[tuple[int, ...]]:
    """Return the Schur monomial expansion by SSYT enumeration."""

    require(alphabet_size > 0, "alphabet size must be positive")
    if shape == ():
        return Counter({(0,) * alphabet_size: 1})
    require(is_partition_shape(shape), "shape must be a partition")
    rows = [[0 for _ in range(length)] for length in shape]
    cells = [(row, col) for row, length in enumerate(shape) for col in range(length)]
    weights: Counter[tuple[int, ...]] = Counter()

    def rec(cell_index: int, counts: list[int]) -> None:
        if cell_index == len(cells):
            weights[tuple(counts)] += 1
            return
        row, col = cells[cell_index]
        lower = 1
        if col > 0:
            lower = max(lower, rows[row][col - 1])
        if row > 0 and col < shape[row - 1]:
            lower = max(lower, rows[row - 1][col] + 1)
        for value in range(lower, alphabet_size + 1):
            rows[row][col] = value
            counts[value - 1] += 1
            rec(cell_index + 1, counts)
            counts[value - 1] -= 1
            rows[row][col] = 0

    rec(0, [0] * alphabet_size)
    return weights


def direct_coefficients(sequence_data: list[SequenceData]) -> Counter[tuple[int, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    for data in sequence_data:
        coeffs[(data.area, data.dinv)] += 1
    return coeffs


def type4_formula_coefficients(
    length: int,
    *,
    step: int,
    skeletons_by_length: dict[int, list[SequenceData]],
    pair_table: PairTable,
) -> tuple[Counter[tuple[int, int]], dict[str, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    counts = {
        "skeletons": 0,
        "tableaux": 0,
        "skeleton_tableau_pairs": 0,
        "schur_monomial_terms": 0,
    }
    schur_cache: dict[Shape, Counter[tuple[int, int]]] = {}
    tableau_cache: dict[tuple[Shape, int], list[AggregatedTableauData]] = {}

    for skeleton_length in range(1, length + 1):
        tableau_size = length - skeleton_length
        skeletons = skeletons_by_length.get(skeleton_length, [])
        counts["skeletons"] += len(skeletons)
        if not skeletons:
            continue
        skeletons_by_endpoint: dict[int, list[SequenceData]] = defaultdict(list)
        for skeleton_data in skeletons:
            skeletons_by_endpoint[skeleton_data.endpoint].append(skeleton_data)
        skeleton_counts: dict[Word, Word] = {
            skeleton_data.sequence: value_counts(skeleton_data.sequence)
            for skeleton_data in skeletons
        }

        for shape in at_most_two_column_shapes(tableau_size):
            size = sum(shape)
            schur_shape = conjugate_partition(shape)
            if schur_shape not in schur_cache:
                schur_cache[schur_shape] = enumerate_ssyt_weights(schur_shape, alphabet_size=2)
            schur_terms = list(schur_cache[schur_shape].items())

            for ambient, skeleton_group in skeletons_by_endpoint.items():
                cache_key = (shape, ambient)
                if cache_key not in tableau_cache:
                    tableau_cache[cache_key] = aggregate_tableau_data(
                        enumerate_bounded_rational_dyck_tableau_data(
                            shape=shape,
                            step=step,
                            max_entry=ambient - 1,
                            pair_table=pair_table,
                        ),
                    )
                tableaux = tableau_cache[cache_key]
                tableau_multiplicity_total = sum(tableau.multiplicity for tableau in tableaux)
                counts["tableaux"] += tableau_multiplicity_total * len(skeleton_group)
                counts["skeleton_tableau_pairs"] += tableau_multiplicity_total * len(skeleton_group)

                for skeleton_data in skeleton_group:
                    skeleton_count_vector = skeleton_counts[skeleton_data.sequence]
                    for tableau_data in tableaux:
                        if tableau_data.counts:
                            cross_dinv_value = cross_dinv_counts_from_table(
                                skeleton_count_vector,
                                tableau_data.counts,
                                pair_table,
                            )
                        else:
                            cross_dinv_value = 0
                        base_area = skeleton_data.area + tableau_data.area
                        base_dinv = skeleton_data.dinv + tableau_data.dinv + cross_dinv_value
                        for (q_power, t_power), multiplicity in schur_terms:
                            contribution = multiplicity * tableau_data.multiplicity
                            coeffs[(base_area + q_power, base_dinv - size + t_power)] += contribution
                            counts["schur_monomial_terms"] += contribution
    return coeffs, counts


def compare_case(
    *,
    step: int,
    length: int,
    direct: Counter[tuple[int, int]],
    skeletons_by_length: dict[int, list[SequenceData]],
    pair_table: PairTable,
) -> dict[str, int | float]:
    case_start = time.perf_counter()
    formula, formula_counts = type4_formula_coefficients(
        length,
        step=step,
        skeletons_by_length=skeletons_by_length,
        pair_table=pair_table,
    )
    mismatches = [
        (key, direct[key], formula[key])
        for key in sorted(set(direct) | set(formula))
        if direct[key] != formula[key]
    ]
    require(not mismatches, f"coefficient mismatch for t={step}, n={length}: {mismatches[:10]}")
    elapsed = time.perf_counter() - case_start
    return {
        "direct_paths": sum(direct.values()),
        "direct_terms": len(direct),
        "formula_terms": len(formula),
        "coefficient_keys": len(set(direct) | set(formula)),
        "skeletons": formula_counts["skeletons"],
        "tableaux": formula_counts["tableaux"],
        "skeleton_tableau_pairs": formula_counts["skeleton_tableau_pairs"],
        "schur_monomial_terms": formula_counts["schur_monomial_terms"],
        "elapsed_seconds": elapsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t-values", required=True, help="Comma-separated rational step values t.")
    parser.add_argument("--n-values", required=True, help="Comma-separated length values n, i.e. rational s-values.")
    args = parser.parse_args()

    steps = parse_int_list(args.t_values)
    lengths = parse_int_list(args.n_values)
    start = time.perf_counter()
    compared: dict[tuple[int, int], dict[str, int | float]] = {}
    skipped: list[tuple[int, int]] = []

    require(all(step >= 0 for step in steps), "all t-values must be non-negative")
    require(all(length > 0 for length in lengths), "all n-values must be positive")
    require(at_most_two_column_shapes(5) == [(2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)], "shape smoke check failed")
    require(is_rational_m_skeleton((0, 2), step=2, ambient=2), "skeleton smoke check failed")
    require(rational_dinv((0, 1, 0), step=2) == 5, "dinv smoke check failed")
    require(comb(3, 2) == 3, "math smoke check failed")

    for step in steps:
        if step == 1:
            for length in lengths:
                skipped.append((step, length))
            continue
        pair_table = build_pair_dinv_table(step * (max(lengths) - 1), step=step)
        direct_by_length, skeletons_by_length = generate_direct_coefficients_and_skeletons(
            max(lengths),
            step=step,
            pair_table=pair_table,
            requested_lengths=set(lengths),
        )
        for length in lengths:
            case_result = compare_case(
                step=step,
                length=length,
                direct=direct_by_length[length],
                skeletons_by_length=skeletons_by_length,
                pair_table=pair_table,
            )
            compared[(step, length)] = case_result
            print(
                f"  t={step}, n={length}: paths={case_result['direct_paths']}, "
                f"keys={case_result['coefficient_keys']}, skeletons={case_result['skeletons']}, "
                f"tableaux={case_result['tableaux']}, elapsed={case_result['elapsed_seconds']:.3f}s",
                flush=True,
            )

    require(compared, "no non-t=1 cases were checked")
    print("rational two-column skeleton/tableau formula check")
    print("  convention: r = n*t + 1; n is the rational s-value / path length")
    print(f"  compared cases: {sorted(compared)}")
    print(f"  skipped t=1 cases: {skipped}")
    print(f"  counts: {compared}")
    print(f"  elapsed: {time.perf_counter() - start:.3f}s")
    print("  all requested finite checks passed")


if __name__ == "__main__":
    main()
