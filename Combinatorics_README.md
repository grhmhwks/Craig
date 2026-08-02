# Combinatorics

This repository contains the [`content`](content/) directory—a collection of
largely self-contained notes on combinatorics—and the initial local CRAIG
tooling. The corpus includes conjectures, proofs and proof outlines,
computational evidence, computer-assisted proof material, reference
implementations, optimized programs, examples, and related research summaries.
Each topic has its own documentation; begin with
[`content/README.md`](content/README.md) and then the relevant `explanation.tex`.

The local index/search milestone, Phase 2 read-only retrieval API, Phase 3
conversational application, Phase 4 provenance interface, Phase 5 mathematical
rendering, Phase 6 approved computation, Phase 7 algorithm traces and
animation, and Phase 8 release packaging are implemented in CRAIG 1.0.
The application is
**CRAIG—the Combinatorial Research Assistance Interactive Guide**: an
open-source, AI-powered application for searching, understanding, visualizing,
and computationally exploring the mathematics contained here.

## Quick start

On Windows, run from the repository root:

```text
scripts\setup.cmd
scripts\start.cmd
```

On macOS or Linux:

```text
sh scripts/setup.sh
sh scripts/start.sh
```

Then open `http://127.0.0.1:8000`. Docker users may instead run
`docker compose up --build`. See [`docs/installation.md`](docs/installation.md)
for manual installation, development-server, diagnostics, upgrade, and
container details.

## Local index and search (Milestone 1)

CRAIG currently provides a dependency-light, read-only command-line index over
the supported source files in `content/`. It requires Python 3.10 or newer with
SQLite FTS5 enabled; no application dependencies are needed. From the repository
root, run:

```text
python -m craig index
python -m craig search "natural language or mathematical query"
```

The generated database is `.craig/index.sqlite3` and is ignored by Git. Normal
indexing hashes every supported source file and skips unchanged files. To
recreate the database, or to restrict and size a search, use:

```text
python -m craig index --rebuild
python -m craig search "strict dominance" --topic string_decompositions
python -m craig search "tableau insertion" --limit 10
```

`explanation.tex` passages receive a default ranking multiplier of `1.5`. Set
`CRAIG_EXPLANATION_BOOST` or pass `--explanation-boost` to change it. Search is
lexical SQLite FTS5 search in this milestone: the index command itself makes no
model calls and performs no corpus code execution.

For development, install the test extra and run the suite:

```text
python -m pip install -e ".[dev]"
python -m pytest -q
```

Markdown, TeX, and Python are chunked using their headings, mathematical
environments, and AST symbols. C/C++ uses a lightweight signature-and-balanced-
brace heuristic (not a full parser), with bounded overlapping line chunks to
keep any unrecognized source searchable.

## Read-only retrieval API (Phase 2)

Phase 2 exposes the index through a framework-independent Python service and a
versioned local HTTP API. Install the project, build the index, and start the
API from the repository root:

```text
python -m pip install -e ".[dev]"
python -m craig index
python -m craig serve
```

The server binds to `127.0.0.1:8000` by default. Interactive OpenAPI
documentation is available at `http://127.0.0.1:8000/docs`. Use `--host` and
`--port` to change the listener. `CRAIG_CONTENT_ROOT` and `CRAIG_INDEX_PATH`
may override the default locations when an alternate approved local layout is
needed.

All public operations are read-only:

| Operation | HTTP endpoint | Purpose |
| --- | --- | --- |
| `list_topics` | `GET /api/v1/topics` | List indexed topics with file and chunk counts. |
| `search_content` | `POST /api/v1/search` | Run ranked global or topic-scoped lexical search. |
| `find_exact` | `POST /api/v1/find-exact` | Locate literal text or notation at exact source lines. |
| `read_source` | `POST /api/v1/read-source` | Read a bounded line range from an indexed source. |

Every source result includes its topic, corpus-relative path, file type,
structural heading/environment when available, exact line bounds, and indexed
SHA-256. Search and exact-match responses support `limit`, `offset`, and
`next_offset` for iterative calls. Query length, result count, source lines,
per-excerpt size, and total returned text have server-side caps; `truncated`
and continuation fields report when a response was bounded.

