#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    temp = 0

    roman_to_int = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
    for i in roman_string:
        int_val = roman_to_int.get(i)
        if int_val > temp:
            number += int_val - 2 * temp
        else:
            number += int_val
        temp = int_val
    return number
