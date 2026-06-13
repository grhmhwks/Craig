from collections import Counter
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
