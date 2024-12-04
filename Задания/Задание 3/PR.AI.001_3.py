#!/usr/bin/env python3
# -*- coding: utf-8 -*-


row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))\
        and not processed[x][y]

def searchBoggle(board, words, result, processed, i, j, path=''):
    processed[i][j] = True

    path += board[i][j]

    if path in words:
        result.add(path)

    for k in range(len(row)):
        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, result, processed, i + row[k], j + col[k], path)

    processed[i][j] = False
 
 
def searchInBoggle(board, words):
    result = set()

    if not board or not len(board):
        return

    (M, N) = (len(board), len(board[0]))

    processed = [[False for x in range(N)] for y in range(M)]

    for i in range(M):
        for j in range(N):
            searchBoggle(board, words, result, processed, i, j)
 
    return result
 
 
if __name__ == '__main__':
 
    board = [
        ['М', 'С', 'Е'],
        ['Р', 'А', 'Т'],
        ['Л', 'О', 'Н']
    ]
 
    dictionary = ['МАРС', 'СОН', 'ЛЕТО', 'ТОН']
 
    validWords = searchInBoggle(board, dictionary)
    print(validWords)