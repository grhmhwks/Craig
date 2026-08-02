export type ChatMode =
  | "research"
  | "explanation"
  | "tutorial"
  | "computation";

export type ProvenanceKind =
  | "repository"
  | "deduction"
  | "computation"
  | "model_knowledge"
  | "external";

export type MathematicalStatus =
  | "proved_result"
  | "computer_assisted_proof"
  | "conjecture"
  | "computational_evidence"
  | "experimental_observation"
  | "proof_outline"
  | "work_in_progress"
  | "unknown";

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
  max_source_excerpt_chars: number;
  external_sources_enabled: boolean;
}

export interface TopicsResponse {
  schema_version: 1;
  topics: TopicSummary[];
  total_topics: number;
}

export interface SourceReference {
  citation_id: string;
  topic: string;
  path: string;
  heading: string | null;
  environment: string | null;
  start_line: number;
  end_line: number;
  file_hash: string;
  excerpt: string;
  mathematical_status: MathematicalStatus;
  status_basis: string | null;
}

export interface ProvenanceAnnotation {
  kind: ProvenanceKind;
  description: string;
  citation_ids: string[];
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  created_at: string;
  sources: SourceReference[];
  provenance: ProvenanceAnnotation[];
  trace?: unknown;
}

export interface ChatEvent {
  schema_version: 1;
  type: string;
  conversation_id: string;
  created_at: string;
  data: Record<string, unknown>;
}

export interface BaseSseEvent {
  schema_version: 1;
  type: string;
  created_at: string;
  data: Record<string, unknown>;
}

export type ComputationClassification =
  | "example"
  | "experiment"
  | "finite_check"
  | "computer_assisted_proof";

export interface ComputationLimits {
  wall_time_seconds: number;
  cpu_time_seconds: number;
  memory_bytes: number;
  output_bytes: number;
  stderr_bytes: number;
  request_bytes: number;
}

export interface ComputationParameter {
  name: string;
  kind: "integer" | "string" | "integer_array";
  label: string;
  description: string;
  required: boolean;
  default: unknown;
  minimum: number | null;
  maximum: number | null;
  max_items: number | null;
}

export interface ComputationOperation {
  id: string;
  title: string;
  description: string;
  classification: ComputationClassification;
  implementation_version: string;
  source_basis: {
    path: string;
    start_line: number;
    end_line: number;
  };
  parameters: ComputationParameter[];
  limits: ComputationLimits;
}

export interface ComputationCatalog {
  schema_version: 1;
  operations: ComputationOperation[];
  max_concurrent_workers: number;
  execution_policy: "isolated_allowlist";
}

export interface ComputationEvent extends BaseSseEvent {
  job_id: string;
}

export interface ComputationStreamRequest {
  operation: string;
  parameters: Record<string, unknown>;
}

export interface ChatStreamRequest {
  message: string;
  mode: ChatMode;
  topic: string | null;
  conversation_id: string | null;
}
