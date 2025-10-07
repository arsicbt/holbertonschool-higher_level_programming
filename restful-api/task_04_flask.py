#!/usr/bin/python3


from flask import Flask
app = Flask(__name__)


# décorateur qui associe une URL à une fonction
@app.route('/')
def home():
    msg = "Welcome to the Flask API!"
    return msg

if __name__ == "__main__": 
    app.run()
