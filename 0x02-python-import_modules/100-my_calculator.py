#!/usr/bin/python3
from sys import argv, exit
import calculator_1 as cal

if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    elif argv[2] == "+":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.add(int(argv[1]), int(argv[3]))))
    elif argv[2] == "-":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == "*":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == "/":
        print("{} {} {} = {}".format(argv[1],
                                     argv[2],
                                     argv[3],
                                     cal.div(int(argv[1]), int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
