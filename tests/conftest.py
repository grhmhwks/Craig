from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def prevent_unintended_live_model_requests(
    request: pytest.FixtureRequest,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Make ordinary tests no-network even when a developer has a live .env."""

    if request.node.get_closest_marker("live_model") is None:
        monkeypatch.setenv("CRAIG_MODEL_PROVIDER", "demo")
