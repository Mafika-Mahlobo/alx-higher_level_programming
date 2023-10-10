#!/usr/bin/python3

"""
Module containing a function that returns a list of availble
attribute or/and methods of  passed object
"""


def lookup(obj):

    """
    this function takes an object and return a list of attributes
    and/or methoda of the object
    """
    return dir(obj)
