#!/usr/bin/python3
"""create"""


def append_write(filename="", text=""):
    """add line in file"""

    with open(filename, "a") as my_file:
        nb_char = my_file.write(str(text))
    my_file.close()
    return (nb_char)
