#!/usr/bin/python3
x = 0
for i in range(0, 10):
    for j in range(0, 10):
        if (((i + 1) == 10 or (i + 2) == 10) and j == 9):
            print("{}{}".format(i, j))
            x = 1
            break
        elif not (j <= i):
            print("{}{},".format(i, j), end=" ")
    if x == 1:
        break
