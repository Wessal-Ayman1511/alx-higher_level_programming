#!/usr/bin/python3
""" module to convert to string"""

import json


def save_to_json_file(my_obj, filename):
    """unction that writes an Object to a text file, using a JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
