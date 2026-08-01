"""Lean, mode-aware prompt contracts for CRAIG's two-stage pipeline."""

from __future__ import annotations

from .models import ChatMode, SourceReference, ToolResult

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
    sources: tuple[SourceReference, ...],
) -> str:
    """Build the answer prompt after retrieval has completed."""

    scope = f"topic `{topic}`" if topic else "the indexed repository"
    result_count = sum(1 for result in tool_results if result.success)
    citation_inventory = ", ".join(
        (
            f"{source.citation_id}=content/{source.path}:"
            f"{source.start_line}-{source.end_line}"
            f" ({source.mathematical_status})"
        )
        for source in sources
    )
    if not citation_inventory:
        citation_inventory = "none"
    return (
        "Role: answer as CRAIG using retrieved repository evidence.\n"
        f"Goal: answer the user from {scope}; {result_count} retrieval result(s) "
        "are available.\nAuthority labels: distinguish repository statements, "
        "deductions from those statements, general model knowledge, and external "
        "information. External information is unavailable in this release. Cite "
        "each repository-backed claim with the supplied citation identifier. "
        "Never present a deduction as an explicit source statement.\nStatus "
        "rules: use only the supplied mathematical status; `unknown` must remain "
        "unknown. Do not turn finite evidence into a general proof. Distinguish "
        "exploratory or sampled computation from an exhaustive finite check, and "
        "call an exhaustive check proof-relevant only when the source explicitly "
        "establishes that role. Do not imply that missing evidence proves a "
        "negative or claim to have executed code.\n"
        f"Available citations: {citation_inventory}.\nMode: "
        f"{_MODE_GUIDANCE[mode]}"
    )


def mode_description(mode: ChatMode) -> str:
    """Return a user-facing one-line description for a chat mode."""

    return _MODE_GUIDANCE[mode]
