#!/usr/bin/python3
""" Creating a class square """


class Square:
    """ Defining class square """
    def __init__(self, size=0):
        """ Initializing squre class
        Args: size=0: size of square """
        self.__size = size

    @property
    def size(self):
        """ Getting size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculating area of square """
        return (self.__size ** 2)
