"""Readable finite checks for Dyck symmetric functions.

This file is intended for the simplified repository item

    contents/dyck_symmetric_functions/code.py

It is a small, dependency-free reference implementation.  It is not the highly
optimized checker used for the largest recorded runs.

Mathematical scope
------------------
Fix a nonnegative integer step parameter tau.  For tau = 1 these are the
classical Dyck and dual Dyck symmetric functions from the 2026 paper.  For
r = s*tau + 1 and tau > 1, the same Schur expansions are conjectural.

For a finite multiset S and dinv value d, the conjectural formulas are

    DS_dual^(tau)(S,d)   = sum_P s_{shape(P)}
    DS_affine^(tau)(S,d) = sum_P s_{shape(P)'}

where P ranges over step-tau rational Dyck tableaux with entries S and
rational dinv d.

What this script checks
-----------------------
For bounded alphabets {1,...,A} and lengths <= L, the script enumerates every
multiset containing 1, every word with that multiset, and every step-tau
rational Dyck tableau with that multiset.  For each multiset and dinv class it
compares coefficient counts in the monomial basis:

* dual mode: consecutive factors must satisfy x[i+1] > x[i] + tau;
* affine mode: consecutive factors must satisfy x[i+1] <= x[i] + tau.

For each positive composition alpha of the length, alpha determines the factor
lengths.  The actual count is the number of words with the requested multiset
and dinv whose forced cuts are contained in the cut set of alpha.  The Schur
side is computed by Kostka numbers: the coefficient of a monomial with content
alpha in s_lambda is the number of SSYT of shape lambda and content the sorted
partition of alpha.

The official larger computations were performed with optimized code.  They are
recorded below for reference and are not run by default.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable, Literal, Sequence


Word = tuple[int, ...]
Counts = tuple[int, ...]
Composition = tuple[int, ...]
Partition = tuple[int, ...]
Shape = tuple[int, ...]
Mode = Literal["dual", "affine"]


RECORDED_EXHAUSTIVE_BOXES: tuple[tuple[int, int, int], ...] = (
    # (tau, alphabet_size, max_length)
    (2, 10, 10),
    (3, 13, 9),
    (4, 16, 8),
)

RECORDED_RANDOM_CLASS_CHECKS: tuple[tuple[int, int, int, int], ...] = (
    # (tau, alphabet_size, length, sampled_classes)
    (2, 11, 12, 100),
    (3, 14, 11, 100),
    (4, 17, 10, 100),
)


@dataclass(frozen=True)
class BoxCheckResult:
    tau: int
    alphabet_size: int
    max_length: int
    modes: tuple[Mode, ...]
    multisets_checked: int
    dinv_classes_checked: int
    partition_classes_checked: int
    compositions_checked: int
    words_checked: int
    tableaux_checked: int
    elapsed_seconds: float


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


# ---------------------------------------------------------------------------
# Basic step-tau statistics and local conditions
# ---------------------------------------------------------------------------


def pair_dinv_tau(left: int, right: int, tau: int) -> int:
    """Return the contribution d_tau(left,right)."""

    require(tau >= 0, "tau must be nonnegative")
    if left <= right:
        return max(0, left + tau - right)
    return max(0, right + 1 + tau - left)


def dinv_tau(word: Sequence[int], tau: int) -> int:
    """Return rational dinv for a finite integer word."""

    values = tuple(word)
    return sum(
        pair_dinv_tau(values[i], values[j], tau)
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )


def is_dual_tau_dyck(word: Sequence[int], tau: int) -> bool:
    """Check the dual condition x[i+1] > x[i] + tau."""

    values = tuple(word)
    return all(value >= 0 for value in values) and all(
        values[i + 1] > values[i] + tau for i in range(len(values) - 1)
    )


def is_affine_tau_dyck(word: Sequence[int], tau: int) -> bool:
    """Check the affine condition x[i+1] <= x[i] + tau."""

    values = tuple(word)
    return all(value >= 0 for value in values) and all(
        values[i + 1] <= values[i] + tau for i in range(len(values) - 1)
    )


def required_cut_mask(word: Word, tau: int, mode: Mode) -> int:
    """Return adjacent cuts forced by the chosen factor condition.

    Bit i corresponds to the cut between word[i] and word[i+1].
    """

    mask = 0
    for i in range(len(word) - 1):
        same_factor_allowed = (
            word[i + 1] > word[i] + tau
            if mode == "dual"
            else word[i + 1] <= word[i] + tau
        )
        if not same_factor_allowed:
            mask |= 1 << i
    return mask


# ---------------------------------------------------------------------------
# Partitions, compositions, and Schur coefficients
# ---------------------------------------------------------------------------


def partition_shapes(total: int) -> list[Shape]:
    """Return all integer partition shapes of total, in reverse lexicographic order."""

    require(total >= 0, "total must be nonnegative")
    out: list[Shape] = []

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for part in range(min(remaining, max_part), 0, -1):
            prefix.append(part)
            rec(remaining - part, part, prefix)
            prefix.pop()

    rec(total, total, [])
    return out


def conjugate_partition(shape: Sequence[int]) -> Shape:
    """Return the conjugate partition."""

    values = tuple(shape)
    if not values:
        return ()
    require(all(values[i] >= values[i + 1] for i in range(len(values) - 1)), "shape must be a partition")
    return tuple(sum(1 for part in values if part >= col) for col in range(1, values[0] + 1))


def positive_compositions(total: int) -> list[Composition]:
    """Return all positive compositions of total."""

    require(total > 0, "total must be positive")
    out: list[Composition] = []

    def rec(remaining: int, prefix: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for part in range(1, remaining + 1):
            prefix.append(part)
            rec(remaining - part, prefix)
            prefix.pop()

    rec(total, [])
    return out


def composition_cut_mask(composition: Sequence[int]) -> int:
    """Return cut positions determined by a composition of a word length."""

    mask = 0
    position = 0
    total = sum(composition)
    for part in composition[:-1]:
        position += part
        require(0 < position < total, "composition has an invalid internal cut")
        mask |= 1 << (position - 1)
    return mask


def composition_groups(total: int) -> dict[Partition, list[tuple[Composition, int]]]:
    """Group positive compositions by their sorted underlying partition."""

    grouped: dict[Partition, list[tuple[Composition, int]]] = defaultdict(list)
    for composition in positive_compositions(total):
        partition = tuple(sorted(composition, reverse=True))
        grouped[partition].append((composition, composition_cut_mask(composition)))
    return dict(grouped)


def count_ssyt_with_content(shape: Shape, content: Partition) -> int:
    """Return the Kostka number K_{shape,content} by direct SSYT enumeration.

    The entries are 1,...,len(content).  Rows are weakly increasing and columns
    are strictly increasing from top to bottom.
    """

    if sum(shape) != sum(content):
        return 0
    if not shape:
        return 1 if not content else 0
    if len(shape) > sum(1 for part in content if part > 0) and shape and shape[0] == 1:
        # This shortcut is optional; the recursion below also handles it.
        pass

    alphabet_size = len(content)
    remaining = list(content)
    rows = [[0 for _ in range(row_length)] for row_length in shape]
    cells = [(row, col) for row, row_length in enumerate(shape) for col in range(row_length)]
    total = 0

    def rec(cell_index: int) -> None:
        nonlocal total
        if cell_index == len(cells):
            total += 1
            return
        row, col = cells[cell_index]
        lower = 1
        if col > 0:
            lower = max(lower, rows[row][col - 1])
        if row > 0 and col < shape[row - 1]:
            lower = max(lower, rows[row - 1][col] + 1)
        for value in range(lower, alphabet_size + 1):
            if remaining[value - 1] == 0:
                continue
            remaining[value - 1] -= 1
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = 0
            remaining[value - 1] += 1

    rec(0)
    return total


# ---------------------------------------------------------------------------
# Multisets, words, and rational Dyck tableaux
# ---------------------------------------------------------------------------


def count_vectors(length: int, alphabet_size: int, *, require_one: bool = True) -> Iterable[Counts]:
    """Yield multiplicity vectors over {1,...,alphabet_size}.

    The exhaustive rational checker uses the normalization that the multiset
    contains 1.  This avoids repeating translation-equivalent classes.
    """

    require(length > 0, "length must be positive")
    require(alphabet_size > 0, "alphabet size must be positive")
    counts = [0] * alphabet_size

    def rec(index: int, remaining: int) -> Iterable[Counts]:
        if index == alphabet_size - 1:
            counts[index] = remaining
            if not require_one or counts[0] > 0:
                yield tuple(counts)
            counts[index] = 0
            return
        for value in range(remaining + 1):
            counts[index] = value
            yield from rec(index + 1, remaining - value)
            counts[index] = 0

    yield from rec(0, length)


def values_from_counts(counts: Counts) -> Word:
    """Expand counts over {1,...,A} into a sorted tuple of values."""

    values: list[int] = []
    for index, multiplicity in enumerate(counts, start=1):
        values.extend([index] * multiplicity)
    return tuple(values)


def unique_words_from_counts(counts: Counts) -> Iterable[Word]:
    """Yield all distinct words with the requested multiplicities."""

    remaining = list(counts)
    length = sum(counts)
    prefix: list[int] = []

    def rec() -> Iterable[Word]:
        if len(prefix) == length:
            yield tuple(prefix)
            return
        for index, multiplicity in enumerate(remaining):
            if multiplicity == 0:
                continue
            remaining[index] -= 1
            prefix.append(index + 1)
            yield from rec()
            prefix.pop()
            remaining[index] += 1

    yield from rec()


def word_mask_counts_by_dinv(counts: Counts, tau: int, mode: Mode) -> tuple[dict[int, Counter[int]], int]:
    """Group words by dinv and required factor-cut mask."""

    grouped: dict[int, Counter[int]] = defaultdict(Counter)
    words_checked = 0
    for word in unique_words_from_counts(counts):
        words_checked += 1
        grouped[dinv_tau(word, tau)][required_cut_mask(word, tau, mode)] += 1
    return dict(grouped), words_checked


def is_tau_dyck_tableau(tableau: Sequence[Sequence[int]], tau: int) -> bool:
    """Check the step-tau rational Dyck tableau condition.

    Rows are stored top-to-bottom.  Each row is dual.  Each column, read from
    bottom to top, is affine.  Equivalently, an upper entry is at most tau
    larger than the entry immediately below it.
    """

    rows = tuple(tuple(row) for row in tableau)
    shape = tuple(len(row) for row in rows)
    if any(part <= 0 for part in shape):
        return not shape
    if any(shape[i] < shape[i + 1] for i in range(len(shape) - 1)):
        return False
    if any(not is_dual_tau_dyck(row, tau) for row in rows):
        return False
    for row in range(len(rows) - 1):
        upper = rows[row]
        lower = rows[row + 1]
        for col in range(len(lower)):
            if upper[col] > lower[col] + tau:
                return False
    return True


def row_reading_word(tableau: Sequence[Sequence[int]]) -> Word:
    """Read rows left-to-right from bottom row to top row."""

    rows = tuple(tuple(row) for row in tableau)
    return tuple(value for row in reversed(rows) for value in row)


def tableau_shape_counts_by_dinv(counts: Counts, tau: int) -> tuple[dict[int, Counter[Shape]], int]:
    """Enumerate rational Dyck tableaux with fixed content.

    The output maps dinv(row-reading word) to a counter of tableau shapes.
    """

    total_size = sum(counts)
    grouped: dict[int, Counter[Shape]] = defaultdict(Counter)
    tableaux_checked = 0

    for shape in partition_shapes(total_size):
        rows = [[0 for _ in range(row_length)] for row_length in shape]
        remaining = list(counts)
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]

        def valid_cell(row: int, col: int, value: int) -> bool:
            if col > 0 and value <= rows[row][col - 1] + tau:
                return False
            if row + 1 < len(shape) and col < shape[row + 1]:
                if value > rows[row + 1][col] + tau:
                    return False
            return True

        def rec(cell_index: int) -> None:
            nonlocal tableaux_checked
            if cell_index == len(cells):
                tableau = tuple(tuple(row) for row in rows)
                require(is_tau_dyck_tableau(tableau, tau), f"internal tableau error: {tableau}")
                grouped[dinv_tau(row_reading_word(tableau), tau)][shape] += 1
                tableaux_checked += 1
                return
            row, col = cells[cell_index]
            for value_index, multiplicity in enumerate(remaining):
                if multiplicity == 0:
                    continue
                value = value_index + 1
                if not valid_cell(row, col, value):
                    continue
                remaining[value_index] -= 1
                rows[row][col] = value
                rec(cell_index + 1)
                rows[row][col] = 0
                remaining[value_index] += 1

        rec(0)

    return dict(grouped), tableaux_checked


# ---------------------------------------------------------------------------
# Coefficient comparisons
# ---------------------------------------------------------------------------


def valid_factorization_count(mask_counts: Counter[int], cut_mask: int) -> int:
    """Count words whose required cuts are contained in cut_mask."""

    return sum(multiplicity for required, multiplicity in mask_counts.items() if required & ~cut_mask == 0)


def schur_prediction(
    shape_counts: Counter[Shape],
    content_partition: Partition,
    *,
    mode: Mode,
    kostka_cache: dict[tuple[Shape, Partition], int],
) -> int:
    """Return the Schur-side coefficient for one content partition."""

    total = 0
    for shape, multiplicity in shape_counts.items():
        schur_shape = shape if mode == "dual" else conjugate_partition(shape)
        key = (schur_shape, content_partition)
        if key not in kostka_cache:
            kostka_cache[key] = count_ssyt_with_content(schur_shape, content_partition)
        total += multiplicity * kostka_cache[key]
    return total


def check_one_multiset(
    counts: Counts,
    *,
    tau: int,
    mode: Mode,
    composition_data: dict[Partition, list[tuple[Composition, int]]],
    kostka_cache: dict[tuple[Shape, Partition], int],
) -> tuple[int, int, int, int]:
    """Check one multiset in one mode.

    Returns:
        (dinv_classes_checked, partition_classes_checked,
         compositions_checked, tableaux_checked)
    """

    word_groups, _words_checked = word_mask_counts_by_dinv(counts, tau, mode)
    tableau_groups, tableaux_checked = tableau_shape_counts_by_dinv(counts, tau)
    dinv_values = sorted(set(word_groups) | set(tableau_groups))
    partition_classes_checked = 0
    compositions_checked = 0

    for dinv in dinv_values:
        mask_counts = word_groups.get(dinv, Counter())
        shape_counts = tableau_groups.get(dinv, Counter())
        for content_partition, comp_and_masks in composition_data.items():
            actual_values = {
                composition: valid_factorization_count(mask_counts, cut_mask)
                for composition, cut_mask in comp_and_masks
            }
            actual_set = set(actual_values.values())
            if len(actual_set) != 1:
                examples = sorted(actual_values.items())[:8]
                raise AssertionError(
                    "factorization coefficients are not symmetric: "
                    f"tau={tau}, mode={mode}, counts={counts}, dinv={dinv}, "
                    f"content_partition={content_partition}, examples={examples}"
                )
            actual = next(iter(actual_set))
            predicted = schur_prediction(
                shape_counts,
                content_partition,
                mode=mode,
                kostka_cache=kostka_cache,
            )
            if actual != predicted:
                raise AssertionError(
                    "Schur-side prediction mismatch: "
                    f"tau={tau}, mode={mode}, counts={counts}, values={values_from_counts(counts)}, "
                    f"dinv={dinv}, content_partition={content_partition}, "
                    f"actual={actual}, predicted={predicted}, shape_counts={dict(shape_counts)}"
                )
            partition_classes_checked += 1
            compositions_checked += len(comp_and_masks)

    return len(dinv_values), partition_classes_checked, compositions_checked, tableaux_checked


def check_box(
    *,
    tau: int,
    alphabet_size: int,
    max_length: int,
    modes: Sequence[Mode] = ("dual",),
) -> BoxCheckResult:
    """Run finite Schur-expansion checks over a normalized bounded box."""

    require(tau >= 0, "tau must be nonnegative")
    require(alphabet_size > 0, "alphabet size must be positive")
    require(max_length > 0, "max length must be positive")
    mode_tuple = tuple(modes)
    require(bool(mode_tuple), "at least one mode must be requested")
    require(all(mode in ("dual", "affine") for mode in mode_tuple), "unknown mode")

    start = time.perf_counter()
    multisets_checked = 0
    dinv_classes_checked = 0
    partition_classes_checked = 0
    compositions_checked = 0
    words_checked = 0
    tableaux_checked = 0
    kostka_cache: dict[tuple[Shape, Partition], int] = {}

    for length in range(1, max_length + 1):
        composition_data = composition_groups(length)
        length_multisets = 0
        for counts in count_vectors(length, alphabet_size, require_one=True):
            length_multisets += 1
            multisets_checked += 1
            # Count words once per multiset for reporting.  The per-mode helper
            # recomputes masks because the forced cuts depend on the mode.
            words_checked += sum(1 for _ in unique_words_from_counts(counts))
            for mode in mode_tuple:
                dc, pc, cc, tc = check_one_multiset(
                    counts,
                    tau=tau,
                    mode=mode,
                    composition_data=composition_data,
                    kostka_cache=kostka_cache,
                )
                dinv_classes_checked += dc
                partition_classes_checked += pc
                compositions_checked += cc
                tableaux_checked += tc
        print(
            f"length={length}: multisets={length_multisets}, modes={','.join(mode_tuple)}",
            flush=True,
        )

    return BoxCheckResult(
        tau=tau,
        alphabet_size=alphabet_size,
        max_length=max_length,
        modes=mode_tuple,
        multisets_checked=multisets_checked,
        dinv_classes_checked=dinv_classes_checked,
        partition_classes_checked=partition_classes_checked,
        compositions_checked=compositions_checked,
        words_checked=words_checked,
        tableaux_checked=tableaux_checked,
        elapsed_seconds=time.perf_counter() - start,
    )


def print_recorded_checks() -> None:
    """Print the large recorded checks from the optimized implementation."""

    print("recorded exhaustive boxes from the optimized checker:")
    for tau, alphabet_size, max_length in RECORDED_EXHAUSTIVE_BOXES:
        print(f"  tau={tau}, alphabet_size={alphabet_size}, max_length={max_length}")
    print("recorded sampled class checks:")
    for tau, alphabet_size, length, samples in RECORDED_RANDOM_CLASS_CHECKS:
        print(f"  tau={tau}, alphabet_size={alphabet_size}, length={length}, sampled_classes={samples}")


def parse_modes(text: str) -> tuple[Mode, ...]:
    if text == "both":
        return ("dual", "affine")
    if text in ("dual", "affine"):
        return (text,)  # type: ignore[return-value]
    raise argparse.ArgumentTypeError("mode must be 'dual', 'affine', or 'both'")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tau", type=int, default=2, help="step parameter tau")
    parser.add_argument("--alphabet-size", "-A", type=int, default=4, help="alphabet {1,...,A}")
    parser.add_argument("--max-length", "-L", type=int, default=4, help="check every length <= L")
    parser.add_argument("--mode", type=parse_modes, default=("dual", "affine"), help="dual, affine, or both")
    parser.add_argument(
        "--show-recorded",
        action="store_true",
        help="print the larger recorded optimized checks before running the small check",
    )
    args = parser.parse_args()

    if args.show_recorded:
        print_recorded_checks()
        print()

    result = check_box(
        tau=args.tau,
        alphabet_size=args.alphabet_size,
        max_length=args.max_length,
        modes=args.mode,
    )
    print("finite Dyck symmetric function check passed")
    print(f"  tau: {result.tau}")
    print(f"  alphabet_size: {result.alphabet_size}")
    print(f"  max_length: {result.max_length}")
    print(f"  modes: {', '.join(result.modes)}")
    print(f"  multisets_checked: {result.multisets_checked}")
    print(f"  dinv_classes_checked: {result.dinv_classes_checked}")
    print(f"  partition_classes_checked: {result.partition_classes_checked}")
    print(f"  compositions_checked: {result.compositions_checked}")
    print(f"  words_checked: {result.words_checked}")
    print(f"  tableaux_checked: {result.tableaux_checked}")
    print(f"  elapsed_seconds: {result.elapsed_seconds:.3f}")


if __name__ == "__main__":
    main()
