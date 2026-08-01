# Phase 4 implementation plan

Phase 4 adds provenance and mathematical-status presentation without changing
the read-only corpus boundary. Nothing in `content/` will be edited or annotated
in place.

## Contract decisions

Every cited answer passage will carry a stable citation identifier and the
existing source location:

- topic and corpus-relative path;
- heading and parsed environment, when available;
- start and end lines;
- indexed file hash;
- a bounded source excerpt suitable for an expandable panel.

Answer claims may use one of four provenance kinds:

- `repository`: stated explicitly in a cited repository passage;
- `deduction`: inferred from repository passages but not stated verbatim;
- `model_knowledge`: uncited general knowledge supplied by a future model;
- `external`: material from an external source.

`external` is reserved in the contract but remains unavailable while web access
is outside CRAIG's tool boundary.

Mathematical material may use one of these statuses:

- `proved_result`;
- `computer_assisted_proof`;
- `conjecture`;
- `computational_evidence`;
- `experimental_observation`;
- `proof_outline`;
- `work_in_progress`;
- `unknown`.

Status is `unknown` unless it is supported by explicit indexed structure or
source language. Phase 4 must never promote computational evidence to a proof,
or silently infer a global status from a filename or topic name.

The HTTP API remains under `/api/v1`. Phase 4 fields will initially be additive
so existing Phase 3 clients continue to work. A breaking event or conversation
shape change requires a new contract version.

## Implementation order

1. Add typed provenance, status, citation, and excerpt fields to the backend
   conversation contracts.
2. Derive status only from explicit parsed environments or clearly marked source
   metadata, preserving `unknown` everywhere else.
3. Carry citation identifiers and bounded excerpts through retrieval tool
   results, streamed events, and stored assistant messages.
4. Strengthen the secondary prompt so repository statements, deductions, and
   general knowledge remain visibly distinct.
5. Render inline citation markers and accessible expandable source panels in the
   React interface.
6. Add fixtures for conflicting conventions, conjectures, computational
   evidence, proof outlines, and unknown status.
7. Add regression tests proving that excerpts remain bounded, paths remain
   corpus-relative, hashes and line ranges survive streaming, and no operation
   writes beneath `content/`.

## Acceptance criteria

- A repository-backed answer exposes inspectable file, heading, line, hash, and
  excerpt metadata.
- Deductions are labeled and retain the citations from which they were derived.
- Unknown status remains visibly unknown.
- Conflicting definitions or conventions are presented separately with their
  own citations.
- Finite or exploratory computation is never labeled as a general proof.
- Source excerpts are text-only, bounded, and rendered without arbitrary HTML.
- Global and topic-scoped conversations retain provenance across follow-up
  turns.
- Phase 3 clients that ignore the new optional fields continue to function.
- The full test suite and a byte-for-byte protected-corpus check pass.

## Explicitly out of scope

- Editing or adding metadata beneath `content/`;
- external web search;
- arbitrary or approved code execution;
- mathematical LaTeX and diagram rendering, which begins in Phase 5;
- persistent conversation history;
- a live provider-specific adapter.

## Implementation status

The backend contracts, conservative classifier, prompt rules, SSE propagation,
conversation storage, deterministic provider output, expandable React evidence
cards, provenance labels, and regression fixtures are implemented.

Backend and dependency-free frontend checks pass. The production frontend
dependency install, typecheck, test, and Vite build still require access to
`registry.npmjs.org`; the current sandbox denies that connection with `EACCES`.
No partial dependency tree or build output is treated as an accepted artifact.
