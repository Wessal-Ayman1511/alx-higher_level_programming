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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json str """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            str_data = json.dumps(list_dictionaries)
            return str_data

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            dic_list = []
        else:
            dic_list = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dic_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy
