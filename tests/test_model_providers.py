from __future__ import annotations

import json
import threading
import urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from typing import Any

import pytest

from craig.chat.errors import ProviderUnavailableError
from craig.chat.models import ToolResult
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


def test_groq_environment_selection_uses_fixed_remote_provider(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    requests: list[tuple[str, dict[str, Any], dict[str, str]]] = []

    def request_groq(
        url: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout: float,
        max_bytes: int,
    ) -> dict[str, Any]:
        del timeout, max_bytes
        requests.append((url, payload, headers))
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

    monkeypatch.setattr("craig.chat.providers._post_json", request_groq)
    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "groq")
    monkeypatch.setenv("CRAIG_MODEL", "qwen/qwen3.6-27b")
    monkeypatch.setenv("GROQ_API_KEY", "secret-groq-test-key")

    provider = provider_from_environment()

    assert isinstance(provider, OpenAICompatibleProvider)
    assert provider.metadata.name == "groq"
    assert provider.metadata.model == "qwen/qwen3.6-27b"
    assert provider.metadata.data_destination == "remote_model"
    assert provider.base_url == "https://api.groq.com/openai/v1"
    assert provider.token_parameter == "max_completion_tokens"
    assert evaluate_provider(provider, tier="strong")["all_passed"] is True
    assert len(requests) == 3
    assert all(
        url == "https://api.groq.com/openai/v1/chat/completions"
        for url, _, _ in requests
    )
    assert all(
        payload["max_completion_tokens"] == 2_000
        and "max_tokens" not in payload
        for _, payload, _ in requests
    )
    assert all(
        headers["Authorization"] == "Bearer secret-groq-test-key"
        for _, _, headers in requests
    )
    assert "secret-groq-test-key" not in json.dumps(
        {
            "name": provider.metadata.name,
            "model": provider.metadata.model,
            "configured": provider.metadata.configured,
            "live": provider.metadata.live,
            "data_destination": provider.metadata.data_destination,
        }
    )


def test_cloudflare_environment_selection_uses_account_scoped_fixed_provider(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    requests: list[tuple[str, dict[str, Any], dict[str, str]]] = []

    def request_cloudflare(
        url: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout: float,
        max_bytes: int,
    ) -> dict[str, Any]:
        del timeout, max_bytes
        requests.append((url, payload, headers))
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

    account_id = "0123456789abcdef0123456789abcdef"
    monkeypatch.setattr("craig.chat.providers._post_json", request_cloudflare)
    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "cloudflare")
    monkeypatch.setenv("CRAIG_MODEL", "@cf/qwen/qwen3-30b-a3b-fp8")
    monkeypatch.setenv("CLOUDFLARE_ACCOUNT_ID", account_id)
    monkeypatch.setenv("CLOUDFLARE_API_TOKEN", "secret-cloudflare-test-token")

    provider = provider_from_environment()

    assert isinstance(provider, OpenAICompatibleProvider)
    assert provider.metadata.name == "cloudflare"
    assert provider.metadata.model == "@cf/qwen/qwen3-30b-a3b-fp8"
    assert provider.metadata.data_destination == "remote_model"
    assert provider.base_url == (
        f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1"
    )
    assert provider.token_parameter == "max_tokens"
    assert evaluate_provider(provider, tier="strong")["all_passed"] is True
    assert len(requests) == 3
    assert all(
        url
        == (
            "https://api.cloudflare.com/client/v4/accounts/"
            f"{account_id}/ai/v1/chat/completions"
        )
        for url, _, _ in requests
    )
    assert all(
        payload["max_tokens"] == 2_000
        and "max_completion_tokens" not in payload
        for _, payload, _ in requests
    )
    assert all(
        headers["Authorization"] == "Bearer secret-cloudflare-test-token"
        for _, _, headers in requests
    )
    assert "secret-cloudflare-test-token" not in json.dumps(
        {
            "name": provider.metadata.name,
            "model": provider.metadata.model,
            "configured": provider.metadata.configured,
            "live": provider.metadata.live,
            "data_destination": provider.metadata.data_destination,
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

    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "groq")
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    missing_groq_key = provider_from_environment()
    assert isinstance(missing_groq_key, UnavailableModelProvider)
    with pytest.raises(ProviderUnavailableError, match="GROQ_API_KEY"):
        tuple(missing_groq_key.stream_answer(None))  # type: ignore[arg-type]

    monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "cloudflare")
    monkeypatch.setenv("CLOUDFLARE_ACCOUNT_ID", "not-an-account-id")
    monkeypatch.setenv("CLOUDFLARE_API_TOKEN", "secret-token")
    invalid_cloudflare_account = provider_from_environment()
    assert isinstance(invalid_cloudflare_account, UnavailableModelProvider)
    with pytest.raises(ProviderUnavailableError, match="32-character hexadecimal"):
        tuple(invalid_cloudflare_account.stream_answer(None))  # type: ignore[arg-type]

    monkeypatch.setenv(
        "CLOUDFLARE_ACCOUNT_ID", "0123456789abcdef0123456789abcdef"
    )
    monkeypatch.delenv("CLOUDFLARE_API_TOKEN", raising=False)
    missing_cloudflare_token = provider_from_environment()
    assert isinstance(missing_cloudflare_token, UnavailableModelProvider)
    with pytest.raises(ProviderUnavailableError, match="CLOUDFLARE_API_TOKEN"):
        tuple(missing_cloudflare_token.stream_answer(None))  # type: ignore[arg-type]


