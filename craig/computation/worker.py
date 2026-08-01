"""JSON-lines entry point for one isolated computation worker."""

from __future__ import annotations

import json
import os
import platform
import sys
import time
import tracemalloc
from typing import Any

PROTOCOL_VERSION = 1


def _emit(message_type: str, data: dict[str, Any]) -> None:
    payload = {"protocol_version": PROTOCOL_VERSION, "type": message_type, "data": data}
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    sys.stdout.write("\n")
    sys.stdout.flush()


def _positive_environment_integer(name: str) -> int:
    value = os.environ.get(name, "")
    try:
        parsed = int(value)
    except ValueError as error:
        raise RuntimeError(f"missing or invalid worker limit: {name}") from error
    if parsed < 1:
        raise RuntimeError(f"worker limit must be positive: {name}")
    return parsed


def _apply_posix_limits() -> None:
    if os.name == "nt":
        return
    import resource

    cpu_seconds = _positive_environment_integer("CRAIG_WORKER_CPU_SECONDS")
    memory_bytes = _positive_environment_integer("CRAIG_WORKER_MEMORY_BYTES")
    output_bytes = _positive_environment_integer("CRAIG_WORKER_OUTPUT_BYTES")
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
    if hasattr(resource, "RLIMIT_AS"):
        resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))
    if hasattr(resource, "RLIMIT_FSIZE"):
        resource.setrlimit(resource.RLIMIT_FSIZE, (output_bytes, output_bytes))


def main() -> int:
    started = time.perf_counter()
    cpu_started = time.process_time()
    try:
        _apply_posix_limits()
        from .errors import InvalidComputationRequest
        from .registry import execute_operation

        request_limit = _positive_environment_integer("CRAIG_WORKER_REQUEST_BYTES")
        raw = sys.stdin.buffer.read(request_limit + 1)
        if len(raw) > request_limit:
            raise InvalidComputationRequest("worker request exceeds its byte limit")
        request = json.loads(raw.decode("utf-8"))
        if not isinstance(request, dict) or set(request) != {
            "protocol_version",
            "operation",
            "parameters",
        }:
            raise InvalidComputationRequest("invalid worker request envelope")
        if request["protocol_version"] != PROTOCOL_VERSION:
            raise InvalidComputationRequest("unsupported worker protocol version")

        forbidden_events = {
            "open",
            "os.system",
            "subprocess.Popen",
            "socket.__new__",
            "socket.connect",
            "socket.bind",
        }

        def deny_external_capabilities(event: str, arguments: tuple[Any, ...]) -> None:
            del arguments
            if event == "import" or event in forbidden_events or event.startswith(
                ("os.exec", "os.spawn")
            ):
                raise PermissionError(
                    f"worker capability is disabled during kernel execution: {event}"
                )

        sys.addaudithook(deny_external_capabilities)

        last_fraction = 0.0

        def progress(fraction: float, label: str) -> None:
            nonlocal last_fraction
            checked = min(0.99, max(last_fraction, float(fraction)))
            last_fraction = checked
            _emit("progress", {"fraction": checked, "label": str(label)[:160]})

        tracemalloc.start()
        result = execute_operation(
            str(request["operation"]),
            request["parameters"],
            progress,
        )
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        encoded_result = json.dumps(
            result,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
        output_limit = _positive_environment_integer("CRAIG_WORKER_OUTPUT_BYTES")
        if len(encoded_result) > output_limit:
            raise MemoryError("serialized computation result exceeds its output limit")
        _emit("progress", {"fraction": 1.0, "label": "Computation complete"})
        _emit(
            "result",
            {
                "result": result,
                "metrics": {
                    "kernel_wall_time_ms": round((time.perf_counter() - started) * 1000, 3),
                    "worker_cpu_time_ms": round((time.process_time() - cpu_started) * 1000, 3),
                    "peak_python_memory_bytes": peak_memory,
                },
                "runtime": {
                    "python_version": platform.python_version(),
                    "platform": sys.platform,
                },
            },
        )
        return 0
    except MemoryError as error:
        _emit("error", {"code": "memory_or_output_limit", "message": str(error)})
        return 3
    except Exception as error:
        code = (
            "invalid_request"
            if error.__class__.__name__ == "InvalidComputationRequest"
            else "worker_failed"
        )
        _emit("error", {"code": code, "message": str(error)[:500]})
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
