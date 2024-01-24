#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for k, v in dic.items():
        dic[k] = v * 2
    return dic
