#!/usr/bin/python3
"""
island_perimeter interview task
"""
from typing import List, Sequence


def  island_perimeter(grid: List[Sequence]) -> int:
    result = 0
    row_len = len(grid)
    for i in range(row_len):
        col_len = len(i)
        for j in range(col_len):
            if grid[i][j] == 1:
                result += 1

