#!/usr/bin/python3
"""module"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """consytuctor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function"""
        if attrs = None:
            return self.__dict__
        dic = {}
        for key, value in sel.__dict__.items():
            if key in attrs:
                dict[key] = value
        return dic
