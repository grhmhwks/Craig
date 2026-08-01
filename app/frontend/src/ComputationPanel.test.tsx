import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";

import { ComputationPanel } from "./ComputationPanel";
import type { ComputationOperation } from "./types";

const operation: ComputationOperation = {
  id: "enumerate_rational_dyck_paths",
  title: "Enumerate rational Dyck paths",
  description: "A bounded exact enumeration.",
  classification: "finite_check",
  implementation_version: "1.0.0",
  source_basis: {
    path: "conjectured_rational_formula/code.py",
    start_line: 67,
    end_line: 82,
  },
  parameters: [
    {
      name: "r",
      kind: "integer",
      label: "East steps r",
      description: "Horizontal endpoint.",
      required: true,
      default: 5,
      minimum: 2,
      maximum: 10,
      max_items: null,
    },
    {
      name: "s",
      kind: "integer",
      label: "North steps s",
      description: "Vertical endpoint.",
      required: true,
      default: 3,
      minimum: 2,
      maximum: 10,
      max_items: null,
    },
  ],
  limits: {
    wall_time_seconds: 8,
    cpu_time_seconds: 6,
    memory_bytes: 268_435_456,
    output_bytes: 262_144,
    stderr_bytes: 32_768,
    request_bytes: 16_384,
  },
};

describe("ComputationPanel", () => {
  it("presents allowlisted parameters and resource limits", () => {
    const html = renderToStaticMarkup(
      <ComputationPanel operations={[operation]} busy={false} onRun={() => {}} />,
    );

    expect(html).toContain("Isolated allowlist");
    expect(html).toContain("Enumerate rational Dyck paths");
    expect(html).toContain('min="2"');
    expect(html).toContain('max="10"');
    expect(html).toContain("256MB memory");
    expect(html).toContain("no child processes");
    expect(html).toContain("Run approved job");
  });
});
