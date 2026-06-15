"""Focused finite checks for the rational dual Dyck symmetric-function formula.

Input parameters are:

* ``t``: rational step;
* ``A``: alphabet size, using the alphabet ``{1, 2, ..., A}``;
* ``L``: maximum word length.

For every length ``1 <= l <= L`` the checker enumerates all words containing
``1``, groups them by multiset and rational dinv, verifies factor-length
symmetry across all positive compositions with the same underlying partition,
and compares the common factorization count with the Dyck-tableau Schur-side
prediction.
"""

from __future__ import annotations

import argparse
import os
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from multiprocessing import Pool
from typing import Iterable

try:
    import numpy as np
    from numba import njit, types
    from numba.typed import Dict
except ImportError:  # pragma: no cover - exercised only on minimal environments.
    np = None
    njit = None
    types = None
    Dict = None


Word = tuple[int, ...]
Composition = tuple[int, ...]
Partition = tuple[int, ...]
Shape = tuple[int, ...]
MultisetKey = int
PartitionMaskData = tuple[Partition, list[Composition], tuple[int, ...]]


@dataclass(frozen=True)
class CheckInput:
    step: int
    alphabet_size: int
    max_length: int
    workers: int = 0


@dataclass
class CheckResult:
    params: CheckInput
    words_generated: int = 0
    words_kept: int = 0
    multisets_checked: int = 0
    dinv_classes_checked: int = 0
    partition_classes_checked: int = 0
    compositions_checked: int = 0
    tableaux_checked: int = 0
    elapsed_seconds: float = 0.0


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dinv_pair(left: int, right: int, *, step: int) -> int:
    if left <= right:
        return max(0, left + step - right)
    return max(0, right + 1 + step - left)


def pair_dinv_table(params: CheckInput) -> tuple[tuple[int, ...], ...]:
    values = range(1, params.alphabet_size + 1)
    return tuple(tuple(dinv_pair(a, b, step=params.step) for b in values) for a in values)


if njit is not None:
    JIT_WORD_RECORD_KEY = types.UniTuple(types.uint64, 3)

    @njit(cache=True)
    def _jit_group_word_records(
        length: int,
        alphabet_size: int,
        pair_dinv_array: np.ndarray,
        base_powers: np.ndarray,
        dinv_limit: int,
        step: int,
        start_word: int,
        stop_word: int,
    ) -> tuple[np.ndarray, np.ndarray, int]:
        counts = np.empty(alphabet_size, dtype=np.int64)
        word = np.empty(length, dtype=np.int64)
        grouped = Dict.empty(key_type=JIT_WORD_RECORD_KEY, value_type=types.int64)
        words_kept = 0

        for encoded_word in range(start_word, stop_word):
            remaining = encoded_word
            has_one = False
            for position in range(length - 1, -1, -1):
                value_index = remaining % alphabet_size
                remaining //= alphabet_size
                word[position] = value_index
                if value_index == 0:
                    has_one = True
            if not has_one:
                continue

            for value_index in range(alphabet_size):
                counts[value_index] = 0

            dinv = 0
            required_dual_cuts = 0
            multiset_key = np.uint64(0)
            previous_index = 0
            for position in range(length):
                value_index = word[position]
                for earlier_index in range(alphabet_size):
                    dinv += counts[earlier_index] * pair_dinv_array[earlier_index, value_index]
                if position > 0:
                    if value_index <= previous_index + step:
                        required_dual_cuts |= 1 << (position - 1)
                previous_index = value_index
                counts[value_index] += 1
                multiset_key += base_powers[value_index]

            record_key = (multiset_key, np.uint64(dinv), np.uint64(required_dual_cuts))
            grouped[record_key] = grouped.get(record_key, 0) + 1
            words_kept += 1

        keys = np.empty((len(grouped), 3), dtype=np.uint64)
        values = np.empty(len(grouped), dtype=np.int64)
        index = 0
        for key, value in grouped.items():
            keys[index, 0] = key[0]
            keys[index, 1] = key[1]
            keys[index, 2] = key[2]
            values[index] = value
            index += 1
        return keys, values, words_kept

