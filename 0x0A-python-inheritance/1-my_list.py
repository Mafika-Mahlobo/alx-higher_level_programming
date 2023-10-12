#!/usr/bin/python3

"""
Module containing a class Mylist that works with lists
"""


class MyList(list):

    """
    this clss contains one method that sorts a list
    in ascending order.
    """

    def print_sorted(self):

        """prints a sorted list"""

        print(sorted(self))
