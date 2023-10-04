#!/usr/bin/python3

"""
This module contain a function that prints a string with new linew 
when it ecounters these characters . ? :
"""


def text_indentation(text):

    """
    Prints 2 new lines with a string (text) each time it encouters characters . ? and :

    Args:
        text(str): input string

    Returns:
        No return vdalue
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

    for char in text:

        if char in ['.', '?', ':']:
            new_text += char + "\n\n"
        else:
            new_text += char

    print(new_text, end="")
