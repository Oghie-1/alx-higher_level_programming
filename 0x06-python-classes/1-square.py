#!/usr/bin/python3

# Write a class Square that defines a square by: (based on 0-square.py


class Square:
    size = 20

    def __init__(self, size=None):
        if self.size is not None:
            self.size = size
        
