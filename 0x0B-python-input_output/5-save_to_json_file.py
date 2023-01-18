#!/usr/bin/python3
# 5-save_to_json_file.py
# tonybnya
"""
Function that writes an Object to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj (string): JSON representation of a string object
        filename (text file): the path to the filename
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
