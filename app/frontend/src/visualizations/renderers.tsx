import { useId } from "react";

import { SvgFrame } from "./SvgFrame";
import type {
  DiagramSpec,
  DyckPathSpec,
  FactorizationSpec,
  ReadingWordSpec,
  SkeletonSpec,
  StringDiagramSpec,
  StringEndpoint,
  TableauSpec,
} from "./schema";

const CELL_SIZE = 52;
const MARGIN = 18;

function reversedRows<T>(rows: T[], orientation: string): Array<[T, number]> {
  const indexed = rows.map((row, index) => [row, index] as [T, number]);
  return orientation === "bottom-to-top" ? indexed.reverse() : indexed;
}

function fallbackTitle(title: string | null, fallback: string): string {
  return title ?? fallback;
}

export function TableauRenderer({ spec }: { spec: TableauSpec }) {
  const shiftedOffset = spec.shifted ? spec.rows.length - 1 : 0;
  const columns = Math.max(...spec.rows.map((row, index) => row.length + (spec.shifted ? index : 0)));
  const width = (Math.max(columns, shiftedOffset + 1) * CELL_SIZE) + MARGIN * 2;
  const height = spec.rows.length * CELL_SIZE + MARGIN * 2;
  const title = fallbackTitle(
    spec.title,
    `${spec.shifted ? "Shifted " : ""}${spec.variant} tableau`,
  );

  return (
    <SvgFrame
      width={width}
      height={height}
      title={title}
      description={`${spec.rows.length} rows in ${spec.orientation} orientation.`}
      className="tableau-visualization"
    >
      {reversedRows(spec.rows, spec.orientation).flatMap(
        ([row, logicalRow], displayRow) =>
          row.map((entries, column) => {
            const x =
              MARGIN +
              (spec.shifted ? logicalRow * CELL_SIZE : 0) +
              column * CELL_SIZE;
            const y = MARGIN + displayRow * CELL_SIZE;
            const value = entries.join(", ");
            return (
              <g key={`${logicalRow}:${column}`}>
                <rect
                  className="visual-cell"
                  x={x}
                  y={y}
                  width={CELL_SIZE}
                  height={CELL_SIZE}
                  rx={2}
                />
                <text
                  className={
                    entries.length > 1
                      ? "visual-cell-text visual-cell-text-small"
                      : "visual-cell-text"
                  }
                  x={x + CELL_SIZE / 2}
                  y={y + CELL_SIZE / 2}
                  textAnchor="middle"
                  dominantBaseline="central"
                >
                  {value}
                </text>
              </g>
            );
          }),
      )}
    </SvgFrame>
  );
}

export function DiagramRenderer({ spec }: { spec: DiagramSpec }) {
  const columns = Math.max(
    ...spec.shape.map((length, index) => length + (spec.shifted ? index : 0)),
  );
  const width = columns * CELL_SIZE + MARGIN * 2;
  const height = spec.shape.length * CELL_SIZE + MARGIN * 2;
  const isSkew = spec.innerShape.some((part) => part > 0);
  const title = fallbackTitle(
    spec.title,
    `${spec.shifted ? "Shifted " : ""}${isSkew ? "skew " : ""}Young diagram`,
  );

  return (
    <SvgFrame
      width={width}
      height={height}
      title={title}
      description={`Shape (${spec.shape.join(", ")})${
        isSkew ? ` with inner shape (${spec.innerShape.join(", ")})` : ""
      }.`}
      className="diagram-visualization"
    >
      {reversedRows(spec.shape, spec.orientation).flatMap(
        ([rowLength, logicalRow], displayRow) => {
          const innerLength = spec.innerShape[logicalRow] ?? 0;
          return Array.from({ length: rowLength - innerLength }, (_, index) => {
            const column = innerLength + index;
            const x =
              MARGIN +
              (spec.shifted ? logicalRow * CELL_SIZE : 0) +
              column * CELL_SIZE;
            const y = MARGIN + displayRow * CELL_SIZE;
            return (
              <rect
                className="visual-cell diagram-cell"
                key={`${logicalRow}:${column}`}
                x={x}
                y={y}
                width={CELL_SIZE}
                height={CELL_SIZE}
                rx={1}
              />
            );
          });
        },
      )}
    </SvgFrame>
  );
}

