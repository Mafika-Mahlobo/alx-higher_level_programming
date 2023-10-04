#!/usr/bin/python3

"""
Module contains a funtion that prints a square with the character #
"""


def print_square(size):
    """
    Function that draws a square with # on the console.

    Args:
        size(int): size of the square

    Returns:
        No return value
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for n in range(size):
            print("#", end="")
        print()
