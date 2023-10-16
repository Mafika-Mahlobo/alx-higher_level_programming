#!/usr/bin/python3

"""A module that contains the rectanle class"""


from models.base import Base


class Rectangle(Base):

    """Rectangle class that inherit from base class"""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of rectangle class, implementing Base logic"""
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for attributes width"""
        self.__width = width

    @property
    def height(self):
        """getter for attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""
        self.__height = height

    @property
    def x(self):
        """getter for attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for atttribute x"""
        self.__x = x

    @property
    def y(self, y):
        """getter for attribute y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for attribute y"""
        self.__y = y
