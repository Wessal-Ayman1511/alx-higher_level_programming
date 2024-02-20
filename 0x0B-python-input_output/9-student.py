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
        return self.__dict__
