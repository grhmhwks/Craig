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

When `CRAIG_MODEL_PROVIDER=cloudflare`, `groq`, or `openai`, CRAIG sends the
following to the selected remote provider:

- the current question and selected conversation mode/topic;
- up to six recent bounded conversation messages;
- bounded retrieved excerpts with citation, path, line, and status metadata
  (up to four ranked passages are expanded; every displayed/model-visible
  excerpt is capped at 1,600 characters);
- CRAIG's answer-generation system instructions.

It does not upload the whole corpus, generated index, computation worker state,
or arbitrary files. The provider's own retention, training, abuse-monitoring,
regional-processing, and account policies apply. Review those policies before
enabling remote mode.

The `cloudflare` preset sends requests only to an account-scoped path on the
fixed `https://api.cloudflare.com` host. The Account ID is validated before it
is inserted into that path. Cloudflare states that Workers AI customer content
is not used to train models or improve Cloudflare or third-party services
without explicit consent. Cloudflare may process customer content to provide
the service, and content can be stored when the customer separately uses a
Cloudflare storage service with Workers AI. Review the current
<https://developers.cloudflare.com/workers-ai/platform/data-usage/> policy
before sending unpublished, confidential, or sensitive material.

The `groq` preset sends requests only to the fixed
`https://api.groq.com/openai/v1` endpoint. Groq currently states that inference
data is not retained by default, while allowing temporary logging for service
reliability or abuse monitoring unless applicable data controls opt out. This
policy can change; review <https://console.groq.com/docs/your-data> before
sending unpublished, confidential, or sensitive material. The `openai` preset
similarly uses only the fixed official OpenAI endpoint and remains subject to
the configured account's current terms and controls.

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