`read_source` accepts only normalized POSIX paths already present in the index.
Absolute paths, traversal components, Windows separators, unindexed files, and
symlink escapes are rejected. Source reads verify the indexed hash and report a
stale index instead of mixing index metadata with changed source text. Retrieval
connections open SQLite in enforced read-only mode and never write beneath
`content/`.

## Conversational interface (Phase 3)

Phase 3 adds a React and TypeScript browser interface, an in-memory conversation
store, separate search-planning and grounded-answer prompts, and a bounded
orchestration loop over the four Phase 2 retrieval operations. Assistant
progress, tool activity, answer text, and completion metadata stream as typed
Server-Sent Events.

For frontend development, run the backend and Vite development server in
separate terminals:

```text
python -m craig serve
```

```text
cd app/frontend
npm install
npm run dev
```

Open `http://127.0.0.1:5173`. To create a production frontend and let the Python
server serve it at `http://127.0.0.1:8000`, run:

```text
cd app/frontend
npm install
npm run build
cd ../..
python -m craig serve
```

The Phase 3 chat endpoints are:

| HTTP endpoint | Purpose |
| --- | --- |
| `GET /api/v1/chat/config` | Return public modes, limits, and non-secret provider status. |
| `POST /api/v1/chat/stream` | Start or continue a turn and stream typed SSE events. |
| `GET /api/v1/conversations/{id}` | Read an active in-memory conversation. |

Research, Explanation, Tutorial, and Computation modes are available globally
or within one indexed topic. Computation-mode chat retrieves relevant code and
mathematical context. A separate typed panel dispatches only the reviewed,
resource-limited operations supplied by Phases 6 and 7.

`CRAIG_MODEL_PROVIDER` selects the backend provider. The default is `demo`, a
deterministic retrieval presentation that exercises the full interface without
a network credential:

```text
CRAIG_MODEL_PROVIDER=demo
```

CRAIG 1.0 also ships opt-in `openai` and loopback-only `local` adapters;
`CRAIG_MODEL` selects their model. Unsupported or incomplete selections are
reported as unavailable rather than silently falling back. Provider credentials
are never read by the frontend or returned by a public endpoint. See
[`docs/model-configuration.md`](docs/model-configuration.md).

Conversation history is bounded, process-local memory. It is cleared whenever
the backend restarts and is not written to the repository. External web search,
semantic retrieval, and arbitrary code execution remain outside this boundary;
the trusted mathematical renderers are supplied separately by Phase 5.

## Provenance and mathematical status (Phase 4)

Phase 4 makes the evidence behind an answer inspectable. Each cited repository
passage now has a stable citation identifier, corpus-relative file, structural
heading and environment, exact line range, indexed SHA-256, bounded text
excerpt, mathematical-status label, and an explanation of the status basis when
one exists. The `sources.ready` SSE event exposes this metadata before answer
streaming finishes, and completed messages retain it for follow-up turns.

The browser displays inline citation identifiers and expandable evidence cards.
Each card shows the file, heading, theorem-like environment, lines, status,
excerpt, and hash. Answer-level provenance notes distinguish:

- explicit repository material;
- CRAIG deductions or retrieval-based synthesis;
- general model knowledge;
- external information.

The external category is reserved for contract compatibility but is not emitted
because external search remains disabled.

Mathematical status is intentionally conservative. CRAIG recognizes explicit
theorem-like and conjecture environments and explicit headings such as
“computer-assisted proof,” “computational evidence,” “proof outline,” and “work
in progress.” Anything else remains **status unknown**. It does not infer status
from a filename or topic name.

The grounded-answer prompt requires citation identifiers, keeps deductions
separate from source statements, preserves unknown status, refuses to promote
finite evidence into a general proof, and distinguishes exploratory computation
from an exhaustive finite check. The full Phase 4 contract is recorded in
[`docs/phase-4-plan.md`](docs/phase-4-plan.md).

