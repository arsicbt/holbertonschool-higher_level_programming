#!/usr/bin/python3
"""
Module:
Countain a function that creates an Object
from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """ Creates an object from JSON file """
    with open(filename, 'r', encoding='utf-8') as fichier:
        return json.load(fichier)
