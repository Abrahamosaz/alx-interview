#!/usr/bin/python3
"""
2d matrix rotate interview task
"""


def rotate_2d_matrix(matrix):
    """
    function to rotate 2d matrix
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix in-place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix (in-place)
    for i in range(n):
        matrix[i] = list(reversed(matrix[i]))