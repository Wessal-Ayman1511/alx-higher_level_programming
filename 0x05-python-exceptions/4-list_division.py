#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    lista = []
    div = 0
    while i < int(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            lista.append(div)
            i += 1
    return lista
