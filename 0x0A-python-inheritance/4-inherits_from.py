#!/usr/bin/python3
"""module for check if the object is exactly an instance of the class
"""


def inherits_from(obj, a_class):
    """def inherits_from(obj, a_class)"""
    return isinstance(obj, a_class) and type(obj) is not a_class
