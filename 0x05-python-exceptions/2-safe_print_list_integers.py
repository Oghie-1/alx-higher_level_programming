#!/usr/bin/python3


# function that prints the first x elements of a list and only integers.

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print(my_list[i], end="")
                count += 1
        print()
        return count
    except (IndexError, ValueError, TypeError):
        print()
        return count