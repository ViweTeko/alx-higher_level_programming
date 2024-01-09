#!/usr/bin/python3

"""Adds all args to a Python list and saves to a file"""
import sys
import os
to_json = __import__("5-save_to_json_file").save_to_json_file
from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(a, filename):
    """Adds all args to Python list and saves to file
    Args:
        a - arguments
        filename - name of file
    """
    if (os.path.exists(filename)):
        stuff = from_json(filename)
    else:
        stuff = []
    stuff.extend(a)
    to_json(stuff, filename)
