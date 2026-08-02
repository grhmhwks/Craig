# Phase 7 algorithm traces and animation

Phase 7 adds deterministic, inspectable algorithm histories to selected
allowlisted computations. It does not execute or modify a program under
`content/`. Trace-producing kernels remain in `craig/computation/`, run under
the Phase 6 worker isolation boundary, and return plain bounded JSON.

## Trace contract

Every trace has schema version `1`, an algorithm identifier, a title, and a
contiguous zero-based event array. An event has exactly these fields:

| Field | Meaning |
| --- | --- |
| `index` | Contiguous zero-based frame index. |
| `kind` | One closed event kind from the vocabulary below. |
| `title` | Short human-readable transition label. |
| `description` | Exact explanation of the transition represented by the frame. |
| `state` | JSON object containing the mathematical state at that frame. |
| `visualizations` | At most three labeled Phase 5 trusted visualization specifications. |

The event vocabulary is `initialization`, `insertion`, `bumping`, `extraction`,
`reinsertion`, `recording`, `local_move`, and `completion`. Extraction and
reinsertion are included in the general contract for reviewed future
algorithms; the initial Phase 7 producers do not invent such steps where their
mathematics has no extraction operation.

A trace contains at most 192 events and 196,608 encoded bytes. An individual
state contains at most 32,768 bytes, and each visualization specification at
most 16,384 bytes. Event titles, descriptions, identifiers, labels, kinds, and
visualization languages are bounded. Objects have closed schemas and trace
indexes must be contiguous.

The Python contract in `craig/computation/traces.py` validates trusted kernel
output. The independent TypeScript contract in
`app/frontend/src/traces/schema.ts` revalidates the API value and sends every
visualization through the Phase 5 schema. An invalid trace produces a text-only
fallback; JSON fields are never interpreted as HTML, SVG, JavaScript, module
names, file paths, or commands.

## Selected algorithms

### Ordinary row insertion and recording

`tableau_row_insertion` accepts 1 through 12 integers from -99 through 99. It
implements the standard ordinary RSK row-insertion baseline: replace the
leftmost row entry strictly larger than the active value, bump the replaced
value to the next row, and append when no larger entry exists. The recording
tableau receives the input position in the new box where that insertion
terminates.

The trace displays insertion tableau `P` and recording tableau `Q` together and
emits initialization, insertion, bumping, recording, and completion events.
The operation is a bounded exact example. Its corpus source basis provides the
context in which ordinary RSK/dual-RSK is contrasted with the specialized
chunked Dyck insertion. CRAIG does **not** present this ordinary baseline as the
chunked Dyck algorithm.

### Dyck-path construction

`dyck_path_statistics` now emits initialization, one local move for every
north/east step, and completion. Each frame retains the input prefix,
coordinates, and partial area sequence. The path renderer distinguishes the
completed prefix from pending steps and marks the active endpoint.

### Type C local moves

`type_c_hecke_word` now emits initialization, one local move for every
generator, and completion. Each frame records the applied prefix, generator,
whether the action changed the state, and the current signed permutation. A
skeleton frame shows the affected neighboring positions and a reading-word
frame identifies the current generator.

All three producers are deterministic. Their trace is included in the result
SHA-256 and is carried with the same normalized parameters, implementation and
source hashes, resource measurements, evidence classification, and claim
boundary as the exact output.

## Browser controls

The trace player provides:

- First, Previous, Play/Pause, Next, and Last controls;
- a range scrubber and slow, normal, or fast playback;
- Left/Right Arrow, Home, End, and Space keyboard controls when the player has
  focus;
- an announced step number, event kind, title, and transition description;
- trusted visualizations for the current frame;
- an expandable exact JSON state inspector.

If `prefers-reduced-motion: reduce` is active, timed playback and its speed
selector are disabled while all manual controls remain available. Existing
global reduced-motion CSS also removes nonessential transitions.

## Validation

Run the complete checks from the repository root:

```text
python -m pytest -q
cd app/frontend
npm run typecheck
npm test -- --configLoader runner
npm exec vite -- build --configLoader runner
```

Backend tests cover the closed vocabulary and schema, byte bounds, known
insertion examples, every word of length at most five over `{1,2,3}`, tableau
and recording invariants, deterministic path and skeleton traces, maximum job
sizes, worker isolation, API handoff, hashes, and unchanged corpus sources.
Frontend tests cover trace schema rejection, trusted visualization handoff,
Dyck progress bounds, player controls, navigation bounds, state inspection, and
safe fallback behavior.
