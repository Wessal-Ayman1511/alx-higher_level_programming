#!/usr/bin/python3
"""module for check if the object is exactly an instance of the class
"""


def is_same_class(obj, a_class):
    """function that check if obj ininstance or not

    Arg:
        obj: input
        a_class: input

    Return:
        true or false
    """
    return type(obj) is a_class
