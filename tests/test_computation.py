from __future__ import annotations

import hashlib
import json
import os
from dataclasses import replace
from math import gcd
from pathlib import Path
from typing import Any

import anyio
import httpx
import pytest

pytest.importorskip("fastapi")
pytest.importorskip("httpx")

from fastapi import FastAPI

from craig.api import create_app
from craig.computation.errors import (
    ComputationLimitExceeded,
    ComputationOperationNotFound,
    InvalidComputationRequest,
)
from craig.computation.isolation import stream_isolated_worker
from craig.computation.registry import execute_operation, validate_parameters
from craig.computation.service import ComputationService, _claim_boundary
from craig.retrieval import RetrievalConfig


def _progress(fraction: float, label: str) -> None:
    assert 0 <= fraction <= 1
    assert label


def _request(
    app: FastAPI,
    method: str,
    url: str,
    *,
    json_body: dict[str, Any] | None = None,
) -> httpx.Response:
    async def send() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://testserver",
        ) as client:
            kwargs = {"json": json_body} if json_body is not None else {}
            return await client.request(method, url, **kwargs)

    return anyio.run(send)


def _sse_payloads(response: httpx.Response) -> list[dict[str, Any]]:
    return [
        json.loads(line.removeprefix("data: "))
        for line in response.text.splitlines()
        if line.startswith("data: ")
    ]


def test_registry_exposes_only_the_reviewed_allowlist(tmp_path: Path) -> None:
    service = ComputationService(tmp_path / "content")
    catalog = service.catalog()

    assert catalog["execution_policy"] == "isolated_allowlist"
    assert catalog["max_concurrent_workers"] == 2
    assert {operation["id"] for operation in catalog["operations"]} == {
        "dyck_path_statistics",
        "enumerate_dyck_paths",
        "enumerate_rational_dyck_paths",
        "type_c_hecke_word",
    }
    assert {
        operation["classification"] for operation in catalog["operations"]
    } == {"example", "finite_check"}
    assert all(operation["limits"]["memory_bytes"] > 0 for operation in catalog["operations"])
    assert all(
        not operation["source_basis"]["path"].startswith("content/")
        for operation in catalog["operations"]
    )


def test_each_evidence_classification_has_an_explicit_claim_boundary() -> None:
    boundaries = {
        classification: _claim_boundary(classification)
        for classification in (
            "example",
            "experiment",
            "finite_check",
            "computer_assisted_proof",
        )
    }

    assert "bounded exact example" in boundaries["example"]
    assert "not an exhaustive check or a proof" in boundaries["experiment"]
    assert "not a proof of an unbounded claim" in boundaries["finite_check"]
    assert "separately reviewed proof obligations" in boundaries[
        "computer_assisted_proof"
    ]


@pytest.mark.parametrize(
    ("operation", "parameters", "message"),
    [
        ("missing", {}, "Unknown computation operation"),
        ("enumerate_dyck_paths", {"semilength": True}, "must be an integer"),
        ("enumerate_dyck_paths", {"semilength": 11}, "cannot exceed 10"),
        (
            "enumerate_dyck_paths",
            {"semilength": 4, "command": "anything"},
            "Unsupported parameter",
        ),
        (
            "dyck_path_statistics",
            {"steps": "EN"},
            "below the diagonal",
        ),
        (
            "enumerate_rational_dyck_paths",
            {"r": 6, "s": 4},
            "must be coprime",
        ),
        (
            "type_c_hecke_word",
            {"rank": 2, "word": [0, 2]},
            "between 0 and rank-1",
        ),
        (
            "dyck_path_statistics",
            {"steps": " " * 20_000 + "NNEE"},
            "request byte limit",
        ),
    ],
)
def test_validation_rejects_every_unapproved_shape(
    operation: str,
    parameters: dict[str, Any],
    message: str,
) -> None:
    error_type = (
        ComputationOperationNotFound if operation == "missing" else InvalidComputationRequest
    )
    with pytest.raises(error_type, match=message):
        validate_parameters(operation, parameters)


