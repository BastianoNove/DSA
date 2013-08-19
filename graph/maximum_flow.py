
from collections import defaultdict
from collections import deque
import graph as graph_utils

class Edge(object):
    def __init__(self, u, v, c = 0, f = 0):
        self.u = u
        self.v = v
        self.c = c # capacity
        self.f = f # flow

def ford_fulkerson(vertices, edges, source, sink):
    """Ford-Fulkerson algorithm"""

    # Add potentially missing edges
    reverse_edges = []
    for edge in edges.values():
        if (edge.v, edge.u) not in edges:
            reverse_edges.append(Edge(edge.v, edge.u))
    for edge in reverse_edges:
        edges[(edge.u, edge.v)] = edge

    path = find_path_residual_network(vertices, edges, source, sink)
    #print('path found: ', path)
    while path:
        print('iteration')
        cf_path = min(path, key=lambda edge: edge.c)
        for edge in path:
            if (edge.u, edge.v) in edges:
                #print('updating edge: {},{}. f {}'.format(edge.u, edge.v, edge.f))
                edge.f = edge.f + cf_path.c
            else:
                edges[(edge.v, edge.u)].f = edges[(edge.v, edge.u)].f - cf_path.c
        path = find_path_residual_network(vertices, edges, source, sink)

def find_path_residual_network(vertices, edges, source, sink):
    """Finds path in residual network. Returns an iterable containing edges in the path"""
    #return dfs(vertices, edges, source, sink, [])
    return bfs(vertices, edges, deque([source]), sink, [])

def dfs(vertices, edges, source, sink, visited, path = None):
    if path is None:
        path = []
    if source == sink:
        #print('returning path')
        #print('path found: ')
        #for edge in path:
        #    print('({}, {}) c: {} f: {}'.format(edge.u, edge.v, edge.c, edge.f), end=", ")
        return path
    #print('source is : ', source)
    visited.append(source)
    for neighbor in source.edges:
        #print('neighbor: ', neighbor)
        if neighbor not in visited:
            #print('neighbor not visited')
            edge = edges[(source.key, neighbor.key)]
            if edge.c - edge.f > 0:
                #print('neighbor has residual capacity')
                new_path = path + [edges[source.key, neighbor.key]]
                p = dfs(vertices, edges, neighbor, sink, visited, new_path)
                if p is None:
                    #print('could not find path')
                    continue
                else:
                    #print('found path!')
                    return p
    return None

def bfs(vertices, edges, queue, sink, visited, path = None):
    if path is None:
        path = []
    source = queue.popleft()
    if source == sink:
        return path
    for neighbor in source.edges:
        if neighbor not in visited:
            edge = edges[(source.key, neighbor.key)]
            if edge.c - edge.f > 0:
                #print('neighbor has residual capacity')
                new_path = path + [edges[source.key, neighbor.key]]
                p = dfs(vertices, edges, neighbor, sink, visited, new_path)
                if p is None:
                    #print('could not find path')
                    continue
                else:
                    #print('found path!')
                    return p
    return None

def print_edges(edges):
    for edge in edges.values():
        print('Edge ({}, {})  c: {}   f:{}'.format(edge.u, edge.v, edge.c, edge.f))

def test():
    edges = {('s', 'v1') : Edge('s', 'v1', 16),
            ('v1', 'v3') : Edge('v1', 'v3', 12),
            ('s', 'v2')  : Edge('s', 'v2', 13),
            ('v2', 'v1') : Edge('v2', 'v1', 4),
            ('v3', 'v2') : Edge('v3', 'v2', 9),
            ('v2', 'v4') : Edge('v2', 'v4', 14),
            ('v4', 't')  : Edge('v4', 't', 4),
            ('v4', 'v3') : Edge('v4', 'v3', 7),
            ('v3', 't')  : Edge('v3', 't', 20)}
    g = graph_utils.make_graph(edges.keys())
    source = g.vertices['s']
    sink = g.vertices['t']
    print_edges(edges)
    print('After Ford-Fulkerson')
    ford_fulkerson(g.vertices, edges, source, sink)
    print_edges(edges)

if __name__ == '__main__':
    test()