## Mathematical rendering (Phase 5)

Assistant messages now support safe Markdown, inline and display TeX through
KaTeX, and bounded JSON visualization blocks. The trusted renderer families are
ordinary, shifted, primed, and set-valued tableaux; Young, shifted, and skew
diagrams; ordinary and rational Dyck paths; reading words; factorizations;
skeletons; and string diagrams.

Raw answer HTML is disabled. Each visualization is schema-validated before
React constructs its HTML or SVG, and invalid or oversized blocks retain a
readable text fallback. The answer prompt documents the same schemas and tells
providers not to invent mathematical data simply to create a graphic. Use
**Preview renderers** in the desktop sidebar for the built-in manual gallery.
The schemas, examples, limits, security boundary, and review procedure are in
[`docs/phase-5-rendering.md`](docs/phase-5-rendering.md).

## Approved computation (Phase 6)

Computation mode now includes a schema-driven panel for five reviewed jobs:
classical Dyck statistics, bounded classical Dyck enumeration, bounded rational
Dyck enumeration, type C 0-Hecke word evaluation, and ordinary tableau row
insertion. Natural-language chat cannot create a command; it remains a
read-only retrieval conversation.

Every job runs in a fresh isolated process outside the repository, accepts only
normalized JSON parameters, and is governed by CPU, memory, wall-time, request,
stdout, stderr, and concurrency limits. Windows workers use one-process Job
Objects; POSIX workers use process groups and resource limits. The kernels live
outside `content/`, have no filesystem or network capability, and never import,
compile, or execute a corpus program.

Results stream progress and retain normalized parameters, evidence
classification, exact output, trusted visualization data, implementation and
source hashes, request/result hashes, runtime measurements, and the governing
limits. Finite checks are explicitly limited to their displayed parameters and
are never described as general proofs. See
[`docs/phase-6-computation.md`](docs/phase-6-computation.md) and the static
[`docs/phase-6-inventory.md`](docs/phase-6-inventory.md).

## Algorithm traces and animation (Phase 7)

Selected bounded computations now return a versioned deterministic trace in
addition to their exact result. Ordinary row insertion shows insertion,
bumping, and recording-tableau updates; Dyck-path statistics show incremental
path construction; and type C 0-Hecke evaluation shows each local move on a
signed-permutation skeleton. The row-insertion operation is explicitly the
ordinary RSK baseline discussed by the corpus, not the specialized chunked
Dyck insertion procedure.

The browser validates the entire trace and each embedded visualization before
rendering it. Users can move to the first, previous, next, or last frame, use a
scrubber, select autoplay speed, navigate with the keyboard, and inspect the
exact JSON mathematical state at every step. Autoplay is disabled when the
operating system requests reduced motion. Invalid or oversized traces produce
a readable fallback and do not render their contents as markup.

The event vocabulary, byte and event limits, selected algorithms, keyboard
controls, security boundary, and validation procedure are documented in
[`docs/phase-7-traces.md`](docs/phase-7-traces.md).

## Release packaging, models, and privacy (Phase 8)

CRAIG 1.0 adds cross-platform setup/launch scripts, the installed `craig`
command, secret-free diagnostics and health reporting, a production frontend,
and optional hardened Docker packaging. `.env.example` documents configuration
without containing credentials.

The deterministic `demo` provider remains the no-network default. Operators
may explicitly enable a remote OpenAI provider or a loopback-only local
OpenAI-compatible endpoint. Retrieval planning stays deterministic and
allowlisted; only bounded answer context reaches a live model. The browser
labels the data destination, and keys remain server-only. See
[`docs/model-configuration.md`](docs/model-configuration.md) and
[`docs/privacy.md`](docs/privacy.md).

A common synthetic evaluation checks citation retention, finite-evidence
boundaries, and unknown-status preservation for both strong and small model
profiles. Mock transports validate this workflow in normal tests; live runs
require explicit operator confirmation and never receive an invented pass. The
versioned implemented/planned ledger is in
[`docs/features.md`](docs/features.md).

