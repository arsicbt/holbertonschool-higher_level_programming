#!/usr/bin/python3


from flask import Flask
app = Flask(__name__)



def home():

    msg = "Welcome to the Flask API!"
    return msg

if __name__ == "__main__": 
    app.run()

