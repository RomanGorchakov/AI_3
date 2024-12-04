#!/usr/bin/env python3
# -*- coding: utf-8 -*-


row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]

def isValid(x, y, mat):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0])

def findMaxLength(mat, x, y, previous):
    if not isValid(x, y, mat) or chr(ord(previous) + 1) != mat[x][y]:
        return 0

    max_len = 0

    for k in range(len(row)):

        length = findMaxLength(mat, x + row[k], y + col[k], mat[x][y])

        max_len = max(max_len, 1 + length)
 
    return max_len

def findMaximumLength(mat, ch):
    if not mat or not len(mat):
        return 0

    (M, N) = (len(mat), len(mat[0]))

    max_len = 0

    for x in range(M):
        for y in range(N):
            if mat[x][y] == ch:
                for k in range(len(row)):
                    length = findMaxLength(mat, x + row[k], y + col[k], ch)
                    max_len = max(max_len, 1 + length)
 
    return max_len
 
 
if __name__ == '__main__':
    matrix = [
        ['D', 'E', 'H', 'X', 'B'],
        ['A', 'O', 'G', 'P', 'E'],
        ['D', 'D', 'C', 'F', 'D'],
        ['E', 'B', 'E', 'A', 'S'],
        ['C', 'D', 'Y', 'E', 'N']
    ]

    character = 'C'
 
    print(findMaximumLength(matrix, character))