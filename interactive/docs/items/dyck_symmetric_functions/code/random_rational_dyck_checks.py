"""Monte Carlo checks for rational dual Dyck symmetric-function classes.

Each trial samples one word uniformly from ``{1, ..., A}^L``.  The sampled word
selects a multiset and dinv value; the checker then exhaustively verifies the
usual factorization-symmetry and Dyck-tableau prediction for that single class.
"""

from __future__ import annotations

import argparse
import random
import time
from collections import Counter
from dataclasses import dataclass
from multiprocessing import Pool

try:
    import numpy as np
    from numba import njit, types
    from numba.typed import Dict
except ImportError:  # pragma: no cover - fallback path for minimal environments.
    np = None
    njit = None
    types = None
    Dict = None

from check_rational_dyck_generalization import (
    CheckInput,
    Composition,
    Partition,
    PartitionMaskData,
    Shape,
    Word,
    composition_groups,
    count_ssyt_with_content,
    dyck_tableau_predictions,
    pair_dinv_table,
    partition_shapes,
    valid_factorization_counts_by_cut_mask,
)


if njit is not None:

    @njit
    def _jit_class_word_extend(
        position: int,
        previous_index: int,
        dinv: int,
        required_dual_cuts: int,
        active_count: int,
        target_dinv: int,
        length: int,
        alphabet_size: int,
        step: int,
        pair_dinv_array: np.ndarray,
        remaining: np.ndarray,
        used_counts: np.ndarray,
        active_indices: np.ndarray,
        mask_counts: Dict,
    ) -> None:
        if dinv > target_dinv:
            return
        if position == length:
            if dinv == target_dinv:
                mask_counts[required_dual_cuts] = mask_counts.get(required_dual_cuts, 0) + 1
            return

        for value_index in range(alphabet_size):
            if remaining[value_index] == 0:
                continue
            dinv_increment = 0
            for active_position in range(active_count):
                earlier_index = active_indices[active_position]
                dinv_increment += used_counts[earlier_index] * pair_dinv_array[earlier_index, value_index]
            next_dinv = dinv + dinv_increment
            if next_dinv > target_dinv:
                continue

            next_required_dual_cuts = required_dual_cuts
            if position > 0 and value_index <= previous_index + step:
                next_required_dual_cuts |= 1 << (position - 1)

            next_active_count = active_count
            if used_counts[value_index] == 0:
                active_indices[next_active_count] = value_index
                next_active_count += 1
            remaining[value_index] -= 1
            used_counts[value_index] += 1
            _jit_class_word_extend(
                position + 1,
                value_index,
                next_dinv,
                next_required_dual_cuts,
                next_active_count,
                target_dinv,
                length,
                alphabet_size,
                step,
                pair_dinv_array,
                remaining,
                used_counts,
                active_indices,
                mask_counts,
            )
            used_counts[value_index] -= 1
            remaining[value_index] += 1


    @njit
    def _jit_class_word_mask_counts(
        counts: np.ndarray,
        target_dinv: int,
        length: int,
        alphabet_size: int,
        step: int,
        pair_dinv_array: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray]:
        remaining = counts.copy()
        used_counts = np.zeros(alphabet_size, dtype=np.int64)
        active_indices = np.empty(alphabet_size, dtype=np.int64)
        mask_counts = Dict.empty(key_type=types.int64, value_type=types.int64)
        _jit_class_word_extend(
            0,
            0,
            0,
            0,
            0,
            target_dinv,
            length,
            alphabet_size,
            step,
            pair_dinv_array,
            remaining,
            used_counts,
            active_indices,
            mask_counts,
        )
        keys = np.empty(len(mask_counts), dtype=np.int64)
        values = np.empty(len(mask_counts), dtype=np.int64)
        index = 0
        for key, value in mask_counts.items():
            keys[index] = key
            values[index] = value
            index += 1
        return keys, values

else:
    _jit_class_word_mask_counts = None


@dataclass(frozen=True)
class RandomCheckInput:
    step: int
    alphabet_size: int
    length: int
    iterations: int
    timeout_seconds: float | None
    seed: int | None
    workers: int = 1


@dataclass
class RandomCheckResult:
    params: RandomCheckInput
    iterations_completed: int = 0
    sampled_words: int = 0
    class_words_checked: int = 0
    dyck_tableaux_checked: int = 0
    partition_classes_checked: int = 0
    compositions_checked: int = 0
    elapsed_seconds: float = 0.0


