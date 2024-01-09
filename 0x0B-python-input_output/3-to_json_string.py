#!/usr/bin/python3

""" This module returns the JSON representation of object """
import json


def to_json_string(my_obj):
    """ Returns JSON representative of object
    Args:
        my_obj - object
    Return:
        JSON object
    """
    return json.dumps(my_obj)
