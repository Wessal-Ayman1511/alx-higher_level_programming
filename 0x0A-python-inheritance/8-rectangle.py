#!/usr/bin/python3
"""module that check valdity"""


class BaseGeometry:
    """create class"""
    def area(self):
        """function that raise erreor"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that check validity"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """derived class"""
    def __init__(self, width, height):
        """constructor"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
