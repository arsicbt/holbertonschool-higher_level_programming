#!/usr/bin/python3
"""
Module that contains the say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name: A string representing the first name
        last_name: A string representing the last name (default: "")

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print(f"My name is {first_name} {last_name}")
