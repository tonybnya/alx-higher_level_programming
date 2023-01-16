#!/usr/bin/python3
# 2-append_write.py
# tonybnya
"""
Appends a string to the end of a text file (UTF-8)
"""


def append_write(filename="", text=""):
    """
    Function that appends to a text file (UTF-8) and returns
    the number of characters added.

    Args:
        filename (text file): the path to the filename
        text (string): the content to insert to the file
    """
    with open(filename, mode='a+', encoding='utf-8') as file:
        contents = file.readlines()
        lines = len(contents)
        chars_added = 0

        if lines == 0:
            file.write(text)
            words = file.readlines()

            for word in words:
                for _ in word:
                    chars_added += 1
        else:
            line_num = lines + 1
            while line_num > lines:
                line = file.readline()
                words = line.strip()

                for word in words:
                    for _ in word:
                        chars_added += 1

                if not line:
                    break

                lines += 1

    return chars_added
