#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div, list_ = 0, []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            list_.append(div)
        except ZeroDivisionError:
            print("division by 0")
            list_.append(0)
        except IndexError:
            print("out of range")
            list_.append(0)
            break
        except TypeError:
            print("wrong type")
            list_.append(0)
        finally:
            continue
    return list_
