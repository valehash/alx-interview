#!/usr/bin/env python3
"""
Script witha function to transpose a 2d matrix
"""

def rotate_2d_matrix(matrix):
    """
    Function that rotates a 2d matrix by 90 degrees
    """ 
    # reversing the matrix
    for i in range(len(matrix)):
        matrix[i].reverse()
    # make transpose of the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # swapping mat[i][j] and mat[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
    matrix.reverse()
