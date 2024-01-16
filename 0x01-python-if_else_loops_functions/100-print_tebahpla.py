#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        print(f"{i:c}", end="")
    else:
        print(f"{(i - 32):c}", end="")
