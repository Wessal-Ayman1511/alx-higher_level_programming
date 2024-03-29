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