## Project vision

CRAIG is intended to make a research repository behave more like an interactive mathematical library than a static collection of papers and code.

A user should be able to ask a precise question such as

> Where is the strict-dominance argument used in the shifted Littlewood–Richardson computations?

or a less formal conceptual question such as

> Do any of the projects use the same kind of local-to-global proof strategy?

CRAIG should locate relevant material even when the user does not know the repository's terminology, explain the result at an appropriate level, distinguish source statements from new deductions, display the underlying combinatorial objects, and—when useful—run approved repository computations to generate examples or reproduce finite checks.

The primary goal is **not** to create a general-purpose mathematics chatbot. CRAIG's first responsibility is to help users discover and understand what is in this repository, what follows from it, how the different topics relate, and how the accompanying computations support the mathematics.

## Intended audience

CRAIG is designed around a central audience, with useful coverage on both sides of it.

### Core audience

- Mathematicians working in combinatorics or in closely related areas of algebra.
- Mathematicians in other fields who are interested in AI-assisted mathematical communication, especially communication across fields.
- AI and computer-science researchers interested in how well relatively modest models can understand and explain mathematics when they are given strong retrieval, provenance, rendering, and computation infrastructure.

### More specialized users

Researchers and other professionals in combinatorics who already know some of the relevant problems should be able to use CRAIG as a fast research index, source navigator, example generator, and interactive technical guide.

### Broader users

Engineers, scientists, students interested in mathematics or AI, and other technically curious readers should be able to use CRAIG as a patient tutor. They may not follow every proof, but they should be able to understand the central objects, motivations, examples, and research questions, and to see how AI can be integrated into a serious mathematical web application.

## Planned user experience

CRAIG will support both of the following entry points:

1. **Global exploration.** A conversation can search across the entire repository and identify connections between topics.
2. **Topic-scoped exploration.** A user can enter a particular topic folder and begin a conversation whose searches are initially restricted to that material.

The assistant will adapt its explanations to the conversation, while also offering explicit modes:

- **Research mode:** precise statements, hypotheses, dependencies, source comparison, and minimal introductory exposition.
- **Explanation mode:** motivation, definitions, examples, and a guided account of the main argument.
- **Tutorial mode:** small steps, frequent examples, careful unpacking of notation, and patient responses to follow-up questions.
- **Computation mode:** executable examples, algorithms, finite checks, performance information, and interpretation of computational output.

The selected mode will guide the response but will not rigidly constrain it. Users should be able to move naturally between modes in one conversation.

## Mathematical authority and provenance

CRAIG will use four kinds of information, in the following order of authority:

1. **Statements explicitly present in the repository.**
2. **Deductions made from repository statements.**
3. **General mathematical knowledge supplied by the model.**
4. **External web sources, if web access is enabled.**

The interface must keep these categories distinct. In particular:

- Repository-based claims should cite the relevant topic, file, section, theorem, definition, code location, or line range.
- A deduction not explicitly stated in the source should be labeled as a deduction.
- General model knowledge should not silently override repository definitions or conventions.
- External sources, if supported, should be visibly separate from repository sources.
- When sources disagree or use different conventions, CRAIG should explain the difference rather than blend them together.

CRAIG should also display the mathematical status of material whenever that status matters. Planned labels include:

- **proved result**;
- **computer-assisted proof**;
- **conjecture**;
- **computational evidence**;
- **experimental observation**;
- **proof outline**;
- **work in progress**.

This distinction is essential. Some programs in `content` provide exploratory evidence, while others exhaust exactly the bounded cases left after a symbolic reduction and therefore form an actual step in a proof.

## Planned conversational architecture

The basic response pipeline will separate retrieval planning from answer generation.

```text
User query + conversation context
        |
        v
Initial system prompt
        |
        v
Search-planning model
        |
        |  tool calls such as search, read, find, and approved computation
        v
CRAIG executes tools against the local repository
        |
        |  the model may refine the search and request more material
        v
Secondary system prompt
+ original user query
+ relevant conversation context
+ retrieved passages and source metadata
+ approved computation results, when used
        |
        v
Answer-generation model
        |
        v
Markdown/LaTeX response
+ citations
+ typed combinatorial visualization blocks
        |
        v
CRAIG user interface
```

