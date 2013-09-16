from node import Node
from collections import deque
import graph

def bfs(node, visit=None):
    if visit is None:
        visit = print
    queue = deque([node])
    visited = {}
    while queue:
        v = queue.popleft()
        visited[v] = True
        visit(v)
        for vertex in v.edges:
            if vertex not in visited and vertex not in queue:
                queue.append(vertex)

def bfs_2(s):
    level = {s : 0}
    parent = {s : None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in u.edges:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    return (level, parent)

if __name__ == '__main__':
    g = graph.make_graph([('y','z'), ('a','b'), ('a', 'd'),  ('b', 'c'), ('c', 'd'), ('b', 'y'), ('c', 'a'), ('d', 'y'), ])
    bfs(g.vertices['a'])
    g = graph.make_graph([('y','z'), ('a','b'), ('a', 'd'),  ('b', 'c'), ('c', 'd'), ('b', 'y'), ('c', 'a'), ('d', 'y'), ])
    level , parent = bfs_2(g.vertices['a'])
    print(level)
    print(parent)

