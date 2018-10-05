#!/usr/bin/python3
""""Module Square"""


class Square():
    """Created a square"""
    def __init__(self, size=0, area=0):
        """Square instantiation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value)
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0] or value[1] is not int:
            raise TypeError("value must be an integer")
        if value[0] or value[1] < 0:
            raise ValueError("value must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.size):
            print("#" * self.size)
