import { useEffect, useRef, useState } from "react";
import type { FormEvent, KeyboardEvent } from "react";

import { loadBootstrap, streamChat, streamComputation } from "./api";
import { ComputationPanel } from "./ComputationPanel";
import { MarkdownMessage } from "./MarkdownMessage";
import { TracePlayer } from "./traces/TracePlayer";
import type {
  ChatConfiguration,
  ChatEvent,
  ChatMessage,
  ChatMode,
  ComputationEvent,
  ComputationOperation,
  MathematicalStatus,
  ProvenanceAnnotation,
  ProvenanceKind,
  SourceReference,
  TopicSummary,
} from "./types";
import { RENDERER_GALLERY_MARKDOWN } from "./visualizations/gallery";

const modeLabels: Record<ChatMode, string> = {
  research: "Research",
  explanation: "Explain",
  tutorial: "Tutorial",
  computation: "Computation",
};

const statusLabels: Record<MathematicalStatus, string> = {
  proved_result: "Proved result",
  computer_assisted_proof: "Computer-assisted proof",
  conjecture: "Conjecture",
  computational_evidence: "Computational evidence",
  experimental_observation: "Experimental observation",
  proof_outline: "Proof outline",
  work_in_progress: "Work in progress",
  unknown: "Status unknown",
};

const provenanceLabels: Record<ProvenanceKind, string> = {
  repository: "Repository statement",
  deduction: "CRAIG deduction",
  computation: "Bounded computation",
  model_knowledge: "Model knowledge",
  external: "External information",
};

const starters: Record<ChatMode, string[]> = {
  research: [
    "What does the repository say about strict dominance?",
    "Compare the main definitions of shifted tableaux.",
    "Find the strongest source for the string decomposition formula.",
  ],
  explanation: [
    "Explain the role of lattice words in the shifted setting.",
    "What is a strict decomposition tableau?",
    "Explain the main idea behind the conjectured rational formula.",
  ],
  tutorial: [
    "Teach me how to read the shifted Littlewood–Richardson notes.",
    "Give me a guided introduction to rational Dyck paths.",
    "Where should I start with skeleton tableau formulas?",
  ],
  computation: [
    "Which code studies the middle coefficients?",
    "Locate the reference implementation for Dyck symmetric functions.",
    "What computations support the conjectured formula?",
  ],
};

function BookIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v16H6.5A2.5 2.5 0 0 0 4 21.5v-16Z" />
      <path d="M20 5.5A2.5 2.5 0 0 0 17.5 3H13v16h4.5a2.5 2.5 0 0 1 2.5 2.5v-16Z" />
    </svg>
  );
}

function SparkIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="m12 2 1.5 5.2L18 10l-4.5 2.8L12 18l-1.5-5.2L6 10l4.5-2.8L12 2Z" />
      <path d="m19 15 .7 2.3L22 18l-2.3.7L19 21l-.7-2.3L16 18l2.3-.7L19 15Z" />
    </svg>
  );
}

function ArrowIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M5 12h13M13 6l6 6-6 6" />
    </svg>
  );
}

function topicLabel(topic: string): string {
  if (topic === "_root") {
    return "Repository guide";
  }
  return topic.replaceAll("_", " ");
}

function sourceLabel(source: SourceReference): string {
  return `content/${source.path}:${source.start_line}–${source.end_line}`;
}

function structureLabel(environment: string | null): string {
  if (!environment) {
    return "Not explicitly classified";
  }
  if (environment.startsWith("heading_")) {
    return `Markdown heading level ${environment.slice("heading_".length)}`;
  }
  return environment.replaceAll("_", " ");
}

