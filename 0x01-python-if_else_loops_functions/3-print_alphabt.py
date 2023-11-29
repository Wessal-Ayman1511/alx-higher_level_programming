#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if alpha != ord('e') and alpha != ord('q'):
        print('{:c}'.format(alpha), end='')
