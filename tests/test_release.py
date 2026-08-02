from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from craig import __version__
from craig.config import MAX_ENVIRONMENT_FILE_BYTES, load_environment_file
from craig.doctor import run_doctor
from craig.retrieval import RetrievalConfig


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


def test_environment_file_is_literal_bounded_and_does_not_override_process(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = tmp_path / ".env"
    path.write_text(
        "# comment\nexport CRAIG_TEST_ONE='literal value'\n"
        'CRAIG_TEST_TWO="$(not-executed)"\n',
        encoding="utf-8",
    )
    monkeypatch.setenv("CRAIG_TEST_ONE", "process wins")

    loaded = load_environment_file(path)

    assert loaded == ("CRAIG_TEST_TWO",)
    assert os.environ["CRAIG_TEST_ONE"] == "process wins"
    assert os.environ["CRAIG_TEST_TWO"] == "$(not-executed)"


@pytest.mark.parametrize("text", ["NOT_AN_ASSIGNMENT", "1BAD=value", "A='open"])
def test_environment_file_rejects_invalid_assignments(
    tmp_path: Path,
    text: str,
) -> None:
    path = tmp_path / ".env"
    path.write_text(text, encoding="utf-8")

    with pytest.raises(ValueError):
        load_environment_file(path)


def test_environment_file_rejects_oversized_input(tmp_path: Path) -> None:
    path = tmp_path / ".env"
    path.write_bytes(b"A=" + b"x" * MAX_ENVIRONMENT_FILE_BYTES)

    with pytest.raises(ValueError, match="exceeds"):
        load_environment_file(path)


def test_doctor_is_secret_free_and_read_only(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    content = tmp_path / "content"
    content.mkdir()
    database = tmp_path / ".craig" / "index.sqlite3"
    database.parent.mkdir()
    database.write_bytes(b"generated test index")
    frontend = tmp_path / "dist"
    frontend.mkdir()
    (frontend / "index.html").write_text("<div id='root'></div>", encoding="utf-8")
    monkeypatch.setenv("OPENAI_API_KEY", "doctor-must-not-return-this")
    monkeypatch.setenv("GROQ_API_KEY", "doctor-must-not-return-groq-key")
    monkeypatch.setenv(
        "CLOUDFLARE_API_TOKEN", "doctor-must-not-return-cloudflare-token"
    )
    monkeypatch.setattr("craig.doctor.shutil.which", lambda command: f"/{command}")
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    report = run_doctor(
        RetrievalConfig(content_root=content, database_path=database),
        frontend_dist=frontend,
    )
    after = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))

    assert report["status"] == "pass"
    assert "doctor-must-not-return-this" not in json.dumps(report)
    assert "doctor-must-not-return-groq-key" not in json.dumps(report)
    assert "doctor-must-not-return-cloudflare-token" not in json.dumps(report)
    assert before == after


def test_release_versions_and_cross_platform_assets_are_consistent() -> None:
    pyproject = (REPOSITORY_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    readme = (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8")
    package = json.loads(
        (REPOSITORY_ROOT / "app" / "frontend" / "package.json").read_text(
            encoding="utf-8"
        )
    )
    env_example = (REPOSITORY_ROOT / ".env.example").read_text(encoding="utf-8")
    compose = (REPOSITORY_ROOT / "docker-compose.yml").read_text(encoding="utf-8")
    dockerfile = (REPOSITORY_ROOT / "Dockerfile").read_text(encoding="utf-8")

    assert __version__ == package["version"] == "1.0.0"
    assert 'version = "1.0.0"' in pyproject
    assert 'readme = "README.md"' in pyproject
    assert "craig = \"craig.cli:main\"" in pyproject
    assert "OPENAI_API_KEY=" in env_example
    assert "GROQ_API_KEY=" in env_example
    assert "CLOUDFLARE_ACCOUNT_ID=" in env_example
    assert "CLOUDFLARE_API_TOKEN=" in env_example
    assert "sk-" not in env_example
    assert (REPOSITORY_ROOT / "scripts" / "setup.cmd").is_file()
    assert (REPOSITORY_ROOT / "scripts" / "start.cmd").is_file()
    assert (REPOSITORY_ROOT / "scripts" / "setup.sh").is_file()
    assert (REPOSITORY_ROOT / "scripts" / "start.sh").is_file()
    assert "CRAIG_INDEX_PATH=/data/index.sqlite3" in dockerfile
    assert "USER craig" in dockerfile
    assert "read_only: true" in compose
    assert "no-new-privileges:true" in compose
    assert "CRAIG_MODEL_MAX_RESPONSE_BYTES" in compose
    assert "GROQ_API_KEY" in compose
    assert "CLOUDFLARE_ACCOUNT_ID" in compose
    assert "CLOUDFLARE_API_TOKEN" in compose
    assert "ollama pull qwen3:4b-instruct" in readme
    assert "curl http://127.0.0.1:11434/v1/models" in readme
    assert "scripts\\setup.cmd" in readme
    assert "sh scripts/setup.sh" in readme

    active_provider_lines = [
        line
        for line in env_example.splitlines()
        if line.startswith("CRAIG_MODEL_PROVIDER=")
    ]
    assert active_provider_lines == ["CRAIG_MODEL_PROVIDER=demo"]


def test_release_documentation_covers_every_phase_eight_surface() -> None:
    installation = (REPOSITORY_ROOT / "docs" / "installation.md").read_text(
        encoding="utf-8"
    )
    models = (REPOSITORY_ROOT / "docs" / "model-configuration.md").read_text(
        encoding="utf-8"
    )
    privacy = (REPOSITORY_ROOT / "docs" / "privacy.md").read_text(
        encoding="utf-8"
    )
    features = (REPOSITORY_ROOT / "docs" / "features.md").read_text(
        encoding="utf-8"
    )

    for platform in ("Windows", "macOS", "Linux", "Docker"):
        assert platform in installation
    assert "Remote OpenAI provider" in models
    assert "Remote Groq provider" in models
    assert "Remote Cloudflare Workers AI provider" in models
    assert "Loopback local provider" in models
    assert "strong" in models and "small" in models
    assert "Conversation history is held only" in privacy
    assert "| 1.0 | 8 |" in features
