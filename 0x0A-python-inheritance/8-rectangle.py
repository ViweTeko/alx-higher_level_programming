#!/usr/bin/python3

"""
This module writes a class Rectangle that inherits from
Base Geometry
"""

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class creates a rectangle inherited from BaseGeometry
    Attributes:
        __init__(self) - Initializer
        width - width of rectangle
        height - height of rectangle
    """
    def __init__(self, width, height):
        """ Initializes the instance"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
