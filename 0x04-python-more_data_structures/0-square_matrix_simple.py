#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    func = lambda x: x ** 2
    new = [[func(val) for val in row] for row in matrix]
    return (new)
