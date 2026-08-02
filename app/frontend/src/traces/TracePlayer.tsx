import { useEffect, useMemo, useState } from "react";
import type { KeyboardEvent } from "react";

import { VisualizationBlock } from "../visualizations/VisualizationBlock";
import { parseAlgorithmTrace } from "./schema";

export type TraceNavigationAction = "first" | "previous" | "next" | "last";

export function traceIndexAfter(
  current: number,
  action: TraceNavigationAction,
  lastIndex: number,
): number {
  if (action === "first") return 0;
  if (action === "last") return lastIndex;
  if (action === "previous") return Math.max(0, current - 1);
  return Math.min(lastIndex, current + 1);
}

export function TracePlayer({ value }: { value: unknown }) {
  const parsed = useMemo(() => parseAlgorithmTrace(value), [value]);
  const [index, setIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [intervalMs, setIntervalMs] = useState(900);
  const [reducedMotion, setReducedMotion] = useState(false);

  useEffect(() => {
    setIndex(0);
    setPlaying(false);
  }, [value]);

  useEffect(() => {
    const query = window.matchMedia?.("(prefers-reduced-motion: reduce)");
    if (!query) return;
    const update = () => {
      setReducedMotion(query.matches);
      if (query.matches) setPlaying(false);
    };
    update();
    query.addEventListener?.("change", update);
    return () => query.removeEventListener?.("change", update);
  }, []);

  const lastIndex = parsed.ok ? parsed.trace.events.length - 1 : 0;

  useEffect(() => {
    if (!playing || !parsed.ok || reducedMotion) return;
    const timer = window.setInterval(() => {
      setIndex((current) => {
        if (current >= parsed.trace.events.length - 1) {
          setPlaying(false);
          return current;
        }
        return current + 1;
      });
    }, intervalMs);
    return () => window.clearInterval(timer);
  }, [intervalMs, parsed, playing, reducedMotion]);

  if (!parsed.ok) {
    return (
      <section className="trace-fallback" role="status">
        <strong>Algorithm trace unavailable</strong>
        <span>{parsed.error}</span>
      </section>
    );
  }

  const event = parsed.trace.events[index];

  function navigate(action: TraceNavigationAction) {
    setPlaying(false);
    setIndex((current) => traceIndexAfter(current, action, lastIndex));
  }

  function handleKeyDown(keyboardEvent: KeyboardEvent<HTMLElement>) {
    const target = keyboardEvent.target as HTMLElement;
    if (
      target !== keyboardEvent.currentTarget &&
      ["BUTTON", "INPUT", "SELECT", "SUMMARY"].includes(target.tagName)
    ) {
      return;
    }
    if (keyboardEvent.key === "ArrowLeft") navigate("previous");
    else if (keyboardEvent.key === "ArrowRight") navigate("next");
    else if (keyboardEvent.key === "Home") navigate("first");
    else if (keyboardEvent.key === "End") navigate("last");
    else if (keyboardEvent.key === " " && !reducedMotion) {
      keyboardEvent.preventDefault();
      setPlaying((current) => !current && index < lastIndex);
    } else return;
    keyboardEvent.preventDefault();
  }

  return (
    <section
      className="trace-player"
      aria-label={`Algorithm trace: ${parsed.trace.title}`}
      onKeyDown={handleKeyDown}
      tabIndex={0}
    >
      <header className="trace-heading">
        <div>
          <span>Deterministic trace</span>
          <strong>{parsed.trace.title}</strong>
        </div>
        <code>{parsed.trace.algorithm}</code>
      </header>

      <div className="trace-controls" aria-label="Trace playback controls">
        <button type="button" onClick={() => navigate("first")} disabled={index === 0}>
          First
        </button>
        <button type="button" onClick={() => navigate("previous")} disabled={index === 0}>
          Previous
        </button>
        <button
          type="button"
          onClick={() => {
            if (index === lastIndex) setIndex(0);
            setPlaying((current) => !current);
          }}
          disabled={reducedMotion || lastIndex === 0}
          title={
            reducedMotion
              ? "Autoplay is disabled by reduced-motion preferences."
              : undefined
          }
        >
          {playing ? "Pause" : "Play"}
        </button>
        <button type="button" onClick={() => navigate("next")} disabled={index === lastIndex}>
          Next
        </button>
        <button type="button" onClick={() => navigate("last")} disabled={index === lastIndex}>
          Last
        </button>
        <label>
          <span>Speed</span>
          <select
            aria-label="Playback speed"
            value={intervalMs}
            disabled={reducedMotion}
            onChange={(changeEvent) => setIntervalMs(Number(changeEvent.target.value))}
          >
            <option value={1500}>Slow</option>
            <option value={900}>Normal</option>
            <option value={450}>Fast</option>
          </select>
        </label>
      </div>

      <label className="trace-scrubber">
        <span>
          Step {index + 1} of {parsed.trace.events.length}
        </span>
        <input
          type="range"
          min={0}
          max={lastIndex}
          value={index}
          aria-label="Trace step"
          onChange={(changeEvent) => {
            setPlaying(false);
            setIndex(Number(changeEvent.target.value));
          }}
        />
      </label>

      <article className="trace-event" aria-live="polite">
        <div className="trace-event-heading">
          <span className={`trace-kind kind-${event.kind}`}>
            {event.kind.replaceAll("_", " ")}
          </span>
          <div>
            <strong>{event.title}</strong>
            <p>{event.description}</p>
          </div>
        </div>
        {event.visualizations.length > 0 && (
          <div className="trace-visualizations">
            {event.visualizations.map((visualization, visualizationIndex) => (
              <section
                className="trace-visualization"
                key={`${event.index}:${visualizationIndex}:${visualization.label}`}
              >
                <h4>{visualization.label}</h4>
                <VisualizationBlock
                  language={visualization.language}
                  source={visualization.source}
                />
              </section>
            ))}
          </div>
        )}
        <details className="trace-state" open>
          <summary>Inspect mathematical state at this step</summary>
          <pre>{JSON.stringify(event.state, null, 2)}</pre>
        </details>
      </article>
      {reducedMotion && (
        <p className="trace-motion-note">
          Autoplay is disabled because reduced motion is enabled. Manual controls remain available.
        </p>
      )}
    </section>
  );
}
