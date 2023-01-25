#!/usr/bin/python3


def matrix_divided(matrix, div):
    mes0 = "matrix must be a matrix (list of lists) of integers/floats"
    mes1 = "Each row of the matrix must have the same size"
    res_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(mes1)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(mes0)
            else:
                inner_list.append(round(items / div, 2))
        res_matrix.append(inner_list)

    return res_matrix
