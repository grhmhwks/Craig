from collections import Counter
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
