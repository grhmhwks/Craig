#!/usr/bin/env python3
"""Finite checks for Dyck skeleton string decompositions.

This file is meant to accompany ``explanation.tex`` for the item on Dyck
skeleton string decompositions.  It is deliberately self-contained and keeps
separate the different kinds of evidence discussed in the note:

* classical sanity checks for the proved special-skeleton formula;
* ``r = tau*s + 1`` coefficient checks at the UPPER cutoff;
* ``r = tau*s + 1`` lower-half map checks at the LOWER cutoff, using the
  currently implemented East3/East5 map and stopping before East7;
* full-rational checks of the intrinsic label-1-zero lower cutoff and the
  naive rational cyclic map (NRCM).

Finite checks are evidence only.  In particular, a lower-half decomposition
checks a proposed root formula on the lower half; it does not prove q,t
symmetry unless symmetry is independently known or the full coefficient
identity is checked directly.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from math import comb, gcd
from typing import Iterable, Sequence

Word = tuple[int, ...]
PairTable = list[list[int]]
UNSUPPORTED_LEVEL_7 = "unsupported_level_7"
KNOWN_STATS: dict[Word, tuple[int, int, int]] = {}


# ---------------------------------------------------------------------------
# Normalized tau-Dyck words and r = tau*s + 1 statistics
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class LocalResult:
    success: bool
    output: Word | None
    case: str
    reason: str | None = None


@dataclass(frozen=True)
class StepResult:
    success: bool
    output: Word | None
    direction: str
    branch: str
    level: int | None
    reason: str | None = None
    window: Word | None = None
    local_case: str | None = None


@dataclass(frozen=True)
class Failure:
    property: str
    defect: int
    source: Word | None
    reason: str


def area(word: Sequence[int]) -> int:
    return sum(word)


def max_total_degree(s: int, tau: int) -> int:
    return tau * comb(s, 2)


def upper_cutoff_r1mod(s: int, tau: int) -> int:
    """Conjectural special-skeleton formula cutoff for r=tau*s+1."""

    return (s - 2) * (tau + 1) - 4


def lower_cutoff_r1mod(s: int, tau: int) -> int:
    """Lower decomposition cutoff for r=tau*s+1."""

    return (s - 2) * tau - 1


def pair_dinv(left: int, right: int, tau: int) -> int:
    if left <= right:
        contribution = left + tau - right
    else:
        contribution = right + 1 + tau - left
    return contribution if contribution > 0 else 0


def build_pair_dinv_table(max_value: int, tau: int) -> PairTable:
    return [[pair_dinv(left, right, tau) for right in range(max_value + 1)] for left in range(max_value + 1)]


def dinv_delta_append_from_table(prefix: Sequence[int], value: int, pair_table: PairTable) -> int:
    return sum(pair_table[left][value] for left in prefix)


def dinv_delta_append_from_counts(counts: Sequence[int], value: int, pair_columns: PairTable) -> int:
    total = 0
    column = pair_columns[value]
    for left, count in enumerate(counts):
        if count:
            total += count * column[left]
    return total


@lru_cache(maxsize=None)
def rational_dinv(word: Word, tau: int) -> int:
    values = tuple(word)
    total = 0
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            total += pair_dinv(left, right, tau)
    return total


@lru_cache(maxsize=None)
def is_normalized(word: Word, tau: int) -> bool:
    values = tuple(word)
    return (
        bool(values)
        and values[0] == 0
        and all(isinstance(value, int) and value >= 0 for value in values)
        and all(values[index + 1] <= values[index] + tau for index in range(len(values) - 1))
    )


def suffix_score_bounder(s: int, tau: int, pair_table: PairTable):
    """Return an exact future upper bound for area+dinv from a prefix state."""

    max_value = tau * (s - 1)
    pair_columns = [[pair_table[left][right] for left in range(max_value + 1)] for right in range(max_value + 1)]

    @lru_cache(maxsize=None)
    def bound(remaining: int, previous: int, counts: tuple[int, ...]) -> int:
        if remaining == 0:
            return 0
        best = -1
        limit = min(max_value, previous + tau)
        for value in range(limit + 1):
            delta = value + dinv_delta_append_from_counts(counts, value, pair_columns)
            next_counts = list(counts)
            next_counts[value] += 1
            candidate = delta + bound(remaining - 1, value, tuple(next_counts))
            if candidate > best:
                best = candidate
        return best

    return bound


def count_normalized_words(s: int, tau: int) -> int:
    counts = [1]
    for _ in range(1, s):
        next_counts = [0] * (len(counts) + tau)
        for previous, count in enumerate(counts):
            if count:
                for value in range(previous + tau + 1):
                    next_counts[value] += count
        counts = next_counts
    return sum(counts)


def load_tau_records(s: int, tau: int, max_defect: int) -> tuple[dict[Word, tuple[int, int, int]], Counter[tuple[int, int]], int]:
    """Enumerate normalized tau-Dyck words in the retained deficit range.

    The recursion prunes prefixes that cannot reach the requested deficit
    range.  It returns a dictionary ``word -> (area,dinv,defect)``, the direct
    coefficient dictionary, and the number of retained leaf words searched.
    """

    if s <= 0:
        raise ValueError("s must be positive")
    if tau <= 0:
        raise ValueError("tau must be positive")
    if max_defect < 0:
        return {}, Counter(), 0

    records: dict[Word, tuple[int, int, int]] = {}
    direct_coeffs: Counter[tuple[int, int]] = Counter()
    searched = 0
    total_degree = max_total_degree(s, tau)
    min_score = total_degree - max_defect
    pair_table = build_pair_dinv_table(tau * (s - 1), tau)
    suffix_bound = suffix_score_bounder(s, tau, pair_table)
    prefix = [0]
    counts = [0] * (tau * (s - 1) + 1)
    counts[0] = 1

    def rec(current_area: int, current_dinv: int) -> None:
        nonlocal searched
        remaining = s - len(prefix)
        if remaining and current_area + current_dinv + suffix_bound(remaining, prefix[-1], tuple(counts)) < min_score:
            return
        if len(prefix) == s:
            searched += 1
            word_defect = total_degree - current_area - current_dinv
            if word_defect <= max_defect:
                word = tuple(prefix)
                records[word] = (current_area, current_dinv, word_defect)
                direct_coeffs[(current_area, current_dinv)] += 1
            return
        previous = prefix[-1]
        for value in range(previous + tau + 1):
            delta = dinv_delta_append_from_table(prefix, value, pair_table)
            prefix.append(value)
            counts[value] += 1
            rec(current_area + value, current_dinv + delta)
            counts[value] -= 1
            prefix.pop()

    rec(0, 0)
    return records, direct_coeffs, searched


@lru_cache(maxsize=None)
def remove_at(word: Word, position: int) -> Word:
    values = tuple(word)
    return values[:position] + values[position + 1 :]


@lru_cache(maxsize=None)
def find_extractable(word: Word, tau: int, *, include_final: bool = True) -> int | None:
    values = tuple(word)
    if not is_normalized(values, tau):
        raise ValueError(f"not normalized: {values}")
    return find_extractable_normalized(values, tau, include_final=include_final)


def find_extractable_normalized(values: Word, tau: int, *, include_final: bool = True) -> int | None:
    max_value = tau * (len(values) - 1)
    prior_counts = [0] * (max_value + 1)
    for index, value in enumerate(values):
        if value == 0:
            prior_counts[0] += 1
            continue
        if not include_final and index == len(values) - 1:
            prior_counts[value] += 1
            continue
        lower = max(0, value - tau)
        prior_count = 0
        for prior in range(lower, value):
            prior_count += prior_counts[prior]
        if prior_count != 1:
            prior_counts[value] += 1
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + tau:
            prior_counts[value] += 1
            continue
        return index
    return None


@lru_cache(maxsize=None)
def is_full_skeleton_normalized(values: Word, tau: int) -> bool:
    return find_extractable_normalized(tuple(values), tau, include_final=True) is None


@lru_cache(maxsize=None)
def excluded_full_skeleton(s: int, tau: int) -> Word:
    if s < 4:
        raise ValueError("excluded skeleton is only defined for s >= 4")
    return (0, 0, 1) + (0,) * (s - 4) + (tau,)


@lru_cache(maxsize=None)
def is_special_skeleton_normalized(values: Word, tau: int) -> bool:
    values = tuple(values)
    if not is_normalized(values, tau) or not is_full_skeleton_normalized(values, tau):
        return False
    return len(values) < 4 or values != excluded_full_skeleton(len(values), tau)


@lru_cache(maxsize=None)
def special_input(s: int, tau: int) -> Word:
    return (0,) * (s - 1) + (tau,)


def label1_zero_r1mod(word: Word) -> bool:
    """For r=tau*s+1, label 1 is position 1, so this means x_1=0."""

    return len(word) > 1 and word[1] == 0


@lru_cache(maxsize=None)
def rational_inject_normalized(values: Word, entry: int, tau: int) -> Word:
    if entry <= 0:
        raise ValueError(f"cannot inject nonpositive entry {entry}")
    lower = max(0, entry - tau)
    anchor = next((index for index, value in enumerate(values) if lower <= value <= entry - 1), None)
    if anchor is None:
        raise ValueError(f"no injection anchor for {entry} in {values}")
    return values[: anchor + 1] + (entry,) + values[anchor + 1 :]


@lru_cache(maxsize=None)
def inject_right_to_left(base: Word, entries: Word, tau: int) -> Word:
    out = tuple(base)
    for entry in reversed(tuple(entries)):
        out = rational_inject_normalized(out, entry, tau)
    return out


def bk2(a: int, b: int, tau: int) -> tuple[int, int]:
    return (b, a) if a > b + tau else (a, b)


@lru_cache(maxsize=None)
def east3(window: Word, tau: int) -> LocalResult:
    values = tuple(window)
    if len(values) != 3:
        raise ValueError("East3 needs a 3-window")
    _, c, d = values
    if c <= d + tau:
        return LocalResult(True, values, "east3_identity")
    return LocalResult(False, None, "east3_fail", "c >> d")


@lru_cache(maxsize=None)
def east5(window: Word, tau: int) -> LocalResult:
    values = tuple(window)
    if len(values) != 5:
        raise ValueError("East5 needs a 5-window")
    a, b, c, d, e = values
    if east3((b, c, d), tau).success:
        return LocalResult(False, None, "east5_outside_domain", "East3 would pass")
    if b <= d + tau:
        if b <= e + tau:
            return LocalResult(True, (a, d, c, b, e), "east5_case2b")
        return LocalResult(False, None, "east5_case2b_fail", "b >> e")
    b_prime, c_prime = bk2(b, c, tau)
    if c_prime <= e + tau:
        return LocalResult(True, (a, d, b_prime, c_prime, e), "east5_case2a")
    return LocalResult(False, None, "east5_case2a_fail", "c' >> e")


def reverse_result(result: LocalResult) -> LocalResult:
    output = None if result.output is None else tuple(reversed(result.output))
    return LocalResult(
        result.success,
        output,
        result.case.replace("east", "west", 1),
        None if result.reason is None else result.reason.replace("East", "West"),
    )


@lru_cache(maxsize=None)
def west3(window: Word, tau: int) -> LocalResult:
    return reverse_result(east3(tuple(reversed(tuple(window))), tau))


@lru_cache(maxsize=None)
def west5(window: Word, tau: int) -> LocalResult:
    return reverse_result(east5(tuple(reversed(tuple(window))), tau))


def checked_step(
    direction: str,
    source: Word,
    output: Word,
    tau: int,
    *,
    branch: str,
    level: int,
    window: Word | None = None,
    local_case: str | None = None,
) -> StepResult:
    if len(source) != len(output):
        return StepResult(False, None, direction, "failed", None, f"{direction} changed length")
    source_stats = KNOWN_STATS.get(source)
    if source_stats is None:
        source_area = area(source)
        source_dinv = rational_dinv(source, tau)
        source_defect = max_total_degree(len(source), tau) - source_area - source_dinv
    else:
        source_area, source_dinv, source_defect = source_stats
    output_stats = KNOWN_STATS.get(output)
    if output_stats is None:
        if not is_normalized(output, tau):
            return StepResult(False, None, direction, "failed", None, f"{direction} produced non-normalized {output}")
        output_area = area(output)
        output_dinv = rational_dinv(output, tau)
        output_defect = max_total_degree(len(output), tau) - output_area - output_dinv
    else:
        output_area, output_dinv, output_defect = output_stats
    if source_defect != output_defect:
        return StepResult(False, None, direction, "failed", None, f"{direction} changed defect: {source} -> {output}")
    if direction == "up" and (output_area != source_area + 1 or output_dinv != source_dinv - 1):
        return StepResult(False, None, direction, "failed", None, f"up changed wrong statistics: {source} -> {output}")
    if direction == "down" and (output_area != source_area - 1 or output_dinv != source_dinv + 1):
        return StepResult(False, None, direction, "failed", None, f"down changed wrong statistics: {source} -> {output}")
    return StepResult(True, output, direction, branch, level, None, window, local_case)


@lru_cache(maxsize=None)
def up_step(word: Word, tau: int) -> StepResult:
    values = tuple(word)
    s = len(values)
    if not is_normalized(values, tau):
        return StepResult(False, None, "up", "failed", None, f"not normalized: {values}")
    try:
        if s >= 4 and values == special_input(s, tau):
            return checked_step("up", values, excluded_full_skeleton(s, tau), tau, branch="special", level=3)
        if is_full_skeleton_normalized(values, tau):
            result = rational_inject_normalized(values[:-1], values[-1] + 1, tau)
            return checked_step("up", values, result, tau, branch="full_skeleton", level=3)
        j1 = find_extractable(values, tau)
        if j1 is None:
            return StepResult(False, None, "up", "failed", None, f"no first extractable in {values}")
        e1 = values[j1]
        c1 = remove_at(values, j1)
        sigma1 = c1 + (e1 - 1,)
        attempt3 = east3(sigma1[-3:], tau)
        if attempt3.success:
            if j1 >= s - 2:
                return StepResult(False, None, "up", "failed", None, f"East3 position bound failed: j1={j1}")
            assert attempt3.output is not None
            result = inject_right_to_left(sigma1[:-2], (attempt3.output[-2] + 1, attempt3.output[-1] + 1), tau)
            return checked_step("up", values, result, tau, branch="local", level=3, window=sigma1[-3:], local_case=attempt3.case)
        j2 = find_extractable(c1, tau)
        if j2 is None:
            return StepResult(False, None, "up", "failed", None, f"no second extractable in {c1}")
        e2 = c1[j2]
        c2 = remove_at(c1, j2)
        sigma2 = c2 + (e1 - 1, e2 - 1)
        attempt5 = east5(sigma2[-5:], tau)
        if attempt5.success:
            if j1 >= s - 3:
                return StepResult(False, None, "up", "failed", None, f"East5 position bound failed: j1={j1}")
            if j2 > len(c1) - 3:
                return StepResult(False, None, "up", "failed", None, f"East5 position bound failed: j2={j2}")
            assert attempt5.output is not None
            base = sigma2[:-5] + attempt5.output[:2]
            result = inject_right_to_left(base, tuple(value + 1 for value in attempt5.output[2:]), tau)
            return checked_step("up", values, result, tau, branch="local", level=5, window=sigma2[-5:], local_case=attempt5.case)
        return StepResult(False, None, "up", "failed", None, UNSUPPORTED_LEVEL_7)
    except (IndexError, ValueError) as exc:
        return StepResult(False, None, "up", "failed", None, str(exc))


@lru_cache(maxsize=None)
def down_step(word: Word, tau: int) -> StepResult:
    values = tuple(word)
    s = len(values)
    if not is_normalized(values, tau):
        return StepResult(False, None, "down", "failed", None, f"not normalized: {values}")
    if is_special_skeleton_normalized(values, tau) and is_full_skeleton_normalized(values, tau):
        return StepResult(False, None, "down", "failed", None, "down undefined on special skeleton")
    try:
        if s >= 4 and values == excluded_full_skeleton(s, tau):
            return checked_step("down", values, special_input(s, tau), tau, branch="excluded_full_skeleton", level=3)
        j1 = find_extractable(values, tau)
        if j1 is None:
            return StepResult(False, None, "down", "failed", None, f"no first extractable in {values}")
        f1 = values[j1]
        d1 = remove_at(values, j1)
        candidate = d1 + (f1 - 1,)
        if is_full_skeleton_normalized(candidate, tau):
            return checked_step("down", values, candidate, tau, branch="to_full_skeleton", level=3)
        j2 = find_extractable(d1, tau)
        if j2 is None:
            return StepResult(False, None, "down", "failed", None, f"no second extractable in {d1}")
        f2 = d1[j2]
        d2 = remove_at(d1, j2)
        tau1 = d2 + (f1 - 1, f2 - 1)
        attempt3 = west3(tau1[-3:], tau)
        if attempt3.success:
            if j1 >= s - 1:
                return StepResult(False, None, "down", "failed", None, f"West3 position bound failed: j1={j1}")
            if j2 >= len(d1) - 1:
                return StepResult(False, None, "down", "failed", None, f"West3 position bound failed: j2={j2}")
            assert attempt3.output is not None
            result = rational_inject_normalized(tau1[:-1], attempt3.output[-1] + 1, tau)
            return checked_step("down", values, result, tau, branch="local", level=3, window=tau1[-3:], local_case=attempt3.case)
        j3 = find_extractable(d2, tau)
        if j3 is None:
            return StepResult(False, None, "down", "failed", None, f"no third extractable in {d2}")
        f3 = d2[j3]
        d3 = remove_at(d2, j3)
        tau2 = d3 + (f1 - 1, f2 - 1, f3 - 1)
        attempt5 = west5(tau2[-5:], tau)
        if attempt5.success:
            if j1 >= s - 2:
                return StepResult(False, None, "down", "failed", None, f"West5 position bound failed: j1={j1}")
            if j2 > len(d1) - 2:
                return StepResult(False, None, "down", "failed", None, f"West5 position bound failed: j2={j2}")
            if j3 > len(d2) - 2:
                return StepResult(False, None, "down", "failed", None, f"West5 position bound failed: j3={j3}")
            assert attempt5.output is not None
            base = tau2[:-5] + attempt5.output[:3]
            result = inject_right_to_left(base, tuple(value + 1 for value in attempt5.output[3:]), tau)
            return checked_step("down", values, result, tau, branch="local", level=5, window=tau2[-5:], local_case=attempt5.case)
        return StepResult(False, None, "down", "failed", None, UNSUPPORTED_LEVEL_7)
    except (IndexError, ValueError) as exc:
        return StepResult(False, None, "down", "failed", None, str(exc))


def interval_coefficients_from_roots(
    roots: Iterable[tuple[Word, tuple[int, int, int]]],
    total_degree: int,
    max_defect: int,
) -> Counter[tuple[int, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    for _word, (word_area, word_dinv, word_defect) in roots:
        if word_defect > max_defect:
            continue
        if word_dinv >= word_area:
            for q_power in range(word_area, word_dinv + 1):
                coeffs[(q_power, total_degree - word_defect - q_power)] += 1
        else:
            # Expansion of the same quotient when the root lies above middle.
            for q_power in range(word_dinv + 1, word_area):
                coeffs[(q_power, total_degree - word_defect - q_power)] -= 1
    return coeffs


def formula_coefficients(records: dict[Word, tuple[int, int, int]], s: int, tau: int, max_defect: int) -> Counter[tuple[int, int]]:
    roots = (
        (word, stats)
        for word, stats in records.items()
        if stats[2] <= max_defect and is_full_skeleton_normalized(word, tau) and is_special_skeleton_normalized(word, tau)
    )
    return interval_coefficients_from_roots(roots, max_total_degree(s, tau), max_defect)


def check_formula(records: dict[Word, tuple[int, int, int]], direct: Counter[tuple[int, int]], s: int, tau: int, max_defect: int) -> tuple[bool, str]:
    formula = formula_coefficients(records, s, tau, max_defect)
    for key in sorted(set(direct) | set(formula)):
        if direct[key] != formula[key]:
            return False, f"mismatch at {key}: direct={direct[key]}, formula={formula[key]}"
    return True, "coefficient dictionaries match"


def check_lower_map(
    records: dict[Word, tuple[int, int, int]],
    s: int,
    tau: int,
    max_defect: int,
) -> tuple[Counter[str], Failure | None]:
    """Check lower-half coverage using the East3/East5 up/down map."""

    global KNOWN_STATS
    KNOWN_STATS = records
    by_defect: dict[int, list[Word]] = defaultdict(list)
    for word, (_, _, word_defect) in records.items():
        if word_defect <= max_defect:
            by_defect[word_defect].append(word)

    counts: Counter[str] = Counter()
    failures: list[Failure] = []
    total_degree = max_total_degree(s, tau)

    for defect in range(max_defect + 1):
        ell = (total_degree - defect) // 2
        target = {word for word in by_defect.get(defect, ()) if records[word][0] <= ell}
        starts = sorted(
            (word for word in target if is_full_skeleton_normalized(word, tau) and is_special_skeleton_normalized(word, tau)),
            key=lambda word: (records[word][0], word),
        )
        counts["target_words"] += len(target)
        counts["special_starts"] += len(starts)
        occurrences: dict[Word, Word] = {}
        blocked_by_level7: set[Word] = set()

        for start in starts:
            current = start
            occurrences[current] = start
            while records[current][0] < ell:
                result = up_step(current, tau)
                counts["up_attempts"] += 1
                if not result.success:
                    if result.reason == UNSUPPORTED_LEVEL_7:
                        counts["unsupported_level_7"] += 1
                        blocked_by_level7.add(current)
                        break
                    failures.append(Failure("up_step_failure", defect, current, result.reason or "unknown failure"))
                    break
                assert result.output is not None
                counts[f"up_level_{result.level}"] += 1
                if result.output not in target:
                    failures.append(Failure("up_left_target", defect, current, f"output {result.output} not in target"))
                down = down_step(result.output, tau)
                counts["down_inverse_attempts"] += 1
                if not down.success:
                    if down.reason == UNSUPPORTED_LEVEL_7:
                        counts["unsupported_level_7"] += 1
                    else:
                        failures.append(Failure("down_inverse_failure", defect, result.output, down.reason or "unknown failure"))
                elif down.output != current:
                    failures.append(Failure("inverse_mismatch", defect, current, f"up={result.output}, down(up)={down.output}"))
                current = result.output
                previous_owner = occurrences.setdefault(current, start)
                if previous_owner != start:
                    failures.append(Failure("duplicate_coverage", defect, current, f"owners={previous_owner}, {start}"))

        missing = target - set(occurrences) - blocked_by_level7
        if missing:
            word = sorted(missing, key=lambda item: (records[item][0], item))[0]
            failures.append(Failure("coverage_missing", defect, word, "not covered by any string"))

        counts["covered_words"] += len(occurrences)
        counts["level7_blocked_words"] += len(blocked_by_level7)

    if failures:
        first = sorted(failures, key=lambda item: (item.defect, area(item.source or ()), item.source or (), item.property))[0]
        return counts, first
    if counts.get("unsupported_level_7", 0):
        return counts, Failure("unsupported_level_7", -1, None, "map reached unsupported East7 branch")
    return counts, None


def subset_records(records: dict[Word, tuple[int, int, int]], max_defect: int) -> tuple[dict[Word, tuple[int, int, int]], Counter[tuple[int, int]]]:
    sub: dict[Word, tuple[int, int, int]] = {}
    direct: Counter[tuple[int, int]] = Counter()
    for word, stats in records.items():
        a, dnv, defect = stats
        if defect <= max_defect:
            sub[word] = stats
            direct[(a, dnv)] += 1
    return sub, direct


# ---------------------------------------------------------------------------
# Full-rational position-coordinate model and NRCM
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RationalStats:
    area: int
    dinv: int
    defect: int


def rational_H_L(r: int, s: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if s <= 0 or r <= 0:
        raise ValueError("r and s must be positive")
    if gcd(r, s) != 1:
        raise ValueError("r and s must be coprime")
    H = tuple((r * i) // s for i in range(s))
    L = tuple((r * i) % s for i in range(s))
    return H, L


def is_valid_rational_path(Q: Word, r: int, s: int) -> bool:
    H, _L = rational_H_L(r, s)
    if len(Q) != s or Q[0] != 0:
        return False
    if any(Q[i] < 0 or Q[i] > H[i] for i in range(s)):
        return False
    heights = [H[i] - Q[i] for i in range(s)]
    return all(heights[i] <= heights[i + 1] for i in range(s - 1))


def generate_rational_paths(r: int, s: int) -> list[Word]:
    H, _L = rational_H_L(r, s)
    Q = [0]
    out: list[Word] = []

    def rec(i: int, previous_height: int) -> None:
        if i == s:
            out.append(tuple(Q))
            return
        for q_value in range(H[i] + 1):
            height = H[i] - q_value
            if height >= previous_height:
                Q.append(q_value)
                rec(i + 1, height)
                Q.pop()

    rec(1, 0)
    return out


def rational_defect_diagnostic(Q: Word, r: int, s: int) -> int:
    """Diagnostic deficit statistic used by the NRCM checks.

    This follows the item-level pair-summand definition.  The v_ij term is not
    clamped; only the adjusted u_ij term is clamped at zero.
    """

    H, L = rational_H_L(r, s)
    delta = tuple(H[i + 1] - H[i] for i in range(s - 1))
    total = 0
    for i in range(1, s):
        for j in range(i + 1, s):
            qi, qj = Q[i], Q[j]
            u = abs(qi - qj)
            if qi != qj and ((qi > qj) != (L[i] > L[j])):
                u -= 1
            u = max(u, 0)
            if qi > qj:
                v = delta[i] - (Q[i + 1] - Q[i])
            elif qj > qi:
                v = delta[i - 1] - (Q[i] - Q[i - 1])
            else:
                v = 0
            total += min(u, v)
    return total


def rational_stats(Q: Word, r: int, s: int) -> RationalStats:
    H, _L = rational_H_L(r, s)
    M = sum(H)
    a = area(Q)
    defect = rational_defect_diagnostic(Q, r, s)
    return RationalStats(a, M - a - defect, defect)


def label1_index(r: int, s: int) -> int:
    _H, L = rational_H_L(r, s)
    return L.index(1)


def label1_zero(Q: Word, r: int, s: int) -> bool:
    return Q[label1_index(r, s)] == 0


def intrinsic_lower_cutoff(paths: Sequence[Word], r: int, s: int) -> int:
    """Largest D such that every label-1-zero path of defect <=D is lower-half."""

    bad_defects: list[int] = []
    root_defects: list[int] = []
    for Q in paths:
        if not label1_zero(Q, r, s):
            continue
        st = rational_stats(Q, r, s)
        root_defects.append(st.defect)
        if st.area > st.dinv:
            bad_defects.append(st.defect)
    if bad_defects:
        return min(bad_defects) - 1
    return max(root_defects) if root_defects else -1


def rational_direct_coefficients(paths: Sequence[Word], r: int, s: int, max_defect: int) -> Counter[tuple[int, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    for Q in paths:
        st = rational_stats(Q, r, s)
        if st.defect <= max_defect:
            coeffs[(st.area, st.dinv)] += 1
    return coeffs


def rational_root_interval_coefficients(paths: Sequence[Word], r: int, s: int, max_defect: int) -> Counter[tuple[int, int]]:
    H, _L = rational_H_L(r, s)
    total_degree = sum(H)
    roots = ((Q, (st.area, st.dinv, st.defect)) for Q in paths if label1_zero(Q, r, s) for st in [rational_stats(Q, r, s)])
    return interval_coefficients_from_roots(roots, total_degree, max_defect)


def nrcm_candidate(Q: Word, r: int, s: int, k: int) -> Word:
    _H, L = rational_H_L(r, s)
    ordered = sorted(range(k, s), key=lambda idx: L[idx])
    out = list(Q)
    if not ordered:
        return tuple(out)
    out[ordered[0]] = Q[ordered[-1]] + 1
    for pos in range(len(ordered) - 1):
        out[ordered[pos + 1]] = Q[ordered[pos]]
    return tuple(out)


def strict_nrcm(Q: Word, r: int, s: int) -> Word | None:
    H, _L = rational_H_L(r, s)
    for k in range(1, s):
        candidate = nrcm_candidate(Q, r, s, k)
        capacity_ok = all(0 <= candidate[i] <= H[i] for i in range(s))
        if capacity_ok:
            return candidate if is_valid_rational_path(candidate, r, s) else None
    return None


def check_nrcm_properties(paths: Sequence[Word], r: int, s: int, max_defect: int) -> tuple[Counter[str], Failure | None]:
    path_set = set(paths)
    counts: Counter[str] = Counter()
    failures: list[Failure] = []
    images: dict[Word, Word] = {}

    for Q in paths:
        st = rational_stats(Q, r, s)
        if st.defect > max_defect:
            continue
        image = strict_nrcm(Q, r, s)
        counts["sources_tested"] += 1
        if image is None:
            counts["undefined"] += 1
            continue
        counts["defined"] += 1
        if image not in path_set:
            failures.append(Failure("nrcm_image_not_path", st.defect, Q, f"image={image}"))
            continue
        imst = rational_stats(image, r, s)
        if imst.area != st.area + 1:
            failures.append(Failure("nrcm_area", st.defect, Q, f"area {st.area}->{imst.area}"))
        if imst.defect != st.defect:
            failures.append(Failure("nrcm_defect", st.defect, Q, f"defect {st.defect}->{imst.defect}"))
        previous = images.setdefault(image, Q)
        if previous != Q:
            failures.append(Failure("nrcm_not_injective", st.defect, Q, f"image={image}, previous={previous}"))

    if failures:
        first = sorted(failures, key=lambda item: (item.defect, item.source or (), item.property))[0]
        return counts, first
    return counts, None


def check_nrcm_coverage(paths: Sequence[Word], r: int, s: int, max_defect: int) -> tuple[Counter[str], Failure | None]:
    """Check whether NRCM strings from label-1-zero roots cover the lower half."""

    path_set = set(paths)
    stats = {Q: rational_stats(Q, r, s) for Q in paths}
    by_defect: dict[int, list[Word]] = defaultdict(list)
    for Q, st in stats.items():
        if st.defect <= max_defect:
            by_defect[st.defect].append(Q)

    H, _L = rational_H_L(r, s)
    total_degree = sum(H)
    counts: Counter[str] = Counter()
    failures: list[Failure] = []

    for defect in range(max_defect + 1):
        ell = (total_degree - defect) // 2
        target = {Q for Q in by_defect.get(defect, ()) if stats[Q].area <= ell}
        starts = sorted((Q for Q in target if label1_zero(Q, r, s)), key=lambda Q: (stats[Q].area, Q))
        counts["target_words"] += len(target)
        counts["starts"] += len(starts)
        occurrences: dict[Word, Word] = {}
        blocked: set[Word] = set()

        for start in starts:
            current = start
            occurrences[current] = start
            while stats[current].area < ell:
                image = strict_nrcm(current, r, s)
                counts["nrcm_attempts"] += 1
                if image is None:
                    counts["undefined_before_middle"] += 1
                    blocked.add(current)
                    break
                if image not in path_set:
                    failures.append(Failure("nrcm_left_path_set", defect, current, f"image={image}"))
                    break
                imst = stats[image]
                if imst.defect != defect:
                    failures.append(Failure("nrcm_changed_defect", defect, current, f"image={image}, image_defect={imst.defect}"))
                    break
                if imst.area > ell:
                    failures.append(Failure("nrcm_left_lower_half", defect, current, f"image={image}"))
                    break
                current = image
                previous = occurrences.setdefault(current, start)
                if previous != start:
                    failures.append(Failure("duplicate_coverage", defect, current, f"owners={previous}, {start}"))
                    break

        missing = target - set(occurrences) - blocked
        if missing:
            word = sorted(missing, key=lambda Q: (stats[Q].area, Q))[0]
            failures.append(Failure("coverage_missing", defect, word, "not covered by NRCM strings"))

        counts["covered_words"] += len(occurrences)
        counts["blocked_words"] += len(blocked)

    if failures:
        first = sorted(failures, key=lambda item: (item.defect, item.source or (), item.property))[0]
        return counts, first
    if counts.get("undefined_before_middle", 0):
        return counts, Failure("nrcm_undefined_before_middle", -1, None, "NRCM undefined before the middle")
    return counts, None


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------


def status_text(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


def format_counter(counter: Counter[str]) -> str:
    if not counter:
        return "{}"
    return "{" + ", ".join(f"{key}: {counter[key]}" for key in sorted(counter)) + "}"


def run_classical(max_n: int) -> bool:
    print("\nCLASSICAL SPECIAL-SKELETON FORMULA CHECKS")
    print("  These are finite sanity checks only; the theorem is proved in the paper.")
    all_ok = True
    for n in range(4, max_n + 1):
        max_defect = 2 * n - 8
        records, direct, searched = load_tau_records(n, 1, max_defect)
        ok, msg = check_formula(records, direct, n, 1, max_defect)
        all_ok = all_ok and ok
        print(
            f"  n={n:2d} upper_defect={max_defect:2d} "
            f"retained={len(records):5d} searched={searched:5d} formula_status={status_text(ok)} ({msg})"
        )
    return all_ok


def run_r1mod_case(s: int, tau: int, *, run_map: bool = True) -> bool:
    upper = upper_cutoff_r1mod(s, tau)
    lower = lower_cutoff_r1mod(s, tau)
    print(f"\nR1MOD CASE tau={tau}, s={s}, r={tau*s+1}")
    print(f"  upper_cutoff={(upper)}; lower_cutoff={lower}")
    if upper < 0:
        print("  empty upper defect range; skipping")
        return True

    start = time.perf_counter()
    records_upper, direct_upper, searched = load_tau_records(s, tau, upper)
    formula_ok, formula_msg = check_formula(records_upper, direct_upper, s, tau, upper)
    total_degree = max_total_degree(s, tau)
    special_roots_upper = [
        (word, stats)
        for word, stats in records_upper.items()
        if stats[2] <= upper and is_full_skeleton_normalized(word, tau) and is_special_skeleton_normalized(word, tau)
    ]
    negative_roots = [word for word, (a, dnv, _d) in special_roots_upper if a > dnv]
    print(
        f"  upper formula: retained={len(records_upper)} searched={searched} "
        f"generated={count_normalized_words(s,tau)} status={status_text(formula_ok)}"
    )
    print(f"    message: {formula_msg}")
    print(f"    special_roots={len(special_roots_upper)} negative_interval_roots={len(negative_roots)} total_degree={total_degree}")

    lower_ok = True
    if lower >= 0:
        records_lower, direct_lower = subset_records(records_upper, lower)
        if not records_lower or any(stats[2] > lower for stats in records_lower.values()):
            records_lower, direct_lower, _ = load_tau_records(s, tau, lower)
        special_lower = {
            word
            for word, stats in records_lower.items()
            if stats[2] <= lower and is_full_skeleton_normalized(word, tau) and is_special_skeleton_normalized(word, tau)
        }
        label_zero_lower = {word for word, stats in records_lower.items() if stats[2] <= lower and label1_zero_r1mod(word)}
        roots_equal = special_lower == label_zero_lower
        roots_below = all(records_lower[word][0] <= records_lower[word][1] for word in label_zero_lower)
        label_root_coeffs = interval_coefficients_from_roots(
            ((word, records_lower[word]) for word in label_zero_lower),
            total_degree,
            lower,
        )
        root_formula_ok = label_root_coeffs == direct_lower
        lower_ok = roots_equal and roots_below and root_formula_ok
        print(
            f"  lower roots: special={len(special_lower)} label1_zero={len(label_zero_lower)} "
            f"root_sets_equal={status_text(roots_equal)} roots_below_middle={status_text(roots_below)}"
        )
        print(f"  lower label1-zero interval formula: status={status_text(root_formula_ok)}")

        if run_map:
            if s < 5:
                print("  lower map: skipped for s<5 (small cases are formula-only in the item runner)")
            else:
                map_counts, map_failure = check_lower_map(records_lower, s, tau, lower)
                map_ok = map_failure is None
                lower_ok = lower_ok and map_ok
                print(f"  lower East3/East5 map: status={status_text(map_ok)} counts={format_counter(map_counts)}")
                if map_failure is not None:
                    print(
                        f"    first_map_issue: property={map_failure.property} defect={map_failure.defect} "
                        f"source={map_failure.source} reason={map_failure.reason}"
                    )
    print(f"  elapsed_seconds={time.perf_counter()-start:.3f}")
    return formula_ok and lower_ok


def run_r1mod_grid(taus: Sequence[int], max_s_by_tau: dict[int, int], *, run_map: bool = True) -> bool:
    print("\nR = TAU*S + 1 CHECKS")
    all_ok = True
    for tau in taus:
        max_s = max_s_by_tau[tau]
        for s in range(4, max_s + 1):
            all_ok = run_r1mod_case(s, tau, run_map=run_map) and all_ok
    return all_ok


def run_general_rational_case(r: int, s: int, *, nrcm_property_defects: int | None = None) -> bool:
    print(f"\nGENERAL RATIONAL CASE r={r}, s={s}")
    start = time.perf_counter()
    paths = generate_rational_paths(r, s)
    H, L = rational_H_L(r, s)
    lower = intrinsic_lower_cutoff(paths, r, s)
    direct = rational_direct_coefficients(paths, r, s, lower)
    root_formula = rational_root_interval_coefficients(paths, r, s, lower)
    formula_ok = direct == root_formula
    root_count = sum(1 for Q in paths if label1_zero(Q, r, s))
    bad_roots_after = sorted(
        (rational_stats(Q, r, s).defect, Q)
        for Q in paths
        if label1_zero(Q, r, s) and rational_stats(Q, r, s).area > rational_stats(Q, r, s).dinv
    )
    first_bad = bad_roots_after[0] if bad_roots_after else None
    print(f"  H={H}")
    print(f"  L={L}; label1_index={label1_index(r,s)}")
    print(f"  paths={len(paths)} label1_zero_roots={root_count} intrinsic_lower_cutoff={lower}")
    print(f"  label1-zero interval formula through lower cutoff: status={status_text(formula_ok)}")
    if first_bad is not None:
        print(f"  first label1-zero root above middle: defect={first_bad[0]} path={first_bad[1]}")

    prop_D = lower if nrcm_property_defects is None else min(lower, nrcm_property_defects)
    prop_counts, prop_failure = check_nrcm_properties(paths, r, s, prop_D)
    prop_ok = prop_failure is None
    print(f"  NRCM property check through defect {prop_D}: status={status_text(prop_ok)} counts={format_counter(prop_counts)}")
    if prop_failure is not None:
        print(
            f"    first_property_issue: property={prop_failure.property} defect={prop_failure.defect} "
            f"source={prop_failure.source} reason={prop_failure.reason}"
        )

    # Search for the largest initial range in which NRCM itself covers the lower half.
    nrcm_full = -1
    first_cov_issue: Failure | None = None
    for D in range(max(0, lower) + 1):
        _counts, issue = check_nrcm_coverage(paths, r, s, D)
        if issue is None:
            nrcm_full = D
        else:
            first_cov_issue = issue
            break
    print(f"  NRCM full lower-half coverage verified through defect: {nrcm_full}")
    if first_cov_issue is not None:
        print(
            f"    first_coverage_issue_after_that: property={first_cov_issue.property} "
            f"defect={first_cov_issue.defect} source={first_cov_issue.source} reason={first_cov_issue.reason}"
        )
    print(f"  elapsed_seconds={time.perf_counter()-start:.3f}")
    return formula_ok and prop_ok


def run_general_rational_grid(pairs: Sequence[tuple[int, int]]) -> bool:
    print("\nGENERAL RATIONAL / NRCM CHECKS")
    all_ok = True
    for r, s in pairs:
        all_ok = run_general_rational_case(r, s) and all_ok
    return all_ok


def quick_preset() -> tuple[int, dict[int, int], list[int], list[tuple[int, int]]]:
    # Classical up to n=9; r1mod grid chosen to keep the default run short.
    max_n = 9
    taus = [2, 3, 4]
    max_s_by_tau = {2: 8, 3: 7, 4: 6}
    rational_pairs = [(5, 3), (7, 4), (8, 5), (10, 7), (11, 7)]
    return max_n, max_s_by_tau, taus, rational_pairs


def medium_preset() -> tuple[int, dict[int, int], list[int], list[tuple[int, int]]]:
    max_n = 10
    taus = [2, 3, 4]
    max_s_by_tau = {2: 10, 3: 9, 4: 8}
    rational_pairs = [(5, 3), (7, 4), (8, 5), (10, 7), (11, 7), (13, 5), (17, 7)]
    return max_n, max_s_by_tau, taus, rational_pairs


def official_r1mod_preset() -> tuple[dict[int, int], list[int]]:
    # Same grid as the item-level official runner, but this file uses the LOWER
    # cutoff for map checks and the UPPER cutoff only for formula checks.
    max_s_by_tau = {2: 14, 3: 12, 4: 10, 5: 9}
    taus = [2, 3, 4, 5]
    return max_s_by_tau, taus


def parse_pair(text: str) -> tuple[int, int]:
    if "/" in text:
        left, right = text.split("/", 1)
    elif "," in text:
        left, right = text.split(",", 1)
    else:
        raise argparse.ArgumentTypeError("pairs must be written as r/s or r,s")
    r, s = int(left), int(right)
    if gcd(r, s) != 1:
        raise argparse.ArgumentTypeError(f"{r}/{s} is not coprime")
    return r, s


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["all", "classical", "r1mod", "general"], default="all")
    parser.add_argument("--preset", choices=["quick", "medium", "official-r1mod"], default="quick")
    parser.add_argument("--classical-max-n", type=int, default=None)
    parser.add_argument("--tau", type=int, action="append", help="tau value for r1mod checks; may be repeated")
    parser.add_argument("--s", type=int, action="append", help="specific s value for r1mod checks; may be repeated")
    parser.add_argument("--pair", type=parse_pair, action="append", help="general rational pair r/s or r,s; may be repeated")
    parser.add_argument("--no-map", action="store_true", help="skip East3/East5 lower map checks for r1mod cases")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.preset == "quick":
        max_n, max_s_by_tau, taus, rational_pairs = quick_preset()
    elif args.preset == "medium":
        max_n, max_s_by_tau, taus, rational_pairs = medium_preset()
    else:
        max_n, _, _, rational_pairs = quick_preset()
        max_s_by_tau, taus = official_r1mod_preset()

    if args.classical_max_n is not None:
        max_n = args.classical_max_n
    if args.tau:
        taus = sorted(set(args.tau))
        max_s_by_tau = {tau: max(args.s) if args.s else max_s_by_tau.get(tau, 7) for tau in taus}
    if args.s and args.tau:
        # When explicit s and tau values are supplied, run the Cartesian product.
        max_s_by_tau = {tau: max(args.s) for tau in taus}
    if args.pair:
        rational_pairs = args.pair

    overall_ok = True
    started = time.perf_counter()

    if args.mode in {"all", "classical"}:
        overall_ok = run_classical(max_n) and overall_ok

    if args.mode in {"all", "r1mod"}:
        if args.s and args.tau:
            print("\nR = TAU*S + 1 CHECKS")
            for tau in taus:
                for s in sorted(set(args.s)):
                    overall_ok = run_r1mod_case(s, tau, run_map=not args.no_map) and overall_ok
        else:
            overall_ok = run_r1mod_grid(taus, max_s_by_tau, run_map=not args.no_map) and overall_ok

    if args.mode in {"all", "general"}:
        overall_ok = run_general_rational_grid(rational_pairs) and overall_ok

    print(f"\nOVERALL_STATUS={status_text(overall_ok)} elapsed_seconds={time.perf_counter()-started:.3f}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
