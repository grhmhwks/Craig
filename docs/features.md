# CRAIG versioned feature ledger

## Implemented releases

| Version | Phase | Implemented capability |
| --- | --- | --- |
| 0.1 | 1 | Structural corpus discovery, chunking, SQLite FTS5 indexing, exact search, ranking, and incremental refresh. |
| 0.2 | 2 | Bounded read-only retrieval service and versioned HTTP API with traversal and stale-index protection. |
| 0.3 | 3 | React conversation interface, SSE streaming, provider-neutral orchestration, modes, and in-memory follow-up context. |
| 0.4 | 4 | Stable citations, source excerpts, provenance categories, conservative mathematical-status handling, and conflict tests. |
| 0.5 | 5 | Safe Markdown/KaTeX and schema-validated tableau, diagram, path, word, factorization, skeleton, and string renderers. |
| 0.6 | 6 | Typed allowlisted computations, process isolation, resource limits, progress, classifications, hashes, and reproducibility. |
| 0.7 | 7 | Versioned algorithm traces, tableau insertion/recording, path and skeleton frames, playback, and state inspection. |
| 1.0 | 8 | Cross-platform and Docker packaging, diagnostics, remote/local model adapters, model evaluation profiles, accessibility, privacy documentation, release tests, and production builds. |

## CRAIG 1.0 boundaries

Implemented:

- protected-corpus indexing and lexical retrieval;
- deterministic demo conversation and opt-in remote/local synthesis;
- four conversation modes with bounded recent context;
- explicit citations, provenance, and mathematical-status boundaries;
- trusted mathematical rendering;
- five curated computation operations and three deterministic trace producers;
- Windows, macOS, Linux, and Docker launch paths;
- memory-only conversations and secret-free public configuration;
- unit, integration, retrieval, rendering, computation, provider, evaluation,
  accessibility-contract, build, and packaging validation.

Not implemented in 1.0:

- semantic/vector retrieval or learned reranking;
- external web search from conversations;
- persistent conversation history or user accounts;
- automatic arbitrary corpus-code execution;
- mobile-native applications;
- a claim that any synthetic or finite evaluation proves general mathematical
  correctness;
- live model quality certification without an operator-supplied model and an
  explicitly recorded evaluation run.

## Planned candidates

Future work may evaluate semantic retrieval, optional local conversation
persistence, additional reviewed computations and trace producers, more
visualization schemas, richer model evaluations, and further frontend code
splitting. Each remains outside the v1.0 compatibility promise until reviewed.
