from __future__ import annotations

import math
from functools import lru_cache
from itertools import combinations, permutations
from math import comb


EXPECTED_CASE1_TABLE = {
    10: (33, 23),
    11: (26, 18),
    12: (16, 11),
    13: (9, 6),
    14: (None, None),
    15: (None, None),
    16: (None, None),
    17: (None, None),
    18: (None, None),
    19: (None, None),
    20: (None, None),
    21: (None, None),
}

EXPECTED_CASE2_TABLE = {
    0: (26, 18),
    1: (23, 16),
    2: (23, 16),
    3: (20, 14),
    4: (20, 14),
    5: (19, 13),
    6: (17, 12),
    7: (16, 11),
    8: (16, 11),
    9: (13, 9),
    10: (13, 9),
    11: (12, 8),
    12: (10, 7),
    13: (9, 6),
    14: (9, 6),
    15: (None, None),
    16: (None, None),
    17: (None, None),
    18: (None, None),
    19: (None, None),
    20: (None, None),
    21: (None, None),
}

EXPECTED_FINITE_COUNTS = {
    ("Case 1", "East"): {"children": 2473, "triples": 9919},
    ("Case 1", "West"): {"children": 2911, "triples": 10311},
    ("Case 2", "East"): {"children": 3860, "triples": 715},
    ("Case 2", "West"): {"children": 4827, "triples": 1756},
}


def unique_permutations(seq: tuple[int, ...]):
    """Yield all distinct permutations of seq."""

    seen = set()
    for perm in permutations(seq):
        if perm not in seen:
            seen.add(perm)
            yield perm


def is_far_apart_decomposable(vals: tuple[int, ...]) -> bool:
    """Return True iff vals has three disjoint pairs at distance at least 2."""

    indices = list(range(7))
    for pair1 in combinations(indices, 2):
        if abs(vals[pair1[0]] - vals[pair1[1]]) < 2:
            continue
        remaining1 = [i for i in indices if i not in pair1]
        for pair2 in combinations(remaining1, 2):
            if abs(vals[pair2[0]] - vals[pair2[1]]) < 2:
                continue
            remaining2 = [i for i in remaining1 if i not in pair2]
            for pair3 in combinations(remaining2, 2):
                if abs(vals[pair3[0]] - vals[pair3[1]]) >= 2:
                    return True
    return False


def east3_fails(p: tuple[int, ...]) -> bool:
    """East3 fails iff the central pair violates the reverse condition."""

    return p[3] > p[4] + 1


def east5_fails(p: tuple[int, ...]) -> bool:
    """Return True iff neither appendix East5 Case 2a nor 2b applies."""

    x_m1, x_0, x_1, x_2 = p[2], p[3], p[4], p[5]
    y_0 = x_m1 if x_m1 > x_0 + 1 else x_0
    case2a = (x_m1 > x_1 + 1) and (y_0 <= x_2 + 1)
    case2b = (x_m1 <= x_1 + 1) and (x_m1 <= x_2 + 1)
    return not case2a and not case2b


def is_valid_l_element(p: tuple[int, ...]) -> bool:
    """Return True iff p has affine first four and reverse last three."""

    return all(p[i + 1] <= p[i] + 1 for i in range(3)) and all(
        p[i] <= p[i + 1] + 1 for i in range(4, 6)
    )


def get_ew() -> set[tuple[int, ...]]:
    """Generate normalized East seven-term patterns surviving the preliminary tests."""

    valid_windows = set()
    base_sequences: list[tuple[int, ...]] = []

    def gen_base(seq: tuple[int, ...]) -> None:
        if len(seq) == 7:
            base_sequences.append(seq)
            return
        for step in (0, 1, 2):
            gen_base(seq + (seq[-1] + step,))

    gen_base((0,))

    for base in base_sequences:
        for perm in unique_permutations(base):
            if (
                is_valid_l_element(perm)
                and east3_fails(perm)
                and east5_fails(perm)
                and is_far_apart_decomposable(perm)
            ):
                valid_windows.add(perm)

    return valid_windows


