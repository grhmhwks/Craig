"""Small semistandard Young tableau enumeration utilities.

Shapes are partitions in top-to-bottom row order.  SSYT entries use the
alphabet ``1, ..., alphabet_size`` by default, with rows weakly increasing and
columns strictly increasing from top to bottom.
"""

from __future__ import annotations

from collections import Counter
from typing import Iterable, Sequence


Shape = tuple[int, ...]
SSYT = tuple[tuple[int, ...], ...]
Weight = tuple[int, ...]


def is_partition_shape(shape: Sequence[int]) -> bool:
    values = tuple(shape)
    return all(isinstance(part, int) and part > 0 for part in values) and all(
        values[index] >= values[index + 1] for index in range(len(values) - 1)
    )


def partition_shapes(max_size: int, *, max_rows: int | None = None) -> list[Shape]:
    if not isinstance(max_size, int) or max_size < 0:
        raise ValueError("max_size must be a non-negative integer")
    if max_rows is not None and (not isinstance(max_rows, int) or max_rows < 0):
        raise ValueError("max_rows must be a non-negative integer or None")

    out: list[Shape] = [()]

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if prefix and (max_rows is None or len(prefix) <= max_rows):
            out.append(tuple(prefix))
        if max_rows is not None and len(prefix) >= max_rows:
            return
        for part in range(min(remaining, max_part), 0, -1):
            rec(remaining - part, part, prefix + [part])

    rec(max_size, max_size, [])
    return out


def shape_size(shape: Sequence[int]) -> int:
    if not is_partition_shape(shape) and tuple(shape) != ():
        raise ValueError("shape must be a partition")
    return sum(shape)


def tableau_shape(tableau: Sequence[Sequence[int]]) -> Shape:
    return tuple(len(row) for row in tableau)


def is_ssyt(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> bool:
    rows = tuple(tuple(row) for row in tableau)
    shape = tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    for row in rows:
        if any(not isinstance(value, int) or value < low or value > high for value in row):
            return False
        if any(row[index] > row[index + 1] for index in range(len(row) - 1)):
            return False
    for row_index in range(len(rows) - 1):
        for column in range(len(rows[row_index + 1])):
            if rows[row_index][column] >= rows[row_index + 1][column]:
                return False
    return True


def is_reverse_ssyt(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> bool:
    rows = tuple(tuple(row) for row in tableau)
    shape = tableau_shape(rows)
    if shape == ():
        return True
    if not is_partition_shape(shape):
        return False
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    for row in rows:
        if any(not isinstance(value, int) or value < low or value > high for value in row):
            return False
        if any(row[index] < row[index + 1] for index in range(len(row) - 1)):
            return False
    for row_index in range(len(rows) - 1):
        for column in range(len(rows[row_index + 1])):
            if rows[row_index][column] <= rows[row_index + 1][column]:
                return False
    return True


def enumerate_ssyt(
    shape: Sequence[int],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> list[SSYT]:
    shape_tuple = tuple(shape)
    if shape_tuple != () and not is_partition_shape(shape_tuple):
        raise ValueError("shape must be a partition in top-to-bottom row order")
    if not isinstance(alphabet_size, int) or alphabet_size <= 0:
        raise ValueError("alphabet_size must be positive")

    cells = [(row, col) for row, length in enumerate(shape_tuple) for col in range(length)]
    rows = [[0 for _ in range(length)] for length in shape_tuple]
    low = alphabet_start
    high = alphabet_start + alphabet_size - 1
    out: list[SSYT] = []

    def rec(cell_index: int) -> None:
        if cell_index == len(cells):
            out.append(tuple(tuple(row) for row in rows))
            return
        row, col = cells[cell_index]
        min_value = low
        if col > 0:
            min_value = max(min_value, rows[row][col - 1])
        if row > 0 and col < shape_tuple[row - 1]:
            min_value = max(min_value, rows[row - 1][col] + 1)
        for value in range(min_value, high + 1):
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = 0

    rec(0)
    return out


def enumerate_reverse_ssyt(
    shape: Sequence[int],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> list[SSYT]:
    high = alphabet_start + alphabet_size - 1
    return tuple(
        tuple(tuple(high - (value - alphabet_start) for value in row) for row in tableau)
        for tableau in enumerate_ssyt(
            shape,
            alphabet_size=alphabet_size,
            alphabet_start=alphabet_start,
        )
    )


def ssyt_weight(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> Weight:
    if not is_ssyt(tableau, alphabet_size=alphabet_size, alphabet_start=alphabet_start):
        raise ValueError("tableau must be an SSYT over the requested alphabet")
    counts = [0] * alphabet_size
    for row in tableau:
        for value in row:
            counts[value - alphabet_start] += 1
    return tuple(counts)


def reverse_ssyt_weight(
    tableau: Sequence[Sequence[int]],
    *,
    alphabet_size: int,
    alphabet_start: int = 1,
) -> Weight:
    if not is_reverse_ssyt(tableau, alphabet_size=alphabet_size, alphabet_start=alphabet_start):
        raise ValueError("tableau must be a reverse SSYT over the requested alphabet")
    counts = [0] * alphabet_size
    for row in tableau:
        for value in row:
            counts[value - alphabet_start] += 1
    return tuple(counts)


def weight_dictionary(tableaux: Iterable[Sequence[Sequence[int]]], *, alphabet_size: int) -> Counter[Weight]:
    weights: Counter[Weight] = Counter()
    for tableau in tableaux:
        weights[ssyt_weight(tableau, alphabet_size=alphabet_size)] += 1
    return weights


def schur_polynomial_by_ssyt(shape: Sequence[int], *, alphabet_size: int) -> Counter[Weight]:
    return weight_dictionary(enumerate_ssyt(shape, alphabet_size=alphabet_size), alphabet_size=alphabet_size)
