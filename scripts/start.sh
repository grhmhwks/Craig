#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPOSITORY_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
cd "$REPOSITORY_ROOT"

if [ ! -x .venv/bin/python ]; then
  echo "error: CRAIG is not installed. Run sh scripts/setup.sh first." >&2
  exit 2
fi

echo "CRAIG will be available at http://127.0.0.1:8000"
exec .venv/bin/python -m craig serve
