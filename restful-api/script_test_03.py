#!/usr/bin/python3

def test():

    import requests

    base_url = "http://localhost:8000"

    for path in ["/", "/data", "/status", "/unknown"]:
        response = requests.get(base_url + path)
        print(f"GET {path} - {response.status_code}")
        print(response.text)
