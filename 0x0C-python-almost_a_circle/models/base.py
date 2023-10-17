#!/usr/bin/python3

"""A module containing a base class"""

import json


class Base:
    """Base class of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor to do initialization when an object is created"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.

        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
