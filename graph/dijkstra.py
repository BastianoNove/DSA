from collections import defaultdict
import graph


def dijkstra(graph, costs):
    pass

def test():
    _cost = { (1,2) : 7, (1,3) : 9, (1,6) : 14, (2,4) : 15,
             (2,3) : 10, (6,3) : 2, (6,5) : 9, (3, 4) : 11,
             (5,4) : 6 }
    cost = defaultdict(lambda : float('inf'))
    for key, value in _cost.items():
        cost[key] = value
    g = graph.make_graph(cost.keys())
    #dijkstra(g, cost)

test()
