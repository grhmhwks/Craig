"""Bounded checks for shifted Littlewood-Richardson conjectures.

This is a curated port of the two source scripts
``skew-GP-expansion.py`` and ``skew-GQ-expansion.py``.  It compares two
homogeneous-degree monomial expansions:

1. the direct skew expansion for a shifted skew shape ``shape/skew``;
2. the expansion obtained from the conjectural shifted Littlewood-Richardson
   rule into non-skew GP or GR functions.

The source GQ script checks the rule for GR functions; the source README notes
that this implies the same expansion for GQ functions.  The default examples
are intentionally small so the checker is quick.  Larger degrees and shapes can
be supplied from the command line.
"""

from __future__ import annotations

import argparse
import copy
import math
from typing import Literal


Kind = Literal["gp", "gq"]
Tableau = list[list[list[int]]]


def parse_shape(text: str) -> list[int]:
    if text.strip() == "":
        return []
    values = [int(part.strip()) for part in text.split(",") if part.strip()]
    if any(value < 0 for value in values):
        raise argparse.ArgumentTypeError("shape parts must be nonnegative")
    if any(values[i] < values[i + 1] for i in range(len(values) - 1)):
        raise argparse.ArgumentTypeError("shape parts must be weakly decreasing")
    return values


def normalized_skew(skew: list[int], shape: list[int]) -> list[int]:
    mu = list(skew)
    lam = list(shape)
    while len(mu) < len(lam):
        mu.append(0)
    if len(mu) > len(lam):
        raise ValueError("skew must have no more parts than shape")
    if any(mu[i] > lam[i] for i in range(len(lam))):
        raise ValueError("skew must be contained in shape")
    return mu


def standard_tabs(kind: Kind, alph: int, skew: list[int], shape: list[int]) -> list[list]:
    """Generate source-standard tableaux and their peak/repeat data."""

    mu = normalized_skew(skew, shape)
    empty_tab: Tableau = [[] for _ in shape]
    tab_list: list[list] = [[empty_tab, []]]

    for n in range(alph):
        new_list: list[list] = []
        for tab, positions in tab_list:
            for row_index in range(len(tab)):
                if len(tab[row_index]) > 0:
                    can_append_to_box = (
                        row_index == len(tab) - 1
                        or len(tab[row_index + 1]) == 0
                        or (
                            mu[row_index] + len(tab[row_index])
                            > mu[row_index + 1] + len(tab[row_index + 1]) + 1
                        )
                    )
                    if can_append_to_box:
                        t_cop = copy.deepcopy(tab)
                        t_cop[row_index][-1] += [n]
                        new_position = [row_index, mu[row_index] + len(t_cop[row_index]) + row_index]
                        new_list.append([t_cop, positions + [new_position]])

                if len(tab[row_index]) < shape[row_index] - mu[row_index]:
                    can_add_box = (
                        row_index == 0
                        or mu[row_index] + len(tab[row_index]) + 1
                        < mu[row_index - 1] + len(tab[row_index - 1])
                    )
                    if can_add_box:
                        t_cop = copy.deepcopy(tab)
                        t_cop[row_index] += [[n]]
                        new_position = [row_index, mu[row_index] + len(t_cop[row_index]) + row_index]
                        new_list.append([t_cop, positions + [new_position]])
        tab_list = new_list

    out: list[list] = []
    for tab, positions in tab_list:
        if any(len(tab[row]) != shape[row] - mu[row] for row in range(len(shape))):
            continue

        peak_set: list[int] = []
        repeat_set: list[int] = []
        diags = 0
        for i in range(0, len(positions) - 2):
            j = i + 1
            k = i + 2
            if positions[j][1] > positions[i][1] and positions[k][0] > positions[j][0]:
                peak_set.append(j)
            if kind == "gp":
                if positions[i] == positions[j] and positions[k][0] > positions[j][0]:
                    peak_set.append(j)
                if positions[j][1] > positions[i][1] and positions[j] == positions[k]:
                    peak_set.append(j)
                if positions[i] == positions[j] and positions[j] == positions[k]:
                    peak_set.append(j)

        for i in range(0, len(positions) - 1):
            if positions[i] == positions[i + 1]:
                if kind == "gp":
                    repeat_set.append(-(i + 1) if positions[i][0] == positions[i][1] - 1 else i + 1)
                else:
                    repeat_set.append(i)

        if kind == "gp":
            for row, col in positions:
                if row == col - 1:
                    diags += 1
            out.append([tab, peak_set, repeat_set, diags])
        else:
            out.append([tab, peak_set, repeat_set])
    return out


