#!/usr/bin/python3

""" This module continues from the previous file """
Rectangle = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class inherits from the base geometry class
    Attributes:
        __init__(self) - Initializes the object
        width - The width of the rectangle
        height - The height of the rectangle
    """

    def __init__(self, width, height):
        """Initializes the instance"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calculates the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Returns object in string format"""
        return "[{}] {}/{}".format(
                self.__class__.__name, self.__width, self.__height)
