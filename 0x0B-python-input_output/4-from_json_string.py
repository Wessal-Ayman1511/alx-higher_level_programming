#!/usr/bin/python3
""" module to convert to string"""

import json


def from_json_string(my_str):
    """function that convert to DS"""
    return json.loads(my_str)
