#!/usr/bin/env python

from collections import defaultdict
import graph as graph_utils
import dfs

def make_graph(edges):
  graph = defaultdict(list)
  for u,v in edges:
    graph[u].append(v)
  return graph

def topsort(graph):
  output = []
  all_edges = list(set(pair for pair in graph.edges if pair[0] != pair[1]))
  incoming_edges = set(pair[1] for pair in graph.edges if pair[0]!=pair[1])
  indegree_zero = [graph.vertices[item] for item in (set(graph.vertices.keys())-incoming_edges)]
  while indegree_zero:
    current_vertex = indegree_zero.pop()
    e_neighbors = [vertex for vertex in current_vertex.edges if vertex!=current_vertex]
    output.append(current_vertex)
    for vertex in e_neighbors:
      all_edges.remove((current_vertex.key, vertex.key))
      for u,v in all_edges:
          if v == vertex.key:
              break
      else:
          indegree_zero.append(vertex)
  if all_edges:
      print('Graph contains cycle')
      print(all_edges)
      return None
  return output

def topsort_dfs(graph):
    sorted_stack = []
    visited = []
    visit = topsort_visit(sorted_stack) 
    for k, v in graph.vertices.items():
        if v not in visited:
            dfs.dfs(v, visited, visit)
    sorted_stack.reverse()
    return sorted_stack 

def topsort_visit(vset=None):
    if vset is None:
        vset = []
    def visit(x):
        vset.append(x)
    return visit

def test():
  graph = graph_utils.make_graph([('a','b'), ('a','d'), ('b','c'), ('c','d'),
                      ('d', 'e'), ('c', 'e'), ('f','f')])
  print([node.key for node in topsort(graph)])
  graph = graph_utils.make_graph([(7,11), (5,11), (7,8), (3,8), (3,10), (11,2), (11,9), (11,10), (8,9)])
  print([node.key for node in topsort(graph)])
  graph = graph_utils.make_graph([('g','h'), ('a', 'h'), ('a', 'b'), ('b', 'c'), ('c', 'f'), ('d', 'c'), ('d', 'e'),
                    ('e', 'f'), ('i', 'i')])
  print([node.key for node in topsort_dfs(graph)])
  #graph = graph_utils.make_graph([(1,2), (2,3), (3,1)])
  #print([node.key for node in topsort(graph)])
test()
