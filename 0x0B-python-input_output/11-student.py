#!/usr/bin/python3
"""create"""


class Student():
    """create class"""
    def __init__(self, first_name, last_name, age):
        """students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns students"""
        return(self.__dict__)
