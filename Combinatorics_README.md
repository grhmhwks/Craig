# Combinatorics

This repository contains the [`content`](content/) directory—a collection of
largely self-contained notes on combinatorics—and the initial local CRAIG
tooling. The corpus includes conjectures, proofs and proof outlines,
computational evidence, computer-assisted proof material, reference
implementations, optimized programs, examples, and related research summaries.
Each topic has its own documentation; begin with
[`content/README.md`](content/README.md) and then the relevant `explanation.tex`.

Milestone 1—the local index and search command below—is implemented. The rest
of the application is a work in progress. Its intended final form is
**CRAIG—the Combinatorial Research Assistance Interactive Guide**: an
open-source, AI-powered application for searching, understanding, visualizing,
and computationally exploring the mathematics contained here.

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
lexical SQLite FTS5 search in this milestone: there are no embeddings, model
calls, code execution, web interface, or diagram renderer.

For development, install the test extra and run the suite:

```text
python -m pip install -e ".[dev]"
python -m pytest -q
```

Markdown, TeX, and Python are chunked using their headings, mathematical
environments, and AST symbols. C/C++ uses a lightweight signature-and-balanced-
brace heuristic (not a full parser), with bounded overlapping line chunks to
keep any unrecognized source searchable.

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

The exact initial provider and model remain open design decisions. The default should favor:

- easy setup for users who fork the repository;
- reliable structured tool calling;
- sufficient mathematical competence for repository-grounded explanations;
- support for long enough contexts to use retrieved material effectively;
- predictable cost, privacy, and availability.

A relatively small or inexpensive model should still be useful when the surrounding infrastructure supplies accurate retrieval, explicit provenance, deterministic rendering, and controlled computation. Evaluating that claim is itself one of the project's research interests.

## External web search

Whether CRAIG should have access to external web search is not yet decided.

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

The eventual local launch experience should be simple. Possible supported paths include:

```text
Docker Compose
```

and a non-Docker development path such as

```text
backend setup
frontend setup
single local launch command
```

These commands do not exist yet. They are part of the planned implementation.

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

- [ ] Define read-only tools such as `list_topics`, `search_content`, `find_exact`, and `read_source`.
- [ ] Return source metadata with every result.
- [ ] Support global and topic-scoped search.
- [ ] Support iterative search calls.
- [ ] Prevent path traversal and access outside approved repository directories.
- [ ] Add result-size and context-budget controls.

### Phase 3 — Implement the first conversational interface

- [ ] Build the chat frontend.
- [ ] Add streaming responses.
- [ ] Implement the initial and secondary system prompts.
- [ ] Build the search-planning and answer-generation orchestration loop.
- [ ] Preserve relevant conversation context for follow-up questions.
- [ ] Add Research, Explanation, Tutorial, and Computation modes.
- [ ] Let users begin globally or inside a topic.
- [ ] Add model-provider configuration without exposing secrets to the browser.

### Phase 4 — Add provenance and mathematical-status handling

- [ ] Display file, section, theorem, and line-level citations.
- [ ] Add expandable source excerpts.
- [ ] Label source statements, deductions, model knowledge, and external information separately.
- [ ] Add proved/conjectural/computational/work-in-progress labels.
- [ ] Teach the prompts not to convert finite evidence into a general proof.
- [ ] Teach the prompts to distinguish exploratory computation from exhaustive proof obligations.
- [ ] Add tests for conflicting definitions and conventions across topics.

### Phase 5 — Add core mathematical rendering

- [ ] Render Markdown and LaTeX reliably.
- [ ] Define schemas for trusted visualization blocks.
- [ ] Implement ordinary and shifted tableaux.
- [ ] Implement set-valued and primed tableaux.
- [ ] Implement Young, shifted, and skew diagrams.
- [ ] Implement ordinary and rational Dyck paths.
- [ ] Implement reading words, factorizations, and skeleton/string diagrams.
- [ ] Provide graceful text fallbacks for invalid visualization specifications.

### Phase 6 — Integrate approved computation

- [ ] Inventory lightweight and heavyweight programs.
- [ ] Select safe curated commands for the first release.
- [ ] Wrap approved mathematical functions in typed interfaces.
- [ ] Validate all parameters.
- [ ] Run computations in isolated workers.
- [ ] Enforce CPU, memory, runtime, and output limits.
- [ ] Stream progress and preserve reproducibility metadata.
- [ ] Connect computation output to visualization renderers.
- [ ] Clearly label examples, experiments, finite checks, and computer-assisted proof runs.

### Phase 7 — Add algorithm traces and animation

- [ ] Define a general event schema for insertion, bumping, extraction, reinsertion, and local moves.
- [ ] Modify or wrap selected algorithms so they emit deterministic traces.
- [ ] Implement step-by-step controls.
- [ ] Animate tableau insertion and recording.
- [ ] Animate path and skeleton transformations where useful.
- [ ] Let users inspect the mathematical state attached to each animation step.

### Phase 8 — Package, test, and document CRAIG

- [ ] Provide a simple local installation path.
- [ ] Add Docker support if it materially simplifies setup.
- [ ] Provide `.env.example` without secrets.
- [ ] Document remote and local model configuration.
- [ ] Add Windows, macOS, and Linux launch instructions.
- [ ] Add unit, integration, retrieval, rendering, and computation tests.
- [ ] Test with both strong and relatively small models.
- [ ] Add accessibility support and keyboard navigation.
- [ ] Document privacy and conversation-storage behavior.
- [ ] Provide a clear versioned list of implemented and planned features.

## Open design decisions

The following choices remain intentionally unresolved:

- Which model/provider should be recommended first?
- Should local inference or a user-supplied remote API key be the default path?
- Should external web search be absent, optional, or enabled by default?
- Which embedding and reranking methods perform best on this repository?
- Should conversation history be stored locally, kept only in memory, or made user-configurable?
- Which computations are safe and useful enough to expose in the first release?
- Which combinatorial visualization schemas should be standardized first?
- What resource limits best balance safety, reproducibility, and hands-on experimentation?
- How should CRAIG evaluate explanation quality across different mathematical backgrounds?
- How much capability can be obtained from relatively small models once the surrounding infrastructure is strong?

## Current status

**Current:** the repository contains the mathematical material under
[`content`](content/) and the Milestone 1 local, read-only FTS5 index and search
commands described above.

**Not yet implemented:** the CRAIG web application, conversational interface,
model integration, semantic retrieval, trusted visualizations, and controlled
computation layer.

The current implementation intentionally stops at local lexical indexing and
search; the later phases in the roadmap remain planned work.

## Open-source status

CRAIG is intended to be developed as an open-source project. The repository should make the mathematical sources, application architecture, renderers, retrieval methods, approved computation wrappers, and evaluation procedures inspectable and reproducible.

## Name

**CRAIG** stands for **Combinatorial Research Assistance Interactive Guide**.
