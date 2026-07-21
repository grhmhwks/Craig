"""Bounded checks for the type C Grothendieck conjecture hierarchy.

This is a curated port of the three source scripts:

* ``c-grothendieck.py``: basic counting version;
* ``c-grothendieck-strong.py``: no repeated adjacent Hecke letters and no
  consecutive entries in the same shifted set-valued tableau box;
* ``c-grothendieck-strongest.py``: peakset-preserving version.

The checks are finite evidence only.  They do not construct the conjectural
bijections and they do not prove the resulting GQ-positivity statement.
"""

from __future__ import annotations

import argparse
import copy
import time
from typing import Literal


Mode = Literal["basic", "strong", "strongest"]


def hecke(index: int, permutation: list[int]) -> list[int]:
    result = copy.copy(permutation)
    if index == 0 and result[0] > 0:
        result[0] = -result[0]
    if index > 0 and result[index - 1] < result[index]:
        result[index - 1], result[index] = result[index], result[index - 1]
    return result


def identity(largest: int) -> list[int]:
    return list(range(1, largest + 2))


def permute(word: list[int], largest: int) -> list[int]:
    result = identity(largest)
    for index in word:
        result = hecke(index, result)
    return result


def words(length: int, largest: int, *, no_equal_adjacent: bool) -> list[list[int]]:
    word_list = [[]]
    while len(word_list[0]) < length:
        next_words: list[list[int]] = []
        for word in word_list:
            for value in range(largest + 1):
                if not no_equal_adjacent or not word or word[-1] != value:
                    next_words.append(word + [value])
        word_list = next_words
    return word_list


def all_words(max_length: int, largest: int, *, no_equal_adjacent: bool) -> list[list[list[int]]]:
    return [words(length, largest, no_equal_adjacent=no_equal_adjacent) for length in range(1, max_length + 1)]


def create_word_perm_pairs(max_length: int, largest: int, *, no_equal_adjacent: bool) -> list[list]:
    pairs: list[list] = []
    for word_group in all_words(max_length, largest, no_equal_adjacent=no_equal_adjacent):
        for word in word_group:
            pairs.append([word, permute(word, largest)])
    pairs.sort(key=lambda item: str(item[1]))
    return pairs


def colreq(bottom: list[int], top: list[int]) -> bool:
    """Source row-adjacency condition for type C unimodal Hecke tableaux."""

    if len(bottom) == 0:
        return True
    if len(top) <= len(bottom):
        return False

    b_row = copy.copy(bottom)
    a_row = copy.copy(top)
    bindex = max(index for index, value in enumerate(b_row) if value == min(b_row))
    for index in range(0, bindex + 1):
        b_row[index] = -b_row[index]
    aindex = max(index for index, value in enumerate(a_row) if value == min(a_row))
    for index in range(0, aindex):
        a_row[index] = -a_row[index]

    if abs(b_row[-1]) >= abs(a_row[0]):
        return False
    if abs(b_row[0]) >= abs(a_row[0]):
        return False

    for index in range(len(b_row)):
        if a_row[index + 1] > b_row[index]:
            for j in range(index + 1, len(b_row)):
                if b_row[index] < b_row[j] < a_row[index + 1]:
                    return False
                if b_row[index] < -b_row[j] < a_row[index + 1]:
                    return False
                if b_row[j] == a_row[index + 1] or b_row[j] == -a_row[index + 1]:
                    return False
            for k in range(0, index + 1):
                if b_row[index] < a_row[k] < a_row[index + 1]:
                    return False
                if b_row[index] < -a_row[k] < a_row[index + 1]:
                    return False
                if a_row[k] == -a_row[index + 1] or a_row[k] == a_row[index + 1]:
                    return False
    return True


def hook(row: list[int]) -> bool:
    if not row:
        return False
    min_index = max(index for index, value in enumerate(row) if value == min(row))
    for index in range(0, min_index):
        if row[index] <= row[index + 1]:
            return False
    for index in range(min_index, len(row) - 1):
        if row[index] >= row[index + 1]:
            return False
    return True


def hecke_tabs_for_shape(words_for_size: list[list[int]], shape: list[int]) -> list[list[int]]:
    valid: list[list[int]] = []
    offsets = [sum(shape[:index]) for index in range(len(shape) + 1)]
    for word in words_for_size:
        good = True
        for row_index in range(len(shape)):
            bottom = word[offsets[row_index] : offsets[row_index + 1]]
            if not hook(bottom):
                good = False
                break
            if row_index < len(shape) - 1:
                top = word[offsets[row_index + 1] : offsets[row_index + 2]]
                if not hook(top) or not colreq(bottom, top):
                    good = False
                    break
        if good:
            valid.append(word)
    return valid


