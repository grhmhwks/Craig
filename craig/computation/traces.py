"""Versioned, bounded contracts for deterministic algorithm traces.

Trace values are plain JSON.  They are produced by reviewed kernels and are
validated again by the browser before any trusted visualization is rendered.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from typing import Any

TRACE_SCHEMA_VERSION = 1
MAX_TRACE_EVENTS = 192
MAX_TRACE_BYTES = 196_608
MAX_STATE_BYTES = 32_768
MAX_VISUALIZATIONS_PER_EVENT = 3

TRACE_EVENT_KINDS = frozenset(
    {
        "initialization",
        "insertion",
        "bumping",
        "extraction",
        "reinsertion",
        "recording",
        "local_move",
        "completion",
    }
)

TRACE_VISUALIZATION_LANGUAGES = frozenset(
    {
        "tableau",
        "young-diagram",
        "dyck-path",
        "reading-word",
        "factorization",
        "skeleton",
        "string-diagram",
    }
)


def _encoded_size(value: Any) -> int:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise ValueError("algorithm traces must contain only JSON values") from error
    return len(encoded)


def _bounded_text(value: Any, name: str, maximum: int) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    normalized = value.strip()
    if len(normalized) > maximum:
        raise ValueError(f"{name} cannot exceed {maximum} characters")
    return normalized


def _validated_visualizations(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        raise ValueError("trace visualizations must be a list")
    if len(value) > MAX_VISUALIZATIONS_PER_EVENT:
        raise ValueError("a trace event contains too many visualizations")
    validated: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, Mapping) or set(item) != {"label", "language", "spec"}:
            raise ValueError("trace visualizations have a closed schema")
        label = _bounded_text(item["label"], "visualization label", 80)
        language = item["language"]
        if language not in TRACE_VISUALIZATION_LANGUAGES:
            raise ValueError("trace visualization language is not allowlisted")
        spec = item["spec"]
        if not isinstance(spec, Mapping):
            raise ValueError("trace visualization spec must be an object")
        if _encoded_size(spec) > 16_384:
            raise ValueError("trace visualization spec is too large")
        validated.append({"label": label, "language": language, "spec": dict(spec)})
    return validated


def algorithm_trace(
    algorithm: str,
    title: str,
    events: Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
    """Validate and return one canonical algorithm-trace object."""

    normalized_events = list(events)
    if not normalized_events or len(normalized_events) > MAX_TRACE_EVENTS:
        raise ValueError(
            f"algorithm traces must contain between 1 and {MAX_TRACE_EVENTS} events"
        )

    validated_events: list[dict[str, Any]] = []
    expected_keys = {
        "index",
        "kind",
        "title",
        "description",
        "state",
        "visualizations",
    }
    for expected_index, event in enumerate(normalized_events):
        if not isinstance(event, Mapping) or set(event) != expected_keys:
            raise ValueError("trace events have a closed schema")
        if event["index"] != expected_index:
            raise ValueError("trace event indexes must be contiguous and zero-based")
        if event["kind"] not in TRACE_EVENT_KINDS:
            raise ValueError("trace event kind is not recognized")
        state = event["state"]
        if not isinstance(state, Mapping):
            raise ValueError("trace event state must be an object")
        if _encoded_size(state) > MAX_STATE_BYTES:
            raise ValueError("trace event state is too large")
        validated_events.append(
            {
                "index": expected_index,
                "kind": event["kind"],
                "title": _bounded_text(event["title"], "event title", 100),
                "description": _bounded_text(
                    event["description"], "event description", 320
                ),
                "state": dict(state),
                "visualizations": _validated_visualizations(event["visualizations"]),
            }
        )

    trace = {
        "schema_version": TRACE_SCHEMA_VERSION,
        "algorithm": _bounded_text(algorithm, "algorithm", 80),
        "title": _bounded_text(title, "trace title", 120),
        "events": validated_events,
    }
    if _encoded_size(trace) > MAX_TRACE_BYTES:
        raise ValueError(f"algorithm trace exceeds the {MAX_TRACE_BYTES}-byte limit")
    return trace
