# Privacy and local data behavior

## Default behavior

The default `demo` provider performs no model or web request. Search, retrieval,
conversation orchestration, rendering, and approved computation remain on the
machine running CRAIG. CRAIG includes no telemetry, analytics, advertising,
external web-search tool, or background upload.

The mathematical `content/` corpus is read-only. The generated SQLite search
index is stored at `.craig/index.sqlite3` by default, outside the corpus.
Isolated computation workers use temporary directories outside the repository
and delete them at job termination.

## Conversation and computation storage

Conversation history is held only in backend process memory. It is not written
to SQLite, files, browser local storage, cookies, or `content/`, and disappears
when the backend stops. Starting a new conversation removes the active browser
view, while restarting the backend clears all server conversations.

Computation results and trace frames remain in the current browser component
state. The backend streams them but does not persist them. Reproducibility hashes
identify request/result content; they are not remote storage identifiers.

Normal server access logs may contain HTTP paths, response status, timing, and
the connecting IP address. CRAIG does not intentionally log request bodies,
conversation text, retrieved excerpts, or model keys.

## Opt-in model providers

When `CRAIG_MODEL_PROVIDER=openai`, CRAIG sends the following to the configured
remote provider:

- the current question and selected conversation mode/topic;
- up to six recent bounded conversation messages;
- bounded retrieved excerpts with citation, path, line, and status metadata;
- CRAIG's answer-generation system instructions.

It does not upload the whole corpus, generated index, computation worker state,
or arbitrary files. The provider's own retention, training, abuse-monitoring,
regional-processing, and account policies apply. Review those policies before
enabling remote mode.

When `CRAIG_MODEL_PROVIDER=local`, the same bounded payload is sent only to a
validated loopback endpoint. The browser visibly labels remote or local model
mode before the user sends a message.

## Secrets

API keys stay in the backend environment or local `.env` file. `.env` is
ignored by Git, and `.env.example` contains placeholders only. Public API
configuration and health responses include provider name, model, configured
state, and the local/remote destination category, but never keys, authorization
headers, response bodies from failed providers, or endpoint credentials.

Anyone with access to the host process, its environment, a readable `.env`, or
container configuration may still be able to obtain its secrets. Use normal OS
permissions or a platform secret manager for shared deployments.
