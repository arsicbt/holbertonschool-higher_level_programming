#!/usr/bin/python3
""" Module --> Write a sentence in a file """


def write_file(filename="", text=""):
    """ Write in a file """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
