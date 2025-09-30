#!/usr/bin/python3
"""
Module:
Countain a class Student  that defines a student by:
(based on 10-student.py)
"""


class Student:
    """ Create a student pattern """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)

        return result

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
