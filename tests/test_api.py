from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("fastapi")
pytest.importorskip("httpx")

from fastapi.testclient import TestClient

from craig.api import create_app
from craig.index import index_repository
from craig.retrieval import RetrievalConfig


def _write(content: Path, relative_path: str, text: str) -> Path:
    path = content / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


@pytest.fixture
def api(tmp_path: Path) -> tuple[TestClient, Path]:
    content = tmp_path / "content"
    database = tmp_path / ".craig" / "index.sqlite3"
    _write(
        content,
        "topic/explanation.tex",
        "\\section{API}\nA bounded retrieval result.\n",
    )
    index_repository(content, database)
    app = create_app(
        RetrievalConfig(
            content_root=content,
            database_path=database,
        )
    )
    return TestClient(app), content


def test_health_topics_and_search_contract(
    api: tuple[TestClient, Path],
) -> None:
    client, _ = api

    health = client.get("/api/v1/health")
    topics = client.get("/api/v1/topics")
    search = client.post("/api/v1/search", json={"query": "bounded"})

    assert health.status_code == 200
    assert health.json() == {
        "schema_version": 1,
        "status": "ok",
        "topic_count": 1,
    }
    assert topics.status_code == 200
    assert topics.json()["topics"][0]["topic"] == "topic"
    assert search.status_code == 200
    result = search.json()["results"][0]
    assert result["path"] == "topic/explanation.tex"
    assert result["file_type"] == ".tex"
    assert result["environment"] == "section"
    assert len(result["file_hash"]) == 64

    openapi = client.get("/openapi.json")
    assert openapi.status_code == 200
    search_schema = openapi.json()["paths"]["/api/v1/search"]["post"][
        "responses"
    ]["200"]["content"]["application/json"]["schema"]
    assert search_schema["$ref"].endswith("/SearchPageResponse")


def test_exact_and_source_endpoints(
    api: tuple[TestClient, Path],
) -> None:
    client, _ = api

    exact = client.post(
        "/api/v1/find-exact",
        json={"query": "bounded retrieval", "context_lines": 0},
    )
    source = client.post(
        "/api/v1/read-source",
        json={
            "path": "topic/explanation.tex",
            "start_line": 1,
            "end_line": 2,
        },
    )

    assert exact.status_code == 200
    assert exact.json()["results"][0]["match_start_line"] == 2
    assert source.status_code == 200
    assert source.json()["text"] == (
        "\\section{API}\nA bounded retrieval result.\n"
    )


def test_api_maps_validation_and_path_security_errors(
    api: tuple[TestClient, Path],
) -> None:
    client, _ = api

    invalid = client.post(
        "/api/v1/search",
        json={"query": "bounded", "unexpected": True},
    )
    traversal = client.post(
        "/api/v1/read-source",
        json={"path": "../outside.tex"},
    )

    assert invalid.status_code == 422
    assert invalid.json()["error"]["code"] == "validation_error"
    assert traversal.status_code == 422
    assert traversal.json()["error"]["code"] == "unsafe_source_path"


def test_api_retrieval_does_not_modify_content(
    api: tuple[TestClient, Path],
) -> None:
    client, content = api
    before = {
        path.relative_to(content).as_posix(): path.read_bytes()
        for path in content.rglob("*")
        if path.is_file()
    }

    client.get("/api/v1/topics")
    client.post("/api/v1/search", json={"query": "bounded"})
    client.post("/api/v1/find-exact", json={"query": "bounded"})
    client.post(
        "/api/v1/read-source",
        json={"path": "topic/explanation.tex"},
    )

    after = {
        path.relative_to(content).as_posix(): path.read_bytes()
        for path in content.rglob("*")
        if path.is_file()
    }
    assert after == before
