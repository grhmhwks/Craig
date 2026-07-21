"""Finite helpers for the ``r = ms + 1`` rational Dyck generalization."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb
from typing import Iterable, Sequence

from .ssyt import Shape, SSYT, enumerate_ssyt, is_partition_shape, schur_polynomial_by_ssyt, ssyt_weight


SequenceWord = tuple[int, ...]
Tableau = tuple[tuple[int, ...], ...]
Weight = tuple[int, ...]


def _check_m(m: int) -> None:
    if not isinstance(m, int) or m < 0:
        raise ValueError("m must be a non-negative integer")


def rational_dinv(sequence: Sequence[int], *, m: int) -> int:
    """Return the rational dinv statistic for an integer sequence."""

    _check_m(m)
    values = tuple(sequence)
    total = 0
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            if left <= right:
                total += max(0, left + m - right)
            else:
                total += max(0, right + 1 + m - left)
    return total


def is_rational_affine_dyck(sequence: Sequence[int], *, m: int) -> bool:
    """Check ``x[i+1] <= x[i] + m``."""

    _check_m(m)
    values = tuple(sequence)
    return all(isinstance(value, int) for value in values) and all(
        values[index + 1] <= values[index] + m for index in range(len(values) - 1)
    )


def is_rational_dual_dyck(sequence: Sequence[int], *, m: int) -> bool:
    """Check ``x[i+1] > x[i] + m``."""

    _check_m(m)
    values = tuple(sequence)
    return all(isinstance(value, int) for value in values) and all(
        values[index + 1] > values[index] + m for index in range(len(values) - 1)
    )


def generate_rational_dyck_sequences(length: int, *, step: int) -> list[SequenceWord]:
    """Generate normalized ``step``-affine Dyck sequences of fixed length."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")

    out: list[SequenceWord] = []

    def rec(prefix: list[int]) -> None:
        if len(prefix) == length:
            out.append(tuple(prefix))
            return
        previous = prefix[-1]
        # Nonnegativity and the initial zero make this finite; the largest
        # possible next entry is obtained by taking the maximum allowed step.
        for value in range(previous + step + 1):
            prefix.append(value)
            rec(prefix)
            prefix.pop()

    rec([0])
    return out


def is_normalized_rational_dyck_sequence(sequence: Sequence[int], *, step: int) -> bool:
    """Check the normalized rational Dyck sequence convention."""

    _check_m(step)
    values = tuple(sequence)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and is_rational_affine_dyck(values, m=step)
    )


def find_rational_extractable_position(
    sequence: Sequence[int],
    *,
    step: int,
    include_final: bool = True,
) -> int | None:
    """Return the leftmost generalized extractable position, if any."""

    _check_m(step)
    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        raise ValueError("sequence must be a normalized rational Dyck sequence")
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
    """Check the generalized ``[0,m]`` skeleton condition."""

    _check_m(step)
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


