import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";

import { App, ModelDataNotice } from "./App";

describe("Phase 8 accessibility", () => {
  it("exposes keyboard navigation and named interaction regions", () => {
    const html = renderToStaticMarkup(<App />);

    expect(html).toContain('class="skip-link" href="#craig-main"');
    expect(html).toContain('id="craig-main" tabindex="-1"');
    expect(html).toContain('aria-label="Repository topics"');
    expect(html).toContain('aria-label="Research scope"');
    expect(html).toContain('aria-label="Conversation"');
    expect(html).toContain('aria-label="Conversation mode"');
    expect(html).toContain('aria-pressed="true"');
    expect(html).toContain('aria-label="Message CRAIG"');
    expect(html).toContain('aria-label="Send message"');
  });

  it("announces where model-bound data is sent", () => {
    const remote = renderToStaticMarkup(
      <ModelDataNotice destination="remote_model" />,
    );
    const local = renderToStaticMarkup(
      <ModelDataNotice destination="local_model" />,
    );
    const disabled = renderToStaticMarkup(
      <ModelDataNotice destination="none" />,
    );

    expect(remote).toContain("sent to the configured provider");
    expect(remote).toContain('role="status"');
    expect(local).toContain("configured loopback endpoint");
    expect(disabled).toBe("");
  });
});
