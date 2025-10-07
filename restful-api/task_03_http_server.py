#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MiniServer(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200, content_type="application/json"):
        """Envoie les en-têtes HTTP de réponse"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_json(self, data, status_code=200):
        """Utilitaire pour envoyer une réponse JSON"""
        self._set_headers(status_code, "application/json")
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        """Gère les requêtes GET selon le chemin"""
        
        # Root
        if self.path == '/':
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # /data endpoint
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(data)
            return

        # /status endpoint
        if self.path == '/status':
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")
            return

        # /info endpoint
        if self.path == '/info':
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json(info)
            return

        # Endpoint indéfini : 404
        error = {"error": "Endpoint not found"}
        self._send_json(error, 404)


def run(server_class=HTTPServer, handler_class=MiniServer, port=8000):
    """Démarre le serveur HTTP"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down.")
        httpd.server_close()


if __name__ == "__main__":
    run()
