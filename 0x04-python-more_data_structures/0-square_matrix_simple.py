#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    for i in range(len(matrix_copy)):
        matrix_copy[i] = list(map(lambda a: a ** 2, matrix_copy[i]))
    return (matrix_copy)
