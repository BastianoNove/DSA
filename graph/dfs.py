from node import Node
import graph

def dfs(node, visited=[]):
    if node in visited:
        return
    visited.append(node)
    for v in node.edges:
        if v not in visited:
          dfs(v, visited)
    print(node.key)

g = graph.make_graph([('y','z'), ('a','b'), ('a', 'd'),  ('b', 'c'), ('c', 'd'), ('b', 'y'), ('c', 'a'), ('d', 'y'), ])
dfs(g.vertices['a'])

