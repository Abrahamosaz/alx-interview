#!/usr/bin/python3
"""
2d matrix rotate interview task
"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    matrix_len = len(matrix)

    # first transpose the matrix
    for i in range(matrix_len):
        for j in range(i, matrix_len):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(matrix_len):
        matrix[i] = list(reversed(matrix[i]))
