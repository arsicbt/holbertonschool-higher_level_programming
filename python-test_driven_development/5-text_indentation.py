#!/usr/bin/python3
"""
Module that contains the text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . ? :

    Args:
        text: A string to be formatted and printed

    Raises:
        TypeError: If text is not a string
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters that trigger indentation
    special_chars = ['.', '?', ':']

    # Process the text character by character
    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end='')

        # If current character is a special character
        if text[i] in special_chars:
            # Print two new lines
            print('\n')

            # Skip any spaces that come after the special character
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            # Continue the loop without incrementing i again
            continue
        i += 1
