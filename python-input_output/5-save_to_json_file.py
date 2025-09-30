#!/usr/bin/python3
"""
Module:
Countain a function that writes an Object
to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file """
    with open(filename, 'w', encoding='utf-8') as fichier:
        fichier.write(json.dumps(my_obj))
