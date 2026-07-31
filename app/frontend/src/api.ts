import { parseSseFrames } from "./lib/sse";
import type {
  ChatConfiguration,
  ChatEvent,
  ChatStreamRequest,
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
}> {
  const [configuration, topics] = await Promise.all([
    getJson<ChatConfiguration>("/api/v1/chat/config"),
    getJson<TopicsResponse>("/api/v1/topics"),
  ]);
  return { configuration, topics };
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
    const parsed = parseSseFrames(buffer);
    buffer = parsed.remainder;
    parsed.events.forEach(onEvent);
    if (done) {
      break;
    }
  }
  if (buffer.trim()) {
    const parsed = parseSseFrames(`${buffer}\n\n`);
    parsed.events.forEach(onEvent);
  }
}
