#!/usr/bin/python3

""" This module writes a Student class which defines a student """


class Student:
    """This class creates a Student class
    Attributes:
        first_name - first name
        last_name - surname
        age - age
        __init__(self, first_name, last_name, age)
        to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """Initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary rep of Student instance
        Return:
            Student object
        """
        return self.__dict__