def children_basic(partition: list[int]) -> list[list[int]]:
    children: list[list[int]] = []
    for index in range(len(partition)):
        if index == 0 or partition[index] < partition[index - 1] - 1:
            child = copy.copy(partition)
            child[index] += 1
            children.append(child)
    if partition[-1] > 1:
        children.append(copy.copy(partition) + [1])
    for index in range(len(partition)):
        if index == len(partition) - 1 or partition[index] > partition[index + 1] + 1:
            children.append(copy.copy(partition))
    return children


def positive_parts(partition: list[int]) -> list[int]:
    return [abs(value) for value in partition]


def children_strong(partition: list[int]) -> list[list[int]]:
    children: list[list[int]] = []
    positive = positive_parts(partition)
    for index in range(len(partition)):
        if index == 0 or positive[index] < positive[index - 1] - 1:
            child = copy.copy(positive)
            child[index] = -child[index] - 1
            children.append(child)
    if positive[-1] > 1:
        children.append(copy.copy(positive) + [-1])
    for index in range(len(partition)):
        if (index == len(partition) - 1 or positive[index] > positive[index + 1] + 1) and partition[index] > 0:
            child = copy.copy(positive)
            child[index] = -child[index]
            children.append(child)
    return children


def create_shapes(length: int, *, strong: bool) -> list[list[list[int]]]:
    if strong:
        sizes = [[], [[-1]]]
        child_func = children_strong
    else:
        sizes = [[], [[1]]]
        child_func = children_basic
    for _ in range(2, length + 1):
        next_sizes: list[list[int]] = []
        for partition in sizes[-1]:
            next_sizes += child_func(partition)
        sizes.append(next_sizes)
    if strong:
        for group in sizes:
            for partition in group:
                for index in range(len(partition)):
                    partition[index] = abs(partition[index])
    return sizes


def distinct_with_multiplicity(values: list[list[int]]) -> list[list]:
    if not values:
        return []
    out = [[1, values[0]]]
    for value in values[1:]:
        spot = -1
        for index, item in enumerate(out):
            if item[1] == value:
                spot = index
                break
        if spot >= 0:
            out[spot][0] += 1
        else:
            out.append([1, value])
        out.sort(key=lambda item: item[0])
    return out


def count_for_perm(length_words: list[list[list[int]]], shape_counts: list[list]) -> list:
    total = 0
    representative: list[int] = []
    if length_words[-1]:
        representative = length_words[-1][0]
    else:
        for group in reversed(length_words):
            if group:
                representative = group[0]
                break
    for multiplicity, shape in shape_counts:
        size = sum(shape)
        reversed_shape = copy.copy(shape)
        reversed_shape.reverse()
        valid_tabs = hecke_tabs_for_shape(length_words[size], reversed_shape)
        total += len(valid_tabs) * multiplicity
    return [representative, total, len(length_words[-1])]


def run_basic_or_strong(mode: Literal["basic", "strong"], length: int, largest: int) -> dict[str, object]:
    strong = mode == "strong"
    shape_counts = distinct_with_multiplicity(copy.deepcopy(create_shapes(length, strong=strong)[length]))
    pairs = create_word_perm_pairs(length, largest, no_equal_adjacent=strong)
    grouped_results: list[list] = []

    index = 0
    while index < len(pairs):
        current_perm = pairs[index][1]
        length_words = [[] for _ in range(length + 1)]
        while index < len(pairs) and pairs[index][1] == current_perm:
            word = pairs[index][0]
            length_words[len(word)].append(word)
            index += 1
        grouped_results.append(count_for_perm(length_words, shape_counts))

    same = sum(1 for result in grouped_results if result[1] == result[2])
    different = len(grouped_results) - same
    return {
        "mode": mode,
        "length": length,
        "largest": largest,
        "permutations": len(grouped_results),
        "same": same,
        "different": different,
        "shape_count_terms": len(shape_counts),
        "sample_results": grouped_results[: min(8, len(grouped_results))],
    }


