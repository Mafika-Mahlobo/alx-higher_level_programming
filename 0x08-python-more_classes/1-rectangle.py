#!/usr/bin/python3

"""
This module contains a Rectoangle calss
"""


class Rectangle:

    """
    Rerectangle class with public methods.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height(int): The height of the new rectangle.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle"""
        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle"""
        self.__height = value
