#!/bin/bash/python3
def no_c(my_string):
    for ch in my_string:
        if (ch != 'c' or ch != 'C'):
            return(my_string)
