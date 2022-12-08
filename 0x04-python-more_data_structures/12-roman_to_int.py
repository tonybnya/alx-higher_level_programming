#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not isinstance(roman_string, str):
        return (0)

    if not roman_string:
        return (0)

    if len(roman_string) == 1:
        return (nums[roman_string])

    number = 0
    prev = number

    for ch in roman_string[::-1]:
        value = nums[ch]
        if value >= prev:
            number += value
            prev = value
        else:
            number -= value

    return (number)
