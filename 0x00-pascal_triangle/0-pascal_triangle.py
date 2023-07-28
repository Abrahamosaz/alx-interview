#!/usr/bin/python3
"""
pascal triangle algorithm
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    pascal_triangle_list = []
    # Iterating through rows
    for n in range(0, n):
        inner_list = []
        # iterating through each value of the row
        for k in range(0, n + 1):
            inner_list.append(factFormula(n, k))
        pascal_triangle_list.append(inner_list)
    return pascal_triangle_list

#function to find factorial
def findFact(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i*findFact(i-1)

# function for the Combination formula
def factFormula(n, k):
    return int(findFact(n)/(findFact(n-k)*findFact(k)))
