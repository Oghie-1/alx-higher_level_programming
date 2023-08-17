#!/usr/bin/python3


def best_score(a_dictionary):
    best_key = None
    max_score = float('-inf')  # Initialize with negative infinity

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_key = key
        else:
            return None

    return best_key
