import { useId } from "react";
import type { ReactNode } from "react";

interface SvgFrameProps {
  width: number;
  height: number;
  title: string;
  description: string;
  className?: string;
  children: ReactNode;
}

export function SvgFrame({
  width,
  height,
  title,
  description,
  className = "",
  children,
}: SvgFrameProps) {
  const identifier = useId().replaceAll(":", "");
  const titleId = `visualization-title-${identifier}`;
  const descriptionId = `visualization-description-${identifier}`;

  return (
    <figure className={`math-visualization ${className}`.trim()}>
      <div className="visualization-scroll">
        <svg
          viewBox={`0 0 ${width} ${height}`}
          width={width}
          height={height}
          role="img"
          aria-labelledby={`${titleId} ${descriptionId}`}
          preserveAspectRatio="xMidYMid meet"
        >
          <title id={titleId}>{title}</title>
          <desc id={descriptionId}>{description}</desc>
          {children}
        </svg>
      </div>
      <figcaption>{title}</figcaption>
    </figure>
  );
}
