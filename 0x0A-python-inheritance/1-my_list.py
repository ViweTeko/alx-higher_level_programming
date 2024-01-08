#!/usr/bin/python3

"""
This module contains a class that inherits another class
along with a class list.
"""

class MyList(list):
    """This class inherits default list class
    Args:
        list: Superclass (Parent)
    Attributes:
        print_sorted - Prints a sorted list
    """
    def print_sorted(self):
        """ Prints sorted list """
        print(sorted(self))
