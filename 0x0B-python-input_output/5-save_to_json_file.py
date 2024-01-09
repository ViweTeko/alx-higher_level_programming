#!/usr/bin/python3

"""This module writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """Writes an object to text file using JSON rep
    Args:
        my_obj - object
        filename - name of file
    """
    import json

    with open(filename, "w", encoding="utf-8") as a:
        json.dump(my_obj, a)
