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
    health_payload = health.json()
    assert health_payload["schema_version"] == 1
    assert health_payload["version"] == "1.0.0"
    assert health_payload["content_available"] is True
    assert health_payload["index_available"] is True
    assert health_payload["corpus_access"] == "read_only"
    assert health_payload["conversation_storage"] == "memory"
    assert health_payload["provider"]["data_destination"] == "none"
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


def test_health_degrades_when_selected_provider_is_unavailable(
    api: tuple[FastAPI, Path],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    existing_app, _ = api
    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "not-configured")
    app = create_app(existing_app.state.retrieval_service.config)

    response = _request(app, "GET", "/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "degraded"
    assert response.json()["provider"]["configured"] is False


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


def test_production_frontend_mount_preserves_api_routes(
    api: tuple[FastAPI, Path],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    existing_app, _ = api
    frontend_dist = tmp_path / "frontend-dist"
    frontend_dist.mkdir()
    (frontend_dist / "index.html").write_text(
        "<!doctype html><title>CRAIG frontend smoke</title>",
        encoding="utf-8",
    )
    monkeypatch.setenv("CRAIG_FRONTEND_DIST", str(frontend_dist))
    app = create_app(existing_app.state.retrieval_service.config)

    home = _request(app, "GET", "/")
    chat_config = _request(app, "GET", "/api/v1/chat/config")

    assert home.status_code == 200
    assert "CRAIG frontend smoke" in home.text
    assert chat_config.status_code == 200
    assert chat_config.json()["stream_transport"] == "sse"
