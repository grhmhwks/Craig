"""Conservative Phase 4 citation and mathematical-status helpers."""

from __future__ import annotations

import hashlib
import re
from typing import Any

from .models import MathematicalStatus

MAX_SOURCE_EXCERPT_CHARS = 1_600

_HEADING_STATUS_RULES: tuple[
    tuple[re.Pattern[str], MathematicalStatus, str],
    ...,
] = (
    (
        re.compile(r"\bcomputer[- ]assisted proof\b", re.IGNORECASE),
        "computer_assisted_proof",
        "explicit computer-assisted proof heading",
    ),
    (
        re.compile(r"\bcomputational evidence\b", re.IGNORECASE),
        "computational_evidence",
        "explicit computational-evidence heading",
    ),
    (
        re.compile(
            r"\bexperimental (?:observation|evidence|results?)\b",
            re.IGNORECASE,
        ),
        "experimental_observation",
        "explicit experimental heading",
    ),
    (
        re.compile(r"\bproof outline\b", re.IGNORECASE),
        "proof_outline",
        "explicit proof-outline heading",
    ),
    (
        re.compile(r"\bwork in progress\b|\bwork-in-progress\b", re.IGNORECASE),
        "work_in_progress",
        "explicit work-in-progress heading",
    ),
)

_PROVED_ENVIRONMENTS = frozenset(
    {"theorem", "lemma", "proposition", "corollary", "proof"}
)
_CONJECTURE_HEADING = re.compile(
    r"^\s*(?:(?:a|the)\s+)?(?:(?:possible|main)\s+)?conjecture\b",
    re.IGNORECASE,
)


def citation_identifier(
    *,
    path: str,
    start_line: int,
    end_line: int,
    file_hash: str,
) -> str:
    """Return a stable short identifier derived only from public source metadata."""

    value = f"{file_hash}:{path}:{start_line}:{end_line}".encode("utf-8")
    digest = hashlib.sha256(value).hexdigest()[:12].upper()
    return f"C-{digest}"


def bounded_excerpt(item: dict[str, Any]) -> str:
    """Extract a text-only source excerpt within the Phase 4 response budget."""

    raw = item.get("snippet") or item.get("excerpt") or item.get("text") or ""
    text = str(raw).replace("\x00", "").strip()
    if len(text) <= MAX_SOURCE_EXCERPT_CHARS:
        return text
    return text[: MAX_SOURCE_EXCERPT_CHARS - 1].rstrip() + "…"


def classify_mathematical_status(
    *,
    heading: str | None,
    environment: str | None,
) -> tuple[MathematicalStatus, str | None]:
    """Classify only explicit structure; return unknown when evidence is absent."""

    if heading:
        for pattern, status, basis in _HEADING_STATUS_RULES:
            if pattern.search(heading):
                return status, basis

    normalized_environment = (environment or "").strip().casefold()
    if normalized_environment == "conjecture":
        return "conjecture", "parsed conjecture environment"
    if normalized_environment in _PROVED_ENVIRONMENTS:
        return (
            "proved_result",
            f"parsed {normalized_environment} environment",
        )
    if heading and _CONJECTURE_HEADING.search(heading):
        return "conjecture", "explicit conjecture heading"
    return "unknown", None
