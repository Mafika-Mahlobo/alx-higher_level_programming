#!/usr/bin/python3

"""
Module containing a function to check if an object is a instance of a class
"""


def is_same_class(obj, a_class):

    """check if obj is an instace of a_class"""

    if type(obj) == a_class:
        return True
    return False
