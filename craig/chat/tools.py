"""Read-only retrieval tool registry used by conversational orchestration."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from ..retrieval import RetrievalService
from .models import ToolCall, ToolResult


class RetrievalToolRegistry:
    """Validate and execute the four Phase 2 operations by public tool name."""

    names = frozenset(
        {"list_topics", "search_content", "find_exact", "read_source"}
    )

    def __init__(self, retrieval: RetrievalService) -> None:
        self.retrieval = retrieval

    def execute(self, call: ToolCall) -> ToolResult:
        """Execute one bounded retrieval call and serialize its result."""

        try:
            output = self._dispatch(call.name, call.arguments)
        except (TypeError, ValueError, RuntimeError) as error:
            return ToolResult(
                call_id=call.call_id,
                name=call.name,
                arguments=call.arguments,
                output={"error": str(error)},
                success=False,
            )
        return ToolResult(
            call_id=call.call_id,
            name=call.name,
            arguments=call.arguments,
            output=output,
            success=True,
        )

    def _dispatch(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name not in self.names:
            raise ValueError(f"Unknown retrieval tool: {name}")
        if name == "list_topics":
            if arguments:
                raise ValueError("list_topics does not accept arguments.")
            return asdict(self.retrieval.list_topics())
        if name == "search_content":
            query = arguments.get("query")
            if not isinstance(query, str):
                raise ValueError("search_content requires a string query.")
            return asdict(
                self.retrieval.search_content(
                    query,
                    topic=self._optional_string(arguments, "topic"),
                    limit=self._optional_integer(arguments, "limit"),
                    offset=self._integer(arguments, "offset", default=0),
                    max_chars=self._optional_integer(arguments, "max_chars"),
                )
            )
        if name == "find_exact":
            query = arguments.get("query")
            if not isinstance(query, str):
                raise ValueError("find_exact requires a string query.")
            return asdict(
                self.retrieval.find_exact(
                    query,
                    topic=self._optional_string(arguments, "topic"),
                    case_sensitive=self._boolean(
                        arguments,
                        "case_sensitive",
                        default=False,
                    ),
                    context_lines=self._integer(
                        arguments,
                        "context_lines",
                        default=2,
                    ),
                    limit=self._optional_integer(arguments, "limit"),
                    offset=self._integer(arguments, "offset", default=0),
                    max_chars=self._optional_integer(arguments, "max_chars"),
                )
            )
        path = arguments.get("path")
        if not isinstance(path, str):
            raise ValueError("read_source requires a string path.")
        return asdict(
            self.retrieval.read_source(
                path,
                start_line=self._integer(arguments, "start_line", default=1),
                end_line=self._optional_integer(arguments, "end_line"),
                max_chars=self._optional_integer(arguments, "max_chars"),
            )
        )

    @staticmethod
    def _optional_string(arguments: dict[str, Any], name: str) -> str | None:
        value = arguments.get(name)
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError(f"{name} must be a string.")
        return value

    @staticmethod
    def _optional_integer(arguments: dict[str, Any], name: str) -> int | None:
        value = arguments.get(name)
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer.")
        return value

    @staticmethod
    def _integer(
        arguments: dict[str, Any],
        name: str,
        *,
        default: int,
    ) -> int:
        value = arguments.get(name, default)
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer.")
        return value

    @staticmethod
    def _boolean(
        arguments: dict[str, Any],
        name: str,
        *,
        default: bool,
    ) -> bool:
        value = arguments.get(name, default)
        if not isinstance(value, bool):
            raise ValueError(f"{name} must be a boolean.")
        return value
