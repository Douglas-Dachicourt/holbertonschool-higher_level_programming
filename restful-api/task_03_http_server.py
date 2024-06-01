#!/usr/bin/python3
"""import hhtp.server and json module"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyHandler(BaseHTTPRequestHandler):
    """
    class MyHandler : inherits methods from http.server module
    It is a class to launch a basic server

    Method (main):

    -do_GET: method who let the guest make requests to the local server

    => To reach different endpoints : /info, /data
    => Response status : 200 if reach success, 404 if Not Found


    """

    def do_GET(self):

        if self.path == "" or self.path == "/":
            self.send_response(200)

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API")

        elif self.path == "/data":
            self.send_response(200)

            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        else:
            self.send_response(404)

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Endpoint not found")


PORT = 8000
httpd = HTTPServer(('localhost', PORT), MyHandler)
httpd.serve_forever()