def test_reviewed_kernels_match_small_exact_examples() -> None:
    stats = execute_operation(
        "dyck_path_statistics",
        {"steps": "NNEE"},
        _progress,
    )["value"]
    classical = execute_operation(
        "enumerate_dyck_paths",
        {"semilength": 4},
        _progress,
    )["value"]
    rational = execute_operation(
        "enumerate_rational_dyck_paths",
        {"r": 5, "s": 3},
        _progress,
    )["value"]
    hecke = execute_operation(
        "type_c_hecke_word",
        {"rank": 3, "word": [0, 1, 0, 2]},
        _progress,
    )["value"]

    assert stats == {
        "steps": "NNEE",
        "semilength": 2,
        "area_sequence": [0, 1],
        "area": 1,
        "dinv": 0,
        "deficit": 0,
        "deficit_pair_count": 0,
        "deficit_consistent": True,
        "leftmost_extractable_index": 1,
        "is_full_skeleton": False,
        "is_special_skeleton": False,
    }
    assert classical["count"] == classical["expected_catalan_count"] == 14
    assert classical["area_dinv_symmetric"] is True
    assert rational["count"] == rational["expected_rational_catalan_count"] == 7
    assert hecke["final_permutation"] == [-2, 3, -1]
    assert hecke["changed_steps"] == [1, 2, 3, 4]


def test_every_public_dyck_bound_satisfies_its_internal_exact_checks() -> None:
    for semilength in range(1, 11):
        result = execute_operation(
            "enumerate_dyck_paths",
            {"semilength": semilength},
            _progress,
        )["value"]
        assert result["count_matches_catalan"] is True
        assert result["area_dinv_symmetric"] is True

    for r in range(2, 11):
        for s in range(2, 11):
            if gcd(r, s) != 1:
                continue
            result = execute_operation(
                "enumerate_rational_dyck_paths",
                {"r": r, "s": s},
                _progress,
            )["value"]
            assert result["count_matches_rational_catalan"] is True


def test_type_c_generators_are_idempotent_on_the_identity() -> None:
    for rank in range(1, 8):
        for generator in range(rank):
            once = execute_operation(
                "type_c_hecke_word",
                {"rank": rank, "word": [generator]},
                _progress,
            )["value"]["final_permutation"]
            twice = execute_operation(
                "type_c_hecke_word",
                {"rank": rank, "word": [generator, generator]},
                _progress,
            )["value"]["final_permutation"]
            assert once == twice


def test_isolated_worker_streams_progress_reproducibility_and_visualization(
    tmp_path: Path,
) -> None:
    content = tmp_path / "content"
    source = content / "middle_coefficients" / "code.py"
    source.parent.mkdir(parents=True)
    source.write_text("reviewed source basis\n", encoding="utf-8")
    before = source.read_bytes()
    service = ComputationService(content)
    prepared = service.prepare("enumerate_dyck_paths", {"semilength": 5})

    events = list(service.stream(prepared))

    assert events[0].type == "computation.started"
    assert events[-1].type == "computation.completed"
    progress = [
        event.data["fraction"]
        for event in events
        if event.type == "computation.progress"
    ]
    assert progress == sorted(progress)
    assert progress[-1] == 1.0
    completed = events[-1].data
    assert completed["classification"] == "finite_check"
    assert "not a proof of an unbounded claim" in completed["claim_boundary"]
    assert completed["visualization"]["language"] == "dyck-path"
    assert completed["output"]["count"] == 42
    assert len(completed["reproducibility"]["request_sha256"]) == 64
    assert len(completed["reproducibility"]["result_sha256"]) == 64
    assert completed["reproducibility"]["source_basis"]["sha256"] == hashlib.sha256(
        before
    ).hexdigest()
    assert completed["resource_usage"]["total_wall_time_ms"] > 0
    assert source.read_bytes() == before


def test_same_request_and_result_have_stable_hashes(tmp_path: Path) -> None:
    service = ComputationService(tmp_path / "content")
    first = service.prepare("dyck_path_statistics", {"steps": "NENE"})
    second = service.prepare("dyck_path_statistics", {"steps": "N E N E"})
    first_result = list(service.stream(first))[-1].data
    second_result = list(service.stream(second))[-1].data

    assert first.request_sha256 == second.request_sha256
    assert (
        first_result["reproducibility"]["result_sha256"]
        == second_result["reproducibility"]["result_sha256"]
    )
    assert first.job_id != second.job_id


