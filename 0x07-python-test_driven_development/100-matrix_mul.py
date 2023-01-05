#!/usr/bin/python3
# 100-matrix_mul.py
# tonybnya
"""
Matrix Multiplication
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices.

    Args:
        m_a (list of lists of integers/floats): 1st matrix
        b_a (list of lists of integers/floats): 2nd matrix

    Returns:
        The Matrix Product
    """
    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")

    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(item, (float, int)))
               for item in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(item, (float, int)))
               for item in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for row in range(len(m_b[0])):
        new_row = []
        for col in range(len(m_b)):
            new_row.append(m_b[col][row])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
