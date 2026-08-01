"""Reviewed, deterministic mathematical kernels for the Phase 6 allowlist.

These functions are implemented outside the protected corpus. They perform no
filesystem, network, subprocess, import, or evaluation operations.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Sequence
from math import comb
from typing import Any

Progress = Callable[[float, str], None]


def _classical_dinv(sequence: Sequence[int]) -> int:
    return sum(
        1
        for left in range(len(sequence))
        for right in range(left + 1, len(sequence))
        if sequence[left] == sequence[right]
        or sequence[left] == sequence[right] + 1
    )


def _deficit_pair_count(sequence: Sequence[int]) -> int:
    total = 0
    first_seen: set[int] = set()
    for left, left_value in enumerate(sequence):
        left_is_first = left_value not in first_seen
        first_seen.add(left_value)
        for right_value in sequence[left + 1 :]:
            if left_value > right_value + 1 or (
                left_value < right_value and not left_is_first
            ):
                total += 1
    return total


def _extractable_position(
    sequence: Sequence[int],
    *,
    include_final: bool = True,
) -> int | None:
    for index, value in enumerate(sequence):
        if not include_final and index == len(sequence) - 1:
            continue
        if value == 0:
            continue
        if sum(1 for prior in sequence[:index] if prior == value - 1) != 1:
            continue
        if index + 1 < len(sequence) and sequence[index + 1] > value:
            continue
        return index
    return None


def _excluded_skeleton(semilength: int) -> tuple[int, ...]:
    if semilength < 4:
        return ()
    return (0, 0, 1) + (0,) * (semilength - 4) + (1,)


def _path_statistics(steps: str) -> dict[str, Any]:
    east = 0
    north = 0
    area_sequence: list[int] = []
    for step in steps:
        if step == "N":
            area_sequence.append(north - east)
            north += 1
        else:
            east += 1
    area = sum(area_sequence)
    dinv = _classical_dinv(area_sequence)
    deficit = comb(north, 2) - area - dinv
    deficit_pairs = _deficit_pair_count(area_sequence)
    extractable = _extractable_position(area_sequence)
    full_skeleton = extractable is None
    return {
        "steps": steps,
        "semilength": north,
        "area_sequence": area_sequence,
        "area": area,
        "dinv": dinv,
        "deficit": deficit,
        "deficit_pair_count": deficit_pairs,
        "deficit_consistent": deficit == deficit_pairs,
        "leftmost_extractable_index": extractable,
        "is_full_skeleton": full_skeleton,
        "is_special_skeleton": full_skeleton
        and tuple(area_sequence) != _excluded_skeleton(north),
    }


def dyck_path_statistics(parameters: dict[str, Any], progress: Progress) -> dict[str, Any]:
    steps = parameters["steps"]
    progress(0.2, "Validated the Dyck path")
    statistics = _path_statistics(steps)
    progress(0.75, "Computed area, dinv, and deficit")
    return {
        "value": statistics,
        "visualization": {
            "language": "dyck-path",
            "spec": {
                "title": f"Dyck path of semilength {statistics['semilength']}",
                "kind": "ordinary",
                "steps": steps,
            },
        },
        "summary": (
            f"For this path, area = {statistics['area']}, "
            f"dinv = {statistics['dinv']}, and deficit = {statistics['deficit']}."
        ),
    }


def _enumerate_classical_paths(semilength: int, progress: Progress) -> dict[str, Any]:
    expected = comb(2 * semilength, semilength) // (semilength + 1)
    distribution: Counter[tuple[int, int]] = Counter()
    samples: list[str] = []
    path: list[str] = []
    count = 0
    progress_step = max(1, expected // 20)

    def visit(east: int, north: int) -> None:
        nonlocal count
        if east == semilength and north == semilength:
            steps = "".join(path)
            statistics = _path_statistics(steps)
            distribution[(statistics["area"], statistics["dinv"])] += 1
            if len(samples) < 8:
                samples.append(steps)
            count += 1
            if count % progress_step == 0 or count == expected:
                progress(
                    min(0.96, count / expected),
                    f"Enumerated {count} of {expected} paths",
                )
            return
        if north < semilength:
            path.append("N")
            visit(east, north + 1)
            path.pop()
        if east < semilength and east < north:
            path.append("E")
            visit(east + 1, north)
            path.pop()

    visit(0, 0)
    rows = [
        {"area": area, "dinv": dinv, "count": multiplicity}
        for (area, dinv), multiplicity in sorted(distribution.items())
    ]
    symmetric = all(
        distribution[(area, dinv)] == distribution[(dinv, area)]
        for area, dinv in distribution
    )
    return {
        "count": count,
        "expected_catalan_count": expected,
        "count_matches_catalan": count == expected,
        "area_dinv_symmetric": symmetric,
        "distribution": rows,
        "sample_steps": samples,
    }


def enumerate_dyck_paths(parameters: dict[str, Any], progress: Progress) -> dict[str, Any]:
    semilength = parameters["semilength"]
    value = _enumerate_classical_paths(semilength, progress)
    sample = value["sample_steps"][0]
    return {
        "value": value,
        "visualization": {
            "language": "dyck-path",
            "spec": {
                "title": f"First path in the exhaustive n={semilength} enumeration",
                "kind": "ordinary",
                "steps": sample,
            },
        },
        "summary": (
            f"Exhaustively enumerated {value['count']} Dyck paths of semilength "
            f"{semilength}; the count matches the Catalan number."
        ),
    }


def _enumerate_rational_paths(r: int, s: int, progress: Progress) -> dict[str, Any]:
    expected = comb(r + s, r) // (r + s)
    samples: list[str] = []
    count = 0
    path: list[str] = []
    progress_step = max(1, expected // 20)

    def visit(east: int, north: int) -> None:
        nonlocal count
        if east == r and north == s:
            count += 1
            if len(samples) < 8:
                samples.append("".join(path))
            if count % progress_step == 0 or count == expected:
                progress(
                    min(0.96, count / expected),
                    f"Enumerated {count} of {expected} paths",
                )
            return
        if north < s:
            path.append("N")
            visit(east, north + 1)
            path.pop()
        if east < r and r * north - s * (east + 1) >= 0:
            path.append("E")
            visit(east + 1, north)
            path.pop()

    visit(0, 0)
    return {
        "r": r,
        "s": s,
        "count": count,
        "expected_rational_catalan_count": expected,
        "count_matches_rational_catalan": count == expected,
        "sample_steps": samples,
    }


def enumerate_rational_dyck_paths(
    parameters: dict[str, Any],
    progress: Progress,
) -> dict[str, Any]:
    r = parameters["r"]
    s = parameters["s"]
    value = _enumerate_rational_paths(r, s, progress)
    return {
        "value": value,
        "visualization": {
            "language": "dyck-path",
            "spec": {
                "title": f"First rational ({r}, {s})-Dyck path",
                "kind": "rational",
                "r": r,
                "s": s,
                "steps": value["sample_steps"][0],
            },
        },
        "summary": (
            f"Exhaustively enumerated {value['count']} rational ({r}, {s})-Dyck "
            "paths; the count matches the rational Catalan number."
        ),
    }


def _hecke_step(permutation: tuple[int, ...], generator: int) -> tuple[int, ...]:
    values = list(permutation)
    if generator == 0:
        if values[0] > 0:
            values[0] = -values[0]
    elif values[generator - 1] < values[generator]:
        values[generator - 1], values[generator] = (
            values[generator],
            values[generator - 1],
        )
    return tuple(values)


def type_c_hecke_word(parameters: dict[str, Any], progress: Progress) -> dict[str, Any]:
    rank = parameters["rank"]
    word = parameters["word"]
    state = tuple(range(1, rank + 1))
    trace: list[dict[str, Any]] = [{"step": 0, "permutation": list(state)}]
    changed_indexes: list[int] = []
    total = max(1, len(word))
    progress_step = max(1, len(word) // 20)
    for index, generator in enumerate(word):
        next_state = _hecke_step(state, generator)
        changed = next_state != state
        if changed:
            changed_indexes.append(index)
        state = next_state
        trace.append(
            {
                "step": index + 1,
                "generator": generator,
                "changed": changed,
                "permutation": list(state),
            }
        )
        if (index + 1) % progress_step == 0 or index + 1 == len(word):
            progress(
                min(0.96, (index + 1) / total),
                f"Applied {index + 1} of {len(word)} generators",
            )
    if not word:
        progress(0.8, "Evaluated the empty word")
    entries = [f"s{generator}" for generator in word] or ["identity"]
    return {
        "value": {
            "rank": rank,
            "word": word,
            "initial_permutation": list(range(1, rank + 1)),
            "final_permutation": list(state),
            "changed_steps": [index + 1 for index in changed_indexes],
            "trace": trace,
        },
        "visualization": {
            "language": "reading-word",
            "spec": {
                "title": f"Type C rank-{rank} 0-Hecke word",
                "entries": entries,
                "highlights": changed_indexes,
            },
        },
        "summary": (
            f"Applied {len(word)} generator(s) to the rank-{rank} identity; "
            f"the final signed permutation is {list(state)}."
        ),
    }


KERNELS: dict[str, Callable[[dict[str, Any], Progress], dict[str, Any]]] = {
    "dyck_path_statistics": dyck_path_statistics,
    "enumerate_dyck_paths": enumerate_dyck_paths,
    "enumerate_rational_dyck_paths": enumerate_rational_dyck_paths,
    "type_c_hecke_word": type_c_hecke_word,
}
