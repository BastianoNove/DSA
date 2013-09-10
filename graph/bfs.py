from node import Node
from collections import deque
import graph

def bfs(node, visit=None):
    if visit is None:
        visit = print
    queue = deque([node])
    visited = []
    while queue:
        v = queue.popleft()
        visited.append(v)
        visit(v)
        for vertex in v.edges:
            if vertex not in visited and vertex not in queue:
                queue.append(vertex)

if __name__ == '__main__':
    g = graph.make_graph([('y','z'), ('a','b'), ('a', 'd'),  ('b', 'c'), ('c', 'd'), ('b', 'y'), ('c', 'a'), ('d', 'y'), ])
    bfs(g.vertices['a'])
