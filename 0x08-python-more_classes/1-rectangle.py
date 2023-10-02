#!/usr/bin/python3

"""
This module contain a class that defines a rectangle
"""


class Rectangle:

    """
    This class defines a rectangle
    """

    def __init__(self, width=0, height=0):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        self.__height = value
