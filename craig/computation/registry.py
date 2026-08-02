"""Closed operation registry and parameter validation."""

from __future__ import annotations

import json
from math import gcd
from typing import Any

from .errors import InvalidComputationRequest, ComputationOperationNotFound
from .kernels import KERNELS, Progress
from .models import ComputationLimits, OperationSpec, ParameterSpec

_SMALL_LIMITS = ComputationLimits(
    wall_time_seconds=3.0,
    cpu_time_seconds=2,
    memory_bytes=192 * 1024 * 1024,
)
_ENUMERATION_LIMITS = ComputationLimits(
    wall_time_seconds=8.0,
    cpu_time_seconds=6,
    memory_bytes=256 * 1024 * 1024,
)

OPERATIONS: dict[str, OperationSpec] = {
    "dyck_path_statistics": OperationSpec(
        id="dyck_path_statistics",
        title="Dyck path statistics",
        description="Compute the area sequence, area, dinv, and deficit of one classical Dyck path.",
        classification="example",
        implementation_version="1.1.0",
        source_path="middle_coefficients/code.py",
        source_start_line=82,
        source_end_line=186,
        parameters=(
            ParameterSpec(
                name="steps",
                kind="string",
                label="N/E steps",
                description="A classical Dyck path that stays above the diagonal.",
                default="NNEENNEE",
                minimum=2,
                maximum=160,
            ),
        ),
        limits=_SMALL_LIMITS,
    ),
    "enumerate_dyck_paths": OperationSpec(
        id="enumerate_dyck_paths",
        title="Enumerate classical Dyck paths",
        description="Exhaustively enumerate a bounded semilength and tabulate area and dinv.",
        classification="finite_check",
        implementation_version="1.0.0",
        source_path="middle_coefficients/code.py",
        source_start_line=82,
        source_end_line=186,
        parameters=(
            ParameterSpec(
                name="semilength",
                kind="integer",
                label="Semilength",
                description="The number of north steps and east steps.",
                default=5,
                minimum=1,
                maximum=10,
            ),
        ),
        limits=_ENUMERATION_LIMITS,
    ),
    "enumerate_rational_dyck_paths": OperationSpec(
        id="enumerate_rational_dyck_paths",
        title="Enumerate rational Dyck paths",
        description="Exhaustively count bounded coprime (r,s)-Dyck paths above the diagonal.",
        classification="finite_check",
        implementation_version="1.0.0",
        source_path="conjectured_rational_formula/code.py",
        source_start_line=67,
        source_end_line=249,
        parameters=(
            ParameterSpec(
                name="r",
                kind="integer",
                label="East steps r",
                description="Horizontal endpoint coordinate.",
                default=5,
                minimum=2,
                maximum=10,
            ),
            ParameterSpec(
                name="s",
                kind="integer",
                label="North steps s",
                description="Vertical endpoint coordinate; must be coprime to r.",
                default=3,
                minimum=2,
                maximum=10,
            ),
        ),
        limits=_ENUMERATION_LIMITS,
    ),
    "type_c_hecke_word": OperationSpec(
        id="type_c_hecke_word",
        title="Evaluate a type C 0-Hecke word",
        description="Apply an allowlisted generator word to the identity signed permutation.",
        classification="example",
        implementation_version="1.1.0",
        source_path="type_c_grothendieck/code.py",
        source_start_line=42,
        source_end_line=62,
        parameters=(
            ParameterSpec(
                name="rank",
                kind="integer",
                label="Rank",
                description="Signed-permutation rank.",
                default=3,
                minimum=1,
                maximum=7,
            ),
            ParameterSpec(
                name="word",
                kind="integer_array",
                label="Generator word",
                description="Comma-separated generators in the range 0 through rank-1.",
                default=(0, 1, 0, 2),
                minimum=0,
                maximum=6,
                max_items=80,
            ),
        ),
        limits=_SMALL_LIMITS,
    ),
    "tableau_row_insertion": OperationSpec(
        id="tableau_row_insertion",
        title="Trace ordinary tableau row insertion",
        description=(
            "Insert a bounded integer word by the ordinary RSK baseline and trace "
            "bumping together with its recording tableau."
        ),
        classification="example",
        implementation_version="1.0.0",
        source_path="dyck_symmetric_functions/explanation.tex",
        source_start_line=164,
        source_end_line=219,
        parameters=(
            ParameterSpec(
                name="word",
                kind="integer_array",
                label="Insertion word",
                description="Comma-separated integers inserted from left to right.",
                default=(3, 1, 4, 1, 5, 2),
                minimum=-99,
                maximum=99,
                max_items=12,
            ),
        ),
        limits=_SMALL_LIMITS,
    ),
}


