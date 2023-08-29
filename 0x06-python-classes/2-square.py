#!/usr/bin/python3

# class Square that defines a square by: (based on 1-square.py)

class Square:
    __size = 1

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

