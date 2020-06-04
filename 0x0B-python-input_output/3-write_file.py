#!/usr/bin/python3
"""create"""


def write_file(filename="", text=""):
    """write a string in a file"""

    with open(filename, "w") as my_file:
        nb_char = my_file.write(str(text))
    my_file.close()
    return (nb_char)
