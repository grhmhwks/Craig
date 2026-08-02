export const MAX_VISUALIZATION_SOURCE_CHARS = 50_000;
export const MAX_GRID_CELLS = 400;
export const MAX_SEQUENCE_ENTRIES = 80;
export const MAX_GRAPH_VERTICES = 40;
export const MAX_GRAPH_EDGES = 120;

export type Orientation = "top-to-bottom" | "bottom-to-top";
export type CellEntries = string[];

export interface TableauSpec {
  kind: "tableau";
  rows: CellEntries[][];
  variant: "ordinary" | "set-valued" | "primed";
  shifted: boolean;
  orientation: Orientation;
  title: string | null;
}

export interface DiagramSpec {
  kind: "diagram";
  shape: number[];
  innerShape: number[];
  shifted: boolean;
  orientation: Orientation;
  title: string | null;
}

export interface DyckPathSpec {
  kind: "dyck-path";
  pathKind: "ordinary" | "rational";
  steps: Array<"N" | "E">;
  width: number;
  height: number;
  boundary: "above" | "below";
  showDiagonal: boolean;
  progress: number;
  title: string | null;
}

export interface ReadingWordSpec {
  kind: "reading-word";
  entries: string[];
  direction: "left-to-right" | "right-to-left";
  highlights: number[];
  title: string | null;
}

export interface FactorizationSpec {
  kind: "factorization";
  factors: string[][];
  separator: string;
  title: string | null;
}

export interface SkeletonVertex {
  id: string;
  label: string;
  x: number | null;
  y: number | null;
}

export interface SkeletonEdge {
  from: string;
  to: string;
  label: string | null;
}

export interface SkeletonSpec {
  kind: "skeleton";
  vertices: SkeletonVertex[];
  edges: SkeletonEdge[];
  directed: boolean;
  title: string | null;
}

export interface StringEndpoint {
  stringId: string;
  index: number;
}

export interface StringLink {
  from: StringEndpoint;
  to: StringEndpoint;
  label: string | null;
}

export interface StringRow {
  id: string;
  label: string;
  entries: string[];
}

export interface StringDiagramSpec {
  kind: "string-diagram";
  strings: StringRow[];
  links: StringLink[];
  title: string | null;
}

export type VisualizationSpec =
  | TableauSpec
  | DiagramSpec
  | DyckPathSpec
  | ReadingWordSpec
  | FactorizationSpec
  | SkeletonSpec
  | StringDiagramSpec;

export type VisualizationLanguage = VisualizationSpec["kind"];

export type VisualizationParseResult =
  | { ok: true; spec: VisualizationSpec }
  | { ok: false; error: string };

const languageAliases: Record<string, VisualizationLanguage> = {
  tableau: "tableau",
  diagram: "diagram",
  "young-diagram": "diagram",
  dyck: "dyck-path",
  "dyck-path": "dyck-path",
  word: "reading-word",
  "reading-word": "reading-word",
  factorization: "factorization",
  skeleton: "skeleton",
  strings: "string-diagram",
  "string-diagram": "string-diagram",
};

class SpecError extends Error {}

function record(value: unknown, name: string): Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new SpecError(`${name} must be a JSON object.`);
  }
  return value as Record<string, unknown>;
}

function onlyKeys(
  value: Record<string, unknown>,
  allowed: readonly string[],
  name: string,
) {
  const allowedSet = new Set(allowed);
  const unexpected = Object.keys(value).filter((key) => !allowedSet.has(key));
  if (unexpected.length > 0) {
    throw new SpecError(`${name} contains unsupported field: ${unexpected[0]}.`);
  }
}

function array(value: unknown, name: string): unknown[] {
  if (!Array.isArray(value)) {
    throw new SpecError(`${name} must be an array.`);
  }
  return value;
}

function boundedString(
  value: unknown,
  name: string,
  { max = 80, allowEmpty = false }: { max?: number; allowEmpty?: boolean } = {},
): string {
  const stringValue =
    typeof value === "string"
      ? value
      : typeof value === "number" && Number.isFinite(value)
        ? String(value)
        : null;
  if (stringValue === null) {
    throw new SpecError(`${name} must be a string or finite number.`);
  }
  const text = stringValue.trim();
  if (!allowEmpty && !text) {
    throw new SpecError(`${name} cannot be empty.`);
  }
  if (text.length > max) {
    throw new SpecError(`${name} cannot exceed ${max} characters.`);
  }
  return text;
}

