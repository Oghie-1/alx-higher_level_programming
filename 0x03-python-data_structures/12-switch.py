#!/usr/bin/python3

a = 89
b = 10

def switch(a, b):
    return b, a

a, b = switch(a, b)
print("a={:d} - b={:d}".format(a, b))
