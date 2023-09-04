#!/usr/bin/python3

def print_square(size):
    size = None
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if isintance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        return size * #
    except Exception as e:
        print(e)
