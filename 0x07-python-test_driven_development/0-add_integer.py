#!/usr/bin/python3
"""
Module with a single function to claculate the total of two integers.
"""

def add_integer(a, b=98):
    """Function that add two intgers and return the sum.

    Args:
        a(int): first number
        b(int): second number"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
