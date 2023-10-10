#!/usr/bin/python3

"""module containing a classs with one method"""


class BaseGeometry:

    """a class with one method that raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")