function optionalTitle(value: unknown): string | null {
  if (value === undefined || value === null) {
    return null;
  }
  return boundedString(value, "title", { max: 120 });
}

function boolean(value: unknown, name: string, fallback: boolean): boolean {
  if (value === undefined) {
    return fallback;
  }
  if (typeof value !== "boolean") {
    throw new SpecError(`${name} must be true or false.`);
  }
  return value;
}

function choice<T extends string>(
  value: unknown,
  name: string,
  choices: readonly T[],
  fallback: T,
): T {
  if (value === undefined) {
    return fallback;
  }
  if (typeof value !== "string" || !choices.includes(value as T)) {
    throw new SpecError(`${name} must be one of: ${choices.join(", ")}.`);
  }
  return value as T;
}

function integer(
  value: unknown,
  name: string,
  { minimum = 0, maximum = 10_000 }: { minimum?: number; maximum?: number } = {},
): number {
  if (!Number.isInteger(value)) {
    throw new SpecError(`${name} must be an integer.`);
  }
  const number = value as number;
  if (number < minimum || number > maximum) {
    throw new SpecError(`${name} must be between ${minimum} and ${maximum}.`);
  }
  return number;
}

function orientation(value: unknown): Orientation {
  return choice(
    value,
    "orientation",
    ["top-to-bottom", "bottom-to-top"] as const,
    "top-to-bottom",
  );
}

function partition(value: unknown, name: string): number[] {
  const values = array(value, name);
  if (values.length < 1 || values.length > 20) {
    throw new SpecError(`${name} must have between 1 and 20 rows.`);
  }
  const result = values.map((part, index) =>
    integer(part, `${name}[${index}]`, { minimum: 0, maximum: 30 }),
  );
  for (let index = 1; index < result.length; index += 1) {
    if (result[index] > result[index - 1]) {
      throw new SpecError(`${name} must be weakly decreasing.`);
    }
  }
  if (result.reduce((sum, part) => sum + part, 0) > MAX_GRID_CELLS) {
    throw new SpecError(`${name} exceeds the ${MAX_GRID_CELLS}-cell limit.`);
  }
  return result;
}

function cell(value: unknown, name: string): CellEntries {
  const entries = Array.isArray(value) ? value : [value];
  if (entries.length < 1 || entries.length > 12) {
    throw new SpecError(`${name} must contain between 1 and 12 entries.`);
  }
  return entries.map((entry, index) =>
    boundedString(entry, `${name}[${index}]`, { max: 24 }),
  );
}

function parseTableau(value: unknown): TableauSpec {
  const input = record(value, "tableau");
  onlyKeys(
    input,
    ["rows", "variant", "shifted", "orientation", "title"],
    "tableau",
  );
  const rowValues = array(input.rows, "rows");
  if (rowValues.length < 1 || rowValues.length > 20) {
    throw new SpecError("rows must contain between 1 and 20 rows.");
  }
  const rows = rowValues.map((row, rowIndex) => {
    const rowEntries = array(row, `rows[${rowIndex}]`);
    if (rowEntries.length < 1 || rowEntries.length > 30) {
      throw new SpecError(
        `rows[${rowIndex}] must contain between 1 and 30 cells.`,
      );
    }
    return rowEntries.map((entry, columnIndex) =>
      cell(entry, `rows[${rowIndex}][${columnIndex}]`),
    );
  });
  const cellCount = rows.reduce((sum, row) => sum + row.length, 0);
  if (cellCount < 1 || cellCount > MAX_GRID_CELLS) {
    throw new SpecError(
      `tableau must contain between 1 and ${MAX_GRID_CELLS} cells.`,
    );
  }
  for (let index = 1; index < rows.length; index += 1) {
    if (rows[index].length > rows[index - 1].length) {
      throw new SpecError("tableau row lengths must be weakly decreasing.");
    }
  }
  const variant = choice(
    input.variant,
    "variant",
    ["ordinary", "set-valued", "primed"] as const,
    "ordinary",
  );
  const shifted = boolean(input.shifted, "shifted", false);
  if (
    shifted &&
    rows.some(
      (row, index) => index > 0 && row.length >= rows[index - 1].length,
    )
  ) {
    throw new SpecError("shifted tableau row lengths must be strictly decreasing.");
  }
  if (variant !== "set-valued" && rows.some((row) => row.some((item) => item.length > 1))) {
    throw new SpecError("multi-entry cells require variant `set-valued`.");
  }
  return {
    kind: "tableau",
    rows,
    variant,
    shifted,
    orientation: orientation(input.orientation),
    title: optionalTitle(input.title),
  };
}

