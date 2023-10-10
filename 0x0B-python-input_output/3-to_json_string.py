#!/usr/bin/python3

"""
Module containing a function that return a 
JSON representation of an objects
"""
import json


def to_json_string(my_obj):

    """Returns the JSON representation of a string object."""

    return json.dumps(my_obj)
