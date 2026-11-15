import getpass
import os
import socket
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_NAME = os.environ.get("APP_NAME", "unknown")
APP_VERSION = os.environ.get("APP_VERSION", "unknown")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        text = (
            f"App name   : {APP_NAME}\n"
            f"Version    : {APP_VERSION}\n"
            f"Hostname   : {socket.gethostname()}\n"
            f"Run as user: {getpass.getuser()}\n"
            f"Port       : {PORT}\n"
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode())


if __name__ == "__main__":
    print(f"Starting {APP_NAME} v{APP_VERSION} on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
