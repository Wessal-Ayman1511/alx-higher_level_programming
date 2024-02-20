#!/usr/bin/python3
"""module to read file"""


def write_file(filename="", text=""):
    """function that write to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
