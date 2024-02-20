#!/usr/bin/python3
"""module to read file"""


def write_file(filename="", text=""):
    """function that write to file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
