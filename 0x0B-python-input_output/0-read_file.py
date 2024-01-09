#!/usr/bin/python3

""" This module contains a function that opens and reads a file """


def read_file(filename=""):
    """ 
    Reads a textfile (UTF8) and prints to stdout
    Args:
        filename: name of file
    """
    with open(filename, "r", encoding="utf-8") as a:
        print(a.read(), end="")
