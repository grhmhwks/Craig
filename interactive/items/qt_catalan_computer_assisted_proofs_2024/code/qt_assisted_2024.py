"""Computer-assisted checks for Lemma 2 and Lemma 3 of Section 9.

This is a curated port of
``Conjectures-and-Computations/qt-catalan/qt-assisted.py``.  It keeps the
source computation's position-coordinate conventions and finite cutoff
``dstar = 20`` while wrapping the script in a reproducible command-line entry
point.
"""

from __future__ import annotations

import argparse
import math
import time
from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Sequence


Path = tuple[int, ...]
Monomial = tuple[int, int]


@dataclass(frozen=True)
class DyckPathRecord:
    m: int
    degree: int
    path: Path


@dataclass(frozen=True)
class Lemma3LayerResult:
    m: int
    ell: int
    path_count: int
    plus_count: int
    minus_count: int
    all_count: int
    ok: bool


def alpha(a: int, b: int, m: int) -> int:
    if a <= b:
        return min(b - a, m)
    return min(a - b - 1, m)


def alpha0(a: int, m: int) -> int:
    return max(0, a - m)


def point(path: Sequence[int], m: int) -> int:
    pt = 0
    for i in range(len(path) - 1, -1, -1):
        if path[i] - path[-1] > -m:
            pt = i
    return pt


def pair(path: Sequence[int], m: int) -> int:
    pr = len(path) - 2
    for i in range(len(path) - 3, -1, -1):
        if path[i] - path[i + 2] >= -m:
            pr = i
    return pr


def right(path: Sequence[int], m: int) -> Path:
    values = tuple(path)
    pt = point(values, m)
    pr = pair(values, m)
    if pt <= pr + 1 and pt < len(values) - 1:
        return values[: pt + 1] + (values[-1] + 1,) + values[pt + 1 : -1]
    return values


def left(path: Sequence[int], m: int) -> Path:
    values = tuple(path)
    pr = pair(values, m)
    if values[-1] - values[pr + 1] >= -m - 1:
        return values[: pr + 1] + values[pr + 2 :] + (values[pr + 1] - 1,)
    return values


def lowest(path: Sequence[int], m: int) -> Path:
    current = tuple(path)
    previous: Path | None = None
    while current != previous:
        previous = current
        current = right(current, m)
    return current


def height(path: Sequence[int]) -> int:
    greatest = 0
    j = 0
    for i, value in enumerate(path):
        if value >= greatest:
            greatest = value
            j = i
    return (greatest - 1) * (len(path) - 1) + j - sum(path)


def lstar(dstar: int, m: int) -> int:
    return int(math.ceil(dstar / m + 1.001))


def extend_degree(prefix: Sequence[int], value: int, m: int, current_degree: int) -> int:
    degree = current_degree
    for k in range(1, len(prefix)):
        degree += alpha(prefix[k], value, m)
    degree -= alpha0(value, m)
    return degree


def generate_records(*, max_m: int = 20, dstar: int = 20, verbose: bool = False) -> list[DyckPathRecord]:
    """Generate all records used by the source computation.

    The source script uses records ``[m, d, [a_0,...,a_l]]``.  This port stores
    them as ``DyckPathRecord`` values with tuple paths.
    """

    records: list[DyckPathRecord] = []
    for m in range(max_m, 0, -1):
        if verbose:
            print(f"generating Dyck paths with m={m}", flush=True)
        max_length = lstar(dstar, m) + 1
        all_for_m = [DyckPathRecord(m, 0, (0,))]
        frontier = [DyckPathRecord(m, 0, (0,))]
        while len(frontier[0].path) < max_length:
            next_frontier: list[DyckPathRecord] = []
            for record in frontier:
                prefix = record.path
                for value in range(prefix[-1] + m + 1):
                    degree = extend_degree(prefix, value, m, record.degree)
                    if degree <= dstar:
                        child = DyckPathRecord(m, degree, prefix + (value,))
                        next_frontier.append(child)
                        all_for_m.append(child)
            frontier = next_frontier
        records.extend(all_for_m)
    return records


def string_okay(record: DyckPathRecord, *, dstar: int = 20) -> bool:
    m = record.m
    path = record.path
    target_length = lstar(dstar, m) + 1
    if len(path) < target_length:
        return True
    if len(path) != target_length:
        return True
    if path[1] > 0:
        return True
    m_total = m * len(path) * (len(path) - 1) // 2
    bound = m_total - height(path) - record.degree
    return sum(lowest(path, m)) <= bound


