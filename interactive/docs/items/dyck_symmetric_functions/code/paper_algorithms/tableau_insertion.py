"""Section 3 tableau insertion helpers.

Tableaux are represented as ``list`` objects ordered bottom row to top row.
Each row is a left-to-right sequence of non-negative integers.

Shape convention used here: rows may have different lengths and no monotone
row-length condition is imposed by ``is_dyck_tableau``.  For each column index,
the cells that exist in rows having that index are read bottom-to-top and must
satisfy the affine Dyck inequality.  This is the bottom-to-top representation
requested by CA-0002; it differs from the protected draft's local prose that
sometimes indexes rows top-to-bottom.

``tabsert`` processes existing rows in the source/paper top-to-bottom order,
which is descending index order under this bottom-to-top storage.  When it
carries a non-empty evicted row past all existing rows, that row is inserted at
index 0, i.e. it becomes a new bottom row in the bottom-to-top list.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .row_insertion import RowsertStep, WorsertStep, is_dual_dyck, rowsert, worsert


Tableau = list[list[int]]


@dataclass(frozen=True)
class TabsertRowTrace:
    row_index: int
    input_row: tuple[int, ...]
    inserted_row: tuple[int, ...]
    evicted_row: tuple[int, ...]
    output_row: tuple[int, ...]
    rowsert_steps: tuple[RowsertStep, ...]


@dataclass(frozen=True)
class ReverseTabsertRowTrace:
    row_index: int
    original_length: int
    input_row: tuple[int, ...]
    kept_row: tuple[int, ...]
    peeled_row: tuple[int, ...]
    accumulated_in: tuple[int, ...]
    recovered_row: tuple[int, ...]
    accumulated_out: tuple[int, ...]
    worsert_steps: tuple[WorsertStep, ...]


def _is_row(value: object) -> bool:
    return isinstance(value, (list, tuple)) and all(
        isinstance(entry, int) and entry >= 0 for entry in value
    )


def shape(tableau: Sequence[Sequence[int]]) -> list[int]:
    """Return row lengths in bottom-to-top order."""

    _require_tableau_like(tableau)
    return [len(row) for row in tableau]


def _require_tableau_like(tableau: Sequence[Sequence[int]]) -> None:
    if not isinstance(tableau, (list, tuple)):
        raise TypeError("tableau must be a list or tuple of rows")
    for row in tableau:
        if not _is_row(row):
            raise TypeError("each tableau row must be a sequence of non-negative integers")


def _copied_tableau(tableau: Sequence[Sequence[int]]) -> Tableau:
    _require_tableau_like(tableau)
    return [list(row) for row in tableau]


def is_affine_dyck(seq: Sequence[int]) -> bool:
    """Return whether ``seq`` satisfies the affine-Dyck step condition."""

    return all(isinstance(value, int) and value >= 0 for value in seq) and all(
        seq[index + 1] <= seq[index] + 1 for index in range(len(seq) - 1)
    )


def is_dyck_tableau(tableau: Sequence[Sequence[int]]) -> bool:
    """Validate the CA-0002 bottom-to-top Dyck tableau convention.

    Empty tableaux are accepted.  Empty rows inside a non-empty tableau are
    rejected, because they create ambiguous shape data for the reverse helper.
    """

    try:
        rows = _copied_tableau(tableau)
    except TypeError:
        return False

    if any(len(row) == 0 for row in rows):
        return len(rows) == 0
    if any(not is_dual_dyck(row) for row in rows):
        return False

    max_len = max((len(row) for row in rows), default=0)
    for column in range(max_len):
        column_values = [row[column] for row in rows if column < len(row)]
        if not is_affine_dyck(column_values):
            return False
    return True


def row_reading_word(tableau: Sequence[Sequence[int]]) -> list[int]:
    """Read rows bottom-to-top, and within each row left-to-right."""

    _require_tableau_like(tableau)
    word: list[int] = []
    for row in tableau:
        word.extend(row)
    return word


def tabsert(
    tableau: Sequence[Sequence[int]],
    inserted_row: Sequence[int],
    *,
    trace: bool = False,
) -> Tableau | tuple[Tableau, list[TabsertRowTrace]]:
    """Insert ``inserted_row`` through ``tableau`` using ``rowsert``.

    Existing rows are processed in source/paper top-to-bottom order, i.e.
    descending index order under bottom-to-top storage.  Inputs are copied and
    never mutated.  If ``trace`` is true, the returned pair is
    ``(updated_tableau, row_traces)``.
    """

    rows = _copied_tableau(tableau)
    if not is_dyck_tableau(rows):
        raise ValueError("tableau must be a valid Dyck tableau")
    if not is_dual_dyck(inserted_row):
        raise ValueError("inserted_row must be a dual Dyck sequence")

    evicted = list(inserted_row)
    traces: list[TabsertRowTrace] = []
    row_index = len(rows) - 1
    while evicted and row_index >= 0:
        input_row = tuple(rows[row_index])
        inserted = tuple(evicted)
        row_trace: list[RowsertStep] = []
        next_evicted, output_row = rowsert(rows[row_index], evicted, trace=row_trace)
        rows[row_index] = output_row
        evicted = next_evicted
        traces.append(
            TabsertRowTrace(
                row_index=row_index,
                input_row=input_row,
                inserted_row=inserted,
                evicted_row=tuple(evicted),
                output_row=tuple(output_row),
                rowsert_steps=tuple(row_trace),
            )
        )
        row_index -= 1

    if evicted:
        rows.insert(0, list(evicted))
        traces.append(
            TabsertRowTrace(
                row_index=0,
                input_row=(),
                inserted_row=tuple(evicted),
                evicted_row=(),
                output_row=tuple(evicted),
                rowsert_steps=(),
            )
        )

    if not is_dyck_tableau(rows):
        raise ValueError("tabsert output is not a valid Dyck tableau under the documented convention")
    return (rows, traces) if trace else rows


def reverse_tabsert(
    updated_tableau: Sequence[Sequence[int]],
    original_shape: Sequence[int],
    *,
    trace: bool = False,
) -> tuple[Tableau, list[int]] | tuple[Tableau, list[int], list[ReverseTabsertRowTrace]]:
    """Bounded rowwise reverse helper for red-team checks.

    ``original_shape`` is the list of original row lengths in bottom-to-top
    order.  Extra updated rows are interpreted as newly added bottom rows and
    initialize the accumulated sequence.  The helper then works through the
    original rows from bottom to top, reversing the corrected top-to-bottom
    forward insertion order.  At original row ``r`` it keeps the first
    ``original_shape[r]`` cells, peels terminal cells as the horizontal-strip
    contribution, runs corrected ``worsert`` on the accumulated sequence
    through the kept row, and passes ``F_minus + F_plus`` downward.  This is an
    executable approximation of the proof's inverse construction, intended for
    finite checks.
    """

    rows = _copied_tableau(updated_tableau)
    if not is_dyck_tableau(rows):
        raise ValueError("updated_tableau must be a valid Dyck tableau")
    if not isinstance(original_shape, (list, tuple)) or any(
        not isinstance(length, int) or length < 0 for length in original_shape
    ):
        raise TypeError("original_shape must be a sequence of non-negative row lengths")
    if len(original_shape) > len(rows):
        raise ValueError("original_shape has more rows than updated_tableau")

    offset = len(rows) - len(original_shape)
    if offset < 0:
        raise ValueError("updated_tableau has fewer rows than original_shape")

    recovered: Tableau = [[] for _ in original_shape]
    accumulated: list[int] = []
    traces: list[ReverseTabsertRowTrace] = []

    for row_index in range(offset):
        current_row = rows[row_index]
        accumulated_in = tuple(accumulated)
        accumulated = accumulated + list(current_row)
        traces.append(
            ReverseTabsertRowTrace(
                row_index=row_index,
                original_length=0,
                input_row=tuple(current_row),
                kept_row=(),
                peeled_row=tuple(current_row),
                accumulated_in=accumulated_in,
                recovered_row=(),
                accumulated_out=tuple(accumulated),
                worsert_steps=(),
            )
        )

    for original_index in range(len(original_shape)):
        row_index = offset + original_index
        current_row = rows[row_index]
        keep_length = original_shape[original_index]
        if keep_length > len(current_row):
            raise ValueError("original_shape cannot exceed updated row lengths")
        kept = list(current_row[:keep_length])
        peeled = list(current_row[keep_length:])
        wor_trace: list[WorsertStep] = []
        recovered_row, f_minus = worsert(accumulated, kept, trace=wor_trace)
        accumulated_out = list(f_minus) + peeled
        recovered[original_index] = recovered_row
        traces.append(
            ReverseTabsertRowTrace(
                row_index=row_index,
                original_length=keep_length,
                input_row=tuple(current_row),
                kept_row=tuple(kept),
                peeled_row=tuple(peeled),
                accumulated_in=tuple(accumulated),
                recovered_row=tuple(recovered_row),
                accumulated_out=tuple(accumulated_out),
                worsert_steps=tuple(wor_trace),
            )
        )
        accumulated = accumulated_out

    if not is_dyck_tableau(recovered):
        raise ValueError("reverse helper recovered an invalid Dyck tableau")
    if not is_dual_dyck(accumulated):
        raise ValueError("reverse helper recovered an invalid inserted row")
    result = (recovered, accumulated)
    return (*result, traces) if trace else result
