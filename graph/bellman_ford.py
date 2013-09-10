import graph

def bellman_ford(g, w, s):
    graph.init_single_source(g, s)
    for i in range(1, len(g.vertices)):
        for u,v in g.edges:
            graph.relax(g.vertices[u], g.vertices[v], w)
    for u,v in g.edges:
        if g.vertices[v].d > g.vertices[u].d + w[(u,v)]:
            return False
    return True

def test():
    w = { (1,2) : 7, (1,3) : 9, (1,6) : 14, (2,4) : 15,
             (2,3) : 10, (6,3) : 2, (6,5) : 9, (3, 4) : 11,
             (5,4) : 6 }
    weights = graph.weights(w)
    g = graph.make_graph(w.keys())
    bellman_ford(g, weights, g.vertices[1])
    assert(g.vertices[1].d == 0)
    assert(g.vertices[2].d == 7)
    assert(g.vertices[3].d == 9)
    assert(g.vertices[4].d == 20)
    assert(g.vertices[5].d == 23)
    assert(g.vertices[6].d == 14)
    print('test passes')

if __name__ == '__main__':
    test()
