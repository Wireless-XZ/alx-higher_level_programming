#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_b) < 2:
        list_ = list(tuple_b)
        list_.append(0)
        tuple_b = tuple(list_)
    while len(tuple_b) > 2:
        list_ = list(tuple_b)
        list_.pop(len(tuple_b) - 1)
        tuple_b = tuple(list_)

    while len(tuple_a) < 2:
        list_ = list(tuple_a)
        list_.append(0)
        tuple_a = tuple(list_)
    while len(tuple_a) > 2:
        list_ = list(tuple_a)
        list_.pop(len(tuple_a) - 1)
        tuple_a = tuple(list_)
    return tuple([x + y for x, y in zip(list(tuple_a), list(tuple_b))])
