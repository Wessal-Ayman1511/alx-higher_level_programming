#!/usr/bin/python3
"""module that inherite sort list"""


class MyList(list):
    """intiating class"""
    def print_sorted(self):
        """function that sort list"""
        print(sorted(self))
