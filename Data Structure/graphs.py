# -*- coding:utf-8 -*-  

'''
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
'''
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def aStar(self, graph, current, end):
    openSet = set()
    closedSet = set()
    path = []

    def retracePath(c):
        path.insert(0,c)
        if c.parent == None:
            return
        retracePath(c.parent)

    openSet.add(current)
    while len(openSet) is not 0:
        current = min(openSet, key=lambda inst:inst.H)
        if current == end:
            return retracePath(current)
        openSet.pop(current)
        closedSet.add(current)
        for tile in graph[current]:
            if tile not in closedSet:
                tile.H = (abs(end.x-tile.x)+abs(end.y-tile.y))*10 
                if tile not in openSet:
                    openSet.add(tile)
                tile.parent = current
    return path

