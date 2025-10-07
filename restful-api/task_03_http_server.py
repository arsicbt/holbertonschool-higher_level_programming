#!/usr/bin/python3


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MiniServer(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200, content_type="application/json"):
        """Là c'est utilitaire pour envoyer les en têtes HTTP de réponse"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """Ici je gère les requêtes GET selon le chemin (self.path)"""
        # Root
        if self.path == '/' or self.path == '':
            self._set_headers(200, "text/plain")
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode('utf-8'))
            return

        # /data endpoint
        if self.path == '/data':
            self._set_headers(200, "application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return

        # /status endpoint
        if self.path == '/status':
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")
            return

        # /info endpoint
        if self.path == '/info':
            self._set_headers(200, "application/json")
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))
            return

        # endpoint indefini : 404
        self._set_headers(404, "application/json")
        error = {"error": "Endpoint not found", "path": self.path}
        self.wfile.write(json.dumps(error).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=MiniServer, port=8000):
    """Démarrer mon mini serveur HTTP"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port} …")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down.")
        httpd.server_close()


if __name__ == "__main__":
    run()
