import { isValidElement } from "react";
import type { ReactElement } from "react";
import ReactMarkdown from "react-markdown";
import type { Components } from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkMath from "remark-math";

import { VisualizationBlock } from "./visualizations/VisualizationBlock";
import { languageFromClassName } from "./visualizations/schema";

const markdownComponents: Components = {
  code({ className, children, node: _node, ...properties }) {
    const language = languageFromClassName(className);
    if (language) {
      return (
        <VisualizationBlock
          language={language}
          source={String(children).replace(/\n$/, "")}
        />
      );
    }
    return (
      <code className={className} {...properties}>
        {children}
      </code>
    );
  },
  pre({ children, node: _node, ...properties }) {
    const child = isValidElement(children)
      ? (children as ReactElement<{ className?: string }>)
      : null;
    if (languageFromClassName(child?.props.className)) {
      return <>{children}</>;
    }
    return <pre {...properties}>{children}</pre>;
  },
};

export function MarkdownMessage({ children }: { children: string }) {
  return (
    <ReactMarkdown
      components={markdownComponents}
      rehypePlugins={[
        [
          rehypeKatex,
          {
            maxExpand: 1_000,
            strict: "warn",
            throwOnError: false,
            trust: false,
          },
        ],
      ]}
      remarkPlugins={[remarkMath]}
      skipHtml
    >
      {children}
    </ReactMarkdown>
  );
}
