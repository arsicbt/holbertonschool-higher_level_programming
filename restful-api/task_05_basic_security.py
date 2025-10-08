#!/usr/bin/python3
from flask import Flask, jsonify
from werkzeug.security import generate_password_hash

app = Flask(__name__)


# User database, hashed passwords
users = {
    "admin": generate_password_hash("admin123"),
    "user1": generate_password_hash("password1"),
    "user2": generate_password_hash("password2")
}

# protect rout
@auth.login_required