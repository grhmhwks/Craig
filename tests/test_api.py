from __future__ import annotations

from pathlib import Path
from typing import Any

import anyio
import httpx
import pytest

pytest.importorskip("fastapi")
pytest.importorskip("httpx")

from fastapi import FastAPI

from craig.api import create_app
from craig.index import index_repository
from craig.retrieval import RetrievalConfig


def _write(content: Path, relative_path: str, text: str) -> Path:
    path = content / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _request(
    app: FastAPI,
    method: str,
    url: str,
    *,
    json: dict[str, Any] | None = None,
) -> httpx.Response:
    async def send() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://testserver",
        ) as client:
            kwargs = {"json": json} if json is not None else {}
            return await client.request(method, url, **kwargs)

    return anyio.run(send)


@pytest.fixture
def api(tmp_path: Path) -> tuple[FastAPI, Path]:
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
    return app, content


def test_health_topics_and_search_contract(
    api: tuple[FastAPI, Path],
) -> None:
    app, _ = api

    health = _request(app, "GET", "/api/v1/health")
    topics = _request(app, "GET", "/api/v1/topics")
    search = _request(
        app,
        "POST",
        "/api/v1/search",
        json={"query": "bounded"},
    )

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

    openapi = _request(app, "GET", "/openapi.json")
    assert openapi.status_code == 200
    search_schema = openapi.json()["paths"]["/api/v1/search"]["post"][
        "responses"
    ]["200"]["content"]["application/json"]["schema"]
    assert search_schema["$ref"].endswith("/SearchPageResponse")


def test_exact_and_source_endpoints(
    api: tuple[FastAPI, Path],
) -> None:
    app, content = api

    exact = _request(
        app,
        "POST",
        "/api/v1/find-exact",
        json={"query": "bounded retrieval", "context_lines": 0},
    )
    source = _request(
        app,
        "POST",
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
    expected = (content / "topic" / "explanation.tex").read_bytes().decode("utf-8")
    assert source.json()["text"] == expected


def test_api_maps_validation_and_path_security_errors(
    api: tuple[FastAPI, Path],
) -> None:
    app, _ = api

    invalid = _request(
        app,
        "POST",
        "/api/v1/search",
        json={"query": "bounded", "unexpected": True},
    )
    traversal = _request(
        app,
        "POST",
        "/api/v1/read-source",
        json={"path": "../outside.tex"},
    )

    assert invalid.status_code == 422
    assert invalid.json()["error"]["code"] == "validation_error"
    assert traversal.status_code == 422
    assert traversal.json()["error"]["code"] == "unsafe_source_path"


def test_api_retrieval_does_not_modify_content(
    api: tuple[FastAPI, Path],
) -> None:
    app, content = api
    before = {
        path.relative_to(content).as_posix(): path.read_bytes()
        for path in content.rglob("*")
        if path.is_file()
    }

    _request(app, "GET", "/api/v1/topics")
    _request(app, "POST", "/api/v1/search", json={"query": "bounded"})
    _request(app, "POST", "/api/v1/find-exact", json={"query": "bounded"})
    _request(
        app,
        "POST",
        "/api/v1/read-source",
        json={"path": "topic/explanation.tex"},
    )

    after = {
        path.relative_to(content).as_posix(): path.read_bytes()
        for path in content.rglob("*")
        if path.is_file()
    }
    assert after == before
