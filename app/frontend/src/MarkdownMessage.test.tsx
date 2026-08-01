import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";

import { MarkdownMessage } from "./MarkdownMessage";

describe("MarkdownMessage", () => {
  it("renders inline and display TeX through KaTeX", () => {
    const html = renderToStaticMarkup(
      <MarkdownMessage>
        {"Inline $x^2$.\n\n$$\n\\sum_i x_i\n$$"}
      </MarkdownMessage>,
    );

    expect(html).toContain('class="katex"');
    expect(html).toContain('class="katex-display"');
  });

  it("omits raw HTML from model-authored Markdown", () => {
    const html = renderToStaticMarkup(
      <MarkdownMessage>{"Safe text <script>alert('no')</script> remains."}</MarkdownMessage>,
    );

    expect(html).not.toContain("<script");
    expect(html).not.toContain("</script>");
    expect(html).toContain("Safe text");
    expect(html).toContain("alert(&#x27;no&#x27;)");
  });

  it("renders trusted blocks and preserves invalid blocks as text", () => {
    const valid = renderToStaticMarkup(
      <MarkdownMessage>{'```tableau\n{"rows":[[1]]}\n```'}</MarkdownMessage>,
    );
    const invalid = renderToStaticMarkup(
      <MarkdownMessage>{'```tableau\n{"rows":[] }\n```'}</MarkdownMessage>,
    );

    expect(valid).toContain('data-visualization="tableau"');
    expect(valid).toContain('role="img"');
    expect(invalid).toContain("Visualization unavailable");
    expect(invalid).toContain("rows must contain between 1 and 20 rows");
    expect(invalid).toContain("{&quot;rows&quot;:[] }");
  });
});
