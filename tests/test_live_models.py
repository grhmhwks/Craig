from __future__ import annotations

import os

import pytest

from craig.chat.providers import provider_from_environment
from craig.evaluation import evaluate_provider


@pytest.mark.live_model
@pytest.mark.parametrize("tier", ["strong", "small"])
def test_opt_in_live_model_profile(
    tier: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    if os.environ.get("CRAIG_RUN_LIVE_MODEL_EVALS") != "1":
        pytest.skip("Set CRAIG_RUN_LIVE_MODEL_EVALS=1 to authorize live requests.")
    variable = f"CRAIG_EVAL_{tier.upper()}_MODEL"
    model = os.environ.get(variable, "").strip()
    if not model:
        pytest.skip(f"Set {variable} to select the {tier} model.")
    monkeypatch.setenv("CRAIG_MODEL", model)
    provider = provider_from_environment()
    if not provider.metadata.configured or not provider.metadata.live:
        pytest.fail("A live CRAIG_MODEL_PROVIDER must be configured.")

    report = evaluate_provider(provider, tier=tier)  # type: ignore[arg-type]

    assert report["all_passed"] is True
