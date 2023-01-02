#!/usr/bin/python3
"""
This module performs the addition of two integers.
"""


def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a (int): an integer
        b (int): another integer - default value is 98

    Returns:
        The sum of the two integers.
    """
    return a + b


if __name__ == '__main__':
    print(add_integer.__doc__)
