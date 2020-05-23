#!/usr/bin/python3
"""Create"""


def add_integer(a, b=98):
    """add two integer
    Args:
        a: int
        b: int
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
