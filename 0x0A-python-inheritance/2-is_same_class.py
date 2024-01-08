#!/usr/bin/python3

""" Checks if its the same class """


def is_same_class(obj, a_class):
    """ Checks if object is the instance of given class
    Args:
        obj (any): Object
        a_class (type): class to match
    Returns:
        True or False
    """
    if type(obj) is a_class:
        return True
    return False
