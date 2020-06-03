#!/usr/bin/python3
"""class"""


class BaseGeometry():
    """create class"""
    pass

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if (type(value) != int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
