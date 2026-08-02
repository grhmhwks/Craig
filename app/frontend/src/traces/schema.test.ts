import { describe, expect, it } from "vitest";

import { parseAlgorithmTrace, traceEventKinds } from "./schema";

function event(index: number, kind: string) {
  return {
    index,
    kind,
    title: `Step ${index}`,
    description: "A deterministic transition.",
    state: { index },
    visualizations: [],
  };
}

describe("Phase 7 algorithm trace schema", () => {
  it("accepts every event kind with contiguous indexes", () => {
    const parsed = parseAlgorithmTrace({
      schema_version: 1,
      algorithm: "contract_test",
      title: "Contract test",
      events: traceEventKinds.map((kind, index) => event(index, kind)),
    });

    expect(parsed.ok).toBe(true);
    if (parsed.ok) {
      expect(parsed.trace.events.map((item) => item.kind)).toEqual(traceEventKinds);
    }
  });

  it("validates every visualization through the trusted renderer schema", () => {
    const accepted = parseAlgorithmTrace({
      schema_version: 1,
      algorithm: "row_insertion",
      title: "Row insertion",
      events: [
        {
          ...event(0, "recording"),
          visualizations: [
            {
              label: "Insertion tableau",
              language: "tableau",
              spec: { rows: [[1, 2], [3]] },
            },
          ],
        },
      ],
    });
    const rejected = parseAlgorithmTrace({
      schema_version: 1,
      algorithm: "row_insertion",
      title: "Row insertion",
      events: [
        {
          ...event(0, "recording"),
          visualizations: [
            {
              label: "Unsafe",
              language: "tableau",
              spec: { rows: [[1]], html: "<script>alert(1)</script>" },
            },
          ],
        },
      ],
    });

    expect(accepted.ok).toBe(true);
    expect(rejected.ok).toBe(false);
  });

  it("rejects unknown fields, event kinds, and noncontiguous indexes", () => {
    const unknownField = parseAlgorithmTrace({
      schema_version: 1,
      algorithm: "test",
      title: "Test",
      events: [{ ...event(0, "local_move"), code: "anything" }],
    });
    const unknownKind = parseAlgorithmTrace({
      schema_version: 1,
      algorithm: "test",
      title: "Test",
      events: [event(0, "execute_code")],
    });
    const indexGap = parseAlgorithmTrace({
      schema_version: 1,
      algorithm: "test",
      title: "Test",
      events: [event(1, "local_move")],
    });

    expect(unknownField.ok).toBe(false);
    expect(unknownKind.ok).toBe(false);
    expect(indexGap.ok).toBe(false);
  });
});
