#!/usr/bin/python3

"""module containing a function that reads  file."""


def read_file(filename=""):

    """Prints the contents of a UTF8 text file to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
