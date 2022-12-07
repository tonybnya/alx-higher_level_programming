#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new = []
        for row in matrix:
            for val in row:
                new.append(val ** 2)
        return (new)
