"""Check where strict NRCM is defined on lower-half sources.

This is a narrower diagnostic than ``check_nrcm_lower_half.py``.  It checks
only that strict NRCM is defined for every path of defect d and area
``a < (M-d)/2``.  The Dyck proof shows that, once strict NRCM is defined, it is
valid and preserves defect.

For slopes ``r=tau*s+1`` the script can use the optimized low-defect generator
from ``check_r1mod_skeleton_strings.py``.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import gcd

import check_nrcm_lower_half as nrcm
import check_r1mod_skeleton_strings as r1mod


def path_records_for_slope(r: int, s: int, max_defect: int) -> tuple[dict[nrcm.Path, nrcm.PathData], str]:
    records, _ = nrcm.load_path_data(r, s, max_defect)
    return records, f"ordinary_generator retained_paths={len(records)}"


def path_records_for_r1mod(tau: int, s: int, max_defect: int) -> tuple[dict[nrcm.Path, nrcm.PathData], str]:
    records, _, searched = r1mod.load_records(s, tau, max_defect)
    out = {q: nrcm.PathData(q, stats[0], stats[2]) for q, stats in records.items()}
    return (
        out,
        "r1mod_generator "
        f"generated_words={r1mod.count_normalized_words(s, tau)} "
        f"searched_leaf_words={searched} retained_paths={len(out)}",
    )


def check_domain_layer(records: dict[nrcm.Path, nrcm.PathData], r: int, s: int, defect: int) -> tuple[Counter[str], nrcm.Failure | None]:
    m_value = nrcm.total_degree(r, s)
    sources = sorted(
        (data for data in records.values() if data.defect == defect and 2 * data.area < m_value - defect),
        key=lambda data: (data.area, data.q),
    )
    counts: Counter[str] = Counter()
    counts["sources_below_midline"] = len(sources)
    for data in sources:
        move = nrcm.nrcm(data.q, r, s)
        counts["attempts"] += 1
        if move is None:
            return counts, nrcm.Failure(defect, data.area, data.q, "NRCM undefined")
        counts["defined_moves"] += 1
        counts[f"suffix_{move.k}"] += 1
    return counts, None


def scan_records(records: dict[nrcm.Path, nrcm.PathData], r: int, s: int, max_defect: int) -> tuple[int, list[str]]:
    consecutive_ok = -1
    lines: list[str] = []
    for defect in range(max_defect + 1):
        counts, failure = check_domain_layer(records, r, s, defect)
        if failure is None:
            if consecutive_ok == defect - 1:
                consecutive_ok = defect
            lines.append(f"  defc={defect}: PASS sources={counts['sources_below_midline']} defined={counts['defined_moves']}")
            continue
        lines.append(
            f"  defc={defect}: FAIL sources={counts['sources_below_midline']} "
            f"defined={counts['defined_moves']} reason={failure.reason} area={failure.area} q={failure.q}"
        )
        break
    return consecutive_ok, lines


def parse_case(text: str) -> tuple[int, int]:
    left, right = text.split("/")
    return int(left), int(right)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--case", type=parse_case, help="slope r/s")
    group.add_argument("--r1mod", nargs=2, metavar=("TAU", "S"), type=int, help="use slope r=tau*s+1")
    parser.add_argument("--max-defect", type=int, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.r1mod is not None:
        tau, s = args.r1mod
        if tau <= 0 or s <= 1:
            raise SystemExit("expected tau>0 and s>1")
        r = tau * s + 1
        records, generator_info = path_records_for_r1mod(tau, s, args.max_defect)
        label = f"tau={tau} s={s} slope={r}/{s}"
    else:
        r, s = args.case
        if r <= 0 or s <= 1 or gcd(r, s) != 1:
            raise SystemExit("expected a positive coprime slope r/s with s>1")
        records, generator_info = path_records_for_slope(r, s, args.max_defect)
        label = f"slope={r}/{s}"

    consecutive_ok, lines = scan_records(records, r, s, args.max_defect)
    print(f"NRCM domain check {label} M={nrcm.total_degree(r, s)}")
    print(f"  {generator_info}")
    for line in lines:
        print(line)
    print(f"  initial_passing_defect_range: 0..{consecutive_ok}" if consecutive_ok >= 0 else "  initial_passing_defect_range: empty")
    failed = consecutive_ok < args.max_defect
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
