#!/usr/bin/python3
"""module for getting attrib for object"""


def lookup(obj):
    """function that returns the list of available
     function that returns the list of available attributes
     and methods of an object

     Args:
     obj: input

     Return:
     list of object attrib
     """
    return dir(obj)
