# Model-provider configuration

CRAIG v1.0 defaults to `demo`, a deterministic local retrieval presentation.
It makes no model API request and requires no secret. Live synthesis is opt-in.

Copy `.env.example` to `.env` or set the same variables in the server process.
CRAIG loads a bounded UTF-8 `.env` file as literal key/value pairs; it does not
execute shell expressions or expand variables. Existing process environment
variables take precedence. `.env` is ignored by Git.

## Remote Cloudflare Workers AI provider

Cloudflare Workers AI is the recommended free remote provider. Create a Workers
AI API token and copy the Account ID by following Cloudflare's
[REST API setup](https://developers.cloudflare.com/workers-ai/get-started/rest-api/),
then configure:

```text
CRAIG_MODEL_PROVIDER=cloudflare
CRAIG_MODEL=@cf/qwen/qwen3-30b-a3b-fp8
CLOUDFLARE_ACCOUNT_ID=your-32-character-account-id
CLOUDFLARE_API_TOKEN=your-secret-api-token
```

CRAIG accepts only a 32-character hexadecimal account ID and constructs the
fixed account-scoped endpoint
`https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions`.
The endpoint is not user-configurable. The API token is used only as backend
Bearer authentication and is never included in public configuration or health
responses.

The adapter uses Cloudflare's
[OpenAI-compatible Chat Completions API](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/)
with a bounded `max_tokens` value. The recommended initial model,
[`@cf/qwen/qwen3-30b-a3b-fp8`](https://developers.cloudflare.com/workers-ai/models/qwen3-30b-a3b-fp8/),
has a 32,768-token context window and supports reasoning. Select another exact
text-generation identifier from the
[Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/)
when needed.

The Workers Free plan currently provides 10,000 neurons per day; review
[current pricing and allocation details](https://developers.cloudflare.com/workers-ai/platform/pricing/).
CRAIG reports HTTP 429 as a retryable quota condition and does not silently
switch providers.

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

## Remote Groq provider

Groq remains an optional remote free-plan provider. It uses a fixed, allowlisted
OpenAI-compatible endpoint rather than a user-configurable remote URL:

```text
CRAIG_MODEL_PROVIDER=groq
CRAIG_MODEL=qwen/qwen3.6-27b
GROQ_API_KEY=your-secret-key
```

As of August 2026, `qwen/qwen3.6-27b` is the recommended starting point for
mathematical synthesis and `openai/gpt-oss-120b` is a comparison candidate.
Confirm current model availability and quotas at
<https://console.groq.com/docs/models> and
<https://console.groq.com/docs/rate-limits>. The adapter sends Bearer
authentication only to `https://api.groq.com/openai/v1/chat/completions` and
uses `max_completion_tokens`.

The browser labels this as a remote model. CRAIG reports HTTP 429 as a quota
condition and does not automatically fall back to another provider. This keeps
the data destination and model choice explicit.

## Loopback local provider

CRAIG can use a local server implementing the OpenAI-compatible Chat
Completions shape. The repository [README](../README.md#run-a-free-model-locally-with-ollama)
walks through installing Ollama, downloading and testing a model, creating
`.env`, running diagnostics, and checking the browser. The final provider block
has this shape:

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

Ollama commonly defaults to a 4,096-token context on systems without substantial
dedicated GPU memory. An 8,192-token context can improve source-heavy CRAIG
turns when memory permits; configure this in Ollama rather than CRAIG's `.env`.
Increasing context consumes additional memory. See
<https://docs.ollama.com/context-length>.

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
read-only retrieval has completed. Search initially produces compact snippets;
CRAIG follows it by reading up to four distinct ranked passages. Evidence is
then capped at 1,600 characters per displayed/model-visible source before the
answer request is constructed.

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
