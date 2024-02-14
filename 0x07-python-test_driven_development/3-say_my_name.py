#!/usr/bin/python3
"""Module for matrix_divided method."""


def say_my_name(first_name, last_name=""):
    """function that print name

    Args:
    first_name: input
    last_name: input

    Return:
    name of person
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
