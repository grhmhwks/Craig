import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";

import { computationMarkdown } from "./App";
import { MarkdownMessage } from "./MarkdownMessage";
import type { ComputationEvent } from "./types";

describe("Phase 6 computation results", () => {
  it("retains claim boundaries, hashes, and trusted visualizations", () => {
    const event: ComputationEvent = {
      schema_version: 1,
      type: "computation.completed",
      job_id: "job_test",
      created_at: "2026-08-01T00:00:00+00:00",
      data: {
        title: "Rational path check",
        classification: "finite_check",
        summary: "Enumerated seven paths.",
        claim_boundary: "This is not a proof of an unbounded claim.",
        output: { count: 7 },
        visualization: {
          language: "dyck-path",
          spec: {
            kind: "rational",
            r: 5,
            s: 3,
            steps: "NNEENEEE",
          },
        },
        reproducibility: {
          request_sha256: "a".repeat(64),
          result_sha256: "b".repeat(64),
          implementation_version: "1.0.0",
          implementation_sha256: "c".repeat(64),
          source_basis: {
            path: "conjectured_rational_formula/code.py",
            start_line: 67,
            end_line: 82,
            sha256: "d".repeat(64),
          },
        },
        resource_usage: { total_wall_time_ms: 12.5 },
      },
    };

    const markdown = computationMarkdown(event);
    const html = renderToStaticMarkup(
      <MarkdownMessage>{markdown}</MarkdownMessage>,
    );

    expect(markdown).toContain("not a proof of an unbounded claim");
    expect(markdown).toContain("a".repeat(64));
    expect(html).toContain('data-visualization="dyck-path"');
    expect(html).toContain("Exact output");
  });
});
