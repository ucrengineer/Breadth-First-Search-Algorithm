""" This program will implement the BFS algorithmn"""
import queue
import numpy as np
import pandas as pd
from Table import *


def bfs_algorithm(Graph,S,G):
    #create empy list of variables
    queue = []
    parent = []
    node = []
    queue.append(S)
    node.append(S)
    #for each node in graph
    for each in Graph:
        #parent(node) = none
        parent.append('None')
    #parent(start node) = self
    parent[S] = 'Self'
    while len(queue) != 0:
        #LIFO function for queue
        #Get the nodes it touches
        v = Graph[queue.pop()]
        #Get the node
        j = node.pop()
        i = 0

        #For each node
        for each in v:
            #If it is touching the node and has not touched before
            if each == 1 and parent[i] == 'None':
                #Parent of that node is v
                parent[i] = j
                #Add that node its touching to queue
                queue.append(i)
                node.append(i)
            #If the node that is popped the goal    
            elif j == G:
                #Want map of graph so continue
                #If just want path add a "return"
                print('success')
            i = i + 1
    print(parent)        
    extract_path(G,parent)

def extract_path(G,parent):
    P = []
    P.append(G)
    u = G
    while parent[u] != 'Self':
        u = parent[u]
        P = [u] + P
    #print(P)
        
    


S = 0
G = 4
bfs_algorithm(Graph,S,G)
