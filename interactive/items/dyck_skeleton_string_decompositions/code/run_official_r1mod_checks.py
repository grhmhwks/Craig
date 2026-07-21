"""Run the official finite checks for the ``r=tau*s+1`` string item.

The official ranges are:

* tau=2, 1 <= s <= 14;
* tau=3, 1 <= s <= 12;
* tau=4, 1 <= s <= 10;
* tau=5, 1 <= s <= 9.

For s <= 4 only the quotient formula is checked.  For s >= 5 both the
formula and the lower-half map are checked.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path


OFFICIAL_RANGES = {
    2: 14,
    3: 12,
    4: 10,
    5: 9,
}


def parse_field(output: str, field: str) -> str:
    match = re.search(rf"^\s*{re.escape(field)}:\s*(.+)$", output, re.MULTILINE)
    return match.group(1).strip() if match else ""


def run_case(checker: Path, tau: int, s: int) -> tuple[bool, str]:
    command = [sys.executable, str(checker), "--tau", str(tau), "--s", str(s)]
    if s <= 4:
        command.append("--formula-only")

    start = time.perf_counter()
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    wall = time.perf_counter() - start
    output = completed.stdout + completed.stderr
    status = parse_field(output, "status")
    if "empty defect range" in output and completed.returncode == 0:
        status = "PASS"
    ok = completed.returncode == 0 and status != "FAIL"
    mode = "formula-only" if s <= 4 else "formula+map"
    max_defect = parse_field(output, "max_defect")
    generated = parse_field(output, "generated_words")
    searched = parse_field(output, "searched_leaf_words")
    retained = parse_field(output, "retained_defect_range_words")
    total = parse_field(output, "total_elapsed_seconds")
    if not total:
        total = f"{wall:.3f}"
    summary = (
        f"tau={tau} s={s} mode={mode} status={'PASS' if ok else 'FAIL'} "
        f"max_defect={max_defect or 'empty'} generated={generated or 'n/a'} "
        f"searched={searched or 'n/a'} retained={retained or 'n/a'} "
        f"elapsed={total}s"
    )
    if not ok:
        summary += "\n" + output
    return ok, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stop-on-fail", action="store_true", help="stop after the first failed official case")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checker = Path(__file__).with_name("check_r1mod_skeleton_strings.py")
    all_ok = True
    start = time.perf_counter()
    for tau, max_s in OFFICIAL_RANGES.items():
        for s in range(1, max_s + 1):
            ok, summary = run_case(checker, tau, s)
            print(summary, flush=True)
            all_ok = all_ok and ok
            if not ok and args.stop_on_fail:
                print(f"overall_elapsed_seconds: {time.perf_counter() - start:.3f}")
                return 1
    print(f"overall_elapsed_seconds: {time.perf_counter() - start:.3f}")
    print(f"overall_status: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
