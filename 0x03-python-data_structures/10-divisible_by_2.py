#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    lista = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            lista[i] = True
        else:
            lista[i] = False
    return lista
