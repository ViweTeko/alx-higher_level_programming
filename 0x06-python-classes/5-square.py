#!/usr/bin/python3
""" Creating square class """
class Square:
    """ Defining square class """
    def __init__(self, size=0):
        """ Initializing square class """
        self.__size = size

    @property
    def size(self):
        """ Getting size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting size of square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculating area of square """
        return (self.__size ** 2)

    def my_print(self):
        """ Printing the square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