def rational_max_total_degree(length: int, *, step: int) -> int:
    """Return the conjectural top total degree for ``r = length*step + 1``."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    return step * comb(length, 2)


def rational_deficit(sequence: Sequence[int], *, step: int) -> int:
    """Return ``M - area - dinv`` with ``M = step*binom(length, 2)``."""

    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        raise ValueError("sequence must be a normalized rational Dyck sequence")
    return rational_max_total_degree(len(values), step=step) - sum(values) - rational_dinv(values, m=step)


def excluded_rational_full_skeleton(length: int, *, step: int) -> SequenceWord:
    """Return ``(0,0,1,0,...,0,step)``."""

    _check_m(step)
    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    if length < 4:
        raise ValueError("the excluded skeleton is only defined for length at least 4")
    return (0, 0, 1) + (0,) * (length - 4) + (step,)


def is_rational_full_skeleton(sequence: Sequence[int], *, step: int) -> bool:
    """Check the generalized full skeleton condition."""

    values = tuple(sequence)
    if not is_normalized_rational_dyck_sequence(values, step=step):
        return False
    return find_rational_extractable_position(values, step=step, include_final=True) is None


def is_rational_special_skeleton(sequence: Sequence[int], *, step: int) -> bool:
    """Check full skeleton status, excluding ``(0,0,1,0,...,0,1)``."""

    values = tuple(sequence)
    if not is_rational_full_skeleton(values, step=step):
        return False
    if len(values) < 4:
        return True
    return values != excluded_rational_full_skeleton(len(values), step=step)


def unique_multiset_permutations(values: Iterable[int]) -> Iterable[SequenceWord]:
    """Yield distinct permutations of a finite multiset in lexicographic order."""

    counts = Counter(values)
    if any(not isinstance(value, int) for value in counts):
        raise ValueError("values must be integers")

    def rec(prefix: list[int], remaining: int) -> Iterable[SequenceWord]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for value in sorted(counts):
            if counts[value] == 0:
                continue
            counts[value] -= 1
            prefix.append(value)
            yield from rec(prefix, remaining - 1)
            prefix.pop()
            counts[value] += 1

    yield from rec([], sum(counts.values()))


def rational_affine_factorization_polynomial(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int,
    variable_count: int,
) -> Counter[Weight]:
    """Count affine factorizations by factor lengths.

    The output coefficient of ``(a0, ..., ak)`` counts ordered factorizations
    into ``variable_count`` possibly empty consecutive factors with lengths
    ``a0, ..., ak`` whose concatenation has the requested rational dinv.
    """

    _check_m(m)
    if not isinstance(target_dinv, int) or target_dinv < 0:
        raise ValueError("target_dinv must be a non-negative integer")
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    values_tuple = tuple(values)
    polynomial: Counter[Weight] = Counter()
    length = len(values_tuple)

    def cut_rec(start: int, factors_left: int, cuts: list[int], sequence: SequenceWord) -> None:
        if factors_left == 1:
            parts = cuts + [length]
            previous = 0
            factor_lengths: list[int] = []
            for stop in parts:
                factor = sequence[previous:stop]
                if not is_rational_affine_dyck(factor, m=m):
                    return
                factor_lengths.append(len(factor))
                previous = stop
            polynomial[tuple(factor_lengths)] += 1
            return
        for stop in range(start, length + 1):
            cut_rec(stop, factors_left - 1, cuts + [stop], sequence)

    for sequence in unique_multiset_permutations(values_tuple):
        if rational_dinv(sequence, m=m) == target_dinv:
            cut_rec(0, variable_count, [], sequence)
    return polynomial


def rational_dual_factorization_polynomial(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int,
    variable_count: int,
) -> Counter[Weight]:
    """Count dual factorizations by factor lengths."""

    _check_m(m)
    if not isinstance(target_dinv, int) or target_dinv < 0:
        raise ValueError("target_dinv must be a non-negative integer")
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    values_tuple = tuple(values)
    polynomial: Counter[Weight] = Counter()
    length = len(values_tuple)

    def cut_rec(start: int, factors_left: int, cuts: list[int], sequence: SequenceWord) -> None:
        if factors_left == 1:
            parts = cuts + [length]
            previous = 0
            factor_lengths: list[int] = []
            for stop in parts:
                factor = sequence[previous:stop]
                if not is_rational_dual_dyck(factor, m=m):
                    return
                factor_lengths.append(len(factor))
                previous = stop
            polynomial[tuple(factor_lengths)] += 1
            return
        for stop in range(start, length + 1):
            cut_rec(stop, factors_left - 1, cuts + [stop], sequence)

    for sequence in unique_multiset_permutations(values_tuple):
        if rational_dinv(sequence, m=m) == target_dinv:
            cut_rec(0, variable_count, [], sequence)
    return polynomial


def rational_row_reading_word(tableau: Sequence[Sequence[int]]) -> SequenceWord:
    """Read rows left-to-right, from bottom row to top row."""

    rows = tuple(tuple(row) for row in tableau)
    return tuple(value for row in reversed(rows) for value in row)


def rational_dyck_tableau_shape(tableau: Sequence[Sequence[int]]) -> Shape:
    return tuple(len(row) for row in tableau)


def is_rational_dyck_tableau(tableau: Sequence[Sequence[int]], *, m: int) -> bool:
    """Check the rational Dyck tableau conditions in top-to-bottom row order."""

    _check_m(m)
    rows = tuple(tuple(row) for row in tableau)
    shape = rational_dyck_tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    if any(not is_rational_dual_dyck(row, m=m) for row in rows):
        return False
    for row_index in range(len(rows) - 1):
        upper = rows[row_index]
        lower = rows[row_index + 1]
        for column in range(len(lower)):
            if upper[column] > lower[column] + m:
                return False
    return True


def enumerate_rational_dyck_tableaux(
    values: Iterable[int],
    *,
    m: int,
    target_dinv: int | None = None,
) -> list[Tableau]:
    """Enumerate rational Dyck tableaux with the requested multiset entries."""

    _check_m(m)
    values_tuple = tuple(values)
    if any(not isinstance(value, int) for value in values_tuple):
        raise ValueError("values must be integers")
    if target_dinv is not None and (not isinstance(target_dinv, int) or target_dinv < 0):
        raise ValueError("target_dinv must be a non-negative integer or None")

    out: list[Tableau] = []
    total_size = len(values_tuple)

    def partition_rec(remaining: int, max_part: int, prefix: list[int]) -> Iterable[Shape]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for part in range(min(remaining, max_part), 0, -1):
            prefix.append(part)
            yield from partition_rec(remaining - part, part, prefix)
            prefix.pop()

    for shape in partition_rec(total_size, total_size, []):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(length)] for length in shape]
        remaining = Counter(values_tuple)

        def valid_cell(row: int, col: int, value: int) -> bool:
            if col > 0 and value <= rows[row][col - 1] + m:
                return False
            if row + 1 < len(shape) and col < shape[row + 1]:
                if value > rows[row + 1][col] + m:
                    return False
            if row > 0 and col < shape[row - 1] and rows[row - 1][col] != 0:
                if rows[row - 1][col] > value + m:
                    return False
            return True

        def fill(cell_index: int) -> None:
            if cell_index == len(cells):
                tableau = tuple(tuple(row) for row in rows)
                if target_dinv is None or rational_dinv(rational_row_reading_word(tableau), m=m) == target_dinv:
                    out.append(tableau)
                return
            row, col = cells[cell_index]
            for value in sorted(remaining):
                if remaining[value] == 0 or not valid_cell(row, col, value):
                    continue
                rows[row][col] = value
                remaining[value] -= 1
                fill(cell_index + 1)
                remaining[value] += 1
                rows[row][col] = 0

        fill(0)
    return out


def shape_counts(tableaux: Iterable[Sequence[Sequence[int]]]) -> Counter[Shape]:
    return Counter(rational_dyck_tableau_shape(tableau) for tableau in tableaux)


def conjugate_partition(shape: Sequence[int]) -> Shape:
    shape_tuple = tuple(shape)
    if shape_tuple == ():
        return ()
    if not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition")
    return tuple(sum(1 for part in shape_tuple if part >= column) for column in range(1, shape_tuple[0] + 1))


def schur_sum_from_tableau_shapes(
    tableaux: Iterable[Sequence[Sequence[int]]],
    *,
    variable_count: int,
    conjugate_shapes: bool,
) -> Counter[Weight]:
    """Expand ``sum_P s_shape(P)`` or ``sum_P s_shape(P)'`` into monomials."""

    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")
    out: Counter[Weight] = Counter()
    for tableau in tableaux:
        shape = rational_dyck_tableau_shape(tableau)
        if conjugate_shapes:
            shape = conjugate_partition(shape)
        for weight, coefficient in schur_polynomial_by_ssyt(shape, alphabet_size=variable_count).items():
            out[weight] += coefficient
    return out


