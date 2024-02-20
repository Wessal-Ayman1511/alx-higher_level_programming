#!/usr/bin/python3
"""module that return attributes of object"""


def class_to_json(obj):
    """funtion return attributes"""
    return obj.__dict__
