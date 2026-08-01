import { describe, expect, it } from "vitest";

import { parseSseFrames } from "./sse";
import type { ComputationEvent } from "../types";

const event = JSON.stringify({
  schema_version: 1,
  type: "text.delta",
  conversation_id: "conv_test",
  created_at: "2026-07-27T00:00:00+00:00",
  data: { delta: "hello" },
});

describe("parseSseFrames", () => {
  it("parses complete LF and CRLF frames", () => {
    const parsed = parseSseFrames(
      `event: text.delta\ndata: ${event}\n\n` +
        `event: text.delta\r\ndata: ${event}\r\n\r\n`,
    );

    expect(parsed.events).toHaveLength(2);
    expect(parsed.events[0].data.delta).toBe("hello");
    expect(parsed.remainder).toBe("");
  });

  it("retains an incomplete frame for the next network chunk", () => {
    const parsed = parseSseFrames(`event: text.delta\ndata: ${event.slice(0, 20)}`);

    expect(parsed.events).toEqual([]);
    expect(parsed.remainder).toContain("event: text.delta");
  });

  it("preserves Phase 4 source and provenance payloads", () => {
    const sourcesReady = JSON.stringify({
      schema_version: 1,
      type: "sources.ready",
      conversation_id: "conv_test",
      created_at: "2026-07-30T00:00:00+00:00",
      data: {
        sources: [{ citation_id: "C-TEST" }],
        provenance: [{ kind: "repository" }],
      },
    });

    const parsed = parseSseFrames(
      `event: sources.ready\ndata: ${sourcesReady}\n\n`,
    );

    expect(parsed.events).toHaveLength(1);
    expect(parsed.events[0].type).toBe("sources.ready");
    expect(
      (parsed.events[0].data.sources as Array<{ citation_id: string }>)[0]
        .citation_id,
    ).toBe("C-TEST");
  });

  it("parses Phase 6 job events without a conversation id", () => {
    const completed = JSON.stringify({
      schema_version: 1,
      type: "computation.completed",
      job_id: "job_test",
      created_at: "2026-08-01T00:00:00+00:00",
      data: { classification: "finite_check", output: { count: 7 } },
    });

    const parsed = parseSseFrames<ComputationEvent>(
      `event: computation.completed\ndata: ${completed}\n\n`,
    );

    expect(parsed.events[0].job_id).toBe("job_test");
    expect(
      (parsed.events[0].data.output as { count: number }).count,
    ).toBe(7);
  });
});
