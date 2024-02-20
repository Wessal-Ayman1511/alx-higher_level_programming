#!/usr/bin/python3
"""module for check if the object is exactly an instance of the class
"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance of,
    or if the object is an instance of a class"""
    return isinstance(obj, a_class)
