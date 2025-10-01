#!/usr/bin/env python3


import pickle


class CustumObject:
    """ Define a custom Python object """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Is student: {self.is_student}")   

    def serialize(self, filenale):
        