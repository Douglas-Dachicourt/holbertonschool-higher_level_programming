#!/usr/bin/python3
"""
This module import http.server and json to be able to run a basic server
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    class MyHandler : inherits methods from http.server module
    It is a class to launch a basic server

    Method:

    - do_GET: method who let the guest make requests to the local server

    Endpoints:

        - Home: "/" or "", prints out a welcoming message
        - Data: "/data", prints out the data available
        - Status: "/status", returns status OK
        - info: "/info", gives information about the server itself

        Status:

        - CODE 200: request has been successful
        - CODE 404: if endpoint is Not Found

    """

    def do_GET(self):
        """
        Handle GET requests to the server

        - Give an OK status and a welcoming message at initial endpoint
        - Give an OK status with some JSON data at data endpoint
        - Give an OK status with some JSON data at info endpoint
        - Give an Error 404 Not Found status if endpoint does not exist


        """

        if self.path == "/":
            self.send_response(200)  # response OK SUCCESS

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)  # response OK SUCCESS

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

            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"OK")
        else:
            self.send_error(404, "Endpoint not found")


def run():
    """
    Let the server run on port 8000
    """
    PORT = 8000

    httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
