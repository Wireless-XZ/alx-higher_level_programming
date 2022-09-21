#!/usr/bin/python3
def uppercase(str):
    up_list = []
    for i in str:
        if ord(i) in range(ord("a"), ord("{")):
            up_list.append(chr(ord(i) - 32))
        else:
            up_list.append(i)

    for j in up_list:
        print("{}".format(j), end="")
    print("")
