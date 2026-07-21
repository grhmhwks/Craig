"""Bounded checks for flat middle coefficients of classical q,t-Catalan.

The checked statement is the finite version of the flat-middle consequence of
the Dyck-skeleton decomposition formula.  For each checked n and each
0 <= d <= 2n-8, this script computes direct coefficients of

    C_n(q,t) = sum_D q^area(D) t^dinv(D)

over all Dyck area sequences D of length n, then verifies that the coefficients
of q^j t^(M-d-j), d <= j <= M-2d, are all equal to the number of special Dyck
skeletons of length n and deficit d.

These are bounded computational checks.  They are not a proof of the
flat-middle theorem or of the larger flat-middle conjecture.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import comb
from typing import Sequence


def is_dyck_sequence(seq: Sequence[int]) -> bool:
    """Return whether seq is a Dyck area sequence in the source convention."""

    return (
        len(seq) > 0
        and seq[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in seq)
        and all(seq[index + 1] <= seq[index] + 1 for index in range(len(seq) - 1))
    )


def generate_dyck_sequences(n: int) -> list[tuple[int, ...]]:
    """Generate all Dyck area sequences of length n."""

    if n <= 0:
        raise ValueError("n must be positive")

    out: list[tuple[int, ...]] = []

    def rec(seq: list[int]) -> None:
        if len(seq) == n:
            out.append(tuple(seq))
            return
        for value in range(seq[-1] + 2):
            rec(seq + [value])

    rec([0])
    return out


def area_statistic(seq: Sequence[int]) -> int:
    return sum(seq)


def di_statistic(seq: Sequence[int]) -> int:
    """Count pairs i<j with seq[i] = seq[j]+1."""

    values = tuple(seq)
    return sum(
        1
        for left in range(len(values))
        for right in range(left + 1, len(values))
        if values[left] == values[right] + 1
    )


def nv_statistic(seq: Sequence[int]) -> int:
    """Count pairs i<j with seq[i] = seq[j]."""

    values = tuple(seq)
    return sum(
        1
        for left in range(len(values))
        for right in range(left + 1, len(values))
        if values[left] == values[right]
    )


def dinv_statistic(seq: Sequence[int]) -> int:
    return di_statistic(seq) + nv_statistic(seq)


def deficit_pair_count(seq: Sequence[int]) -> int:
    """Count the source paper's two explicit deficit-pair types."""

    values = tuple(seq)
    total = 0
    first_seen: set[int] = set()
    for left, left_value in enumerate(values):
        left_is_first = left_value not in first_seen
        first_seen.add(left_value)
        for right in range(left + 1, len(values)):
            right_value = values[right]
            type_a = left_value > right_value + 1
            type_b = left_value < right_value and not left_is_first
            if type_a or type_b:
                total += 1
    return total


def deficit_statistic(seq: Sequence[int]) -> int:
    n = len(seq)
    return comb(n, 2) - area_statistic(seq) - dinv_statistic(seq)


def find_extractable_position(seq: Sequence[int], *, include_final: bool = True) -> int | None:
    """Return the leftmost extractable position, if any."""

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
    return is_dyck_sequence(seq) and find_extractable_position(seq, include_final=True) is None


def excluded_full_skeleton(n: int) -> tuple[int, ...]:
    """Return the exceptional full skeleton excluded from the special count."""

    if n < 4:
        return ()
    return (0, 0) + (1,) + (0,) * (n - 4) + (1,)


