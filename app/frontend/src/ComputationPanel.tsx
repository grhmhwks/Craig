import { useEffect, useMemo, useState } from "react";
import type { FormEvent } from "react";

import type { ComputationOperation } from "./types";

interface ComputationPanelProps {
  operations: ComputationOperation[];
  busy: boolean;
  onRun: (
    operation: ComputationOperation,
    parameters: Record<string, unknown>,
  ) => void;
}

function inputValue(value: unknown): string {
  if (Array.isArray(value)) return value.join(", ");
  return value === null || value === undefined ? "" : String(value);
}

function initialValues(operation: ComputationOperation | undefined) {
  return Object.fromEntries(
    (operation?.parameters ?? []).map((parameter) => [
      parameter.name,
      inputValue(parameter.default),
    ]),
  );
}

export function ComputationPanel({
  operations,
  busy,
  onRun,
}: ComputationPanelProps) {
  const [operationId, setOperationId] = useState(operations[0]?.id ?? "");
  const operation = useMemo(
    () => operations.find((item) => item.id === operationId) ?? operations[0],
    [operationId, operations],
  );
  const [values, setValues] = useState<Record<string, string>>(() =>
    initialValues(operation),
  );
  const [localError, setLocalError] = useState<string | null>(null);

  useEffect(() => {
    if (!operationId && operations[0]) setOperationId(operations[0].id);
  }, [operationId, operations]);

  useEffect(() => {
    setValues(initialValues(operation));
    setLocalError(null);
  }, [operation]);

  function submit(event: FormEvent) {
    event.preventDefault();
    if (!operation || busy) return;
    try {
      const parameters = Object.fromEntries(
        operation.parameters.map((parameter) => {
          const raw = values[parameter.name] ?? "";
          if (parameter.kind === "integer") {
            if (!/^-?\d+$/.test(raw.trim())) {
              throw new Error(`${parameter.label} must be an integer.`);
            }
            return [parameter.name, Number(raw)];
          }
          if (parameter.kind === "integer_array") {
            const entries = raw.trim()
              ? raw.split(",").map((entry) => {
                  if (!/^-?\d+$/.test(entry.trim())) {
                    throw new Error(
                      `${parameter.label} must be a comma-separated integer list.`,
                    );
                  }
                  return Number(entry.trim());
                })
              : [];
            if (
              parameter.max_items !== null &&
              entries.length > parameter.max_items
            ) {
              throw new Error(
                `${parameter.label} cannot contain more than ${parameter.max_items} entries.`,
              );
            }
            if (
              entries.some(
                (entry) =>
                  (parameter.minimum !== null && entry < parameter.minimum) ||
                  (parameter.maximum !== null && entry > parameter.maximum),
              )
            ) {
              throw new Error(
                `${parameter.label} contains an entry outside its allowed range.`,
              );
            }
            return [parameter.name, entries];
          }
          return [parameter.name, raw];
        }),
      );
      setLocalError(null);
      onRun(operation, parameters);
    } catch (reason) {
      setLocalError(reason instanceof Error ? reason.message : String(reason));
    }
  }

  if (!operation) return null;

  return (
    <form className="computation-panel" onSubmit={submit}>
      <div className="computation-heading">
        <div>
          <span>Isolated allowlist</span>
          <strong>Approved computation</strong>
        </div>
        <span className={`computation-class ${operation.classification}`}>
          {operation.classification.replaceAll("_", " ")}
        </span>
      </div>

      <label className="computation-operation">
        <span>Operation</span>
        <select
          value={operation.id}
          disabled={busy}
          onChange={(event) => setOperationId(event.target.value)}
        >
          {operations.map((item) => (
            <option value={item.id} key={item.id}>
              {item.title}
            </option>
          ))}
        </select>
      </label>
      <p className="computation-description">{operation.description}</p>

      <div className="computation-parameters">
        {operation.parameters.map((parameter) => (
          <label key={parameter.name}>
            <span>{parameter.label}</span>
            <input
              type={parameter.kind === "integer" ? "number" : "text"}
              value={values[parameter.name] ?? ""}
              min={
                parameter.kind === "integer"
                  ? (parameter.minimum ?? undefined)
                  : undefined
              }
              max={
                parameter.kind === "integer"
                  ? (parameter.maximum ?? undefined)
                  : undefined
              }
              minLength={
                parameter.kind === "string"
                  ? (parameter.minimum ?? undefined)
                  : undefined
              }
              maxLength={
                parameter.kind === "string"
                  ? (parameter.maximum ?? undefined)
                  : undefined
              }
              required={parameter.required}
              disabled={busy}
              onChange={(event) =>
                setValues((current) => ({
                  ...current,
                  [parameter.name]: event.target.value,
                }))
              }
            />
            <small>{parameter.description}</small>
          </label>
        ))}
      </div>

      <div className="computation-run-row">
        <small>
          {operation.limits.wall_time_seconds}s wall · {Math.round(
            operation.limits.memory_bytes / 1024 / 1024,
          )}
          MB memory · no child processes
        </small>
        <button type="submit" disabled={busy}>
          {busy ? "Worker active" : "Run approved job"}
        </button>
      </div>
      {localError && (
        <p className="computation-local-error" role="alert">
          {localError}
        </p>
      )}
    </form>
  );
}
