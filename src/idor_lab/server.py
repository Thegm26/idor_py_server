from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


HOST = "127.0.0.1"
PORT = 8000


class LabHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        - `/`
        - `/profile?user=guest`

        Build the vulnerable route first, then the fixed route.
        """
        parsed_path = urlparse(self.path)
        match parsed_path.path:
            case "/":
                self.send_response(501)
                self.end_headers()
                self.wfile.write(b"Provide a valid endpoint")
            case "/profile":
                parsed_queries = (parse_qs(parsed_path.query))
                if 'user' in parsed_queries:
                    self.send_response(200)
                    self.end_headers()
                    text = f"Welcome {parsed_queries['user'][0]}\n"
                    bytes_text = text.encode()
                    self.wfile.write(bytes_text)
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"Provide User\n")
            case _:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Error - Path does not exist \n")


def run():
    server = HTTPServer((HOST, PORT), LabHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    server.serve_forever()
