
#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', "*")
        self.send_header('Access-Control-Allow-Credentials',  'true')
        self.send_header('Access-Control-Allow-Methods',  'GET, POST, PUT')
        self.send_header('Access-Control-Allow-Headers',  'application/json')
        self.send_header('Origin',  'http://127.0.0.1')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8888)