"""Checks for the conjectural ``r = tau*s + 1`` skeleton-string formula.

This item-level checker covers the tau>1 rational case, which remains
conjectural.  It verifies finite instances of:

1. the special-skeleton quotient formula in a defect range;
2. the current East3/East5 partial lower-half string map.

Finite checks are evidence only, not proof.
"""

from __future__ import annotations

import argparse
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from math import comb
from typing import Iterable, Sequence


Word = tuple[int, ...]
PairTable = list[list[int]]
UNSUPPORTED_LEVEL_7 = "unsupported_level_7"
KNOWN_STATS: dict[Word, tuple[int, int, int]] = {}


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


def max_total_degree(s: int, tau: int) -> int:
    return tau * comb(s, 2)


def conjectural_defect_bound(s: int, tau: int) -> int:
    return (s - 2) * (tau + 1) - 4


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


def area(word: Sequence[int]) -> int:
    return sum(word)


def pair_dinv(left: int, right: int, tau: int) -> int:
    if left <= right:
        contribution = left + tau - right
    else:
        contribution = right + 1 + tau - left
    return contribution if contribution > 0 else 0


def build_pair_dinv_table(max_value: int, tau: int) -> PairTable:
    return [[pair_dinv(left, right, tau) for right in range(max_value + 1)] for left in range(max_value + 1)]


def dinv_delta_append_from_table(prefix: Sequence[int], value: int, pair_table: PairTable) -> int:
    total = 0
    for left in prefix:
        total += pair_table[left][value]
    return total


def dinv_delta_append_from_counts(counts: Sequence[int], value: int, pair_columns: PairTable) -> int:
    total = 0
    column = pair_columns[value]
    for left, count in enumerate(counts):
        if count:
            total += count * column[left]
    return total


def suffix_score_bounder(s: int, tau: int, pair_table: PairTable):
    """Return an exact maximum future ``area+dinv`` scorer for a prefix state."""

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


def dinv_delta_append(prefix: Sequence[int], value: int, tau: int) -> int:
    total = 0
    for left in prefix:
        if left <= value:
            total += max(0, left + tau - value)
        else:
            total += max(0, value + 1 + tau - left)
    return total


@lru_cache(maxsize=None)
def rational_dinv(word: Word, tau: int) -> int:
    values = tuple(word)
    total = 0
    for index, left in enumerate(values):
        for right in values[index + 1 :]:
            if left <= right:
                total += max(0, left + tau - right)
            else:
                total += max(0, right + 1 + tau - left)
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


def generate_words_with_stats(s: int, tau: int) -> Iterable[tuple[Word, int, int, int]]:
    """Generate normalized tau-affine words with incremental area/dinv."""

    if s <= 0:
        raise ValueError("s must be positive")
    if tau <= 0:
        raise ValueError("tau must be positive")
    m_total = max_total_degree(s, tau)
    pair_table = build_pair_dinv_table(tau * (s - 1), tau)
    prefix = [0]

    def rec(current_area: int, current_dinv: int) -> Iterable[tuple[Word, int, int, int]]:
        if len(prefix) == s:
            word = tuple(prefix)
            yield word, current_area, current_dinv, m_total - current_area - current_dinv
            return
        previous = prefix[-1]
        for value in range(previous + tau + 1):
            delta = dinv_delta_append_from_table(prefix, value, pair_table)
            prefix.append(value)
            yield from rec(current_area + value, current_dinv + delta)
            prefix.pop()

    yield from rec(0, 0)


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
def is_full_skeleton(word: Word, tau: int) -> bool:
    values = tuple(word)
    return is_normalized(values, tau) and is_full_skeleton_normalized(values, tau)


@lru_cache(maxsize=None)
def is_full_skeleton_normalized(values: Word, tau: int) -> bool:
    return find_extractable_normalized(values, tau, include_final=True) is None


@lru_cache(maxsize=None)
def excluded_full_skeleton(s: int, tau: int) -> Word:
    if s < 4:
        raise ValueError("excluded skeleton is only defined for s >= 4")
    return (0, 0, 1) + (0,) * (s - 4) + (tau,)


@lru_cache(maxsize=None)
def is_special_skeleton(word: Word, tau: int) -> bool:
    values = tuple(word)
    if not is_normalized(values, tau) or not is_full_skeleton_normalized(values, tau):
        return False
    return is_special_skeleton_normalized(values, tau)