The search phase will not be restricted to one tool call. A good answer may require an iterative sequence such as

```text
list relevant topics
    -> search for a concept
    -> read the surrounding definition
    -> locate a cited lemma
    -> inspect the accompanying code
    -> generate a small example
    -> answer
```

The search-planning model and answer-generation model may initially be the same model, but the architecture should allow different models to be used for the two roles.

### Phase 3 implementation defaults

The first conversational interface will use the following boundaries:

- the frontend will use React and TypeScript;
- streamed assistant events will use Server-Sent Events over HTTP;
- conversation state will remain in backend memory for the initial release and
  will not be persisted;
- the model layer will use a provider-neutral backend adapter, with a
  deterministic fake provider for orchestration tests and provider credentials
  supplied only through backend configuration;
- search planning and answer generation may use the same configured model, but
  will remain separate orchestration stages with separate prompts;
- Research, Explanation, Tutorial, and Computation will initially be prompt and
  presentation modes over the same retrieval boundary;
- Computation mode will not execute repository programs until the reviewed,
  isolated computation layer in Phase 6 exists;
- external web search will not be part of the Phase 3 tool set;
- retrieval provenance will remain attached to conversation events so Phase 4
  can add richer citation and mathematical-status presentation without changing
  the orchestration contract.

## Repository retrieval and indexing

CRAIG should automatically discover new topic folders that follow the repository's conventions. Adding a new folder with an `explanation.tex` and related source files should not require application code changes.

### Files indexed by default

The initial index should focus on curated source material, including:

- `.tex`;
- `.md`;
- `.py`;
- `.cpp` and related source-code files;
- selected structured data files explicitly included by a topic.

Generated and build artifacts should normally be excluded, including:

- `.aux`;
- `.log`;
- `.synctex.gz`;
- compiled PDFs when the corresponding source is available;
- executables, caches, temporary files, and generated output.

A later manifest may allow a topic to opt specific supporting files into or out of the index.

### Index structure

The index should preserve enough structure to support accurate mathematical citation and retrieval:

- topic folder;
- relative path;
- document type;
- section and subsection headings;
- theorem, lemma, proposition, definition, conjecture, proof, example, and algorithm environments;
- function, class, and command-line entry points in source code;
- line ranges;
- declared mathematical status;
- links between exposition and accompanying code.

`explanation.tex` should normally receive greater retrieval weight because it is the intended entry point for a topic. Exact lexical search remains important for mathematical notation and named results, while semantic search should support conceptual or “vibe-level” queries whose wording does not match the source.

A likely first implementation is hybrid retrieval:

- SQLite FTS5 or an equivalent full-text index for exact and lexical search;
- optional embeddings for semantic similarity;
- repository-specific reranking based on topic, file role, headings, and source status.

The retrieval implementation is provisional and should be evaluated against a set of real questions drawn from the repository.

## Mathematical rendering and visualization

Ordinary prose and mathematics should be rendered from Markdown with high-quality LaTeX support, likely through KaTeX or an equivalent browser renderer.

CRAIG will also support deterministic renderers for combinatorial objects. The model should return typed, declarative specifications rather than arbitrary HTML, JavaScript, or SVG. For example:

````text
```tableau
{
  "rows": [["1", "2'"], ["3"]],
  "shifted": true,
  "orientation": "top-to-bottom"
}
```
````

The frontend will validate the specification and pass it to a trusted renderer.

Planned visualization types include:

- ordinary, rational, and related Dyck paths;
- Young diagrams, shifted diagrams, skew shapes, and partitions;
- ordinary, shifted, marked, primed, and set-valued tableaux;
- reading words and factorizations;
- skeletons and string decompositions;
- posets, small graphs, and permutation diagrams when needed;
- specialized notation for insertion and local-move algorithms.

