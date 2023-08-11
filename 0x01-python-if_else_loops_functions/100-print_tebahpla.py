#!/usr/bin/python3

def reversealpha():
    for char in range(ord('z'), ord('a') - 1, -1):
        print(chr(char).upper() if (ord('z') - char) % 2 == 0 else chr(char), end="")

reversealpha()
