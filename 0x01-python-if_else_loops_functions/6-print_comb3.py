#!/usr/bin/python3

def print_combinations():
    for tens_digit in range(10):
        for ones_digit in range(tens_digit + 1, 10):
            print(f"{tens_digit:01d}{ones_digit:01d}", end=', ' if ones_digit < 9 else '\n')

print_combinations()

