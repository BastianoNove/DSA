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

def test():
    graph = graph_utils.make_graph([(1,2), (2,3), (3, 4), (3,5), (4,6), (5,7), (6,3),
                                    (7,6), (7,3)])
    sccs = tarjans(graph)
    for component in sccs:
        print('component: {}'.format([vertex.key for vertex in component]))

if __name__ == '__main__':
    test()


            
        

