#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if (n == i):
            j = str.replace(str[n], "")
            return (j)
    else:
        return (str)
