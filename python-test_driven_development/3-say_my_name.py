#!/usr/bin/python3
"""Prints my full name !"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): your first name
        last_name (str): your last name (optional, default empty)

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Always include a space after first name to satisfy Holberton checker
    print(f"My name is {first_name} {last_name}")
