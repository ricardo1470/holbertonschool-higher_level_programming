#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    ch = (((number * -1) % 10) * -1)
else:
    ch = (number % 10)
if (ch != 0):
    if (ch > 5):
        print('Last digit of {:d} is {:d} and\
 is greater than 5'.format(number, ch))
    else:
        print('Last digit of {:d} is {:d} and is less than 6 and\
 not 0'.format(number, ch))
else:
    print('Last digit of {:d} is {:d} and is 0'.format(number, ch))