A later goal is **dynamic algorithm visualization**. For insertion procedures, the interface should be able to animate:

- the entry currently being inserted;
- the box being examined;
- one entry bumping another;
- row or column transitions;
- recording-tableau updates;
- the evolving insertion and recording objects;
- forward, backward, pause, and step controls.

The mathematical state—not a prerecorded animation—should determine each frame so that the visualization can be generated from examples produced by repository code.

## Code and computation

The code in `content` is part of the mathematical library and should be integrated into CRAIG rather than treated as passive text.

The planned execution model has two levels:

1. **Curated commands.** CRAIG may run reviewed repository commands with validated parameters.
2. **Approved mathematical functions.** CRAIG may call registered functions through typed interfaces to generate examples, statistics, diagrams, and finite checks.

Examples of future tools might include:

```text
generate_dyck_paths(n=6)
render_rational_path(r=5, s=3, index=2)
run_formula_check(r=5, s=3)
generate_shifted_tableaux(shape=[4,2], max_entries=6)
trace_insertion(word=[...])
```

The initial application will **not** execute arbitrary model-generated shell commands, Python, or C++. Computation must remain tied to reviewed repository routines or explicitly approved wrappers.

Execution should be:

- read-only with respect to the repository;
- isolated from the host system;
- subject to CPU, memory, output-size, and runtime limits;
- reproducible, with the command, parameters, software version, and relevant source revision displayed;
- explicit about whether a run is an example, an experiment, a sanity check, or a finite proof obligation;
- able to stream progress for computations whose educational value includes seeing the cost of exhaustive verification.

Large optimized computations may be documented and inspectable even when they are not appropriate to run in an ordinary local session. Smaller reference implementations should be available for hands-on exploration.

## Read-only design

CRAIG is intended as an exploration, explanation, visualization, and computation interface. It will not edit the repository.

In particular, the application should not:

- modify source files;
- rewrite proofs or code in place;
- create commits or branches;
- apply patches;
- alter recorded computational results.

A user may ask CRAIG to discuss possible corrections or extensions, but any such proposal should remain in the conversation and should not be written into the repository by the application.

## Model access

The application should not depend permanently on one commercial provider. The model layer should be provider-neutral and support at least the following deployment patterns:

- a user-supplied API key for a supported remote provider;
- a local model served through a compatible local inference service;
- additional provider adapters added without changing the retrieval, rendering, or computation layers.

The project will not rely on a shared public API key committed to the repository. Secrets must remain outside the frontend and outside version control.

CRAIG 1.0 uses the deterministic no-network provider by default and supports an
operator-configured remote OpenAI model or local OpenAI-compatible model. Exact
live model selection remains an operator decision and should favor:

- easy setup for users who fork the repository;
- reliable structured tool calling;
- sufficient mathematical competence for repository-grounded explanations;
- support for long enough contexts to use retrieved material effectively;
- predictable cost, privacy, and availability.

A relatively small or inexpensive model should still be useful when the surrounding infrastructure supplies accurate retrieval, explicit provenance, deterministic rendering, and controlled computation. Evaluating that claim is itself one of the project's research interests.

## External web search

CRAIG 1.0 has no conversational web-search capability. Whether a future release
should add opt-in external search remains undecided.

Possible policies include:

- no web access, making the repository the complete information boundary;
- opt-in web access for references, later literature, and external definitions;
- web access only after repository retrieval has been exhausted;
- separate repository and web search modes.

Any implementation must preserve the authority order described above and must never make an external source appear to be part of the repository.

## Provisional technical stack

The following stack is a practical starting point rather than a final commitment:

### Frontend

- React and TypeScript;
- Markdown rendering with KaTeX-compatible mathematics;
- custom React/SVG combinatorial renderers;
- streaming chat responses;
- source and provenance panels;
- global and topic-scoped navigation;
- optional animation controls for algorithms.

### Backend

- Python with FastAPI or an equivalent framework;
- repository indexing and retrieval services;
- model-provider adapters;
- prompt and tool orchestration;
- controlled computation workers;
- a local SQLite database for indexes, metadata, settings, and optionally conversation history.

