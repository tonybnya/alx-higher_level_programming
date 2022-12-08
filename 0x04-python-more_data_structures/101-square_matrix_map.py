#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = matrix.copy()
    return ((list(map(lambda row: list(map(lambda y: (y**2), row)), new))))
