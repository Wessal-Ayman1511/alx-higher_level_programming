#!/usr/bin/python3
""" module to add two integers """


def add_integer(a, b=98):
    """adds two integers

    Args:
    a: first int
    b: second int

    Raises:
    TypeError if a, b is not int or float

    Return:
    the addition of the two numbers
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
