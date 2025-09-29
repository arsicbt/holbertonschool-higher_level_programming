#!/usr/bin/python3
import json
"""
Module --> Write a function that returns
the JSON representation of an object
"""


def to_json_string(my_obj):
    """ returns the JSON representation of an object """
    return json.dumps(my_obj)
