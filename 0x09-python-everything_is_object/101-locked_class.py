#!/usr/bin/python3
# 101-locked_class.py
# tonybnya
"""
Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """Definition of the Locked Class."""
    __slots__ = "first_name"
