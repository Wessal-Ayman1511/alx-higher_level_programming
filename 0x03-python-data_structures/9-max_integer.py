#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = my_list[0]
    for i in range(len(my_list) - 1):
        if my_list[i] > mx:
            mx = my_list[i]
    return mx
