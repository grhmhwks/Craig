import { useEffect, useRef, useState } from "react";
import type { FormEvent, KeyboardEvent } from "react";
import ReactMarkdown from "react-markdown";

import { loadBootstrap, streamChat } from "./api";
import type {
  ChatConfiguration,
  ChatEvent,
  ChatMessage,
  ChatMode,
  SourceReference,
  TopicSummary,
} from "./types";

const modeLabels: Record<ChatMode, string> = {
  research: "Research",
  explanation: "Explain",
  tutorial: "Tutorial",
  computation: "Computation",
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
  return `${source.path}:${source.start_line}–${source.end_line}`;
}

function App() {
  const [configuration, setConfiguration] =
    useState<ChatConfiguration | null>(null);
  const [topics, setTopics] = useState<TopicSummary[]>([]);
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
      .then(({ configuration: nextConfiguration, topics: nextTopics }) => {
        setConfiguration(nextConfiguration);
        setTopics(nextTopics.topics);
      })
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
          message.id === pendingAssistantId ? completed : message,
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
    };
    const pendingAssistantId = `local_assistant_${crypto.randomUUID()}`;
    const pendingAssistant: ChatMessage = {
      id: pendingAssistantId,
      role: "assistant",
      content: "",
      created_at: now,
      sources: [],
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

        <button className="new-chat" type="button" onClick={beginNewConversation}>
          <SparkIcon />
          New conversation
        </button>

        <nav className="scope-nav" aria-label="Repository topics">
          <p className="nav-label">Research scope</p>
          <button
            className={topic === null ? "scope-item active" : "scope-item"}
            type="button"
            onClick={() => setTopic(null)}
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

      <main className="workspace">
        <header className="topbar">
          <div className="scope-title">
            <span>Current scope</span>
            <strong>{topic ? topicLabel(topic) : "Entire corpus"}</strong>
          </div>
          <div className="provider-status">
            <span className={provider?.live ? "status-light live" : "status-light"} />
            <div>
              <small>{provider?.live ? "Live provider" : "Local demonstration"}</small>
              <strong>{provider?.model ?? "Loading provider…"}</strong>
            </div>
          </div>
        </header>

        <section className={empty ? "conversation empty" : "conversation"}>
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
            <div className="message-list" aria-live="polite">
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
                        <ReactMarkdown>{message.content}</ReactMarkdown>
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
                  </div>
                  {message.sources.length > 0 && (
                    <div className="source-row" aria-label="Repository sources">
                      {message.sources.slice(0, 6).map((source) => (
                        <span
                          className="source-chip"
                          key={`${source.path}:${source.start_line}:${source.end_line}`}
                          title={source.heading ?? source.path}
                        >
                          {sourceLabel(source)}
                        </span>
                      ))}
                    </div>
                  )}
                </article>
              ))}
              {activity && (
                <div className="activity-line">
                  <span className="activity-pulse" />
                  Using {activity}
                </div>
              )}
              <div ref={endRef} />
            </div>
          )}
        </section>

        <section className="controls">
          <div className="mode-strip" aria-label="Conversation mode">
            {(Object.keys(modeLabels) as ChatMode[]).map((item) => (
              <button
                type="button"
                className={mode === item ? "active" : ""}
                key={item}
                onClick={() => setMode(item)}
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
            <span className={error ? "request-status error" : "request-status"}>
              {error ?? (busy ? status : activeMode?.description ?? status)}
            </span>
            <span>
              {mode === "computation"
                ? "Inspection only · execution arrives in Phase 6"
                : "Enter to send · Shift+Enter for a new line"}
            </span>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
