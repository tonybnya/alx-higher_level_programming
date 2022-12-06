#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_value = my_list[0]
        for val in my_list[1:]:
            if val > max_value:
                max_value = val
        return (max_value)
    return(None)
