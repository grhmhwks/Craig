from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import anyio
import httpx
import pytest

from craig.api import create_app
from craig.chat.errors import InvalidChatRequest
from craig.chat.models import (
    AnswerRequest,
    ChatEvent,
    PlanningRequest,
    ProvenanceAnnotation,
    ToolCall,
    ToolResult,
)
from craig.chat.providers import (
    DemoModelProvider,
    ProviderMetadata,
    UnavailableModelProvider,
)
from craig.chat.service import ChatService, PreparedTurn
from craig.index import index_repository
from craig.retrieval import RetrievalConfig, RetrievalService


def _write(content: Path, relative_path: str, text: str) -> Path:
    path = content / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


@pytest.fixture
def chat(tmp_path: Path) -> tuple[ChatService, RetrievalConfig, Path]:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    _write(
        content,
        "alpha/explanation.tex",
        (
            "\\section{Strict widgets}\n"
            "A strict widget has decreasing positive parts.\n"
            "\\begin{lemma}[Dominance]\n"
            "Every nonzero lattice widget has strictly dominant weight.\n"
            "\\end{lemma}\n"
        ),
    )
    _write(
        content,
        "beta/notes.md",
        "# Other widgets\nA separate construction uses weak widgets.\n",
    )
    index_repository(content, database)
    config = RetrievalConfig(
        content_root=content,
        database_path=database,
    )
    service = ChatService(
        RetrievalService(config),
        provider=DemoModelProvider(),
    )
    return service, config, content


def _run_turn(
    service: ChatService,
    *,
    message: str = "Explain strict dominant weight",
    mode: str = "explanation",
    topic: str | None = "alpha",
    conversation_id: str | None = None,
) -> tuple[PreparedTurn, list[ChatEvent]]:
    turn = service.prepare(
        message=message,
        mode=mode,
        topic=topic,
        conversation_id=conversation_id,
    )
    return turn, list(service.stream(turn))


