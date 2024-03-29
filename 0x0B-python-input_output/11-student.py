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
        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic

    def reload_from_json(self, json):
        """function"""
        for key, value in json.items():
            if key in self.__dict__:
                setattr(self, key, value)
