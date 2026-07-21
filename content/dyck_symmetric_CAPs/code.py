"""Finite appendix checks for the 2026 Dyck-symmetric-functions paper.

The mathematical checker bodies in this file are the Python listings printed
in Appendices A and B of Graham Hawkes,

    Dyck Symmetric Functions and Applications to q,t-Catalan Polynomials,
    arXiv:2605.13003 (2026).

The appendix listings are embedded below without algorithmic changes.  The
small command-line dispatcher is repository glue so that the four proof
checks can live in one readable ``code.py`` file.

Run, for example,

    python code.py residual
    python code.py seven-window
    python code.py limited-nonzero
    python code.py prefix
    python code.py all

Do not run with ``python -O``: assertions are part of the verification.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Appendix A.1: core Dyck-sequence routines (paper listing).
CORE_SOURCE = r'''from itertools import combinations
from math import comb

def is_Dyck(S):
    S = tuple(S)
    return (
        len(S) > 0
        and S[0] == 0
        and all(isinstance(x, int) and x >= 0 for x in S)
        and all(S[i + 1] <= S[i] + 1 for i in range(len(S) - 1))
    )

def generate_Dycks(n):
    out = []
    def rec(S):
        if len(S) == n:
            out.append(tuple(S))
            return
        for x in range(S[-1] + 2):
            rec(S + [x])
    rec([0])
    return out

def area(S):
    return sum(S)

def dinv(S):
    S = tuple(S)
    return sum(
        1
        for i in range(len(S))
        for j in range(i + 1, len(S))
        if S[i] == S[j] or S[i] == S[j] + 1
    )

def defc(S):
    return comb(len(S), 2) - area(S) - dinv(S)

def find_extractable(S):
    S = tuple(S)
    for j, x in enumerate(S):
        if x == 0:
            continue
        if sum(1 for i in range(j) if S[i] == x - 1) != 1:
            continue
        if j + 1 < len(S) and S[j + 1] > x:
            continue
        return j, x
    return None

def remove_at(S, j):
    S = tuple(S)
    return S[:j] + S[j + 1:]

def is_full_skeleton(S):
    return is_Dyck(S) and find_extractable(S) is None

def epsilon(n):
    return () if n < 4 else tuple([0, 0, 1] + [0] * (n - 4) + [1])

def omega(n):
    return tuple([0] * (n - 1) + [1])

def is_special_skeleton(S):
    S = tuple(S)
    return is_full_skeleton(S) and S != epsilon(len(S))

def inject(S, e):
    S = tuple(S)
    for i, x in enumerate(S):
        if x == e - 1:
            ans = S[:i + 1] + (e,) + S[i + 1:]
            assert is_Dyck(ans)
            return ans
    raise ValueError(f"cannot inject {e} into {S}")

def inject_right_to_left(base, entries):
    out = tuple(base)
    for e in reversed(tuple(entries)):
        out = inject(out, e)
    return out
# Local affine/reverse helpers.

def bk2(a, b):
    return (b, a) if a > b + 1 else (a, b)

def fw2(a, b):
    return (b, a) if b > a + 1 else (a, b)

def bk3(a, b, c):
    if a > b + 1:
        a, b = b, a
    if b > c + 1:
        b, c = c, b
    if a > b + 1:
        a, b = b, a
    return a, b, c
# Local East and West maps.

def East3(W):
    W = tuple(W)
    assert len(W) == 3
    return W if W[1] <= W[2] + 1 else None

def East5(W):
    W = tuple(W)
    assert len(W) == 5
    x_m2, x_m1, x_0, x_1, x_2 = W
    y_m1, y_0 = bk2(x_m1, x_0)
    if x_m1 > x_1 + 1 and y_0 <= x_2 + 1:
        return (x_m2, x_1, y_m1, y_0, x_2)
    if x_m1 <= x_1 + 1 and x_m1 <= x_2 + 1:
        return (x_m2, x_1, x_0, x_m1, x_2)
    return None
_CASE4A = {
    (3, 3, 4, 1, 2): (1, 2, 4, 3, 3),
    (3, 4, 4, 1, 2): (1, 2, 4, 3, 4),
    (4, 3, 4, 1, 2): (1, 2, 4, 4, 3),
    (2, 3, 4, 1, 2): (1, 2, 4, 3, 2),
}
_CASE4B = {
    (3, 3, 4, 2, 1): (2, 1, 4, 3, 3),
    (3, 4, 4, 2, 1): (2, 1, 4, 3, 4),
    (4, 3, 4, 2, 1): (2, 1, 4, 4, 3),
    (2, 3, 4, 2, 1): (2, 1, 4, 3, 2),
}
_CASE4C = {
    (3, 4, 4, 2, 2): (2, 2, 4, 4, 3),
    (3, 4, 5, 2, 2): (2, 2, 5, 4, 3),
}
_CASE4D = {
    (3, 3, 4): lambda o: (2, o, 4, 3, 3),
    (3, 4, 4): lambda o: (2, o, 4, 3, 4),
    (4, 3, 4): lambda o: (2, o, 4, 4, 3),
    (2, 3, 4): lambda o: (2, o, 2, 4, 3),
    (3, 4, 2): lambda o: (2, o, 4, 3, 2),
}

def East7(W):
    W = tuple(W)
    assert len(W) == 7
    x_m3, x_m2, x_m1, x_0, x_1, x_2, x_3 = W
    if x_0 <= x_1 + 1:
        return W
    y_m1, y_0 = bk2(x_m1, x_0)
    if x_m1 > x_1 + 1 and y_0 <= x_2 + 1:
        return (x_m3, x_m2, x_1, y_m1, y_0, x_2, x_3)
    if x_m1 <= x_1 + 1 and x_m1 <= x_2 + 1:
        return (x_m3, x_m2, x_1, x_0, x_m1, x_2, x_3)
    if min(x_m2, x_m1, x_0) > max(x_1, x_2) + 1:
        return (x_m3,) + fw2(x_1, x_2) + bk3(x_m2, x_m1, x_0) + (x_3,)
    shift = max(x_1, x_2) - 2
    reduced = (x_m2 - shift, x_m1 - shift, x_0 - shift,
               x_1 - shift, x_2 - shift)
    for table in (_CASE4A, _CASE4B, _CASE4C):
        if reduced in table:
            return (x_m3,) + tuple(y + shift for y in table[reduced]) + (x_3,)
    if reduced[4] == 2 and reduced[3] <= 0 and reduced[:3] in _CASE4D:
        return (x_m3,) + tuple(y + shift for y in _CASE4D[reduced[:3]](reduced[3])) + (x_3,)
    raise ValueError(f"East7 undefined on {W}")

def rev(W):
    return tuple(reversed(tuple(W)))

def West3(W):
    ans = East3(rev(W))
    return None if ans is None else rev(ans)

def West5(W):
    ans = East5(rev(W))
    return None if ans is None else rev(ans)

def West7(W):
    return rev(East7(rev(W)))

def is_far_apart_decomposable(W):
    W = tuple(W)
    assert len(W) == 7
    indices = list(range(7))
    for p1 in combinations(indices, 2):
        if abs(W[p1[0]] - W[p1[1]]) < 2:
            continue
        r1 = [i for i in indices if i not in p1]
        for p2 in combinations(r1, 2):
            if abs(W[p2[0]] - W[p2[1]]) < 2:
                continue
            r2 = [i for i in r1 if i not in p2]
            for p3 in combinations(r2, 2):
                if abs(W[p3[0]] - W[p3[1]]) >= 2:
                    return True
    return False
# Global up and down maps.

def up(S):
    S = tuple(S)
    n = len(S)
    if S == omega(n):
        return epsilon(n), 3
    if is_full_skeleton(S):
        return inject(S[:-1], S[-1] + 1), 3
    j1, e1 = find_extractable(S)
    C1 = remove_at(S, j1)
    sigma1 = C1 + (e1 - 1,)
    if East3(sigma1[-3:]) is not None:
        ans = inject_right_to_left(sigma1[:-2], (sigma1[-2] + 1, sigma1[-1] + 1))
        return ans, 3
    j2, e2 = find_extractable(C1)
    C2 = remove_at(C1, j2)
    sigma2 = C2 + (e1 - 1, e2 - 1)
    W5 = East5(sigma2[-5:])
    if W5 is not None:
        base = sigma2[:-5] + W5[:2]
        ans = inject_right_to_left(base, tuple(x + 1 for x in W5[2:]))
        return ans, 5
    j3, e3 = find_extractable(C2)
    C3 = remove_at(C2, j3)
    sigma3 = C3 + (e1 - 1, e2 - 1, e3 - 1)
    W7 = sigma3[-7:]
    assert not is_far_apart_decomposable(W7)
    E7 = East7(W7)
    new_sigma3 = sigma3[:-7] + E7
    ans = inject_right_to_left(new_sigma3[:-4], tuple(x + 1 for x in new_sigma3[-4:]))
    return ans, 7

def down(S):
    S = tuple(S)
    n = len(S)
    if S == epsilon(n):
        return omega(n), 3
    j1, f1 = find_extractable(S)
    D1 = remove_at(S, j1)
    candidate = D1 + (f1 - 1,)
    if find_extractable(candidate) is None:
        assert is_Dyck(candidate)
        return candidate, 3
    j2, f2 = find_extractable(D1)
    D2 = remove_at(D1, j2)
    tau1 = D2 + (f1 - 1, f2 - 1)
    if West3(tau1[-3:]) is not None:
        return inject(tau1[:-1], tau1[-1] + 1), 3
    j3, f3 = find_extractable(D2)
    D3 = remove_at(D2, j3)
    tau2 = D3 + (f1 - 1, f2 - 1, f3 - 1)
    W5 = West5(tau2[-5:])
    if W5 is not None:
        base = tau2[:-5] + W5[:3]
        ans = inject_right_to_left(base, tuple(x + 1 for x in W5[3:]))
        return ans, 5
    j4, f4 = find_extractable(D3)
    D4 = remove_at(D3, j4)
    tau3 = D4 + (f1 - 1, f2 - 1, f3 - 1, f4 - 1)
    W7 = tau3[-7:]
    assert not is_far_apart_decomposable(W7)
    new_tau3 = tau3[:-7] + West7(W7)
    ans = inject_right_to_left(new_tau3[:-3], tuple(x + 1 for x in new_tau3[-3:]))
    return ans, 7
'''

# Appendix A.2: lower-half string construction (paper listing).
MAKE_STRINGS_SOURCE = r'''def make_strings(n, d):
    ell = (comb(n, 2) - d) // 2
    all_dyck = [S for S in generate_Dycks(n) if defc(S) == d]
    target = {S for S in all_dyck if area(S) <= ell}
    starts = sorted(
        [S for S in target if is_special_skeleton(S)],
        key=lambda S: (area(S), S),
    )
    strings = []
    levels = []
    for start in starts:
        chain = [start]
        current = start
        while area(current) < ell:
            nxt, level = up(current)
            assert defc(nxt) == d
            assert area(nxt) == area(current) + 1
            chain.append(nxt)
            levels.append((current, nxt, level))
            current = nxt
        strings.append(tuple(chain))
    covered = [S for chain in strings for S in chain]
    assert set(covered) == target
    assert len(covered) == len(set(covered))
    return tuple(strings), tuple(levels)
'''

# Appendix B proof-checking listings.
PAPER_LISTINGS = {
    'residual': (
        'Appendix B.1 residual finite check',
        r'''from collections import Counter
from math import comb

def stop(message):
    raise AssertionError(message)

def is_dyck_sequence(seq):
    return (
        bool(seq)
        and seq[0] == 0
        and all(x >= 0 for x in seq)
        and all(seq[i + 1] <= seq[i] + 1
                for i in range(len(seq) - 1))
    )

def deficit_and_area(seq):
    first_index = {}
    for i, value in enumerate(seq):
        first_index.setdefault(value, i)
    deficit = 0
    for i, left in enumerate(seq):
        for right in seq[i + 1:]:
            if left > right + 1:
                deficit += 1
            elif left < right and first_index[left] != i:
                deficit += 1
    return deficit, sum(seq)

def generate_dyck_sequences(length):
    sequences = []
    def extend(prefix):
        if len(prefix) == length:
            sequences.append(prefix)
            return
        for next_value in range(prefix[-1] + 2):
            extend(prefix + (next_value,))
    extend((0,))
    return sequences

def leftmost_extractable(seq):
    for index, value in enumerate(seq):
        has_parent = sum(x == value - 1 for x in seq[:index]) == 1
        next_ok = index == len(seq) - 1 or seq[index + 1] <= value
        if value > 0 and has_parent and next_ok:
            return index, value
    return None

def remove_index(seq, index):
    return seq[:index] + seq[index + 1:]

def is_full_skeleton(seq):
    return is_dyck_sequence(seq) and leftmost_extractable(seq) is None

def almost_zero_sequence(length):
    return (0,) * (length - 1) + (1,)

def excluded_skeleton(length):
    return (0, 0, 1) + (0,) * (length - 4) + (1,)

def is_special_skeleton(seq):
    return is_full_skeleton(seq) and seq != excluded_skeleton(len(seq))

def inject_after_first_parent(seq, value):
    for index, entry in enumerate(seq):
        if entry == value - 1:
            result = seq[:index + 1] + (value,) + seq[index + 1:]
            if is_dyck_sequence(result):
                return result
            stop(("skeleton injection produced non-Dyck",
                  seq, value, result))
    stop(("skeleton injection failed", seq, value))

def east3_applies(window3):
    _, x0, x1 = window3
    return x0 <= x1 + 1

def west3_applies(window3):
    return east3_applies(tuple(reversed(window3)))

def east5_case2b_applies(window5):
    _, x_minus1, x0, x1, x2 = window5
    return (
        x0 > x1 + 1
        and x_minus1 <= x1 + 1
        and x_minus1 <= x2 + 1
    )

def west5_case2b_applies(window5):
    return east5_case2b_applies(tuple(reversed(window5)))

def check_up_prefix(seq, length, deficit, half_area_limit):
    if seq == almost_zero_sequence(length):
        return "up special"
    if is_full_skeleton(seq):
        result = inject_after_first_parent(seq[:-1], seq[-1] + 1)
        if len(result) != length:
            stop(("up skeleton changed length", seq, result))
        return "up skeleton"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: up first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    word1 = child1 + (value1 - 1,)
    if east3_applies(word1[-3:]):
        if index1 >= length - 2:
            stop(("position lemma: up/East3 position", seq, index1))
        return "up East3"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: up second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if not (index1 < length - 3 and index2 < len(child1) - 3):
        stop(("position lemma: up/East5 position",
              seq, index1, child1, index2))
    if not east5_case2b_applies(word2[-5:]):
        stop(("seven-window lemma: up would reach East7",
              length, deficit, half_area_limit, seq, word2[-5:]))
    return "up East5 case 2b"

def check_down_prefix(seq, length, deficit, half_area_limit):
    if seq == excluded_skeleton(length):
        return "down special"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: down first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    skeleton_candidate = child1 + (value1 - 1,)
    if is_full_skeleton(skeleton_candidate):
        if len(skeleton_candidate) != length:
            stop(("down skeleton changed length", seq, skeleton_candidate))
        return "down skeleton"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: down second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if west3_applies(word2[-3:]):
        if not (index1 < length - 1 and index2 < len(child1) - 1):
            stop(("position lemma: down/West3 position",
                  seq, index1, child1, index2))
        return "down West3"
    third = leftmost_extractable(child2)
    if third is None:
        stop(("extraction lemma: down third extraction failed",
              length, deficit, half_area_limit, seq, child2))
    index3, value3 = third
    child3 = remove_index(child2, index3)
    word3 = child3 + (value1 - 1, value2 - 1, value3 - 1)
    if not (
        index1 < length - 2
        and index2 < len(child1) - 2
        and index3 < len(child2) - 2
    ):
        stop(("position lemma: down/West5 position",
              seq, index1, child1, index2, child2, index3))
    if not west5_case2b_applies(word3[-5:]):
        stop(("seven-window lemma: down would reach West7",
              length, deficit, half_area_limit, seq, word3[-5:]))
    return "down West5 case 2b"

def main():
    up_counts = Counter()
    down_counts = Counter()
    by_length = {
        length: {"up": Counter(), "down": Counter()}
        for length in range(4, 8)
    }
    for length in range(4, 8):
        for seq in generate_dyck_sequences(length):
            deficit, area = deficit_and_area(seq)
            if deficit > 2 * length - 8:
                continue
            half_area_limit = (comb(length, 2) - deficit) // 2
            if area <= half_area_limit - 1:
                label = check_up_prefix(
                    seq, length, deficit, half_area_limit)
                up_counts[label] += 1
                by_length[length]["up"][label] += 1
            if area <= half_area_limit and not is_special_skeleton(seq):
                label = check_down_prefix(
                    seq, length, deficit, half_area_limit)
                down_counts[label] += 1
                by_length[length]["down"][label] += 1
    print("EverythingOkay = True")
    print("up counts  ", dict(up_counts))
    print("down counts", dict(down_counts))
    print()
    for length in range(4, 8):
        print(f"n={length}")
        print("  up:  ", dict(by_length[length]["up"]))
        print("  down:", dict(by_length[length]["down"]))
    print()
    print("No East7 or West7 branch was reached for 4 <= n <= 7.")
if __name__ == "__main__":
    main()
''',
    ),
    'seven-window': (
        'Appendix B.6 East7/West7 seven-window check',
        r'''from __future__ import annotations

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

''',
    ),
    'limited-nonzero': (
        'Appendix B.5 limited-nonzero check for Lemma 5.27',
        r'''from collections import Counter
from math import comb
N_MIN, N_MAX = 4, 13
MAX_NONZERO = 7

def require(test, message):
    if not test:
        raise AssertionError(message)

def nonzero_count(S):
    return sum(1 for x in S if x != 0)

def ell_value(n, d):
    return (comb(n, 2) - d) // 2

def check_image(source, image, n, d, delta):
    require(is_Dyck(image), f"non-Dyck image: {source} -> {image}")
    require(len(image) == n, f"length changed: {source} -> {image}")
    require(defc(image) == d, f"deficit changed: {source} -> {image}")
    require(area(image) == area(source) + delta,
            f"wrong area change: {source} -> {image}")

def checked_up(S, n, d, ell):
    S = tuple(S)
    if S == omega(n):
        image = epsilon(n)
        check_image(S, image, n, d, 1)
        return "up special", 3
    if is_full_skeleton(S):
        image = inject(S[:-1], S[-1] + 1)
        check_image(S, image, n, d, 1)
        return "up skeleton", 3
    j1, e1 = find_extractable(S)
    C1 = remove_at(S, j1)
    sigma1 = C1 + (e1 - 1,)
    if East3(sigma1[-3:]) is not None:
        require(j1 < n - 2, f"up East3 position bound: {S}")
        image = inject_right_to_left(sigma1[:-2],
                                     (sigma1[-2] + 1, sigma1[-1] + 1))
        check_image(S, image, n, d, 1)
        return "up East3", 3
    j2, e2 = find_extractable(C1)
    C2 = remove_at(C1, j2)
    sigma2 = C2 + (e1 - 1, e2 - 1)
    E5 = East5(sigma2[-5:])
    if E5 is not None:
        require(j1 < n - 3 and j2 < len(C1) - 3,
                f"up East5 position bound: {S}")
        base = sigma2[:-5] + E5[:2]
        image = inject_right_to_left(base, tuple(x + 1 for x in E5[2:]))
        check_image(S, image, n, d, 1)
        return "up East5", 5
    j3, e3 = find_extractable(C2)
    C3 = remove_at(C2, j3)
    sigma3 = C3 + (e1 - 1, e2 - 1, e3 - 1)
    W7 = sigma3[-7:]
    require(not is_far_apart_decomposable(W7), f"bad East7 window: {S}")
    require(j1 < n - 3 and j2 < len(C1) - 3 and j3 < len(C2) - 3,
            f"up East7 position bound: {S}")
    E7 = East7(W7)
    image = inject_right_to_left(sigma3[:-7] + E7[:-4],
                                 tuple(x + 1 for x in E7[-4:]))
    check_image(S, image, n, d, 1)
    return "up East7", 7

def checked_down(S, n, d, ell):
    S = tuple(S)
    if S == epsilon(n):
        image = omega(n)
        check_image(S, image, n, d, -1)
        return "down special", 3
    j1, f1 = find_extractable(S)
    D1 = remove_at(S, j1)
    candidate = D1 + (f1 - 1,)
    if find_extractable(candidate) is None:
        check_image(S, candidate, n, d, -1)
        return "down skeleton", 3
    j2, f2 = find_extractable(D1)
    D2 = remove_at(D1, j2)
    tau1 = D2 + (f1 - 1, f2 - 1)
    if West3(tau1[-3:]) is not None:
        require(j1 < n - 1 and j2 < len(D1) - 1,
                f"down West3 position bound: {S}")
        image = inject(tau1[:-1], tau1[-1] + 1)
        check_image(S, image, n, d, -1)
        return "down West3", 3
    j3, f3 = find_extractable(D2)
    D3 = remove_at(D2, j3)
    tau2 = D3 + (f1 - 1, f2 - 1, f3 - 1)
    W5 = West5(tau2[-5:])
    if W5 is not None:
        require(j1 < n - 2 and j2 < len(D1) - 2 and j3 < len(D2) - 2,
                f"down West5 position bound: {S}")
        base = tau2[:-5] + W5[:3]
        image = inject_right_to_left(base, tuple(x + 1 for x in W5[3:]))
        check_image(S, image, n, d, -1)
        return "down West5", 5
    j4, f4 = find_extractable(D3)
    D4 = remove_at(D3, j4)
    tau3 = D4 + (f1 - 1, f2 - 1, f3 - 1, f4 - 1)
    W7 = tau3[-7:]
    require(not is_far_apart_decomposable(W7), f"bad West7 window: {S}")
    require(j1 < n - 2 and j2 < len(D1) - 2
            and j3 < len(D2) - 2 and j4 < len(D3) - 2,
            f"down West7 position bound: {S}")
    E7 = West7(W7)
    image = inject_right_to_left(tau3[:-7] + E7[:-3],
                                 tuple(x + 1 for x in E7[-3:]))
    check_image(S, image, n, d, -1)
    return "down West7", 7

def run_limited_nonzero_checker():
    generated = {}
    eligible = Counter()
    branches = Counter()
    levels = Counter()
    failures = []
    for n in range(N_MIN, N_MAX + 1):
        seqs = [S for S in generate_Dycks(n) if nonzero_count(S) <= MAX_NONZERO]
        generated[n] = len(seqs)
        for S in seqs:
            d = defc(S)
            if d > 2 * n - 8:
                continue
            ell = ell_value(n, d)
            try:
                if area(S) < ell:
                    branch, level = checked_up(S, n, d, ell)
                    eligible[(n, "up")] += 1
                    branches[("up", branch)] += 1
                    levels[("up", level)] += 1
                if area(S) <= ell and not is_special_skeleton(S):
                    branch, level = checked_down(S, n, d, ell)
                    eligible[(n, "down")] += 1
                    branches[("down", branch)] += 1
                    levels[("down", level)] += 1
            except Exception as exc:
                failures.append((n, S, str(exc)))
    require(not failures, f"first failure: {failures[0] if failures else None}")
    up_total = sum(v for (n, direction), v in eligible.items()
                   if direction == "up")
    down_total = sum(v for (n, direction), v in eligible.items()
                     if direction == "down")
    print("generated by n:", generated)
    print("eligible up calls:", up_total)
    print("eligible down calls:", down_total)
    print("eligible calls by n/direction:", dict(sorted(eligible.items())))
    print("branches:", dict(sorted(branches.items())))
    print("levels:", dict(sorted(levels.items())))
    print("position-bound or image failures:", len(failures))
    print("status: PASS")
run_limited_nonzero_checker()
''',
    ),
    'prefix': (
        'Appendix B.5 prefix-form check for Lemma 5.27',
        r'''from collections import Counter
from itertools import product
from math import comb
N_MIN, N_MAX = 9, 16
EXPECTED = {
    (9, 1, "pq_lt_4"): 504, (9, 1, "pq_eq_4"): 3024,
    (10, 1, "pq_lt_4"): 720, (10, 1, "pq_eq_4"): 5040,
    (11, 1, "pq_lt_4"): 990, (11, 1, "pq_eq_4"): 7920,
    (12, 1, "pq_lt_4"): 1320, (12, 1, "pq_eq_4"): 11880,
    (13, 1, "pq_lt_4"): 1716, (13, 1, "pq_eq_4"): 17160,
    (14, 1, "pq_lt_4"): 2184, (14, 1, "pq_eq_4"): 24024,
    (15, 1, "pq_lt_4"): 2730, (15, 1, "pq_eq_4"): 32760,
    (16, 1, "pq_lt_4"): 3360, (16, 1, "pq_eq_4"): 43680,
    (9, 2, "pq_lt_4"): 336, (9, 2, "pq_eq_4"): 1680,
    (10, 2, "pq_lt_4"): 504, (10, 2, "pq_eq_4"): 3024,
    (11, 2, "pq_lt_4"): 720, (11, 2, "pq_eq_4"): 5040,
    (12, 2, "pq_lt_4"): 990, (12, 2, "pq_eq_4"): 7920,
    (13, 2, "pq_lt_4"): 1320, (13, 2, "pq_eq_4"): 11880,
    (14, 2, "pq_lt_4"): 1716, (14, 2, "pq_eq_4"): 17160,
    (15, 2, "pq_lt_4"): 2184, (15, 2, "pq_eq_4"): 24024,
    (16, 2, "pq_lt_4"): 2730, (16, 2, "pq_eq_4"): 32760,
}

def require(test, message):
    if not test:
        raise AssertionError(message)

def bounded_product(bounds):
    return product(*(range(bound + 1) for bound in bounds))

def defc(word):
    n = len(word)
    dinv_count = sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        if word[i] == word[j] or word[i] == word[j] + 1
    )
    return comb(n, 2) - area(word) - dinv_count

def claim_words(n, claim, subcase):
    if claim == 1 and subcase == "pq_lt_4":
        prefix = tuple(range(0, n - 3))
        bounds = (n - 3, n - 2, n - 1)
    elif claim == 1 and subcase == "pq_eq_4":
        prefix = tuple(range(0, n - 4))
        bounds = (n - 4, n - 3, n - 2, n - 1)
    elif claim == 2 and subcase == "pq_lt_4":
        prefix = (0,) + tuple(range(0, n - 4))
        bounds = (n - 4, n - 3, n - 2)
    elif claim == 2 and subcase == "pq_eq_4":
        prefix = (0,) + tuple(range(0, n - 5))
        bounds = (n - 5, n - 4, n - 3, n - 2)
    else:
        raise ValueError("unknown claim/subcase")
    for stars in bounded_product(bounds):
        yield prefix + stars

def run_prefix_checker():
    counts = Counter()
    failures = []
    for n in range(N_MIN, N_MAX + 1):
        M = comb(n, 2)
        for claim in (1, 2):
            for subcase in ("pq_lt_4", "pq_eq_4"):
                # In the p+q=4 boundary this is q+1 for up (2,2)
                # and q for down (1,3).
                adjustment = 3 if subcase == "pq_eq_4" else 0
                for word in claim_words(n, claim, subcase):
                    counts[(n, claim, subcase)] += 1
                    D = defc(word)
                    A = area(word)
                    deficit_contradiction = D > 2 * n - 8
                    area_contradiction = 2 * A > M - D - 2 * adjustment
                    if not (deficit_contradiction or area_contradiction):
                        failures.append((n, claim, subcase, word, D, A))
    require(dict(counts) == EXPECTED, "word counts do not match")
    require(not failures, f"first failure: {failures[0] if failures else None}")
    print("counts by n/claim/subcase:", dict(sorted(counts.items())))
    print("failures:", len(failures))
    print("status: PASS")
run_prefix_checker()
''',
    ),
}


CHECK_ORDER = ("residual", "limited-nonzero", "prefix", "seven-window")


def run_paper_listing(name: str) -> None:
    """Execute one appendix checker in a fresh shared paper namespace."""

    label, source = PAPER_LISTINGS[name]
    print(f"\n=== {label} ===", flush=True)
    namespace = {
        "__name__": "__main__",
        "__file__": f"<paper-listing:{name}>",
    }
    exec(compile(CORE_SOURCE, "<appendix-a-core>", "exec"), namespace)
    exec(compile(MAKE_STRINGS_SOURCE, "<appendix-a-make-strings>", "exec"), namespace)
    exec(compile(source, f"<appendix-b:{name}>", "exec"), namespace)


def extract_listings(destination: Path) -> None:
    """Write the embedded paper listings as separate source files."""

    destination.mkdir(parents=True, exist_ok=True)
    (destination / "appendix_a_core.py").write_text(CORE_SOURCE, encoding="utf-8")
    (destination / "appendix_a_make_strings.py").write_text(
        MAKE_STRINGS_SOURCE, encoding="utf-8"
    )
    for name, (_label, source) in PAPER_LISTINGS.items():
        (destination / f"appendix_b_{name.replace('-', '_')}.py").write_text(
            source, encoding="utf-8"
        )
    print(f"Wrote paper listings to {destination}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "check",
        nargs="?",
        default="all",
        choices=("all",) + CHECK_ORDER,
        help="appendix check to run (default: all)",
    )
    parser.add_argument(
        "--extract",
        type=Path,
        metavar="DIRECTORY",
        help="also write the embedded paper listings as separate .py files",
    )
    return parser.parse_args()


def main() -> None:
    if sys.flags.optimize:
        raise SystemExit(
            "Run with ordinary Python, not python -O: assertions are part of the checks."
        )

    args = parse_args()
    if args.extract is not None:
        extract_listings(args.extract)

    names = CHECK_ORDER if args.check == "all" else (args.check,)
    for name in names:
        run_paper_listing(name)

    print("\nAll requested appendix checks completed successfully.")


if __name__ == "__main__":
    main()
