#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for i in my_list:
            if x != 0:
                print(i, end="")
            else:
                break
            len += 1
            x -= 1
        print("")
    except:
        pass

    return len