### Search

- section-aware parsing of TeX and Markdown;
- function-aware parsing of Python and C++;
- lexical search through SQLite FTS5 or an equivalent engine;
- optional vector search and reranking;
- source-location metadata attached to every returned passage.

### Packaging

CRAIG 1.0 supports both of these local launch paths:

```text
Docker Compose
```

and a non-Docker development path such as

```text
backend setup
frontend setup
single local launch command
```

The platform setup/start scripts provide a unified non-Docker path, while
`docker compose up --build` provides the container path. Both build generated
artifacts outside the protected `content/` corpus.

A likely future repository layout is:

```text
Combinatorics/
├── content/
├── app/
│   ├── backend/
│   │   ├── api/
│   │   ├── indexing/
│   │   ├── retrieval/
│   │   ├── models/
│   │   ├── computation/
│   │   └── prompts/
│   └── frontend/
│       └── src/
│           ├── chat/
│           ├── sources/
│           ├── topics/
│           └── renderers/
├── tests/
├── scripts/
├── .env.example
├── docker-compose.yml
└── README.md
```

## Planned implementation roadmap

The ordering below is a working to-do list, not a promise that every detail will remain unchanged.

### Phase 0 — Curate the repository

- [ ] Remove or ignore generated TeX artifacts and temporary files.
- [ ] Correct accidental filenames and double extensions.
- [ ] Confirm a consistent topic-folder convention.
- [ ] Decide whether each topic needs a small metadata file.
- [ ] Record each document's mathematical status where it cannot be inferred safely.
- [ ] Identify the canonical source file when several versions of the same material exist.
- [ ] Define links between `explanation.tex`, reference code, optimized code, data, and specialized proof notes.

### Phase 1 — Build the local mathematical index

- [ ] Discover topic folders automatically.
- [ ] Parse Markdown and TeX by structural units rather than arbitrary token windows.
- [ ] Parse Python and C++ by functions, classes, docstrings, and command-line entry points.
- [ ] Store paths, line ranges, headings, environments, and source status.
- [ ] Implement exact and full-text search.
- [ ] Evaluate semantic search and embeddings.
- [ ] Add repository-specific reranking.
- [ ] Build a repeatable index-refresh command.
- [ ] Create retrieval tests based on real repository questions.

### Phase 2 — Implement the retrieval API

- [x] Define read-only tools such as `list_topics`, `search_content`, `find_exact`, and `read_source`.
- [x] Return source metadata with every result.
- [x] Support global and topic-scoped search.
- [x] Support iterative search calls.
- [x] Prevent path traversal and access outside approved repository directories.
- [x] Add result-size and context-budget controls.

### Phase 3 — Implement the first conversational interface

- [x] Build the chat frontend.
- [x] Add streaming responses.
- [x] Implement the initial and secondary system prompts.
- [x] Build the search-planning and answer-generation orchestration loop.
- [x] Preserve relevant conversation context for follow-up questions.
- [x] Add Research, Explanation, Tutorial, and Computation modes.
- [x] Let users begin globally or inside a topic.
- [x] Add model-provider configuration without exposing secrets to the browser.

### Phase 4 — Add provenance and mathematical-status handling

The implementation contract and acceptance criteria are recorded in
[`docs/phase-4-plan.md`](docs/phase-4-plan.md).

- [x] Display file, section, theorem, and line-level citations.
- [x] Add expandable source excerpts.
- [x] Label source statements, deductions, model knowledge, and external information separately.
- [x] Add proved/conjectural/computational/work-in-progress labels.
- [x] Teach the prompts not to convert finite evidence into a general proof.
- [x] Teach the prompts to distinguish exploratory computation from exhaustive proof obligations.
- [x] Add tests for conflicting definitions and conventions across topics.

### Phase 5 — Add core mathematical rendering