@dataclass
class TrialSummary:
    iteration: int
    sample_word: Word
    target_dinv: int
    class_words: int
    tableaux: int
    partition_classes: int
    compositions: int
    elapsed_seconds: float


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def random_word(*, length: int, alphabet_size: int, rng: random.Random) -> Word:
    return tuple(rng.randint(1, alphabet_size) for _ in range(length))


def counts_from_word(word: Word, *, alphabet_size: int) -> tuple[int, ...]:
    counts = [0] * alphabet_size
    for value in word:
        counts[value - 1] += 1
    return tuple(counts)


def multiset_from_counts(counts: tuple[int, ...]) -> Word:
    values: list[int] = []
    for index, multiplicity in enumerate(counts, start=1):
        values.extend([index] * multiplicity)
    return tuple(values)


def word_dinv(word: Word, pair_dinv: tuple[tuple[int, ...], ...]) -> int:
    total = 0
    for right in range(len(word)):
        right_index = word[right] - 1
        for left in range(right):
            total += pair_dinv[word[left] - 1][right_index]
    return total


def class_word_mask_counts(
    *,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> Counter[int]:
    if _jit_class_word_mask_counts is not None:
        counts_array = np.array(counts, dtype=np.int64)
        pair_dinv_array = np.array(pair_dinv, dtype=np.int64)
        keys, values = _jit_class_word_mask_counts(
            counts_array,
            target_dinv,
            params.length,
            params.alphabet_size,
            params.step,
            pair_dinv_array,
        )
        return Counter({int(key): int(value) for key, value in zip(keys, values)})

    remaining = list(counts)
    used_counts = [0] * params.alphabet_size
    active_indices: list[int] = []
    mask_counts: Counter[int] = Counter()

    def extend(position: int, previous_index: int, dinv: int, required_dual_cuts: int) -> None:
        if dinv > target_dinv:
            return
        if position == params.length:
            if dinv == target_dinv:
                mask_counts[required_dual_cuts] += 1
            return

        for value_index in range(params.alphabet_size):
            if remaining[value_index] == 0:
                continue
            dinv_increment = 0
            for earlier_index in active_indices:
                dinv_increment += used_counts[earlier_index] * pair_dinv[earlier_index][value_index]
            next_dinv = dinv + dinv_increment
            if next_dinv > target_dinv:
                continue

            next_required_dual_cuts = required_dual_cuts
            if position > 0 and value_index <= previous_index + params.step:
                next_required_dual_cuts |= 1 << (position - 1)

            first_value = used_counts[value_index] == 0
            if first_value:
                active_indices.append(value_index)
            remaining[value_index] -= 1
            used_counts[value_index] += 1
            extend(position + 1, value_index, next_dinv, next_required_dual_cuts)
            used_counts[value_index] -= 1
            remaining[value_index] += 1
            if first_value:
                active_indices.pop()

    extend(0, 0, 0, 0)
    return mask_counts


def class_tableau_shape_counts(
    *,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
) -> Counter[Shape]:
    shape_counts: Counter[Shape] = Counter()

    for shape in partition_shapes(params.length):
        cells = [(row, col) for row in range(len(shape) - 1, -1, -1) for col in range(shape[row])]
        rows = [[0 for _ in range(row_length)] for row_length in shape]
        remaining = list(counts)
        used_counts = [0] * params.alphabet_size
        active_indices: list[int] = []

        def fill(cell_index: int, dinv: int) -> None:
            if dinv > target_dinv:
                return
            if cell_index == len(cells):
                if dinv == target_dinv:
                    shape_counts[shape] += 1
                return

            row, col = cells[cell_index]
            lower = 1
            if col > 0:
                lower = rows[row][col - 1] + params.step + 1
            upper = params.alphabet_size
            if row + 1 < len(shape) and col < shape[row + 1]:
                upper = min(upper, rows[row + 1][col] + params.step)

            for value in range(lower, upper + 1):
                value_index = value - 1
                if remaining[value_index] == 0:
                    continue
                dinv_increment = 0
                for earlier_index in active_indices:
                    dinv_increment += used_counts[earlier_index] * pair_dinv[earlier_index][value_index]
                next_dinv = dinv + dinv_increment
                if next_dinv > target_dinv:
                    continue

                first_value = used_counts[value_index] == 0
                if first_value:
                    active_indices.append(value_index)
                remaining[value_index] -= 1
                used_counts[value_index] += 1
                rows[row][col] = value
                fill(cell_index + 1, next_dinv)
                rows[row][col] = 0
                used_counts[value_index] -= 1
                remaining[value_index] += 1
                if first_value:
                    active_indices.pop()

        fill(0, 0)

    return shape_counts


def verify_sampled_class(
    *,
    sample_word: Word,
    counts: tuple[int, ...],
    target_dinv: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
    partitions: list[PartitionMaskData],
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> tuple[int, int, int, int]:
    mask_counts = class_word_mask_counts(
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
    )
    class_word_count = sum(mask_counts.values())
    require(
        class_word_count > 0,
        f"internal error: sampled word class is empty for word={sample_word}, dinv={target_dinv}",
    )
    shape_counts = class_tableau_shape_counts(
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
    )
    valid_by_cut_mask = valid_factorization_counts_by_cut_mask(mask_counts, length=params.length)
    predictions = dyck_tableau_predictions(
        shape_counts,
        partitions,
        ssyt_cache=ssyt_cache,
        prediction_cache=prediction_cache,
    )
    multiset = multiset_from_counts(counts)
    partition_classes_checked = 0
    compositions_checked = 0

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
                    f"t={params.step}, sample_word={sample_word}, multiset={multiset}, "
                    f"dinv={target_dinv}, partition={partition}, examples={examples}"
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
                f"t={params.step}, sample_word={sample_word}, multiset={multiset}, "
                f"dinv={target_dinv}, partition={partition}, factorization_count={actual}, "
                f"tableau_prediction={predicted}, examples={examples}"
            )
        partition_classes_checked += 1
        compositions_checked += len(compositions)

    return class_word_count, sum(shape_counts.values()), partition_classes_checked, compositions_checked


def run_one_trial(
    *,
    iteration: int,
    seed: int,
    params: RandomCheckInput,
    pair_dinv: tuple[tuple[int, ...], ...],
    partitions: list[PartitionMaskData],
    ssyt_cache: dict[tuple[Shape, Partition], int],
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]],
) -> TrialSummary:
    rng = random.Random(seed)
    sample_start = time.perf_counter()
    sample_word = random_word(length=params.length, alphabet_size=params.alphabet_size, rng=rng)
    counts = counts_from_word(sample_word, alphabet_size=params.alphabet_size)
    target_dinv = word_dinv(sample_word, pair_dinv)
    class_words, tableaux, partition_classes, compositions = verify_sampled_class(
        sample_word=sample_word,
        counts=counts,
        target_dinv=target_dinv,
        params=params,
        pair_dinv=pair_dinv,
        partitions=partitions,
        ssyt_cache=ssyt_cache,
        prediction_cache=prediction_cache,
    )
    return TrialSummary(
        iteration=iteration,
        sample_word=sample_word,
        target_dinv=target_dinv,
        class_words=class_words,
        tableaux=tableaux,
        partition_classes=partition_classes,
        compositions=compositions,
        elapsed_seconds=time.perf_counter() - sample_start,
    )


