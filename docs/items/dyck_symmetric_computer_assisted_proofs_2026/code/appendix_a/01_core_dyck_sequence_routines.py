from itertools import combinations
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
