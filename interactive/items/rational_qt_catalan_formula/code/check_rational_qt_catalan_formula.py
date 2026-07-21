"""Finite checks for the rational q,t-Catalan formula.

This is a curated port of
``Conjectures-and-Computations/qt-catalan/qt-conjecture.py``.  It keeps the
source script's step-coordinate convention and the same monomial comparison,
but exposes a reproducible command-line interface.
"""

from __future__ import annotations

import argparse
import math
from collections import Counter
from dataclasses import dataclass
from math import gcd
from typing import Sequence


StepPath = tuple[int, ...]
Monomial = tuple[int, int]


@dataclass(frozen=True)
class PathRecord:
    degree: int
    path: StepPath


@dataclass(frozen=True)
class CheckResult:
    r: int
    n: int
    ell: int
    closest_index: int
    closest_height: int
    max_area: int
    path_count: int
    all_count: int
    plus_count: int
    minus_count: int
    ok: bool
    first_difference: Monomial | None


def beta(n: int, ell: int, i: int, j: int, path: Sequence[int]) -> float:
    return sum(path[i : j + 1]) - n * (j - i + 1) / (ell + 1)


def gamma(n: int, ell: int, i: int, j: int, path: Sequence[int]) -> int:
    value = beta(n, ell, i, j, path)
    if value < 0:
        return min(path[i - 1], math.floor(-value))
    if value > 0:
        return min(path[i], math.floor(value))
    return 0


def generate_paths(ell: int, n: int) -> list[PathRecord]:
    """Generate the source script's step-coordinate Dyck paths."""

    frontier = [PathRecord(0, ())]
    while len(frontier[0].path) < ell:
        next_frontier: list[PathRecord] = []
        for record in frontier:
            prefix = record.path
            room = math.floor((len(prefix) + 1) * n / (ell + 1) - sum(prefix))
            for value in range(int(room) + 1):
                child_path = prefix + (value,)
                degree = record.degree
                for k in range(1, len(child_path)):
                    degree += gamma(n, ell, k, len(child_path) - 1, child_path)
                next_frontier.append(PathRecord(degree, child_path))
        frontier = next_frontier
    return frontier


def max_area(ell: int, n: int) -> int:
    return sum(int(math.floor((i + 1) * n / (ell + 1))) for i in range(ell))


def closest_point(r: int, n: int) -> tuple[int, int]:
    """Return the source script's closest point [q, floor((q+1)n/r)]."""

    ell = r - 1
    closest: tuple[int, int] | None = None
    for q in range(ell):
        fractional_scaled = round((ell + 1) * ((q + 1) * n / (ell + 1) - math.floor((q + 1) * n / (ell + 1))))
        if fractional_scaled == 1:
            closest = (q, math.floor((q + 1) * n / (ell + 1)))
    if closest is None:
        raise ValueError(f"no closest point found for r={r}, n={n}; expected gcd(r,n)=1")
    return closest


def path_area(record: PathRecord, ell: int, n: int) -> int:
    area = max_area(ell, n)
    for p in range(len(record.path)):
        area -= sum(record.path[: p + 1])
    return area


def monomial_counts(r: int, n: int) -> tuple[Counter[Monomial], Counter[Monomial], Counter[Monomial], list[PathRecord], int, tuple[int, int]]:
    ell = r - 1
    paths = generate_paths(ell, n)
    total_area = max_area(ell, n)
    closest = closest_point(r, n)
    all_terms: Counter[Monomial] = Counter()
    plus_terms: Counter[Monomial] = Counter()
    minus_terms: Counter[Monomial] = Counter()

    for record in paths:
        area = path_area(record, ell, n)
        all_terms[(area, total_area - record.degree)] += 1
        if sum(record.path[: closest[0] + 1]) != closest[1]:
            continue
        if area <= total_area - area - record.degree:
            for q_degree in range(area, int(total_area - area - record.degree + 1)):
                plus_terms[(q_degree, total_area - record.degree)] += 1
        else:
            for q_degree in range(int(total_area - area - record.degree + 1), area):
                minus_terms[(q_degree, total_area - record.degree)] += 1

    return all_terms, plus_terms, minus_terms, paths, total_area, closest


def check_conjecture(r: int, n: int) -> CheckResult:
    if r <= 1 or n <= 0:
        raise ValueError("expected r>1 and n>0")
    if gcd(r, n) != 1:
        raise ValueError("the source conjecture check is intended for gcd(r,n)=1")

    all_terms, plus_terms, minus_terms, paths, total_area, closest = monomial_counts(r, n)
    right_side = all_terms + minus_terms
    ok = plus_terms == right_side
    first_difference = None
    if not ok:
        for key in sorted(set(plus_terms) | set(right_side), key=lambda item: item[1] + item[0] / 1000):
            if plus_terms[key] != right_side[key]:
                first_difference = key
                break
    return CheckResult(
        r=r,
        n=n,
        ell=r - 1,
        closest_index=closest[0],
        closest_height=closest[1],
        max_area=total_area,
        path_count=len(paths),
        all_count=sum(all_terms.values()),
        plus_count=sum(plus_terms.values()),
        minus_count=sum(minus_terms.values()),
        ok=ok,
        first_difference=first_difference,
    )


def parse_case(text: str) -> tuple[int, int]:
    if "/" in text:
        left, right = text.split("/", 1)
    elif "," in text:
        left, right = text.split(",", 1)
    else:
        raise argparse.ArgumentTypeError("expected a case in the form r/n")
    return int(left), int(right)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        type=parse_case,
        dest="cases",
        help="case r/n to check; may be supplied multiple times; default is 7/12",
    )
    parser.add_argument("--show-difference", action="store_true", help="print the first mismatched monomial if a case fails")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cases = args.cases or [(7, 12)]
    all_ok = True
    print("rational q,t-Catalan formula finite check")
    for r, n in cases:
        result = check_conjecture(r, n)
        all_ok = all_ok and result.ok
        print(f"  case: r={r} n={n}")
        print(f"    ell: {result.ell}")
        print(f"    closest_point: ({result.closest_index}, {result.closest_height})")
        print(f"    max_area: {result.max_area}")
        print(f"    generated_paths: {result.path_count}")
        print(f"    all_terms: {result.all_count}")
        print(f"    plus_terms: {result.plus_count}")
        print(f"    minus_terms: {result.minus_count}")
        print(f"    status: {'PASS' if result.ok else 'FAIL'}")
        if args.show_difference and result.first_difference is not None:
            print(f"    first_difference: {result.first_difference}")
    print(f"overall_status: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