else:
    JIT_WORD_RECORD_KEY = None
    _jit_group_word_records = None


def effective_word_group_workers(params: CheckInput, *, length: int, words_generated: int) -> int:
    if _jit_group_word_records is None:
        return 1
    if params.workers < 0:
        raise AssertionError("workers must be non-negative")
    if params.workers > 0:
        return params.workers
    configured = os.environ.get("DYCK_CHECK_WORKERS")
    if configured:
        workers = int(configured)
        require(workers > 0, "DYCK_CHECK_WORKERS must be positive")
        return workers
    if words_generated < 50_000_000:
        return 1
    return min(os.cpu_count() or 1, 8)


def _jit_group_word_records_worker(
    args: tuple[int, int, tuple[tuple[int, ...], ...], int, int, int, int],
) -> tuple[np.ndarray, np.ndarray, int]:
    length, alphabet_size, pair_dinv, dinv_limit, step, start_word, stop_word = args
    base_powers = np.array([(length + 1) ** index for index in range(alphabet_size)], dtype=np.uint64)
    pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
    return _jit_group_word_records(
        length,
        alphabet_size,
        pair_dinv_array,
        base_powers,
        dinv_limit,
        step,
        start_word,
        stop_word,
    )


def partition_shapes(total_size: int) -> Iterable[Shape]:
    def rec(remaining: int, max_part: int, prefix: list[int]) -> Iterable[Shape]:
        if remaining == 0:
            yield tuple(prefix)
            return
        for part in range(min(remaining, max_part), 0, -1):
            prefix.append(part)
            yield from rec(remaining - part, part, prefix)
            prefix.pop()

    yield from rec(total_size, total_size, [])


def positive_compositions(total: int) -> list[Composition]:
    if total <= 0:
        return []
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


def underlying_partition(composition: Composition) -> Partition:
    return tuple(sorted(composition, reverse=True))


def composition_cut_mask(composition: Composition) -> int:
    mask = 0
    position = 0
    total = sum(composition)
    for part in composition[:-1]:
        position += part
        if 0 < position < total:
            mask |= 1 << (position - 1)
    return mask


def composition_groups(length: int) -> list[PartitionMaskData]:
    grouped: defaultdict[Partition, list[tuple[Composition, int]]] = defaultdict(list)
    for composition in positive_compositions(length):
        grouped[underlying_partition(composition)].append((composition, composition_cut_mask(composition)))
    out: list[PartitionMaskData] = []
    for partition, values in grouped.items():
        compositions = [composition for composition, _cut_mask in values]
        cut_masks = tuple(cut_mask for _composition, cut_mask in values)
        out.append((partition, compositions, cut_masks))
    return out


def multiset_from_key(key: MultisetKey, *, alphabet_size: int, length: int) -> Word:
    base = length + 1
    values: list[int] = []
    for index in range(1, alphabet_size + 1):
        multiplicity = key % base
        key //= base
        values.extend([index] * multiplicity)
    return tuple(values)