def partition_weights(total: int, *, max_parts: int) -> list[Weight]:
    if not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    if not isinstance(max_parts, int) or max_parts <= 0:
        raise ValueError("max_parts must be positive")
    out: list[Weight] = []

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if len(prefix) == max_parts:
            if remaining == 0:
                out.append(tuple(prefix))
            return
        slots_left = max_parts - len(prefix) - 1
        for part in range(min(remaining, max_part), -1, -1):
            prefix.append(part)
            rec(remaining - part, part, prefix)
            prefix.pop()

    rec(total, total, [])
    return out


def schur_expansion_from_monomial_symmetric(
    monomial_coefficients: Counter[Weight] | dict[Weight, int],
    *,
    variable_count: int,
) -> Counter[Shape]:
    """Convert a symmetric monomial dictionary to Schur coefficients.

    Keys are exponent partitions padded to ``variable_count`` parts, as in the
    monomial symmetric basis in that many variables.
    """

    if not monomial_coefficients:
        return Counter()
    if not isinstance(variable_count, int) or variable_count <= 0:
        raise ValueError("variable_count must be positive")

    normalized: Counter[Weight] = Counter()
    total: int | None = None
    for weight, coefficient in monomial_coefficients.items():
        weight_tuple = tuple(weight)
        if len(weight_tuple) != variable_count:
            raise ValueError("all weights must have length variable_count")
        if any(part < 0 for part in weight_tuple) or tuple(sorted(weight_tuple, reverse=True)) != weight_tuple:
            raise ValueError("weights must be partitions padded with zeros")
        if total is None:
            total = sum(weight_tuple)
        elif sum(weight_tuple) != total:
            raise ValueError("all weights must have the same total degree")
        normalized[weight_tuple] += coefficient

    assert total is not None
    partitions = partition_weights(total, max_parts=variable_count)
    remaining = {partition: Fraction(normalized.get(partition, 0)) for partition in partitions}
    coefficients: Counter[Shape] = Counter()

    for shape in partitions:
        shape_no_zeros = tuple(part for part in shape if part)
        if len(shape_no_zeros) > variable_count:
            continue
        schur_terms = Counter(
            ssyt_weight(tableau, alphabet_size=variable_count)
            for tableau in enumerate_ssyt(shape_no_zeros, alphabet_size=variable_count)
        )
        coefficient = remaining[shape]
        if coefficient:
            if coefficient.denominator != 1:
                raise ValueError(f"non-integral Schur coefficient for shape {shape}: {coefficient}")
            coefficients[shape_no_zeros] = int(coefficient)
        for weight, kostka in schur_terms.items():
            if weight in remaining:
                remaining[weight] -= coefficient * kostka

    if any(value != 0 for value in remaining.values()):
        raise ValueError(f"monomial coefficients were not fully converted: {remaining}")
    return coefficients


