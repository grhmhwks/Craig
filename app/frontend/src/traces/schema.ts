import { parseVisualizationBlock } from "../visualizations/schema";

export const TRACE_SCHEMA_VERSION = 1;
export const MAX_TRACE_EVENTS = 192;
export const MAX_TRACE_BYTES = 196_608;
export const MAX_TRACE_STATE_BYTES = 32_768;

export const traceEventKinds = [
  "initialization",
  "insertion",
  "bumping",
  "extraction",
  "reinsertion",
  "recording",
  "local_move",
  "completion",
] as const;

export type TraceEventKind = (typeof traceEventKinds)[number];

export interface TraceVisualization {
  label: string;
  language: string;
  source: string;
}

export interface AlgorithmTraceEvent {
  index: number;
  kind: TraceEventKind;
  title: string;
  description: string;
  state: Record<string, unknown>;
  visualizations: TraceVisualization[];
}

export interface AlgorithmTrace {
  schemaVersion: 1;
  algorithm: string;
  title: string;
  events: AlgorithmTraceEvent[];
}

export type TraceParseResult =
  | { ok: true; trace: AlgorithmTrace }
  | { ok: false; error: string };

class TraceSpecError extends Error {}

function record(value: unknown, name: string): Record<string, unknown> {
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    throw new TraceSpecError(`${name} must be an object.`);
  }
  return value as Record<string, unknown>;
}

function onlyKeys(
  value: Record<string, unknown>,
  allowed: readonly string[],
  name: string,
) {
  const extra = Object.keys(value).find((key) => !allowed.includes(key));
  if (extra) {
    throw new TraceSpecError(`${name} contains unsupported field: ${extra}.`);
  }
}

function textValue(value: unknown, name: string, maximum: number): string {
  if (typeof value !== "string" || value.trim().length === 0) {
    throw new TraceSpecError(`${name} must be a non-empty string.`);
  }
  const normalized = value.trim();
  if (normalized.length > maximum) {
    throw new TraceSpecError(`${name} cannot exceed ${maximum} characters.`);
  }
  return normalized;
}

function serialized(value: unknown, name: string): string {
  try {
    const result = JSON.stringify(value);
    if (result === undefined) throw new Error("not JSON");
    return result;
  } catch {
    throw new TraceSpecError(`${name} must contain only JSON values.`);
  }
}

function byteLength(value: string): number {
  return new TextEncoder().encode(value).byteLength;
}

export function parseAlgorithmTrace(value: unknown): TraceParseResult {
  try {
    const source = serialized(value, "trace");
    if (byteLength(source) > MAX_TRACE_BYTES) {
      throw new TraceSpecError(`trace exceeds the ${MAX_TRACE_BYTES}-byte limit.`);
    }
    const input = record(value, "trace");
    onlyKeys(input, ["schema_version", "algorithm", "title", "events"], "trace");
    if (input.schema_version !== TRACE_SCHEMA_VERSION) {
      throw new TraceSpecError("trace schema_version must equal 1.");
    }
    const eventValues = input.events;
    if (!Array.isArray(eventValues)) {
      throw new TraceSpecError("events must be an array.");
    }
    if (eventValues.length < 1 || eventValues.length > MAX_TRACE_EVENTS) {
      throw new TraceSpecError(
        `events must contain between 1 and ${MAX_TRACE_EVENTS} entries.`,
      );
    }
    const events = eventValues.map((value, expectedIndex) => {
      const event = record(value, `events[${expectedIndex}]`);
      onlyKeys(
        event,
        ["index", "kind", "title", "description", "state", "visualizations"],
        `events[${expectedIndex}]`,
      );
      if (event.index !== expectedIndex) {
        throw new TraceSpecError("event indexes must be contiguous and zero-based.");
      }
      if (
        typeof event.kind !== "string" ||
        !traceEventKinds.includes(event.kind as TraceEventKind)
      ) {
        throw new TraceSpecError(`events[${expectedIndex}].kind is not recognized.`);
      }
      const state = record(event.state, `events[${expectedIndex}].state`);
      if (byteLength(serialized(state, "event state")) > MAX_TRACE_STATE_BYTES) {
        throw new TraceSpecError(`events[${expectedIndex}].state is too large.`);
      }
      if (!Array.isArray(event.visualizations) || event.visualizations.length > 3) {
        throw new TraceSpecError(
          `events[${expectedIndex}].visualizations must contain at most 3 entries.`,
        );
      }
      const visualizations = event.visualizations.map((item, visualizationIndex) => {
        const visualization = record(
          item,
          `events[${expectedIndex}].visualizations[${visualizationIndex}]`,
        );
        onlyKeys(
          visualization,
          ["label", "language", "spec"],
          `events[${expectedIndex}].visualizations[${visualizationIndex}]`,
        );
        const language = textValue(visualization.language, "language", 40);
        const visualizationSource = serialized(visualization.spec, "visualization spec");
        const parsed = parseVisualizationBlock(language, visualizationSource);
        if (!parsed.ok) {
          throw new TraceSpecError(`invalid trace visualization: ${parsed.error}`);
        }
        return {
          label: textValue(visualization.label, "visualization label", 80),
          language,
          source: visualizationSource,
        };
      });
      return {
        index: expectedIndex,
        kind: event.kind as TraceEventKind,
        title: textValue(event.title, "event title", 100),
        description: textValue(event.description, "event description", 320),
        state,
        visualizations,
      };
    });
    return {
      ok: true,
      trace: {
        schemaVersion: 1,
        algorithm: textValue(input.algorithm, "algorithm", 80),
        title: textValue(input.title, "trace title", 120),
        events,
      },
    };
  } catch (error) {
    return {
      ok: false,
      error: error instanceof Error ? error.message : "Invalid algorithm trace.",
    };
  }
}
