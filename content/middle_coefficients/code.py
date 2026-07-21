"""Checks for flat middle coefficients in classical and rational q,t-Catalan models.

This file is intended for the simplified repository item

    contents/qt_catalan_middle_coefficients/code.py

It has three independent layers, matching the skeleton-string item.

1. Classical Dyck case.
   For ordinary Dyck area sequences, the 2026 skeleton-string theorem proves
   flat middle coefficients for 0 <= d <= 2n-8.  This code gives a bounded
   regression check: it enumerates Dyck sequences, counts special skeletons,
   verifies area(S) <= defc(S) for every special skeleton in the range, and
   checks that the middle-band coefficients equal the special-skeleton count.

2. The r = tau*s + 1 family.
   The previous skeleton-string item checks the conjectural special-skeleton
   formula in finite ranges.  This file does not re-check that formula.
   Instead, it verifies the extra root-area condition needed for the flat
   middle consequence: every special tau-Dyck skeleton in the checked deficit
   range satisfies area(S) <= defc_tau(S).

3. General rational slopes.
   In the absence of a general skeleton decomposition, this file directly
   enumerates rational Dyck paths in position coordinates and checks that the
   coefficients in each band

       q^j t^(M-d-j),    d <= j <= M-2d,

   are independent of j for the requested finite cases.

All checks are finite computations.  They are evidence/regression tests, not
proofs of the conjectural rational statements.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from math import comb, gcd
from typing import Iterable, Sequence


Word = tuple[int, ...]
CoeffDict = Counter[tuple[int, int]]


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_case_list(text: str) -> list[tuple[int, int]]:
    """Parse a comma-separated list such as '5/3,7/4,11/8'."""

    out: list[tuple[int, int]] = []
    if not text.strip():
        return out
    for raw in text.split(','):
        item = raw.strip()
        if not item:
            continue
        if '/' not in item:
            raise argparse.ArgumentTypeError(f"expected r/s case, got {item!r}")
        left, right = item.split('/', 1)
        out.append((int(left), int(right)))
    return out


# ---------------------------------------------------------------------------
# 1. Classical Dyck case
# ---------------------------------------------------------------------------


def is_dyck_sequence(seq: Sequence[int]) -> bool:
    """Return whether seq is a classical Dyck area sequence."""

    return (
        len(seq) > 0
        and seq[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in seq)
        and all(seq[index + 1] <= seq[index] + 1 for index in range(len(seq) - 1))
    )


def generate_dyck_sequences(n: int) -> list[Word]:
    """Generate all classical Dyck area sequences of length n."""

    if n <= 0:
        raise ValueError("n must be positive")

    out: list[Word] = []

    def rec(prefix: list[int]) -> None:
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for value in range(prefix[-1] + 2):
            prefix.append(value)
            rec(prefix)
            prefix.pop()

    rec([0])
    return out


def classical_area(seq: Sequence[int]) -> int:
    return sum(seq)


def classical_dinv(seq: Sequence[int]) -> int:
    """Classical dinv in the area-sequence convention."""

    values = tuple(seq)
    return sum(
        1
        for left in range(len(values))
        for right in range(left + 1, len(values))
        if values[left] == values[right] or values[left] == values[right] + 1
    )


def classical_defc(seq: Sequence[int]) -> int:
    n = len(seq)
    return comb(n, 2) - classical_area(seq) - classical_dinv(seq)


def classical_deficit_pair_count(seq: Sequence[int]) -> int:
    """Count the explicit deficit-pair types used as a consistency check."""

    values = tuple(seq)
    total = 0
    first_seen: set[int] = set()
    for left, left_value in enumerate(values):
        left_is_first = left_value not in first_seen
        first_seen.add(left_value)
        for right_value in values[left + 1:]:
            type_a = left_value > right_value + 1
            type_b = left_value < right_value and not left_is_first
            if type_a or type_b:
                total += 1
    return total


def classical_find_extractable(seq: Sequence[int], *, include_final: bool = True) -> int | None:
    """Return the leftmost extractable position, if one exists."""

    values = tuple(seq)
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        if sum(1 for prior in values[:index] if prior == value - 1) != 1:
            continue
        if index + 1 < len(values) and values[index + 1] > value:
            continue
        return index
    return None


def is_full_dyck_skeleton(seq: Sequence[int]) -> bool:
    return is_dyck_sequence(seq) and classical_find_extractable(seq, include_final=True) is None


def classical_excluded_skeleton(n: int) -> Word:
    """The exceptional full skeleton epsilon_n, for n >= 4."""

    if n < 4:
        return ()
    return (0, 0, 1) + (0,) * (n - 4) + (1,)


def is_special_dyck_skeleton(seq: Sequence[int]) -> bool:
    values = tuple(seq)
    return is_full_dyck_skeleton(values) and values != classical_excluded_skeleton(len(values))


@dataclass(frozen=True)
class ClassicalSummary:
    n_min: int
    n_max: int
    sequence_count: int
    checked_bands: int
    checked_coefficients: int
    skeleton_area_checks: int
    special_skeleton_counts: dict[int, dict[int, int]]


def check_classical_flat_middle(n_min: int, n_max: int) -> ClassicalSummary:
    """Check the proved classical skeleton range for n_min <= n <= n_max."""

    require(4 <= n_min <= n_max, "require 4 <= n_min <= n_max")

    sequence_count = 0
    checked_bands = 0
    checked_coefficients = 0
    skeleton_area_checks = 0
    special_skeleton_counts: dict[int, dict[int, int]] = {}

    for n in range(n_min, n_max + 1):
        m_total = comb(n, 2)
        coeffs: CoeffDict = Counter()
        skeleton_counts: Counter[int] = Counter()
        sequences = generate_dyck_sequences(n)
        sequence_count += len(sequences)

        for seq in sequences:
            require(is_dyck_sequence(seq), f"generator produced non-Dyck sequence: {seq}")
            area = classical_area(seq)
            dinv = classical_dinv(seq)
            defc = classical_defc(seq)
            require(
                defc == classical_deficit_pair_count(seq),
                f"deficit formula/pair mismatch: n={n}, seq={seq}",
            )
            coeffs[(area, dinv)] += 1

            if is_special_dyck_skeleton(seq):
                require(
                    area <= defc,
                    "classical special skeleton violates area <= deficit: "
                    f"n={n}, seq={seq}, area={area}, defc={defc}",
                )
                skeleton_area_checks += 1
                skeleton_counts[defc] += 1

        special_skeleton_counts[n] = dict(sorted(skeleton_counts.items()))

        for d in range(0, 2 * n - 8 + 1):
            target = skeleton_counts[d]
            band_values: list[int] = []
            for j in range(d, m_total - 2 * d + 1):
                coefficient = coeffs[(j, m_total - d - j)]
                band_values.append(coefficient)
                require(
                    coefficient == target,
                    "classical flat middle coefficient mismatch: "
                    f"n={n}, d={d}, j={j}, coeff={coefficient}, "
                    f"special_skeleton_count={target}",
                )
                checked_coefficients += 1
            require(len(set(band_values)) <= 1, f"classical band is not flat: n={n}, d={d}")
            checked_bands += 1

    return ClassicalSummary(
        n_min=n_min,
        n_max=n_max,
        sequence_count=sequence_count,
        checked_bands=checked_bands,
        checked_coefficients=checked_coefficients,
        skeleton_area_checks=skeleton_area_checks,
        special_skeleton_counts=special_skeleton_counts,
    )


# ---------------------------------------------------------------------------
# 2. r = tau*s + 1 special-skeleton area-bound checks
# ---------------------------------------------------------------------------


def r1mod_total_degree(s: int, tau: int) -> int:
    return tau * comb(s, 2)


def r1mod_conjectural_bound(s: int, tau: int) -> int:
    return (s - 2) * (tau + 1) - 4


def r1mod_pair_dinv(left: int, right: int, tau: int) -> int:
    if left <= right:
        contribution = left + tau - right
    else:
        contribution = right + 1 + tau - left
    return contribution if contribution > 0 else 0


def r1mod_pair_table(max_value: int, tau: int) -> list[list[int]]:
    return [[r1mod_pair_dinv(left, right, tau) for right in range(max_value + 1)] for left in range(max_value + 1)]


def r1mod_dinv_append(prefix: Sequence[int], value: int, pair_table: list[list[int]]) -> int:
    return sum(pair_table[left][value] for left in prefix)


def r1mod_is_normalized(word: Sequence[int], tau: int) -> bool:
    values = tuple(word)
    return (
        len(values) > 0
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and all(values[index + 1] <= values[index] + tau for index in range(len(values) - 1))
    )


def r1mod_area(word: Sequence[int]) -> int:
    return sum(word)


def r1mod_dinv(word: Sequence[int], tau: int) -> int:
    values = tuple(word)
    return sum(
        r1mod_pair_dinv(values[left], values[right], tau)
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )


def r1mod_defc(word: Sequence[int], tau: int) -> int:
    values = tuple(word)
    return r1mod_total_degree(len(values), tau) - r1mod_area(values) - r1mod_dinv(values, tau)


def r1mod_suffix_score_bounder(s: int, tau: int, pair_table: list[list[int]]):
    """Exact upper bound for future area+dinv from a prefix state.

    This is copied in spirit from the skeleton-string item: it lets us enumerate
    only words that can still land in the requested low-deficit range.
    """

    max_value = tau * (s - 1)
    pair_columns = [[pair_table[left][right] for left in range(max_value + 1)] for right in range(max_value + 1)]

    @lru_cache(maxsize=None)
    def bound(remaining: int, previous: int, counts: tuple[int, ...]) -> int:
        if remaining == 0:
            return 0
        best = -1
        for value in range(min(max_value, previous + tau) + 1):
            dinv_delta = sum(count * pair_columns[value][left] for left, count in enumerate(counts) if count)
            next_counts = list(counts)
            next_counts[value] += 1
            best = max(best, value + dinv_delta + bound(remaining - 1, value, tuple(next_counts)))
        return best

    return bound


def r1mod_generate_records(s: int, tau: int, max_deficit: int) -> dict[Word, tuple[int, int, int]]:
    """Generate normalized tau-Dyck words with defc <= max_deficit.

    Return word -> (area, dinv, defc).
    """

    require(s >= 1 and tau >= 1, "require s >= 1 and tau >= 1")
    if max_deficit < 0:
        return {}

    total_degree = r1mod_total_degree(s, tau)
    min_score = total_degree - max_deficit
    max_value = tau * (s - 1)
    pair_table = r1mod_pair_table(max_value, tau)
    suffix_bound = r1mod_suffix_score_bounder(s, tau, pair_table)

    records: dict[Word, tuple[int, int, int]] = {}
    prefix = [0]
    counts = [0] * (max_value + 1)
    counts[0] = 1

    def rec(current_area: int, current_dinv: int) -> None:
        remaining = s - len(prefix)
        if remaining:
            best_possible_score = current_area + current_dinv + suffix_bound(remaining, prefix[-1], tuple(counts))
            if best_possible_score < min_score:
                return
        if len(prefix) == s:
            defc = total_degree - current_area - current_dinv
            if defc <= max_deficit:
                records[tuple(prefix)] = (current_area, current_dinv, defc)
            return
        for value in range(prefix[-1] + tau + 1):
            delta = r1mod_dinv_append(prefix, value, pair_table)
            prefix.append(value)
            counts[value] += 1
            rec(current_area + value, current_dinv + delta)
            counts[value] -= 1
            prefix.pop()

    rec(0, 0)
    return records


def r1mod_find_extractable(word: Sequence[int], tau: int, *, include_final: bool = True) -> int | None:
    values = tuple(word)
    require(r1mod_is_normalized(values, tau), f"not a normalized tau-Dyck word: {values}")
    for index, value in enumerate(values):
        if not include_final and index == len(values) - 1:
            continue
        if value == 0:
            continue
        lower = max(0, value - tau)
        prior_count = sum(1 for prior in values[:index] if lower <= prior <= value - 1)
        if prior_count != 1:
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + tau:
            continue
        return index
    return None


def is_r1mod_full_skeleton(word: Sequence[int], tau: int) -> bool:
    values = tuple(word)
    return r1mod_is_normalized(values, tau) and r1mod_find_extractable(values, tau, include_final=True) is None


def r1mod_excluded_skeleton(s: int, tau: int) -> Word:
    if s < 4:
        return ()
    return (0, 0, 1) + (0,) * (s - 4) + (tau,)


def is_r1mod_special_skeleton(word: Sequence[int], tau: int) -> bool:
    values = tuple(word)
    return is_r1mod_full_skeleton(values, tau) and values != r1mod_excluded_skeleton(len(values), tau)


R1MOD_OFFICIAL_RANGES: dict[int, int] = {
    2: 14,
    3: 12,
    4: 10,
    5: 9,
}

R1MOD_QUICK_CASES: list[tuple[int, int]] = [
    (2, 5),
    (2, 6),
    (2, 7),
    (3, 5),
    (3, 6),
    (4, 5),
]


@dataclass(frozen=True)
class R1ModCaseSummary:
    tau: int
    s: int
    max_deficit: int
    retained_words: int
    special_skeletons_checked: int
    special_skeleton_counts: dict[int, int]


def check_r1mod_skeleton_area_bound(tau: int, s: int, max_deficit: int | None = None) -> R1ModCaseSummary:
    """Check area(S) <= defc(S) for special tau-Dyck skeletons in range."""

    require(tau > 1, "this r=1 mod s check is intended for tau > 1")
    require(s >= 1, "require s >= 1")
    if max_deficit is None:
        max_deficit = r1mod_conjectural_bound(s, tau)

    records = r1mod_generate_records(s, tau, max_deficit)
    skeleton_counts: Counter[int] = Counter()
    checked = 0

    for word, (area, _dinv, defc) in records.items():
        if is_r1mod_special_skeleton(word, tau):
            require(
                area <= defc,
                "r=tau*s+1 special skeleton violates area <= deficit: "
                f"tau={tau}, s={s}, word={word}, area={area}, defc={defc}",
            )
            skeleton_counts[defc] += 1
            checked += 1

    return R1ModCaseSummary(
        tau=tau,
        s=s,
        max_deficit=max_deficit,
        retained_words=len(records),
        special_skeletons_checked=checked,
        special_skeleton_counts=dict(sorted(skeleton_counts.items())),
    )


def r1mod_cases_for_mode(mode: str, explicit_cases: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if explicit_cases:
        return explicit_cases
    if mode == "none":
        return []
    if mode == "quick":
        return R1MOD_QUICK_CASES
    if mode == "official":
        return [(tau, s) for tau, max_s in R1MOD_OFFICIAL_RANGES.items() for s in range(1, max_s + 1)]
    raise ValueError(f"unknown r1mod mode: {mode}")


# ---------------------------------------------------------------------------
# 3. General rational direct flat-middle checks
# ---------------------------------------------------------------------------


def rational_heights(r: int, s: int) -> Word:
    return tuple((r * index) // s for index in range(s))


def rational_labels(r: int, s: int) -> Word:
    return tuple((r * index) % s for index in range(s))


def rational_total_degree(r: int, s: int) -> int:
    return sum(rational_heights(r, s))


def generate_rational_paths(r: int, s: int) -> Iterable[Word]:
    """Generate rational Dyck paths in Q-position coordinates.

    H_i=floor(ri/s), Q_i is the area below the diagonal in column i, and
    P_i=H_i-Q_i must be nondecreasing.
    """

    require(r > 0 and s > 1 and gcd(r, s) == 1, "require coprime positive r,s with s > 1")
    heights = rational_heights(r, s)
    path_heights = [0] * s

    def rec(index: int, min_height: int) -> Iterable[Word]:
        if index == s:
            yield tuple(heights[i] - path_heights[i] for i in range(s))
            return
        for value in range(min_height, heights[index] + 1):
            path_heights[index] = value
            yield from rec(index + 1, value)

    yield from rec(1, 0)


def rational_pair_summand(q_values: Sequence[int], r: int, s: int, i: int, j: int) -> int:
    """Diagnostic deficit summand used by the rational-path checks."""

    q = tuple(q_values)
    labels = rational_labels(r, s)
    heights = rational_heights(r, s)
    qi, qj = q[i], q[j]
    u_value = abs(qi - qj)
    if qi != qj and ((qi > qj) != (labels[i] > labels[j])):
        u_value -= 1
    u_value = max(u_value, 0)

    if qi > qj:
        v_value = (heights[i + 1] - heights[i]) - (q[i + 1] - q[i])
    elif qj > qi:
        v_value = (heights[i] - heights[i - 1]) - (q[i] - q[i - 1])
    else:
        v_value = 0
    return min(u_value, v_value)


def rational_defc(q_values: Sequence[int], r: int, s: int) -> int:
    return sum(rational_pair_summand(q_values, r, s, i, j) for i in range(1, s) for j in range(i + 1, s))


def rational_area(q_values: Sequence[int]) -> int:
    return sum(q_values)


def rational_dinv(q_values: Sequence[int], r: int, s: int) -> int:
    return rational_total_degree(r, s) - rational_area(q_values) - rational_defc(q_values, r, s)


DEFAULT_RATIONAL_CASES: list[tuple[int, int]] = [
    # These are deliberately modest default cases.  They include both
    # r=tau*s+1 examples and non-r=1 mod s rational slopes.
    (5, 3),
    (7, 4),
    (8, 5),
    (10, 7),
    (11, 8),
    (13, 8),
]


@dataclass(frozen=True)
class RationalCaseSummary:
    r: int
    s: int
    total_degree: int
    path_count: int
    max_deficit_checked: int
    checked_bands: int
    checked_coefficients: int
    representative_common_values: dict[int, int]


def check_rational_flat_middle(r: int, s: int, max_deficit: int | None = None) -> RationalCaseSummary:
    """Directly check flat middle bands for one rational slope r/s."""

    require(r > 0 and s > 1 and gcd(r, s) == 1, "require coprime positive r,s with s > 1")
    m_total = rational_total_degree(r, s)
    if max_deficit is None:
        max_deficit = m_total // 3
    require(max_deficit >= 0, "max_deficit must be nonnegative")

    coeffs: CoeffDict = Counter()
    path_count = 0
    for q_values in generate_rational_paths(r, s):
        path_count += 1
        area = rational_area(q_values)
        defc = rational_defc(q_values, r, s)
        dinv = m_total - area - defc
        require(dinv >= 0, f"negative dinv for r/s={r}/{s}, q={q_values}")
        coeffs[(area, dinv)] += 1

    checked_bands = 0
    checked_coefficients = 0
    representative_common_values: dict[int, int] = {}

    for d in range(0, max_deficit + 1):
        if d > m_total - 2 * d:
            break
        values = []
        for j in range(d, m_total - 2 * d + 1):
            coefficient = coeffs[(j, m_total - d - j)]
            values.append(coefficient)
            checked_coefficients += 1
        require(
            len(set(values)) <= 1,
            "rational flat middle coefficient mismatch: "
            f"r/s={r}/{s}, d={d}, values={values}",
        )
        representative_common_values[d] = values[0] if values else 0
        checked_bands += 1

    return RationalCaseSummary(
        r=r,
        s=s,
        total_degree=m_total,
        path_count=path_count,
        max_deficit_checked=max_deficit,
        checked_bands=checked_bands,
        checked_coefficients=checked_coefficients,
        representative_common_values=representative_common_values,
    )


def rational_grid_cases(s_max: int, r_max: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for s in range(2, s_max + 1):
        for r in range(s + 1, r_max + 1):
            if gcd(r, s) == 1:
                out.append((r, s))
    return out


# ---------------------------------------------------------------------------
# Command-line interface
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("--skip-classical", action="store_true", help="skip the classical Dyck check")
    parser.add_argument("--classical-n-min", type=int, default=4)
    parser.add_argument("--classical-n-max", type=int, default=8)

    parser.add_argument(
        "--r1mod-mode",
        choices=("none", "quick", "official"),
        default="quick",
        help="which r=tau*s+1 special-skeleton area-bound cases to run",
    )
    parser.add_argument(
        "--r1mod-case",
        action="append",
        default=[],
        metavar="TAU:S",
        help="explicit r=1 mod s case; may be repeated, e.g. --r1mod-case 2:14",
    )

    parser.add_argument("--skip-rational", action="store_true", help="skip direct general rational checks")
    parser.add_argument(
        "--rational-cases",
        type=parse_case_list,
        default=None,
        help="comma-separated direct rational cases, e.g. '5/3,7/4,13/8'",
    )
    parser.add_argument("--rational-grid", action="store_true", help="use a coprime grid instead of the default rational cases")
    parser.add_argument("--rational-s-max", type=int, default=8, help="largest s for --rational-grid")
    parser.add_argument("--rational-r-max", type=int, default=13, help="largest r for --rational-grid")
    parser.add_argument(
        "--rational-max-deficit",
        type=int,
        default=None,
        help="override the direct rational deficit bound; default is floor(M/3) per case",
    )

    args = parser.parse_args()

    print("Flat middle coefficient checks")
    print("  convention: coefficients are q^area t^dinv")
    print()

    if not args.skip_classical:
        classical = check_classical_flat_middle(args.classical_n_min, args.classical_n_max)
        print("Classical Dyck skeleton range: PASS")
        print(f"  n range: {classical.n_min}..{classical.n_max}")
        print("  theorem range: 0 <= d <= 2n-8")
        print(f"  generated sequences: {classical.sequence_count}")
        print(f"  checked bands: {classical.checked_bands}")
        print(f"  checked coefficients: {classical.checked_coefficients}")
        print(f"  special-skeleton area checks: {classical.skeleton_area_checks}")
        print(f"  special skeleton counts: {classical.special_skeleton_counts}")
        print()

    explicit_r1mod_cases: list[tuple[int, int]] = []
    for item in args.r1mod_case:
        if ':' not in item:
            raise SystemExit(f"expected TAU:S for --r1mod-case, got {item!r}")
        tau_text, s_text = item.split(':', 1)
        explicit_r1mod_cases.append((int(tau_text), int(s_text)))

    r1mod_cases = r1mod_cases_for_mode(args.r1mod_mode, explicit_r1mod_cases)
    if r1mod_cases:
        print("r = tau*s + 1 special-skeleton area bounds")
        print("  note: this does not re-check the skeleton formula from the previous item")
        total_r1mod_skeletons = 0
        for tau, s in r1mod_cases:
            summary = check_r1mod_skeleton_area_bound(tau, s)
            total_r1mod_skeletons += summary.special_skeletons_checked
            print(
                f"  PASS tau={tau}, s={s}, max_deficit={summary.max_deficit}, "
                f"retained_words={summary.retained_words}, "
                f"special_skeletons_checked={summary.special_skeletons_checked}, "
                f"counts={summary.special_skeleton_counts}"
            )
        print(f"  total special-skeleton area checks: {total_r1mod_skeletons}")
        print()

    if not args.skip_rational:
        if args.rational_grid:
            rational_cases = rational_grid_cases(args.rational_s_max, args.rational_r_max)
        elif args.rational_cases is not None:
            rational_cases = args.rational_cases
        else:
            rational_cases = DEFAULT_RATIONAL_CASES

        print("Direct general rational flat-middle checks")
        total_paths = 0
        total_bands = 0
        total_coefficients = 0
        for r, s in rational_cases:
            summary = check_rational_flat_middle(r, s, args.rational_max_deficit)
            total_paths += summary.path_count
            total_bands += summary.checked_bands
            total_coefficients += summary.checked_coefficients
            print(
                f"  PASS r/s={r}/{s}, M={summary.total_degree}, "
                f"paths={summary.path_count}, max_deficit_checked={summary.max_deficit_checked}, "
                f"bands={summary.checked_bands}, coefficients={summary.checked_coefficients}, "
                f"common_values={summary.representative_common_values}"
            )
        print(f"  total rational paths generated: {total_paths}")
        print(f"  total rational bands checked: {total_bands}")
        print(f"  total rational coefficients checked: {total_coefficients}")
        print()

    print("Overall status: PASS")


if __name__ == "__main__":
    main()
