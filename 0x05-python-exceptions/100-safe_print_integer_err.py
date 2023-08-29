#!/usr/bin/python3

# function that prints an integer.

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False


value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
