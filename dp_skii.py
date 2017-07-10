#!/usr/bin/env python
#-*- coding: utf-8 -*-
#poj#1088

import numpy as np
from dfs_skii import *

row, col = AA.shape

def dp(i,j):
    "记录从xy出发最长的路径"
    max = 0
    "max记录从临接点出发的最长距离"
    if memory[i][j] > 0:
        return memory[i][j]
    "记录是否处理过,否则直接返回原来的值"

    if j >= 1:
        if AA[i,j] > AA[i,j-1]:
            if max < dp(i,j-1):
                max = dp(i,j-1)
    "向左走"
    if j+1 <= col-1:
        if AA[i,j] > AA[i,j+1]:
            if max < dp(i,j+1):
                max = dp(i,j+1)

    if i >= 1:
        if AA[i,j] > AA[i-1,j]:
            if max < dp(i-1,j):
                max = dp(i-1,j)

    if i+1 <= row-1:
        if AA[i,j] > AA[i+1,j]:
            if max < dp(i+1,j):
                max = dp(i+1,j)

    return max + 1

if __name__ == "__main__":
    maxlen = 0
    memory = [[0 for i in range(0,col)] for j in range(row)]
    for i in range(0,row):
        for j in range(0,col):
            memory[i][j] = dp(i,j)
            if maxlen < memory[i][j]:
                maxlen = memory[i][j]

    print 'The longest path starting at this point is',memory
    print 'Hence the longest path is',maxlen - 1