def run_trial_batch(args: tuple[RandomCheckInput, list[tuple[int, int]]]) -> list[TrialSummary]:
    params, trials = args
    pair_dinv = pair_dinv_table(CheckInput(params.step, params.alphabet_size, params.length))
    partitions = composition_groups(params.length)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    return [
        run_one_trial(
            iteration=iteration,
            seed=seed,
            params=params,
            pair_dinv=pair_dinv,
            partitions=partitions,
            ssyt_cache=ssyt_cache,
            prediction_cache=prediction_cache,
        )
        for iteration, seed in trials
    ]


def print_trial_summary(summary: TrialSummary) -> None:
    print(
        f"  iteration={summary.iteration}: word={summary.sample_word}, dinv={summary.target_dinv}, "
        f"class words={summary.class_words}, tableaux={summary.tableaux}, "
        f"elapsed={summary.elapsed_seconds:.3f}s",
        flush=True,
    )


def run_random_checks(params: RandomCheckInput) -> RandomCheckResult:
    require(params.step >= 0, "t must be non-negative")
    require(params.alphabet_size > 0, "alphabet size A must be positive")
    require(params.length > 0, "length L must be positive")
    require(params.iterations >= 0, "iterations must be non-negative")
    require(params.timeout_seconds is None or params.timeout_seconds > 0, "timeout must be positive")
    require(params.iterations > 0 or params.timeout_seconds is not None, "use iterations, timeout, or both")
    require(params.workers > 0, "workers must be positive")

    result = RandomCheckResult(params=params)
    seed_rng = random.Random(params.seed)
    pair_dinv = pair_dinv_table(CheckInput(params.step, params.alphabet_size, params.length))
    partitions = composition_groups(params.length)
    ssyt_cache: dict[tuple[Shape, Partition], int] = {}
    prediction_cache: dict[tuple[tuple[Shape, int], ...], list[int]] = {}
    start = time.perf_counter()

    if params.workers > 1 and params.timeout_seconds is None:
        trials = [
            (iteration, seed_rng.randrange(0, 2**63))
            for iteration in range(1, params.iterations + 1)
        ]
        batches = [[] for _ in range(min(params.workers, len(trials)))]
        for index, trial in enumerate(trials):
            batches[index % len(batches)].append(trial)
        with Pool(processes=len(batches)) as pool:
            batch_results = pool.map(run_trial_batch, [(params, batch) for batch in batches if batch])
        summaries = sorted((summary for batch in batch_results for summary in batch), key=lambda item: item.iteration)
        for summary in summaries:
            print_trial_summary(summary)
            result.iterations_completed += 1
            result.sampled_words += 1
            result.class_words_checked += summary.class_words
            result.dyck_tableaux_checked += summary.tableaux
            result.partition_classes_checked += summary.partition_classes
            result.compositions_checked += summary.compositions
        result.elapsed_seconds = time.perf_counter() - start
        return result

    while result.iterations_completed < params.iterations or params.timeout_seconds is not None:
        if params.iterations and result.iterations_completed >= params.iterations:
            break
        elapsed = time.perf_counter() - start
        if params.timeout_seconds is not None and elapsed >= params.timeout_seconds:
            break

        summary = run_one_trial(
            iteration=result.iterations_completed + 1,
            seed=seed_rng.randrange(0, 2**63),
            params=params,
            pair_dinv=pair_dinv,
            partitions=partitions,
            ssyt_cache=ssyt_cache,
            prediction_cache=prediction_cache,
        )
        result.iterations_completed += 1
        result.sampled_words += 1
        result.class_words_checked += summary.class_words
        result.dyck_tableaux_checked += summary.tableaux
        result.partition_classes_checked += summary.partition_classes
        result.compositions_checked += summary.compositions
        print_trial_summary(summary)

    result.elapsed_seconds = time.perf_counter() - start
    return result


