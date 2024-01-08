#!/usr/bin/python3

""" 
Creates a base geometry class
(Continues from the previous two files)
"""
class BaseGeometry:
    """ Creates a base geometry class
    Attributes:
        area(self) - area of base geometry
        integer_validator(self, name, vale) - validates value
        __init__(self) - initializer
        name - Name of geometry
        value - Value of geometry
    Raise:
        Exception
    """
    def area(self):
        """ Raises exception """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Validates values
        Raises:
            TypeError: value not int
            ValueError: value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
