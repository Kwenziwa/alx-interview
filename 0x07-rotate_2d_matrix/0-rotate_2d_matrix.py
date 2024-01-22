#!/usr/bin/python3
# Author: Kwenziwa Lizwi Khanyile
# Date Created: 2024-01-22
# Description: 2D Matrix rotation


def rotate_2d_matrix(matrix):
    matrix.reverse()
    mylen = len(matrix)
    for x in range(mylen):
        for y in range(x):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
