"""Check the lower-cutoff root/partition correspondence for r=tau*s+1.

At the lower cutoff B=(s-2)*tau-1, the special skeleton roots should be in
statistic-preserving bijection with partitions whose parts are at most s-2.
The checker verifies the required fiber counts:

    root deficit = partition size,
    root area    = partition length.

Equivalently, after conjugating partitions, this can be phrased as a statement
about partitions of length at most s-2, but then root area is the largest part
of the conjugate partition, not its length.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter
from typing import Iterable

import check_r1mod_skeleton_strings as skeletons


Case = tuple[int, int]
Word = tuple[int, ...]


OFFICIAL_RANGES = {
    2: 14,
    3: 12,
    4: 10,
    5: 9,
}


def lower_cutoff(s: int, tau: int) -> int:
    return (s - 2) * tau - 1


def generate_partitions_with_bounded_parts(max_size: int, max_part: int) -> Iterable[tuple[int, ...]]:
    """Yield all partitions with size <= max_size and every part <= max_part."""

    current: list[int] = []

    def rec(remaining: int, largest_allowed: int) -> Iterable[tuple[int, ...]]:
        yield tuple(current)
        for part in range(min(remaining, largest_allowed, max_part), 0, -1):
            current.append(part)
            yield from rec(remaining - part, part)
            current.pop()

    yield from rec(max_size, max_part)


def partition_counts(s: int, max_defect: int) -> Counter[Case]:
    max_part = s - 2
    counts: Counter[Case] = Counter()
    for partition in generate_partitions_with_bounded_parts(max_defect, max_part):
        counts[(sum(partition), len(partition))] += 1
    return counts


def root_counts(s: int, tau: int, max_defect: int) -> Counter[Case]:
    records, _direct, _searched = skeletons.load_records(s, tau, max_defect)
    counts: Counter[Case] = Counter()
    for word, (word_area, _word_dinv, word_defect) in records.items():
        if word_defect > max_defect:
            continue
        if not skeletons.is_full_skeleton_normalized(word, tau):
            continue
        if not skeletons.is_special_skeleton_normalized(word, tau):
            continue
        counts[(word_defect, word_area)] += 1
    return counts


def first_difference(left: Counter[Case], right: Counter[Case]) -> tuple[Case, int, int] | None:
    for key in sorted(set(left) | set(right)):
        if left[key] != right[key]:
            return key, left[key], right[key]
    return None


def run_case(s: int, tau: int) -> bool:
    max_defect = lower_cutoff(s, tau)
    if max_defect < 0:
        print(f"tau={tau} s={s} max_defect={max_defect} status=EMPTY")
        return True

    start = time.perf_counter()
    roots = root_counts(s, tau, max_defect)
    partitions = partition_counts(s, max_defect)
    diff = first_difference(roots, partitions)
    elapsed = time.perf_counter() - start
    root_total = sum(roots.values())
    partition_total = sum(partitions.values())

    status = "PASS" if diff is None else "FAIL"
    print(
        f"tau={tau} s={s} max_defect={max_defect} "
        f"roots={root_total} partitions={partition_total} "
        f"status={status} elapsed_seconds={elapsed:.3f}",
        flush=True,
    )
    if diff is not None:
        key, root_count, partition_count = diff
        print(
            "  first_difference: "
            f"(defect_or_size={key[0]}, area_or_length={key[1]}) "
            f"roots={root_count} partitions={partition_count}",
            flush=True,
        )
    return diff is None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s", type=int, help="single length s to check")
    parser.add_argument("--tau", type=int, help="single tau to check")
    parser.add_argument("--official-grid", action="store_true", help="check the official finite grid")
    parser.add_argument("--max-s", type=int, help="optional upper bound on s for grid runs")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.official_grid:
        ok = True
        for tau, max_s in OFFICIAL_RANGES.items():
            if args.max_s is not None:
                max_s = min(max_s, args.max_s)
            for s in range(3, max_s + 1):
                ok = run_case(s, tau) and ok
        print(f"status: {'PASS' if ok else 'FAIL'}")
        return 0 if ok else 1

    if args.s is None or args.tau is None:
        raise SystemExit("provide --s and --tau, or use --official-grid")
    ok = run_case(args.s, args.tau)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