def word_list(max_length: int, largest: int) -> list[list[list]]:
    base = identity(largest)
    all_by_length = [[[base, []]]]
    while len(all_by_length[-1][0][1]) < max_length:
        next_group: list[list] = []
        for perm, word in all_by_length[-1]:
            for value in range(largest + 1):
                if not word or word[-1] != value:
                    next_group.append([hecke(value, perm), word + [value]])
        all_by_length.append(next_group)
    return all_by_length


def create_perm_dict(max_length: int, largest: int) -> dict[str, dict[str, list]]:
    pairs: list[list] = []
    for group in word_list(max_length, largest)[1:]:
        pairs += group
    pairs.sort(key=lambda item: str(item[0]))
    result: dict[str, dict[str, list]] = {}
    for perm, word in pairs:
        result.setdefault(str(perm), {"words": []})["words"].append(word)
    return result


def add_word_peaks(perm_data: dict[str, dict[str, list]]) -> dict[str, dict[str, list]]:
    for perm in perm_data:
        peaksets: list[list[int]] = []
        for word in perm_data[perm]["words"]:
            peaks = [len(word)]
            for index in range(1, len(word) - 1):
                if word[index - 1] < word[index] and word[index] > word[index + 1]:
                    peaks.append(index)
            peaksets.append(peaks)
        peaksets.sort(key=lambda item: str(item))
        perm_data[perm]["peaksets"] = peaksets
    return perm_data


def hecke_tab(word: list[int]) -> list[list[int]]:
    tableau: list[list[int]] = []
    remainder = copy.copy(word)
    while not hook(remainder):
        index = 1
        while index <= len(remainder) and not hook(remainder[index:]):
            index += 1
        if index > len(remainder) or max(remainder[:index]) >= max(remainder[index:]):
            return []
        tableau.append(remainder[index:])
        remainder = remainder[:index]
        if len(tableau) > 1 and not colreq(tableau[-1], tableau[-2]):
            return []
    tableau.append(remainder)
    if len(tableau) > 1 and not colreq(tableau[-1], tableau[-2]):
        return []
    return tableau


def add_hecke_tabs(perm_data: dict[str, dict[str, list]]) -> dict[str, dict[str, list]]:
    for perm in perm_data:
        tabs: list[list[list[int]]] = []
        for word in perm_data[perm]["words"]:
            tab = hecke_tab(word)
            if tab:
                tabs.append(tab)
        perm_data[perm]["tabs"] = tabs
    return perm_data


def standard_shifted_svts(max_length: int) -> list[list[list]]:
    tabs: list[list[list]] = [[ [[], [], [], []] ]]
    for entry in range(max_length):
        big_tabs: list[list] = []
        for tab, positions, peakset, shape in tabs[-1]:
            for row_index in range(len(tab)):
                if entry - 1 not in tab[row_index][-1] and (
                    row_index == len(tab) - 1 or len(tab[row_index]) > 1 + len(tab[row_index + 1])
                ):
                    t_cop = copy.deepcopy(tab)
                    p_cop = copy.copy(positions)
                    k_cop = copy.copy(peakset)
                    t_cop[row_index][-1] += [entry]
                    new_position = [row_index, len(t_cop[row_index]) - 1 + row_index]
                    p_cop += [new_position]
                    if len(positions) > 1 and positions[-2][1] < positions[-1][1] and positions[-1][0] < new_position[0]:
                        k_cop += [entry - 1]
                    big_tabs.append([t_cop, p_cop, k_cop, shape])

                if row_index == 0 or 1 + len(tab[row_index]) < len(tab[row_index - 1]):
                    t_cop = copy.deepcopy(tab)
                    p_cop = copy.copy(positions)
                    k_cop = copy.copy(peakset)
                    s_cop = copy.deepcopy(shape)
                    t_cop[row_index] += [[entry]]
                    new_position = [row_index, len(t_cop[row_index]) - 1 + row_index]
                    p_cop += [new_position]
                    if len(positions) > 1 and positions[-2][1] < positions[-1][1] and positions[-1][0] < new_position[0]:
                        k_cop += [entry - 1]
                    s_cop[row_index] += 1
                    big_tabs.append([t_cop, p_cop, k_cop, s_cop])

            if len(tab) == 0 or len(tab[-1]) > 1:
                t_cop = copy.deepcopy(tab)
                p_cop = copy.copy(positions)
                k_cop = copy.copy(peakset)
                s_cop = copy.deepcopy(shape)
                t_cop += [[[entry]]]
                new_position = [len(t_cop) - 1, len(t_cop) - 1]
                p_cop += [new_position]
                if len(positions) > 1 and positions[-2][1] < positions[-1][1] and positions[-1][0] < new_position[0]:
                    k_cop += [entry - 1]
                s_cop += [1]
                big_tabs.append([t_cop, p_cop, k_cop, s_cop])
        tabs.append(big_tabs)
    return tabs


