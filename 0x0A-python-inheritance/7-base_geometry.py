#!/usr/bin/python3
"""module that check valdity"""


class BaseGeometry:
    """create class"""
    def area(self):
        """function that raise erreor"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that check validity"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
