#!/usr/bin/python3

def print_num():
    for number in range((100)):
        print(f"{number:02d}", end=", " if number < 99 else '\n')
print_num()
