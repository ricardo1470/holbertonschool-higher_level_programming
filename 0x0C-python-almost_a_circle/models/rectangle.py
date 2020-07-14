#!/usr/bin/python3
"""create class rectangle"""
from models.base import Base
 


class Rectangle(Base):
    """init class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Args:
            width (int)
            height (int)
            x (int)
            y (int)
            id (int)"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height porperty"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x axis"""
        return self.__x

    @x.setter
    def x(self, value):
        """x axis"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y axis"""
        return self.__y

    @y.setter
    def y(self, value):
        """y axis"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area"""
        return (self.width * self.height)

    def __str__(self):
        """overriding str"""
        a, b, c, d, e = self.id, self.x, self.y, self.width, self.height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    def display(self):
        """update the class Rectangle"""
        if (self.y > 0):
            print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """update class args"""
        var_arg = ["id", "width", "height", "x", "y"]
        if (args):
            for i, arg in enumerate(args):
                if i < 5:
                    setattr(self, var_arg[i], arg)
        for key, value in kwargs.items():
            if (hasattr(self, key)):
                setattr(self, key, value)

    def to_dictionary(self):
        """create dictionary"""
        dic_arg = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y}
        return (dic_arg)

def draw(list_rectangles, list_squares):
    """list for turtle"""
