#!/usr/bin/python3
""" Module --> Read a file """

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as fichier:
        print(fichier.read(), end="")
