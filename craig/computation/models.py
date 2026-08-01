"""Typed contracts for curated computations and streamed events."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any, Literal
from uuid import uuid4


def _utc_timestamp() -> str:
    return datetime.now(UTC).isoformat()


def _new_identifier(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"

EvidenceClassification = Literal[
    "example",
    "experiment",
    "finite_check",
    "computer_assisted_proof",
]
ParameterKind = Literal["integer", "string", "integer_array"]


@dataclass(frozen=True, slots=True)
class ComputationLimits:
    """Hard limits applied to one isolated worker process."""

    wall_time_seconds: float
    cpu_time_seconds: int
    memory_bytes: int
    output_bytes: int = 262_144
    stderr_bytes: int = 32_768
    request_bytes: int = 16_384


@dataclass(frozen=True, slots=True)
class ParameterSpec:
    """Public description of one closed operation parameter."""

    name: str
    kind: ParameterKind
    label: str
    description: str
    required: bool = True
    default: Any = None
    minimum: int | None = None
    maximum: int | None = None
    max_items: int | None = None


@dataclass(frozen=True, slots=True)
class OperationSpec:
    """One reviewed operation in the public allowlist."""

    id: str
    title: str
    description: str
    classification: EvidenceClassification
    implementation_version: str
    source_path: str
    source_start_line: int
    source_end_line: int
    parameters: tuple[ParameterSpec, ...]
    limits: ComputationLimits

    def public_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "classification": self.classification,
            "implementation_version": self.implementation_version,
            "source_basis": {
                "path": self.source_path,
                "start_line": self.source_start_line,
                "end_line": self.source_end_line,
            },
            "parameters": [asdict(parameter) for parameter in self.parameters],
            "limits": asdict(self.limits),
        }


@dataclass(frozen=True, slots=True)
class PreparedComputation:
    """A normalized request safe to send to the isolated worker."""

    operation: OperationSpec
    parameters: dict[str, Any]
    request_sha256: str
    job_id: str = field(default_factory=lambda: _new_identifier("job"))


@dataclass(frozen=True, slots=True)
class ComputationEvent:
    """One SSE event from a computation job."""

    type: str
    job_id: str
    data: dict[str, Any]
    created_at: str = field(default_factory=_utc_timestamp)
