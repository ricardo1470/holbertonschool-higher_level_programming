#!/usr/bin/python3
"""Create class"""


class Rectangle():
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Initialize Rectangle width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Initialize Rectangle height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
