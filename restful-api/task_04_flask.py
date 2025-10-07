#!/usr/bin/python3


from flask import Flask, jsonify, request
app = Flask(__name__)

users = [
    {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}
]

# décorateur qui associe une URL à une fonction
@app.route('/')
def home():
    msg = "Welcome to the Flask API!"
    return msg

@app.route('/data')
def data():
    user_id = [i['username'] for i in users]
    extract_id = jsonify(user_id)
    return extract_id

@app.route('/status')
def status():
    return abort(200, description="OK")

@app.route('/users/<username>')
def show_user(username):
    response = "User profil:"
    return response, username

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user_data = request.get_json()

    new_user = {
        "username": new_user_data.get('username'),
        "name": new_user_data.get('name')
    }

    users.append(new_user)
    return jsonify({201, "New user created!"})

if __name__ == "__main__": 
    app.run()
