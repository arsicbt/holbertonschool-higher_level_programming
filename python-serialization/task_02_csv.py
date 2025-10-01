#!/usr/bin/python3
"""
Module:
Countain a function that convert CSV to JSON
"""


import csv
import json


def convert_csv_to_json(filename):
    """ Convert CSV file to JSON """

    csvfile = open(filename, 'r')
    jsonfile = open(filename, 'w')

    try:
        reader = csv.DictReader(csvfile, filename)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write('\n')
        return True

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{filename}' not found")
        return False
