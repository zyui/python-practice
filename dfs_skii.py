#!/usr/bin/env python
#-*- coding: utf-8 -*-
#sloving poj problem 1088 using DFS

import numpy as np

AA = np.matrix('1 2 3 4 5;16 ,17 ,18 ,19 ,6;15 ,24 ,25, 20, 7;14, 23 ,22, 21 ,8;13, 12 ,11, 10,9;12.8,12.4,18,22,22')
#print A[0,1]  #
#print A.shape[1] #

def matrix2dict(A):             #graph in dictionary form
    " convert matrix to dict"
    row, col = A.shape
    dict = {}
    for i in range(0,row):
        for j in range(0,col):
            key = (i,j)
            value = []
            if i+1 in range(row):
                value.append((i+1,j))
            if i-1 in range(row):
                value.append((i-1,j))
            if j+1 in range(col):
                value.append((i,j+1))
            if j-1 in range(col):
                value.append((i,j-1))
            dict[key] = value
            #print key, value
    return dict

def dfs(graph,source):
    "return the list of possible path"

    path = [source]
    stack = [(source,path)]

    while stack:
        (v,path) = stack.pop()
        #print set(graph[v]) - visited
        for next in set(graph[v]) - set(path):
            #print AA[next],AA[v]
            if AA[next] <= AA[v]:
                stack.append((next,path + [next]))

        else:
# The usage of yield:  used in a generator function...
# return an iterator ，Call it with next or send(msg)
            yield path #+ [next]

if __name__ == "__main__":
    g = matrix2dict(AA)
    #print g
    allpath = list(dfs(g,(2,2)))   #list of all possible path
    m = len(allpath)  # 279 possible path
    path_len = []     #the list of path length

    for i in range(m):
        path_len.append(len(allpath[i]))

    maxlen = max(np.asarray(path_len))

    idx_max = path_len.index(maxlen)
    maxpath = allpath[idx_max]

    print "The longest path starting at (2,2) is", allpath[idx_max], "and the length is", maxlen-1
