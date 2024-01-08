#!/usr/bin/python3

""" This continues from the previous file """


class BaseGeometry:
    """ This class creates a base geometry class.
    Attributes:
        area(self) - Area of base gemometry
    Raise:
        Exception - A general exception
    """
    def area(self):
        """ Raises an exception if not implemented """
        raise Exception("area() is not implemented")
