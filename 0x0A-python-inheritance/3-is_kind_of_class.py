#!/usr/bin/python3

"""
Module containing a function that checks if an object
is an instace of a class or parent class.
"""


def is_kind_of_class(obj, a_class):

    """
    checks if an obj is an instance of a_class or parent of a_class

    Args:
        obj: and object. can be any type
        a_class(class): this is a class

    Return: boolen value

    """

    if isinstance(obj, a_class):
        return True
    return False
