#!/usr/bin/python3
def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error)
    for rw in matrix:
        if len(rw) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(rw, list) or len(rw) == 0:
            raise TypeError(error)
        for element in rw:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
    return [[round(elem / div, 2) for elem in rw] for rw in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
