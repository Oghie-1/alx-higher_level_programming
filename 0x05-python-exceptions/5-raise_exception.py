#!/usr/bin/python3

# function that raises a type exception.

def raise_exception():
    try:
        raise TypeError("wrong type")

    except TypeError:
        print("Exception raised")