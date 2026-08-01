import type { BaseSseEvent, ChatEvent } from "../types";

export interface ParsedSse<Event extends BaseSseEvent> {
  events: Event[];
  remainder: string;
}

function nextBoundary(buffer: string): { index: number; length: number } | null {
  const lf = buffer.indexOf("\n\n");
  const crlf = buffer.indexOf("\r\n\r\n");
  if (lf < 0 && crlf < 0) {
    return null;
  }
  if (crlf >= 0 && (lf < 0 || crlf < lf)) {
    return { index: crlf, length: 4 };
  }
  return { index: lf, length: 2 };
}

export function parseSseFrames<
  Event extends BaseSseEvent = ChatEvent,
>(buffer: string): ParsedSse<Event> {
  const events: Event[] = [];
  let remainder = buffer;

  while (true) {
    const boundary = nextBoundary(remainder);
    if (!boundary) {
      break;
    }
    const frame = remainder.slice(0, boundary.index);
    remainder = remainder.slice(boundary.index + boundary.length);
    const data = frame
      .split(/\r?\n/)
      .filter((line) => line.startsWith("data:"))
      .map((line) => line.replace(/^data:\s?/, ""))
      .join("\n");
    if (!data) {
      continue;
    }
    events.push(JSON.parse(data) as Event);
  }

  return { events, remainder };
}
