#!/usr/bin/python3

def print_alpha():
    for letter in range(ord("a"), ord("z") + 1):
        print(f"{chr(letter)}", end=" ")
print_alpha()
