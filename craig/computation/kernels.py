"""Reviewed, deterministic mathematical kernels for the Phase 7 allowlist.

These functions are implemented outside the protected corpus. They perform no
filesystem, network, subprocess, import, or evaluation operations.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Sequence
from math import comb
from typing import Any

from .traces import algorithm_trace

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
    events: list[dict[str, Any]] = [
        {
            "index": 0,
            "kind": "initialization",
            "title": "Start at the origin",
            "description": "Initialize the path at (0, 0) before reading any steps.",
            "state": {
                "step_index": 0,
                "prefix": "",
                "east": 0,
                "north": 0,
                "partial_area_sequence": [],
            },
            "visualizations": [
                {
                    "label": "Path construction",
                    "language": "dyck-path",
                    "spec": {
                        "title": "Dyck path construction: 0 steps",
                        "kind": "ordinary",
                        "steps": steps,
                        "progress": 0,
                    },
                }
            ],
        }
    ]
    east = north = 0
    partial_area_sequence: list[int] = []
    for index, step in enumerate(steps):
        if step == "N":
            partial_area_sequence.append(north - east)
            north += 1
        else:
            east += 1
        events.append(
            {
                "index": len(events),
                "kind": "local_move",
                "title": f"Take {step} step {index + 1}",
                "description": (
                    f"Extend the path by one {'north' if step == 'N' else 'east'} step "
                    f"to ({east}, {north})."
                ),
                "state": {
                    "step_index": index + 1,
                    "step": step,
                    "prefix": steps[: index + 1],
                    "east": east,
                    "north": north,
                    "partial_area_sequence": list(partial_area_sequence),
                },
                "visualizations": [
                    {
                        "label": "Path construction",
                        "language": "dyck-path",
                        "spec": {
                            "title": f"Dyck path construction: {index + 1} steps",
                            "kind": "ordinary",
                            "steps": steps,
                            "progress": index + 1,
                        },
                    }
                ],
            }
        )
    events.append(
        {
            "index": len(events),
            "kind": "completion",
            "title": "Compute the path statistics",
            "description": "The completed path determines its area sequence, area, dinv, and deficit.",
            "state": statistics,
            "visualizations": [
                {
                    "label": "Completed path",
                    "language": "dyck-path",
                    "spec": {
                        "title": f"Completed Dyck path of semilength {statistics['semilength']}",
                        "kind": "ordinary",
                        "steps": steps,
                        "progress": len(steps),
                    },
                }
            ],
        }
    )
    return {
        "value": statistics,
        "trace": algorithm_trace(
            "dyck_path_construction",
            "Construct the Dyck path step by step",
            events,
        ),
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
    value_trace: list[dict[str, Any]] = [{"step": 0, "permutation": list(state)}]
    entries = [f"s{generator}" for generator in word] or ["identity"]

    def skeleton_spec(
        permutation: tuple[int, ...],
        generator: int | None,
        title: str,
    ) -> dict[str, Any]:
        vertices = [
            {
                "id": f"p{index}",
                "label": str(value),
                "x": 50 if rank == 1 else round(10 + (80 * index / (rank - 1)), 3),
                "y": 50,
            }
            for index, value in enumerate(permutation)
        ]
        edges = []
        if generator is not None and generator > 0:
            edges.append(
                {
                    "from": f"p{generator - 1}",
                    "to": f"p{generator}",
                    "label": f"s{generator}",
                }
            )
        return {
            "title": title,
            "vertices": vertices,
            "edges": edges,
            "directed": False,
        }

    events: list[dict[str, Any]] = [
        {
            "index": 0,
            "kind": "initialization",
            "title": "Start with the identity",
            "description": f"Initialize the rank-{rank} signed permutation.",
            "state": {
                "word_index": 0,
                "permutation": list(state),
                "applied_prefix": [],
            },
            "visualizations": [
                {
                    "label": "Signed permutation skeleton",
                    "language": "skeleton",
                    "spec": skeleton_spec(state, None, "Identity signed permutation"),
                },
                {
                    "label": "Generator word",
                    "language": "reading-word",
                    "spec": {
                        "title": f"Type C rank-{rank} 0-Hecke word",
                        "entries": entries,
                        "highlights": [],
                    },
                },
            ],
        }
    ]
    changed_indexes: list[int] = []
    total = max(1, len(word))
    progress_step = max(1, len(word) // 20)
    for index, generator in enumerate(word):
        next_state = _hecke_step(state, generator)
        changed = next_state != state
        if changed:
            changed_indexes.append(index)
        state = next_state
        value_trace.append(
            {
                "step": index + 1,
                "generator": generator,
                "changed": changed,
                "permutation": list(state),
            }
        )
        events.append(
            {
                "index": len(events),
                "kind": "local_move",
                "title": f"Apply generator s{generator}",
                "description": (
                    f"Generator s{generator} {'changes' if changed else 'fixes'} "
                    "the current signed permutation under the 0-Hecke action."
                ),
                "state": {
                    "word_index": index + 1,
                    "generator": generator,
                    "changed": changed,
                    "permutation": list(state),
                    "applied_prefix": word[: index + 1],
                },
                "visualizations": [
                    {
                        "label": "Signed permutation skeleton",
                        "language": "skeleton",
                        "spec": skeleton_spec(
                            state,
                            generator,
                            f"After generator s{generator} at step {index + 1}",
                        ),
                    },
                    {
                        "label": "Generator word",
                        "language": "reading-word",
                        "spec": {
                            "title": f"Generator {index + 1} of {len(word)}",
                            "entries": entries,
                            "highlights": [index],
                        },
                    },
                ],
            }
        )
        if (index + 1) % progress_step == 0 or index + 1 == len(word):
            progress(
                min(0.96, (index + 1) / total),
                f"Applied {index + 1} of {len(word)} generators",
            )
    if not word:
        progress(0.8, "Evaluated the empty word")
    events.append(
        {
            "index": len(events),
            "kind": "completion",
            "title": "Finish the 0-Hecke action",
            "description": "The displayed signed permutation is the value of the full generator word.",
            "state": {
                "word_index": len(word),
                "permutation": list(state),
                "changed_steps": [index + 1 for index in changed_indexes],
            },
            "visualizations": [
                {
                    "label": "Final signed permutation skeleton",
                    "language": "skeleton",
                    "spec": skeleton_spec(state, None, "Final signed permutation"),
                },
                {
                    "label": "Generator word",
                    "language": "reading-word",
                    "spec": {
                        "title": f"Completed type C rank-{rank} 0-Hecke word",
                        "entries": entries,
                        "highlights": changed_indexes,
                    },
                },
            ],
        }
    )
    return {
        "value": {
            "rank": rank,
            "word": word,
            "initial_permutation": list(range(1, rank + 1)),
            "final_permutation": list(state),
            "changed_steps": [index + 1 for index in changed_indexes],
            "trace": value_trace,
        },
        "trace": algorithm_trace(
            "type_c_hecke_action",
            "Apply a type C 0-Hecke word by local moves",
            events,
        ),
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


def _tableau_visualizations(
    insertion: Sequence[Sequence[int]],
    recording: Sequence[Sequence[int]],
    title: str,
) -> list[dict[str, Any]]:
    if not insertion:
        return []
    return [
        {
            "label": "Insertion tableau P",
            "language": "tableau",
            "spec": {
                "title": f"{title}: insertion tableau P",
                "rows": [list(row) for row in insertion],
            },
        },
        {
            "label": "Recording tableau Q",
            "language": "tableau",
            "spec": {
                "title": f"{title}: recording tableau Q",
                "rows": [list(row) for row in recording],
            },
        },
    ]


def tableau_row_insertion(parameters: dict[str, Any], progress: Progress) -> dict[str, Any]:
    """Trace bounded ordinary RSK row insertion and its recording tableau."""

    word = parameters["word"]
    insertion: list[list[int]] = []
    recording: list[list[int]] = []
    events: list[dict[str, Any]] = [
        {
            "index": 0,
            "kind": "initialization",
            "title": "Start with empty tableaux",
            "description": "Initialize the ordinary insertion and recording tableaux P and Q.",
            "state": {
                "word": word,
                "input_position": 0,
                "insertion_tableau": [],
                "recording_tableau": [],
            },
            "visualizations": [],
        }
    ]
    for input_index, letter in enumerate(word):
        active = letter
        row_index = 0
        events.append(
            {
                "index": len(events),
                "kind": "insertion",
                "title": f"Insert {letter}",
                "description": f"Begin row insertion for word position {input_index + 1}.",
                "state": {
                    "word": word,
                    "input_position": input_index + 1,
                    "active_value": active,
                    "target_row": row_index + 1,
                    "insertion_tableau": [list(row) for row in insertion],
                    "recording_tableau": [list(row) for row in recording],
                },
                "visualizations": _tableau_visualizations(
                    insertion, recording, f"Before inserting {letter}"
                ),
            }
        )
        while row_index < len(insertion):
            row = insertion[row_index]
            column = next(
                (index for index, value in enumerate(row) if value > active),
                None,
            )
            if column is None:
                break
            bumped = row[column]
            row[column] = active
            events.append(
                {
                    "index": len(events),
                    "kind": "bumping",
                    "title": f"Bump {bumped} from row {row_index + 1}",
                    "description": (
                        f"Replace the leftmost entry greater than {active}; "
                        f"continue with the bumped value {bumped}."
                    ),
                    "state": {
                        "word": word,
                        "input_position": input_index + 1,
                        "inserted_value": active,
                        "bumped_value": bumped,
                        "row": row_index + 1,
                        "column": column + 1,
                        "insertion_tableau": [list(item) for item in insertion],
                        "recording_tableau": [list(item) for item in recording],
                    },
                    "visualizations": _tableau_visualizations(
                        insertion,
                        recording,
                        f"After bumping {bumped} from row {row_index + 1}",
                    ),
                }
            )
            active = bumped
            row_index += 1

        if row_index == len(insertion):
            insertion.append([active])
            recording.append([input_index + 1])
            column_index = 0
        else:
            insertion[row_index].append(active)
            recording[row_index].append(input_index + 1)
            column_index = len(insertion[row_index]) - 1
        events.append(
            {
                "index": len(events),
                "kind": "recording",
                "title": f"Record position {input_index + 1}",
                "description": (
                    f"The insertion terminates in row {row_index + 1}, column "
                    f"{column_index + 1}; add {input_index + 1} to Q in the same box."
                ),
                "state": {
                    "word": word,
                    "input_position": input_index + 1,
                    "new_box": {"row": row_index + 1, "column": column_index + 1},
                    "insertion_tableau": [list(row) for row in insertion],
                    "recording_tableau": [list(row) for row in recording],
                },
                "visualizations": _tableau_visualizations(
                    insertion, recording, f"After inserting word position {input_index + 1}"
                ),
            }
        )
        progress(
            min(0.96, (input_index + 1) / len(word)),
            f"Inserted {input_index + 1} of {len(word)} letters",
        )

    final_state = {
        "word": word,
        "shape": [len(row) for row in insertion],
        "insertion_tableau": insertion,
        "recording_tableau": recording,
    }
    events.append(
        {
            "index": len(events),
            "kind": "completion",
            "title": "Complete the insertion correspondence",
            "description": "P and Q have the same shape, and Q records where each insertion terminated.",
            "state": final_state,
            "visualizations": _tableau_visualizations(
                insertion, recording, "Completed row insertion"
            ),
        }
    )
    return {
        "value": final_state,
        "trace": algorithm_trace(
            "ordinary_rsk_row_insertion",
            "Ordinary row insertion with recording tableau",
            events,
        ),
        "visualization": {
            "language": "tableau",
            "spec": {
                "title": "Final insertion tableau P",
                "rows": insertion,
            },
        },
        "summary": (
            f"Inserted {len(word)} letters by ordinary row insertion; "
            f"the common tableau shape is {[len(row) for row in insertion]}."
        ),
    }


KERNELS: dict[str, Callable[[dict[str, Any], Progress], dict[str, Any]]] = {
    "dyck_path_statistics": dyck_path_statistics,
    "enumerate_dyck_paths": enumerate_dyck_paths,
    "enumerate_rational_dyck_paths": enumerate_rational_dyck_paths,
    "type_c_hecke_word": type_c_hecke_word,
    "tableau_row_insertion": tableau_row_insertion,
}
