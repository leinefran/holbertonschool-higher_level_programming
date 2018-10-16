#!/usr/bin/python3
"""A BaseGeometry Class"""


class BaseGeometry:
    """"Represents a class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Represents a class Rectangle"""

    def __init__(self, width, height):
        """Rectangle Instantiation"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        a = self.__width * self.__height
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

        return str(a)

class Square(Rectangle):
    """Represents the class Rectangle"""

    def __init__(self, size):
        """Square instantiation with size"""

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        a = self.__size * self.__size
        print("[Rectangle] {}/{}".format(self.__size, self.__size))

        return str(a)
