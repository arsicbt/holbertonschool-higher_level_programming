#!/usr/bin/python3
"""
Basic serialization module for Python dictionaries
Provides functionality to serialize to JSON and deserialize from JSON
"""


import json


def serialize_and_save_to_file(data, filename):
    """ Serialize a Python dictionary to a JSON file """

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        return True

    except TypeError as error:
        print(f"Serialization error: {error}")
        return False


def load_and_deserialize(filename):
    """ Deserialize a JSON file to recreate a Python dictionary """

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            object = json.load(f)
        return object

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None