def group_words_for_length(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> tuple[dict[MultisetKey, dict[int, Counter[int]]], int, int]:
    if _jit_group_word_records is not None:
        return group_words_for_length_jit(length, params=params, pair_dinv=pair_dinv)

    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
    words_generated = params.alphabet_size**length
    words_kept = 0
    base_powers = tuple((length + 1) ** index for index in range(params.alphabet_size))

    for first_one_position in range(length):
        counts = [0] * params.alphabet_size
        active_indices: list[int] = []

        def extend(
            position: int,
            previous_index: int,
            dinv: int,
            required_dual_cuts: int,
            multiset_key: int,
        ) -> None:
            nonlocal words_kept
            if position == length:
                grouped[multiset_key][dinv][required_dual_cuts] += 1
                words_kept += 1
                return

            if position < first_one_position:
                choices = range(1, params.alphabet_size)
            elif position == first_one_position:
                choices = range(1)
            else:
                choices = range(params.alphabet_size)

            for value_index in choices:
                dinv_increment = 0
                for earlier_index in active_indices:
                    dinv_increment += counts[earlier_index] * pair_dinv[earlier_index][value_index]
                next_required_dual_cuts = required_dual_cuts
                if position > 0:
                    previous_value = previous_index + 1
                    current_value = value_index + 1
                    if current_value <= previous_value + params.step:
                        next_required_dual_cuts |= 1 << (position - 1)
                first_value = counts[value_index] == 0
                if first_value:
                    active_indices.append(value_index)
                counts[value_index] += 1
                extend(
                    position + 1,
                    value_index,
                    dinv + dinv_increment,
                    next_required_dual_cuts,
                    multiset_key + base_powers[value_index],
                )
                counts[value_index] -= 1
                if first_value:
                    active_indices.pop()

        extend(0, 0, 0, 0, 0)

    expected_kept = words_generated - (params.alphabet_size - 1) ** length
    require(words_kept == expected_kept, f"internal word-count mismatch for length {length}")
    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}, words_generated, words_kept


def group_words_for_length_jit(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> tuple[dict[MultisetKey, dict[int, Counter[int]]], int, int]:
    require(np is not None, "NumPy is required for the JIT word-grouping backend")
    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[int]]] = defaultdict(lambda: defaultdict(Counter))
    words_generated = params.alphabet_size**length
    max_pair_dinv = max(max(row) for row in pair_dinv)
    dinv_limit = max_pair_dinv * length * (length - 1) // 2 + 1
    base_powers = np.array([(length + 1) ** index for index in range(params.alphabet_size)], dtype=np.uint64)
    pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
    workers = effective_word_group_workers(params, length=length, words_generated=words_generated)

    encoded_counts: dict[tuple[int, int, int], int] = {}
    words_kept = 0
    if workers == 1:
        record_batches = [
            _jit_group_word_records(
                length,
                params.alphabet_size,
                pair_dinv_array,
                base_powers,
                dinv_limit,
                params.step,
                0,
                words_generated,
            )
        ]
    else:
        chunk_size = (words_generated + workers - 1) // workers
        jobs = []
        for worker_index in range(workers):
            start_word = worker_index * chunk_size
            stop_word = min(words_generated, start_word + chunk_size)
            if start_word < stop_word:
                jobs.append(
                    (length, params.alphabet_size, pair_dinv, dinv_limit, params.step, start_word, stop_word)
                )
        with Pool(processes=len(jobs)) as pool:
            record_batches = pool.map(_jit_group_word_records_worker, jobs)

    for encoded_keys, multiplicities, batch_words_kept in record_batches:
        words_kept += batch_words_kept
        for index, multiplicity in enumerate(multiplicities):
            key = (int(encoded_keys[index, 0]), int(encoded_keys[index, 1]), int(encoded_keys[index, 2]))
            encoded_counts[key] = encoded_counts.get(key, 0) + int(multiplicity)

    for (multiset_key, dinv, required_dual_cuts), multiplicity in encoded_counts.items():
        grouped[multiset_key][dinv][required_dual_cuts] = multiplicity

    expected_kept = words_generated - (params.alphabet_size - 1) ** length
    require(words_kept == expected_kept, f"internal word-count mismatch for length {length}")
    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}, words_generated, words_kept


