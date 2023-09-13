#!/usr/bin/python3
"""Module 1-my_list
Creates a class inheriting from the list class.
"""


class MyList(list):
    """Custom list class that prints in ascending order."""
    def print_sorted(self):
        sorted_list = sorted(self)
        return sorted_list
