#!/usr/bin/env python3
"""
Module:
Countain 2 functions that serialize and deserialize
Python dictionary and XML file
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serialize dictionary to XML file """

    root = ET.Element('data')

    with open(filename, 'r', encoding='utf-8') as f:
        # Iterate through the dictionary items
        for k, v in dictionary.items():
            # Add them as child elements to the root
            child = ET.SubElement(root, k)
            # Handle types conversions
            child.text = str(v)

        tree = ET.ElementTree(root)
        # Write the XML tree to the provided filename
        tree.write(filename, encoding="utf-8")

    return tree


def deserialize_from_xml(filename):
    """ Deserialize XML content to Python dictionary """

    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    # Navigate through the XML elements
    for child in root:
        # Reconstruct the dictionary
        dictionary[child.tag] = child.text

    return dictionary
