#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_list = []
    for items in set_1:
        if items not in set_2:
            new_list.append(items)
    for items in set_2:
        if items not in set_1:
            new_list.append(items)
    return new_list
