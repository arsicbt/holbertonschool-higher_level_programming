#!/usr/bin/python3


from flask import Flask
app = Flask(__name__)



def home():

    msg = "Welcome to the Flask API!"
    return msg