def partitions(n: int, k: int) -> list[list[int]]:
    if n <= 0:
        return [[]]
    par_list = [[1]]
    while sum(par_list[0]) < n:
        new_list: list[list[int]] = []
        for par in par_list:
            if len(par) == 1 or (len(par) > 1 and par[-1] < par[-2]):
                p_cop = copy.copy(par)
                p_cop[-1] += 1
                new_list.append(p_cop)
            if len(par) < k:
                p_cop = copy.copy(par)
                p_cop.append(1)
                new_list.append(p_cop)
        par_list = new_list
    return par_list


def polynomial(kind: Kind, tab_data: list, num_vars: int) -> list[list[int]]:
    values: list[list[int]] = []
    tab = tab_data[0]
    peak_set = tab_data[1]
    repeat_set = tab_data[2]
    diags = tab_data[3] if kind == "gp" else 0
    degree = sum(len(box) for row in tab for box in row)

    for par in partitions(degree, num_vars):
        weak_seq: list[int] = []
        for index, part in enumerate(par):
            weak_seq += [index + 1] * part

        good = True
        power_of_two = len(par) - diags
        for i in range(0, len(weak_seq) - 2):
            if weak_seq[i] == weak_seq[i + 1] == weak_seq[i + 2] and i + 1 in peak_set:
                good = False
        for i in range(0, len(weak_seq) - 1):
            if weak_seq[i] == weak_seq[i + 1]:
                if kind == "gp":
                    if -(i + 1) in repeat_set:
                        good = False
                    if i + 1 in repeat_set:
                        power_of_two -= 1
                elif i in repeat_set:
                    good = False
        if good:
            multiplicity = int(math.pow(2, power_of_two)) if kind == "gp" else 1
            values += [par] * multiplicity
    return values


def distinct_elements(values: list[list[int]]) -> list[list]:
    if not values:
        return []
    values = sorted(values, key=lambda x: str(x))
    out = [[1, values[0]]]
    for value in values[1:]:
        if value == out[-1][1]:
            out[-1][0] += 1
        else:
            out.append([1, value])
    out.reverse()
    return out


def monomial_exp(kind: Kind, degree: int, skew: list[int], shape: list[int], num_vars: int) -> list[list]:
    values: list[list[int]] = []
    for tab_data in standard_tabs(kind, degree, list(skew), list(shape)):
        values += polynomial(kind, tab_data, num_vars)
    return distinct_elements(values)


def sequences(length: int, maxi: int) -> list[list[int]]:
    seq_list = [[]]
    while len(seq_list[0]) < length:
        seq_list = [seq + [value] for seq in seq_list for value in range(maxi + 1)]
    return seq_list


def row(m: int, n: int) -> list[list[list[int]]]:
    """Create one-row shifted set-valued tableaux of length m and max entry n.

    The source representation is 1' -> 1, 1 -> 2, 2' -> 3, 2 -> 4, and so on.
    """

    row_tabs: list[list[list[int]]] = [[]]
    while len(row_tabs[0]) < m:
        new_tabs: list[list[list[int]]] = []
        for row_tab in row_tabs:
            previous = row_tab[-1][-1] if row_tab else 1
            for bit_string in sequences(2 * n + 1 - previous, 1):
                subset = [index + previous for index, bit in enumerate(bit_string) if bit == 0]
                if subset and (previous % 2 == 0 or previous < subset[0] or not row_tab):
                    new_tabs.append(row_tab + [subset])
        row_tabs = new_tabs
    return row_tabs


