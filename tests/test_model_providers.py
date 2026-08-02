from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

import pytest

from craig.chat.errors import ProviderUnavailableError
from craig.chat.providers import (
    OpenAICompatibleProvider,
    UnavailableModelProvider,
    provider_from_environment,
)
from craig.evaluation import evaluate_provider


def _evaluation_answer(question: str) -> str:
    if "strict widget" in question:
        return "A strict widget is decreasing, as stated in [C-EVAL-1]."
    if "finite computation" in question:
        return "[C-EVAL-2] is a finite check and is not a proof for every n."
    return "The status is unknown in [C-EVAL-3], so it is not established as a theorem."


def _requester(
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
    timeout: float,
    max_bytes: int,
) -> dict[str, Any]:
    del timeout, max_bytes
    assert url.endswith("/v1/chat/completions")
    assert headers["Content-Type"] == "application/json"
    assert payload["stream"] is False
    context = json.loads(payload["messages"][1]["content"])
    return {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": _evaluation_answer(context["question"]),
                }
            }
        ]
    }


@pytest.mark.parametrize(
    ("tier", "model"),
    [("strong", "strong-test"), ("small", "small-test")],
)
def test_identical_strong_and_small_profiles_pass_the_release_contract(
    tier: str,
    model: str,
) -> None:
    provider = OpenAICompatibleProvider(
        name="local",
        model=model,
        base_url="http://127.0.0.1:11434/v1",
        api_key=None,
        data_destination="local_model",
        requester=_requester,
    )

    report = evaluate_provider(provider, tier=tier)  # type: ignore[arg-type]

    assert report["all_passed"] is True
    assert report["passed_cases"] == report["case_count"] == 3
    assert report["provider"]["model"] == model  # type: ignore[index]


def test_provider_environment_selection_is_explicit_and_secret_free(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "openai")
    monkeypatch.setenv("CRAIG_MODEL", "remote-test-model")
    monkeypatch.setenv("OPENAI_API_KEY", "secret-test-key")

    provider = provider_from_environment()
    metadata = provider.metadata

    assert metadata.name == "openai"
    assert metadata.model == "remote-test-model"
    assert metadata.configured is True
    assert metadata.live is True
    assert metadata.data_destination == "remote_model"
    assert "secret-test-key" not in json.dumps(
        {
            "name": metadata.name,
            "model": metadata.model,
            "configured": metadata.configured,
            "live": metadata.live,
            "data_destination": metadata.data_destination,
        }
    )


def test_missing_or_unsafe_provider_configuration_is_unavailable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "openai")
    monkeypatch.setenv("CRAIG_MODEL", "model")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    missing_key = provider_from_environment()
    assert isinstance(missing_key, UnavailableModelProvider)

    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "local")
    monkeypatch.setenv("CRAIG_MODEL_BASE_URL", "http://example.com/v1")
    unsafe_local = provider_from_environment()
    assert isinstance(unsafe_local, UnavailableModelProvider)
    with pytest.raises(ProviderUnavailableError, match="loopback"):
        tuple(unsafe_local.stream_answer(None))  # type: ignore[arg-type]


def test_provider_rejects_malformed_completion_payload() -> None:
    provider = OpenAICompatibleProvider(
        name="local",
        model="test",
        base_url="http://localhost:1234/v1",
        api_key=None,
        data_destination="local_model",
        requester=lambda *_: {"choices": []},
    )

    with pytest.raises(ProviderUnavailableError, match="completion choice"):
        provider._response_text({"choices": []})


def test_real_loopback_http_transport_uses_bounded_chat_completions() -> None:
    received: list[dict[str, Any]] = []

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802
            length = int(self.headers["Content-Length"])
            payload = json.loads(self.rfile.read(length))
            received.append(payload)
            context = json.loads(payload["messages"][1]["content"])
            body = json.dumps(
                {
                    "choices": [
                        {
                            "message": {
                                "role": "assistant",
                                "content": _evaluation_answer(context["question"]),
                            }
                        }
                    ]
                }
            ).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: object) -> None:
            del format, args

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        provider = OpenAICompatibleProvider(
            name="local",
            model="loopback-test",
            base_url=f"http://127.0.0.1:{server.server_port}/v1",
            api_key=None,
            data_destination="local_model",
            timeout_seconds=3,
        )
        report = evaluate_provider(provider, tier="small")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)

    assert report["all_passed"] is True
    assert len(received) == 3
    assert all(payload["model"] == "loopback-test" for payload in received)
    assert all(payload["max_tokens"] == 2_000 for payload in received)


def test_loopback_transport_refuses_http_redirects() -> None:
    paths: list[str] = []

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802
            paths.append(self.path)
            self.send_response(302)
            self.send_header(
                "Location",
                f"http://127.0.0.1:{self.server.server_port}/leaked",
            )
            self.end_headers()

        def do_GET(self) -> None:  # noqa: N802
            paths.append(self.path)
            self.send_response(500)
            self.end_headers()

        def log_message(self, format: str, *args: object) -> None:
            del format, args

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        provider = OpenAICompatibleProvider(
            name="local",
            model="redirect-test",
            base_url=f"http://127.0.0.1:{server.server_port}/v1",
            api_key=None,
            data_destination="local_model",
            timeout_seconds=3,
        )
        with pytest.raises(ProviderUnavailableError, match="HTTP 302"):
            evaluate_provider(provider, tier="small")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)

    assert paths == ["/v1/chat/completions"]
