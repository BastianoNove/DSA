from node import Node

def make_graph(edges):
    graph = dict()
    vertices = []
    for u, v in edges:
        vertices.append(u)
        vertices.append(v)
    vertices = list(set(vertices))
    for v in vertices:
        graph[v] = Node(v)

    for u,v in edges:
        graph[u].edges.append(graph[v])

    return graph