#!/usr/bin/python3

"""
This module contains function that inserts a line of text
after each line containing a specific string (keyword)
"""


def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword

    Args:
        filenane: The file to read and write to
        search_string: The string to search
        new_string: The new string to add to the file
    """

    with open(filename, mode="r+", encoding="utf-8") as a:
        newln = ""
        for line in a:
            newln += line
            if search_string in line:
                newln += new_string
        a.seek(0)
        a.write(newln)
