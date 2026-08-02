@echo off
setlocal
cd /d "%~dp0\.."

if not exist ".venv\Scripts\python.exe" (
  echo error: CRAIG is not installed. Run scripts\setup.cmd first.
  exit /b 2
)

echo CRAIG will be available at http://127.0.0.1:8000
".venv\Scripts\python.exe" -m craig serve
