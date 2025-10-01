#!/usr/bin/python3
"""
Module:
Countain a function that convert CSV to JSON
"""


import csv
import json


def convert_csv_to_json(filename):
    """ Convert CSV file to JSON """

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        
        return True

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return False
