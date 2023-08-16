#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if __name__ == "__main__":
    new_matrix = square_matrix_simple(matrix)
    print("{}".format(new_matrix))
    print("{}".format(matrix))
