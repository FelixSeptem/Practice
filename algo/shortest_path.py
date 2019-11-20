# -*- coding:utf-8 -*-
class Graph:
    def __init__(self, vertex_count: int) -> None:
        self.adj = [[] for _ in range(vertex_count)]

    def add_edge(self, s: int, t: int, w: int) -> None:
        edge = Edge(s, t, w)
        self.adj[s].append(edge)

    def __len__(self) -> int:
        return len(self.adj)


class Vertex:
    def __init__(self, v: int, dist: int) -> None:
        self.id = v
        self.dist = dist

    def __gt__(self, other) -> bool:
        return self.dist > other.dist

    def __repr__(self) -> str:
        return str((self.id, self.dist))


class Edge:
    def __init__(self, source: int, target: int, weight: int) -> None:
        self.s = source
        self.t = target
        self.w = weight


class VertexPriorityQueue:
    def __init__(self) -> None:
        self.vertices = []

    def get(self) -> Vertex:
        return heapq.heappop(self.vertices)

    def put(self, v: Vertex) -> None:
        self.vertices.append(v)
        self.update_priority()

    def empty(self) -> bool:
        return len(self.vertices) == 0

    def update_priority(self) -> None:
        heapq.heapify(self.vertices)

    def __repr__(self) -> str:
        return str(self.vertices)


def dijkstra(g: Graph, s: int, t: int) -> int:
    size = len(g)

    pq = VertexPriorityQueue()  # 节点队列
    in_queue = [False] * size   # 已入队标记
    vertices = [                # 需要随时更新离s的最短距离的节点列表
        Vertex(v, float('inf')) for v in range(size)
    ]
    predecessor = [-1] * size   # 先驱

    vertices[s].dist = 0
    pq.put(vertices[s])
    in_queue[s] = True

    while not pq.empty():
        v = pq.get()
        if v.id == t:
            break
        for edge in g.adj[v.id]:
            if v.dist + edge.w < vertices[edge.t].dist:
                # 当修改了pq中的元素的优先级后：
                # 1. 有入队操作：触发了pq的堆化，此后出队可以取到优先级最高的顶点
                # 2. 无入队操作：此后出队取到的顶点可能不是优先级最高的，会有bug
                # 为确保正确，需要手动更新一次
                vertices[edge.t].dist = v.dist + edge.w
                predecessor[edge.t] = v.id
                pq.update_priority()        # 更新堆结构
            if not in_queue[edge.t]:
                pq.put(vertices[edge.t])
                in_queue[edge.t] = True

    for n in print_path(s, t, predecessor):
        if n == t:
            print(t)
        else:
            print(n, end=' -> ')
    return vertices[t].dist


def print_path(s: int, t: int, p: List[int]) -> Generator[int, None, None]:
    if t == s:
        yield s
    else:
        yield from print_path(s, p[t], p)
        yield t

from queue import PriorityQueue

@dataclass
class Edge:
    start_id: int
    end_id: int
    weight: int

@dataclass(order=True)
class Vertex:
    distance_to_start = float("inf")
    vertex_id: int

class Graph:
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]
    
    def add_edge(self, from_vertex: int, to_vertex: int, weight: int) -> None:
        self._adjacency[from_vertex].append(Edge(from_vertex, to_vertex, weight))

    def dijkstra(self, from_vertex: int, to_vertex: int) -> None:
        vertices = [Vertex(i) for i in range(self._num_vertices)]
        vertices[from_vertex].distance_to_start = 0
        visited = [False] * self._num_vertices
        predecessor = [-1] * self._num_vertices
        q = PriorityQueue()
        q.put(vertices[from_vertex])
        visited[from_vertex] = True
        while not q.empty():
            min_vertex = q.get()
            if min_vertex.vertex_id == to_vertex:
                break
            for edge in self._adjacency[min_vertex.vertex_id]:
                next_vertex = vertices[edge.end_id]
                if min_vertex.distance_to_start + edge.weight < next_vertex.distance_to_start:
                    next_vertex.distance_to_start = min_vertex.distance_to_start + edge.weight
                    predecessor[next_vertex.vertex_id] = min_vertex.vertex_id
                    if not visited[next_vertex.vertex_id]:
                        q.put(next_vertex)
                        visited[next_vertex.vertex_id] = True
            
        path = lambda x: path(predecessor[x]) + [str(x)] if from_vertex != x else [str(from_vertex)]
        print("->".join(path(to_vertex)))