def at_most_two_column_shapes(total_size: int) -> list[Shape]:
    """Return partition shapes of ``total_size`` with at most two columns."""

    if not isinstance(total_size, int) or total_size < 0:
        raise ValueError("total_size must be a non-negative integer")
    if total_size == 0:
        return [()]
    out: list[Shape] = []
    for two_cell_rows in range(total_size // 2, -1, -1):
        one_cell_rows = total_size - 2 * two_cell_rows
        shape = (2,) * two_cell_rows + (1,) * one_cell_rows
        out.append(shape)
    return out


def enumerate_bounded_rational_dyck_tableaux(
    shape: Sequence[int],
    *,
    step: int,
    max_entry: int,
) -> list[Tableau]:
    """Enumerate rational Dyck tableaux of a fixed shape and entry interval.

    Rows are in top-to-bottom order, entries lie in ``[0,max_entry]``, rows are
    rational dual Dyck sequences, and columns read bottom-to-top are rational
    affine Dyck sequences.
    """

    _check_m(step)
    if not isinstance(max_entry, int):
        raise ValueError("max_entry must be an integer")
    shape_tuple = tuple(shape)
    if shape_tuple == ():
        return [()]
    if not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition")
    if max_entry < 0:
        return []

    rows = [[0 for _ in range(length)] for length in shape_tuple]
    cells = [(row, col) for row in range(len(shape_tuple) - 1, -1, -1) for col in range(shape_tuple[row])]
    out: list[Tableau] = []

    def valid_cell(row: int, col: int, value: int) -> bool:
        if col > 0 and value <= rows[row][col - 1] + step:
            return False
        if row + 1 < len(shape_tuple) and col < shape_tuple[row + 1]:
            if value > rows[row + 1][col] + step:
                return False
        if row > 0 and col < shape_tuple[row - 1] and rows[row - 1][col] != 0:
            if rows[row - 1][col] > value + step:
                return False
        return True

    def rec(cell_index: int) -> None:
        if cell_index == len(cells):
            out.append(tuple(tuple(row) for row in rows))
            return
        row, col = cells[cell_index]
        for value in range(max_entry + 1):
            if not valid_cell(row, col, value):
                continue
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = 0

    rec(0)
    return out


def rational_qt_catalan_direct_coefficients(length: int, *, step: int) -> Counter[tuple[int, int]]:
    """Direct ``q^area t^dinv`` coefficients from normalized rational Dyck words."""

    coeffs: Counter[tuple[int, int]] = Counter()
    for sequence in generate_rational_dyck_sequences(length, step=step):
        coeffs[(sum(sequence), rational_dinv(sequence, m=step))] += 1
    return coeffs


def rational_two_column_formula_coefficients(length: int, *, step: int) -> Counter[tuple[int, int]]:
    """Formula-side coefficients using rational skeletons and two-column tabs."""

    if not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    _check_m(step)

    coeffs: Counter[tuple[int, int]] = Counter()
    for skeleton_length in range(1, length + 1):
        tableau_size = length - skeleton_length
        for skeleton in generate_rational_dyck_sequences(skeleton_length, step=step):
            if not is_rational_m_skeleton(skeleton, step=step):
                continue
            ambient = skeleton[-1]
            for shape in at_most_two_column_shapes(tableau_size):
                for tableau in enumerate_bounded_rational_dyck_tableaux(
                    shape,
                    step=step,
                    max_entry=ambient - 1,
                ):
                    rr = rational_row_reading_word(tableau)
                    base = skeleton + rr
                    base_area = sum(base)
                    base_dinv = rational_dinv(base, m=step)
                    size = sum(shape)
                    schur_shape = conjugate_partition(shape)
                    for weight, multiplicity in schur_polynomial_by_ssyt(schur_shape, alphabet_size=2).items():
                        q_power, t_power = weight
                        coeffs[(base_area + q_power, base_dinv - size + t_power)] += multiplicity
    return coeffs


def rational_skeleton_string_formula_coefficients(
    length: int,
    *,
    step: int,
    max_deficit: int,
) -> Counter[tuple[int, int]]:
    """Expand the special-skeleton quotient formula in the rational setting."""

    if not isinstance(max_deficit, int) or max_deficit < 0:
        raise ValueError("max_deficit must be a non-negative integer")
    total_degree = rational_max_total_degree(length, step=step)
    coeffs: Counter[tuple[int, int]] = Counter()
    for sequence in generate_rational_dyck_sequences(length, step=step):
        if not is_rational_special_skeleton(sequence, step=step):
            continue
        deficit = rational_deficit(sequence, step=step)
        if deficit > max_deficit:
            continue
        area = sum(sequence)
        dinv = rational_dinv(sequence, m=step)
        if dinv >= area:
            for q_power in range(area, dinv + 1):
                coeffs[(q_power, total_degree - deficit - q_power)] += 1
        else:
            for q_power in range(dinv + 1, area):
                coeffs[(q_power, total_degree - deficit - q_power)] -= 1
    return coeffs
