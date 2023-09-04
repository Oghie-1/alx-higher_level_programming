#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """
    if type(text) is not str:
        raise TypeError("NOT STR")

    for delim in ".:?":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
