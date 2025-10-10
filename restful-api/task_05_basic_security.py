#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, 
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-this-in-production'

# Extensions nécessaires
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# DB avec 2 roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Gerer les erreurs pour JWT - Tout retourne : 401
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    """Verify username and password"""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@auth.error_handler
def unauthorized():
    """Custom error handler for basic auth"""
    return jsonify({"error": "Unauthorized"}), 401

# Routes
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected route with Basic Authentication"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint - returns JWT token"""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    # Verifie les informations d'identifications
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Creer un token d'acces pour le role opportun
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    
    return jsonify({"access_token": access_token}), 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Protected route with JWT Authentication"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only route - requires JWT with admin role"""
    current_user = get_jwt_identity()
    claims = get_jwt()
    
    # Est ce que l'utilisateur à la role d'admin ?
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403 # NON
    
    return "Admin Access: Granted" # OUI

if __name__ == '__main__':
    app.run(debug=True, port=5000)