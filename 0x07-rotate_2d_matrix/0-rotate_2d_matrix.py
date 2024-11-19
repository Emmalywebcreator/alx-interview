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
    
    for row in transp_matrix:
        row.reverse()
    
    print('\nRotated matrix')
    for row in transp_matrix:
        print(row)

    return rotate_2d_matrix
