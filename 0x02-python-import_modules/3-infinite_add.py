#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

tot = 0

if len(argv) == 1:
    print(str(0))

else:
    for i in range(1, len(argv)):
        tot += int(argv[i])

    print(str(tot))
