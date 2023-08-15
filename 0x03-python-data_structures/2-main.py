#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
element = 9
new_list = replace_in_list(my_list, idx, element)


if new_list is not None:
    print("\nNew Element at index {:d} is {}".format(idx, new_list[idx]))
    print(new_list)
    print(my_list)
else:
    print("Index out of range.")
