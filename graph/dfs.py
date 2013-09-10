from node import Node
import graph

def dfs(node, visited=None, visit=None):
    if visit is None:
        visit = print
    if visited is None:
        visited = []
    if node in visited:
        return
    visited.append(node)
    for v in node.edges:
        if v not in visited:
          dfs(v, visited, visit)
    visit(node.key)

if __name__ == '__main__':
    g = graph.make_graph([('y','z'), ('a','b'), ('a', 'd'),  ('b', 'c'), ('c', 'd'), ('b', 'y'), ('c', 'a'), ('d', 'y'), ])
    dfs(g.vertices['a'])

