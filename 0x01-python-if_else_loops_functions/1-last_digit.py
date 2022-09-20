#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number > 0):
    print("Last digit of {} is {}".format(number, (number % 10)), end=" ")
else:
    print("Last digit of {} is {}".format(number, ((number * -1) % 10)), end=" ")
    number *= -1

if ((number % 10) > 5):
    print("and is greater than 5")
elif ((number % 10) == 0):
    print("and is zero")
else:
    print("and is less than 6 and not 0")
