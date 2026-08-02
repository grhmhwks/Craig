from __future__ import annotations

import json
from collections import Counter
from itertools import product
from pathlib import Path

import pytest

from craig.computation.registry import execute_operation
from craig.computation.service import ComputationService
from craig.computation.traces import (
    MAX_TRACE_BYTES,
    TRACE_EVENT_KINDS,
    algorithm_trace,
)


def _progress(fraction: float, label: str) -> None:
    assert 0 <= fraction <= 1
    assert label


def _event(index: int, kind: str = "local_move") -> dict[str, object]:
    return {
        "index": index,
        "kind": kind,
        "title": f"Step {index}",
        "description": "A deterministic mathematical transition.",
        "state": {"index": index},
        "visualizations": [],
    }


def test_general_trace_contract_covers_the_phase_seven_vocabulary() -> None:
    events = [_event(index, kind) for index, kind in enumerate(sorted(TRACE_EVENT_KINDS))]

    trace = algorithm_trace("contract_test", "Contract test", events)

    assert trace["schema_version"] == 1
    assert [event["index"] for event in trace["events"]] == list(range(len(events)))
    assert {event["kind"] for event in trace["events"]} == TRACE_EVENT_KINDS


@pytest.mark.parametrize(
    "events",
    [
        [],
        [{**_event(0), "code": "print('no')"}],
        [_event(1)],
        [_event(0, "unknown")],
        [{**_event(0), "state": []}],
        [
            {
                **_event(0),
                "visualizations": [
                    {"label": "Unsafe", "language": "html", "spec": {}}
                ],
            }
        ],
    ],
)
def test_trace_contract_rejects_unbounded_or_unknown_shapes(
    events: list[dict[str, object]],
) -> None:
    with pytest.raises(ValueError):
        algorithm_trace("contract_test", "Contract test", events)


def test_trace_contract_enforces_its_total_byte_limit() -> None:
    events = [_event(0)]
    events[0]["state"] = {"text": "x" * MAX_TRACE_BYTES}

    with pytest.raises(ValueError, match="state is too large"):
        algorithm_trace("contract_test", "Contract test", events)


def _assert_partition_shape(rows: list[list[int]]) -> None:
    assert rows
    assert all(rows[index] for index in range(len(rows)))
    assert all(len(left) >= len(right) for left, right in zip(rows, rows[1:]))


def _assert_ordinary_tableau(rows: list[list[int]]) -> None:
    _assert_partition_shape(rows)
    assert all(
        all(left <= right for left, right in zip(row, row[1:])) for row in rows
    )
    for row_index in range(len(rows) - 1):
        for column, lower in enumerate(rows[row_index + 1]):
            assert rows[row_index][column] < lower


def _assert_standard_tableau(rows: list[list[int]], size: int) -> None:
    _assert_partition_shape(rows)
    assert sorted(entry for row in rows for entry in row) == list(range(1, size + 1))
    assert all(
        all(left < right for left, right in zip(row, row[1:])) for row in rows
    )
    for row_index in range(len(rows) - 1):
        for column, lower in enumerate(rows[row_index + 1]):
            assert rows[row_index][column] < lower


def test_tableau_row_insertion_matches_a_known_bumping_example() -> None:
    result = execute_operation(
        "tableau_row_insertion",
        {"word": [3, 1, 2, 1]},
        _progress,
    )

    assert result["value"] == {
        "word": [3, 1, 2, 1],
        "shape": [2, 1, 1],
        "insertion_tableau": [[1, 1], [2], [3]],
        "recording_tableau": [[1, 3], [2], [4]],
    }
    kinds = [event["kind"] for event in result["trace"]["events"]]
    assert kinds[0] == "initialization"
    assert "insertion" in kinds
    assert "bumping" in kinds
    assert "recording" in kinds
    assert kinds[-1] == "completion"
    assert len(result["trace"]["events"][-1]["visualizations"]) == 2


def test_tableau_invariants_hold_for_every_small_word() -> None:
    for length in range(1, 6):
        for word_tuple in product(range(1, 4), repeat=length):
            word = list(word_tuple)
            result = execute_operation(
                "tableau_row_insertion",
                {"word": word},
                _progress,
            )
            value = result["value"]
            insertion = value["insertion_tableau"]
            recording = value["recording_tableau"]
            _assert_ordinary_tableau(insertion)
            _assert_standard_tableau(recording, length)
            assert [len(row) for row in insertion] == [len(row) for row in recording]
            assert Counter(entry for row in insertion for entry in row) == Counter(word)


def test_trace_producers_are_deterministic_and_end_in_the_exact_output() -> None:
    cases = [
        ("dyck_path_statistics", {"steps": "NNEENNEE"}),
        ("tableau_row_insertion", {"word": [3, 1, 4, 1, 5, 2]}),
        ("type_c_hecke_word", {"rank": 4, "word": [0, 1, 3, 2, 1]}),
    ]
    for operation, parameters in cases:
        first = execute_operation(operation, parameters, _progress)
        second = execute_operation(operation, parameters, _progress)
        assert first["trace"] == second["trace"]
        assert first["trace"]["events"][-1]["kind"] == "completion"

    dyck = execute_operation("dyck_path_statistics", {"steps": "NNEE"}, _progress)
    assert len(dyck["trace"]["events"]) == len("NNEE") + 2
    assert dyck["trace"]["events"][-1]["state"] == dyck["value"]
    progress_values = [
        event["visualizations"][0]["spec"]["progress"]
        for event in dyck["trace"]["events"]
    ]
    assert progress_values == [0, 1, 2, 3, 4, 4]

    hecke = execute_operation(
        "type_c_hecke_word",
        {"rank": 3, "word": [0, 1, 0, 2]},
        _progress,
    )
    local_moves = hecke["trace"]["events"][1:-1]
    assert len(local_moves) == 4
    assert all(event["kind"] == "local_move" for event in local_moves)
    assert all(
        event["visualizations"][0]["language"] == "skeleton"
        for event in local_moves
    )
    assert local_moves[-1]["state"]["permutation"] == hecke["value"][
        "final_permutation"
    ]


def test_maximum_trace_jobs_stay_below_worker_output_limit() -> None:
    cases = [
        ("dyck_path_statistics", {"steps": "N" * 80 + "E" * 80}),
        ("tableau_row_insertion", {"word": list(range(12, 0, -1))}),
        (
            "type_c_hecke_word",
            {"rank": 7, "word": [index % 7 for index in range(80)]},
        ),
    ]
    for operation, parameters in cases:
        result = execute_operation(operation, parameters, _progress)
        encoded = json.dumps(result, separators=(",", ":")).encode("utf-8")
        assert len(encoded) < 196_608


def test_isolated_service_carries_trace_and_reproducibility(tmp_path: Path) -> None:
    source = tmp_path / "content" / "dyck_symmetric_functions" / "explanation.tex"
    source.parent.mkdir(parents=True)
    source.write_text("ordinary insertion context\n", encoding="utf-8")
    service = ComputationService(tmp_path / "content")
    prepared = service.prepare("tableau_row_insertion", {"word": [2, 1, 3]})

    completed = list(service.stream(prepared))[-1]

    assert completed.type == "computation.completed"
    assert completed.data["trace"]["algorithm"] == "ordinary_rsk_row_insertion"
    assert completed.data["trace"]["events"][-1]["state"]["insertion_tableau"] == [
        [1, 3],
        [2],
    ]
    assert len(completed.data["reproducibility"]["result_sha256"]) == 64
