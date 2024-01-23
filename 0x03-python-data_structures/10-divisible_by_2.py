#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    ls = []
    for i in my_list:
        if i % 2 == 0:
            ls.append(True)
        else:
            ls.append(False)
    return ls
