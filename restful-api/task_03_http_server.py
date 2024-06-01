#!/usr/bin/python3
"""
This module contain a class SimpleHTTPRequestHandler to let a basic
python server run
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    The SimpleHTTPRequestHandler inherits methods from http.server module

    Method:

    - do_GET: method who let the guest make requests to the local server


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


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """
    Function run

    Run the server with the specified server class, handler class, and port

    """
    server_address = ("localhost", port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
