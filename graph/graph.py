from node import Node 

def make_graph(edges):
    graph = dict()
    vertices = []
    for u, v in edges:
        vertices.append(u)
        vertices.append(v)
    vertices = list(set(vertices))
    for v in vertices:
        to_insert = Node(v)
        graph[v] = to_insert 

    for u,v in edges:
        graph[u].edges.append(graph[v])

    return graph
