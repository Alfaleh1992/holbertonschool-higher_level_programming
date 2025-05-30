#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""

class MyList(list):
    """
    MyList class extends built-in list with additional sorted printing.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        Does not modify the original list.
        """
        print(sorted(self))

    def __str__(self):
        """
        Returns string representation of the list.
        """
        return super().__str__()
