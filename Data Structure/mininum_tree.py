# -*- coding:utf-8 -*-  


# coding: utf-8
import re


# Class WeightedGraph
class WeightedGraph:
    def __init__(self, path):
        # open file to initialize the graph
        file = open(path, "r")
        p = re.compile("\d+")

        # initialize the graph
        self.vertices, self.edges = map(int, p.findall(file.readline()))
        # use adjacent matrix to represent the graph
        self.graph = [[0]*self.vertices for _ in range(self.vertices)]

        # populate the graph
        for i in range(self.edges):
            u, v, weight = map(int, p.findall(file.readline()))
            self.graph[u][v] = weight
            self.graph[v][u] = weight


# Union find data structure for quick kruskal algorithm
class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    # judge two node connected or not
    def connected(self, p, q):
        return self._find(p) == self._find(q)

    # quick union two component
    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    # find the root of p
    def _find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p



# prim algorithm
def prim(G):
    # initialize the MST and the set X
    MST = set()
    X = set()

    # select an arbitrary vertex to begin with
    X.add(0)
    while len(X) != G.vertices:
        crossing = set()
        # for each element x in X, add the edge (x, k) to crossing if
        # k is not in X
        for x in X:
            for k in range(G.vertices):
                if k not in X and G.graph[x][k] != 0:
                    crossing.add((x, k))
        # find the edge with the smallest weight in crossing
        edge = sorted(crossing, key=lambda e:G.graph[e[0]][e[1]])[0]
        # add this edge to MST
        MST.add(edge)
        # add the new vertex to X
        X.add(edge[1])
    return MST


# kruskal algorithm
def kruskal(G):
    # initialize MST
    MST = set()
    edges = set()
    # collect all edges from graph G
    for j in range(G.vertices):
        for k in range(G.vertices):
            if G.graph[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    # sort all edges in graph G by weights from smallest to largest
    sorted_edges = sorted(edges, key=lambda e:G.graph[e[0]][e[1]])
    uf = UF(G.vertices)
    for e in sorted_edges:
        u, v = e
        # if u, v already connected, abort this edge
        if uf.connected(u, v):
            continue
        # if not, connect them and add this edge to the MST
        uf.union(u, v)
        MST.add(e)
    return MST

'''
# Kruskal

def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]


def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1


def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u: u for u in G}, {u: 0 for u in G}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T


a, b, c, d, e, f, g, h = range(8)
G = {
    a: {b, c, d, e, f},
    b: {c, e},
    c: {d},
    d: {e},
    e: {f},
    f: {c, g, h},
    g: {f, h},
    h: {f, g}
}
from scipy.stats import uniform

rv = uniform(loc=0, scale=1)
V = {i: rv.rvs(size=2) for i in range(8)}

import numpy as np

G = {u: {v: np.linalg.norm(V[u] - V[v], ord=2) for v in G[u]} for u in G}

k = kruskal(G)

from scipy.stats import uniform

import matplotlib.pyplot as plt

for i in V:
    plt.plot(V[i][0], V[i][1], 'o')
for i in G:
    for j in G[i]:
        temp = list(zip(V[i], V[j]))
        plt.plot(temp[0], temp[1], 'k')

for i in k:
    temp = list(zip(V[i[0]], V[i[1]]))
    plt.plot(temp[0], temp[1], 'r', lw=8, alpha=0.6)
plt.show()

# prim
from heapq import heappop, heappush


def prim(G, s):
    P, Q = {}, [(0, None, s)]
    while Q:
        _, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        for v, w in G[u].items():
            heappush(Q, (w, u, v))
        return P
'''