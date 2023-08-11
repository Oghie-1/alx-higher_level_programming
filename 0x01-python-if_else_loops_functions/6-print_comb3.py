#!/usr/bin/python3

def print_combinations():
    for i in range(10):
        for j in range(tens_digit + 1, 10):
            print("{}{}".format(i, j), end=", " if tens_digit != 8 else "\n")


print_combinations()

