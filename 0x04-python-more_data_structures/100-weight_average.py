#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    divisor = dividend = 0
    holder = 1
    for tuple_ in my_list:
        for i in tuple_:
            holder *= i
        dividend += holder
        divisor += i
        holder = 1
    return dividend / divisor
