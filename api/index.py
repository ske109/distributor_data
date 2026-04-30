from http.server import BaseHTTPRequestHandler
import requests
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ... (your existing login/fetch logic) ...
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Success!")