def print_result(result: RandomCheckResult) -> None:
    params = result.params
    print(f"completed random checks: t={params.step}, alphabet={{1,...,{params.alphabet_size}}}, length={params.length}")
    print(f"  iterations completed: {result.iterations_completed}")
    print(f"  sampled words: {result.sampled_words}")
    print(f"  class words checked: {result.class_words_checked}")
    print(f"  Dyck tableaux checked: {result.dyck_tableaux_checked}")
    print(f"  partition classes checked: {result.partition_classes_checked}")
    print(f"  positive compositions checked: {result.compositions_checked}")
    print(f"  elapsed: {result.elapsed_seconds:.3f}s")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, required=True, help="Rational step t.")
    parser.add_argument("--alphabet-size", "-A", type=int, required=True, help="Alphabet size A.")
    parser.add_argument("--length", "-L", type=int, required=True, help="Sampled word length.")
    parser.add_argument("--iterations", type=int, default=100, help="Maximum sampled classes to check.")
    parser.add_argument("--timeout-seconds", type=float, default=None, help="Optional wall-clock timeout.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed.")
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Parallel worker processes for fixed-iteration runs.",
    )
    args = parser.parse_args()

    result = run_random_checks(
        RandomCheckInput(
            step=args.t,
            alphabet_size=args.alphabet_size,
            length=args.length,
            iterations=args.iterations,
            timeout_seconds=args.timeout_seconds,
            seed=args.seed,
            workers=args.workers,
        )
    )
    print_result(result)
    print("all sampled finite checks passed")


if __name__ == "__main__":
    main()
