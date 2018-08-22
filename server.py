from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import os
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """ gets the parsed url request"""
        parsed_path = urlparse(self.path)
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

            try:
                cow_image = cow.Stegosaurus()
                msg = cow_image.milk(parsed_qs['msg'][0])
                self.send_response(200)
                # self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(msg.encode())
                return

            except KeyError:
                different_cow = cow.BongCow()
                msg = different_cow.milk("400")
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(msg.encode())
        else:
            cow_ghost = cow.Ghostbusters()
            msg = cow_ghost.milk("404")
            self.send_response(404)
            self.end_headers()
            self.wfile.write(msg.encode())

    def do_POST(self):
        """ sends the parsed url request"""
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            try:
                cow_image = cow.Beavis()
                msg_post = cow_image.milk(parsed_qs['msg'][0])
                json_image = json.dumps({'Content': msg_post})
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                print(json_image)
                self.wfile.write(json_image.encode())
                return
            except KeyError:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                different_cow_image = cow.BongCow()
                msg = different_cow_image.milk("400")
                self.wfile.write(msg.encode())
        else:
            self.send_response(404)
            self.end_headers()
            bad_cow = cow.DragonAndCow()
            msg = bad_cow.milk("404")
            self.wfile.write(msg.encode())


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
