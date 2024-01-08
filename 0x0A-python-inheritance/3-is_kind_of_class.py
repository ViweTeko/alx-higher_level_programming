#!/usr/bin/python3

""" This module checks if object passed is instance
of class inherited from specified class.
"""


def is_kind_of_class(obj, a_class):
    """ Checks if object is instance of class
    inherited from that class
    Args:
        obj: Object
        a_class: Specified class
    Return:
        True or False
    """
    return isinstance(obj, a_class)
