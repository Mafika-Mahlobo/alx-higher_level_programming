#!/usr/bin/python3

"""
Module containing a function that object
represented by a JSON str.
"""
import json


def from_json_string(my_str):

    """Returns the Python object representation of a JSON string."""

    return json.loads(my_str)
