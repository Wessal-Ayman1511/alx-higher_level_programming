#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for inner in matrix:
        if len (inner) == 0:
            print()
        for j in range(len(inner)):
            print("{:d}".format(inner[j]),
                    end='\n' if j == len(inner) - 1 else " ")
