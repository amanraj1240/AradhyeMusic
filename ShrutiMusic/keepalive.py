"""Tiny HTTP keepalive server for Render's free Web Service tier.

Render's free Web Service requires a process to bind to $PORT within 60s,
otherwise the service is marked as failed. Telegram bots don't naturally
serve HTTP, so this module spins up a minimal stdlib HTTP server in a
daemon thread that responds 200 OK on /, /health, and /healthz.

Pair this with an external pinger (e.g. UptimeRobot every 5 minutes) so
Render doesn't sleep the service after 15 minutes of inactivity.
"""

import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"AradhyeMusic bot is alive\n")

    def do_HEAD(self):  # noqa: N802
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):  # silence default access log
        return


def _run(port: int) -> None:
    server = ThreadingHTTPServer(("0.0.0.0", port), _Handler)
    server.serve_forever()


def start_keepalive_server() -> None:
    """Start the keepalive HTTP server in a background daemon thread.

    Reads PORT from env (Render sets this automatically). If PORT is not
    set (e.g. local dev or Background Worker mode), this is a no-op.
    """
    port_str = os.environ.get("PORT")
    if not port_str:
        return
    try:
        port = int(port_str)
    except ValueError:
        return
    thread = threading.Thread(target=_run, args=(port,), daemon=True, name="keepalive-http")
    thread.start()
