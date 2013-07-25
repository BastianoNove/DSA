from node import Node
from collections import deque
import graph

def bfs(node):
    queue = deque([node])
    visited = []
    while queue:
        v = queue.popleft()
        visited.append(v)
        print(v.key)
        for vertex in v.edges:
            if vertex not in visited and vertex not in queue:
                queue.append(vertex)

g = graph.make_graph([('y','z'), ('a','b'), ('a', 'd'),  ('b', 'c'), ('c', 'd'), ('b', 'y'), ('c', 'a'), ('d', 'y'), ])
bfs(g.vertices['a'])
