#!/usr/bin/python3
"""module that check valdity"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    def __init__(self, size):
        """constructor"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return super().__str__()
