#!/usr/bin/python3


""" Creates an object from json file """


def load_from_json_file(filename):
    """Creates an object from JSON file
    Args:
        filename - name of file
    """
    import json

    with open(filename, encoding="utf-8") as b:
        my_obj = json.loads(b.read())
    return my_obj
