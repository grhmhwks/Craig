import {
  DiagramRenderer,
  DyckPathRenderer,
  FactorizationRenderer,
  ReadingWordRenderer,
  SkeletonRenderer,
  StringDiagramRenderer,
  TableauRenderer,
} from "./renderers";
import { parseVisualizationBlock } from "./schema";
import type { VisualizationSpec } from "./schema";

interface VisualizationBlockProps {
  language: string;
  source: string;
}

function Renderer({ spec }: { spec: VisualizationSpec }) {
  switch (spec.kind) {
    case "tableau":
      return <TableauRenderer spec={spec} />;
    case "diagram":
      return <DiagramRenderer spec={spec} />;
    case "dyck-path":
      return <DyckPathRenderer spec={spec} />;
    case "reading-word":
      return <ReadingWordRenderer spec={spec} />;
    case "factorization":
      return <FactorizationRenderer spec={spec} />;
    case "skeleton":
      return <SkeletonRenderer spec={spec} />;
    case "string-diagram":
      return <StringDiagramRenderer spec={spec} />;
  }
}

export function VisualizationBlock({
  language,
  source,
}: VisualizationBlockProps) {
  const parsed = parseVisualizationBlock(language, source);
  if (!parsed.ok) {
    return (
      <figure className="visualization-fallback" role="group">
        <figcaption>
          <strong>Visualization unavailable</strong>
          <span>{parsed.error}</span>
        </figcaption>
        <pre>{source}</pre>
      </figure>
    );
  }

  return (
    <div className="visualization-block" data-visualization={parsed.spec.kind}>
      <Renderer spec={parsed.spec} />
      <details className="visualization-specification">
        <summary>Inspect trusted specification</summary>
        <pre>{source.trim()}</pre>
      </details>
    </div>
  );
}
