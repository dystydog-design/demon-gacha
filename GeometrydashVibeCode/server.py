
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.request

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/demons"):
            url = "https://api.aredl.net/v2/api/aredl/levels"

            try:
                request = urllib.request.Request(
                    url,
                    headers={
                        "User-Agent": "Mozilla/5.0",
                        "Accept": "application/json"
                    }
                )

                with urllib.request.urlopen(request) as response:
                    data = response.read()

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(data)

            except Exception as error:
                print("AREDL error:", error)
                self.send_error(502, str(error))

        else:
            super().do_GET()

server = HTTPServer(("localhost", 8000), Handler)
print("Server running at http://localhost:8000")
server.serve_forever()
