"""Provider-neutral planning and answer-generation interfaces."""

from __future__ import annotations

import os
import re
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Protocol

from .errors import ProviderUnavailableError
from .models import (
    AnswerRequest,
    PlanningRequest,
    ProvenanceAnnotation,
    ToolCall,
    ToolResult,
)


@dataclass(frozen=True, slots=True)
class ProviderMetadata:
    """Non-secret provider information safe to return to the browser."""

    name: str
    model: str
    configured: bool
    live: bool


class ModelProvider(Protocol):
    """Two-stage provider contract used by the orchestration service."""

    @property
    def metadata(self) -> ProviderMetadata:
        """Return browser-safe provider status."""

    def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
        """Choose initial read-only retrieval calls."""

    def refine(
        self,
        request: PlanningRequest,
        results: tuple[ToolResult, ...],
    ) -> tuple[ToolCall, ...]:
        """Choose a bounded follow-up retrieval step, if one is useful."""

    def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
        """Yield text fragments for the grounded assistant answer."""

    def answer_annotations(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        """Describe non-repository reasoning or knowledge used in the answer."""


class DemoModelProvider:
    """Deterministic local provider for UI development and orchestration tests."""

    metadata = ProviderMetadata(
        name="demo",
        model="deterministic-retrieval",
        configured=True,
        live=False,
    )

    def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
        """Plan a small lexical search, optionally adding exact-text lookup."""

        lowered = request.message.casefold()
        if any(
            phrase in lowered
            for phrase in ("list topics", "which topics", "what topics")
        ):
            return (ToolCall(name="list_topics", arguments={}),)

        shared = {
            "query": request.message,
            "topic": request.topic,
            "limit": 4,
            "max_chars": 6_000,
        }
        calls = [ToolCall(name="search_content", arguments=shared)]
        quoted = re.search(r"[\"“](.{2,160}?)[\"”]", request.message)
        if quoted:
            calls.append(
                ToolCall(
                    name="find_exact",
                    arguments={
                        "query": quoted.group(1),
                        "topic": request.topic,
                        "case_sensitive": False,
                        "context_lines": 2,
                        "limit": 3,
                        "max_chars": 4_000,
                    },
                )
            )
        return tuple(calls)

    def refine(
        self,
        request: PlanningRequest,
        results: tuple[ToolResult, ...],
    ) -> tuple[ToolCall, ...]:
        """Read the highest-ranked source passage after the initial search."""

        del request
        if any(result.name == "read_source" for result in results):
            return ()
        for result in results:
            if not result.success or result.name not in {
                "search_content",
                "find_exact",
            }:
                continue
            candidates = result.output.get("results")
            if not isinstance(candidates, (list, tuple)) or not candidates:
                continue
            top = candidates[0]
            if not isinstance(top, dict):
                continue
            path = top.get("path")
            start = top.get("start_line", top.get("match_start_line"))
            end = top.get("end_line", top.get("match_end_line"))
            if (
                isinstance(path, str)
                and isinstance(start, int)
                and isinstance(end, int)
            ):
                return (
                    ToolCall(
                        name="read_source",
                        arguments={
                            "path": path,
                            "start_line": start,
                            "end_line": end,
                            "max_chars": 8_000,
                        },
                    ),
                )
        return ()

    def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
        """Yield a transparent retrieval summary without claiming model insight."""

        answer = self._answer(request)
        pieces = re.findall(r"\S+\s*", answer)
        for index in range(0, len(pieces), 10):
            yield "".join(pieces[index : index + 10])

    def answer_annotations(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        """Label retrieval ranking and optional tutorial guidance explicitly."""

        annotations: list[ProvenanceAnnotation] = []
        citation_ids = tuple(source.citation_id for source in request.sources)
        if citation_ids:
            annotations.append(
                ProvenanceAnnotation(
                    kind="deduction",
                    description=(
                        "CRAIG selected and ordered these passages using lexical "
                        "retrieval; that relevance ordering is not a statement "
                        "made by the repository."
                    ),
                    citation_ids=citation_ids,
                )
            )
        else:
            annotations.append(
                ProvenanceAnnotation(
                    kind="deduction",
                    description=(
                        "The no-result statement describes this bounded lexical "
                        "search; it does not prove that the corpus contains no "
                        "relevant material."
                    ),
                )
            )
        if request.mode == "tutorial" and request.sources:
            annotations.append(
                ProvenanceAnnotation(
                    kind="model_knowledge",
                    description=(
                        "The suggested reading sequence is general pedagogical "
                        "guidance supplied by CRAIG."
                    ),
                )
            )
        return tuple(annotations)

    def _answer(self, request: AnswerRequest) -> str:
        if request.mode == "computation":
            preface = (
                "This conversational turn performed retrieval only; I did not "
                "run repository code. Approved Phase 7 jobs and deterministic "
                "traces are available in "
                "the computation panel. Here is the indexed material most "
                "relevant to the request."
            )
        elif request.mode == "tutorial":
            preface = (
                "Here is a guided starting point through the most relevant "
                "repository material."
            )
        elif request.mode == "explanation":
            preface = (
                "Here are the source passages that most directly support an "
                "explanation of the question."
            )
        else:
            preface = (
                "Here are the strongest indexed findings for this research "
                "question."
            )

        if not request.sources:
            return (
                f"{preface}\n\nNo matching passage was found in the current "
                "lexical index. Try a shorter mathematical term, an exact quoted "
                "phrase, or a different topic scope."
            )

        sections = [preface]
        for index, source in enumerate(request.sources, start=1):
            heading = source.heading or "Source passage"
            compact_excerpt = re.sub(r"\s+", " ", source.excerpt).strip()
            status = source.mathematical_status.replace("_", " ")
            sections.append(
                f"### {index}. {heading} [{source.citation_id}]\n\n"
                f"{compact_excerpt}\n\n"
                f"Status: **{status}**  \n"
                f"`content/{source.path}:{source.start_line}-{source.end_line}`"
            )
        if request.mode == "tutorial":
            sections.append(
                "A useful next step is to open the first cited section, identify "
                "its definitions, and then compare them with the next retrieved "
                "passage."
            )
        return "\n\n".join(sections)

class UnavailableModelProvider:
    """Stable failure provider for unsupported or unconfigured selections."""

    def __init__(self, name: str, model: str) -> None:
        self.metadata = ProviderMetadata(
            name=name,
            model=model,
            configured=False,
            live=False,
        )

    def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
        del request
        self._raise()

    def refine(
        self,
        request: PlanningRequest,
        results: tuple[ToolResult, ...],
    ) -> tuple[ToolCall, ...]:
        del request, results
        self._raise()

    def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
        del request
        self._raise()

    def answer_annotations(
        self,
        request: AnswerRequest,
    ) -> tuple[ProvenanceAnnotation, ...]:
        del request
        self._raise()

    def _raise(self) -> None:
        raise ProviderUnavailableError(
            f"Model provider `{self.metadata.name}` is not configured in this "
            "Phase 7 build. Set CRAIG_MODEL_PROVIDER=demo to use the local "
            "retrieval demonstration."
        )


def provider_from_environment() -> ModelProvider:
    """Create the selected provider without reading or returning any secret."""

    name = os.environ.get("CRAIG_MODEL_PROVIDER", "demo").strip().casefold()
    model = os.environ.get("CRAIG_MODEL", "").strip()
    if name == "demo":
        return DemoModelProvider()
    return UnavailableModelProvider(
        name=name or "unconfigured",
        model=model or "unconfigured",
    )