def tableau_shape_groups_for_length(
    length: int,
    *,
    params: CheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> dict[MultisetKey, dict[int, Counter[Shape]]]:
    grouped: defaultdict[MultisetKey, defaultdict[int, Counter[Shape]]] = defaultdict(lambda: defaultdict(Counter))
    base_powers = tuple((length + 1) ** index for index in range(params.alphabet_size))

    for shape in partition_shapes(length):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(row_length)] for row_length in shape]
        for first_one_cell_index in range(length):
            counts = [0] * params.alphabet_size
            active_indices: list[int] = []

            def fill(cell_index: int, dinv: int, multiset_key: int) -> None:
                if cell_index == len(cells):
                    grouped[multiset_key][dinv][shape] += 1
                    return

                row, col = cells[cell_index]
                lower = 1
                if col > 0:
                    lower = rows[row][col - 1] + params.step + 1
                upper = params.alphabet_size
                if row + 1 < len(shape) and col < shape[row + 1]:
                    upper = min(upper, rows[row + 1][col] + params.step)

                if cell_index < first_one_cell_index:
                    lower = max(lower, 2)
                    values = range(lower, upper + 1)
                elif cell_index == first_one_cell_index:
                    if lower > 1 or upper < 1:
                        return
                    values = (1,)
                else:
                    values = range(lower, upper + 1)

                for value in values:
                    value_index = value - 1
                    dinv_increment = 0
                    for earlier_index in active_indices:
                        dinv_increment += counts[earlier_index] * pair_dinv[earlier_index][value_index]
                    rows[row][col] = value
                    first_value = counts[value_index] == 0
                    if first_value:
                        active_indices.append(value_index)
                    counts[value_index] += 1
                    fill(cell_index + 1, dinv + dinv_increment, multiset_key + base_powers[value_index])
                    counts[value_index] -= 1
                    if first_value:
                        active_indices.pop()
                    rows[row][col] = 0

            fill(0, 0, 0)

    return {key: dict(by_dinv) for key, by_dinv in grouped.items()}


def count_ssyt_with_content(shape: Shape, content: Partition) -> int:
    """Return the Kostka number for ``shape`` and dominant content ``content``."""

    if sum(shape) != sum(content):
        return 0
    alphabet_size = len(content)
    if not shape:
        return 1 if not content else 0
    remaining = list(content)
    cells = [(row, col) for row, length in enumerate(shape) for col in range(length)]
    rows = [[-1 for _ in range(length)] for length in shape]
    total = 0

    def rec(cell_index: int) -> None:
        nonlocal total
        if cell_index == len(cells):
            total += 1
            return
        row, col = cells[cell_index]
        min_value = 0
        if col > 0:
            min_value = max(min_value, rows[row][col - 1])
        if row > 0 and col < shape[row - 1]:
            min_value = max(min_value, rows[row - 1][col] + 1)
        for value in range(min_value, alphabet_size):
            if remaining[value] == 0:
                continue
            remaining[value] -= 1
            rows[row][col] = value
            rec(cell_index + 1)
            rows[row][col] = -1
            remaining[value] += 1

    rec(0)
    return total


def dyck_tableau_prediction(
    shape_counts: Counter[Shape],
    partition: Partition,
    *,
    ssyt_cache: dict[tuple[Shape, Partition], int],
) -> int:
    total = 0
    for shape, tableau_count in shape_counts.items():
        key = (shape, partition)
        if key not in ssyt_cache:
            ssyt_cache[key] = count_ssyt_with_content(shape, partition)
        total += tableau_count * ssyt_cache[key]
    return total


