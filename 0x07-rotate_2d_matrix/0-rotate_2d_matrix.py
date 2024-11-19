#!/usr/bin/python3
"""
Rotates a 2D nxn matrix by 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the given 2D matrix in-place.
    """
    n = len(matrix)
    if matrix is None or n < 1:
        return
    if n == 1:
        return
    else:
        new_matrix = [row[:] for row in matrix]

        for i in range(0, n):
            for j in range(0, n):
                new_matrix[j][n-1-i] = matrix[i][j]
            return new_matrix
