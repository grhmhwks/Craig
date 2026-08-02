import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";

import { TracePlayer, traceIndexAfter } from "./TracePlayer";

const trace = {
  schema_version: 1,
  algorithm: "ordinary_rsk_row_insertion",
  title: "Ordinary row insertion",
  events: [
    {
      index: 0,
      kind: "recording",
      title: "Record position 1",
      description: "Add the first recording box.",
      state: {
        insertion_tableau: [[2]],
        recording_tableau: [[1]],
      },
      visualizations: [
        {
          label: "Insertion tableau P",
          language: "tableau",
          spec: { rows: [[2]] },
        },
      ],
    },
    {
      index: 1,
      kind: "completion",
      title: "Complete",
      description: "The insertion is complete.",
      state: { shape: [1] },
      visualizations: [],
    },
  ],
};

describe("Phase 7 trace player", () => {
  it("renders controls, trusted frames, and inspectable mathematical state", () => {
    const html = renderToStaticMarkup(<TracePlayer value={trace} />);

    expect(html).toContain("Deterministic trace");
    expect(html).toContain("Previous");
    expect(html).toContain("Play");
    expect(html).toContain("Next");
    expect(html).toContain('aria-label="Trace step"');
    expect(html).toContain('data-visualization="tableau"');
    expect(html).toContain("Inspect mathematical state at this step");
    expect(html).toContain("insertion_tableau");
  });

  it("bounds every navigation action", () => {
    expect(traceIndexAfter(1, "first", 4)).toBe(0);
    expect(traceIndexAfter(0, "previous", 4)).toBe(0);
    expect(traceIndexAfter(1, "next", 4)).toBe(2);
    expect(traceIndexAfter(4, "next", 4)).toBe(4);
    expect(traceIndexAfter(1, "last", 4)).toBe(4);
  });

  it("degrades safely when a trace is invalid", () => {
    const html = renderToStaticMarkup(
      <TracePlayer value={{ ...trace, schema_version: 99 }} />,
    );

    expect(html).toContain("Algorithm trace unavailable");
    expect(html).not.toContain("Trace playback controls");
  });
});
