"""Lean, mode-aware prompt contracts for CRAIG's two-stage pipeline."""

from __future__ import annotations

from .models import ChatMode, ToolResult

_MODE_GUIDANCE: dict[ChatMode, str] = {
    "research": (
        "Synthesize the strongest repository evidence, note gaps or conflicts, "
        "and keep source locations attached to supported claims."
    ),
    "explanation": (
        "Explain the retrieved mathematics directly and clearly, defining "
        "specialized terms before relying on them."
    ),
    "tutorial": (
        "Teach incrementally: establish prerequisites, give a small conceptual "
        "path through the material, and suggest a useful next question."
    ),
    "computation": (
        "Retrieval is available, but no repository program may be executed in "
        "Phase 3. Clearly distinguish inspectable code from an actual run."
    ),
}


def initial_system_prompt(mode: ChatMode, topic: str | None) -> str:
    """Build the search-planning prompt without repeating policy."""

    scope = f"topic `{topic}`" if topic else "the complete indexed corpus"
    return (
        "Role: plan read-only retrieval for CRAIG, a local combinatorics "
        f"research assistant.\nGoal: gather enough evidence from {scope} to "
        "answer the user's question.\nConstraints: use only the provided "
        "list_topics, search_content, find_exact, and read_source operations; "
        "never request repository writes, shell execution, external web search, "
        "or unapproved computation. Stop when the core question has useful "
        "source support or the index has no relevant evidence.\nMode: "
        f"{_MODE_GUIDANCE[mode]}"
    )


def secondary_system_prompt(
    mode: ChatMode,
    topic: str | None,
    tool_results: tuple[ToolResult, ...],
) -> str:
    """Build the answer prompt after retrieval has completed."""

    scope = f"topic `{topic}`" if topic else "the indexed repository"
    result_count = sum(1 for result in tool_results if result.success)
    return (
        "Role: answer as CRAIG using retrieved repository evidence.\n"
        f"Goal: answer the user from {scope}; {result_count} retrieval result(s) "
        "are available.\nConstraints: do not imply that missing evidence proves "
        "a negative; do not turn finite evidence into a general proof; cite only "
        "the source locations supplied by the application; label uncertainty "
        "plainly; do not claim to have executed code.\nMode: "
        f"{_MODE_GUIDANCE[mode]}"
    )


def mode_description(mode: ChatMode) -> str:
    """Return a user-facing one-line description for a chat mode."""

    return _MODE_GUIDANCE[mode]
