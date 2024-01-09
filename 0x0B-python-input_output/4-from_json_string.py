#!/usr/bin/python3

"""This module returns Python data structure
represented by JSON string
"""


def from_json_string(my_str):
    """Returns object represented by JSON string
    Args:
        my_str - my string
    """
    import json
    return json.loads(my_str)
