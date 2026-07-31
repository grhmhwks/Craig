export type ChatMode =
  | "research"
  | "explanation"
  | "tutorial"
  | "computation";

export interface TopicSummary {
  topic: string;
  file_count: number;
  chunk_count: number;
}

export interface ProviderStatus {
  name: string;
  model: string;
  configured: boolean;
  live: boolean;
}

export interface ModeConfig {
  id: ChatMode;
  description: string;
  computation_enabled: boolean;
}

export interface ChatConfiguration {
  schema_version: 1;
  provider: ProviderStatus;
  modes: ModeConfig[];
  stream_transport: "sse";
  conversation_storage: "memory";
  max_message_chars: number;
}

export interface TopicsResponse {
  schema_version: 1;
  topics: TopicSummary[];
  total_topics: number;
}

export interface SourceReference {
  topic: string;
  path: string;
  heading: string | null;
  environment: string | null;
  start_line: number;
  end_line: number;
  file_hash: string;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  created_at: string;
  sources: SourceReference[];
}

export interface ChatEvent {
  schema_version: 1;
  type: string;
  conversation_id: string;
  created_at: string;
  data: Record<string, unknown>;
}

export interface ChatStreamRequest {
  message: string;
  mode: ChatMode;
  topic: string | null;
  conversation_id: string | null;
}
