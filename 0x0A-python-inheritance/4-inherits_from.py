#!/usr/bin/python3

""" This module checks for inheritance """


def inherits_from(obj, a_class):
    """ Checks for inheritance of an object
    Args:
        obj: Object
        a_class: Class
    Return:
        True or Flase
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
