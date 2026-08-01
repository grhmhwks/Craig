# Phase 6 approved computation

Phase 6 adds deterministic local computation without turning repository files
or model output into commands. The protected `content/` directory remains
read-only. Corpus programs are statically inventoried, but workers execute only
reviewed kernels in `craig/computation/`.

The program inventory and allowlist rationale are recorded in
[`phase-6-inventory.md`](phase-6-inventory.md).

## Public operations

The first release exposes four operations:

- `dyck_path_statistics`: a bounded exact example for one classical path;
- `enumerate_dyck_paths`: an exhaustive finite check for semilength at most 10;
- `enumerate_rational_dyck_paths`: an exhaustive finite check for coprime
  endpoints `2 <= r,s <= 10`;
- `type_c_hecke_word`: a bounded exact example for rank at most 7 and a word of
  at most 80 generators.

The catalog is available at `GET /api/v1/computations`. A job is submitted to
`POST /api/v1/computations/stream`:

```json
{
  "operation": "enumerate_rational_dyck_paths",
  "parameters": {"r": 5, "s": 3}
}
```

The response is Server-Sent Events containing `computation.started`, monotone
`computation.progress`, and either `computation.completed` or
`computation.error`. Unknown operations and extra parameters are rejected
before response streaming begins.

## Isolation boundary

Every job runs in a new Python process with:

- isolated interpreter mode (`-I`) and bytecode writes disabled;
- a fresh temporary working directory outside the repository;
- a minimal environment and a versioned JSON-lines protocol;
- a closed operation registry and validation repeated inside the worker;
- a Python audit hook denying imports, file opens, sockets, subprocesses, and
  process-execution calls during kernel execution;
- no shell invocation, user-supplied path, module, function, or command;
- at most two concurrent workers by default.

On Windows, the process is assigned to a Job Object before receiving its
request. The Job Object caps per-process CPU time and memory, permits only one
active process, and kills the worker when its job handle closes. On POSIX,
`setrlimit` caps CPU time, address space, and file size, and the worker runs in a
new process group. The parent independently enforces wall time, request bytes,
stdout bytes, and stderr bytes on every platform. Cancellation or generator
closure kills the process tree and releases the worker slot.

The current public profiles allow either 3 seconds wall / 2 seconds CPU / 192
MiB memory for small examples, or 8 seconds wall / 6 seconds CPU / 256 MiB for
enumerations. Requests are limited to 16 KiB, stdout to 256 KiB, and stderr to
32 KiB. Operation schemas add much tighter mathematical bounds.

## Results and mathematical status

A completed event includes:

- normalized parameters and a user-facing summary;
- exact structured output;
- an optional trusted Phase 5 visualization specification;
- evidence classification (`example` or `finite_check` in this release);
- an explicit claim boundary;
- implementation version and SHA-256;
- corpus source basis, line interval, and current SHA-256;
- canonical request and result SHA-256 values;
- worker runtime, CPU time, Python allocation peak, and total wall time;
- the limits that governed the run.

An exhaustive finite check means only that every object in the displayed
bounded case was enumerated. It is never promoted to a proof of an unbounded
claim. No first-release operation is labeled `computer_assisted_proof`; adding
one requires a separate proof-obligation review and registry revision.

## Browser workflow

Start the Python server and Vite as documented in the main README, select
**Computation**, choose an approved operation, enter its parameters, and choose
**Run approved job**. Chat in Computation mode still performs read-only
retrieval. This separation prevents a provider response from dispatching code.

The browser shows progress, the result classification and claim boundary, the
trusted visualization, exact JSON, hashes, source basis, and timing. Job results
remain in browser conversation state only; the backend does not persist them.

## Validation

```text
python -m pytest -q
cd app/frontend
npm run typecheck
npm test
npm run build
```

Backend tests cover the allowlist, validation, exact small cases, worker
progress, stable hashes, content integrity, wall/output termination, API
validation, SSE, and OpenAPI. Frontend tests cover computation SSE events,
schema-driven controls, claim boundaries, hashes, and the trusted renderer
handoff.
