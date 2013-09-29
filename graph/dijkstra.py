from collections import defaultdict
import graph as graph_utils
import heapq

def dijkstra_2(graph, costs, start_vertex):
    current_node = graph.vertices[start_vertex.key]
    graph_utils.init_single_source(graph, current_node)
    unvisited = set(graph.vertices[vertex] for vertex in graph.vertices)
    while current_node:
        neighbors = [vertex for vertex in current_node.edges
                     if vertex in unvisited]
        for neighbor in neighbors:
            if (current_node.d + costs[(current_node.key, neighbor.key)]) < neighbor.d:
                neighbor.d = current_node.d + costs[(current_node.key, neighbor.key)]
        unvisited.remove(current_node)
        if not unvisited:
            break
        min_node = min(unvisited, key=lambda x: x.d)
        current_node = min_node if min_node.d != float('inf')  and min_node in unvisited else None

def dijkstra(graph, weights, start_vertex):
    graph_utils.init_single_source(graph, start_vertex)
    queue = [vertex for vertex in graph.vertices.values()] # vertices to process
    heapq.heapify(queue)
    s = [] # set of vertices with shortest path already determined
    while queue:
        u = heapq.heappop(queue) # extract min
        s.append(u)
        for v in u.edges:
            graph_utils.relax(u, v, weights)

def test():
    cost = { (1,2) : 7, (1,3) : 9, (1,6) : 14, (2,4) : 15,
             (2,3) : 10, (6,3) : 2, (6,5) : 9, (3, 4) : 11,
             (5,4) : 6 }
    cost = graph_utils.weights(cost)
    g = graph_utils.make_graph(cost.keys())
    dijkstra(g, cost, g.vertices[1])
    for vertex in g.vertices.values():
        print(vertex)

if __name__ == '__main__':
    test()