def check_lemma2(records: Sequence[DyckPathRecord], *, dstar: int = 20) -> tuple[bool, list[DyckPathRecord]]:
    failures = [record for record in records if not string_okay(record, dstar=dstar)]
    return not failures, failures


def sort_monomials(values: Iterable[Monomial]) -> list[Monomial]:
    return sorted(values, key=lambda item: item[1] + item[0] / 1000)


def grouped_by_m_and_length(records: Sequence[DyckPathRecord]) -> Iterable[list[DyckPathRecord]]:
    start = 0
    ordered = list(records)
    while start < len(ordered):
        end = start
        while (
            end < len(ordered) - 1
            and ordered[end].m == ordered[end + 1].m
            and len(ordered[end].path) == len(ordered[end + 1].path)
        ):
            end += 1
        end += 1
        yield ordered[start:end]
        start = end


def check_lemma3(records: Sequence[DyckPathRecord], *, verbose: bool = False) -> tuple[bool, list[Lemma3LayerResult]]:
    results: list[Lemma3LayerResult] = []
    all_ok = True
    for layer in grouped_by_m_and_length(records):
        ell = len(layer[0].path) - 1
        if ell == 0:
            continue
        m = layer[0].m
        m_total = m * (ell + 1) * ell // 2
        plus: list[Monomial] = []
        minus: list[Monomial] = []
        all_monomials: list[Monomial] = []

        for record in layer:
            path = record.path
            degree = record.degree
            path_area = sum(path)
            all_monomials.append((path_area, m_total - degree))
            if path[1] != 0:
                continue
            if path_area <= m_total - path_area - degree:
                for q_degree in range(path_area, int(m_total - path_area - degree + 1)):
                    plus.append((q_degree, m_total - degree))
            else:
                for q_degree in range(int(m_total - path_area - degree + 1), path_area):
                    minus.append((q_degree, m_total - degree))

        ok = sort_monomials(plus) == sort_monomials(all_monomials + minus)
        all_ok = all_ok and ok
        result = Lemma3LayerResult(
            m=m,
            ell=ell,
            path_count=len(layer),
            plus_count=len(plus),
            minus_count=len(minus),
            all_count=len(all_monomials),
            ok=ok,
        )
        results.append(result)
        if verbose:
            status = "PASS" if ok else "FAIL"
            print(f"lemma3 m={m} ell={ell}: {status}", flush=True)
    return all_ok, results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=20, help="largest m to include; source value is 20")
    parser.add_argument("--dstar", type=int, default=20, help="degree cutoff; source value is 20")
    parser.add_argument("--lemma", choices=("all", "2", "3"), default="all", help="which check to run")
    parser.add_argument("--verbose", action="store_true", help="print per-m and per-layer progress")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    start = time.perf_counter()
    records = generate_records(max_m=args.max_m, dstar=args.dstar, verbose=args.verbose)
    print("qt-Catalan 2024 computer-assisted checks")
    print(f"  max_m: {args.max_m}")
    print(f"  dstar: {args.dstar}")
    print(f"  generated_records: {len(records)}")
    by_m = Counter(record.m for record in records)
    print(f"  records_by_m: {dict(sorted(by_m.items()))}")

    ok = True
    if args.lemma in ("all", "2"):
        lemma2_ok, failures = check_lemma2(records, dstar=args.dstar)
        print(f"  lemma2_status: {'PASS' if lemma2_ok else 'FAIL'}")
        print(f"  lemma2_failures: {len(failures)}")
        for failure in failures[:5]:
            print(f"  lemma2_failure: m={failure.m} degree={failure.degree} path={failure.path}")
        ok = ok and lemma2_ok

    if args.lemma in ("all", "3"):
        lemma3_ok, layer_results = check_lemma3(records, verbose=args.verbose)
        print(f"  lemma3_status: {'PASS' if lemma3_ok else 'FAIL'}")
        print(f"  lemma3_layers_checked: {len(layer_results)}")
        failures = [result for result in layer_results if not result.ok]
        print(f"  lemma3_failures: {len(failures)}")
        if layer_results:
            print(
                "  lemma3_last_layer: "
                f"m={layer_results[-1].m} ell={layer_results[-1].ell} "
                f"path_count={layer_results[-1].path_count}"
            )
        for failure in failures[:5]:
            print(f"  lemma3_failure: m={failure.m} ell={failure.ell}")
        ok = ok and lemma3_ok

    print(f"  elapsed_seconds: {time.perf_counter() - start:.3f}")
    print(f"  status: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
