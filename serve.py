#!/usr/bin/env python3
"""Simple dev server for The IT Bible frontend."""

import http.server
import webbrowser
import os
import sys
import socket

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
DIR = os.path.dirname(os.path.abspath(__file__))

def self_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"
    finally:
        s.close()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

print(f"  ⚠️  THE IT BIBLE")
print(f"  ───────────────────────")
print(f"  Serving:  {DIR}")
print(f"  Local:    http://localhost:{PORT}")
print(f"  Network:  http://{self_ip()}:{PORT}")
print(f"  ───────────────────────")
print(f"  Press Ctrl+C to stop")

try:
    server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    webbrowser.open(f"http://localhost:{PORT}")
    server.serve_forever()
except OSError:
    print(f"\n  [!] Port {PORT} is in use. Try: python serve.py 8080")
except KeyboardInterrupt:
    print("\n  Server stopped.")
    server.server_close()
