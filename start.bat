@echo off
title The IT Bible Server
cd /d "%~dp0"
cls

echo.
echo   ^>^>^> THE IT BIBLE ^<^<^<
echo.
echo   Locating Python...

:: Check for py (Python launcher, always in PATH when Python is installed)
where py >nul 2>nul
if %errorlevel% equ 0 goto :run_py

:: Check for python via full path
if exist "C:\Python314\python.exe" set PYCMD=C:\Python314\python.exe & goto :run
if exist "C:\Python313\python.exe" set PYCMD=C:\Python313\python.exe & goto :run
if exist "C:\Python312\python.exe" set PYCMD=C:\Python312\python.exe & goto :run

echo   [!] Python not found.
echo.
echo   Options:
echo     npx http-server .   (if Node.js is installed)
echo     python serve.py     (if Python is in your PATH)
echo.
pause
exit /b

:run_py
echo   Found: py (Python Launcher)
echo.
echo   Server starting at http://localhost:3000
echo   Press Ctrl+C to stop
echo.
start /b "" cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:3000"
py serve.py
goto :end

:run
echo   Found: %PYCMD%
echo.
echo   Server starting at http://localhost:3000
echo   Press Ctrl+C to stop
echo.
start /b "" cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:3000"
%PYCMD% serve.py
goto :end

:end
echo.
echo   Server stopped.
pause
