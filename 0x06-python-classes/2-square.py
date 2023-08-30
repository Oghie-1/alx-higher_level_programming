#!/usr/bin/python3

"""Define class Square. with exceptions if size not int"""


class Square:
    def __init__(self, size=0):
        
        """initialize new sqr"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
             raise ValueError("size must be >= 0")
        self.__size = size """returns size of sqr"""

