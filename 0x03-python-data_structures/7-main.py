#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
tuple_c = (1, 89, 139)
tuple_d = (88, 11, 908)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
print(add_tuple((), ()))
print(add_tuple(tuple_c, tuple_d))
