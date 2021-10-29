import http.server
import socketserver
import os
PORT = 9000

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        possible_name = self.path.strip("/")+'.html'
        if self.path == '/':
            # default routing, instead of "index.html"
            self.path = '/index.html'
        elif os.path.isfile(possible_name):
            # extensionless page serving
            self.path = possible_name
        elif self.path == '/other':
            self.path = '/other.html'
        elif self.path == '/autre':
            self.path = '/autre.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)
Handler = MyRequestHandler
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