function parseDiagram(value: unknown): DiagramSpec {
  const input = record(value, "diagram");
  onlyKeys(
    input,
    ["shape", "inner_shape", "shifted", "orientation", "title"],
    "diagram",
  );
  const shape = partition(input.shape, "shape");
  if (shape.reduce((sum, part) => sum + part, 0) < 1) {
    throw new SpecError("shape must contain at least one cell.");
  }
  const innerShape =
    input.inner_shape === undefined ? [] : partition(input.inner_shape, "inner_shape");
  const shifted = boolean(input.shifted, "shifted", false);
  if (
    shifted &&
    shape.some((part, index) => index > 0 && part > 0 && part >= shape[index - 1])
  ) {
    throw new SpecError("a shifted shape must be strictly decreasing.");
  }
  if (
    shifted &&
    innerShape.some(
      (part, index) =>
        index > 0 && part > 0 && part >= innerShape[index - 1],
    )
  ) {
    throw new SpecError("a shifted inner_shape must be strictly decreasing.");
  }
  if (innerShape.length > shape.length) {
    throw new SpecError("inner_shape cannot have more rows than shape.");
  }
  innerShape.forEach((part, index) => {
    if (part > shape[index]) {
      throw new SpecError(`inner_shape[${index}] cannot exceed shape[${index}].`);
    }
  });
  return {
    kind: "diagram",
    shape,
    innerShape,
    shifted,
    orientation: orientation(input.orientation),
    title: optionalTitle(input.title),
  };
}

function parseDyckPath(value: unknown): DyckPathSpec {
  const input = record(value, "dyck path");
  onlyKeys(
    input,
    [
      "steps",
      "kind",
      "r",
      "s",
      "boundary",
      "show_diagonal",
      "progress",
      "title",
    ],
    "dyck path",
  );
  const pathKind = choice(
    input.kind,
    "kind",
    ["ordinary", "rational"] as const,
    "ordinary",
  );
  const rawSteps = boundedString(input.steps, "steps", { max: 160 })
    .toUpperCase()
    .replaceAll(/\s/g, "");
  if (!/^[NE]+$/.test(rawSteps)) {
    throw new SpecError("steps may contain only N and E.");
  }
  const steps = [...rawSteps] as Array<"N" | "E">;
  const eastCount = steps.filter((step) => step === "E").length;
  const northCount = steps.length - eastCount;
  if (eastCount < 1 || northCount < 1) {
    throw new SpecError("steps must contain at least one N and one E.");
  }
  if (pathKind === "ordinary" && eastCount !== northCount) {
    throw new SpecError("an ordinary Dyck path must have equally many N and E steps.");
  }
  const width =
    input.r === undefined
      ? eastCount
      : integer(input.r, "r", { minimum: 1, maximum: 80 });
  const height =
    input.s === undefined
      ? northCount
      : integer(input.s, "s", { minimum: 1, maximum: 80 });
  if (eastCount !== width || northCount !== height) {
    throw new SpecError("the step endpoint must equal (r, s).");
  }
  const boundary = choice(
    input.boundary,
    "boundary",
    ["above", "below"] as const,
    "above",
  );
  let x = 0;
  let y = 0;
  steps.forEach((step, index) => {
    if (step === "E") x += 1;
    else y += 1;
    const signedDistance = width * y - height * x;
    if (
      (boundary === "above" && signedDistance < 0) ||
      (boundary === "below" && signedDistance > 0)
    ) {
      throw new SpecError(
        `steps leave the ${boundary}-diagonal region at position ${index + 1}.`,
      );
    }
  });
  return {
    kind: "dyck-path",
    pathKind,
    steps,
    width,
    height,
    boundary,
    showDiagonal: boolean(input.show_diagonal, "show_diagonal", true),
    progress:
      input.progress === undefined
        ? steps.length
        : integer(input.progress, "progress", {
            minimum: 0,
            maximum: steps.length,
          }),
    title: optionalTitle(input.title),
  };
}

function stringEntries(value: unknown, name: string, maximum = MAX_SEQUENCE_ENTRIES): string[] {
  const values = array(value, name);
  if (values.length < 1 || values.length > maximum) {
    throw new SpecError(`${name} must contain between 1 and ${maximum} entries.`);
  }
  return values.map((entry, index) =>
    boundedString(entry, `${name}[${index}]`, { max: 32 }),
  );
}

