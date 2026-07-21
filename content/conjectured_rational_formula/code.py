"""Finite checks for a conjectural rational q,t-Catalan formula.

The mathematical parameters are coprime positive integers ``r`` and ``s``.
Paths run from ``(0,0)`` to ``(s,r)`` and remain below the diagonal of slope
``r/s``.  The implementation uses position coordinates and exact integer
arithmetic.  It depends only on the Python standard library.

For every path Q, the checker computes ``area(Q)`` and ``dinv(Q)``.  It then
compares the direct rational q,t-Catalan coefficient dictionary with the
signed-string dictionary indexed by the distinguished paths for which the
column of label 1 has position-coordinate value 0.

Examples
--------
Reproduce the source paper's main sample (written there in width/height order
as (7,12), hence (r,s)=(12,7) here):

    python code.py

Check several cases:

    python code.py --case 5/3 --case 8/5 --case 12/7

Check every ordered coprime pair with 2 <= r,s <= 15:

    python code.py --grid 2 15 --workers 2

No third-party packages are required.
"""

from __future__ import annotations

import argparse
import os
import time
from collections import defaultdict
from dataclasses import dataclass
from math import comb, gcd
from multiprocessing import Pool, freeze_support
from typing import Iterable


Monomial = tuple[int, int]
Mismatch = tuple[Monomial, int, int]


@dataclass(frozen=True, slots=True)
class CheckResult:
    """Summary of one exact finite check."""

    r: int
    s: int
    closest_column: int
    closest_height: int
    max_total_degree: int
    path_count: int
    expected_path_count: int
    distinguished_paths: int
    positive_terms: int
    negative_terms: int
    negative_paths: int
    ok: bool
    first_difference: Mismatch | None
    elapsed_seconds: float


