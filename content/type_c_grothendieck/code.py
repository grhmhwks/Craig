#!/usr/bin/env python3
"""Peakset-refined finite checks for the type C K-Stanley conjecture.

The rank convention follows the paper: ``W_a`` has simple generators
``s_0, ..., s_{a-1}``.  For every signed permutation ``w``, degree ``n`` and
peak set ``S`` in the requested finite range, this program compares

* repetition-free type C Hecke words for ``w`` of length ``n`` and peak set
  ``S``;
* pairs ``(P,Q)`` where ``P`` is a strict decomposition tableau for ``w`` and
  ``Q`` is a standard shifted set-valued tableau of the same shape, with
  ``n`` labels, peak set ``S``, and no consecutive labels in one box.

The implementation uses only the Python standard library.  It counts words by
aggregating continuation states instead of storing the words themselves.
Finite agreement is evidence for the conjectural peakset-preserving
correspondence; it is not a proof and does not construct a bijection.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from functools import lru_cache
from typing import DefaultDict, Iterable, Iterator


Permutation = tuple[int, ...]
Row = tuple[int, ...]
Shape = tuple[int, ...]
Position = tuple[int, int]
PeakMask = int


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def hecke_step(permutation: Permutation, generator: int) -> Permutation:
    """Apply one type C 0-Hecke generator to a signed permutation."""

    values = list(permutation)
    if generator == 0:
        if values[0] > 0:
            values[0] = -values[0]
    elif values[generator - 1] < values[generator]:
        values[generator - 1], values[generator] = (
            values[generator],
            values[generator - 1],
        )
    return tuple(values)


@lru_cache(maxsize=None)
def apply_row(permutation: Permutation, row: Row) -> Permutation:
    for generator in row:
        permutation = hecke_step(permutation, generator)
    return permutation


def peak_tuple(mask: PeakMask, degree: int) -> tuple[int, ...]:
    return tuple(index for index in range(2, degree) if mask & (1 << index))


def count_words(
    rank: int,
    max_degree: int,
) -> tuple[Counter[tuple[Permutation, int, PeakMask]], int, int]:
    """Count repetition-free Hecke words by permutation, length and peaks.

    A continuation state stores ``(permutation, last letter, last comparison
    was a rise, peak mask)``.  This is all the information needed to append a
    new generator and decide whether the previous position becomes a peak.
    """

    identity = tuple(range(1, rank + 1))
    totals: Counter[tuple[Permutation, int, PeakMask]] = Counter()
    totals[(identity, 0, 0)] = 1
    total_words = 1

    # (permutation, last_generator, previous_comparison_was_rise, peak_mask)
    states: Counter[tuple[Permutation, int, bool, PeakMask]] = Counter()
    for generator in range(rank):
        states[(hecke_step(identity, generator), generator, False, 0)] += 1

    state_count = 0
    for degree in range(1, max_degree + 1):
        level_words = 0
        for (permutation, _last, _rise, peaks), multiplicity in states.items():
            totals[(permutation, degree, peaks)] += multiplicity
            level_words += multiplicity
        expected = rank * (rank - 1) ** (degree - 1)
        require(level_words == expected, f"word count mismatch in degree {degree}")
        total_words += level_words
        state_count += len(states)

        if degree == max_degree:
            break

        next_states: Counter[tuple[Permutation, int, bool, PeakMask]] = Counter()
        new_degree = degree + 1
        for (permutation, last, previous_rise, peaks), multiplicity in states.items():
            for generator in range(rank):
                if generator == last:
                    continue
                new_peaks = peaks
                if previous_rise and last > generator:
                    # Appending position new_degree makes position
                    # new_degree-1 into a peak.
                    new_peaks |= 1 << (new_degree - 1)
                next_states[
                    (
                        hecke_step(permutation, generator),
                        generator,
                        last < generator,
                        new_peaks,
                    )
                ] += multiplicity
        states = next_states

    return totals, total_words, state_count


def is_unimodal(row: Row) -> bool:
    if not row:
        return False
    dip = max(index for index, value in enumerate(row) if value == min(row))
    return all(row[index] > row[index + 1] for index in range(dip)) and all(
        row[index] < row[index + 1] for index in range(dip, len(row) - 1)
    )


def unimodal_rows(rank: int) -> dict[int, tuple[Row, ...]]:
    """Generate every strict unimodal row over ``0,...,rank-1``."""

    rows: DefaultDict[int, set[Row]] = defaultdict(set)
    for dip in range(rank):
        larger = tuple(range(dip + 1, rank))
        for left_mask in range(1 << len(larger)):
            left = tuple(
                value
                for bit, value in reversed(tuple(enumerate(larger)))
                if left_mask & (1 << bit)
            )
            for right_mask in range(1 << len(larger)):
                right = tuple(
                    value
                    for bit, value in enumerate(larger)
                    if right_mask & (1 << bit)
                )
                row = left + (dip,) + right
                require(is_unimodal(row), f"internal non-unimodal row: {row}")
                rows[len(row)].add(row)
    return {length: tuple(sorted(group)) for length, group in rows.items()}


def column_compatible(bottom: Row, top: Row) -> bool:
    """The two-row strict-decomposition-tableau condition from the source."""

    if not bottom:
        return True
    if len(top) <= len(bottom):
        return False

    b_row = list(bottom)
    a_row = list(top)
    b_index = max(index for index, value in enumerate(b_row) if value == min(b_row))
    for index in range(b_index + 1):
        b_row[index] = -b_row[index]
    a_index = max(index for index, value in enumerate(a_row) if value == min(a_row))
    for index in range(a_index):
        a_row[index] = -a_row[index]

    if abs(b_row[-1]) >= abs(a_row[0]):
        return False
    if abs(b_row[0]) >= abs(a_row[0]):
        return False

    for index in range(len(b_row)):
        if a_row[index + 1] > b_row[index]:
            for later in range(index + 1, len(b_row)):
                if b_row[index] < b_row[later] < a_row[index + 1]:
                    return False
                if b_row[index] < -b_row[later] < a_row[index + 1]:
                    return False
                if b_row[later] in (a_row[index + 1], -a_row[index + 1]):
                    return False
            for earlier in range(index + 1):
                if b_row[index] < a_row[earlier] < a_row[index + 1]:
                    return False
                if b_row[index] < -a_row[earlier] < a_row[index + 1]:
                    return False
                if a_row[earlier] in (a_row[index + 1], -a_row[index + 1]):
                    return False
    return True


def strict_shapes(max_size: int, max_part: int) -> Iterator[Shape]:
    yield ()

    def rec(remaining: int, cap: int, prefix: Shape) -> Iterator[Shape]:
        for part in range(min(remaining, cap), 0, -1):
            shape = prefix + (part,)
            yield shape
            yield from rec(remaining - part, part - 1, shape)

    yield from rec(max_size, max_part, ())


def count_hecke_tableaux(
    rank: int,
    max_degree: int,
) -> tuple[dict[Permutation, Counter[Shape]], int, int]:
    """Count strict decomposition tableaux by permutation and shape."""

    identity = tuple(range(1, rank + 1))
    rows = unimodal_rows(rank)
    maximum_row_length = max(rows)
    shapes = tuple(strict_shapes(max_degree, maximum_row_length))

    compatibility: dict[tuple[int, int], dict[Row, tuple[Row, ...]]] = {}
    for bottom_length, bottom_rows in rows.items():
        for top_length, top_rows in rows.items():
            if top_length <= bottom_length:
                continue
            compatibility[(bottom_length, top_length)] = {
                bottom: tuple(top for top in top_rows if column_compatible(bottom, top))
                for bottom in bottom_rows
            }

    counts: dict[Permutation, Counter[Shape]] = defaultdict(Counter)
    counts[identity][()] = 1
    total_tableaux = 1

    for shape in shapes:
        if not shape:
            continue
        bottom_length = shape[-1]
        states: Counter[tuple[Row, Permutation]] = Counter()
        for bottom in rows.get(bottom_length, ()):
            states[(bottom, apply_row(identity, bottom))] += 1

        current_length = bottom_length
        for top_length in reversed(shape[:-1]):
            next_states: Counter[tuple[Row, Permutation]] = Counter()
            table = compatibility[(current_length, top_length)]
            for (bottom, permutation), multiplicity in states.items():
                for top in table.get(bottom, ()):
                    next_states[(top, apply_row(permutation, top))] += multiplicity
            states = next_states
            current_length = top_length
            if not states:
                break

        for (_top, permutation), multiplicity in states.items():
            counts[permutation][shape] += multiplicity
            total_tableaux += multiplicity

    return counts, total_tableaux, len(shapes)


def recording_children(
    shape: Shape,
    previous_position: Position | None,
) -> Iterable[tuple[Shape, Position]]:
    """Valid positions for the next largest recording-tableau label."""

    row_count = len(shape)
    for row in range(row_count):
        # Add the new label to the last existing box of this row.
        existing = (row, row + shape[row] - 1)
        if previous_position != existing and (
            row == row_count - 1 or shape[row] > shape[row + 1] + 1
        ):
            yield shape, existing

        # Add a new outer-corner box at the end of this row.
        if row == 0 or shape[row] + 1 < shape[row - 1]:
            new_shape = list(shape)
            new_position = (row, row + shape[row])
            new_shape[row] += 1
            yield tuple(new_shape), new_position

    # Add a new bottom row.
    if not shape or shape[-1] > 1:
        row = len(shape)
        yield shape + (1,), (row, row)


def count_recording_tableaux(
    max_degree: int,
    allowed_shapes: set[Shape],
) -> tuple[dict[Shape, Counter[tuple[int, PeakMask]]], int, int]:
    """Count restricted standard shifted set-valued tableaux.

    States are aggregated by shape, the positions of the two most recent
    labels, and peak set.  The full tableau is unnecessary for future choices.
    """

    counts: dict[Shape, Counter[tuple[int, PeakMask]]] = defaultdict(Counter)
    counts[()][(0, 0)] = 1
    total_tableaux = 1

    # (shape, position of n-1, position of n, peak mask)
    states: Counter[tuple[Shape, Position | None, Position | None, PeakMask]] = Counter()
    states[((), None, None, 0)] = 1
    state_count = 1

    for label in range(1, max_degree + 1):
        next_states: Counter[
            tuple[Shape, Position | None, Position, PeakMask]
        ] = Counter()
        for (shape, previous_previous, previous, peaks), multiplicity in states.items():
            for new_shape, new_position in recording_children(shape, previous):
                new_peaks = peaks
                if (
                    label >= 3
                    and previous_previous is not None
                    and previous is not None
                    and previous_previous[1] < previous[1]
                    and previous[0] < new_position[0]
                ):
                    # The middle label label-1 is a peak.
                    new_peaks |= 1 << (label - 1)
                next_states[(new_shape, previous, new_position, new_peaks)] += multiplicity
        states = next_states
        state_count += len(states)
        for (shape, _previous_previous, _previous, peaks), multiplicity in states.items():
            if shape in allowed_shapes:
                counts[shape][(label, peaks)] += multiplicity
                total_tableaux += multiplicity

    return counts, total_tableaux, state_count


def combine_tableau_counts(
    hecke_counts: dict[Permutation, Counter[Shape]],
    recording_counts: dict[Shape, Counter[tuple[int, PeakMask]]],
) -> Counter[tuple[Permutation, int, PeakMask]]:
    pair_counts: Counter[tuple[Permutation, int, PeakMask]] = Counter()
    for permutation, shapes in hecke_counts.items():
        for shape, hecke_multiplicity in shapes.items():
            for (degree, peaks), recording_multiplicity in recording_counts.get(
                shape, Counter()
            ).items():
                pair_counts[(permutation, degree, peaks)] += (
                    hecke_multiplicity * recording_multiplicity
                )
    return pair_counts


def check(rank: int, max_degree: int, show_mismatches: int) -> dict[str, object]:
    start = time.perf_counter()

    stage = time.perf_counter()
    word_counts, total_words, word_states = count_words(rank, max_degree)
    word_seconds = time.perf_counter() - stage

    stage = time.perf_counter()
    hecke_counts, total_hecke, strict_shape_count = count_hecke_tableaux(
        rank, max_degree
    )
    hecke_seconds = time.perf_counter() - stage

    stage = time.perf_counter()
    allowed_shapes = {shape for shapes in hecke_counts.values() for shape in shapes}
    recording_counts, total_recording, recording_states = count_recording_tableaux(
        max_degree, allowed_shapes
    )
    recording_seconds = time.perf_counter() - stage

    stage = time.perf_counter()
    pair_counts = combine_tableau_counts(hecke_counts, recording_counts)
    all_keys = set(word_counts) | set(pair_counts)
    mismatches = [
        (key, word_counts[key], pair_counts[key])
        for key in all_keys
        if word_counts[key] != pair_counts[key]
    ]
    mismatches.sort(key=lambda item: (item[0][1], item[0][0], item[0][2]))
    compare_seconds = time.perf_counter() - stage

    print("type C peakset-refined finite check")
    print(f"  Coxeter group: W_{rank} (generators 0,...,{rank - 1})")
    print(f"  degrees: 0 <= n <= {max_degree}")
    print(f"  repetition-free words counted: {total_words}")
    print(f"  aggregated word states: {word_states}")
    print(f"  strict shapes considered: {strict_shape_count}")
    print(f"  strict decomposition tableaux: {total_hecke}")
    print(f"  restricted recording tableaux: {total_recording}")
    print(f"  aggregated recording states: {recording_states}")
    print(f"  word-side bins: {len(word_counts)}")
    print(f"  tableau-side bins: {len(pair_counts)}")
    print(f"  mismatched bins: {len(mismatches)}")
    print(
        "  timings seconds: "
        f"words={word_seconds:.3f}, "
        f"Hecke-tableaux={hecke_seconds:.3f}, "
        f"recording-tableaux={recording_seconds:.3f}, "
        f"combine/compare={compare_seconds:.3f}, "
        f"total={time.perf_counter() - start:.3f}"
    )

    for (permutation, degree, peaks), word_value, pair_value in mismatches[
        :show_mismatches
    ]:
        print(
            "  mismatch: "
            f"w={permutation}, n={degree}, Peak={peak_tuple(peaks, degree)}, "
            f"words={word_value}, pairs={pair_value}"
        )

    passed = not mismatches
    print(f"  status: {'PASS' if passed else 'FAIL'}")
    return {
        "passed": passed,
        "mismatches": len(mismatches),
        "total_words": total_words,
        "total_hecke": total_hecke,
        "total_recording": total_recording,
        "elapsed": time.perf_counter() - start,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rank",
        type=int,
        default=4,
        help="Type C rank a; W_a has generators 0,...,a-1 (default: 4).",
    )
    parser.add_argument(
        "--max-degree",
        type=int,
        default=12,
        help="Maximum Hecke-word length / recording-tableau size (default: 12).",
    )
    parser.add_argument(
        "--show-mismatches",
        type=int,
        default=5,
        help="Maximum mismatch records to print (default: 5).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.rank < 1:
        raise SystemExit("rank must be positive")
    if args.max_degree < 0:
        raise SystemExit("max-degree must be nonnegative")
    result = check(args.rank, args.max_degree, args.show_mismatches)
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