function parseReadingWord(value: unknown): ReadingWordSpec {
  const input = record(value, "reading word");
  onlyKeys(input, ["entries", "direction", "highlights", "title"], "reading word");
  const entries = stringEntries(input.entries, "entries");
  const highlights =
    input.highlights === undefined
      ? []
      : array(input.highlights, "highlights").map((entry, index) =>
          integer(entry, `highlights[${index}]`, {
            minimum: 0,
            maximum: entries.length - 1,
          }),
        );
  if (new Set(highlights).size !== highlights.length) {
    throw new SpecError("highlights cannot contain duplicate indexes.");
  }
  return {
    kind: "reading-word",
    entries,
    direction: choice(
      input.direction,
      "direction",
      ["left-to-right", "right-to-left"] as const,
      "left-to-right",
    ),
    highlights,
    title: optionalTitle(input.title),
  };
}

function parseFactorization(value: unknown): FactorizationSpec {
  const input = record(value, "factorization");
  onlyKeys(input, ["factors", "separator", "title"], "factorization");
  const factors = array(input.factors, "factors");
  if (factors.length < 1 || factors.length > 20) {
    throw new SpecError("factors must contain between 1 and 20 factors.");
  }
  const normalized = factors.map((factor, index) =>
    stringEntries(factor, `factors[${index}]`, 40),
  );
  const entryCount = normalized.reduce((sum, factor) => sum + factor.length, 0);
  if (entryCount > MAX_SEQUENCE_ENTRIES) {
    throw new SpecError(
      `factorization exceeds the ${MAX_SEQUENCE_ENTRIES}-entry limit.`,
    );
  }
  return {
    kind: "factorization",
    factors: normalized,
    separator:
      input.separator === undefined
        ? "·"
        : boundedString(input.separator, "separator", { max: 4 }),
    title: optionalTitle(input.title),
  };
}

function coordinate(value: unknown, name: string): number | null {
  if (value === undefined || value === null) return null;
  if (typeof value !== "number" || !Number.isFinite(value) || value < 0 || value > 100) {
    throw new SpecError(`${name} must be a finite number between 0 and 100.`);
  }
  return value;
}

function parseSkeleton(value: unknown): SkeletonSpec {
  const input = record(value, "skeleton");
  onlyKeys(input, ["vertices", "edges", "directed", "title"], "skeleton");
  const vertexValues = array(input.vertices, "vertices");
  if (vertexValues.length < 1 || vertexValues.length > MAX_GRAPH_VERTICES) {
    throw new SpecError(
      `vertices must contain between 1 and ${MAX_GRAPH_VERTICES} items.`,
    );
  }
  const vertices = vertexValues.map((value, index) => {
    const vertex = record(value, `vertices[${index}]`);
    onlyKeys(vertex, ["id", "label", "x", "y"], `vertices[${index}]`);
    return {
      id: boundedString(vertex.id, `vertices[${index}].id`, { max: 40 }),
      label: boundedString(vertex.label, `vertices[${index}].label`, { max: 40 }),
      x: coordinate(vertex.x, `vertices[${index}].x`),
      y: coordinate(vertex.y, `vertices[${index}].y`),
    };
  });
  const ids = new Set(vertices.map((vertex) => vertex.id));
  if (ids.size !== vertices.length) {
    throw new SpecError("vertex ids must be unique.");
  }
  const edgeValues = input.edges === undefined ? [] : array(input.edges, "edges");
  if (edgeValues.length > MAX_GRAPH_EDGES) {
    throw new SpecError(`edges cannot exceed ${MAX_GRAPH_EDGES} items.`);
  }
  const edges = edgeValues.map((value, index) => {
    const edge = record(value, `edges[${index}]`);
    onlyKeys(edge, ["from", "to", "label"], `edges[${index}]`);
    const from = boundedString(edge.from, `edges[${index}].from`, { max: 40 });
    const to = boundedString(edge.to, `edges[${index}].to`, { max: 40 });
    if (!ids.has(from) || !ids.has(to)) {
      throw new SpecError(`edges[${index}] refers to an unknown vertex.`);
    }
    return {
      from,
      to,
      label:
        edge.label === undefined || edge.label === null
          ? null
          : boundedString(edge.label, `edges[${index}].label`, { max: 40 }),
    };
  });
  const explicitCoordinates = vertices.every(
    (vertex) => vertex.x !== null && vertex.y !== null,
  );
  const absentCoordinates = vertices.every(
    (vertex) => vertex.x === null && vertex.y === null,
  );
  if (!explicitCoordinates && !absentCoordinates) {
    throw new SpecError("provide coordinates for every vertex or for none of them.");
  }
  return {
    kind: "skeleton",
    vertices,
    edges,
    directed: boolean(input.directed, "directed", false),
    title: optionalTitle(input.title),
  };
}