def test_wall_and_output_limits_stop_workers(tmp_path: Path) -> None:
    service = ComputationService(tmp_path / "content")
    prepared = service.prepare("enumerate_dyck_paths", {"semilength": 10})
    tiny_time = replace(prepared.operation.limits, wall_time_seconds=0.001)
    tiny_output = replace(prepared.operation.limits, output_bytes=64)

    with pytest.raises(ComputationLimitExceeded, match="wall-time limit"):
        list(
            stream_isolated_worker(
                prepared.operation.id,
                prepared.parameters,
                tiny_time,
                forbidden_roots=(service.content_root,),
            )
        )
    with pytest.raises(ComputationLimitExceeded, match="stdout byte limit"):
        list(
            stream_isolated_worker(
                prepared.operation.id,
                prepared.parameters,
                tiny_output,
                forbidden_roots=(service.content_root,),
            )
        )


@pytest.mark.skipif(os.name != "nt", reason="Windows Job Object enforcement test")
def test_windows_job_object_enforces_process_memory(tmp_path: Path) -> None:
    service = ComputationService(tmp_path / "content")
    prepared = service.prepare("dyck_path_statistics", {"steps": "NNEE"})
    constrained = replace(
        prepared.operation.limits,
        memory_bytes=8 * 1024 * 1024,
    )

    with pytest.raises(ComputationLimitExceeded, match="CPU or memory limit"):
        list(
            stream_isolated_worker(
                prepared.operation.id,
                prepared.parameters,
                constrained,
                forbidden_roots=(service.content_root,),
            )
        )


def test_prepared_request_integrity_is_rechecked_before_execution(
    tmp_path: Path,
) -> None:
    service = ComputationService(tmp_path / "content")
    prepared = service.prepare("dyck_path_statistics", {"steps": "NNEE"})
    tampered = replace(prepared, parameters={"steps": "NENE"})

    events = list(service.stream(tampered))

    assert [event.type for event in events] == ["computation.error"]
    assert events[0].data["code"] == "invalid_computation_request"
    assert "integrity check" in events[0].data["message"]


def test_concurrency_limit_rejects_without_starting_a_worker(tmp_path: Path) -> None:
    service = ComputationService(tmp_path / "content", max_workers=1)
    prepared = service.prepare("dyck_path_statistics", {"steps": "NNEE"})
    assert service._slots.acquire(blocking=False)
    try:
        events = list(service.stream(prepared))
    finally:
        service._slots.release()

    assert [event.type for event in events] == ["computation.error"]
    assert events[0].data["code"] == "computation_busy"


def test_api_catalog_validation_and_sse_contract(tmp_path: Path) -> None:
    config = RetrievalConfig(
        content_root=tmp_path / "content",
        database_path=tmp_path / ".craig" / "index.sqlite3",
    )
    app = create_app(config)

    catalog = _request(app, "GET", "/api/v1/computations")
    configuration = _request(app, "GET", "/api/v1/chat/config")
    invalid = _request(
        app,
        "POST",
        "/api/v1/computations/stream",
        json_body={"operation": "anything", "parameters": {}},
    )
    stream = _request(
        app,
        "POST",
        "/api/v1/computations/stream",
        json_body={
            "operation": "enumerate_rational_dyck_paths",
            "parameters": {"r": 5, "s": 3},
        },
    )

    assert catalog.status_code == 200
    assert len(catalog.json()["operations"]) == 4
    computation_mode = next(
        mode
        for mode in configuration.json()["modes"]
        if mode["id"] == "computation"
    )
    assert computation_mode["computation_enabled"] is True
    assert invalid.status_code == 404
    assert invalid.json()["error"]["code"] == "computation_not_found"
    assert stream.status_code == 200
    assert stream.headers["content-type"].startswith("text/event-stream")
    payloads = _sse_payloads(stream)
    assert payloads[0]["type"] == "computation.started"
    assert payloads[-1]["type"] == "computation.completed"
    assert payloads[-1]["data"]["output"]["count"] == 7
    assert all(payload["job_id"] == payloads[0]["job_id"] for payload in payloads)

    openapi = _request(app, "GET", "/openapi.json").json()
    catalog_schema = openapi["paths"]["/api/v1/computations"]["get"]["responses"][
        "200"
    ]["content"]["application/json"]["schema"]
    assert catalog_schema["$ref"].endswith("/ComputationCatalogResponse")
