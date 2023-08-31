#!/usr/bin/python3

"""Define class Square. area"""

class Square:


    def __init__(self, size=0):
        """Initialize Square.
            size (int): size of square.
            area: returns current area of square.
        """
        

        if not  isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        square_area = self.__size * self.__size
        return square_area
