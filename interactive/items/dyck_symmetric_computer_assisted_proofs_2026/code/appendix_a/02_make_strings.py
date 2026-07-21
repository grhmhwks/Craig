def make_strings(n, d):
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
