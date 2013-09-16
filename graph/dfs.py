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
    visit(node)

parent = {}
def dfs_2(g):
    for s in g.vertices.values():
        if s not in parent or parent[s] is None:
            parent[s] = None
            s.predecessor = None
            dfs_visit(s, g)

def dfs_visit(s, g):
    for v in s.edges:
        if v not in parent or parent[v] is None:
            parent[v] = s
            v.predecessor= s
            dfs_visit(v, g)

if __name__ == '__main__':
    g = graph.make_graph([('y','z'), ('a','b'), ('a', 'd'),  ('b', 'c'), ('c', 'd'), ('b', 'y'), ('c', 'a'), ('d', 'y'), ])
    dfs(g.vertices['a'])

    g = graph.make_graph([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'),
                          ('e', 'f'), ('f', 'g'), ('g', 'c')])
    dfs_2(g)
    for vertex in g.vertices.items():
        print(vertex)
