#!/usr/bin/python3
for i in range(0, 100):
    for j in range(i, 10):
        print(f"{i:d}{j:d}", end="\n" if i == 9 and j == 9 else ", ")
