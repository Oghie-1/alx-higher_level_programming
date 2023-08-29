#!/usr/bin/python3

# function that executes a function safely.

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception:", e, file=sys.stderr)
        return None
