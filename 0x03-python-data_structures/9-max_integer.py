#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list < 0):
        return (None)
    a = my_list[0]
    for i in range(0, len(my_list)):
        if (my_list > a):
            a = my_list[i]
        return (a)
