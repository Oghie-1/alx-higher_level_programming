#!/usr/bin/python3

# function that divides element by element 2 lists.

def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]

                if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                    raise TypeError("wrong type")

                if element_2 == 0:
                    raise ZeroDivisionError("division by 0")

                result.append(element_1 / element_2)

            except IndexError:
                print("out of range")
                result.append(0)
            except TypeError as e:
                print(e)
                result.append(0)
            except ZeroDivisionError as e:
                print(e)
                result.append(0)
    finally:
        return result