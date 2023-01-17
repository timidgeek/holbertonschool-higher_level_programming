#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print("\n".join(" ".join(["{}".format(item) for item in row])
    for row in matrix))