def over(top_row: list[list[int]], bottom_row: list[list[int]], offset: int) -> bool:
    for i, top in enumerate(top_row):
        bot = [float("inf")]
        if 0 <= i + offset < len(bottom_row):
            bot = bottom_row[i + offset]
        if max(top) > min(bot):
            return False
        if max(top) == min(bot) and max(top) % 2 == 0:
            return False
    return True


def flag(skew: list[int], shape: list[int]) -> list[Tableau]:
    mu = normalized_skew(skew, shape)
    if not shape:
        return []

    flag_tabs: list[Tableau] = [[one_row] for one_row in row(shape[0] - mu[0], 1)]
    for row_number in range(2, len(shape) + 1):
        new_tabs: list[Tableau] = []
        row_tabs = row(shape[row_number - 1] - mu[row_number - 1], row_number)
        for partial in flag_tabs:
            for new_row in row_tabs:
                if over(partial[-1], new_row, mu[row_number - 2] - 1 - mu[row_number - 1]):
                    new_tabs.append(partial + [new_row])
        flag_tabs = new_tabs
    return flag_tabs


def read_w(tableau: Tableau) -> list[int]:
    word: list[int] = []
    for row_index in range(len(tableau) - 1, -1, -1):
        for box in tableau[row_index]:
            word += list(box)
    return word


def no_prime_diag(tableau: Tableau, diag_rows: list[int]) -> bool:
    for row_index in diag_rows:
        if row_index < len(tableau) and tableau[row_index]:
            if any(entry % 2 == 1 for entry in tableau[row_index][0]):
                return False
    return True


def first_unprimed(word: list[int]) -> bool:
    if not word:
        return True
    maxi = max(word)
    if maxi % 2 == 1:
        return False
    starts = [0] * int(maxi / 2)
    for entry in word:
        base = math.ceil(entry / 2)
        if starts[base - 1] == 0:
            starts[base - 1] = 1 if entry % 2 == 0 else -1
    return all(value != -1 for value in starts)


def primed_start(tableau: Tableau) -> Tableau:
    result = copy.deepcopy(tableau)
    word = read_w(result)
    if not word or max(word) % 2 == 1:
        return result
    for n in range(1, int(max(word) / 2) + 1):
        changed = False
        for row_index in range(len(result) - 1, -1, -1):
            for box in result[row_index]:
                for entry_index, entry in enumerate(box):
                    if not changed and entry == 2 * n:
                        changed = True
                        box[entry_index] -= 1
    return result


def back(tableau: Tableau) -> list[int]:
    backword: list[int] = []
    for row in tableau:
        for box_index in range(len(row) - 1, -1, -1):
            box = copy.copy(row[box_index])
            box.sort(key=lambda x: -(x % 2) + 1 / x)
            backword += box
    return backword


def forw(tableau: Tableau) -> list[int]:
    forword: list[int] = []
    for row_index in range(len(tableau) - 1, -1, -1):
        for box in tableau[row_index]:
            copied = copy.copy(box)
            copied.sort(key=lambda x: (x % 2) + 1 / x)
            forword += copied
    return forword


def lattice(tableau: Tableau) -> bool:
    word_max = max(read_w(tableau), default=0)
    counts = [0] * (math.ceil(word_max / 2) + 3)

    for entry in back(tableau):
        base = math.ceil(entry / 2)
        if entry % 2 == 0:
            counts[base] += 1
            if base > 1 and counts[base] > counts[base - 1]:
                return False
        elif base > 1 and counts[base] == counts[base - 1]:
            return False

    for entry in forw(tableau):
        base = math.ceil(entry / 2)
        if entry % 2 == 1:
            counts[base] += 1
            if base > 1 and counts[base] > counts[base - 1]:
                return False
        elif counts[base + 1] == counts[base]:
            return False
    return True


