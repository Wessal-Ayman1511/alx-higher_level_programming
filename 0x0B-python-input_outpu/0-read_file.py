#!/usr/bin/python3
"""module to read file"""


def read_file(filename=""):
    """function that reas from file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
