#!/usr/bin/python3
'''
Module that defines MyList class
'''


class MyList(list):
    """
    MyList class that inherits from list

    Public Methods:
        print_sorted(self): prints the list in ascending sorted order
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order

        The original list is not modified - only the printed output is sorted.
        Assumes all elements are integers.
        """
        print(sorted(self))
