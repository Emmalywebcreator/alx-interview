#!/usr/bin/python3
"""
Rotates a 2D matrix by 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the given 2D matrix in-place.
    """
    print("Original matrix")
    for row in matrix:
        print(row)

    transp_matrix = [list(row) for row in zip(*matrix)]
    print("\nTransposed matrix")
    for row in transp_matrix:
        print(row)
    
    for i, row in enumerate(transp_matrix):
        transp_matrix[i] = row[::-1]
    
    matrix[:] = transp_matrix

    return rotate_2d_matrix
