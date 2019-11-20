# -*- coding:utf-8 -*-
class Undigraph(object):

    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, s, t):
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_tbl[s].append(t)
        self.adj_tbl[t].append(s)
        return True
    
    def __len__(self):
        return self.v_num

    def __getitem__(self, ind):
        if ind > self.v_num:
            raise IndexError("No Such Vertex!")
        return self.adj_tbl[ind]

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)


def find_vertex_by_degree(graph, s, degree):
    if len(graph) <= 1:
        return []
    if degree == 0:
        return [s]
    d_vertices = []
    queue = deque()
    prev = [-1] * len(graph)
    visited = [False] * len(graph)
    visited[s] = True
    queue.append(s)
    while len(queue) > 0:
        sz = len(queue)
        for i in range(sz):
            v = queue.popleft()
            for adj_v in graph[v]:
                if not visited[adj_v]:
                    prev[adj_v] = v
                    visited[adj_v] = True
                    queue.append(adj_v)
        degree -= 1
        if degree == 0 and len(queue) != 0:
            return queue 



class Digraph(object):

    def __init__(self, vertex_num):
        self.v_num = vertex_num
        self.adj_tbl = []
        for i in range(self.v_num + 1):
            self.adj_tbl.append([])
    
    def add_edge(self, frm, to):
        if frm > self.v_num or to > self.v_num:
            return False
        self.adj_tbl[frm].append(to)

    def __len__(self):
        return self.v_num

    def __getitem__(self, ind):
        if ind > self.v_num:
            raise IndexError("No such vertex!")
        return self.ajd_tbl[ind]

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)

class Graph:
    """Undirected graph."""
    def __init__(self, num_vertices):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]

    def add_edge(self, s, t):
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s, t, prev):
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s, t):
        """Print out the path from Vertex s to Vertex t
        using bfs.
        """
        if s == t: return

        visited = [False] * self._num_vertices
        visited[s] = True
        q = deque()
        q.append(s)
        prev = [None] * self._num_vertices

        while q:
            v = q.popleft()
            for neighbour in self._adjacency[v]:
                if not visited[neighbour]:
                    prev[neighbour] = v
                    if neighbour == t:
                        print("->".join(self._generate_path(s, t, prev)))
                        return
                    visited[neighbour] = True
                    q.append(neighbour)

    def dfs(self, s, t):
        """Print out a path from Vertex s to Vertex t
        using dfs.
        """
        found = False
        visited = [False] * self._num_vertices
        prev = [None] * self._num_vertices

        def _dfs(from_vertex: int) -> None:
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self._adjacency[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)
        
        _dfs(s)
        print("->".join(self._generate_path(s, t, prev)))