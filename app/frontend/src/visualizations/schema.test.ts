import { describe, expect, it } from "vitest";

import {
  MAX_GRID_CELLS,
  languageFromClassName,
  parseVisualizationBlock,
} from "./schema";

describe("trusted visualization schemas", () => {
  it.each([
    [
      "tableau",
      { rows: [[1, "2'"], [["2", "3"]]], variant: "set-valued" },
      "tableau",
    ],
    [
      "young-diagram",
      { shape: [4, 3, 1], inner_shape: [1], shifted: true },
      "diagram",
    ],
    [
      "dyck-path",
      { kind: "rational", r: 5, s: 3, steps: "NNEENEEE" },
      "dyck-path",
    ],
    ["reading-word", { entries: ["1", "2'", "3"] }, "reading-word"],
    ["factorization", { factors: [[1, 2], [3]] }, "factorization"],
    [
      "skeleton",
      {
        vertices: [
          { id: "a", label: "A" },
          { id: "b", label: "B" },
        ],
        edges: [{ from: "a", to: "b" }],
      },
      "skeleton",
    ],
    [
      "string-diagram",
      {
        strings: [
          { id: "a", label: "A", entries: [1, 2] },
          { id: "b", label: "B", entries: [3] },
        ],
        links: [
          {
            from: { string: "a", index: 0 },
            to: { string: "b", index: 0 },
          },
        ],
      },
      "string-diagram",
    ],
  ])("accepts a bounded %s specification", (language, value, expectedKind) => {
    const parsed = parseVisualizationBlock(language, JSON.stringify(value));

    expect(parsed.ok).toBe(true);
    if (parsed.ok) {
      expect(parsed.spec.kind).toBe(expectedKind);
    }
  });

  it("normalizes aliases from Markdown language classes", () => {
    expect(languageFromClassName("language-young-diagram")).toBe("diagram");
    expect(languageFromClassName("foo language-dyck bar")).toBe("dyck-path");
    expect(languageFromClassName("language-javascript")).toBeNull();
  });

  it("rejects unknown fields and arbitrary payloads", () => {
    const unknownField = parseVisualizationBlock(
      "tableau",
      JSON.stringify({ rows: [[1]], html: "<script>alert(1)</script>" }),
    );
    const invalidJson = parseVisualizationBlock("tableau", "not JSON");

    expect(unknownField).toEqual({
      ok: false,
      error: "tableau contains unsupported field: html.",
    });
    expect(invalidJson.ok).toBe(false);
  });

  it("enforces shape, cell, and sequence limits", () => {
    const oversized = parseVisualizationBlock(
      "tableau",
      JSON.stringify({
        rows: Array.from({ length: 20 }, () =>
          Array.from({ length: Math.ceil(MAX_GRID_CELLS / 20) + 1 }, () => 1),
        ),
      }),
    );
    const growingShape = parseVisualizationBlock(
      "young-diagram",
      JSON.stringify({ shape: [2, 3] }),
    );
    const emptyShape = parseVisualizationBlock(
      "young-diagram",
      JSON.stringify({ shape: [0] }),
    );
    const nonStrictShiftedShape = parseVisualizationBlock(
      "young-diagram",
      JSON.stringify({ shape: [3, 3], shifted: true }),
    );

    expect(oversized.ok).toBe(false);
    expect(growingShape).toEqual({
      ok: false,
      error: "shape must be weakly decreasing.",
    });
    expect(emptyShape).toEqual({
      ok: false,
      error: "shape must contain at least one cell.",
    });
    expect(nonStrictShiftedShape).toEqual({
      ok: false,
      error: "a shifted shape must be strictly decreasing.",
    });
  });

  it("validates the selected side of a Dyck diagonal", () => {
    const above = parseVisualizationBlock(
      "dyck-path",
      JSON.stringify({ steps: "NENEEENN", kind: "ordinary" }),
    );
    const below = parseVisualizationBlock(
      "dyck-path",
      JSON.stringify({
        steps: "ENEN",
        kind: "ordinary",
        boundary: "below",
      }),
    );

    expect(above.ok).toBe(false);
    expect(below.ok).toBe(true);
  });

  it("requires graph references and string endpoints to exist", () => {
    const skeleton = parseVisualizationBlock(
      "skeleton",
      JSON.stringify({
        vertices: [{ id: "a", label: "A" }],
        edges: [{ from: "a", to: "missing" }],
      }),
    );
    const strings = parseVisualizationBlock(
      "string-diagram",
      JSON.stringify({
        strings: [{ id: "a", label: "A", entries: [1] }],
        links: [
          {
            from: { string: "a", index: 0 },
            to: { string: "a", index: 2 },
          },
        ],
      }),
    );

    expect(skeleton.ok).toBe(false);
    expect(strings.ok).toBe(false);
  });
});