def operation_spec(operation: str) -> OperationSpec:
    if not isinstance(operation, str) or operation not in OPERATIONS:
        raise ComputationOperationNotFound(
            "Unknown computation operation; choose an id from the public allowlist."
        )
    return OPERATIONS[operation]


def _integer(value: Any, parameter: ParameterSpec) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise InvalidComputationRequest(f"{parameter.name} must be an integer.")
    if parameter.minimum is not None and value < parameter.minimum:
        raise InvalidComputationRequest(
            f"{parameter.name} must be at least {parameter.minimum}."
        )
    if parameter.maximum is not None and value > parameter.maximum:
        raise InvalidComputationRequest(
            f"{parameter.name} cannot exceed {parameter.maximum}."
        )
    return value


def _string(value: Any, parameter: ParameterSpec) -> str:
    if not isinstance(value, str):
        raise InvalidComputationRequest(f"{parameter.name} must be a string.")
    normalized = "".join(value.upper().split())
    if parameter.minimum is not None and len(normalized) < parameter.minimum:
        raise InvalidComputationRequest(
            f"{parameter.name} must have at least {parameter.minimum} characters."
        )
    if parameter.maximum is not None and len(normalized) > parameter.maximum:
        raise InvalidComputationRequest(
            f"{parameter.name} cannot exceed {parameter.maximum} characters."
        )
    return normalized


def _integer_array(value: Any, parameter: ParameterSpec) -> list[int]:
    if not isinstance(value, (list, tuple)):
        raise InvalidComputationRequest(f"{parameter.name} must be an integer array.")
    if parameter.max_items is not None and len(value) > parameter.max_items:
        raise InvalidComputationRequest(
            f"{parameter.name} cannot contain more than {parameter.max_items} items."
        )
    return [_integer(item, parameter) for item in value]


def validate_parameters(operation: str, parameters: Any) -> dict[str, Any]:
    spec = operation_spec(operation)
    if not isinstance(parameters, dict):
        raise InvalidComputationRequest("parameters must be a JSON object.")
    try:
        raw_parameters = json.dumps(
            parameters,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise InvalidComputationRequest("parameters must contain JSON values.") from error
    if len(raw_parameters) > spec.limits.request_bytes:
        raise InvalidComputationRequest("parameters exceed the request byte limit.")
    allowed = {parameter.name for parameter in spec.parameters}
    unexpected = sorted(set(parameters) - allowed)
    if unexpected:
        raise InvalidComputationRequest(
            f"Unsupported parameter for {operation}: {unexpected[0]}."
        )
    normalized: dict[str, Any] = {}
    for parameter in spec.parameters:
        if parameter.name in parameters:
            value = parameters[parameter.name]
        elif parameter.default is not None:
            value = parameter.default
        elif parameter.required:
            raise InvalidComputationRequest(
                f"Missing required parameter: {parameter.name}."
            )
        else:
            continue
        if parameter.kind == "integer":
            normalized[parameter.name] = _integer(value, parameter)
        elif parameter.kind == "string":
            normalized[parameter.name] = _string(value, parameter)
        else:
            normalized[parameter.name] = _integer_array(value, parameter)

    if operation == "dyck_path_statistics":
        steps = normalized["steps"]
        if not steps or any(step not in "NE" for step in steps):
            raise InvalidComputationRequest("steps may contain only N and E.")
        east = north = 0
        for index, step in enumerate(steps):
            if step == "N":
                north += 1
            else:
                east += 1
            if east > north:
                raise InvalidComputationRequest(
                    f"steps go below the diagonal at position {index + 1}."
                )
        if east != north:
            raise InvalidComputationRequest(
                "steps must end with equally many N and E steps."
            )
        if east > 80:
            raise InvalidComputationRequest("steps cannot exceed semilength 80.")
    elif operation == "enumerate_rational_dyck_paths":
        if gcd(normalized["r"], normalized["s"]) != 1:
            raise InvalidComputationRequest("r and s must be coprime.")
    elif operation == "type_c_hecke_word":
        rank = normalized["rank"]
        if any(generator >= rank for generator in normalized["word"]):
            raise InvalidComputationRequest(
                "every generator must be between 0 and rank-1."
            )
    elif operation == "tableau_row_insertion" and not normalized["word"]:
        raise InvalidComputationRequest("word must contain at least one integer.")

    encoded = json.dumps(normalized, separators=(",", ":"), sort_keys=True).encode()
    if len(encoded) > spec.limits.request_bytes:
        raise InvalidComputationRequest("normalized parameters exceed the request limit.")
    return normalized


def execute_operation(
    operation: str,
    parameters: Any,
    progress: Progress,
) -> dict[str, Any]:
    normalized = validate_parameters(operation, parameters)
    kernel = KERNELS[operation]
    return kernel(normalized, progress)
