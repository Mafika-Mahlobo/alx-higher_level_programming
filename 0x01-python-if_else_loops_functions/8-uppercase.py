#!/usr/bin/python3
def uppercase(str):
    new_str = str
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new_str = new_str.replace(str[i], chr(ord(str[i]) - 32))

    print(new_str)
