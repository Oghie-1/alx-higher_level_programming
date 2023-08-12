#!/usr/bin/python3
import decimal


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]  # Exclude the script name

    total = sum(decimal.Decimal(arg) for arg in args)
    print("{}".format(total))
