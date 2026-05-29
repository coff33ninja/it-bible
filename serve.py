#!/usr/bin/env python3
"""Dev server with TTS proxy for The IT Bible frontend."""

import http.server
import json
import os
import sys
import socket
import urllib.parse
import asyncio

try:
    import edge_tts
    HAS_TTS = True
except ImportError:
    HAS_TTS = False

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


TTS_CACHE = {}
TTS_READY = False
TTS_ERROR = None

if not HAS_TTS:
    TTS_ERROR = "edge-tts not installed. Run: uv sync"


async def synthesize(text, voice):
    if not HAS_TTS:
        return b""
    key = f"{voice}:{text}"
    if key in TTS_CACHE:
        return TTS_CACHE[key]
    data = b""
    async for chunk in edge_tts.Communicate(text, voice).stream():
        if chunk["type"] == "audio":
            data += chunk["data"]
    TTS_CACHE[key] = data
    return data


async def warmup_tts():
    global TTS_READY, TTS_ERROR
    if not HAS_TTS:
        TTS_ERROR = "edge-tts not installed"
        return
    voices = ["en-US-ChristopherNeural", "en-US-MichelleNeural",
              "en-US-GuyNeural", "en-US-JennyNeural"]
    for v in voices:
        try:
            await synthesize("Preload.", v)
            print(f"  [TTS] Warmed: {v}")
        except Exception as e:
            print(f"  [TTS] Warm failed for {v}: {e}")
            TTS_ERROR = str(e)
    TTS_READY = True


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path == "/tts":
            params = urllib.parse.parse_qs(parsed.query)
            text = params.get("text", [""])[0]
            voice = params.get("voice", ["en-US-GuyNeural"])[0]
            if not text:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error":"missing text"}')
                return

            audio = asyncio.run(synthesize(text, voice))
            self.send_response(200)
            self.send_header("Content-Type", "audio/mpeg")
            self.send_header("Content-Length", str(len(audio)))
            self.send_header("Cache-Control", "public, max-age=86400")
            self.end_headers()
            self.wfile.write(audio)
            return

        if parsed.path == "/tts-voices":
            voices = asyncio.run(edge_tts.list_voices())
            us = [v for v in voices if "en-US" in v["Name"]]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps([{
                "name": v["ShortName"],
                "gender": v["Gender"],
                "friendly": v["FriendlyName"],
            } for v in us]).encode())
            return

        if parsed.path == "/tts-status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(json.dumps({"ready": TTS_READY, "error": TTS_ERROR}).encode())
            return

        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()


print("  >>  THE IT BIBLE  <<")
print("")
print(f"  Serving:  {DIR}")
print(f"  Local:    http://localhost:{PORT}")
print(f"  Network:  http://{self_ip()}:{PORT}")
print("")
print("  Warming TTS voices...")
if HAS_TTS:
    asyncio.run(warmup_tts())
    print("  TTS ready.")
else:
    print("  TTS unavailable (edge-tts not installed). Run: uv sync")
print("")
print(f"  TTS API:  http://localhost:{PORT}/tts?text=hello&voice=en-US-GuyNeural")
print("  Press Ctrl+C to stop")

try:
    server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    import webbrowser
    webbrowser.open(f"http://localhost:{PORT}")
    server.serve_forever()
except OSError:
    print(f"\n  [!] Port {PORT} is in use. Try: python serve.py 8080")
except KeyboardInterrupt:
    print("\n  Server stopped.")
    server.server_close()