def weights(word: list[int]) -> list[int]:
    max_base = max((math.ceil(entry / 2) for entry in word), default=0)
    counts = [0] * max(9, max_base)
    for entry in word:
        counts[math.ceil(entry / 2) - 1] += 1
    return counts


def rule_expand(kind: Kind, skew: list[int], shape: list[int]) -> list[list]:
    mu = normalized_skew(skew, shape)
    tableaux = flag(mu, shape)
    weights_seen: list[list[int]] = []

    if kind == "gp":
        diag_rows = [row_index for row_index in range(len(shape)) if mu[row_index] == 0]
        for tableau in tableaux:
            if no_prime_diag(tableau, diag_rows) and lattice(tableau):
                weights_seen.append(weights(read_w(tableau)))
    else:
        for tableau in tableaux:
            if first_unprimed(read_w(tableau)) and lattice(primed_start(tableau)):
                weights_seen.append(weights(read_w(tableau)))

    expanded = distinct_elements(weights_seen)
    expanded.sort(key=lambda x: str(x[1]))
    expanded.reverse()
    return expanded


def list_expand(kind: Kind, expansion: list[list], degree: int, num_vars: int) -> list[list]:
    values: list[list[int]] = []
    for multiplicity, shape in expansion:
        if sum(shape) <= degree:
            for monomial_multiplicity, partition in monomial_exp(kind, degree, [], shape, num_vars):
                values += [partition] * (monomial_multiplicity * multiplicity)
    return distinct_elements(values)


def compare(kind: Kind, degree: int, skew: list[int], shape: list[int], num_vars: int) -> dict[str, object]:
    direct = monomial_exp(kind, degree, list(skew), list(shape), num_vars)
    rule = rule_expand(kind, list(skew), list(shape))
    reconstructed = list_expand(kind, rule, degree, num_vars)
    return {
        "kind": kind,
        "degree": degree,
        "skew": list(skew),
        "shape": list(shape),
        "num_vars": num_vars,
        "direct": direct,
        "rule": rule,
        "reconstructed": reconstructed,
        "pass": direct == reconstructed,
    }


def run_case(kind: Kind, degree: int, skew: list[int], shape: list[int], num_vars: int) -> bool:
    result = compare(kind, degree, skew, shape, num_vars)
    label = "GP" if kind == "gp" else "GQ/GR"
    print(f"{label} shifted LR bounded check")
    print(f"  degree: {degree}")
    print(f"  shape/skew: {shape}/{skew}")
    print(f"  variables: {num_vars}")
    print(f"  direct monomial terms: {len(result['direct'])}")
    print(f"  conjectural rule terms: {len(result['rule'])}")
    print(f"  reconstructed monomial terms: {len(result['reconstructed'])}")
    print(f"  rule expansion: {result['rule']}")
    print(f"  PASS: {result['pass']}")
    return bool(result["pass"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["gp", "gq", "both"], default="both")
    parser.add_argument("--degree", type=int, default=5)
    parser.add_argument("--skew", type=parse_shape, default=parse_shape("1"))
    parser.add_argument("--shape", type=parse_shape, default=parse_shape("3,1"))
    parser.add_argument("--num-vars", type=int, default=3)
    args = parser.parse_args()

    if args.degree < 0:
        raise SystemExit("degree must be nonnegative")
    if args.num_vars <= 0:
        raise SystemExit("num-vars must be positive")
    normalized_skew(args.skew, args.shape)

    kinds: list[Kind] = ["gp", "gq"] if args.kind == "both" else [args.kind]  # type: ignore[list-item]
    passes = [run_case(kind, args.degree, args.skew, args.shape, args.num_vars) for kind in kinds]
    if not all(passes):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
