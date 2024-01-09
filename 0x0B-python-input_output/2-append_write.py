#!/usr/bin/python3

""" This modules contains a function that appends to a file """


def append_write(filename="", text=""):
    """ This function appends written text to text file
    Args:
        filename: name of file
        text: text to append
    Return:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as a:
        count = a.write(text)
    return count
