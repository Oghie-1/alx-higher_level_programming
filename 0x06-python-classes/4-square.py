#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size  # Use the setter to validate and set the size

    @property
    def size(self):
        return self.__size  # Getter for size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2

