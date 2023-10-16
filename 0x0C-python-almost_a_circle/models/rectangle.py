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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("width must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter for attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""

        if not isinstance(heigh, int):
            raise TypeError("heigh must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter for attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for atttribute x"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for attribute y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for attribute y"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints rectangle on stdout using '#'"""

        for i in range(self.__height):
            for k in range(self.__width):
                print("#", end="")
            print()
