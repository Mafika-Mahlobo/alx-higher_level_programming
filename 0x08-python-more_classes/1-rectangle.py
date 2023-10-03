#!/usr/bin/python3

"""
This module contain a class that defines a rectangle
"""


class Rectangle:

    """
    This class defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes an instance of theia class.

        Args:
            width(int): width of a rectangle
            height(int): height of a rectangle

        Returns:
            self.__width(int): width of a rectangle instance
            self.__height(int): height of a rectangle instance
        """

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

    @property
    def width(self):

        """ Returns width ofa rectangle instace"""
        return self.__width

    @width.setter
    def width(self, value):

        """Sets the width of a rectnge"""
        self.__width = value

    @property
    def height(self):

        """Returns the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectagnle"""
        self.__height = value