def ceiling_heights(r: int, s: int) -> tuple[int, ...]:
    """Return H_i=floor(r*i/s), for 0 <= i < s."""

    return tuple(r * i // s for i in range(s))


def column_labels(r: int, s: int) -> tuple[int, ...]:
    """Return the residues L_i = r*i mod s."""

    return tuple((r * i) % s for i in range(s))


def rational_catalan_number(r: int, s: int) -> int:
    """Return the number of (r,s)-Dyck paths when gcd(r,s)=1."""

    return comb(r + s, r) // (r + s)


def _clean_coefficients(values: dict[Monomial, int]) -> dict[Monomial, int]:
    return {monomial: coefficient for monomial, coefficient in values.items() if coefficient}


def check_case(r: int, s: int) -> CheckResult:
    """Check the conjectural signed-string formula for one coprime pair.

    Position coordinates are Q=(Q_0,...,Q_{s-1}).  Put

        H_i = floor(r*i/s),  P_i = H_i-Q_i.

    A valid path has Q_0=0, 0<=Q_i<=H_i, and weakly increasing P_i.  During
    recursive generation we choose the P_i, which makes validity automatic.

    The deficit statistic is accumulated one newly completed pair at a time.
    The integer pair formula used below is equivalent to the affine-height
    threshold-count definition in the mathematical explanation.
    """

    if r < 2 or s < 2:
        raise ValueError("expected r>=2 and s>=2")
    if gcd(r, s) != 1:
        raise ValueError(f"expected a coprime pair, got r={r}, s={s}")

    start = time.perf_counter()
    heights = ceiling_heights(r, s)
    labels = column_labels(r, s)
    increments = tuple(heights[i + 1] - heights[i] for i in range(s - 1))
    total_degree = sum(heights)
    closest_column = labels.index(1)
    closest_height = heights[closest_column]

    # Current position coordinates.  Q_0 is always 0.
    path = [0] * s

    direct: dict[Monomial, int] = defaultdict(int)
    predicted: dict[Monomial, int] = defaultdict(int)

    path_count = 0
    distinguished_paths = 0
    positive_terms = 0
    negative_terms = 0
    negative_paths = 0

    def pair_deficit(i: int, j: int) -> int:
        """Return the deficit contribution of the completed pair (i,j)."""

        left = path[i]
        right = path[j]
        distance = abs(left - right)

        # Correct the integer distance when the Q-order and label-order point
        # in opposite directions.  This is floor(|q_i-q_j|) for the affine
        # heights q_i=Q_i+L_i/s.
        if left != right and ((left > right) != (labels[i] > labels[j])):
            distance -= 1
            if distance < 0:
                distance = 0

        if left > right:
            local_room = increments[i] - (path[i + 1] - left)
        elif right > left:
            local_room = increments[i - 1] - (left - path[i - 1])
        else:
            return 0

        # local_room is nonnegative on valid paths.
        return min(distance, local_room)

    def visit(
        column: int,
        previous_path_height: int,
        area: int,
        deficit: int,
    ) -> None:
        nonlocal path_count
        nonlocal distinguished_paths
        nonlocal positive_terms
        nonlocal negative_terms
        nonlocal negative_paths

        if column == s:
            path_count += 1
            dinv = total_degree - area - deficit
            direct[(area, dinv)] += 1

            # L_i=1 singles out the lattice point closest to the diagonal.
            # Q_i=0 means the path passes through that point.
            if path[closest_column] != 0:
                return

            distinguished_paths += 1
            total = area + dinv
            if area <= dinv:
                for q_degree in range(area, dinv + 1):
                    predicted[(q_degree, total - q_degree)] += 1
                    positive_terms += 1
            else:
                # The open interval is empty when area=dinv+1.
                contributed = False
                for q_degree in range(dinv + 1, area):
                    predicted[(q_degree, total - q_degree)] -= 1
                    negative_terms += 1
                    contributed = True
                if contributed:
                    negative_paths += 1
            return

        ceiling = heights[column]
        for path_height in range(previous_path_height, ceiling + 1):
            coordinate = ceiling - path_height
            path[column] = coordinate

            new_deficit = deficit
            # Appending column j completes precisely the pairs (i,j) with
            # 1 <= i < j.  Shared prefixes therefore reuse earlier work.
            for left_column in range(1, column):
                new_deficit += pair_deficit(left_column, column)

            visit(
                column + 1,
                path_height,
                area + coordinate,
                new_deficit,
            )

    visit(column=1, previous_path_height=0, area=0, deficit=0)

    expected_path_count = rational_catalan_number(r, s)
    if path_count != expected_path_count:
        raise RuntimeError(
            "path enumeration failed its Catalan-number check: "
            f"generated={path_count}, expected={expected_path_count}"
        )

    direct_clean = _clean_coefficients(direct)
    predicted_clean = _clean_coefficients(predicted)
    first_difference: Mismatch | None = None
    for monomial in sorted(
        set(direct_clean) | set(predicted_clean),
        key=lambda item: (item[0] + item[1], item[0], item[1]),
    ):
        actual = direct_clean.get(monomial, 0)
        conjectured = predicted_clean.get(monomial, 0)
        if actual != conjectured:
            first_difference = (monomial, actual, conjectured)
            break

    return CheckResult(
        r=r,
        s=s,
        closest_column=closest_column,
        closest_height=closest_height,
        max_total_degree=total_degree,
        path_count=path_count,
        expected_path_count=expected_path_count,
        distinguished_paths=distinguished_paths,
        positive_terms=positive_terms,
        negative_terms=negative_terms,
        negative_paths=negative_paths,
        ok=first_difference is None,
        first_difference=first_difference,
        elapsed_seconds=time.perf_counter() - start,
    )


def _check_pair(pair: tuple[int, int]) -> CheckResult:
    return check_case(*pair)


def parse_case(text: str) -> tuple[int, int]:
    try:
        left, right = text.replace(",", "/").split("/", 1)
        return int(left), int(right)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("expected a case in the form r/s") from exc


def ordered_coprime_grid(lower: int, upper: int) -> list[tuple[int, int]]:
    if lower < 2 or upper < lower:
        raise ValueError("expected 2 <= grid lower bound <= grid upper bound")
    return [
        (r, s)
        for r in range(lower, upper + 1)
        for s in range(lower, upper + 1)
        if gcd(r, s) == 1
    ]


def run_cases(cases: Iterable[tuple[int, int]], workers: int) -> list[CheckResult]:
    unique_cases = sorted(set(cases))
    if workers <= 1 or len(unique_cases) <= 1:
        return [check_case(r, s) for r, s in unique_cases]

    # chunksize=1 matters here: it prevents the two largest neighboring grid
    # cases from being assigned to the same process.
    with Pool(processes=workers) as pool:
        results = list(pool.imap_unordered(_check_pair, unique_cases, chunksize=1))
    return sorted(results, key=lambda result: (result.r, result.s))


def print_case(result: CheckResult, show_difference: bool) -> None:
    print(f"case r={result.r} s={result.s}")
    print(
        "  closest_label_1_point: "
        f"({result.closest_column}, {result.closest_height})"
    )
    print(f"  max_total_degree: {result.max_total_degree}")
    print(f"  generated_paths: {result.path_count}")
    print(f"  distinguished_paths: {result.distinguished_paths}")
    print(f"  positive_string_terms: {result.positive_terms}")
    print(f"  negative_string_terms: {result.negative_terms}")
    print(f"  negative_distinguished_paths: {result.negative_paths}")
    print(f"  elapsed_seconds: {result.elapsed_seconds:.3f}")
    print(f"  status: {'PASS' if result.ok else 'FAIL'}")
    if show_difference and result.first_difference is not None:
        monomial, actual, conjectured = result.first_difference
        print(
            "  first_difference: "
            f"q^{monomial[0]} t^{monomial[1]} "
            f"direct={actual} conjectured={conjectured}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        type=parse_case,
        dest="cases",
        help=(
            "coprime case r/s in standard slope notation; may be repeated; "
            "the default is 12/7"
        ),
    )
    parser.add_argument(
        "--grid",
        nargs=2,
        type=int,
        metavar=("MIN", "MAX"),
        help="check every ordered coprime pair with MIN <= r,s <= MAX",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="worker processes; 0 selects at most two automatically",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="print every case when checking a grid",
    )
    parser.add_argument(
        "--show-difference",
        action="store_true",
        help="show the first coefficient mismatch for a failed case",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cases: list[tuple[int, int]] = list(args.cases or [])
    grid_requested = args.grid is not None
    if args.grid is not None:
        cases.extend(ordered_coprime_grid(args.grid[0], args.grid[1]))
    if not cases:
        # The source paper writes this example in width/height order as
        # (7,12).  Standard slope notation is therefore (r,s)=(12,7).
        cases = [(12, 7)]

    workers = args.workers
    if workers < 0:
        raise SystemExit("workers must be nonnegative")
    if workers == 0:
        workers = min(2, os.cpu_count() or 1)

    wall_start = time.perf_counter()
    results = run_cases(cases, workers=workers)
    wall_elapsed = time.perf_counter() - wall_start

    print("rational q,t-Catalan conjecture finite check")
    if not grid_requested or args.verbose:
        for index, result in enumerate(results):
            if index:
                print()
            print_case(result, show_difference=args.show_difference)

    all_ok = all(result.ok for result in results)
    total_paths = sum(result.path_count for result in results)
    negative_cases = sum(result.negative_terms > 0 for result in results)
    total_negative_terms = sum(result.negative_terms for result in results)

    if grid_requested:
        print(f"grid_cases: {len(results)}")
        print(f"grid_generated_paths: {total_paths}")
        print(f"grid_cases_with_negative_terms: {negative_cases}")
        print(f"grid_negative_terms: {total_negative_terms}")
        largest = sorted(results, key=lambda result: result.path_count, reverse=True)[:2]
        print(
            "grid_largest_cases: "
            + ", ".join(
                f"({result.r},{result.s}) paths={result.path_count}" for result in largest
            )
        )
    print(f"wall_elapsed_seconds: {wall_elapsed:.3f}")
    print(f"overall_status: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    freeze_support()
    raise SystemExit(main())
