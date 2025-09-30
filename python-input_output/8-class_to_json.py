#!/usr/bin/python3
"""
Module:
Countain a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """ Function for the module """
    return obj.__dict__