@lru_cache(maxsize=None)
def is_special_skeleton_normalized(values: Word, tau: int) -> bool:
    return len(values) < 4 or values != excluded_full_skeleton(len(values), tau)


@lru_cache(maxsize=None)
def special_input(s: int, tau: int) -> Word:
    return (0,) * (s - 1) + (tau,)


@lru_cache(maxsize=None)
def rational_inject(word: Word, entry: int, tau: int) -> Word:
    values = tuple(word)
    if entry <= 0:
        raise ValueError(f"cannot inject nonpositive entry {entry}")
    out = rational_inject_normalized(values, entry, tau)
    if not is_normalized(out, tau):
        raise ValueError(f"injection produced non-normalized word {out}")
    return out


def rational_inject_normalized(values: Word, entry: int, tau: int) -> Word:
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


def load_records(s: int, tau: int, max_defect: int) -> tuple[dict[Word, tuple[int, int, int]], Counter[tuple[int, int]], int]:
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


def formula_coefficients(records: dict[Word, tuple[int, int, int]], s: int, tau: int, max_defect: int) -> Counter[tuple[int, int]]:
    coeffs: Counter[tuple[int, int]] = Counter()
    total_degree = max_total_degree(s, tau)
    for word, (word_area, word_dinv, word_defect) in records.items():
        if word_defect > max_defect or not is_full_skeleton_normalized(word, tau) or not is_special_skeleton_normalized(word, tau):
            continue
        if word_dinv >= word_area:
            for q_power in range(word_area, word_dinv + 1):
                coeffs[(q_power, total_degree - word_defect - q_power)] += 1
        else:
            for q_power in range(word_dinv + 1, word_area):
                coeffs[(q_power, total_degree - word_defect - q_power)] -= 1
    return coeffs


def check_formula(records: dict[Word, tuple[int, int, int]], direct: Counter[tuple[int, int]], s: int, tau: int, max_defect: int) -> tuple[bool, str]:
    formula = formula_coefficients(records, s, tau, max_defect)
    for key in sorted(set(direct) | set(formula)):
        if direct[key] != formula[key]:
            return False, f"formula mismatch at {key}: direct={direct[key]}, formula={formula[key]}"
    return True, "formula coefficients match"


