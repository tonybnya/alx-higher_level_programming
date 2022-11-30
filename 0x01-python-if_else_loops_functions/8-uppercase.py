#!/usr/bin/python3
def uppercase(str):
    new = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            new += chr(ord(ch) - 32)
        else:
            new += ch

    print(new)
