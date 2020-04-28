#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        ch = ((number * -1) % 10)
    else:
        ch = (number % 10)
    print("{:d}".format(ch), end="")
    return(ch)