def is_special_dyck_skeleton(seq: Sequence[int]) -> bool:
    values = tuple(seq)
    return is_full_dyck_skeleton(values) and values != excluded_full_skeleton(len(values))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_check(n_min: int, n_max: int, max_representative_bands: int) -> dict[str, object]:
    total_sequences = 0
    dyck_validation_checks = 0
    formula_pair_deficit_checks = 0
    coefficient_total_checks = 0
    checked_bands = 0
    checked_coefficients = 0
    flat_band_checks = 0
    skeleton_match_checks = 0
    sequences_by_n: dict[int, int] = {}
    special_skeleton_counts: dict[int, dict[int, int]] = {}
    representative_bands: list[dict[str, object]] = []

    for n in range(n_min, n_max + 1):
        m_total = comb(n, 2)
        coeffs: Counter[tuple[int, int]] = Counter()
        skeleton_counts: Counter[int] = Counter()
        sequences = generate_dyck_sequences(n)
        sequences_by_n[n] = len(sequences)
        total_sequences += len(sequences)

        for seq in sequences:
            require(is_dyck_sequence(seq), f"generator produced non-Dyck sequence: {seq}")
            dyck_validation_checks += 1

            area = area_statistic(seq)
            dinv = dinv_statistic(seq)
            formula_defc = deficit_statistic(seq)
            pair_defc = deficit_pair_count(seq)
            require(
                formula_defc == pair_defc,
                "formula/pair deficit mismatch: "
                f"n={n}, seq={seq}, formula={formula_defc}, pairs={pair_defc}",
            )
            require(
                formula_defc == m_total - area - dinv,
                f"deficit formula mismatch: n={n}, seq={seq}",
            )
            formula_pair_deficit_checks += 1
            coeffs[(area, dinv)] += 1

            if is_special_dyck_skeleton(seq):
                require(
                    area <= formula_defc,
                    f"special skeleton violates area <= deficit: n={n}, seq={seq}",
                )
                skeleton_counts[formula_defc] += 1

        require(
            sum(coeffs.values()) == len(sequences),
            f"coefficient dictionary total mismatch for n={n}",
        )
        coefficient_total_checks += 1
        special_skeleton_counts[n] = dict(sorted(skeleton_counts.items()))

        for d in range(0, 2 * n - 7):
            target = skeleton_counts[d]
            band: list[tuple[int, int, int]] = []
            for j in range(d, m_total - 2 * d + 1):
                coeff = coeffs[(j, m_total - d - j)]
                band.append((j, m_total - d - j, coeff))
                require(
                    coeff == target,
                    "flat middle coefficient mismatch: "
                    f"n={n}, d={d}, target_special_skeletons={target}, "
                    f"at q^{j} t^{m_total - d - j} coefficient={coeff}, band={band}",
                )
                checked_coefficients += 1
                skeleton_match_checks += 1

            require(
                len({coeff for _, _, coeff in band}) <= 1,
                f"band is not flat: n={n}, d={d}, band={band}",
            )
            flat_band_checks += 1
            checked_bands += 1

            if len(representative_bands) < max_representative_bands and (
                d > 0 or not representative_bands
            ):
                representative_bands.append(
                    {
                        "n": n,
                        "d": d,
                        "special_skeleton_count": target,
                        "band": band,
                    }
                )

    require(
        any(item["d"] > 0 for item in representative_bands),
        "representative bands did not include a nonzero deficit",
    )

    return {
        "n_min": n_min,
        "n_max": n_max,
        "total_sequences": total_sequences,
        "sequences_by_n": sequences_by_n,
        "special_skeleton_counts": special_skeleton_counts,
        "dyck_validation_checks": dyck_validation_checks,
        "formula_pair_deficit_checks": formula_pair_deficit_checks,
        "coefficient_total_checks": coefficient_total_checks,
        "checked_bands": checked_bands,
        "checked_coefficients": checked_coefficients,
        "flat_band_checks": flat_band_checks,
        "skeleton_match_checks": skeleton_match_checks,
        "representative_bands": representative_bands,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-min", type=int, default=4, help="smallest n to check")
    parser.add_argument("--n-max", type=int, default=8, help="largest n to check")
    parser.add_argument(
        "--representative-bands",
        type=int,
        default=10,
        help="maximum number of representative bands to print",
    )
    args = parser.parse_args()

    if args.n_min < 4 or args.n_max < args.n_min:
        raise SystemExit("require 4 <= n-min <= n-max")
    if args.representative_bands < 1:
        raise SystemExit("representative-bands must be positive")

    summary = run_check(args.n_min, args.n_max, args.representative_bands)

    print("Flat middle coefficient bounded check")
    print(f"  n range: {summary['n_min']}..{summary['n_max']}")
    print("  direct coefficient convention: each Dyck sequence contributes q^area t^dinv")
    print(f"  checked theorem range: 0 <= d <= 2n-8")
    print(f"  generated Dyck sequences: {summary['total_sequences']}")
    print(f"  sequences by n: {summary['sequences_by_n']}")
    print(f"  special skeleton counts by n,d: {summary['special_skeleton_counts']}")
    print(f"  Dyck validation checks: {summary['dyck_validation_checks']}")
    print(f"  formula-vs-pair deficit checks: {summary['formula_pair_deficit_checks']}")
    print(f"  coefficient total checks: {summary['coefficient_total_checks']}")
    print(f"  checked (n,d) bands: {summary['checked_bands']}")
    print(f"  checked coefficients in bands: {summary['checked_coefficients']}")
    print(f"  flat-band checks: {summary['flat_band_checks']}")
    print(f"  skeleton-count match checks: {summary['skeleton_match_checks']}")
    print(f"  representative bands: {summary['representative_bands']}")
    print("  PASS")


if __name__ == "__main__":
    main()
