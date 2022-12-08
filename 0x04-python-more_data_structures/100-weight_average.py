#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0

    for item in my_list:
        score += item[0] * item[1]
        weight += item[-1]

    return (score / weight)
