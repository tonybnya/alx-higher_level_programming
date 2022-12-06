#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new = ""
        for ch in my_string:
            if ch != 'c' or ch != 'C':
                new += ch
        return (new)
