import http.server


class SputHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_PUT(self):
        print
        self.headers
        length = int(self.headers["Content-Length"])
        path = self.translate_path(self.path)
        with open(path, "wb") as dst:
            dst.write(self.rfile.read(length))


if __name__ == '__main__':
    http.server.test(HandlerClass=SputHTTPRequestHandler)

