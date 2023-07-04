#!/usr/bin/python3
"""
defines a function that add two numbers.

if input are not integers or floats, it raises a type  error.
"""
def add_integer(a, b=98):
    """Args:
          a (int): first number
          b (int): second"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
