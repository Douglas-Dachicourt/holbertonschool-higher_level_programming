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
            self.send_response(200)  # HTTP 200 OK SUCCESS

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")  # response body
        elif self.path == "/data":
            self.send_response(200)  # HTTP 200 OK SUCCESS

            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))  # response body
        elif self.path == "/info":
            self.send_response(200)  # HTTP 200 OK SUCCESS

            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))  # response body
        elif self.path == "/status":
            self.send_response(200)  # HTTP 200 OK SUCCESS

            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"OK")  # response body
        else:
            self.send_error(404, "Endpoint not found")  # HTTP 404 Not Found


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """
    Function run

    Run the server with the specified server class, handler class, and port

    Parameters:

    - server_class: we use HTTP server
    - handler_server: the request handler to use
    - port: we work on local port 8000

    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server launched on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()  # run the server if it is exectued through the script
