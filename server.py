from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import httpie
import os


# cheese = cow.Beavis()

# msg = cheese.milk('This is the message')

# print(msg)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # import pdb; pdb.set_trace()
        parsed_path = urlparse(self.path)
        print(parsed_path)
        parsed_qs = parse_qs(parsed_path.query)

        # set a status code
        # set any headers
        # set any body data on the response
        # end headers

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Hello World!</h1></body></html>')
            return

        elif parsed_path.path == '/cow':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            msg = parsed_qs['msg'][0]
            print(cow.Ghostbusters().milk(httpie.msg))
            self.wfile.write(cow.Ghostbusters().milk(msg).encode())
            # self.wfile.write(b'<html><body><h1>Cow!</h1></body></html>')
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/cow':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            msg = parse_qs['msg'][0]


def create_server():
    return HTTPServer(
        ('127.0.0.1', int(os.environ['PORT'])),
        SimpleHTTPRequestHandler
    )

def run_forever():
    server = create_server()

    try:
        server.serve_forever()
        print(f'Server running on {os.environ["PORT"]}')

    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
