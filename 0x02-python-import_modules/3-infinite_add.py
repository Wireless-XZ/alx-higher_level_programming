#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) - 1 == 0:
        print("0")
    else:
        i, sum_ = 1, 0
        while i < len(argv):
            sum_ += int(argv[i])
            i += 1
        print(sum_)
