"""Repeatable synthetic evaluations for configured answer-generation models."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

from .chat.models import (
    AnswerRequest,
    ChatMessage,
    ConversationSnapshot,
    SourceReference,
)
from .chat.prompts import secondary_system_prompt
from .chat.providers import ModelProvider

EvaluationTier = Literal["strong", "small"]


@dataclass(frozen=True, slots=True)
class EvaluationCase:
    id: str
    question: str
    source: SourceReference
    required_terms: tuple[str, ...]
    boundary_terms: tuple[str, ...] = ()


def _source(
    citation_id: str,
    excerpt: str,
    status: str,
) -> SourceReference:
    return SourceReference(
        citation_id=citation_id,
        topic="synthetic_release_evaluation",
        path="synthetic/evaluation.txt",
        heading="Synthetic release fixture",
        environment=None,
        start_line=1,
        end_line=1,
        file_hash="0" * 64,
        excerpt=excerpt,
        mathematical_status=status,  # type: ignore[arg-type]
        status_basis="Synthetic Phase 8 evaluation fixture.",
    )


EVALUATION_CASES: tuple[EvaluationCase, ...] = (
    EvaluationCase(
        id="citation_grounding",
        question="What is a strict widget according to the supplied source?",
        source=_source(
            "C-EVAL-1",
            "A strict widget is a finite sequence of decreasing positive integers.",
            "proved_result",
        ),
        required_terms=("C-EVAL-1", "decreasing"),
    ),
    EvaluationCase(
        id="finite_evidence_boundary",
        question="Does this finite computation prove the claim for every n?",
        source=_source(
            "C-EVAL-2",
            "The program exhaustively checked n at most 6. This finite check is not a proof for all n.",
            "computational_evidence",
        ),
        required_terms=("C-EVAL-2",),
        boundary_terms=("not a proof", "does not prove", "finite check"),
    ),
    EvaluationCase(
        id="unknown_status",
        question="Is the supplied statement a proved theorem?",
        source=_source(
            "C-EVAL-3",
            "The notes state that blue widgets appear to be unimodal.",
            "unknown",
        ),
        required_terms=("C-EVAL-3", "unknown"),
    ),
)


def _request(case: EvaluationCase) -> AnswerRequest:
    timestamp = "2000-01-01T00:00:00+00:00"
    conversation = ConversationSnapshot(
        id=f"eval_{case.id}",
        mode="research",
        topic=None,
        created_at=timestamp,
        updated_at=timestamp,
        messages=(
            ChatMessage(
                id=f"eval_user_{case.id}",
                role="user",
                content=case.question,
                created_at=timestamp,
            ),
        ),
    )
    return AnswerRequest(
        message=case.question,
        mode="research",
        topic=None,
        conversation=conversation,
        tool_results=(),
        sources=(case.source,),
        system_prompt=secondary_system_prompt(
            "research",
            None,
            (),
            (case.source,),
        ),
    )


def evaluate_provider(
    provider: ModelProvider,
    *,
    tier: EvaluationTier,
) -> dict[str, object]:
    """Evaluate one configured model against the same bounded release cases."""

    if tier not in {"strong", "small"}:
        raise ValueError("tier must be strong or small")
    results: list[dict[str, object]] = []
    for case in EVALUATION_CASES:
        answer = "".join(provider.stream_answer(_request(case))).strip()
        lowered = answer.casefold()
        required = {
            term: term.casefold() in lowered for term in case.required_terms
        }
        boundary_passed = not case.boundary_terms or any(
            term.casefold() in lowered for term in case.boundary_terms
        )
        passed = bool(answer) and all(required.values()) and boundary_passed
        results.append(
            {
                "id": case.id,
                "passed": passed,
                "required_terms": required,
                "boundary_passed": boundary_passed,
                "answer": answer,
            }
        )
    passed_cases = sum(bool(result["passed"]) for result in results)
    return {
        "schema_version": 1,
        "tier": tier,
        "provider": asdict(provider.metadata),
        "case_count": len(results),
        "passed_cases": passed_cases,
        "all_passed": passed_cases == len(results),
        "cases": results,
        "limitations": (
            "This synthetic release evaluation checks citation retention and "
            "status boundaries; it is not a comprehensive measure of mathematical quality."
        ),
    }
