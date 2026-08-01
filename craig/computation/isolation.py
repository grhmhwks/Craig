"""Cross-platform subprocess isolation for curated computations."""

from __future__ import annotations

import json
import os
import queue
import signal
import subprocess
import sys
import tempfile
import threading
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any, BinaryIO

from .errors import ComputationLimitExceeded, ComputationWorkerFailure
from .models import ComputationLimits

_BOOTSTRAP = (
    "import sys;"
    "sys.path.insert(0,sys.argv[1]);"
    "from craig.computation.worker import main;"
    "raise SystemExit(main())"
)


class _WindowsJob:
    """Windows Job Object enforcing one process, CPU, and memory limits."""

    def __init__(self, process: subprocess.Popen[bytes], limits: ComputationLimits):
        self._handle: int | None = None
        if os.name != "nt":
            return
        import ctypes
        from ctypes import wintypes

        class IO_COUNTERS(ctypes.Structure):
            _fields_ = [
                ("ReadOperationCount", ctypes.c_ulonglong),
                ("WriteOperationCount", ctypes.c_ulonglong),
                ("OtherOperationCount", ctypes.c_ulonglong),
                ("ReadTransferCount", ctypes.c_ulonglong),
                ("WriteTransferCount", ctypes.c_ulonglong),
                ("OtherTransferCount", ctypes.c_ulonglong),
            ]

        class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [
                ("PerProcessUserTimeLimit", ctypes.c_longlong),
                ("PerJobUserTimeLimit", ctypes.c_longlong),
                ("LimitFlags", wintypes.DWORD),
                ("MinimumWorkingSetSize", ctypes.c_size_t),
                ("MaximumWorkingSetSize", ctypes.c_size_t),
                ("ActiveProcessLimit", wintypes.DWORD),
                ("Affinity", ctypes.c_size_t),
                ("PriorityClass", wintypes.DWORD),
                ("SchedulingClass", wintypes.DWORD),
            ]

        class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [
                ("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION),
                ("IoInfo", IO_COUNTERS),
                ("ProcessMemoryLimit", ctypes.c_size_t),
                ("JobMemoryLimit", ctypes.c_size_t),
                ("PeakProcessMemoryUsed", ctypes.c_size_t),
                ("PeakJobMemoryUsed", ctypes.c_size_t),
            ]

        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
        kernel32.CreateJobObjectW.restype = wintypes.HANDLE
        kernel32.SetInformationJobObject.argtypes = [
            wintypes.HANDLE,
            ctypes.c_int,
            ctypes.c_void_p,
            wintypes.DWORD,
        ]
        kernel32.SetInformationJobObject.restype = wintypes.BOOL
        kernel32.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
        kernel32.AssignProcessToJobObject.restype = wintypes.BOOL
        handle = kernel32.CreateJobObjectW(None, None)
        if not handle:
            raise OSError(ctypes.get_last_error(), "CreateJobObjectW failed")
        self._kernel32 = kernel32
        self._handle = int(handle)
        info = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
        job_object_limit_process_time = 0x00000002
        job_object_limit_active_process = 0x00000008
        job_object_limit_process_memory = 0x00000100
        job_object_limit_kill_on_close = 0x00002000
        info.BasicLimitInformation.LimitFlags = (
            job_object_limit_process_time
            | job_object_limit_active_process
            | job_object_limit_process_memory
            | job_object_limit_kill_on_close
        )
        info.BasicLimitInformation.PerProcessUserTimeLimit = (
            limits.cpu_time_seconds * 10_000_000
        )
        info.BasicLimitInformation.ActiveProcessLimit = 1
        info.ProcessMemoryLimit = limits.memory_bytes
        if not kernel32.SetInformationJobObject(
            handle,
            9,
            ctypes.byref(info),
            ctypes.sizeof(info),
        ):
            self.close()
            raise OSError(ctypes.get_last_error(), "SetInformationJobObject failed")
        if not kernel32.AssignProcessToJobObject(
            handle,
            wintypes.HANDLE(process._handle),  # type: ignore[attr-defined]
        ):
            self.close()
            raise OSError(ctypes.get_last_error(), "AssignProcessToJobObject failed")

    def close(self) -> None:
        if self._handle is not None:
            self._kernel32.CloseHandle(self._handle)
            self._handle = None


def _worker_environment(
    limits: ComputationLimits,
    temporary_directory: str,
) -> dict[str, str]:
    keep = ("SYSTEMROOT", "WINDIR")
    environment = {key: os.environ[key] for key in keep if key in os.environ}
    environment.update(
        {
            "PYTHONIOENCODING": "utf-8",
            "TEMP": temporary_directory,
            "TMP": temporary_directory,
            "TMPDIR": temporary_directory,
            "CRAIG_WORKER_CPU_SECONDS": str(limits.cpu_time_seconds),
            "CRAIG_WORKER_MEMORY_BYTES": str(limits.memory_bytes),
            "CRAIG_WORKER_OUTPUT_BYTES": str(limits.output_bytes),
            "CRAIG_WORKER_REQUEST_BYTES": str(limits.request_bytes),
        }
    )
    return environment


def _reader(
    stream: BinaryIO,
    channel: str,
    messages: queue.Queue[tuple[str, bytes | None]],
) -> None:
    try:
        while True:
            chunk = stream.readline()
            if not chunk:
                break
            messages.put((channel, chunk))
    finally:
        messages.put((f"{channel}.done", None))


def _terminate(process: subprocess.Popen[bytes], job: _WindowsJob | None) -> None:
    if process.poll() is not None:
        return
    if os.name == "nt":
        if job is not None:
            job.close()
        else:
            process.kill()
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    try:
        process.wait(timeout=1)
    except subprocess.TimeoutExpired:
        process.kill()


def stream_isolated_worker(
    operation: str,
    parameters: dict[str, Any],
    limits: ComputationLimits,
    *,
    forbidden_roots: tuple[Path, ...] = (),
) -> Iterator[dict[str, Any]]:
    """Yield validated JSON messages from one resource-limited worker."""

    request = json.dumps(
        {
            "protocol_version": 1,
            "operation": operation,
            "parameters": parameters,
        },
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    if len(request) > limits.request_bytes:
        raise ComputationLimitExceeded("worker request exceeds its byte limit")

    package_root = Path(__file__).resolve().parents[2]
    temporary_root = Path(tempfile.gettempdir()).resolve()
    for root in (package_root, *forbidden_roots):
        try:
            temporary_root.relative_to(root.resolve())
        except ValueError:
            continue
        raise ComputationWorkerFailure(
            "the operating-system temporary directory overlaps a protected root"
        )
    command = [
        sys.executable,
        "-I",
        "-B",
        "-X",
        "utf8",
        "-c",
        _BOOTSTRAP,
        str(package_root),
    ]
    creationflags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    messages: queue.Queue[tuple[str, bytes | None]] = queue.Queue()
    process: subprocess.Popen[bytes] | None = None
    job: _WindowsJob | None = None
    started = time.monotonic()
    with tempfile.TemporaryDirectory(
        prefix="craig-computation-",
        dir=temporary_root,
    ) as temporary:
        try:
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=temporary,
                env=_worker_environment(limits, temporary),
                creationflags=creationflags,
                start_new_session=os.name != "nt",
            )
            try:
                job = _WindowsJob(process, limits)
            except OSError as error:
                process.kill()
                process.wait()
                raise ComputationWorkerFailure(
                    f"could not establish the operating-system worker sandbox: {error}"
                ) from error
            assert process.stdin is not None
            assert process.stdout is not None
            assert process.stderr is not None
            stdout_thread = threading.Thread(
                target=_reader,
                args=(process.stdout, "stdout", messages),
                daemon=True,
            )
            stderr_thread = threading.Thread(
                target=_reader,
                args=(process.stderr, "stderr", messages),
                daemon=True,
            )
            stdout_thread.start()
            stderr_thread.start()
            process.stdin.write(request)
            process.stdin.close()

            stdout_bytes = 0
            stderr_bytes = 0
            stdout_done = False
            stderr_done = False
            result_seen = False
            worker_error: tuple[str, str] | None = None
            while True:
                elapsed = time.monotonic() - started
                if elapsed > limits.wall_time_seconds:
                    _terminate(process, job)
                    raise ComputationLimitExceeded(
                        f"worker exceeded the {limits.wall_time_seconds:g}-second wall-time limit"
                    )
                try:
                    channel, chunk = messages.get(timeout=0.05)
                except queue.Empty:
                    if process.poll() is not None and stdout_done and stderr_done:
                        break
                    continue
                if channel == "stdout.done":
                    stdout_done = True
                elif channel == "stderr.done":
                    stderr_done = True
                elif channel == "stderr" and chunk is not None:
                    stderr_bytes += len(chunk)
                    if stderr_bytes > limits.stderr_bytes:
                        _terminate(process, job)
                        raise ComputationLimitExceeded(
                            "worker exceeded the stderr byte limit"
                        )
                elif channel == "stdout" and chunk is not None:
                    stdout_bytes += len(chunk)
                    if stdout_bytes > limits.output_bytes:
                        _terminate(process, job)
                        raise ComputationLimitExceeded(
                            "worker exceeded the stdout byte limit"
                        )
                    try:
                        envelope = json.loads(chunk.decode("utf-8"))
                    except (UnicodeDecodeError, json.JSONDecodeError) as error:
                        _terminate(process, job)
                        raise ComputationWorkerFailure(
                            "worker returned an invalid JSON-lines message"
                        ) from error
                    if not isinstance(envelope, dict) or envelope.get(
                        "protocol_version"
                    ) != 1:
                        raise ComputationWorkerFailure(
                            "worker returned an invalid protocol envelope"
                        )
                    message_type = envelope.get("type")
                    data = envelope.get("data")
                    if not isinstance(message_type, str) or not isinstance(data, dict):
                        raise ComputationWorkerFailure(
                            "worker returned an invalid message shape"
                        )
                    if message_type == "error":
                        worker_error = (
                            str(data.get("code", "worker_failed")),
                            str(data.get("message", "worker failed")),
                        )
                    elif message_type == "result":
                        if result_seen:
                            raise ComputationWorkerFailure(
                                "worker returned more than one result"
                            )
                        result_seen = True
                        yield {"type": message_type, "data": data}
                    elif message_type == "progress":
                        yield {"type": message_type, "data": data}
                    else:
                        raise ComputationWorkerFailure(
                            f"worker returned unsupported message type: {message_type}"
                        )
                if process.poll() is not None and stdout_done and stderr_done:
                    break

            return_code = process.wait(timeout=1)
            if worker_error is not None:
                code, message = worker_error
                if code == "memory_or_output_limit":
                    raise ComputationLimitExceeded(message)
                raise ComputationWorkerFailure(message)
            if return_code != 0:
                raise ComputationLimitExceeded(
                    "worker was stopped by an operating-system CPU or memory limit"
                )
            if not result_seen:
                raise ComputationWorkerFailure("worker exited without a result")
        finally:
            if process is not None:
                _terminate(process, job)
            if job is not None:
                job.close()