def test_retrieval_refinement_expands_multiple_distinct_ranked_sources() -> None:
    results = (
        ToolResult(
            call_id="search",
            name="search_content",
            arguments={},
            output={
                "results": [
                    {
                        "path": f"topic/source-{index}.tex",
                        "start_line": index * 10 + 1,
                        "end_line": index * 10 + 9,
                    }
                    for index in range(5)
                ]
            },
            success=True,
        ),
    )

    calls = OpenAICompatibleProvider(
        name="local",
        model="test",
        base_url="http://127.0.0.1:11434/v1",
        api_key=None,
        data_destination="local_model",
        requester=_requester,
    ).refine(None, results)  # type: ignore[arg-type]

    assert len(calls) == 4
    assert all(call.name == "read_source" for call in calls)
    assert [call.arguments["path"] for call in calls] == [
        f"topic/source-{index}.tex" for index in range(4)
    ]


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


def test_loopback_transport_refuses_http_redirects(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    urls: list[str] = []

    class RedirectingOpener:
        def open(self, request: Any, *, timeout: float) -> None:
            del timeout
            urls.append(request.full_url)
            raise urllib.error.HTTPError(
                request.full_url,
                302,
                "Found",
                {"Location": "http://127.0.0.1:9999/leaked"},
                BytesIO(),
            )

    monkeypatch.setattr(
        "craig.chat.providers.urllib.request.build_opener",
        lambda *_: RedirectingOpener(),
    )
    provider = OpenAICompatibleProvider(
        name="local",
        model="redirect-test",
        base_url="http://127.0.0.1:1234/v1",
        api_key=None,
        data_destination="local_model",
        timeout_seconds=3,
    )

    with pytest.raises(ProviderUnavailableError, match="HTTP 302"):
        evaluate_provider(provider, tier="small")

    assert urls == ["http://127.0.0.1:1234/v1/chat/completions"]


def test_transport_reports_rate_limits_without_exposing_response_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class RateLimitedOpener:
        def open(self, request: Any, *, timeout: float) -> None:
            del timeout
            raise urllib.error.HTTPError(
                request.full_url,
                429,
                "Too Many Requests",
                {"x-request-id": "safe-request-id"},
                BytesIO(b"provider-internal-quota-details"),
            )

    monkeypatch.setattr(
        "craig.chat.providers.urllib.request.build_opener",
        lambda *_: RateLimitedOpener(),
    )
    provider = OpenAICompatibleProvider(
        name="local",
        model="rate-limit-test",
        base_url="http://127.0.0.1:1234/v1",
        api_key=None,
        data_destination="local_model",
        timeout_seconds=3,
    )
    with pytest.raises(ProviderUnavailableError) as captured:
        evaluate_provider(provider, tier="small")

    message = str(captured.value)
    assert "request limit was reached" in message
    assert "safe-request-id" in message
    assert "provider-internal-quota-details" not in message
