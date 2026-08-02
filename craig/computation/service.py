"""Preparation, execution, and provenance for curated computation jobs."""

from __future__ import annotations

import hashlib
import json
import threading
import time
from collections.abc import Iterator
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .errors import (
    ComputationBusy,
    ComputationError,
    ComputationLimitExceeded,
    ComputationWorkerFailure,
    InvalidComputationRequest,
)
from .isolation import stream_isolated_worker
from .models import ComputationEvent, OperationSpec, PreparedComputation
from .registry import OPERATIONS, operation_spec, validate_parameters


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _claim_boundary(classification: str) -> str:
    boundaries = {
        "example": "This result is a bounded exact example.",
        "experiment": (
            "This result is an exploratory bounded experiment; it is not an "
            "exhaustive check or a proof."
        ),
        "finite_check": (
            "This is an exhaustive check only for the displayed finite "
            "parameters; it is not a proof of an unbounded claim."
        ),
        "computer_assisted_proof": (
            "This run is proof-relevant only under its separately reviewed "
            "proof obligations and exact reproducibility contract."
        ),
    }
    return boundaries.get(
        classification,
        "This computation has an unknown evidentiary classification.",
    )


def _error_code(error: ComputationError) -> str:
    if isinstance(error, ComputationLimitExceeded):
        return "computation_limit_exceeded"
    if isinstance(error, ComputationWorkerFailure):
        return "computation_worker_failed"
    if isinstance(error, InvalidComputationRequest):
        return "invalid_computation_request"
    if isinstance(error, ComputationBusy):
        return "computation_busy"
    return "computation_failed"


class ComputationService:
    """Run reviewed operations in bounded isolated workers."""

    def __init__(self, content_root: Path, *, max_workers: int = 2) -> None:
        if isinstance(max_workers, bool) or not isinstance(max_workers, int) or max_workers < 1:
            raise ValueError("max_workers must be a positive integer")
        self.content_root = content_root.resolve()
        self.max_workers = max_workers
        self._slots = threading.BoundedSemaphore(max_workers)
        computation_root = Path(__file__).resolve().parent
        digest = hashlib.sha256()
        for name in (
            "isolation.py",
            "kernels.py",
            "models.py",
            "registry.py",
            "traces.py",
            "worker.py",
        ):
            digest.update(name.encode("utf-8"))
            digest.update(b"\0")
            digest.update((computation_root / name).read_bytes())
        self.implementation_sha256 = digest.hexdigest()

    def catalog(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "operations": [
                OPERATIONS[operation].public_dict() for operation in sorted(OPERATIONS)
            ],
            "max_concurrent_workers": self.max_workers,
            "execution_policy": "isolated_allowlist",
        }

    def prepare(self, operation: str, parameters: Any) -> PreparedComputation:
        spec = operation_spec(operation)
        normalized = validate_parameters(operation, parameters)
        request_sha256 = self._request_sha256(spec, normalized)
        return PreparedComputation(
            operation=spec,
            parameters=normalized,
            request_sha256=request_sha256,
        )

    def _request_sha256(
        self,
        spec: OperationSpec,
        parameters: dict[str, Any],
    ) -> str:
        return _sha256(
            {
                "operation": spec.id,
                "parameters": parameters,
                "implementation_version": spec.implementation_version,
                "implementation_sha256": self.implementation_sha256,
            }
        )

    def _source_sha256(self, prepared: PreparedComputation) -> str | None:
        candidate = (self.content_root / prepared.operation.source_path).resolve()
        try:
            candidate.relative_to(self.content_root)
        except ValueError:
            return None
        if not candidate.is_file():
            return None
        return hashlib.sha256(candidate.read_bytes()).hexdigest()

    def stream(self, prepared: PreparedComputation) -> Iterator[ComputationEvent]:
        try:
            registered = operation_spec(prepared.operation.id)
            normalized = validate_parameters(registered.id, prepared.parameters)
            if prepared.operation != registered or normalized != prepared.parameters:
                raise InvalidComputationRequest(
                    "prepared computation does not match the reviewed registry"
                )
            if prepared.request_sha256 != self._request_sha256(registered, normalized):
                raise InvalidComputationRequest(
                    "prepared computation failed its request integrity check"
                )
        except ComputationError as error:
            yield self._event(
                "computation.error",
                prepared,
                {"code": _error_code(error), "message": str(error)},
            )
            return
        if not self._slots.acquire(blocking=False):
            yield self._event(
                "computation.error",
                prepared,
                {
                    "code": "computation_busy",
                    "message": (
                        f"All {self.max_workers} computation worker slots are occupied."
                    ),
                },
            )
            return
        started = time.monotonic()
        try:
            yield self._event(
                "computation.started",
                prepared,
                {
                    "operation": prepared.operation.id,
                    "title": prepared.operation.title,
                    "classification": prepared.operation.classification,
                    "parameters": prepared.parameters,
                    "limits": asdict(prepared.operation.limits),
                    "request_sha256": prepared.request_sha256,
                },
            )
            result_envelope: dict[str, Any] | None = None
            for message in stream_isolated_worker(
                prepared.operation.id,
                prepared.parameters,
                prepared.operation.limits,
                forbidden_roots=(self.content_root,),
            ):
                if message["type"] == "progress":
                    yield self._event("computation.progress", prepared, message["data"])
                elif message["type"] == "result":
                    result_envelope = message["data"]
            if result_envelope is None:
                raise ComputationError("worker did not provide a result")
            result = result_envelope["result"]
            result_sha256 = _sha256(result)
            yield self._event(
                "computation.completed",
                prepared,
                {
                    "operation": prepared.operation.id,
                    "title": prepared.operation.title,
                    "classification": prepared.operation.classification,
                    "parameters": prepared.parameters,
                    "summary": result["summary"],
                    "output": result["value"],
                    "visualization": result.get("visualization"),
                    "trace": result.get("trace"),
                    "reproducibility": {
                        "implementation_version": (
                            prepared.operation.implementation_version
                        ),
                        "implementation_sha256": self.implementation_sha256,
                        "source_basis": {
                            "path": prepared.operation.source_path,
                            "start_line": prepared.operation.source_start_line,
                            "end_line": prepared.operation.source_end_line,
                            "sha256": self._source_sha256(prepared),
                        },
                        "request_sha256": prepared.request_sha256,
                        "result_sha256": result_sha256,
                        "worker_runtime": result_envelope.get("runtime", {}),
                    },
                    "resource_usage": {
                        **result_envelope.get("metrics", {}),
                        "total_wall_time_ms": round(
                            (time.monotonic() - started) * 1000,
                            3,
                        ),
                    },
                    "limits": asdict(prepared.operation.limits),
                    "claim_boundary": _claim_boundary(
                        prepared.operation.classification
                    ),
                },
            )
        except ComputationError as error:
            yield self._event(
                "computation.error",
                prepared,
                {
                    "code": _error_code(error),
                    "message": str(error),
                },
            )
        except Exception:
            yield self._event(
                "computation.error",
                prepared,
                {
                    "code": "unexpected_computation_failure",
                    "message": "The isolated computation failed unexpectedly.",
                },
            )
        finally:
            self._slots.release()

    @staticmethod
    def _event(
        event_type: str,
        prepared: PreparedComputation,
        data: dict[str, Any],
    ) -> ComputationEvent:
        return ComputationEvent(
            type=event_type,
            job_id=prepared.job_id,
            data=data,
        )
