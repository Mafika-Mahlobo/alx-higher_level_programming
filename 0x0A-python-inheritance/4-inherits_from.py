#!/usr/bin/python3

"""
Module containing a function to check is an object is an instance of
of a class that inherited from a specified class (passed)
"""


def inherits_from(obj, a_class):

    """checks if obj is an instance of a class that inherited from a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