def check_map(
    records: dict[Word, tuple[int, int, int]],
    s: int,
    tau: int,
    max_defect: int,
    *,
    report_level7: bool = False,
) -> tuple[Counter[str], Failure | None, list[Failure]]:
    global KNOWN_STATS
    KNOWN_STATS = records
    by_defect: dict[int, list[Word]] = defaultdict(list)
    for word, (_, _, word_defect) in records.items():
        if word_defect <= max_defect:
            by_defect[word_defect].append(word)
    counts: Counter[str] = Counter()
    failures: list[Failure] = []
    level7_records: dict[tuple[str, int, Word], Failure] = {}
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
                        if report_level7:
                            level7_records.setdefault(
                                ("up", defect, current),
                                Failure("level7_blocked_up", defect, current, result.reason),
                            )
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
                        if report_level7:
                            level7_records.setdefault(
                                ("down_inverse", defect, result.output),
                                Failure("level7_blocked_down_inverse", defect, result.output, down.reason),
                            )
                    else:
                        failures.append(Failure("down_inverse_failure", defect, result.output, down.reason or "unknown failure"))
                elif down.output != current:
                    failures.append(Failure("inverse_mismatch", defect, current, f"up={result.output}, down(up)={down.output}"))
                current = result.output
                previous_owner = occurrences.setdefault(current, start)
                if previous_owner != start:
                    failures.append(Failure("duplicate_coverage", defect, current, f"owners={previous_owner}, {start}"))

        for word in sorted(target, key=lambda item: (records[item][0], item)):
            if word in occurrences:
                continue
            current = word
            seen: set[Word] = set()
            while not (is_full_skeleton_normalized(current, tau) and is_special_skeleton_normalized(current, tau)):
                if current in seen:
                    failures.append(Failure("descent_cycle", defect, word, f"cycle at {current}"))
                    break
                seen.add(current)
                result = down_step(current, tau)
                counts["descent_attempts"] += 1
                if not result.success:
                    if result.reason == UNSUPPORTED_LEVEL_7:
                        counts["unsupported_level_7"] += 1
                        blocked_by_level7.add(word)
                        if report_level7:
                            level7_records.setdefault(
                                ("descent", defect, word),
                                Failure("level7_blocked_descent", defect, word, result.reason),
                            )
                    else:
                        failures.append(Failure("descent_failure", defect, word, result.reason or "unknown failure"))
                    break
                assert result.output is not None
                current = result.output
                if current not in target:
                    failures.append(Failure("descent_left_target", defect, word, f"down reached {current} outside target"))
                    break
            else:
                failures.append(Failure("coverage_missing_despite_descent", defect, word, f"descends to {current}"))

        missing = target - set(occurrences) - blocked_by_level7
        if missing:
            word = sorted(missing, key=lambda item: (records[item][0], item))[0]
            failures.append(Failure("coverage_missing", defect, word, "not covered"))

        counts["covered_words"] += len(occurrences)
        counts["level7_blocked_words"] += len(blocked_by_level7)

    if failures:
        first = sorted(failures, key=lambda item: (item.defect, area(item.source or ()), item.source or (), item.property))[0]
        return counts, first, sorted(level7_records.values(), key=lambda item: (item.defect, area(item.source or ()), item.source or (), item.property))
    return counts, None, sorted(level7_records.values(), key=lambda item: (item.defect, area(item.source or ()), item.source or (), item.property))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s", type=int, required=True, help="length s")
    parser.add_argument("--tau", type=int, required=True, help="tau in r=tau*s+1; intended tau>1")
    parser.add_argument(
        "--max-defect",
        default="conjectural",
        help="integer max defect, or 'conjectural' for (s-2)(tau+1)-4",
    )
    parser.add_argument("--formula-only", action="store_true", help="only check the quotient formula")
    parser.add_argument("--map-only", action="store_true", help="only check the lower-half map")
    parser.add_argument("--report-level7", action="store_true", help="print words blocked by unsupported level-7 moves")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.formula_only and args.map_only:
        raise SystemExit("choose at most one of --formula-only and --map-only")
    if args.tau <= 1:
        raise SystemExit("this checker is for the conjectural tau>1 case")
    max_defect = conjectural_defect_bound(args.s, args.tau) if args.max_defect == "conjectural" else int(args.max_defect)
    if max_defect < 0:
        print(f"empty defect range: max_defect={max_defect}")
        return 0

    start = time.perf_counter()
    records, direct, searched = load_records(args.s, args.tau, max_defect)
    load_elapsed = time.perf_counter() - start
    print("r = tau*s + 1 skeleton-string check")
    print(f"  s: {args.s}")
    print(f"  tau: {args.tau}")
    print(f"  max_defect: {max_defect}")
    print(f"  generated_words: {count_normalized_words(args.s, args.tau)}")
    print(f"  searched_leaf_words: {searched}")
    print(f"  retained_defect_range_words: {len(records)}")
    print(f"  generation_elapsed_seconds: {load_elapsed:.3f}")

    ok = True
    if not args.map_only:
        formula_start = time.perf_counter()
        formula_ok, formula_message = check_formula(records, direct, args.s, args.tau, max_defect)
        print(f"  formula_status: {'PASS' if formula_ok else 'FAIL'}")
        print(f"  formula_message: {formula_message}")
        print(f"  formula_elapsed_seconds: {time.perf_counter() - formula_start:.3f}")
        ok = ok and formula_ok

    if not args.formula_only:
        map_start = time.perf_counter()
        map_counts, failure, level7_records = check_map(
            records,
            args.s,
            args.tau,
            max_defect,
            report_level7=args.report_level7,
        )
        map_partial = failure is None and map_counts.get("unsupported_level_7", 0) > 0
        if failure is None and not map_partial:
            map_status = "PASS"
        elif map_partial:
            map_status = "PARTIAL"
        else:
            map_status = "FAIL"
        print(f"  map_status: {map_status}")
        print(f"  map_counts: {dict(sorted(map_counts.items()))}")
        if args.report_level7:
            print(f"  level7_records: {len(level7_records)}")
            for record in level7_records:
                print(
                    "  level7_record: "
                    f"property={record.property} defect={record.defect} "
                    f"area={area(record.source or ())} source={record.source} "
                    f"reason={record.reason}"
                )
        if failure is not None:
            print(f"  first_failed_property: {failure.property}")
            print(f"  first_failed_defect: {failure.defect}")
            print(f"  first_failed_source: {failure.source}")
            print(f"  first_failure_reason: {failure.reason}")
        print(f"  map_elapsed_seconds: {time.perf_counter() - map_start:.3f}")
        ok = ok and failure is None and not map_partial

    print(f"  total_elapsed_seconds: {time.perf_counter() - start:.3f}")
    print(f"  status: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
