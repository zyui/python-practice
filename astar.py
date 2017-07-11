#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy as np
import heapq

class Graph(object):
    "define graph class"
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def add_vertex(self,vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = {}

    def add_edge(self,edge):
        (source,target,weight) = tuple(edge)
        if target not in self._graph_dict.keys():
            self.add_vertex(target)
        if source in self._graph_dict.keys():
            self._graph_dict[source][target] = weight
        else:
            self.add_vertex(source)
            self._graph_dict[source][target] = weight

class Queue(object):
    "Priority Queue"
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item, priority):
        "an element with high priority is served before an element with low priority"
        heapq.heappush(self.items,(priority,item))

    def dequeue(self):
        "if we want to access the smallest item without popping it, use heap[0]"
        return heapq.heappop(self.items)[1]


def manhattan(x,y):
    "heuristic function: h() "
    (x1,x2) = x
    (y1,y2) = y
    return abs(x1-y1)+abs(x2-y2)

def astar(source,target,graph):
    current = source
    queue = Queue()
    queue.enqueue(source,0)
    parent = {}
    costSum = {}
    parent[source] = None
    costSum[source] = 0
    "costSum = best distance from source to current node = g(). Also store the visited node"
    while not queue.isEmpty():
        current = queue.dequeue()
        #print current
        if current == target:
            break

        for next in graph._graph_dict[current].keys():
            newcost = costSum[current] + graph._graph_dict[current][next]
            "newcost from s to next g(next) = g(current) + d(current,next)"
            if next not in costSum or newcost < costSum[next]:
                "if next not visited or find smaller g(next)"
                costSum[next] = newcost
                priority = newcost + manhattan(target,next)
                "f() function"
                queue.enqueue(next,priority)
                parent[next] = current

    return parent, costSum

if __name__ == '__main__':
    g = Graph({(1,1):{(2,1):1.2,(1,2):1}\
               #(1,1) adj node (2,1) and (1,2), and weight associated of the edge are 1.2 and 1
                  ,(1,2):{(2,2):1.3,(1,3):0.3}\
                  ,(2,2):{(2,3):0.4,(3,2):0.9}\
                  ,(2,1):{(3,1):0.9,(2,2):1.2}\
                  ,(2,3):{(3,3):0.8}\
                  ,(3,3):{}\
                  ,(1,3):{(2,3):1.9}\
                  ,(3,1):{(3,2):1.8}})
    #or: g._graph_dict = {'A':{'C':2,'B':1},'B':{'C':1.2},'C':{}} somethong alike
    g.add_edge(((3,2),(3,3),0.9))
    t = (3,3)
    s = (1,1)
    (parent, distance) = astar((1,1),(3,3),g)
    t = (3,3)
    #print path
    path = []
    while parent[t]:
        path.append(t)
        t = parent[t]
    path.append(s)
    print path
    print distance


