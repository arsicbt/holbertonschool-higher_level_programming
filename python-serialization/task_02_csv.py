#!/usr/bin/python3
"""
Module:
Countain a function that convert CSV to JSON
"""


import csv
import json


def convert_csv_to_json(filename):
    """ Convert CSV file to JSON """

    if filename.endswith('.csv'):
        json_filename = filename.replace('.csv', '.json')
    else:
        json_filename = filename + '.json'

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            
            with open(json_filename, 'w') as jsonfile:
                for row in reader:
                    json.dump(row, jsonfile)
                    jsonfile.write('\n')
        
        return True

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return False
