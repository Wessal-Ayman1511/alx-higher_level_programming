#!/usr/bin/python3
"""module"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """consytuctor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of obj"""
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
