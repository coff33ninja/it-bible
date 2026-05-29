@echo off
title The IT Bible - Server
cd /d "%~dp0"

:: ── 1. Install uv (if missing) ──────────────────────────────────────────────
where uv >nul 2>&1
if errorlevel 1 (
    echo [IT BIBLE] Installing uv...
    powershell -ExecutionPolicy ByPass -Command "& {irm https://astral.sh/uv/install.ps1 | iex}"
    if errorlevel 1 (
        echo [IT BIBLE] Failed to install uv. Install manually: https://astral.sh/uv
        pause
        exit /b 1
    )
)

:: ── 2. Locate uv executable ─────────────────────────────────────────────────
set UV_EXE=uv
where uv >nul 2>&1 || (
    if exist "%USERPROFILE%\.local\bin\uv.exe" set "UV_EXE=%USERPROFILE%\.local\bin\uv.exe"
    if exist "%USERPROFILE%\.cargo\bin\uv.exe" set "UV_EXE=%USERPROFILE%\.cargo\bin\uv.exe"
)
for /f "tokens=1-2" %%a in ('"%UV_EXE%" --version') do set UVVER=%%a %%b
echo [IT BIBLE] %UVVER%

:: ── 3. Ensure Python (uv-managed) ───────────────────────────────────────────
echo [IT BIBLE] Ensuring Python...
"%UV_EXE%" python install 3.11

:: ── 4. Sync dependencies & create .venv ─────────────────────────────────────
echo [IT BIBLE] Installing dependencies...
"%UV_EXE%" sync

:: ── 5. Launch server ────────────────────────────────────────────────────────
echo.
"%UV_EXE%" run serve.py

pause