export function DyckPathRenderer({ spec }: { spec: DyckPathSpec }) {
  const longestSide = Math.max(spec.width, spec.height);
  const stepSize = Math.max(12, Math.min(42, 610 / longestSide));
  const plotWidth = spec.width * stepSize;
  const plotHeight = spec.height * stepSize;
  const margin = 34;
  const points: Array<[number, number]> = [[0, 0]];
  let x = 0;
  let y = 0;
  spec.steps.forEach((step) => {
    if (step === "E") x += 1;
    else y += 1;
    points.push([x, y]);
  });
  const pointString = points
    .map(([pointX, pointY]) =>
      `${margin + pointX * stepSize},${margin + plotHeight - pointY * stepSize}`,
    )
    .join(" ");
  const completedPointString = points
    .slice(0, spec.progress + 1)
    .map(
      ([pointX, pointY]) =>
        `${margin + pointX * stepSize},${margin + plotHeight - pointY * stepSize}`,
    )
    .join(" ");
  const activePoint = points[spec.progress];
  const title = fallbackTitle(
    spec.title,
    spec.pathKind === "ordinary"
      ? `Dyck path of semilength ${spec.width}`
      : `Rational Dyck path (${spec.width}, ${spec.height})`,
  );

  return (
    <SvgFrame
      width={plotWidth + margin * 2}
      height={plotHeight + margin * 2}
      title={title}
      description={`${spec.progress} of ${spec.steps.length} steps shown, staying ${spec.boundary} the diagonal.`}
      className="dyck-visualization"
    >
      {Array.from({ length: spec.width + 1 }, (_, index) => (
        <line
          className="dyck-grid"
          key={`vertical:${index}`}
          x1={margin + index * stepSize}
          y1={margin}
          x2={margin + index * stepSize}
          y2={margin + plotHeight}
        />
      ))}
      {Array.from({ length: spec.height + 1 }, (_, index) => (
        <line
          className="dyck-grid"
          key={`horizontal:${index}`}
          x1={margin}
          y1={margin + index * stepSize}
          x2={margin + plotWidth}
          y2={margin + index * stepSize}
        />
      ))}
      {spec.showDiagonal && (
        <line
          className="dyck-diagonal"
          x1={margin}
          y1={margin + plotHeight}
          x2={margin + plotWidth}
          y2={margin}
        />
      )}
      {spec.progress < spec.steps.length && (
        <polyline className="dyck-path-pending" points={pointString} />
      )}
      <polyline className="dyck-path" points={completedPointString} />
      {points.map(([pointX, pointY], index) => (
        <circle
          className={index <= spec.progress ? "dyck-point" : "dyck-point pending"}
          key={`${pointX}:${pointY}:${index}`}
          cx={margin + pointX * stepSize}
          cy={margin + plotHeight - pointY * stepSize}
          r={Math.max(2.2, stepSize * 0.08)}
        />
      ))}
      {activePoint && (
        <circle
          className="dyck-active-point"
          cx={margin + activePoint[0] * stepSize}
          cy={margin + plotHeight - activePoint[1] * stepSize}
          r={Math.max(4, stepSize * 0.14)}
        />
      )}
      <text className="axis-label" x={margin - 7} y={margin + plotHeight + 18}>
        0
      </text>
      <text
        className="axis-label"
        x={margin + plotWidth - 4}
        y={margin + plotHeight + 18}
      >
        {spec.width}
      </text>
      <text className="axis-label" x={margin - 22} y={margin + 4}>
        {spec.height}
      </text>
    </SvgFrame>
  );
}

export function ReadingWordRenderer({ spec }: { spec: ReadingWordSpec }) {
  const entries =
    spec.direction === "right-to-left" ? [...spec.entries].reverse() : spec.entries;
  const highlighted = new Set(spec.highlights);
  return (
    <figure className="math-visualization sequence-visualization">
      <div
        className={`word-sequence direction-${spec.direction}`}
        role="img"
        aria-label={`${spec.direction} reading word: ${spec.entries.join(", ")}`}
      >
        {entries.map((entry, displayIndex) => {
          const logicalIndex =
            spec.direction === "right-to-left"
              ? spec.entries.length - displayIndex - 1
              : displayIndex;
          return (
            <span
              className={highlighted.has(logicalIndex) ? "highlighted" : ""}
              key={`${logicalIndex}:${entry}`}
            >
              <small>{logicalIndex + 1}</small>
              <strong>{entry}</strong>
            </span>
          );
        })}
      </div>
      <figcaption>
        {fallbackTitle(spec.title, `${spec.direction} reading word`)}
      </figcaption>
    </figure>
  );
}

export function FactorizationRenderer({ spec }: { spec: FactorizationSpec }) {
  return (
    <figure className="math-visualization sequence-visualization">
      <div
        className="factorization-row"
        role="img"
        aria-label={`Factorization: ${spec.factors
          .map((factor) => factor.join(" "))
          .join(` ${spec.separator} `)}`}
      >
        {spec.factors.map((factor, factorIndex) => (
          <span className="factor-group" key={`${factorIndex}:${factor.join(":")}`}>
            <small>factor {factorIndex + 1}</small>
            <span>
              {factor.map((entry, entryIndex) => (
                <strong key={`${entryIndex}:${entry}`}>{entry}</strong>
              ))}
            </span>
            {factorIndex < spec.factors.length - 1 && (
              <i aria-hidden="true">{spec.separator}</i>
            )}
          </span>
        ))}
      </div>
      <figcaption>{fallbackTitle(spec.title, "Factorization")}</figcaption>
    </figure>
  );
}

interface PositionedVertex {
  id: string;
  label: string;
  x: number;
  y: number;
}

