#!/usr/bin/env python3
def print_last_digit(number):
    number = abs(number) % 10
    print(f"{number:d}", end="")
    return number
