#!/usr/bin/python3
even = 122
odd = 89
alphabet = ""
i = 0
while i < 26:
    if i % 2 == 0:
        alphabet += chr(even)
        even -= 2
    else:
        alphabet += chr(odd)
        odd -= 2
    i += 1
print("{}".format(alphabet), end="")
