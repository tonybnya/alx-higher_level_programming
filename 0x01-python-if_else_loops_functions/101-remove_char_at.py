#!/usr/bin/python3
def remove_char_at(str, n):
    idx = 0
    new = ""
    for ch in str:
        if idx != n:
            new += ch
        else:
            pass
        idx += 1
    return new