def test_chat_orchestration_streams_tools_text_and_sources(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    service, _, _ = chat

    turn, events = _run_turn(service)

    event_types = [event.type for event in events]
    assert event_types[:3] == [
        "conversation.created",
        "message.accepted",
        "status",
    ]
    assert [event.data["name"] for event in events if event.type == "tool.call"] == [
        "search_content",
        "read_source",
        "read_source",
    ]
    assert "text.delta" in event_types
    assert event_types[-1] == "message.completed"
    completed = events[-1].data["message"]
    assert completed["role"] == "assistant"
    assert completed["sources"]
    assert completed["sources"][0]["topic"] == "alpha"
    assert completed["sources"][0]["citation_id"].startswith("C-")
    assert completed["sources"][0]["excerpt"]
    assert completed["sources"][0]["mathematical_status"] == "proved_result"
    assert completed["sources"][0]["citation_id"] in completed["content"]
    assert [note["kind"] for note in completed["provenance"]] == [
        "repository",
        "deduction",
    ]
    snapshot = service.store.get(turn.conversation_id)
    assert [message.role for message in snapshot.messages] == ["user", "assistant"]
    assert snapshot.messages[-1].provenance


def test_follow_up_preserves_in_memory_context(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    service, _, _ = chat
    first, _ = _run_turn(service)
    first_snapshot = service.store.get(first.conversation_id)
    first_citation = first_snapshot.messages[-1].sources[0].citation_id

    second, events = _run_turn(
        service,
        message="Where is that lemma stated?",
        mode="research",
        conversation_id=first.conversation_id,
    )

    assert second.conversation_id == first.conversation_id
    assert events[0].type == "conversation.resumed"
    snapshot = service.store.get(first.conversation_id)
    assert len(snapshot.messages) == 4
    assert snapshot.mode == "research"
    assert snapshot.messages[-2].content == "Where is that lemma stated?"
    assert snapshot.messages[1].sources[0].citation_id == first_citation
    assert snapshot.messages[1].provenance


def test_provider_receives_separate_prompts_and_follow_up_context(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    _, config, _ = chat

    class RecordingProvider:
        metadata = ProviderMetadata(
            name="recording",
            model="test",
            configured=True,
            live=False,
        )

        def __init__(self) -> None:
            self.planning: list[PlanningRequest] = []
            self.answers: list[AnswerRequest] = []

        def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
            self.planning.append(request)
            return ()

        def refine(
            self,
            request: PlanningRequest,
            results: tuple[ToolResult, ...],
        ) -> tuple[ToolCall, ...]:
            del request, results
            return ()

        def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
            self.answers.append(request)
            yield "Grounded test response."

        def answer_annotations(
            self,
            request: AnswerRequest,
        ) -> tuple[ProvenanceAnnotation, ...]:
            del request
            return ()

    provider = RecordingProvider()
    service = ChatService(
        RetrievalService(config),
        provider=provider,
    )
    first, _ = _run_turn(service)
    _run_turn(
        service,
        message="Follow up on that result",
        conversation_id=first.conversation_id,
    )

    assert provider.planning[0].system_prompt.startswith(
        "Role: plan read-only retrieval"
    )
    assert provider.answers[0].system_prompt.startswith("Role: answer as CRAIG")
    assert provider.planning[0].system_prompt != provider.answers[0].system_prompt
    assert "`unknown` must remain unknown" in provider.answers[0].system_prompt
    assert "exhaustive finite check" in provider.answers[0].system_prompt
    assert "Do not turn finite evidence into a general proof" in (
        provider.answers[0].system_prompt
    )
    assert "`tableau`" in provider.answers[0].system_prompt
    assert "`dyck-path`" in provider.answers[0].system_prompt
    assert "never emit raw HTML or SVG" in provider.answers[0].system_prompt
    assert "Do not invent mathematical data" in provider.answers[0].system_prompt
    assert [message.role for message in provider.planning[1].conversation.messages] == [
        "user",
        "assistant",
        "user",
    ]


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("research", "strongest indexed findings"),
        ("explanation", "source passages"),
        ("tutorial", "guided starting point"),
        ("computation", "I did not run repository code"),
    ],
)
def test_modes_change_the_answer_profile(
    chat: tuple[ChatService, RetrievalConfig, Path],
    mode: str,
    expected: str,
) -> None:
    service, _, _ = chat

    _, events = _run_turn(service, mode=mode)

    answer = events[-1].data["message"]["content"]
    assert expected in answer
    provenance_kinds = {
        note["kind"] for note in events[-1].data["message"]["provenance"]
    }
    assert "repository" in provenance_kinds
    assert "deduction" in provenance_kinds
    if mode == "tutorial":
        assert "model_knowledge" in provenance_kinds
    else:
        assert "model_knowledge" not in provenance_kinds


def test_chat_validation_rejects_bad_scope_and_oversized_messages(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    service, _, _ = chat

    with pytest.raises(InvalidChatRequest):
        service.prepare(
            message="question",
            mode="unknown",
            topic=None,
            conversation_id=None,
        )
    with pytest.raises(InvalidChatRequest):
        service.prepare(
            message="question",
            mode="research",
            topic="missing",
            conversation_id=None,
        )
    with pytest.raises(InvalidChatRequest):
        service.prepare(
            message="x" * (service.config.max_message_chars + 1),
            mode="research",
            topic=None,
            conversation_id=None,
        )


def test_public_config_never_exposes_environment_secrets(
    chat: tuple[ChatService, RetrievalConfig, Path],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    service, _, _ = chat
    monkeypatch.setenv("OPENAI_API_KEY", "do-not-return-this-value")

    payload = json.dumps(service.public_config())

    assert "do-not-return-this-value" not in payload
    assert service.public_config()["provider"] == {
        "name": "demo",
        "model": "deterministic-retrieval",
        "configured": True,
        "live": False,
        "data_destination": "none",
    }


def test_unavailable_provider_emits_a_typed_stream_error(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    _, config, _ = chat
    service = ChatService(
        RetrievalService(config),
        provider=UnavailableModelProvider("remote", "unconfigured"),
    )
    turn = service.prepare(
        message="Explain widgets",
        mode="explanation",
        topic=None,
        conversation_id=None,
    )

    events = list(service.stream(turn))

    assert events[-1].type == "error"
    assert events[-1].data["code"] == "chat_failed"
    assert "not configured" in events[-1].data["message"]


def test_external_provenance_is_suppressed_while_external_tools_are_disabled(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    _, config, _ = chat

    class AnnotatingProvider:
        metadata = ProviderMetadata(
            name="annotating",
            model="test",
            configured=True,
            live=False,
        )

        def plan(self, request: PlanningRequest) -> tuple[ToolCall, ...]:
            del request
            return ()

        def refine(
            self,
            request: PlanningRequest,
            results: tuple[ToolResult, ...],
        ) -> tuple[ToolCall, ...]:
            del request, results
            return ()

        def stream_answer(self, request: AnswerRequest) -> Iterator[str]:
            del request
            yield "Provider response."

        def answer_annotations(
            self,
            request: AnswerRequest,
        ) -> tuple[ProvenanceAnnotation, ...]:
            del request
            return (
                ProvenanceAnnotation(
                    kind="external",
                    description="Disabled external material.",
                ),
                ProvenanceAnnotation(
                    kind="model_knowledge",
                    description="General provider knowledge.",
                ),
            )

    service = ChatService(
        RetrievalService(config),
        provider=AnnotatingProvider(),
    )
    _, events = _run_turn(service)

    provenance = events[-1].data["message"]["provenance"]
    assert [annotation["kind"] for annotation in provenance] == [
        "model_knowledge"
    ]


def _request(
    app: Any,
    method: str,
    url: str,
    *,
    json_body: dict[str, Any] | None = None,
) -> httpx.Response:
    async def send() -> httpx.Response:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://testserver",
        ) as client:
            kwargs = {"json": json_body} if json_body is not None else {}
            return await client.request(method, url, **kwargs)

    return anyio.run(send)


def _sse_events(response: httpx.Response) -> list[dict[str, Any]]:
    events = []
    for block in response.text.split("\n\n"):
        data_line = next(
            (line for line in block.splitlines() if line.startswith("data: ")),
            None,
        )
        if data_line:
            events.append(json.loads(data_line.removeprefix("data: ")))
    return events


def test_chat_http_sse_contract_and_conversation_lookup(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    service, config, _ = chat
    app = create_app(config, chat_service=service)

    configuration = _request(app, "GET", "/api/v1/chat/config")
    stream = _request(
        app,
        "POST",
        "/api/v1/chat/stream",
        json_body={
            "message": "Explain strict dominant weight",
            "mode": "explanation",
            "topic": "alpha",
        },
    )

    assert configuration.status_code == 200
    assert "OPENAI_API_KEY" not in configuration.text
    assert configuration.json()["max_source_excerpt_chars"] == 1600
    assert configuration.json()["external_sources_enabled"] is False
    assert stream.status_code == 200
    assert stream.headers["content-type"].startswith("text/event-stream")
    events = _sse_events(stream)
    assert events[0]["type"] == "conversation.created"
    assert events[-1]["type"] == "message.completed"
    source_event = next(event for event in events if event["type"] == "sources.ready")
    assert source_event["data"]["sources"][0]["citation_id"].startswith("C-")
    assert source_event["data"]["sources"][0]["excerpt"]
    assert source_event["data"]["provenance"][0]["kind"] == "repository"
    conversation_id = events[0]["conversation_id"]
    lookup = _request(
        app,
        "GET",
        f"/api/v1/conversations/{conversation_id}",
    )
    assert lookup.status_code == 200
    assert len(lookup.json()["messages"]) == 2
    assert lookup.json()["messages"][-1]["sources"][0]["status_basis"]
    assert lookup.json()["messages"][-1]["provenance"]
    openapi = _request(app, "GET", "/openapi.json").json()
    source_schema = openapi["components"]["schemas"]["SourceReferenceResponse"]
    assert {
        "citation_id",
        "excerpt",
        "mathematical_status",
        "status_basis",
    }.issubset(source_schema["properties"])
    message_schema = openapi["components"]["schemas"]["ChatMessageResponse"]
    assert "provenance" in message_schema["properties"]


def test_conflicting_conventions_keep_separate_global_citations(
    tmp_path: Path,
) -> None:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    _write(
        content,
        "ascending/explanation.tex",
        (
            "\\section{Widget conventions}\n"
            "\\begin{definition}[Ascending convention]\n"
            "A widget word is read from left to right.\n"
            "\\end{definition}\n"
        ),
    )
    _write(
        content,
        "descending/explanation.tex",
        (
            "\\section{Widget conventions}\n"
            "\\begin{definition}[Descending convention]\n"
            "A widget word is read from right to left.\n"
            "\\end{definition}\n"
        ),
    )
    index_repository(content, database)
    service = ChatService(
        RetrievalService(
            RetrievalConfig(
                content_root=content,
                database_path=database,
            )
        ),
        provider=DemoModelProvider(),
    )

    _, events = _run_turn(
        service,
        message="widget",
        mode="research",
        topic=None,
    )
    completed = events[-1].data["message"]
    sources = completed["sources"]

    assert {source["topic"] for source in sources} == {"ascending", "descending"}
    assert len({source["citation_id"] for source in sources}) == len(sources)
    combined_excerpts = " ".join(source["excerpt"] for source in sources)
    assert "left to right" in combined_excerpts
    assert "right to left" in combined_excerpts
    assert all(source["mathematical_status"] == "unknown" for source in sources)
    assert all(
        source["citation_id"] in completed["content"] for source in sources
    )
    assert "Ascending convention" in completed["content"]
    assert "Descending convention" in completed["content"]


def test_multiple_ranked_passages_are_expanded_before_generation(
    tmp_path: Path,
) -> None:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    for topic, label in (("first", "alpha context"), ("second", "beta context")):
        _write(
            content,
            f"{topic}/explanation.tex",
            (
                f"\\section{{{label}}}\n"
                f"This opening sentence supplies the full {label}.\n"
                "Several definitions and qualifications belong to this passage.\n"
                "The distinctive retrieval marker appears at the end.\n"
            ),
        )
    index_repository(content, database)
    service = ChatService(
        RetrievalService(
            RetrievalConfig(
                content_root=content,
                database_path=database,
            )
        ),
        provider=DemoModelProvider(),
    )

    _, events = _run_turn(
        service,
        message="retrieval marker",
        mode="research",
        topic=None,
    )

    read_calls = [
        event.data["arguments"]["path"]
        for event in events
        if event.type == "tool.call" and event.data["name"] == "read_source"
    ]
    completed = events[-1].data["message"]
    assert set(read_calls) == {
        "first/explanation.tex",
        "second/explanation.tex",
    }
    assert {
        source["excerpt"].splitlines()[0] for source in completed["sources"]
    } == {"\\section{alpha context}", "\\section{beta context}"}


def test_explicit_status_structure_survives_chat_stream(
    tmp_path: Path,
) -> None:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    _write(
        content,
        "status/explanation.tex",
        (
            "\\section{Computational evidence}\n"
            "A marker was observed in a finite calculation.\n"
            "\\begin{conjecture}[Marker conjecture]\n"
            "The marker should occur in every rank.\n"
            "\\end{conjecture}\n"
            "\\begin{theorem}[Marker theorem]\n"
            "The marker occurs in rank one.\n"
            "\\end{theorem}\n"
        ),
    )
    index_repository(content, database)
    service = ChatService(
        RetrievalService(
            RetrievalConfig(
                content_root=content,
                database_path=database,
            )
        ),
        provider=DemoModelProvider(),
    )

    _, events = _run_turn(
        service,
        message="marker",
        mode="research",
        topic="status",
    )
    sources = events[-1].data["message"]["sources"]
    statuses_by_environment = {
        source["environment"]: source["mathematical_status"]
        for source in sources
    }

    assert statuses_by_environment["section"] == "computational_evidence"
    assert statuses_by_environment["conjecture"] == "conjecture"
    assert statuses_by_environment["theorem"] == "proved_result"


def test_chat_http_operations_leave_content_unchanged(
    chat: tuple[ChatService, RetrievalConfig, Path],
) -> None:
    service, config, content = chat
    app = create_app(config, chat_service=service)
    before = {
        path.relative_to(content).as_posix(): path.read_bytes()
        for path in content.rglob("*")
        if path.is_file()
    }

    response = _request(
        app,
        "POST",
        "/api/v1/chat/stream",
        json_body={
            "message": "Research strict widgets",
            "mode": "research",
        },
    )

    after = {
        path.relative_to(content).as_posix(): path.read_bytes()
        for path in content.rglob("*")
        if path.is_file()
    }
    assert response.status_code == 200
    assert after == before
