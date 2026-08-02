# CRAIG v1.0 installation and launch

CRAIG runs locally with Python 3.10 or newer, Node.js, npm, and SQLite FTS5.
The setup scripts create `.venv/`, install the Python application, build the
browser frontend, and generate `.craig/index.sqlite3`. They read `content/` but
never write beneath it.

## Windows

From Command Prompt or PowerShell in the repository root:

```text
scripts\setup.cmd
scripts\start.cmd
```

Open `http://127.0.0.1:8000`. The `.cmd` scripts deliberately call `npm.cmd`,
so they are not affected by PowerShell's `.ps1` execution policy.

To run the frontend development server instead, keep the Python backend running
and use a second terminal:

```text
cd app\frontend
npm.cmd run dev
```

The development frontend is normally at `http://127.0.0.1:5173`.

## macOS and Linux

From a POSIX shell in the repository root:

```text
sh scripts/setup.sh
sh scripts/start.sh
```

Open `http://127.0.0.1:8000`. Set `PYTHON_BIN` when the desired interpreter is
not named `python3`:

```text
PYTHON_BIN=python3.12 sh scripts/setup.sh
```

## Manual installation

The equivalent manual workflow is:

```text
python -m venv .venv
python -m pip install -e ".[dev]"
cd app/frontend
npm ci
npm run build
cd ../..
python -m craig index
python -m craig doctor
python -m craig serve
```

Activate the virtual environment or replace `python` with the environment's
interpreter as appropriate. An installed console entry point is also available:

```text
craig --version
craig doctor
craig serve
```

## Docker

Docker is optional. It is useful when installing Python and Node separately is
inconvenient:

```text
docker compose up --build
```

Open `http://127.0.0.1:8000`. The container:

- builds the frontend in a separate Node stage;
- installs only the Python runtime into the final image;
- runs as an unprivileged user with all Linux capabilities dropped;
- uses a read-only application filesystem and `no-new-privileges`;
- writes temporary worker files only under a bounded `/tmp` tmpfs;
- writes the generated search index to the `craig-data` volume at `/data`;
- keeps the copied mathematical corpus read-only at runtime.

Stop the service with `docker compose down`. The named index volume is retained.
Use `docker compose down --volumes` only when you intentionally want to remove
that generated index; it never removes repository files.

## Diagnostics and upgrades

`craig doctor` checks Python, SQLite FTS5, the corpus, generated index, frontend
build, Node availability, and secret-free provider status. `--json` returns a
machine-readable report. It performs no writes.

After pulling an update, rerun the platform setup script. `npm ci` follows the
locked dependency graph and `craig index` incrementally refreshes only changed
source hashes.