export function computationMarkdown(event: ComputationEvent): string {
  const data = event.data;
  const visualization = data.visualization as
    | { language?: unknown; spec?: unknown }
    | null
    | undefined;
  const reproducibility = (data.reproducibility ?? {}) as Record<string, unknown>;
  const sourceBasis = (reproducibility.source_basis ?? {}) as Record<
    string,
    unknown
  >;
  const resourceUsage = (data.resource_usage ?? {}) as Record<string, unknown>;
  const visualizationBlock =
    visualization &&
    typeof visualization.language === "string" &&
    visualization.spec &&
    typeof visualization.spec === "object"
      ? `\n\n\`\`\`${visualization.language}\n${JSON.stringify(
          visualization.spec,
          null,
          2,
        )}\n\`\`\``
      : "";
  return `## ${String(data.title ?? data.operation ?? "Computation result")}

${String(data.summary ?? "The isolated worker completed.")}

**Classification:** ${String(data.classification ?? "unknown").replaceAll("_", " ")}

${String(data.claim_boundary ?? "This result applies only to the displayed parameters.")}${visualizationBlock}

### Exact output

\`\`\`json
${JSON.stringify(data.output ?? {}, null, 2)}
\`\`\`

### Reproducibility

- Job: \`${event.job_id}\`
- Request SHA-256: \`${String(reproducibility.request_sha256 ?? "unavailable")}\`
- Result SHA-256: \`${String(reproducibility.result_sha256 ?? "unavailable")}\`
- Implementation: \`${String(reproducibility.implementation_version ?? "unknown")}\` / \`${String(reproducibility.implementation_sha256 ?? "unavailable")}\`
- Corpus basis: \`content/${String(sourceBasis.path ?? "unknown")}\`, lines ${String(sourceBasis.start_line ?? "?")}–${String(sourceBasis.end_line ?? "?")}, SHA-256 \`${String(sourceBasis.sha256 ?? "unavailable")}\`
- Worker wall time: ${String(resourceUsage.total_wall_time_ms ?? "?")} ms
`;
}

function SourcePanel({ source }: { source: SourceReference }) {
  return (
    <details className="source-card">
      <summary>
        <span className="citation-id">{source.citation_id}</span>
        <span className="source-summary">
          <strong>{source.heading ?? source.path}</strong>
          <small>{sourceLabel(source)}</small>
        </span>
        <span
          className={`status-badge status-${source.mathematical_status}`}
        >
          {statusLabels[source.mathematical_status]}
        </span>
      </summary>
      <div className="source-detail">
        <dl>
          <div>
            <dt>Topic</dt>
            <dd>{topicLabel(source.topic)}</dd>
          </div>
          <div>
            <dt>File</dt>
            <dd>content/{source.path}</dd>
          </div>
          <div>
            <dt>Structure</dt>
            <dd>{structureLabel(source.environment)}</dd>
          </div>
          <div>
            <dt>Heading</dt>
            <dd>{source.heading ?? "Not available"}</dd>
          </div>
          <div>
            <dt>Lines</dt>
            <dd>
              {source.start_line}–{source.end_line}
            </dd>
          </div>
        </dl>
        <p className="status-basis">
          {source.status_basis ??
            "No explicit mathematical-status marker was found."}
        </p>
        <pre>{source.excerpt || "No excerpt was returned."}</pre>
        <p className="source-hash" title={source.file_hash}>
          Indexed SHA-256: {source.file_hash}
        </p>
      </div>
    </details>
  );
}

function ProvenancePanel({
  annotations,
}: {
  annotations: ProvenanceAnnotation[];
}) {
  return (
    <section className="provenance-panel" aria-label="Answer provenance">
      <h4>Answer provenance</h4>
      {annotations.map((annotation, index) => (
        <div
          className={`provenance-note provenance-${annotation.kind}`}
          key={`${annotation.kind}:${index}`}
        >
          <span>{provenanceLabels[annotation.kind]}</span>
          <p>{annotation.description}</p>
          {annotation.citation_ids.length > 0 && (
            <small>{annotation.citation_ids.join(" · ")}</small>
          )}
        </div>
      ))}
    </section>
  );
}

export function ModelDataNotice({
  destination,
}: {
  destination: "none" | "local_model" | "remote_model" | undefined;
}) {
  if (destination === "remote_model") {
    return (
      <p className="model-data-notice" role="status">
        Remote model enabled: your question, recent conversation, and retrieved
        excerpts are sent to the configured provider.
      </p>
    );
  }
  if (destination === "local_model") {
    return (
      <p className="model-data-notice local" role="status">
        Local model enabled: bounded conversation and retrieved excerpts are
        sent only to the configured loopback endpoint.
      </p>
    );
  }
  return null;
}

