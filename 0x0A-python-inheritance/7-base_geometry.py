#!/usr/bin/python3

"""
module containing a classs with two methods
that raise an exception and validates an integer respectively.
"""


class BaseGeometry:

    """a class with that with two methods. area and integer validator"""

    def area(self):
        """raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        validate an integer value

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
