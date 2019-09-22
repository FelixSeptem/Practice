# -*- coding:utf-8 -*-  
# 迪杰斯特拉算法适用于带权重的有向无环图（权重非负）

# graph["a"] = {}
# graph["a"]["fin"] = 1
# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5
# graph["fin"] = {} ←------终点没有任何邻居

# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity

# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None

def dijstra(start, target, graph):
    costs, parents = init_costs(graph, start, target), init_parents(graph, start, target)
    node = find_lowest_cost_node(costs) # ←------在未处理的节点中找出开销最小的节点
    while node: # ←------这个while循环在所有节点都被处理过后结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys(): # ←------遍历当前节点的所有邻居
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost: # ←------如果经当前节点前往该邻居更近，
                costs[n] = new_cost # ←------就更新该邻居的开销
                parents[n] = node # ←------同时将该邻居的父节点设置为当前节点
        processed.add(node) # ←------将当前节点标记为处理过
        node = find_lowest_cost_node(costs) # ←------找出接下来要处理的节点，并循环


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # ←------遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # ←------如果当前节点的开销更低且未处理过，
            lowest_cost = cost # ←------就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node

def init_costs(graph, start, target):
    costs = {}
    for node in range graph[start].keys():
        costs[node] = graph[start][node]
    if costs.get(target, None) is None:
        costs[target] = float("inf")
    return costs

def init_parents(graph, start, target)：
    parents = {}
    for node in range graph[start].keys():
        parents[node] = start
    if parents.get(target, None) is None:
        parents[target] = None
    return parents


# 啊哈 P152
def warshal():
    for k in range(k):
        for i in range(n):
            for j in range(n):
                if e[i][j] > e[i][k] + e[k][j]:
                    e[i][j] = e[i][k] + e[k][j]


# Bellman-Ford 解决负权边  啊哈 P163  优化队列P171  对比P177
def bellman():
    for k in range(n-1):
        for i in range(m):
            if dis[v[i]] > dis[u[i]] + w[i]:
                dis[v[i]] = dis[u[i]] + w[i]