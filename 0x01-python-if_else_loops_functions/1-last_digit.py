#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = 0
if number == 0:
     print("Last digit of {} is {} and is {}".format(number, number, number))
     x = 1
elif (number > 0):
     print("Last digit of {} is {}".format(number, (number % 10)), end=" ")
else:
     print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, -1 * ((number * -1) % 10)))
     x = 1

if ((number % 10) > 5 and x == 0):
     print("and is greater than 5")
elif ((number % 10) == 0 and x == 0):
     print("and is zero")
else:
     if x == 0:
          print("and is less than 6 and not 0")
