#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

operators = ['+', '-', '*', '/']

if not len(argv) == 4:
    print(f"Usage: {argv[0]} <a> <operator> <b>")
    exit(1)

elif not argv[2] in operators:
    print(f"Unknown operator. Available operators: +, -, * and /")
    exit(1)

else:
    if argv[2] == operators[0]:
        print(f"{argv[1]} {argv[2]} {argv[3]} = "
              f"{add(int(argv[1]), int(argv[3]))}")
    elif argv[2] == operators[1]:
        print(f"{argv[1]} {argv[2]} {argv[3]} = "
              f"{sub(int(argv[1]), int(argv[3]))}")
    elif argv[2] == operators[2]:
        print(f"{argv[1]} {argv[2]} {argv[3]} = "
              f"{mul(int(argv[1]), int(argv[3]))}")
    elif argv[2] == operators[3]:
        print(f"{argv[1]} {argv[2]} {argv[3]} = "
              f"{div(int(argv[1]), int(argv[3]))}")

    exit(0)