export function App() {
  const [configuration, setConfiguration] =
    useState<ChatConfiguration | null>(null);
  const [topics, setTopics] = useState<TopicSummary[]>([]);
  const [computations, setComputations] = useState<ComputationOperation[]>([]);
  const [mode, setMode] = useState<ChatMode>("research");
  const [topic, setTopic] = useState<string | null>(null);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [status, setStatus] = useState("Ready");
  const [activity, setActivity] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const abortRef = useRef<AbortController | null>(null);
  const endRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    loadBootstrap()
      .then(
        ({
          configuration: nextConfiguration,
          topics: nextTopics,
          computations: nextComputations,
        }) => {
          setConfiguration(nextConfiguration);
          setTopics(nextTopics.topics);
          setComputations(nextComputations.operations);
        },
      )
      .catch((reason: unknown) => {
        setError(reason instanceof Error ? reason.message : String(reason));
      });
    return () => abortRef.current?.abort();
  }, []);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [messages, activity]);

  function beginNewConversation() {
    abortRef.current?.abort();
    abortRef.current = null;
    setConversationId(null);
    setMessages([]);
    setInput("");
    setError(null);
    setActivity(null);
    setStatus("Ready");
    setBusy(false);
  }

  function showRendererGallery() {
    beginNewConversation();
    setMessages([
      {
        id: `local_gallery_${crypto.randomUUID()}`,
        role: "assistant",
        content: RENDERER_GALLERY_MARKDOWN,
        created_at: new Date().toISOString(),
        sources: [],
        provenance: [
          {
            kind: "model_knowledge",
            description:
              "This local gallery demonstrates trusted Phase 5 renderers; it is not repository evidence.",
            citation_ids: [],
          },
        ],
      },
    ]);
  }

  function applyEvent(event: ChatEvent, pendingAssistantId: string) {
    if (
      event.type === "conversation.created" ||
      event.type === "conversation.resumed"
    ) {
      setConversationId(event.conversation_id);
      return;
    }
    if (event.type === "status") {
      setStatus(String(event.data.label ?? "Working"));
      return;
    }
    if (event.type === "tool.call") {
      const name = String(event.data.name ?? "retrieval");
      setActivity(name.replaceAll("_", " "));
      return;
    }
    if (event.type === "tool.result") {
      setActivity(null);
      return;
    }
    if (event.type === "sources.ready") {
      const sources = (event.data.sources ?? []) as SourceReference[];
      const provenance = (event.data.provenance ?? []) as ProvenanceAnnotation[];
      setMessages((current) =>
        current.map((message) =>
          message.id === pendingAssistantId
            ? { ...message, sources, provenance }
            : message,
        ),
      );
      return;
    }
    if (event.type === "text.delta") {
      const delta = String(event.data.delta ?? "");
      setMessages((current) =>
        current.map((message) =>
          message.id === pendingAssistantId
            ? { ...message, content: `${message.content}${delta}` }
            : message,
        ),
      );
      return;
    }
    if (event.type === "message.completed") {
      const completed = event.data.message as unknown as ChatMessage;
      setMessages((current) =>
        current.map((message) =>
          message.id === pendingAssistantId
            ? {
                ...completed,
                sources: completed.sources ?? [],
                provenance: completed.provenance ?? [],
              }
            : message,
        ),
      );
      setStatus("Ready");
      setActivity(null);
      return;
    }
    if (event.type === "error") {
      setError(String(event.data.message ?? "The chat request failed."));
      setStatus("Stopped");
      setActivity(null);
    }
  }

  async function submitMessage(rawMessage: string) {
    const message = rawMessage.trim();
    if (!message || busy) {
      return;
    }
    const now = new Date().toISOString();
    const userMessage: ChatMessage = {
      id: `local_user_${crypto.randomUUID()}`,
      role: "user",
      content: message,
      created_at: now,
      sources: [],
      provenance: [],
    };
    const pendingAssistantId = `local_assistant_${crypto.randomUUID()}`;
    const pendingAssistant: ChatMessage = {
      id: pendingAssistantId,
      role: "assistant",
      content: "",
      created_at: now,
      sources: [],
      provenance: [],
    };
    setMessages((current) => [...current, userMessage, pendingAssistant]);
    setInput("");
    setError(null);
    setBusy(true);
    setStatus("Connecting");
    const controller = new AbortController();
    abortRef.current = controller;
    try {
      await streamChat(
        {
          message,
          mode,
          topic,
          conversation_id: conversationId,
        },
        (event) => applyEvent(event, pendingAssistantId),
        controller.signal,
      );
    } catch (reason: unknown) {
      if (!controller.signal.aborted) {
        setError(reason instanceof Error ? reason.message : String(reason));
        setStatus("Stopped");
      }
    } finally {
      if (abortRef.current === controller) {
        setBusy(false);
        abortRef.current = null;
      }
    }
  }

  async function runComputation(
    operation: ComputationOperation,
    parameters: Record<string, unknown>,
  ) {
    if (busy) return;
    const now = new Date().toISOString();
    const userMessage: ChatMessage = {
      id: `local_user_${crypto.randomUUID()}`,
      role: "user",
      content: `Run approved computation: ${operation.title} with ${JSON.stringify(parameters)}.`,
      created_at: now,
      sources: [],
      provenance: [],
    };
    const pendingAssistantId = `local_computation_${crypto.randomUUID()}`;
    const pendingAssistant: ChatMessage = {
      id: pendingAssistantId,
      role: "assistant",
      content: "",
      created_at: now,
      sources: [],
      provenance: [],
    };
    setMessages((current) => [...current, userMessage, pendingAssistant]);
    setError(null);
    setBusy(true);
    setStatus("Starting isolated worker");
    const controller = new AbortController();
    abortRef.current = controller;
    try {
      await streamComputation(
        { operation: operation.id, parameters },
        (event) => {
          if (event.type === "computation.started") {
            setStatus("Worker isolated");
            setActivity(operation.title.toLowerCase());
          } else if (event.type === "computation.progress") {
            const fraction = Number(event.data.fraction ?? 0);
            const label = String(event.data.label ?? "Computing");
            setStatus(`${label} · ${Math.round(fraction * 100)}%`);
            setActivity(label.toLowerCase());
          } else if (event.type === "computation.completed") {
            setMessages((current) =>
              current.map((message) =>
                message.id === pendingAssistantId
                  ? {
                      ...message,
                      content: computationMarkdown(event),
                      trace: event.data.trace,
                      provenance: [
                        {
                          kind: "computation",
                          description:
                            "Produced by a typed, allowlisted, resource-limited Phase 7 worker. Deterministic trace frames, the claim boundary, and reproducibility hashes are shown with the result.",
                          citation_ids: [],
                        },
                      ],
                    }
                  : message,
              ),
            );
            setStatus("Ready");
            setActivity(null);
          } else if (event.type === "computation.error") {
            const message = String(
              event.data.message ?? "The isolated computation failed.",
            );
            setMessages((current) =>
              current.map((item) =>
                item.id === pendingAssistantId
                  ? {
                      ...item,
                      content: `**Computation stopped:** ${message}`,
                      provenance: [
                        {
                          kind: "computation",
                          description:
                            "The worker returned no mathematical result.",
                          citation_ids: [],
                        },
                      ],
                    }
                  : item,
              ),
            );
            setError(message);
            setStatus("Stopped");
            setActivity(null);
          }
        },
        controller.signal,
      );
    } catch (reason: unknown) {
      if (!controller.signal.aborted) {
        const message = reason instanceof Error ? reason.message : String(reason);
        setError(message);
        setStatus("Stopped");
        setActivity(null);
        setMessages((current) =>
          current.map((item) =>
            item.id === pendingAssistantId
              ? {
                  ...item,
                  content: `**Computation stopped:** ${message}`,
                  provenance: [
                    {
                      kind: "computation",
                      description:
                        "The request was rejected or interrupted before a mathematical result was produced.",
                      citation_ids: [],
                    },
                  ],
                }
              : item,
          ),
        );
      }
    } finally {
      if (abortRef.current === controller) {
        setBusy(false);
        abortRef.current = null;
      }
    }
  }

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    void submitMessage(input);
  }

  function handleComposerKeyDown(event: KeyboardEvent<HTMLTextAreaElement>) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      void submitMessage(input);
    }
  }

  const provider = configuration?.provider;
  const activeMode = configuration?.modes.find((item) => item.id === mode);
  const empty = messages.length === 0;

  return (
    <div className="app-shell">
      <a className="skip-link" href="#craig-main">
        Skip to conversation
      </a>
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">
            <BookIcon />
          </div>
          <div>
            <strong>CRAIG</strong>
            <span>Combinatorial research guide</span>
          </div>
        </div>

        <button
          className="new-chat"
          type="button"
          onClick={beginNewConversation}
          aria-label="Start a new conversation"
        >
          <SparkIcon />
          New conversation
        </button>
        <button
          className="gallery-button"
          type="button"
          onClick={showRendererGallery}
        >
          Preview renderers
        </button>

        <nav className="scope-nav" aria-label="Repository topics">
          <p className="nav-label">Research scope</p>
          <button
            className={topic === null ? "scope-item active" : "scope-item"}
            type="button"
            onClick={() => setTopic(null)}
            aria-current={topic === null ? "page" : undefined}
          >
            <span className="scope-glyph">∞</span>
            <span>
              <strong>Entire corpus</strong>
              <small>{topics.reduce((sum, item) => sum + item.file_count, 0)} files</small>
            </span>
          </button>
          <div className="topic-list">
            {topics.map((item) => (
              <button
                className={topic === item.topic ? "scope-item active" : "scope-item"}
                type="button"
                key={item.topic}
                onClick={() => setTopic(item.topic)}
                aria-current={topic === item.topic ? "page" : undefined}
              >
                <span className="scope-dot" />
                <span>
                  <strong>{topicLabel(item.topic)}</strong>
                  <small>{item.chunk_count} passages</small>
                </span>
              </button>
            ))}
          </div>
        </nav>

        <div className="sidebar-foot">
          <div className="read-only-badge">
            <span />
            Local · read-only corpus
          </div>
          <p>Conversation state stays in memory and clears when the server stops.</p>
        </div>
      </aside>

      <main className="workspace" id="craig-main" tabIndex={-1}>
        <header className="topbar">
          <div className="scope-title">
            <span>Current scope</span>
            <strong>{topic ? topicLabel(topic) : "Entire corpus"}</strong>
          </div>
          <label className="mobile-scope-selector">
            <span>Research scope</span>
            <select
              aria-label="Research scope"
              value={topic ?? ""}
              onChange={(event) => setTopic(event.target.value || null)}
            >
              <option value="">Entire corpus</option>
              {topics.map((item) => (
                <option value={item.topic} key={item.topic}>
                  {topicLabel(item.topic)}
                </option>
              ))}
            </select>
          </label>
          <div
            className="provider-status"
            aria-label={`Provider: ${provider?.model ?? "loading"}`}
          >
            <span className={provider?.live ? "status-light live" : "status-light"} />
            <div>
              <small>
                {!provider
                  ? "Loading provider"
                  : !provider.configured
                    ? "Provider unavailable"
                    : provider.data_destination === "remote_model"
                      ? "Remote provider"
                      : provider.data_destination === "local_model"
                        ? "Local model"
                        : "Local demonstration"}
              </small>
              <strong>{provider?.model ?? "Loading provider…"}</strong>
            </div>
          </div>
        </header>

        <section
          className={empty ? "conversation empty" : "conversation"}
          aria-label="Conversation"
          aria-busy={busy}
        >
          {empty ? (
            <div className="welcome">
              <div className="welcome-kicker">
                <span />
                Repository-grounded conversation
              </div>
              <h1>
                Ask the corpus.
                <br />
                <em>Follow the mathematics.</em>
              </h1>
              <p className="welcome-copy">
                Search definitions, inspect arguments, and trace ideas across the
                combinatorics notes without changing a source file.
              </p>

              <div className="starter-grid">
                {starters[mode].map((starter, index) => (
                  <button
                    type="button"
                    key={starter}
                    onClick={() => void submitMessage(starter)}
                  >
                    <span>0{index + 1}</span>
                    <p>{starter}</p>
                    <ArrowIcon />
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div
              className="message-list"
              aria-live="polite"
              aria-relevant="additions text"
            >
              {messages.map((message) => (
                <article className={`message ${message.role}`} key={message.id}>
                  <div className="message-meta">
                    <span>{message.role === "user" ? "You" : "CRAIG"}</span>
                    {message.role === "assistant" && (
                      <small>{modeLabels[mode]} mode</small>
                    )}
                  </div>
                  <div className="message-body">
                    {message.role === "assistant" ? (
                      message.content ? (
                        <MarkdownMessage>{message.content}</MarkdownMessage>
                      ) : (
                        <div className="thinking-line">
                          <i />
                          <i />
                          <i />
                        </div>
                      )
                    ) : (
                      <p>{message.content}</p>
                    )}
                    {message.role === "assistant" && message.trace !== undefined && (
                      <TracePlayer value={message.trace} />
                    )}
                  </div>
                  {message.role === "assistant" &&
                    message.provenance.length > 0 && (
                      <ProvenancePanel annotations={message.provenance} />
                    )}
                  {message.sources.length > 0 && (
                    <section
                      className="source-section"
                      aria-label="Repository sources"
                    >
                      <div className="source-section-heading">
                        <span>Inspect cited evidence</span>
                        <small>{message.sources.length} passage(s)</small>
                      </div>
                      <div className="source-list">
                        {message.sources.map((source) => (
                          <SourcePanel
                            source={source}
                            key={source.citation_id}
                          />
                        ))}
                      </div>
                    </section>
                  )}
                </article>
              ))}
              {activity && (
                <div className="activity-line" role="status">
                  <span className="activity-pulse" />
                  Using {activity}
                </div>
              )}
              <div ref={endRef} />
            </div>
          )}
        </section>

        <section className="controls">
          <ModelDataNotice destination={provider?.data_destination} />
          {mode === "computation" && (
            <ComputationPanel
              operations={computations}
              busy={busy}
              onRun={(operation, parameters) =>
                void runComputation(operation, parameters)
              }
            />
          )}
          <div className="mode-strip" aria-label="Conversation mode">
            {(Object.keys(modeLabels) as ChatMode[]).map((item) => (
              <button
                type="button"
                className={mode === item ? "active" : ""}
                key={item}
                onClick={() => setMode(item)}
                aria-pressed={mode === item}
                title={
                  configuration?.modes.find((entry) => entry.id === item)
                    ?.description
                }
              >
                {modeLabels[item]}
              </button>
            ))}
          </div>

          <form className="composer" onSubmit={handleSubmit}>
            <textarea
              value={input}
              onChange={(event) => setInput(event.target.value)}
              onKeyDown={handleComposerKeyDown}
              placeholder={`Ask in ${modeLabels[mode].toLowerCase()} mode…`}
              aria-label="Message CRAIG"
              rows={2}
              maxLength={configuration?.max_message_chars ?? 8000}
              disabled={busy}
            />
            <button
              className="send-button"
              type="submit"
              disabled={busy || !input.trim()}
              aria-label="Send message"
            >
              <ArrowIcon />
            </button>
          </form>

          <div className="composer-foot">
            <span
              className={error ? "request-status error" : "request-status"}
              role={error ? "alert" : "status"}
              aria-live="polite"
            >
              {error ?? (busy ? status : activeMode?.description ?? status)}
            </span>
            <span>
              {mode === "computation"
                ? "Use the approved panel to execute · chat remains retrieval-grounded"
                : "Enter to send · Shift+Enter for a new line"}
            </span>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
