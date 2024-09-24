#!/usr/bin/env python3
"""
Script ot create pascals triangle with arrays
"""
from typing import List


def pascal_triangle(n: int) -> List[int]:
    """Function to calculate and display pascals triangle"""
    if (n <= 0 ):
        return []
    
    res = [[1]]
    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
