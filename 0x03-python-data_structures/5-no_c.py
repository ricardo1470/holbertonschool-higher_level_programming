#!/bin/bash/python3
def no_c(my_string):
    for ch in my_string:
        i = my_string
        return(i.translate({ord('c'): None, ord('C'): None}))
