#!/usr/bin/python3
# 1-write_file.py
# tonybnya
"""
Writes a string to a text file encoded with the standard encoding mode UTF-8.
"""


def write_file(filename="", text=""):
    """
    Function that writes to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (text file): the path to the filename
        text (string): the content to insert to the file

    Returns:
        the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)

    with open(filename, encoding='utf-8') as file:
        # run = True
        # while run:
        #     line = file.readline()

        #     if not line:
        #         break

        #     words = line.split()
        #     chars = 0

        #     for word in words:
        #         for _ in word:
        #             chars += 1
        lines = file.readlines()
        chars = 0
        for line in lines:
            chars += len(line)

    return chars
