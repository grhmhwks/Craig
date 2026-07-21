#!/usr/bin/env python3
"""Exhaustive small-case checks for the shifted Q/R and P conjectures.

The charged bound N means

    number of missing inner boxes + number of actual entries <= N.

Modes
-----
qr
    Generate standard shifted set-valued tableaux in which consecutive labels
    never share a box, refine by the ordinary peak set, and compare the skew
    count with the coefficient-weighted straight count.

p
    Generate standard shifted set-valued tableaux with same-box consecutive
    labels allowed.  Refine by the P-peak set, the set of same-box consecutive
    pairs, and the set of labels in diagonal boxes.  Convert these records to
    dominant-monomial counts using the fitting and multiplicity rule described
    in explanation.tex, then compare the two sides.

both
    Run qr and then p.

Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from typing import DefaultDict, Iterable, Iterator, TypeAlias

Shape: TypeAlias = tuple[int, ...]
Position: TypeAlias = tuple[int, int]
Mask: TypeAlias = int
SkewShape: TypeAlias = tuple[Shape, Shape]


# =============================================================================
# Common shifted-shape utilities
# =============================================================================


def shape_size(shape: Shape) -> int:
    return sum(shape)


def is_strict_partition(shape: Shape) -> bool:
    return all(part > 0 for part in shape) and all(
        shape[i] > shape[i + 1] for i in range(len(shape) - 1)
    )


def validate_shape_pair(outer: Shape, inner: Shape) -> None:
    if not is_strict_partition(outer):
        raise ValueError(f"outer shape is not a strict partition: {outer}")
    if inner and not is_strict_partition(inner):
        raise ValueError(f"inner shape is not a strict partition: {inner}")
    if len(inner) > len(outer):
        raise ValueError(f"inner shape {inner} has more rows than outer shape {outer}")
    padded = inner + (0,) * (len(outer) - len(inner))
    if any(padded[row] > outer[row] for row in range(len(outer))):
        raise ValueError(f"inner shape {inner} is not contained in outer shape {outer}")


def addable_rows(shape: Shape) -> tuple[int, ...]:
    """Rows in which one addable outer-corner box may be inserted."""

    rows = [
        row
        for row in range(len(shape))
        if row == 0 or shape[row - 1] >= shape[row] + 2
    ]
    if not shape or shape[-1] >= 2:
        rows.append(len(shape))
    return tuple(rows)


def terminal_rows(shape: Shape) -> tuple[int, ...]:
    """Rows whose rightmost box has no box immediately below it."""

    return tuple(
        row
        for row in range(len(shape))
        if row == len(shape) - 1 or shape[row] >= shape[row + 1] + 2
    )


def add_box(shape: Shape, row: int) -> Shape:
    new_shape = list(shape)
    if row == len(new_shape):
        new_shape.append(1)
    else:
        new_shape[row] += 1
    return tuple(new_shape)


def position_of_new_box(shape: Shape, row: int) -> Position:
    if row == len(shape):
        return row, row
    return row, row + shape[row]


def position_of_terminal_box(shape: Shape, row: int) -> Position:
    return row, row + shape[row] - 1


def is_diagonal(position: Position) -> bool:
    return position[0] == position[1]


# =============================================================================
# Canonical prefixes and simultaneous straight/skew generation
# =============================================================================


def added_cell(previous_shape: Shape, next_shape: Shape) -> Position:
    """The unique cell added between two consecutive canonical shapes."""

    if len(next_shape) == len(previous_shape) + 1:
        row = len(previous_shape)
        return row, row
    for row, (old_length, new_length) in enumerate(zip(previous_shape, next_shape)):
        if new_length == old_length + 1:
            return row, row + old_length
    raise ValueError(
        f"shapes are not consecutive by one box: {previous_shape}, {next_shape}"
    )


def truncate_canonical_chain(
    canonical_chain: tuple[Shape, ...], occupied_position: Position
) -> tuple[Shape, ...]:
    """Remove canonical prefixes whose singleton box receives another label."""

    for label in range(1, len(canonical_chain)):
        if added_cell(canonical_chain[label - 1], canonical_chain[label]) == occupied_position:
            return canonical_chain[:label]
    return canonical_chain


def can_extend_canonical_chain(shape: Shape, row: int) -> bool:
    """Whether a new box is next in the row-canonical order."""

    return row == len(shape) or (bool(shape) and row == len(shape) - 1)


def shift_mask(mask: Mask, removed_labels: int, *, minimum_index: int) -> Mask:
    """Relabel after removing 1,...,removed_labels and discard small indices."""

    shifted = mask >> removed_labels
    return shifted & ~((1 << minimum_index) - 1)


def mask_tuple(mask: Mask, *, start: int) -> tuple[int, ...]:
    values: list[int] = []
    index = start
    while (1 << index) <= mask:
        if mask & (1 << index):
            values.append(index)
        index += 1
    return tuple(values)


@dataclass(frozen=True, slots=True)
class GenerationLevel:
    entries: int
    compressed_states: int
    tableaux: int
    straight_shapes_seen: int
    skew_shapes_seen: int


# =============================================================================
# Highest-weight coefficient enumeration
# =============================================================================


def nonempty_subsets(values: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
    for mask in range(1, 1 << len(values)):
        yield tuple(values[index] for index in range(len(values)) if mask & (1 << index))


@lru_cache(maxsize=None)
def one_row_tableaux(
    length: int, maximum_value: int
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """All legal set-valued rows over 1',1,...,m',m.

    Encoding: i' = 2*i-1 and i = 2*i.  The ordinary tableau alphabet order is
    1' < 1 < 2' < 2 < ... .
    """

    rows: tuple[tuple[tuple[int, ...], ...], ...] = ((),)
    for _ in range(length):
        new_rows: list[tuple[tuple[int, ...], ...]] = []
        for row in rows:
            rightmost = row[-1][-1] if row else 1
            values = tuple(range(rightmost, 2 * maximum_value + 1))
            for subset in nonempty_subsets(values):
                # If the previous maximum is primed, equality in the row would
                # repeat a primed value and is forbidden.
                if not row or rightmost % 2 == 0 or rightmost < subset[0]:
                    new_rows.append(row + (subset,))
        rows = tuple(new_rows)
    return rows


def rows_are_compatible(
    top_row: tuple[tuple[int, ...], ...],
    top_skew: int,
    bottom_row: tuple[tuple[int, ...], ...],
    bottom_skew: int,
) -> bool:
    if top_skew + len(top_row) < 1 + bottom_skew + len(bottom_row):
        return False

    for index, top_box in enumerate(top_row):
        bottom_index = (top_skew + index) - (bottom_skew + 1)
        if 0 <= bottom_index < len(bottom_row):
            bottom_box = bottom_row[bottom_index]
            top_maximum = max(top_box)
            bottom_minimum = min(bottom_box)
            if top_maximum > bottom_minimum:
                return False
            # Equality of an unprimed value in a column is forbidden.
            if top_maximum == bottom_minimum and top_maximum % 2 == 0:
                return False
    return True


def diagonal_box_is_primed(
    row: tuple[tuple[int, ...], ...], inner_row_length: int
) -> bool:
    """For P-tableaux, require every entry in a present diagonal box to be primed."""

    if inner_row_length != 0 or not row:
        return True
    return all(encoded % 2 == 1 for encoded in row[0])


def flagged_tableaux(
    outer: Shape, inner: Shape, *, p_diagonal: bool
) -> Iterator[tuple[tuple[tuple[int, ...], ...], ...]]:
    """Enumerate the row-flagged tableaux used for highest-weight coefficients."""

    validate_shape_pair(outer, inner)
    padded_inner = inner + (0,) * (len(outer) - len(inner))

    choices: list[tuple[tuple[tuple[int, ...], ...], ...]] = []
    for row_index in range(len(outer)):
        rows = one_row_tableaux(
            outer[row_index] - padded_inner[row_index], row_index + 1
        )
        if p_diagonal:
            rows = tuple(
                row
                for row in rows
                if diagonal_box_is_primed(row, padded_inner[row_index])
            )
        choices.append(rows)

    def recurse(
        row_index: int,
        chosen_rows: tuple[tuple[tuple[int, ...], ...], ...],
    ) -> Iterator[tuple[tuple[tuple[int, ...], ...], ...]]:
        if row_index == len(outer):
            yield chosen_rows
            return
        for candidate in choices[row_index]:
            if row_index == 0 or rows_are_compatible(
                chosen_rows[-1],
                padded_inner[row_index - 1],
                candidate,
                padded_inner[row_index],
            ):
                yield from recurse(row_index + 1, chosen_rows + (candidate,))

    yield from recurse(0, ())


def sorted_box(box: tuple[int, ...]) -> tuple[int, ...]:
    """Special order used in the lattice reading word.

    Unprimed entries first in increasing order, then primed entries in
    decreasing order.
    """

    return tuple(
        sorted(
            box,
            key=lambda encoded: (
                (0, encoded // 2)
                if encoded % 2 == 0
                else (1, -((encoded + 1) // 2))
            ),
        )
    )


def reading_word(
    tableau: tuple[tuple[tuple[int, ...], ...], ...]
) -> tuple[int, ...]:
    word: list[int] = []
    for row in reversed(tableau):
        for box in row:
            word.extend(sorted_box(box))
    return tuple(word)


def has_primed_property(word: tuple[int, ...]) -> bool:
    """The first RR box/occurrence for every value is primed and not unprimed."""

    seen_values: set[int] = set()
    for encoded in word:
        value = (encoded + 1) // 2
        if value not in seen_values:
            if encoded % 2 == 0:
                return False
            seen_values.add(value)
    return True


def has_lattice_property(word: tuple[int, ...]) -> bool:
    if not word:
        return True

    largest_value = max((encoded + 1) // 2 for encoded in word)
    counts = [0] * (largest_value + 2)

    # Backward pass: count unprimed letters; an upper prime is forbidden at a tie.
    for encoded in reversed(word):
        value = (encoded + 1) // 2
        if encoded % 2 == 0:
            counts[value] += 1
            if value > 1 and counts[value] > counts[value - 1]:
                return False
        elif value > 1 and counts[value] == counts[value - 1]:
            return False

    # Forward pass, retaining the backward tallies: count primed letters; a
    # lower unprimed letter is forbidden at a tie.
    for encoded in word:
        value = (encoded + 1) // 2
        if encoded % 2 == 1:
            counts[value] += 1
            if value > 1 and counts[value] > counts[value - 1]:
                return False
        elif counts[value + 1] == counts[value]:
            return False

    return True


def tableau_weight(word: tuple[int, ...]) -> Shape:
    if not word:
        return ()
    largest = max((encoded + 1) // 2 for encoded in word)
    weight = [0] * largest
    for encoded in word:
        weight[(encoded + 1) // 2 - 1] += 1
    while weight and weight[-1] == 0:
        weight.pop()
    return tuple(weight)


@lru_cache(maxsize=None)
def r_expansion_coefficients(outer: Shape, inner: Shape) -> tuple[tuple[Shape, int], ...]:
    coefficients: Counter[Shape] = Counter()
    for tableau in flagged_tableaux(outer, inner, p_diagonal=False):
        word = reading_word(tableau)
        if not has_primed_property(word) or not has_lattice_property(word):
            continue
        weight = tableau_weight(word)
        if weight and not is_strict_partition(weight):
            raise AssertionError(f"non-strict R highest weight {weight} for {outer}/{inner}")
        coefficients[weight] += 1
    return tuple(sorted(coefficients.items()))


@lru_cache(maxsize=None)
def p_expansion_coefficients(outer: Shape, inner: Shape) -> tuple[tuple[Shape, int], ...]:
    coefficients: Counter[Shape] = Counter()
    for tableau in flagged_tableaux(outer, inner, p_diagonal=True):
        word = reading_word(tableau)
        if not has_lattice_property(word):
            continue
        weight = tableau_weight(word)
        if weight and not is_strict_partition(weight):
            raise AssertionError(f"non-strict P highest weight {weight} for {outer}/{inner}")
        coefficients[weight] += 1
    return tuple(sorted(coefficients.items()))


# =============================================================================
# Q/R peak-refined check
# =============================================================================

QRPeakCounter: TypeAlias = Counter[Mask]
QRDegreeCounts: TypeAlias = DefaultDict[int, QRPeakCounter]
QRStraightCounts: TypeAlias = DefaultDict[Shape, QRDegreeCounts]
QRSkewCounts: TypeAlias = DefaultDict[SkewShape, QRDegreeCounts]


@dataclass(frozen=True, slots=True)
class QRState:
    shape: Shape
    previous_previous_position: Position | None
    previous_position: Position | None
    peak_mask: Mask
    canonical_chain: tuple[Shape, ...]


@dataclass(frozen=True, slots=True)
class QRFailure:
    outer: Shape
    inner: Shape
    actual_entries: int
    left: QRPeakCounter
    right: QRPeakCounter
    coefficients: tuple[tuple[Shape, int], ...]


def update_qr_peak_mask(
    peak_mask: Mask,
    previous_previous: Position | None,
    previous: Position | None,
    new_position: Position,
    new_label: int,
) -> Mask:
    if new_label >= 3:
        assert previous_previous is not None and previous is not None
        if previous_previous[1] < previous[1] and new_position[0] > previous[0]:
            peak_mask |= 1 << (new_label - 1)
    return peak_mask


def generate_qr_counts(
    max_entries: int, *, progress: bool = False
) -> tuple[QRStraightCounts, QRSkewCounts, tuple[GenerationLevel, ...]]:
    if max_entries < 1:
        raise ValueError("max_entries must be positive")

    states: Counter[QRState] = Counter(
        {
            QRState(
                shape=(),
                previous_previous_position=None,
                previous_position=None,
                peak_mask=0,
                canonical_chain=((),),
            ): 1
        }
    )
    straight: QRStraightCounts = defaultdict(lambda: defaultdict(Counter))
    skew: QRSkewCounts = defaultdict(lambda: defaultdict(Counter))
    levels: list[GenerationLevel] = []

    for new_label in range(1, max_entries + 1):
        next_states: Counter[QRState] = Counter()
        for state, multiplicity in states.items():
            shape = state.shape

            # Add the label to an existing terminal box, except that the QR
            # inflation model forbids consecutive labels in the same box.
            for row in terminal_rows(shape):
                position = position_of_terminal_box(shape, row)
                if position == state.previous_position:
                    continue
                peak = update_qr_peak_mask(
                    state.peak_mask,
                    state.previous_previous_position,
                    state.previous_position,
                    position,
                    new_label,
                )
                chain = truncate_canonical_chain(state.canonical_chain, position)
                next_states[
                    QRState(
                        shape,
                        state.previous_position,
                        position,
                        peak,
                        chain,
                    )
                ] += multiplicity

            # Add the label in a new outer-corner box.
            for row in addable_rows(shape):
                new_shape = add_box(shape, row)
                position = position_of_new_box(shape, row)
                peak = update_qr_peak_mask(
                    state.peak_mask,
                    state.previous_previous_position,
                    state.previous_position,
                    position,
                    new_label,
                )
                chain = state.canonical_chain
                if (
                    len(chain) - 1 == new_label - 1
                    and can_extend_canonical_chain(shape, row)
                ):
                    chain = chain + (new_shape,)
                next_states[
                    QRState(
                        new_shape,
                        state.previous_position,
                        position,
                        peak,
                        chain,
                    )
                ] += multiplicity

        states = next_states
        for state, multiplicity in states.items():
            straight[state.shape][new_label][state.peak_mask] += multiplicity
            for missing in range(1, len(state.canonical_chain)):
                actual = new_label - missing
                if actual <= 0:
                    continue
                inner = state.canonical_chain[missing]
                peak = shift_mask(state.peak_mask, missing, minimum_index=2)
                skew[(state.shape, inner)][actual][peak] += multiplicity

        level = GenerationLevel(
            new_label,
            len(states),
            sum(states.values()),
            len(straight),
            len(skew),
        )
        levels.append(level)
        if progress:
            print(
                f"[Q/R] generated n={new_label:2d}: {level.tableaux:9d} tableaux, "
                f"{level.compressed_states:8d} states, {level.skew_shapes_seen:5d} skew shapes",
                flush=True,
            )

    return straight, skew, tuple(levels)


def compare_qr_counts(
    max_entries: int,
    straight: QRStraightCounts,
    skew: QRSkewCounts,
    *,
    stop_on_first_failure: bool = False,
    progress: bool = False,
) -> tuple[tuple[QRFailure, ...], int]:
    failures: list[QRFailure] = []
    comparisons = 0
    ordered = sorted(
        skew,
        key=lambda pair: (
            shape_size(pair[0]),
            shape_size(pair[1]),
            pair[0],
            pair[1],
        ),
    )

    for index, (outer, inner) in enumerate(ordered, start=1):
        coefficients = r_expansion_coefficients(outer, inner)
        degree_limit = max_entries - shape_size(inner)
        for actual in range(1, degree_limit + 1):
            comparisons += 1
            left = Counter(skew[(outer, inner)].get(actual, Counter()))
            right: QRPeakCounter = Counter()
            for straight_shape, coefficient in coefficients:
                if shape_size(straight_shape) > actual:
                    continue
                for peak, multiplicity in straight.get(straight_shape, {}).get(actual, {}).items():
                    right[peak] += coefficient * multiplicity
            if left != right:
                failures.append(QRFailure(outer, inner, actual, left, right, coefficients))
                if stop_on_first_failure:
                    return tuple(failures), comparisons
        if progress and (index % 50 == 0 or index == len(ordered)):
            print(f"[Q/R] checked {index:5d}/{len(ordered):5d} skew shapes", flush=True)
    return tuple(failures), comparisons


def total_qr_straight(straight: QRStraightCounts) -> int:
    return sum(
        multiplicity
        for degree_counts in straight.values()
        for peak_counts in degree_counts.values()
        for multiplicity in peak_counts.values()
    )


def total_qr_skew(skew: QRSkewCounts) -> int:
    return sum(
        multiplicity
        for degree_counts in skew.values()
        for peak_counts in degree_counts.values()
        for multiplicity in peak_counts.values()
    )


def format_qr_counter(counter: QRPeakCounter) -> str:
    return repr({mask_tuple(mask, start=2): value for mask, value in sorted(counter.items())})


def run_qr(
    max_entries: int,
    *,
    progress: bool,
    stop_on_first_failure: bool,
) -> int:
    total_start = time.perf_counter()
    generation_start = time.perf_counter()
    straight, skew, levels = generate_qr_counts(max_entries, progress=progress)
    generation_seconds = time.perf_counter() - generation_start

    comparison_start = time.perf_counter()
    failures, comparisons = compare_qr_counts(
        max_entries,
        straight,
        skew,
        stop_on_first_failure=stop_on_first_failure,
        progress=progress,
    )
    comparison_seconds = time.perf_counter() - comparison_start
    total_seconds = time.perf_counter() - total_start

    final = levels[-1]
    print("Q/R CHECK")
    print(f"maximum charged entries: {max_entries}")
    print(f"straight shapes:          {len(straight)}")
    print(f"proper skew shapes:       {len(skew)}")
    print(f"straight tableaux:        {total_qr_straight(straight)}")
    print(f"derived skew tableaux:    {total_qr_skew(skew)}")
    print(f"tableaux at top degree:   {final.tableaux}")
    print(f"compressed top states:    {final.compressed_states}")
    print(f"shape-degree comparisons: {comparisons}")
    print(f"generation runtime:       {generation_seconds:.6f} seconds")
    print(f"comparison runtime:       {comparison_seconds:.6f} seconds")
    print(f"total runtime:            {total_seconds:.6f} seconds")

    if not failures:
        print("result: PASS")
        return 0

    print(f"result: FAIL ({len(failures)} failure(s) recorded)")
    for failure in failures[:10]:
        print(f"  shape {failure.outer}/{failure.inner}, actual entries {failure.actual_entries}")
        print(f"    left:  {format_qr_counter(failure.left)}")
        print(f"    right: {format_qr_counter(failure.right)}")
        print(f"    coefficients: {dict(failure.coefficients)}")
    if len(failures) > 10:
        print(f"  ... {len(failures) - 10} additional failures omitted")
    return 1


# =============================================================================
# P dominant-monomial check
# =============================================================================

PSignature: TypeAlias = tuple[Mask, Mask, Mask]  # P-peaks, same-box pairs, diagonal labels
PSignatureCounter: TypeAlias = Counter[PSignature]
PMonomialCounter: TypeAlias = Counter[Shape]
PDegreeCounts: TypeAlias = DefaultDict[int, PSignatureCounter]
PStraightCounts: TypeAlias = DefaultDict[Shape, PDegreeCounts]
PSkewCounts: TypeAlias = DefaultDict[SkewShape, PDegreeCounts]


@dataclass(frozen=True, slots=True)
class PState:
    shape: Shape
    previous_previous_position: Position | None
    previous_position: Position | None
    p_peak_mask: Mask
    same_box_mask: Mask
    diagonal_mask: Mask
    canonical_chain: tuple[Shape, ...]


@dataclass(frozen=True, slots=True)
class PFailure:
    outer: Shape
    inner: Shape
    actual_entries: int
    left_signatures: PSignatureCounter
    right_signatures: PSignatureCounter
    left_monomials: PMonomialCounter
    right_monomials: PMonomialCounter
    coefficients: tuple[tuple[Shape, int], ...]


def is_northeast(first: Position, second: Position) -> bool:
    return second != first and second[0] <= first[0]


def is_southwest(first: Position, second: Position) -> bool:
    return second[0] > first[0]


def update_p_peak_mask(
    p_peak_mask: Mask,
    previous_previous: Position | None,
    previous: Position | None,
    new_position: Position,
    new_label: int,
) -> Mask:
    if new_label < 3:
        return p_peak_mask
    assert previous_previous is not None and previous is not None
    left = previous_previous == previous or is_northeast(previous_previous, previous)
    right = previous == new_position or is_southwest(previous, new_position)
    if left and right:
        p_peak_mask |= 1 << (new_label - 1)
    return p_peak_mask


def update_same_box_mask(
    same_box_mask: Mask,
    previous: Position | None,
    new_position: Position,
    new_label: int,
) -> Mask:
    if new_label >= 2 and previous == new_position:
        same_box_mask |= 1 << (new_label - 1)
    return same_box_mask


def update_diagonal_mask(
    diagonal_mask: Mask, new_position: Position, new_label: int
) -> Mask:
    if is_diagonal(new_position):
        diagonal_mask |= 1 << new_label
    return diagonal_mask


def generate_p_counts(
    max_entries: int, *, progress: bool = False
) -> tuple[PStraightCounts, PSkewCounts, tuple[GenerationLevel, ...]]:
    if max_entries < 1:
        raise ValueError("max_entries must be positive")

    states: Counter[PState] = Counter(
        {
            PState(
                shape=(),
                previous_previous_position=None,
                previous_position=None,
                p_peak_mask=0,
                same_box_mask=0,
                diagonal_mask=0,
                canonical_chain=((),),
            ): 1
        }
    )
    straight: PStraightCounts = defaultdict(lambda: defaultdict(Counter))
    skew: PSkewCounts = defaultdict(lambda: defaultdict(Counter))
    levels: list[GenerationLevel] = []

    for new_label in range(1, max_entries + 1):
        next_states: Counter[PState] = Counter()
        for state, multiplicity in states.items():
            shape = state.shape

            # Same-box consecutive labels are allowed in the P standard model.
            for row in terminal_rows(shape):
                position = position_of_terminal_box(shape, row)
                p_peak = update_p_peak_mask(
                    state.p_peak_mask,
                    state.previous_previous_position,
                    state.previous_position,
                    position,
                    new_label,
                )
                same_box = update_same_box_mask(
                    state.same_box_mask,
                    state.previous_position,
                    position,
                    new_label,
                )
                diagonal = update_diagonal_mask(
                    state.diagonal_mask, position, new_label
                )
                chain = truncate_canonical_chain(state.canonical_chain, position)
                next_states[
                    PState(
                        shape,
                        state.previous_position,
                        position,
                        p_peak,
                        same_box,
                        diagonal,
                        chain,
                    )
                ] += multiplicity

            for row in addable_rows(shape):
                new_shape = add_box(shape, row)
                position = position_of_new_box(shape, row)
                p_peak = update_p_peak_mask(
                    state.p_peak_mask,
                    state.previous_previous_position,
                    state.previous_position,
                    position,
                    new_label,
                )
                same_box = update_same_box_mask(
                    state.same_box_mask,
                    state.previous_position,
                    position,
                    new_label,
                )
                diagonal = update_diagonal_mask(
                    state.diagonal_mask, position, new_label
                )
                chain = state.canonical_chain
                if (
                    len(chain) - 1 == new_label - 1
                    and can_extend_canonical_chain(shape, row)
                ):
                    chain = chain + (new_shape,)
                next_states[
                    PState(
                        new_shape,
                        state.previous_position,
                        position,
                        p_peak,
                        same_box,
                        diagonal,
                        chain,
                    )
                ] += multiplicity

        states = next_states
        for state, multiplicity in states.items():
            signature = (
                state.p_peak_mask,
                state.same_box_mask,
                state.diagonal_mask,
            )
            straight[state.shape][new_label][signature] += multiplicity

            for missing in range(1, len(state.canonical_chain)):
                actual = new_label - missing
                if actual <= 0:
                    continue
                inner = state.canonical_chain[missing]
                skew_signature = (
                    shift_mask(state.p_peak_mask, missing, minimum_index=2),
                    shift_mask(state.same_box_mask, missing, minimum_index=1),
                    shift_mask(state.diagonal_mask, missing, minimum_index=1),
                )
                skew[(state.shape, inner)][actual][skew_signature] += multiplicity

        level = GenerationLevel(
            new_label,
            len(states),
            sum(states.values()),
            len(straight),
            len(skew),
        )
        levels.append(level)
        if progress:
            print(
                f"[P]   generated n={new_label:2d}: {level.tableaux:9d} tableaux, "
                f"{level.compressed_states:8d} states, {level.skew_shapes_seen:5d} skew shapes",
                flush=True,
            )

    return straight, skew, tuple(levels)


@lru_cache(maxsize=None)
def partitions_of_size(n: int, max_length: int) -> tuple[Shape, ...]:
    if n < 0 or max_length < 0:
        return ()
    if n == 0:
        return ((),)
    if max_length == 0:
        return ()

    result: list[Shape] = []

    def recurse(remaining: int, largest_allowed: int, prefix: list[int]) -> None:
        if remaining == 0:
            result.append(tuple(prefix))
            return
        if len(prefix) == max_length:
            return
        for part in range(min(largest_allowed, remaining), 0, -1):
            prefix.append(part)
            recurse(remaining - part, part, prefix)
            prefix.pop()

    recurse(n, n, [])
    return tuple(result)


def partition_intervals(partition: Shape) -> tuple[tuple[int, int], ...]:
    """Inclusive intervals of labels belonging to the consecutive parts."""

    intervals: list[tuple[int, int]] = []
    start = 1
    for part in partition:
        end = start + part - 1
        intervals.append((start, end))
        start = end + 1
    return tuple(intervals)


def interval_mask(start: int, end: int) -> Mask:
    return ((1 << (end + 1)) - 1) ^ ((1 << start) - 1)


@lru_cache(maxsize=None)
def fitting_partitions_with_weights(
    num_entries: int,
    p_peak_mask: Mask,
    same_box_mask: Mask,
    diagonal_mask: Mask,
    max_length: int,
) -> tuple[tuple[Shape, int], ...]:
    """Return every fitting dominant partition and its 2^free-parts weight."""

    result: list[tuple[Shape, int]] = []
    diagonal_same_box = same_box_mask & diagonal_mask

    for partition in partitions_of_size(num_entries, max_length):
        intervals = partition_intervals(partition)
        beginnings = 0
        ends = 0
        for start, end in intervals:
            beginnings |= 1 << start
            ends |= 1 << end

        if p_peak_mask & ~(beginnings | ends):
            continue
        if diagonal_same_box & ~ends:
            continue

        free_parts = 0
        for start, end in intervals:
            labels = interval_mask(start, end)
            if labels & diagonal_mask:
                continue

            # A same-box pair d,d+1 is wholly inside this part exactly when
            # d lies between start and end-1.
            possible_d = interval_mask(start, end - 1) if start < end else 0
            if same_box_mask & possible_d:
                continue
            free_parts += 1

        result.append((partition, 1 << free_parts))

    return tuple(result)


def p_signatures_to_monomials(
    num_entries: int,
    signatures: PSignatureCounter,
    max_length: int,
) -> PMonomialCounter:
    monomials: PMonomialCounter = Counter()
    for (p_peak, same_box, diagonal), multiplicity in signatures.items():
        for partition, marking_multiplicity in fitting_partitions_with_weights(
            num_entries,
            p_peak,
            same_box,
            diagonal,
            max_length,
        ):
            monomials[partition] += multiplicity * marking_multiplicity
    return monomials


def compare_p_counts(
    max_entries: int,
    straight: PStraightCounts,
    skew: PSkewCounts,
    *,
    num_vars: int,
    stop_on_first_failure: bool = False,
    progress: bool = False,
) -> tuple[tuple[PFailure, ...], int]:
    failures: list[PFailure] = []
    comparisons = 0
    ordered = sorted(
        skew,
        key=lambda pair: (
            shape_size(pair[0]),
            shape_size(pair[1]),
            pair[0],
            pair[1],
        ),
    )

    for index, (outer, inner) in enumerate(ordered, start=1):
        coefficients = p_expansion_coefficients(outer, inner)
        degree_limit = max_entries - shape_size(inner)
        for actual in range(1, degree_limit + 1):
            comparisons += 1
            left_signatures = Counter(skew[(outer, inner)].get(actual, Counter()))
            right_signatures: PSignatureCounter = Counter()
            for straight_shape, coefficient in coefficients:
                if shape_size(straight_shape) > actual:
                    continue
                for signature, multiplicity in straight.get(straight_shape, {}).get(actual, {}).items():
                    right_signatures[signature] += coefficient * multiplicity

            max_length = min(num_vars, actual)
            left_monomials = p_signatures_to_monomials(actual, left_signatures, max_length)
            right_monomials = p_signatures_to_monomials(actual, right_signatures, max_length)
            if left_monomials != right_monomials:
                failures.append(
                    PFailure(
                        outer,
                        inner,
                        actual,
                        left_signatures,
                        right_signatures,
                        left_monomials,
                        right_monomials,
                        coefficients,
                    )
                )
                if stop_on_first_failure:
                    return tuple(failures), comparisons

        if progress and (index % 50 == 0 or index == len(ordered)):
            print(f"[P]   checked {index:5d}/{len(ordered):5d} skew shapes", flush=True)

    return tuple(failures), comparisons


def total_p_straight(straight: PStraightCounts) -> int:
    return sum(
        multiplicity
        for degree_counts in straight.values()
        for signature_counts in degree_counts.values()
        for multiplicity in signature_counts.values()
    )


def total_p_skew(skew: PSkewCounts) -> int:
    return sum(
        multiplicity
        for degree_counts in skew.values()
        for signature_counts in degree_counts.values()
        for multiplicity in signature_counts.values()
    )


def format_p_signatures(counter: PSignatureCounter) -> str:
    formatted = {
        (
            mask_tuple(p_peak, start=2),
            mask_tuple(same_box, start=1),
            mask_tuple(diagonal, start=1),
        ): multiplicity
        for (p_peak, same_box, diagonal), multiplicity in sorted(counter.items())
    }
    return repr(formatted)


def format_monomials(counter: PMonomialCounter) -> str:
    return repr(dict(sorted(counter.items())))


def run_p(
    max_entries: int,
    *,
    num_vars: int,
    progress: bool,
    stop_on_first_failure: bool,
) -> int:
    total_start = time.perf_counter()
    generation_start = time.perf_counter()
    straight, skew, levels = generate_p_counts(max_entries, progress=progress)
    generation_seconds = time.perf_counter() - generation_start

    comparison_start = time.perf_counter()
    failures, comparisons = compare_p_counts(
        max_entries,
        straight,
        skew,
        num_vars=num_vars,
        stop_on_first_failure=stop_on_first_failure,
        progress=progress,
    )
    comparison_seconds = time.perf_counter() - comparison_start
    total_seconds = time.perf_counter() - total_start

    final = levels[-1]
    print("P CHECK")
    print(f"maximum charged entries: {max_entries}")
    print(f"maximum monomial length:  {num_vars}")
    print(f"straight shapes:          {len(straight)}")
    print(f"proper skew shapes:       {len(skew)}")
    print(f"straight tableaux:        {total_p_straight(straight)}")
    print(f"derived skew tableaux:    {total_p_skew(skew)}")
    print(f"tableaux at top degree:   {final.tableaux}")
    print(f"compressed top states:    {final.compressed_states}")
    print(f"shape-degree comparisons: {comparisons}")
    print(f"generation runtime:       {generation_seconds:.6f} seconds")
    print(f"comparison runtime:       {comparison_seconds:.6f} seconds")
    print(f"total runtime:            {total_seconds:.6f} seconds")

    if not failures:
        print("result: PASS")
        return 0

    print(f"result: FAIL ({len(failures)} failure(s) recorded)")
    for failure in failures[:10]:
        print(f"  shape {failure.outer}/{failure.inner}, actual entries {failure.actual_entries}")
        print(f"    left monomials:  {format_monomials(failure.left_monomials)}")
        print(f"    right monomials: {format_monomials(failure.right_monomials)}")
        print(f"    left signatures:  {format_p_signatures(failure.left_signatures)}")
        print(f"    right signatures: {format_p_signatures(failure.right_signatures)}")
        print(f"    coefficients: {dict(failure.coefficients)}")
    if len(failures) > 10:
        print(f"  ... {len(failures) - 10} additional failures omitted")
    return 1


# =============================================================================
# Command line
# =============================================================================


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("qr", "p", "both"),
        default="both",
        help="which check to run (default: both)",
    )
    parser.add_argument(
        "--max-entries",
        type=int,
        default=15,
        help="maximum missing-box count plus actual-entry count (default: 15)",
    )
    parser.add_argument(
        "--num-vars",
        type=int,
        default=None,
        help="P check: maximum dominant-monomial length; defaults to max-entries",
    )
    parser.add_argument("--progress", action="store_true", help="print progress")
    parser.add_argument(
        "--stop-on-first-failure",
        action="store_true",
        help="stop a check at its first discrepancy",
    )
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.max_entries < 1:
            raise ValueError("max_entries must be positive")
        num_vars = args.max_entries if args.num_vars is None else args.num_vars
        if num_vars < 1:
            raise ValueError("num_vars must be positive")

        statuses: list[int] = []
        if args.mode in ("qr", "both"):
            statuses.append(
                run_qr(
                    args.max_entries,
                    progress=args.progress,
                    stop_on_first_failure=args.stop_on_first_failure,
                )
            )
        if args.mode == "both":
            print()
        if args.mode in ("p", "both"):
            statuses.append(
                run_p(
                    args.max_entries,
                    num_vars=num_vars,
                    progress=args.progress,
                    stop_on_first_failure=args.stop_on_first_failure,
                )
            )
        return 0 if all(status == 0 for status in statuses) else 1
    except (ValueError, AssertionError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