function parseEndpoint(
  value: unknown,
  name: string,
  rows: Map<string, number>,
): StringEndpoint {
  const endpoint = record(value, name);
  onlyKeys(endpoint, ["string", "index"], name);
  const stringId = boundedString(endpoint.string, `${name}.string`, { max: 40 });
  const length = rows.get(stringId);
  if (length === undefined) {
    throw new SpecError(`${name} refers to an unknown string.`);
  }
  return {
    stringId,
    index: integer(endpoint.index, `${name}.index`, {
      minimum: 0,
      maximum: length - 1,
    }),
  };
}

function parseStringDiagram(value: unknown): StringDiagramSpec {
  const input = record(value, "string diagram");
  onlyKeys(input, ["strings", "links", "title"], "string diagram");
  const stringValues = array(input.strings, "strings");
  if (stringValues.length < 1 || stringValues.length > 16) {
    throw new SpecError("strings must contain between 1 and 16 rows.");
  }
  const strings = stringValues.map((value, index) => {
    const row = record(value, `strings[${index}]`);
    onlyKeys(row, ["id", "label", "entries"], `strings[${index}]`);
    return {
      id: boundedString(row.id, `strings[${index}].id`, { max: 40 }),
      label: boundedString(row.label, `strings[${index}].label`, { max: 60 }),
      entries: stringEntries(row.entries, `strings[${index}].entries`, 30),
    };
  });
  const entryCount = strings.reduce((sum, row) => sum + row.entries.length, 0);
  if (entryCount > MAX_GRID_CELLS) {
    throw new SpecError(
      `string diagram exceeds the ${MAX_GRID_CELLS}-entry limit.`,
    );
  }
  const rowLengths = new Map(strings.map((row) => [row.id, row.entries.length]));
  if (rowLengths.size !== strings.length) {
    throw new SpecError("string ids must be unique.");
  }
  const linkValues = input.links === undefined ? [] : array(input.links, "links");
  if (linkValues.length > MAX_GRAPH_EDGES) {
    throw new SpecError(`links cannot exceed ${MAX_GRAPH_EDGES} items.`);
  }
  const links = linkValues.map((value, index) => {
    const link = record(value, `links[${index}]`);
    onlyKeys(link, ["from", "to", "label"], `links[${index}]`);
    return {
      from: parseEndpoint(link.from, `links[${index}].from`, rowLengths),
      to: parseEndpoint(link.to, `links[${index}].to`, rowLengths),
      label:
        link.label === undefined || link.label === null
          ? null
          : boundedString(link.label, `links[${index}].label`, { max: 40 }),
    };
  });
  return {
    kind: "string-diagram",
    strings,
    links,
    title: optionalTitle(input.title),
  };
}

export function visualizationLanguage(
  language: string | null | undefined,
): VisualizationLanguage | null {
  if (!language) return null;
  return languageAliases[language.trim().toLowerCase()] ?? null;
}

export function languageFromClassName(
  className: string | undefined,
): VisualizationLanguage | null {
  const match = /(?:^|\s)language-([\w-]+)/.exec(className ?? "");
  return visualizationLanguage(match?.[1]);
}

export function parseVisualizationBlock(
  language: string,
  source: string,
): VisualizationParseResult {
  const kind = visualizationLanguage(language);
  if (!kind) {
    return { ok: false, error: `Unsupported visualization language: ${language}.` };
  }
  if (source.length > MAX_VISUALIZATION_SOURCE_CHARS) {
    return {
      ok: false,
      error: `Visualization JSON exceeds ${MAX_VISUALIZATION_SOURCE_CHARS} characters.`,
    };
  }
  try {
    const value: unknown = JSON.parse(source);
    const spec =
      kind === "tableau"
        ? parseTableau(value)
        : kind === "diagram"
          ? parseDiagram(value)
          : kind === "dyck-path"
            ? parseDyckPath(value)
            : kind === "reading-word"
              ? parseReadingWord(value)
              : kind === "factorization"
                ? parseFactorization(value)
                : kind === "skeleton"
                  ? parseSkeleton(value)
                  : parseStringDiagram(value);
    return { ok: true, spec };
  } catch (error) {
    return {
      ok: false,
      error: error instanceof Error ? error.message : "Invalid visualization JSON.",
    };
  }
}