def create_q_peak_dict(tabs: list[list[list]]) -> dict[str, dict[str, list]]:
    rows: list[list] = []
    for size, group in enumerate(tabs):
        for tab in group:
            rows.append([tab[3], [size] + tab[2]])
    rows.sort(key=lambda item: str(item[0]))
    result: dict[str, dict[str, list]] = {}
    for shape, peakset in rows:
        result.setdefault(str(shape), {"peaksets": []})["peaksets"].append(peakset)
    return result


def add_tableau_peaks(max_length: int, perm_data: dict[str, dict[str, list]]) -> dict[str, dict[str, list]]:
    qdict = create_q_peak_dict(standard_shifted_svts(max_length))
    for perm in perm_data:
        tabpeaks: list[list[int]] = []
        for tab in perm_data[perm]["tabs"]:
            shape = [len(row) for row in tab]
            tabpeaks += qdict[str(shape)]["peaksets"]
        tabpeaks.sort(key=lambda item: str(item))
        perm_data[perm]["tabpeaks"] = tabpeaks
    return perm_data


def run_strongest(length: int, largest: int) -> dict[str, object]:
    timings: list[float] = []
    start = time.time()
    data = create_perm_dict(length, largest)
    timings.append(time.time() - start)
    start = time.time()
    add_word_peaks(data)
    timings.append(time.time() - start)
    start = time.time()
    add_hecke_tabs(data)
    timings.append(time.time() - start)
    start = time.time()
    add_tableau_peaks(length, data)
    timings.append(time.time() - start)

    good = 0
    bad = 0
    bad_examples: list[str] = []
    for perm in data:
        if data[perm]["peaksets"] == data[perm]["tabpeaks"]:
            good += 1
        else:
            bad += 1
            if len(bad_examples) < 5:
                bad_examples.append(perm)
    return {
        "mode": "strongest",
        "length": length,
        "largest": largest,
        "permutations": len(data),
        "same": good,
        "different": bad,
        "bad_examples": bad_examples,
        "timings_seconds": [round(value, 4) for value in timings],
    }


def print_summary(summary: dict[str, object]) -> None:
    mode = str(summary["mode"])
    label = {
        "basic": "Basic type C Grothendieck count check",
        "strong": "Strong type C Grothendieck count check",
        "strongest": "Strongest type C Grothendieck peakset check",
    }[mode]
    print(label)
    print(f"  max word length: {summary['length']}")
    print(f"  largest generator index: {summary['largest']}")
    print(f"  grouped signed permutations: {summary['permutations']}")
    print(f"  matching groups: {summary['same']}")
    print(f"  mismatching groups: {summary['different']}")
    if "shape_count_terms" in summary:
        print(f"  shifted tableau shape-count terms: {summary['shape_count_terms']}")
        print(f"  sample [word, tableau_count, word_count] records: {summary['sample_results']}")
    if "bad_examples" in summary:
        print(f"  bad examples: {summary['bad_examples']}")
        print(f"  timings seconds: {summary['timings_seconds']}")
    print(f"  PASS: {summary['different'] == 0}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["basic", "strong", "strongest", "all"], default="all")
    parser.add_argument("--length", type=int, default=4)
    parser.add_argument("--largest", type=int, default=3)
    args = parser.parse_args()

    if args.length <= 0:
        raise SystemExit("length must be positive")
    if args.largest < 0:
        raise SystemExit("largest must be nonnegative")
    if args.length > 8 or args.largest > 4:
        print("warning: this direct enumerator can grow quickly; source defaults include length=8, largest=4")

    modes: list[Mode] = ["basic", "strong", "strongest"] if args.mode == "all" else [args.mode]  # type: ignore[list-item]
    summaries: list[dict[str, object]] = []
    for mode in modes:
        if mode in ("basic", "strong"):
            summaries.append(run_basic_or_strong(mode, args.length, args.largest))
        else:
            summaries.append(run_strongest(args.length, args.largest))
        print_summary(summaries[-1])

    if any(summary["different"] != 0 for summary in summaries):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
