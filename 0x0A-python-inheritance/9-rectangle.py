#!/usr/bin/python3
"""module that check valdity"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """derived class"""
    def __init__(self, width, height):
        """constructor"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area implemented"""
        return self.__width * self.__height

    def __str__(self):
        """str function"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
