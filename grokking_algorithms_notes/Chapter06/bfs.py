# -*- coding:utf-8 -*-  
# graph = {}
# graph["you"] = ["alice", "bob", "claire"]
# graph["bob"] = ["anuj", "peggy"]
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []

def bfs(graph, target, start):
    from collections import deque
    queue = deque()
    searched = set()
    queue += graph[start]
    while queue:
        n = queue.popleft()
        if n in searched:
            continue
        searched.add(n)
        if n==target:
            return True
        else:
            queue += graph[n]
    return False

def dfs(graph, target, start):
    stack = []
    searched = set()
    stack.append(start)
    while stack:
        n = stack.pop()
        if n in searched:
            continue
        searched.add(n)
        if n==searched:
            return True
        if len(graph[n]):
            stack.append(graph[n][0])
    return False
            