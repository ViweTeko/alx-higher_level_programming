#!/usr/bin/python3

""" This module returns a dictionary description"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__
