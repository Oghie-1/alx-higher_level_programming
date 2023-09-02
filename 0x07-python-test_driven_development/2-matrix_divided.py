#!/usr/bin/python3
"""

This module defines a matrix division function

"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number

    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """

    try:
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise TypeError("matrix must be a list of lists")
        
        if not all(isinstance(val, (int, float)) for row in matrix for val in row):
            raise TypeError("matrix must contain only integers or floats")
        
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        
        if div == 0:
            raise ZeroDivisionError("division by zero")
        
        row_length = len(matrix[0])
        
        if any(len(row) != row_length for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        
        result = [[round(val / div, 2) for val in row] for row in matrix]
        
        return result
    except (TypeError, ZeroDivisionError) as e:
        return str(e)
