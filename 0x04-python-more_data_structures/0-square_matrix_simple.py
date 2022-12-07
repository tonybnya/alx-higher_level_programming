#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    func = lambda val: val ** 2
    return ([[func(val) for val in row] for row in matrix])
