# CRAIG

CRAIG—the **Combinatorial Research Assistance Interactive Guide**—is a local,
repository-grounded interface for exploring the mathematical sources in
[`content/`](content/). It combines read-only retrieval, inspectable citations,
mathematical rendering, approved computations, and algorithm traces with either
a no-network demonstration or an explicitly configured language model.

CRAIG 1.0 supports five model-provider modes. Provider selection is a backend
`.env` setting, so secrets never enter the browser:

| Provider | Cost and data path | Configuration |
| --- | --- | --- |
| `demo` | No model, credential, or network request | Default |
| `local` | A model running on this computer through a loopback OpenAI-compatible API | Ollama walkthrough below |
| `cloudflare` | A hosted open-source model through Cloudflare Workers AI; a free daily allocation applies | Cloudflare walkthrough below |
| `groq` | A hosted model through Groq; a free-plan account and quotas apply | Groq walkthrough below |
| `openai` | A user-selected OpenAI model; normal provider charges and policies apply | API-key walkthrough below |

For live model-backed answers, **Cloudflare Workers AI is strongly recommended
for most users**. Choose the local Ollama path only if you have sufficiently
capable local hardware to run a model with mathematical reasoning quality
comparable to the recommended Cloudflare model, or if keeping every model
request on the local computer is more important than answer quality and speed.
Small local models can run on ordinary computers, but they are not equivalent
substitutes for the recommended hosted model and may produce materially weaker
mathematical synthesis and citation use.

The mathematical corpus is protected and read-only. Generated indexes,
configuration, conversations, and evaluation reports remain outside
`content/`.

## Requirements

For the native installation:

- Git;
- Python 3.10 or newer with SQLite FTS5;
- Node.js and npm;
- Windows 10/11, macOS, or Linux.

Ollama is required only when you choose a free local model. A Cloudflare, Groq,
or OpenAI account is required only when selecting that remote provider. Docker
is optional.

## Clone and run the no-model demonstration

The demonstration is the quickest way to verify the application before adding
a model. It performs retrieval and presents source passages deterministically;
it makes no model request.

### Windows

Open Command Prompt or PowerShell:

```text
git clone <repository-url>
cd Craig
scripts\setup.cmd
scripts\start.cmd
```

Open <http://127.0.0.1:8000>. The Windows scripts call `npm.cmd` so PowerShell's
script-execution policy does not block npm.

### macOS and Linux

```text
git clone <repository-url>
cd Craig
sh scripts/setup.sh
sh scripts/start.sh
```

Open <http://127.0.0.1:8000>.

The setup script creates `.venv/`, installs CRAIG, builds the production
frontend, and writes the generated search index to `.craig/index.sqlite3`.
It reads but never writes the protected corpus.

## Run a free model locally with Ollama

