#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            len += 1
        print()
        return len
    except IndexError:
        print()
        return len