- [x] Render Markdown and LaTeX reliably.
- [x] Define schemas for trusted visualization blocks.
- [x] Implement ordinary and shifted tableaux.
- [x] Implement set-valued and primed tableaux.
- [x] Implement Young, shifted, and skew diagrams.
- [x] Implement ordinary and rational Dyck paths.
- [x] Implement reading words, factorizations, and skeleton/string diagrams.
- [x] Provide graceful text fallbacks for invalid visualization specifications.

### Phase 6 — Integrate approved computation

- [x] Inventory lightweight and heavyweight programs.
- [x] Select safe curated commands for the first release.
- [x] Wrap approved mathematical functions in typed interfaces.
- [x] Validate all parameters.
- [x] Run computations in isolated workers.
- [x] Enforce CPU, memory, runtime, and output limits.
- [x] Stream progress and preserve reproducibility metadata.
- [x] Connect computation output to visualization renderers.
- [x] Clearly label examples, experiments, finite checks, and computer-assisted proof runs.

### Phase 7 — Add algorithm traces and animation

- [x] Define a general event schema for insertion, bumping, extraction, reinsertion, and local moves.
- [x] Modify or wrap selected algorithms so they emit deterministic traces.
- [x] Implement step-by-step controls.
- [x] Animate tableau insertion and recording.
- [x] Animate path and skeleton transformations where useful.
- [x] Let users inspect the mathematical state attached to each animation step.

### Phase 8 — Package, test, and document CRAIG

- [x] Provide a simple local installation path.
- [x] Add Docker support because it materially simplifies mixed Python/Node setup.
- [x] Provide `.env.example` without secrets.
- [x] Document remote and local model configuration.
- [x] Add Windows, macOS, and Linux launch instructions.
- [x] Add unit, integration, retrieval, rendering, and computation tests.
- [x] Add identical strong/small evaluation profiles, mocked contract tests, and opt-in live runs.
- [x] Add accessibility support and keyboard navigation.
- [x] Document privacy and conversation-storage behavior.
- [x] Provide a clear versioned list of implemented and planned features.

## Open design decisions

The following choices remain intentionally unresolved:

- Which embedding and reranking methods perform best on this repository?
- Should later versions persist conversation history locally or make persistence user-configurable?
- Which additional computations merit a future allowlist revision?
- Which additional combinatorial visualization schemas should follow the Phase 5 core set?
- What resource limits best balance safety, reproducibility, and hands-on experimentation?
- How should CRAIG evaluate explanation quality across different mathematical backgrounds?
- How much capability can be obtained from relatively small models once the surrounding infrastructure is strong?

## Current status

**Current:** the repository contains the mathematical material under
[`content`](content/), the Milestone 1 local FTS5 index/search commands, the
Phase 2 read-only retrieval service and HTTP API, and the Phase 3 browser
conversation interface and orchestration layer described above. Phase 4 adds
stable citations, bounded source excerpts, explicit provenance categories,
conservative mathematical-status handling, and expandable evidence panels.
Phase 5 adds safe Markdown and TeX plus schema-validated mathematical
visualizations and readable invalid-block fallbacks. Phase 6 adds typed,
allowlisted, isolated computation with resource limits, progress events,
reproducibility metadata, and trusted visualization handoff.
Phase 7 adds a bounded event contract, deterministic tableau/path/skeleton
traces, accessible playback controls, and inspectable per-step state.
Phase 8 packages these capabilities as CRAIG 1.0 with cross-platform and Docker
launch paths, diagnostics, opt-in remote/local model synthesis, shared model
evaluations, accessibility disclosures, and explicit privacy/storage behavior.

**Not implemented in 1.0:** semantic retrieval, external conversation web
search, or persistent conversation storage. The deterministic provider remains
fully usable without credentials. Live model quality is reported only by an
explicit evaluation run against an operator-supplied model.

## Open-source status

CRAIG is intended to be developed as an open-source project. The repository should make the mathematical sources, application architecture, renderers, retrieval methods, approved computation wrappers, and evaluation procedures inspectable and reproducible.

## Name

**CRAIG** stands for **Combinatorial Research Assistance Interactive Guide**.
