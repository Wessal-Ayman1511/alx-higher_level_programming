#!/usr/bin/python3
""" matrix module """


def matrix_divided(matrix, div):
    """ function tha divide matrix

    Args:
    matrix: input
    div: input

    Return:
    divided matrix
    """
    ms_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(ms_error)
    for rw in matrix:
        if not isinstance(rw, list) or len(rw) == 0:
            raise TypeError(ms_error)
        if len(rw) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in rw:
            if not isinstance(element, (int, float)):
                raise TypeError(ms_error)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in rw] for rw in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