function skeletonPositions(spec: SkeletonSpec): PositionedVertex[] {
  const explicit = spec.vertices.every(
    (vertex) => vertex.x !== null && vertex.y !== null,
  );
  if (explicit) {
    return spec.vertices.map((vertex) => ({
      id: vertex.id,
      label: vertex.label,
      x: 50 + (vertex.x ?? 0) * 5.2,
      y: 40 + (vertex.y ?? 0) * 3,
    }));
  }
  return spec.vertices.map((vertex, index) => {
    const angle = (Math.PI * 2 * index) / spec.vertices.length - Math.PI / 2;
    return {
      id: vertex.id,
      label: vertex.label,
      x: 310 + Math.cos(angle) * 210,
      y: 190 + Math.sin(angle) * 125,
    };
  });
}

export function SkeletonRenderer({ spec }: { spec: SkeletonSpec }) {
  const markerId = `arrow-${useId().replaceAll(":", "")}`;
  const vertices = skeletonPositions(spec);
  const byId = new Map(vertices.map((vertex) => [vertex.id, vertex]));
  const title = fallbackTitle(spec.title, "Skeleton diagram");
  return (
    <SvgFrame
      width={620}
      height={380}
      title={title}
      description={`${vertices.length} vertices and ${spec.edges.length} edges.`}
      className="skeleton-visualization"
    >
      <defs>
        <marker
          id={markerId}
          viewBox="0 0 10 10"
          refX="9"
          refY="5"
          markerWidth="7"
          markerHeight="7"
          orient="auto-start-reverse"
        >
          <path className="edge-arrow" d="M 0 0 L 10 5 L 0 10 z" />
        </marker>
      </defs>
      {spec.edges.map((edge, index) => {
        const from = byId.get(edge.from)!;
        const to = byId.get(edge.to)!;
        const middleX = (from.x + to.x) / 2;
        const middleY = (from.y + to.y) / 2;
        return (
          <g key={`${edge.from}:${edge.to}:${index}`}>
            <line
              className="skeleton-edge"
              x1={from.x}
              y1={from.y}
              x2={to.x}
              y2={to.y}
              markerEnd={spec.directed ? `url(#${markerId})` : undefined}
            />
            {edge.label && (
              <text className="edge-label" x={middleX} y={middleY - 7}>
                {edge.label}
              </text>
            )}
          </g>
        );
      })}
      {vertices.map((vertex) => (
        <g key={vertex.id}>
          <circle className="skeleton-vertex" cx={vertex.x} cy={vertex.y} r={24} />
          <text
            className="skeleton-label"
            x={vertex.x}
            y={vertex.y}
            textAnchor="middle"
            dominantBaseline="central"
          >
            {vertex.label}
          </text>
        </g>
      ))}
    </SvgFrame>
  );
}

function endpointPosition(
  endpoint: StringEndpoint,
  rowIndexes: Map<string, number>,
): [number, number] {
  return [145 + endpoint.index * 54, 54 + (rowIndexes.get(endpoint.stringId) ?? 0) * 82];
}

export function StringDiagramRenderer({ spec }: { spec: StringDiagramSpec }) {
  const longest = Math.max(...spec.strings.map((row) => row.entries.length));
  const width = 180 + longest * 54;
  const height = 40 + spec.strings.length * 82;
  const rowIndexes = new Map(spec.strings.map((row, index) => [row.id, index]));
  const title = fallbackTitle(spec.title, "String diagram");
  return (
    <SvgFrame
      width={width}
      height={height}
      title={title}
      description={`${spec.strings.length} strings with ${spec.links.length} links.`}
      className="string-visualization"
    >
      {spec.links.map((link, index) => {
        const [fromX, fromY] = endpointPosition(link.from, rowIndexes);
        const [toX, toY] = endpointPosition(link.to, rowIndexes);
        const bend = Math.max(24, Math.abs(toY - fromY) * 0.35);
        return (
          <g key={`${link.from.stringId}:${link.from.index}:${index}`}>
            <path
              className="string-link"
              d={`M ${fromX} ${fromY} C ${fromX + bend} ${fromY}, ${
                toX - bend
              } ${toY}, ${toX} ${toY}`}
            />
            {link.label && (
              <text
                className="edge-label"
                x={(fromX + toX) / 2}
                y={(fromY + toY) / 2 - 8}
              >
                {link.label}
              </text>
            )}
          </g>
        );
      })}
      {spec.strings.flatMap((row, rowIndex) => {
        const y = 54 + rowIndex * 82;
        return [
          <text className="string-row-label" x={14} y={y} key={`${row.id}:label`}>
            {row.label}
          </text>,
          <line
            className="string-baseline"
            x1={128}
            y1={y}
            x2={145 + (row.entries.length - 1) * 54}
            y2={y}
            key={`${row.id}:baseline`}
          />,
          ...row.entries.map((entry, entryIndex) => {
            const x = 145 + entryIndex * 54;
            return (
              <g key={`${row.id}:${entryIndex}`}>
                <circle className="string-entry" cx={x} cy={y} r={18} />
                <text
                  className="string-entry-label"
                  x={x}
                  y={y}
                  textAnchor="middle"
                  dominantBaseline="central"
                >
                  {entry}
                </text>
              </g>
            );
          }),
        ];
      })}
    </SvgFrame>
  );
}
