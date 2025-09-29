#!/usr/bin/python3
"""
Module --> Countain a function that appends
a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
