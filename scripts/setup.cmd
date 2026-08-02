@echo off
setlocal
cd /d "%~dp0\.."

where python >nul 2>nul || (
  echo error: Python 3.10 or newer is required.
  exit /b 2
)
where node >nul 2>nul || (
  echo error: Node.js is required to build the frontend.
  exit /b 2
)
where npm.cmd >nul 2>nul || (
  echo error: npm.cmd was not found.
  exit /b 2
)

if not exist ".venv\Scripts\python.exe" (
  python -m venv .venv || exit /b 2
)

".venv\Scripts\python.exe" -m pip install -e ".[dev]" || exit /b 2
pushd app\frontend
call npm.cmd ci || (popd & exit /b 2)
call npm.cmd run build || (popd & exit /b 2)
popd
".venv\Scripts\python.exe" -m craig index || exit /b 2
".venv\Scripts\python.exe" -m craig doctor
exit /b %errorlevel%