def get_ww(ew: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    """West windows are ordinary reversals of East windows."""

    return {tuple(reversed(w)) for w in ew}


def window_stats(window: tuple[int, ...], m: int, suffix_len: int) -> tuple[int, int]:
    """Compute corrected local id and q0 for a window and prefix max m."""

    seen = {}
    win_first = []
    for i, value in enumerate(window):
        if value not in seen:
            seen[value] = i
            win_first.append(True)
        else:
            win_first.append(False)

    is_initial = [win_first[i] and window[i] > m for i in range(len(window))]

    pair_count = 0
    for i in range(len(window)):
        for j in range(i + 1, len(window)):
            vi, vj = window[i], window[j]
            if vi > vj + 1:
                pair_count += 1
            elif vi < vj and not is_initial[i]:
                pair_count += 1

    suffix_start = len(window) - suffix_len
    suffix_correction = 0
    for j in range(suffix_start, len(window)):
        for value in range(m + 1, window[j]):
            if value not in window[:j]:
                suffix_correction += 1

    int_defc = pair_count - suffix_correction

    q0 = sum(max(0, (m - 1) - value) for i, value in enumerate(window) if not is_initial[i])
    return int_defc, q0


def compute_id_mid(window: tuple[int, ...], suffix_len: int) -> tuple[int, int]:
    """Return id_mid(w)=id(w,max(w[0]-1,w[6]-1,mid(w)))."""

    mid_value = sorted(window, reverse=True)[3]
    m = max(window[0] - 1, window[6] - 1, mid_value)
    int_defc, _ = window_stats(window, m, suffix_len)
    return int_defc, m


def compute_id_base(window: tuple[int, ...], suffix_len: int) -> int:
    """Return id_base(w)=id(w,max(w[0]-1,w[6]-1))."""

    int_defc, _ = window_stats(window, max(window[0] - 1, window[6] - 1), suffix_len)
    return int_defc


def compute_k_from_n(n_value: int) -> int:
    """Largest K with C(K,2) <= C(n,2)/2."""

    half = comb(n_value, 2) // 2
    test = 0
    while comb(test + 1, 2) <= half:
        test += 1
    return test


def compute_nk_case1(id_val: int) -> tuple[int | None, int | None]:
    """Compute Case 1 N(id), K(id), including the -4 area penalty."""

    max_n = None
    for n_value in range(8, 300):
        m0 = math.ceil((n_value + id_val - 16) / 3)
        q_star = 3 * m0 - (n_value + id_val - 16)
        lhs_twice = 2 * (comb(m0 + 1, 2) + (m0 - 1) * (n_value - m0 - 1) - q_star)
        rhs_twice = comb(n_value, 2) - id_val - q_star - 3 * (n_value - m0 - 8) - 8
        if lhs_twice <= rhs_twice:
            max_n = n_value
    if max_n is None:
        return None, None
    return max_n, compute_k_from_n(max_n)


def compute_nk_case2(id_val: int) -> tuple[int | None, int | None]:
    """Compute Case 2 N(id), K(id), including the -4 area penalty."""

    max_n = None
    for n_value in range(8, 300):
        chi_numer = 2 * n_value + id_val - 24
        m0 = max(0, math.ceil(chi_numer / 4))
        q_star = max(0, min(4 * m0 - chi_numer, 3))
        lhs_twice = 2 * (comb(m0 + 1, 2) + (m0 - 1) * (n_value - m0 - 1) - q_star)
        rhs_twice = comb(n_value, 2) - id_val - q_star - 4 * (n_value - m0 - 8) - 8
        if lhs_twice <= rhs_twice:
            max_n = n_value
    if max_n is None:
        return None, None
    return max_n, compute_k_from_n(max_n)


def get_groups(window: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Partition sorted(window) into maximal blocks separated by gaps at least 2."""

    sorted_vals = sorted(window)
    groups: list[tuple[int, ...]] = []
    current = [sorted_vals[0]]
    for i in range(1, len(sorted_vals)):
        if sorted_vals[i] - sorted_vals[i - 1] <= 1:
            current.append(sorted_vals[i])
        else:
            groups.append(tuple(current))
            current = [sorted_vals[i]]
    groups.append(tuple(current))
    return groups


@lru_cache(maxsize=None)
def get_children_absolute(window: tuple[int, ...], k_limit: int) -> tuple[tuple[int, ...], ...]:
    """Generate absolute gap-expanded children with max value at most k_limit."""

    extra = k_limit - max(window)
    if extra < 0:
        return ()

    groups = get_groups(window)
    num_gaps = len(groups) + 1
    children = set()

    def gen_compositions(remaining: int, num_parts: int, current: tuple[int, ...] = ()):
        if num_parts == 1:
            yield current + (remaining,)
            return
        for part in range(remaining + 1):
            yield from gen_compositions(remaining - part, num_parts - 1, current + (part,))

    for composition in gen_compositions(extra, num_gaps):
        cumulative_shift = 0
        group_shifts = []
        for gap_index in range(len(groups)):
            cumulative_shift += composition[gap_index]
            group_shifts.append(cumulative_shift)

        value_map = {}
        for group_index, group in enumerate(groups):
            for value in group:
                if value not in value_map:
                    value_map[value] = value + group_shifts[group_index]

        children.add(tuple(value_map[value] for value in window))

    return tuple(sorted(children))


def gen_partitions(total: int, max_parts: int, max_val: int):
    """Yield partitions of exactly total with <= max_parts parts in [1,max_val]."""

    if total == 0:
        yield ()
        return
    if max_parts == 0 or max_val <= 0:
        return
    for first in range(min(total, max_val), 0, -1):
        for rest in gen_partitions(total - first, max_parts - 1, first):
            yield (first,) + rest


def gen_partitions_upto(max_total: int, max_parts: int, max_val: int):
    """Yield partitions with total <= max_total and bounded length/value."""

    yield ()
    if max_total <= 0 or max_parts <= 0 or max_val <= 0:
        return
    for total in range(1, max_total + 1):
        yield from gen_partitions(total, max_parts, max_val)


@lru_cache(maxsize=None)
def cached_partitions_upto(max_total: int, max_parts: int, max_val: int) -> tuple[tuple[int, ...], ...]:
    """Cached tuple form of gen_partitions_upto."""

    return tuple(gen_partitions_upto(max_total, max_parts, max_val))


def compute_defc_and_area(seq: list[int]) -> tuple[int, int]:
    """Compute defc=binom(n,2)-area-dinv and area=sum(seq)."""

    dinv = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j] or seq[i] == seq[j] + 1:
                dinv += 1
    area = sum(seq)
    return comb(len(seq), 2) - area - dinv, area


@lru_cache(maxsize=None)
def m_max_for_n(n_value: int) -> int:
    """Largest m satisfying C(m,2) <= floor(C(n,2)/2)."""

    half = comb(n_value, 2) // 2
    value = 0
    while comb(value + 1, 2) <= half:
        value += 1
    return value


@lru_cache(maxsize=None)
def first_n_with_m_allowed(m_value: int) -> int:
    """Smallest n>=8 for which m satisfies the prefix area bound."""

    n_value = 8
    while m_value > m_max_for_n(n_value):
        n_value += 1
    return n_value


def deficit_n_upper(
    coeff: int,
    m_value: int,
    int_defc: int,
    q0: int,
    n_limit: int,
) -> int:
    """Largest n that can survive the deficit lower bound with q'=0."""

    numerator = coeff * m_value + 8 * coeff - 8 - int_defc - q0
    if coeff == 2:
        return n_limit
    return min(n_limit, numerator // (coeff - 2))


def check_window_single(
    *,
    case_label: str,
    side_label: str,
    base_window: tuple[int, ...],
    child: tuple[int, ...],
    id_val: int,
    n_value: int,
    m_value: int,
    g_value: int,
    coeff: int,
    int_defc_q0: tuple[int, int],
    child_area: int,
) -> dict | None:
    """Return first counterexample for one child/n/m triple, if any."""

    target_defc = 2 * n_value - 8
    total_free = n_value - m_value - 8
    if total_free < 0:
        return None

    int_defc, q0 = int_defc_q0
    q_prime_max = target_defc - int_defc - q0 - coeff * total_free
    if q_prime_max < 0:
        return None

    max_part = max(0, m_value - 1)
    prefix = list(range(m_value + 1))
    prefix_area = comb(m_value + 1, 2)
    m_repeats = [m_value]
    window_list = list(child)
    m_choose = comb(n_value, 2)

    for repeat_count in range(total_free + 1):
        if m_value == 0 and repeat_count < total_free:
            continue

        middle_len = total_free - repeat_count
        base_area = prefix_area + repeat_count * m_value + child_area
        max_partition_sum = min(q_prime_max, middle_len * max_part)
        min_possible_area = base_area + middle_len * (m_value - 1) - max_partition_sum
        if 2 * min_possible_area > m_choose - 8:
            continue

        for partition in cached_partitions_upto(q_prime_max, middle_len, max_part):
            extended = list(partition) + [0] * (middle_len - len(partition))
            middle = [m_value - 1 - deficit for deficit in reversed(extended)]
            seq = prefix + m_repeats * repeat_count + middle + window_list
            defc, area = compute_defc_and_area(seq)

            if defc > target_defc:
                continue
            if 2 * area > m_choose - defc - 8:
                continue

            return {
                "case": case_label,
                "side": side_label,
                "base_window": base_window,
                "child": child,
                "id": id_val,
                "n": n_value,
                "m": m_value,
                "g": g_value,
                "coeff": coeff,
                "repeat_count": repeat_count,
                "middle_len": middle_len,
                "partition": partition,
                "prefix": prefix + m_repeats * repeat_count + middle,
                "seq": seq,
                "defc": defc,
                "area": area,
                "target_defc": target_defc,
            }

    return None


def compare_threshold_table(
    label: str,
    computed: dict[int, tuple[int | None, int | None]],
    expected: dict[int, tuple[int | None, int | None]],
) -> bool:
    """Print an exact threshold table comparison."""

    mismatches = []
    for id_val in sorted(expected):
        if computed.get(id_val) != expected[id_val]:
            mismatches.append((id_val, computed.get(id_val), expected[id_val]))

    if not mismatches:
        print(f"{label} threshold table comparison: MATCH")
        return True

    print(f"{label} threshold table comparison: MISMATCH")
    for id_val, got, want in mismatches:
        print(f"  id={id_val}: computed={got}, expected={want}")
    return False


def print_table(label: str, table: dict[int, tuple[int | None, int | None]]) -> None:
    """Print a threshold table."""

    print(label)
    print(f"{'id':>4} {'N':>8} {'K':>8}")
    for id_val in sorted(table):
        n_value, k_value = table[id_val]
        n_text = "--" if n_value is None else str(n_value)
        k_text = "--" if k_value is None else str(k_value)
        print(f"{id_val:>4} {n_text:>8} {k_text:>8}")
    print()


def build_threshold_table(case_num: int) -> dict[int, tuple[int | None, int | None]]:
    """Build the threshold table for one case."""

    if case_num == 1:
        return {id_val: compute_nk_case1(id_val) for id_val in range(10, 22)}
    return {id_val: compute_nk_case2(id_val) for id_val in range(0, 22)}


def verify_id_mid_bound(windows: dict[str, set[tuple[int, ...]]]) -> bool:
    """Verify id_mid(w)>=10 over EW union WW."""

    min_record = None
    distribution: dict[int, int] = {}
    for suffix_len, side_label, side_windows in (
        (3, "East", windows["East"]),
        (4, "West", windows["West"]),
    ):
        for window in side_windows:
            id_val, threshold = compute_id_mid(window, suffix_len)
            distribution[id_val] = distribution.get(id_val, 0) + 1
            if min_record is None or id_val < min_record[0]:
                min_record = (id_val, threshold, side_label, window)

    assert min_record is not None
    ok = min_record[0] >= 10
    print(
        "id_mid structural check over EW union WW: "
        f"{'PASS' if ok else 'FAIL'} (min id_mid={min_record[0]}, "
        f"threshold={min_record[1]}, side={min_record[2]}, window={min_record[3]})"
    )
    print(f"id_mid distribution: {dict(sorted(distribution.items()))}\n")
    return ok


def id_from_table(
    id_val: int,
    table: dict[int, tuple[int | None, int | None]],
    *,
    case_label: str,
    side_label: str,
    window: tuple[int, ...],
) -> tuple[int | None, int | None]:
    """Look up an id without clamping; reject unexpected values."""

    if id_val not in table:
        raise ValueError(
            f"Unexpected id in {case_label} {side_label}: id={id_val}, window={window}"
        )
    return table[id_val]


def run_case(
    *,
    case_num: int,
    side_label: str,
    windows: set[tuple[int, ...]],
    table: dict[int, tuple[int | None, int | None]],
) -> tuple[list[dict], dict[str, int]]:
    """Run one finite case."""

    case_label = f"Case {case_num}"
    problems = []
    suffix_len = 3 if side_label == "East" else 4
    windows_checked = 0
    children_generated = 0
    active_children = 0
    triples_checked = 0

    for base_window in sorted(windows):
        windows_checked += 1
        if case_num == 1:
            id_val, _ = compute_id_mid(base_window, suffix_len)
        else:
            id_val = compute_id_base(base_window, suffix_len)

        n_limit, k_limit = id_from_table(
            id_val,
            table,
            case_label=case_label,
            side_label=side_label,
            window=base_window,
        )
        if n_limit is None or k_limit is None:
            continue

        children = get_children_absolute(base_window, k_limit)
        children_generated += len(children)
        for child in children:
            child_has_checked_triple = False
            child_area = sum(child)
            fourth_largest = sorted(child, reverse=True)[3]
            if case_num == 1:
                m_start = max(0, child[0] - 1, child[6] - 1, fourth_largest)
                m_stop = m_max_for_n(n_limit)
            else:
                m_start = max(0, child[0] - 1, child[6] - 1)
                m_stop = min(m_max_for_n(n_limit), fourth_largest - 1)

            if m_start > m_stop:
                continue

            for m_value in range(m_start, m_stop + 1):
                g_value = sum(1 for value in child if value > m_value)
                if case_num == 1:
                    if g_value > 3:
                        continue
                    coeff = 3
                else:
                    if g_value < 4:
                        continue
                    coeff = g_value

                stats = window_stats(child, m_value, suffix_len)
                n_start = max(8, m_value + 8, first_n_with_m_allowed(m_value))
                n_stop = deficit_n_upper(coeff, m_value, stats[0], stats[1], n_limit)
                if n_start > n_stop:
                    continue

                for n_value in range(n_start, n_stop + 1):
                    triples_checked += 1
                    child_has_checked_triple = True
                    problem = check_window_single(
                        case_label=case_label,
                        side_label=side_label,
                        base_window=base_window,
                        child=child,
                        id_val=id_val,
                        n_value=n_value,
                        m_value=m_value,
                        g_value=g_value,
                        coeff=coeff,
                        int_defc_q0=stats,
                        child_area=child_area,
                    )
                    if problem is not None:
                        problems.append(problem)
                        print_first_failure(problem)
                        return problems, {
                            "windows": windows_checked,
                            "children": children_generated,
                            "active_children": active_children,
                            "triples": triples_checked,
                        }

            if child_has_checked_triple:
                active_children += 1

    counts = {
        "windows": windows_checked,
        "children": children_generated,
        "active_children": active_children,
        "triples": triples_checked,
    }
    print(
        f"{case_label} {side_label}: windows={windows_checked}, "
        f"children={children_generated}, active_children={active_children}, "
        f"triples={triples_checked}, problems={len(problems)}"
    )
    return problems, counts


def print_first_failure(problem: dict) -> None:
    """Print the first failed obligation."""

    print("FIRST FAILURE")
    for key in (
        "case",
        "side",
        "base_window",
        "child",
        "id",
        "n",
        "m",
        "g",
        "coeff",
        "repeat_count",
        "middle_len",
        "partition",
        "prefix",
        "seq",
        "defc",
        "area",
        "target_defc",
    ):
        print(f"  {key}: {problem[key]}")


def compare_counts(counts_by_case: dict[tuple[str, str], dict[str, float | int]]) -> bool:
    """Compare finite-search counts with the expected finite-check counts."""

    all_match = True
    print("\nExpected finite-count comparison:")
    for key, expected in EXPECTED_FINITE_COUNTS.items():
        got = counts_by_case[key]
        got_pair = {"children": int(got["children"]), "triples": int(got["triples"])}
        if got_pair == expected:
            print(f"  {key[0]} {key[1]}: MATCH {got_pair}")
        else:
            all_match = False
            print(f"  {key[0]} {key[1]}: MISMATCH got={got_pair}, expected={expected}")

    if not all_match:
        print(
            "  Count note: children are absolute generated children for finite "
            "table rows; triples are finite (child,n,m) checks after actual-g "
            "deficit pruning."
        )
    print()
    return all_match


def main() -> None:
    """Run the East7-West7 seven-window checker."""

    ew = get_ew()
    ww = get_ww(ew)
    ew_ww = ew | ww
    print(f"  |EW| = {len(ew)}, |WW| = {len(ww)}, |EW union WW| = {len(ew_ww)}\n")

    case1_table = build_threshold_table(case_num=1)
    case2_table = build_threshold_table(case_num=2)
    print_table("Case 1 threshold table", case1_table)
    print_table("Case 2 threshold table", case2_table)

    table_results = [
        compare_threshold_table("Case 1", case1_table, EXPECTED_CASE1_TABLE),
        compare_threshold_table("Case 2", case2_table, EXPECTED_CASE2_TABLE),
    ]
    print()

    id_mid_ok = verify_id_mid_bound({"East": ew, "West": ww})

    all_problems = []
    counts_by_case: dict[tuple[str, str], dict[str, float | int]] = {}

    for case_num, side_label, windows, table in (
        (1, "East", ew, case1_table),
        (1, "West", ww, case1_table),
        (2, "East", ew, case2_table),
        (2, "West", ww, case2_table),
    ):
        problems, counts = run_case(
            case_num=case_num,
            side_label=side_label,
            windows=windows,
            table=table,
        )
        all_problems.extend(problems)
        counts_by_case[(f"Case {case_num}", side_label)] = counts

    counts_match = compare_counts(counts_by_case)

    tables_ok = all(table_results)
    if tables_ok:
        print("Threshold-table checks: MATCH")
    else:
        print("Threshold-table checks: MISMATCH")

    if id_mid_ok:
        print("id_mid>=10 check: PASS")
    else:
        print("id_mid>=10 check: FAIL")

    if tables_ok and id_mid_ok and not all_problems:
        if not counts_match:
            print("Counts differ from expected finite counts; see comparison above.")
        print("SUCCESS: East7/West7 seven-window verification passed.")
        return

    print(f"FAILED: problems={len(all_problems)}, tables_ok={tables_ok}, id_mid_ok={id_mid_ok}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()

