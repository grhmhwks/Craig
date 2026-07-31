import { describe, expect, it } from "vitest";

import { parseSseFrames } from "./sse";

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
});
