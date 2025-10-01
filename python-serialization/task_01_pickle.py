#!/usr/bin/env python3
"""
Module:
Serialize and deserialize
custom Python objects
"""


import pickle
import os


class CustomObject:
    """ Define a custom Python object """

    def __init__(self, name, age, is_student):
        """ Define attributs """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ Display attributs """
        print(f"Name: {self.name}\nAge:
        {self.age}\nIs student: {self.is_student}")

    def serialize(self, filename):
        """ Serialize the custom onject to a JSON file """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True

        except (TypeError) as error:
            raise TypeError(f"Serialization error {error}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """ Deserialize the custom object in the the JSON file """

        file_size = os.path.getsize(filename)

        if file_size == 0:
            print(f"'{filename}' is empty")
            return None

        try:
            with open(filename, 'rb') as f:
                object = pickle.load(f)
            return object

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{filename}' not found")
            return None
