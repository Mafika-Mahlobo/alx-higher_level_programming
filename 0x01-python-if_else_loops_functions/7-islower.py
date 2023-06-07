#!/usr/bin/python3
def islower(c):
    if type(c) == str:
        if ord(c) >= 97 and ord(c) <= 122:
            return True
        else:
            return False
    else:
        return False
