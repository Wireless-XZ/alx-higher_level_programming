#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in matrix:
            x = 0
            for j in i:
                if x < len(i) - 1:
                    print("{:d}".format(j), end=" ")
                else:
                    print("{:d}".format(j))
                    break
                x += 1
    else:
        print("")
