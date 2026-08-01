from __future__ import annotations

import pytest

from craig.chat.provenance import (
    MAX_SOURCE_EXCERPT_CHARS,
    bounded_excerpt,
    citation_identifier,
    classify_mathematical_status,
)


@pytest.mark.parametrize(
    ("heading", "environment", "expected_status", "expected_basis"),
    [
        (
            "A computer-assisted proof",
            "section",
            "computer_assisted_proof",
            "explicit computer-assisted proof heading",
        ),
        (
            "Computational evidence",
            "heading_2",
            "computational_evidence",
            "explicit computational-evidence heading",
        ),
        (
            "Experimental results",
            None,
            "experimental_observation",
            "explicit experimental heading",
        ),
        (
            "Proof outline",
            "proof",
            "proof_outline",
            "explicit proof-outline heading",
        ),
        (
            "Work in progress",
            None,
            "work_in_progress",
            "explicit work-in-progress heading",
        ),
        (
            "A possible conjecture",
            "section",
            "conjecture",
            "explicit conjecture heading",
        ),
        ("Main result", "theorem", "proved_result", "parsed theorem environment"),
        (
            "Conjecture resolved",
            "theorem",
            "proved_result",
            "parsed theorem environment",
        ),
        (
            "Proof of Conjecture 2",
            "proof",
            "proved_result",
            "parsed proof environment",
        ),
        ("Dominance", "lemma", "proved_result", "parsed lemma environment"),
        (None, "conjecture", "conjecture", "parsed conjecture environment"),
        ("Discussion of a conjecture", "section", "unknown", None),
        ("Definition", "definition", "unknown", None),
        (None, None, "unknown", None),
    ],
)
def test_status_classification_requires_explicit_structure(
    heading: str | None,
    environment: str | None,
    expected_status: str,
    expected_basis: str | None,
) -> None:
    status, basis = classify_mathematical_status(
        heading=heading,
        environment=environment,
    )

    assert status == expected_status
    assert basis == expected_basis


def test_citation_identifier_is_stable_and_location_sensitive() -> None:
    arguments = {
        "path": "topic/explanation.tex",
        "start_line": 10,
        "end_line": 14,
        "file_hash": "a" * 64,
    }

    first = citation_identifier(**arguments)
    repeated = citation_identifier(**arguments)
    moved = citation_identifier(**{**arguments, "start_line": 11})

    assert first == repeated
    assert first.startswith("C-")
    assert first != moved


def test_source_excerpt_is_text_only_and_bounded() -> None:
    excerpt = bounded_excerpt(
        {
            "snippet": "begin\x00" + ("x" * (MAX_SOURCE_EXCERPT_CHARS + 100)),
        }
    )

    assert "\x00" not in excerpt
    assert len(excerpt) == MAX_SOURCE_EXCERPT_CHARS
    assert excerpt.endswith("…")
