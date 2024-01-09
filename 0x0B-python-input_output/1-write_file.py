#!/usr/bin/python3

""" This module contains a function that writes str to .txt file"""


def write_file(filename="", text=""):
    """ This function writes a string to a text file.
    Args:
        filename: name of file
        text: text to write
    Return:
        number of characters
    """
    with open(filename, "w", encoding="utf-8") as a:
        count = a.write(text)
    return count
