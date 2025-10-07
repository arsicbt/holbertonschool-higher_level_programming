#!/usr/bin/python3


from flask import Flask, jsonify, request, abort
app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# décorateur qui associe une URL à une fonction
@app.route('/')
def home():
    msg = "Welcome to the Flask API!"
    return msg


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def show_user(username):

    u = users.get(username)
    if not u:
        abort(404, description="User not found")
    return jsonify(u)

@app.route('/add_user', methods=['POST'])
def add_user():

    new_user_data = request.get_json()

    if "username" not in new_user_data or not new_user_data:
        abort(400, description="Username is required")

    username = new_user_data['username']
    if username in users:
        abort(400, description="Username already exists")
    
    users[username] = {
        "username": username,
        "name": new_user_data.get("name", ""),
        "age": new_user_data.get("age", 0),
        "city": new_user_data.get("city", "")
    }
    
    return jsonify({"message": "User added"}), 201

if __name__ == "__main__": 
    app.run()
