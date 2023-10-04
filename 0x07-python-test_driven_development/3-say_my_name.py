#!/usr/bin/python3

"""
this module contains a function that prints
 a message wiith user name and surname
"""


def say_my_name(first_name, last_name=""):

    """
    This function prints out user's name and surname back to the user

    Args:
        first_name(str): first name
        last_name(str): last name

        Returns:
            0
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
