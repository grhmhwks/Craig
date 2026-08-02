#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPOSITORY_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
cd "$REPOSITORY_ROOT"

PYTHON_BIN=${PYTHON_BIN:-python3}
command -v "$PYTHON_BIN" >/dev/null 2>&1 || {
  echo "error: Python 3.10 or newer is required." >&2
  exit 2
}
command -v node >/dev/null 2>&1 || {
  echo "error: Node.js is required to build the frontend." >&2
  exit 2
}
command -v npm >/dev/null 2>&1 || {
  echo "error: npm was not found." >&2
  exit 2
}

if [ ! -x .venv/bin/python ]; then
  "$PYTHON_BIN" -m venv .venv
fi

.venv/bin/python -m pip install -e '.[dev]'
(
  cd app/frontend
  npm ci
  npm run build
)
.venv/bin/python -m craig index
.venv/bin/python -m craig doctor
