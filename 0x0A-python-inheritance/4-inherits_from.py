#!/usr/bin/python3
"""def class object"""


def inherits_from(obj, a_class):
    """return inherits"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
