#!/usr/bin/python3
"""
Rotates a 2D nxn matrix by 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the given 2D matrix in-place.
    """
    n = len(matrix)
    """Step 1: Transpose the matrix (swap rows and columns)"""
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    """Step 2: Reverse each row to complete the rotation"""
    for row in matrix:
        row.reverse()
