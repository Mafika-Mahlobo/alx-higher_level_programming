#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print(f"Last digit of {number} is {abs(umber) % 10} and is 0")
elif number < 6 and not number == 0:
    print(f"Last digit of {number} is {abs(number) % 10} and is"
          "less than 6 and not 0")
elif number < 5:
    print(f"Last digit of {number} is {abs(number) % 10} and is"
          "greater than 5")