#!/usr/bin/python3
# 8-class_to_json.py
# tonybnya
"""
Class to JSON
"""


def class_to_json(obj):
    """
    Function to return the dictionary description with simple DSA
    for JSON serialization of an object.

    Arg:
        obj (object): instance of a Class

    Returns:
        Dictionary representation
    """
    return obj.__dict__
