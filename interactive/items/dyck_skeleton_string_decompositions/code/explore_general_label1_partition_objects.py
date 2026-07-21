"""Explore partition-like models for low-defect label-1-zero rational paths.

For a coprime slope r/s, this script restricts to paths with value 0 in the
label-1 position and to the intrinsic low-defect range where all such paths lie
weakly below the middle area.  It compares the bivariate fibers

    (defect, area)

with ordinary partitions whose largest part is at most s-2.  In the special
family r=tau*s+1 this ordinary partition model matches the lower-root fibers.
For general slopes the first mismatch points to the extra restriction needed
for a more refined partition-like object.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import gcd

import check_nrcm_lower_half as nrcm


Fiber = tuple[int, int]
Path = tuple[int, ...]


def intrinsic_label1_zero_cutoff(paths: list[Path], r: int, s: int) -> int:
    label_index = nrcm.labels(r, s).index(1)
    total = nrcm.total_degree(r, s)
    bad_defects: list[int] = []
    root_defects: list[int] = []
    for path in paths:
        if path[label_index] != 0:
            continue
        defect = nrcm.defect(path, r, s)
        root_defects.append(defect)
        if 2 * nrcm.area(path) > total - defect:
            bad_defects.append(defect)
    if bad_defects:
        return min(bad_defects) - 1
    return max(root_defects, default=-1)


def label1_zero_fibers(paths: list[Path], r: int, s: int, max_defect: int) -> Counter[Fiber]:
    label_index = nrcm.labels(r, s).index(1)
    counts: Counter[Fiber] = Counter()
    for path in paths:
        if path[label_index] != 0:
            continue
        defect = nrcm.defect(path, r, s)
        if defect <= max_defect:
            counts[(defect, nrcm.area(path))] += 1
    return counts


def label1_zero_paths_in_fiber(paths: list[Path], r: int, s: int, fiber: Fiber) -> list[Path]:
    label_index = nrcm.labels(r, s).index(1)
    target_defect, target_area = fiber
    return sorted(
        path
        for path in paths
        if path[label_index] == 0
        and nrcm.defect(path, r, s) == target_defect
        and nrcm.area(path) == target_area
    )


def ordinary_partitions_in_fiber(max_part: int, fiber: Fiber) -> list[tuple[int, ...]]:
    target_size, target_length = fiber
    out: list[tuple[int, ...]] = []
    current: list[int] = []

    def rec(remaining: int, largest_allowed: int, remaining_length: int) -> None:
        if remaining_length == 0:
            if remaining == 0:
                out.append(tuple(current))
            return
        for part in range(min(remaining, largest_allowed, max_part), 0, -1):
            current.append(part)
            rec(remaining - part, part, remaining_length - 1)
            current.pop()

    rec(target_size, max_part, target_length)
    return out


def ordinary_partition_fibers(max_defect: int, max_part: int) -> Counter[Fiber]:
    counts: Counter[Fiber] = Counter()
    current: list[int] = []

    def rec(remaining: int, largest_allowed: int) -> None:
        counts[(sum(current), len(current))] += 1
        for part in range(min(remaining, largest_allowed, max_part), 0, -1):
            current.append(part)
            rec(remaining - part, part)
            current.pop()

    rec(max_defect, max_part)
    return counts


def first_difference(left: Counter[Fiber], right: Counter[Fiber]) -> tuple[Fiber, int, int] | None:
    for key in sorted(set(left) | set(right)):
        if left[key] != right[key]:
            return key, left[key], right[key]
    return None


def run_case(r: int, s: int) -> bool:
    if r <= 0 or s <= 1 or gcd(r, s) != 1:
        raise SystemExit("expected a positive coprime slope r/s with s>1")

    paths = list(nrcm.valid_paths(r, s))
    labels = nrcm.labels(r, s)
    cutoff = intrinsic_label1_zero_cutoff(paths, r, s)
    roots = label1_zero_fibers(paths, r, s, cutoff)
    ordinary = ordinary_partition_fibers(cutoff, s - 2) if cutoff >= 0 else Counter()
    diff = first_difference(roots, ordinary)
    root_total = sum(roots.values())
    ordinary_total = sum(ordinary.values())
    status = "MATCH" if diff is None else "DIFF"

    print(f"general label-1-zero partition-object exploration r={r} s={s}")
    print(f"  H: {nrcm.ceiling_heights(r, s)}")
    print(f"  L: {labels}")
    print(f"  label1_index: {labels.index(1)}")
    print(f"  total_degree: {nrcm.total_degree(r, s)}")
    print(f"  intrinsic_low_defect_cutoff: {cutoff}")
    print(f"  label1_zero_paths_in_range: {root_total}")
    print(f"  ordinary_partitions_largest_part_at_most_{s - 2}: {ordinary_total}")
    print(f"  ordinary_partition_model: {status}")
    if diff is not None:
        fiber, root_count, partition_count = diff
        defect, area = fiber
        print(
            "  first_difference: "
            f"defect/size={defect} area/length={area} "
            f"paths={root_count} ordinary_partitions={partition_count}"
        )
        print(f"  paths_in_first_difference: {label1_zero_paths_in_fiber(paths, r, s, fiber)}")
        print(f"  ordinary_partitions_in_first_difference: {ordinary_partitions_in_fiber(s - 2, fiber)}")
    return diff is None


def parse_case(text: str) -> tuple[int, int]:
    left, right = text.split("/")
    return int(left), int(right)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=parse_case, required=True, help="slope r/s")
    return parser.parse_args()


def main() -> int:
    r, s = parse_args().case
    run_case(r, s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
