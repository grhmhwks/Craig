import { describe, expect, it } from "vitest";

import { RENDERER_GALLERY_MARKDOWN } from "./gallery";
import { parseVisualizationBlock } from "./schema";

describe("renderer gallery", () => {
  it("contains a valid example for every trusted renderer family", () => {
    const blocks = [...RENDERER_GALLERY_MARKDOWN.matchAll(
      /```([\w-]+)\n([\s\S]*?)\n```/g,
    )];
    const results = blocks.map((match) =>
      parseVisualizationBlock(match[1], match[2]),
    );

    expect(blocks).toHaveLength(9);
    expect(results.every((result) => result.ok)).toBe(true);
    expect(
      new Set(
        results.flatMap((result) => (result.ok ? [result.spec.kind] : [])),
      ),
    ).toEqual(
      new Set([
        "tableau",
        "diagram",
        "dyck-path",
        "reading-word",
        "factorization",
        "skeleton",
        "string-diagram",
      ]),
    );
  });
});
