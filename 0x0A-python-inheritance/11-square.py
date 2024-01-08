#!/usr/bin/python3

""" Continues from previous file """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class creates a square by inheriting
    class Rectangle

    Attributes:
        __init__(self): Initializes the object
        size: Size of the square
    """
    def __init__(self, size):
        """This initializes the instance with the number of
        arguments in the base class Rectangle

        size: Size of the square
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """ Returns the string format of object to overwrite base class
        of str
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                self.__size, self.__size)
