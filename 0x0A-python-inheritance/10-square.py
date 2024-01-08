#!/usr/bin/python3

""" This module inherits from the rectangle class """

Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """ This class inherits from Rectangle class
    Attributes:
        __init__(self): Initializer
        size: square size
    """
    def __init__(self, size):
        """This initializes the instance

        size: Square size
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
