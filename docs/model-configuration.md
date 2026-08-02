# Model-provider configuration

CRAIG v1.0 defaults to `demo`, a deterministic local retrieval presentation.
It makes no model API request and requires no secret. Live synthesis is opt-in.

Copy `.env.example` to `.env` or set the same variables in the server process.
CRAIG loads a bounded UTF-8 `.env` file as literal key/value pairs; it does not
execute shell expressions or expand variables. Existing process environment
variables take precedence. `.env` is ignored by Git.

## Remote OpenAI provider

```text
CRAIG_MODEL_PROVIDER=openai
CRAIG_MODEL=your-model-id
OPENAI_API_KEY=your-secret-key
```

Restart CRAIG after changing configuration. The key remains in the server
environment and is sent as HTTP Bearer authentication; it is never returned by
the public configuration or health endpoints. OpenAI's documentation likewise
requires API keys to stay out of browser code and recommends loading them from
a server-side environment variable or key manager:
<https://platform.openai.com/docs/api-reference/backward-compatibility>.

The adapter uses `POST https://api.openai.com/v1/chat/completions` with system
and user messages and a bounded `max_completion_tokens` value. Select a model
that currently supports Chat Completions and pin a snapshot when repeatable
evaluation matters. The current model catalog is maintained at
<https://developers.openai.com/api/docs/models>.

## Loopback local provider

CRAIG can use a local server implementing the OpenAI-compatible Chat
Completions shape:

```text
CRAIG_MODEL_PROVIDER=local
CRAIG_MODEL=your-local-model-id
CRAIG_MODEL_BASE_URL=http://127.0.0.1:11434/v1
CRAIG_MODEL_API_KEY=
```

Local endpoints must use `localhost` or a loopback IP address. CRAIG rejects
hostnames, LAN addresses, embedded credentials, query strings, and fragments in
local mode. `CRAIG_MODEL_API_KEY` is optional for local servers that require a
token. Local requests use `max_tokens`, which is widely implemented by
compatible local servers.

## Shared limits

```text
CRAIG_MODEL_TIMEOUT_SECONDS=60
CRAIG_MODEL_MAX_OUTPUT_TOKENS=2000
CRAIG_MODEL_MAX_RESPONSE_BYTES=1048576
```

Timeouts are restricted to 1–180 seconds, output tokens to 64–32,768, model
responses to 1 KiB–4 MiB, and encoded requests to 256 KiB. Endpoint errors are
reduced to status and safe request identifiers; response bodies and secrets are
not exposed to the browser.

Retrieval planning remains deterministic and allowlisted for every provider.
The model never chooses shell commands, computation operations, file paths, or
retrieval tool names. It receives data only after CRAIG's existing bounded
read-only retrieval has completed.

## Strong and small model evaluation

Use the same synthetic cases and configuration limits for both tiers:

```text
craig evaluate-model --tier strong --confirm-live --output .craig/evaluations/strong.json
craig evaluate-model --tier small --confirm-live --output .craig/evaluations/small.json
```

Change only `CRAIG_MODEL` (and provider endpoint if necessary) between runs.
The explicit `--confirm-live` flag is required because a run may transmit data
and incur provider charges. Reports may contain model answers and therefore
belong outside `content/`; `.craig/` is ignored by Git.

The release evaluation checks three contracts using synthetic material:

- retention of supplied citation identifiers;
- refusal to promote a finite check into an unbounded proof;
- preservation of `unknown` mathematical status.

Unit tests exercise both strong and small profiles against a deterministic fake
transport. Optional `live_model` tests and the CLI contact real endpoints only
when explicitly enabled. No live quality result is claimed merely because the
adapter or mocked profiles pass.

To run the optional live tests, configure one provider as above, then set the
two model IDs and the explicit authorization flag. In PowerShell:

```text
$env:CRAIG_RUN_LIVE_MODEL_EVALS="1"
$env:CRAIG_EVAL_STRONG_MODEL="your-strong-model-id"
$env:CRAIG_EVAL_SMALL_MODEL="your-small-model-id"
python -m pytest -m live_model
```

In a POSIX shell, use `export` instead of `$env:`. These tests make three
requests per tier and may transmit data or incur charges.
