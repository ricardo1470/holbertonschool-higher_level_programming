#!/usr/bin/python
def print_last_digit(number):
    ch = abs(number) % 10
    print(ch, end="")
    return(ch)
