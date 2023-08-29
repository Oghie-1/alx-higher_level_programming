#!/usr/bin/python3

# function that raises a name exception with a message.


def raise_exception_msg(message=""):
    try:
        raise NameError ("Wrong Name")
    except NameError:
        print("{}".format(message))


