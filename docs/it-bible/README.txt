THE IT BIBLE — SERVER OPTIONS

All files are in the `docs/it-bible/` directory.
Run the server from there.

Option 1 — Python (built-in, no install needed):
  start.bat           (double-click me!)
  py serve.py         (default port 3000)
  py serve.py 8080    (custom port)

Option 2 — npx (requires Node.js):
  npx http-server . -p 3000 -c-1
  npx serve .

Option 3 — PowerShell one-liner:
  Start-Process 'http://localhost:3000'; py serve.py

Open http://localhost:3000 in your browser.
Press Ctrl+C to stop the server.

To add new warnings:
  1. Create a new subfolder under docs/it-bible/ (e.g. 41-new-book/)
  2. Place a README.md inside with the warning content
  3. Run: powershell -File generate-index.ps1
  4. Refresh the browser

Each book lives in its own subfolder as README.md
for clean GitHub rendering.
