#!/usr/bin/python3

"""A module containing a base class"""


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
