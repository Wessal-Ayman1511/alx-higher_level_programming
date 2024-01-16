#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(0, len(str)):
        if i == n:
            continue
        else:
            print("{:s}".format(str[i]), end="")
