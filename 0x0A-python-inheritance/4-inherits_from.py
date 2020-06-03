#!/usr/bin/python3
"""def class object"""


def inherits_from(obj, a_class):
    """return inherits"""
    if (type(obj) is not a_class):
        return(issubclass(type(obj), a_class))
    else:
        False
