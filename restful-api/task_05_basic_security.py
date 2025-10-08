#!/usr/bin/python3
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()  # initialise l’authentification basique


# User database, hashed passwords
# stocke jamais les mots de passe en clair !
users = {
    "admin": generate_password_hash("admin123"),
    "user1": generate_password_hash("password1"),
    "user2": generate_password_hash("password2")
}


@auth.verify_password
def verify_password(username, password):
    """Vérifie que l’utilisateur existe et que le mot de passe est correct"""
    if username in users and
    check_password_hash(users.get(username), password):
        return username  # OUI
    return None  # NON


@auth.error_handler
def unauthorized():
    """Gestion personnalisée des erreurs pour accès non autorisé"""
    # Retourne toujours 401 si pas authentifié
    return jsonify({"error": "Unauthorized access"}), 401


@app.route('/')
def public():
    """Route publique - accessible sans authentification"""
    return jsonify({"message": "This is a public endpoint"})


@app.route('/protected')
@auth.login_required
def protected():
    """Route protégée - nécessite authentification Basic Auth"""
    return jsonify({
        "message": f"Hello {auth.current_user()}!",
        "info": "This is a protected endpoint"
    })


@app.route('/admin')
@auth.login_required
def admin():
    """Route admin - accessible uniquement pour les boss"""
    if auth.current_user() == "admin":
        return jsonify({
            "message": "Welcome Admin!",
            "access": "full"
        })
    return jsonify({"error": "Admin access required"}), 403


if __name__ == '__main__':
    print("\nTest credentials:")
    print("  Username: admin, Password: admin123")
    print("  Username: user1, Password: password1")
    print("  Username: user2, Password: password2")
    print("\nEndpoints:")
    print("  / - Public (no auth)")
    print("  /protected - Requires authentication")
    print("  /admin - Requires admin user\n")