[Ollama](https://docs.ollama.com/) is a local model manager and inference
server. It downloads a selected model, runs it on your CPU/GPU, and exposes the
loopback Chat Completions endpoint CRAIG uses. No API key is required for
Ollama's local endpoint.

This is an advanced alternative to the recommended Cloudflare setup below.
Use it when your computer can run a model of comparable mathematical capability,
or when local-only processing is a firm requirement and you accept that smaller
models may give weaker answers. Otherwise, use
[Cloudflare Workers AI](#run-a-free-remote-model-with-cloudflare-workers-ai).

Use the native CRAIG installation for this path. The supplied Docker container
does not connect to an Ollama instance on the host because CRAIG deliberately
restricts local providers to the server's own loopback interface.

### 1. Install Ollama

- Windows: follow the [official Windows instructions](https://docs.ollama.com/windows).
- macOS: follow the [official macOS instructions](https://docs.ollama.com/macos).
- Linux: follow the [official Linux instructions](https://docs.ollama.com/linux).

Open a new terminal and check the installation:

```text
ollama --version
```

Ollama normally runs its local API at `http://127.0.0.1:11434`.

Ollama commonly defaults to a 4,096-token context on computers without large
dedicated GPU memory. CRAIG works at that setting, but source-heavy questions
benefit from an 8,192-token context when memory permits. In the Ollama desktop
application, use its context-length setting; alternatively configure the Ollama
server with `OLLAMA_CONTEXT_LENGTH=8192` and restart Ollama. A larger context
uses more memory. See Ollama's
[context-length documentation](https://docs.ollama.com/context-length).

For an explicitly local-only Ollama installation, its optional
`OLLAMA_NO_CLOUD=1` server setting disables Ollama cloud features. This setting
belongs to the Ollama process—not CRAIG's `.env`—and requires an Ollama restart.
Selecting a downloaded local model such as `qwen3:4b-instruct` does not select a
cloud model.

### 2. Choose and download a model

A conservative model for testing the local integration on an ordinary computer
is the 2.5 GB instruction-tuned model below. It is not presented as equivalent
in answer quality to CRAIG's recommended Cloudflare model:

```text
ollama pull qwen3:4b-instruct
```

Alternatives include:

| Model | Approximate download | Use case |
| --- | ---: | --- |
| `llama3.2` | 2.0 GB | Lower resource use; weaker mathematical synthesis |
| `qwen3:4b-instruct` | 2.5 GB | Local integration starting point; weaker than the recommended hosted model |
| `qwen3.5:9b` | 6.6 GB | More capable hardware; larger and slower on CPU |

Model file size is not the same as total runtime memory. If a model cannot
load or makes the computer unresponsive, remove it with `ollama rm <model>` and
choose a smaller one. Current models and exact sizes are listed in the
[Ollama model library](https://registry.ollama.com/library).

Test the selected model directly:

```text
ollama run qwen3:4b-instruct
```

Ask a short question, then enter `/bye`. Confirm the installed name with:

```text
ollama list
```

### 3. Create your private CRAIG configuration

From the repository root, copy the committed template. Do not commit the
resulting `.env`; Git already ignores it.

Windows:

```text
copy .env.example .env
notepad .env
```

macOS/Linux:

```text
cp .env.example .env
${EDITOR:-vi} .env
```

Set the provider section to these values, using the exact model name shown by
`ollama list`:

```text
CRAIG_MODEL_PROVIDER=local
CRAIG_MODEL=qwen3:4b-instruct
CRAIG_MODEL_BASE_URL=http://127.0.0.1:11434/v1
CRAIG_MODEL_API_KEY=
CRAIG_MODEL_TIMEOUT_SECONDS=120
CRAIG_MODEL_MAX_OUTPUT_TOKENS=2000
CRAIG_MODEL_MAX_RESPONSE_BYTES=1048576
```

There must be exactly one active `CRAIG_MODEL_PROVIDER=` line. The revised
`.env.example` uses one shared provider block, so change its values rather than
adding a second block. Existing process environment variables take precedence
over `.env` values.

### 4. Verify Ollama and CRAIG

Check Ollama's compatible API:

```text
curl http://127.0.0.1:11434/v1/models
```

Then run CRAIG's read-only diagnostics.

Windows:

```text
.venv\Scripts\python.exe -m craig doctor
```

macOS/Linux:

```text
.venv/bin/python -m craig doctor
```

The provider check should name `local`, your chosen model, and the
`local_model` data destination.

### 5. Restart and use CRAIG

Stop a running CRAIG backend with `Ctrl+C`, then start it again so it reloads
`.env`:

```text
scripts\start.cmd
```

On macOS/Linux, use:

```text
sh scripts/start.sh
```

Open <http://127.0.0.1:8000> and hard-refresh the page. The provider indicator
should say **Local model** and display the selected model name. The first answer
may be slower while Ollama loads the model.

CRAIG retrieves sources before calling the model. The local model receives the
current question, mode/topic, up to six bounded recent messages, and bounded
retrieved excerpts—not the complete corpus. Always inspect the evidence cards:
small local models can omit citations, use a different convention, or make
overbroad claims even when the connection is functioning correctly.

For each turn, lexical search first returns short match snippets. CRAIG then
reads up to four distinct, highest-ranked source passages and replaces their
snippets with the actual indexed line ranges before answer generation. Each
displayed evidence excerpt is capped at 1,600 characters and is the same
excerpt made available to the model. A lower-ranked result beyond the expansion
limit may still be represented by its shorter search snippet.

### 6. Optionally evaluate the model

This makes three synthetic requests and records whether the model retains
citations, preserves an unknown status, and respects the finite-proof boundary:

Windows:

```text
.venv\Scripts\python.exe -m craig evaluate-model --tier small --confirm-live --output .craig\evaluations\local-small.json
```

macOS/Linux:

```text
.venv/bin/python -m craig evaluate-model --tier small --confirm-live --output .craig/evaluations/local-small.json
```

`--confirm-live` means “contact the configured model.” With the loopback
configuration above, it does not turn the request into a remote API call. A
failed case is a quality warning, not necessarily a connection failure.

## Run a free remote model with Cloudflare Workers AI

Cloudflare Workers AI is CRAIG's recommended free remote option. Retrieval and
the search index remain local; only the bounded answer-generation payload is
sent to the selected Cloudflare-hosted model. The Workers Free plan currently
includes a daily allocation of 10,000 neurons. Review the current
[Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)
before relying on a particular quota.

### 1. Create the Cloudflare credentials

Sign in or create an account in the
[Cloudflare dashboard](https://dash.cloudflare.com/), then open **Workers AI**
and select **Use REST API**. Follow Cloudflare's
[REST API setup instructions](https://developers.cloudflare.com/workers-ai/get-started/rest-api/)
to create a Workers AI API token and copy the 32-character Account ID. The
standard token template grants the Workers AI permissions required for model
inference.

Copy `.env.example` to `.env` if you have not already, then set:

```text
CRAIG_MODEL_PROVIDER=cloudflare
CRAIG_MODEL=@cf/qwen/qwen3-30b-a3b-fp8
CLOUDFLARE_ACCOUNT_ID=your-32-character-account-id
CLOUDFLARE_API_TOKEN=your-secret-api-token
CRAIG_MODEL_TIMEOUT_SECONDS=60
CRAIG_MODEL_MAX_OUTPUT_TOKENS=2000
CRAIG_MODEL_MAX_RESPONSE_BYTES=1048576
```

The recommended initial model is
[`@cf/qwen/qwen3-30b-a3b-fp8`](https://developers.cloudflare.com/workers-ai/models/qwen3-30b-a3b-fp8/),
a Cloudflare-hosted reasoning model with a 32,768-token context window. Model
availability and pricing can change, so use the exact identifier from the
[Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/)
if you select a different text-generation model.

Never paste the token into CRAIG's browser UI, source code, a commit, an issue,
or a screenshot. CRAIG constructs the account-scoped official endpoint itself;
the Cloudflare URL is not user-configurable, and the token remains in the
backend environment.

### 2. Restart and verify CRAIG

Stop a running backend with `Ctrl+C`, restart it with `scripts\start.cmd` on
Windows or `sh scripts/start.sh` on macOS/Linux, and run `craig doctor`. Open
<http://127.0.0.1:8000> and hard-refresh. The provider indicator should display
**Remote model**, `cloudflare`, and the selected model ID.

CRAIG reports quota responses as retryable provider-limit errors and never
silently sends the request to another service. Cloudflare states that it does
not use Workers AI customer content to train models or improve Cloudflare or
third-party services without explicit consent; review the current
[Workers AI data-usage policy](https://developers.cloudflare.com/workers-ai/platform/data-usage/)
before sending unpublished or sensitive work.

Optionally run the three-case remote model evaluation:

```text
craig evaluate-model --tier strong --confirm-live --output .craig/evaluations/cloudflare-strong.json
```

## Run a free remote model with Groq

This option moves answer generation off the local computer while retaining
CRAIG's local, deterministic retrieval. Create a key in the
[Groq console](https://console.groq.com/keys), copy `.env.example` to `.env`,
and set:

```text
CRAIG_MODEL_PROVIDER=groq
CRAIG_MODEL=qwen/qwen3.6-27b
GROQ_API_KEY=your-secret-key
CRAIG_MODEL_TIMEOUT_SECONDS=60
CRAIG_MODEL_MAX_OUTPUT_TOKENS=2000
CRAIG_MODEL_MAX_RESPONSE_BYTES=1048576
```

`qwen/qwen3.6-27b` is the recommended initial mathematical model as of August
2026. `openai/gpt-oss-120b` is a useful comparison candidate. Models, preview
status, and free-plan limits can change, so check Groq's
[model documentation](https://console.groq.com/docs/models) and
[rate-limit table](https://console.groq.com/docs/rate-limits) when configuring
a new installation.

Never paste the key into CRAIG's browser UI, source code, a commit, an issue,
or a screenshot. Stop and restart CRAIG after editing `.env`, then run `craig
doctor`. The browser should display **Remote model**, `groq`, and the selected
model name. A quota response is reported as a retryable provider-limit error;
CRAIG does not silently send the request to another service.

Remote Groq mode sends the bounded answer payload described below to Groq.
According to Groq's current
[data documentation](https://console.groq.com/docs/your-data), inference data
is not retained by default, but inputs and outputs may be logged temporarily
for reliability or abuse monitoring unless the applicable data controls opt
out. Review the current policy before sending unpublished or sensitive work.

Optionally run the same three-case evaluation used for local models:

```text
craig evaluate-model --tier strong --confirm-live --output .craig/evaluations/groq-strong.json
```

`--confirm-live` explicitly acknowledges that this command contacts the remote
provider.

## Use an OpenAI model

Create `.env` from `.env.example`, then set:

```text
CRAIG_MODEL_PROVIDER=openai
CRAIG_MODEL=your-chat-completions-model-id
OPENAI_API_KEY=your-secret-key
```

Select a current model that supports Chat Completions from the
[OpenAI model catalog](https://developers.openai.com/api/docs/models). Restart
CRAIG after editing `.env`. Never place an API key in frontend code, a committed
file, an issue, or a screenshot.

Remote mode sends bounded questions, recent conversation, and retrieved
excerpts to OpenAI. Provider charges, retention, and account policies apply.
CRAIG never returns the key through its public API.

## Use another local inference server

CRAIG can use a different server when it implements the OpenAI-compatible
`POST /v1/chat/completions` response shape and listens on this computer's
loopback interface:

```text
CRAIG_MODEL_PROVIDER=local
CRAIG_MODEL=the-server-model-id
CRAIG_MODEL_BASE_URL=http://127.0.0.1:<port>/v1
CRAIG_MODEL_API_KEY=optional-local-token
```

For safety, CRAIG rejects local-provider hostnames other than `localhost`,
non-loopback IP addresses, credentials embedded in URLs, query strings,
fragments, and HTTP redirects.

## The configuration template

[`.env.example`](.env.example) is the only file users are expected to copy and
edit. CRAIG does not require a personal JSON/YAML/Python configuration file or
an Ollama `Modelfile`. Docker Compose reads the same `.env` values. Optional
Ollama server settings such as `OLLAMA_CONTEXT_LENGTH` and `OLLAMA_NO_CLOUD`
belong to Ollama's application/service environment and are not CRAIG files.

The template also documents optional corpus/index/frontend path overrides and
bounded model-request limits. `CRAIG_ENV_FILE` may be set in the launching
process when the private environment file must live somewhere else.

## Docker

To run the default demonstration in a container:

```text
docker compose up --build
```

Open <http://127.0.0.1:8000>. The container runs unprivileged with a read-only
application filesystem and stores its generated index in the `craig-data`
volume.

The supplied Compose configuration supports `demo`, `cloudflare`, `groq`, and
`openai` through `.env`. A host-installed Ollama service is not part of the
Compose stack; use the native installation for the documented local-model
path. If your existing `.env` selects `local`, change it to `demo`,
`cloudflare`, `groq`, or `openai` before starting the supplied Compose stack.

## Common problems

### PowerShell says `npm.ps1` cannot run

Use `scripts\setup.cmd` or call `npm.cmd`, not `npm`. CRAIG does not require a
PowerShell execution-policy change.

### npm cannot find `package.json`

Frontend npm commands must be run from `app/frontend/`. The platform setup
scripts already change to the correct directory.

### CRAIG still says “Local demonstration”

1. Ensure `.env` is in the repository root.
2. Ensure it has exactly one active `CRAIG_MODEL_PROVIDER=` assignment.
3. Check whether a process-level environment variable is overriding `.env`.
4. Stop and restart the backend.
5. Run `craig doctor`, then hard-refresh the browser.

### CRAIG cannot reach Ollama

Run:

```text
ollama list
curl http://127.0.0.1:11434/v1/models
```

On desktop systems, confirm the Ollama application is running. Use the exact
model name printed by `ollama list` and keep `/v1` at the end of
`CRAIG_MODEL_BASE_URL`.

### The first answer times out

Loading a model on CPU can be slow. Set `CRAIG_MODEL_TIMEOUT_SECONDS=180`, the
maximum accepted value, restart CRAIG, and try again. If the computer is under
heavy memory pressure, choose a smaller model.

### Port 8000 is already in use

Stop the older CRAIG process with `Ctrl+C`, or launch on another port:

```text
python -m craig serve --port 8001
```

## Privacy and trust boundaries

- The default demonstration makes no model or web request.
- Local-provider traffic is restricted to a validated loopback endpoint.
- Remote-provider data is limited but leaves the machine.
- Conversations are held only in backend memory and disappear on restart.
- CRAIG does not provide conversational web search or telemetry.
- Model-generated prose is not repository evidence unless it carries a
  displayed source citation.
- Computation is limited to reviewed, typed operations; models cannot execute
  arbitrary shell commands or repository programs.

Read [the complete privacy and storage description](docs/privacy.md) before
enabling a remote provider.

## Development and further documentation

Run the automated suites:

```text
python -m pytest -q
cd app/frontend
npm.cmd test
npm.cmd run build
```

On macOS/Linux, use `npm` instead of `npm.cmd`.

- [Detailed installation and Docker notes](docs/installation.md)
- [Provider limits and evaluation](docs/model-configuration.md)
- [Privacy and conversation storage](docs/privacy.md)
- [Versioned feature ledger](docs/features.md)
- [Architecture, mathematical scope, and roadmap](Combinatorics_README.md)
