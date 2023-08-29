#!/usr/bin/python3

# Python function def magic_calculation(a, b): 
#that does exactly the same as the bytecode in Readme


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except:
            result = b + a
            break

    return result


magic_calculation(a, b)