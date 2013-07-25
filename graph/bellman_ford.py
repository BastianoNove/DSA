import graph

def bellman_ford(g, w, s):
    graph.init_single_source(g, s)
    for i in range(1, len(g.keys())):
        for u,v in graph.edges:
            graph.relax(graph.vertices[u], graph.vertices[v], w)
    for u,v in graph.edges:
        if graph.vertices[v].d > graph.vertices[u].d + w[(u,v)]:
            return False
    return True

def test():
    w = { (1,2) : 7, (1,3) : 9, (1,6) : 14, (2,4) : 15,
             (2,3) : 10, (6,3) : 2, (6,5) : 9, (3, 4) : 11,
             (5,4) : 6 }
    w = graph.weights(w)
    g = graph.make_graph(w.keys())
    print(bellman_ford(g, w, g.vertices[1]))
    print('tests pass')

test()
