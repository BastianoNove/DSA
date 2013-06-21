from collections import defaultdict
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

def weights(edges, value = float('inf')):
    '''Returns a defaultdict and initializes all non-existing edges
       to value'''
    w = defaultdict(lambda: value)
    for u, v in edges.items():
        w[(u, v)] = val
    return w
    
def init_single_source(graph, source):
    for _, vertex in graph.iteritems():
        vertex.d = float('inf')
        vertex.predecesor = None
    source.d = 0

def relax(u, v, w):
    if v.d > (u.d + w[(u.key, v.key)]):
        v.d = u.d + w[(u.key, v.key)]
        v.predecesor = u

