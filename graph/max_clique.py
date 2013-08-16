import graph as graph_utils

def max_clique(graph):
    degree = []
    for vertex in graph.vertices.values():
        degree.append((vertex, len(vertex.edges)))
    sorted_degree = sorted(degree, key=lambda x: x[1], reverse=True)
    V = [vertex[0] for vertex in sorted_degree]
    cliques = []
    for vertex in V:
        clique = [vertex]
        for v in V:
            if vertex == v:
                continue
            if check_clique(clique, v):
                clique.append(v)
        if len(clique) > 1:
            cliques.append(clique)
    return [] if not cliques else max(cliques, key=len)


def check_clique(clique, node):
    for vertex in clique:
        if node not in vertex.edges or vertex not in node.edges:
            return False
    return True

def test():
    edges = [('b', 'a'), ('c', 'b'), ('d', 'c'), ('e', 'd'), ('a', 'e'), ('g', 'a'),
             ('g', 'b'), ('h', 'b'), ('h', 'f'), ('h', 'g'), ('a', 'b'), ('b', 'c'),
             ('c', 'd'), ('d', 'e'), ('e', 'a'), ('a', 'g'), ('b', 'g'), ('b', 'h'),
             ('f', 'h'), ('g', 'h'), ('h', 'i'), ('i', 'h'), ('g', 'i'), ('i', 'g'),
             ('f', 'i'), ('i', 'f'), ('g', 'f'), ('f', 'g'), ('c', 'h'), ('h', 'c'),
             ('d', 'f'), ('f', 'd'), ('i', 'e'), ('e', 'i')]
    graph = graph_utils.make_graph(edges)
    clique = max_clique(graph)
    print([v.key for v in clique])


if __name__ == '__main__':
    test()


