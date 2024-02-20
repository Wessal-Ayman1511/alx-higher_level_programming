#!/usr/bin/python3
"""module that check valdity"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    """Square module"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of Square"""
        return self.__size ** 2
