#!/usr/bin/env python3
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def pretty_print(title, response):
    print(f"\n=== {title} ===")
    print("Status code:", response.status_code)
    try:
        print(json.dumps(response.json(), indent=4))
    except Exception:
        print(response.text)

def test_home():
    r = requests.get(f"{BASE_URL}/")
    pretty_print("HOME /", r)

def test_data():
    r = requests.get(f"{BASE_URL}/data")
    pretty_print("GET /data", r)

def test_get_user(username):
    r = requests.get(f"{BASE_URL}/users/{username}")
    pretty_print(f"GET /users/{username}", r)

def test_add_user():
    new_user = {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "Paris"
    }
    r = requests.post(f"{BASE_URL}/add_user", json=new_user)
    pretty_print("POST /add_user", r)

if __name__ == "__main__":
    print("🚀 Tests du serveur Flask\n")

    test_home()                # Test accueil
    test_data()                # Test liste d’utilisateurs
    test_get_user("jane")      # Test profil existant
    test_get_user("bob")       # Test profil inexistant (devrait 404)
    test_add_user()            # Test ajout d’un nouvel utilisateur
    test_data()                # Vérifier la liste après ajout
