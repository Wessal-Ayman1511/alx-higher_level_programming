#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print(
                f"{(ord(i) - 32):c}"
                if ord(i) >= 97 and ord(i) <= 122 else f"{ord(i):c}", end="")
    print()
