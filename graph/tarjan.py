"""Tarjan's Algorithm. Finds the strongly connected components in a graph"""

import graph as graph_utils

INDEX = 0
STACK = 1
COMPONENTS = 2

def tarjans(graph):
    index = 0
    stack = []
    components = []
    state = [index, stack, components] 

    for vertex in graph.vertices:
        # augment vertices with index and lowlink 
        setattr(graph.vertices[vertex], 'indx', -1)
        setattr(graph.vertices[vertex], 'lowlink', -1)

    for vertex in graph.vertices:
        vertex = graph.vertices[vertex]
        if vertex.indx == -1:
            strongconnect(vertex, state)
    return state[COMPONENTS]

def strongconnect(vertex, state):
    vertex.indx = state[INDEX] 
    vertex.lowlink = state[INDEX]
    state[INDEX] = state[INDEX] + 1
    state[STACK].append(vertex)


    for neighbor in vertex.edges:
        if neighbor.indx  == -1:
            strongconnect(neighbor, state)
            vertex.lowlink = min(vertex.lowlink, neighbor.lowlink)
        elif neighbor in state[STACK]:
            vertex.lowlink = min(vertex.lowlink, neighbor.indx)

    if vertex.lowlink == vertex.indx:
        # start new strongly connected component
        component = []
        while True:
            w = state[STACK].pop()
            component.append(w)
            if w == vertex:
                break
        state[COMPONENTS].append(component)

def print_components(components):
    for component in components:
        print('component: {}'.format([vertex.key for vertex in component]))

def test():
    graph = graph_utils.make_graph([(1,2), (2,3), (3, 4), (3,5), (4,6), (5,7), (6,3),
                                    (7,6), (7,3)])
    print('first test: ') 
    sccs = tarjans(graph)
    print_components(sccs)
    graph = graph_utils.make_graph([(1,2), (2,4), (4,3), (3,1), (5,3), (5,4), (5,6), (6,7),
                                    (7,5), (9,8), (8, 10), (10,9), (10,11), (11,10),
                                    (12,13), (11,13)])
    print('second test: ') 
    sccs = tarjans(graph)
    print_components(sccs)

if __name__ == '__main__':
    test()


            
        

