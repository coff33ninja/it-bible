THE IT BIBLE — SERVER OPTIONS

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
  1. Create a new .md file (e.g. 46-new-book.md)
  2. Run: powershell -File generate-index.ps1
  3. Refresh the browser