def dyck_tableau_predictions(
    shape_counts: Counter[Shape],
    partitions: list[PartitionMaskData],
    *,
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> list[int]:
    if not shape_counts:
        return [0] * len(partitions)
    cache_key = tuple(sorted(shape_counts.items()))
    if cache_key in prediction_cache:
        return prediction_cache[cache_key]
    out = [0] * len(partitions)
    for shape, tableau_count in shape_counts.items():
        for index, (partition, _compositions, _cut_masks) in enumerate(partitions):
            key = (shape, partition)
            if key not in ssyt_cache:
                ssyt_cache[key] = count_ssyt_with_content(shape, partition)
            out[index] += tableau_count * ssyt_cache[key]
    prediction_cache[cache_key] = out
    return out


def valid_factorization_count(mask_counts: Counter[int], cut_mask: int) -> int:
    total = 0
    for required_mask, multiplicity in mask_counts.items():
        if required_mask & ~cut_mask == 0:
            total += multiplicity
    return total


def valid_factorization_counts_by_cut_mask(mask_counts: Counter[int], *, length: int) -> list[int]:
    """Return counts for every cut mask by subset zeta transform."""

    mask_count = 1 << max(0, length - 1)
    counts = [0] * mask_count
    for required_mask, multiplicity in mask_counts.items():
        counts[required_mask] = multiplicity
    for bit in range(max(0, length - 1)):
        bit_mask = 1 << bit
        for mask in range(mask_count):
            if mask & bit_mask:
                counts[mask] += counts[mask ^ bit_mask]
    return counts


def cached_valid_factorization_counts_by_cut_mask(
    mask_counts: Counter[int],
    *,
    length: int,
    cache: dict[tuple[int, tuple[tuple[int, int], ...]], list[int]],
) -> list[int]:
    cache_key = (length, tuple(mask_counts.items()))
    if cache_key not in cache:
        cache[cache_key] = valid_factorization_counts_by_cut_mask(mask_counts, length=length)
    return cache[cache_key]


def check_partition_class(
    *,
    params: CheckInput,
    multiset: Word,
    dinv: int,
    partition: Partition,
    compositions: list[Composition],
    cut_masks: tuple[int, ...],
    valid_by_cut_mask: list[int],
    predicted: int,
) -> int:
    actual = valid_by_cut_mask[cut_masks[0]]
    for index in range(1, len(cut_masks)):
        if valid_by_cut_mask[cut_masks[index]] != actual:
            values = {
                composition: valid_by_cut_mask[cut_mask]
                for composition, cut_mask in zip(compositions, cut_masks)
            }
            examples = sorted(values.items())[:8]
            raise AssertionError(
                "factorization symmetry mismatch: "
                f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                f"partition={partition}, examples={examples}"
            )
    if actual != predicted:
        values = {
            composition: valid_by_cut_mask[cut_mask]
            for composition, cut_mask in zip(compositions, cut_masks)
        }
        examples = sorted(values.items())[:8]
        raise AssertionError(
            "Dyck-tableau prediction mismatch: "
            f"t={params.step}, multiset={multiset}, dinv={dinv}, "
            f"partition={partition}, factorization_count={actual}, "
            f"tableau_prediction={predicted}, examples={examples}"
        )
    return len(compositions)


def run_check(params: CheckInput) -> CheckResult:
    require(params.step >= 0, "t must be non-negative")
    require(params.alphabet_size > 0, "alphabet size A must be positive")
    require(params.max_length > 0, "max length L must be positive")

    start = time.perf_counter()
    result = CheckResult(params=params)
    pair_dinv = pair_dinv_table(params)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    valid_cut_mask_cache: dict[tuple[int, tuple[tuple[int, int], ...]], list[int]] = {}

    for length in range(1, params.max_length + 1):
        length_start = time.perf_counter()
        word_groups, words_generated, words_kept = group_words_for_length(
            length,
            params=params,
            pair_dinv=pair_dinv,
        )
        tableau_groups = tableau_shape_groups_for_length(
            length,
            params=params,
            pair_dinv=pair_dinv,
        )
        partitions = composition_groups(length)
        result.words_generated += words_generated
        result.words_kept += words_kept

        length_multisets = 0
        length_dinv_classes = 0
        length_partition_classes = 0
        for key in sorted(set(word_groups) | set(tableau_groups)):
            multiset = multiset_from_key(key, alphabet_size=params.alphabet_size, length=length)
            words_by_dinv = word_groups.get(key, {})
            tableaux_by_dinv = tableau_groups.get(key, {})
            length_multisets += 1
            for dinv in sorted(set(words_by_dinv) | set(tableaux_by_dinv)):
                length_dinv_classes += 1
                mask_counts = words_by_dinv.get(dinv, Counter())
                valid_by_cut_mask = cached_valid_factorization_counts_by_cut_mask(
                    mask_counts,
                    length=length,
                    cache=valid_cut_mask_cache,
                )
                shape_counts = tableaux_by_dinv.get(dinv, Counter())
                result.tableaux_checked += sum(shape_counts.values())
                predictions = dyck_tableau_predictions(
                    shape_counts,
                    partitions,
                    ssyt_cache=ssyt_cache,
                    prediction_cache=prediction_cache,
                )
                for partition_index, (partition, compositions, cut_masks) in enumerate(partitions):
                    actual = valid_by_cut_mask[cut_masks[0]]
                    for cut_mask in cut_masks[1:]:
                        if valid_by_cut_mask[cut_mask] != actual:
                            values = {
                                composition: valid_by_cut_mask[composition_cut_mask]
                                for composition, composition_cut_mask in zip(compositions, cut_masks)
                            }
                            examples = sorted(values.items())[:8]
                            raise AssertionError(
                                "factorization symmetry mismatch: "
                                f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                                f"partition={partition}, examples={examples}"
                            )
                    predicted = predictions[partition_index]
                    if actual != predicted:
                        values = {
                            composition: valid_by_cut_mask[composition_cut_mask]
                            for composition, composition_cut_mask in zip(compositions, cut_masks)
                        }
                        examples = sorted(values.items())[:8]
                        raise AssertionError(
                            "Dyck-tableau prediction mismatch: "
                            f"t={params.step}, multiset={multiset}, dinv={dinv}, "
                            f"partition={partition}, factorization_count={actual}, "
                            f"tableau_prediction={predicted}, examples={examples}"
                        )
                    result.compositions_checked += len(compositions)
                    length_partition_classes += 1

        result.multisets_checked += length_multisets
        result.dinv_classes_checked += length_dinv_classes
        result.partition_classes_checked += length_partition_classes
        print(
            f"  length={length}: generated={words_generated}, kept={words_kept}, "
            f"multisets={length_multisets}, dinv classes={length_dinv_classes}, "
            f"partitions={length_partition_classes}, elapsed={time.perf_counter() - length_start:.3f}s",
            flush=True,
        )

    result.elapsed_seconds = time.perf_counter() - start
    return result


def print_result(result: CheckResult) -> None:
    params = result.params
    print(f"completed: t={params.step}, alphabet={{1,...,{params.alphabet_size}}}, lengths<= {params.max_length}")
    print(f"  words generated: {result.words_generated}")
    print(f"  1-containing words checked: {result.words_kept}")
    print(f"  multisets checked: {result.multisets_checked}")
    print(f"  dinv classes checked: {result.dinv_classes_checked}")
    print(f"  partition classes checked: {result.partition_classes_checked}")
    print(f"  positive compositions checked: {result.compositions_checked}")
    print(f"  Dyck tableaux checked: {result.tableaux_checked}")
    print(f"  elapsed: {result.elapsed_seconds:.3f}s")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, required=True, help="Rational step t.")
    parser.add_argument("--alphabet-size", "-A", type=int, required=True, help="Alphabet size A.")
    parser.add_argument("--max-length", "-L", type=int, required=True, help="Maximum word length L.")
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Word-grouping worker processes. Use 0 for automatic selection.",
    )
    args = parser.parse_args()

    result = run_check(
        CheckInput(
            step=args.t,
            alphabet_size=args.alphabet_size,
            max_length=args.max_length,
            workers=args.workers,
        )
    )
    print_result(result)
    print("all requested finite checks passed")


if __name__ == "__main__":
    main()
