#!/usr/bin/python3
'''Module for Base class.'''

import json


class Base:
    """ class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        ''' constructor '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ to json str """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            # str_data = json.dumps(list_dictionaries)
            # return str_data
            return json.dumps(list_dictionaries)
