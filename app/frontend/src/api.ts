import { parseSseFrames } from "./lib/sse";
import type {
  ChatConfiguration,
  ChatEvent,
  ChatStreamRequest,
  ComputationCatalog,
  ComputationEvent,
  ComputationStreamRequest,
  TopicsResponse,
} from "./types";

async function readError(response: Response): Promise<string> {
  try {
    const payload = (await response.json()) as {
      error?: { message?: string };
    };
    return payload.error?.message ?? `Request failed with ${response.status}`;
  } catch {
    return `Request failed with ${response.status}`;
  }
}

async function getJson<T>(path: string): Promise<T> {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(await readError(response));
  }
  return (await response.json()) as T;
}

export async function loadBootstrap(): Promise<{
  configuration: ChatConfiguration;
  topics: TopicsResponse;
  computations: ComputationCatalog;
}> {
  const [configuration, topics, computations] = await Promise.all([
    getJson<ChatConfiguration>("/api/v1/chat/config"),
    getJson<TopicsResponse>("/api/v1/topics"),
    getJson<ComputationCatalog>("/api/v1/computations"),
  ]);
  return { configuration, topics, computations };
}

export async function streamChat(
  request: ChatStreamRequest,
  onEvent: (event: ChatEvent) => void,
  signal?: AbortSignal,
): Promise<void> {
  const response = await fetch("/api/v1/chat/stream", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
    signal,
  });
  if (!response.ok) {
    throw new Error(await readError(response));
  }
  if (!response.body) {
    throw new Error("The browser did not provide a streaming response body.");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  while (true) {
    const { done, value } = await reader.read();
    buffer += decoder.decode(value, { stream: !done });
    const parsed = parseSseFrames<ChatEvent>(buffer);
    buffer = parsed.remainder;
    parsed.events.forEach(onEvent);
    if (done) {
      break;
    }
  }
  if (buffer.trim()) {
    const parsed = parseSseFrames<ChatEvent>(`${buffer}\n\n`);
    parsed.events.forEach(onEvent);
  }
}

export async function streamComputation(
  request: ComputationStreamRequest,
  onEvent: (event: ComputationEvent) => void,
  signal?: AbortSignal,
): Promise<void> {
  const response = await fetch("/api/v1/computations/stream", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
    signal,
  });
  if (!response.ok) {
    throw new Error(await readError(response));
  }
  if (!response.body) {
    throw new Error("The browser did not provide a computation stream.");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  while (true) {
    const { done, value } = await reader.read();
    buffer += decoder.decode(value, { stream: !done });
    const parsed = parseSseFrames<ComputationEvent>(buffer);
    buffer = parsed.remainder;
    parsed.events.forEach(onEvent);
    if (done) break;
  }
  if (buffer.trim()) {
    const parsed = parseSseFrames<ComputationEvent>(`${buffer}\n\n`);
    parsed.events.forEach(onEvent);
  }
}
