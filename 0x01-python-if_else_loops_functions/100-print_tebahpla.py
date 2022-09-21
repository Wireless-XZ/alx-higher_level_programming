#!/usr/bin/python3
n = 1
for i in reversed(range(ord("a"), ord("{"))):
    if n % 2 == 0:
        i = i - 32
    print("{}".format(chr(i)), end="")
    n += 1
