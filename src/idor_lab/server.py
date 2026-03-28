from http.server import BaseHTTPRequestHandler, HTTPServer


HOST = "127.0.0.1"
PORT = 8000


class LabHandler(BaseHTTPRequestHandler):
    @route('/')
    def do_GET(self):
        """
        Suggested routes:
        - `/`
        - `/profile?user=guest`
        - `/fixed-profile?user=guest`

        Build the vulnerable route first, then the fixed route.
        """
        self.send_response(501)
        self.end_headers()
        self.wfile.write(b"TODO: implement routes")


def run():
    server = HTTPServer((HOST, PORT), LabHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    server.serve_forever()
