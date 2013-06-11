#!/usr/bin/env python

from collections import defaultdict 

def make_graph(edges):
  graph = defaultdict(list)
  for u,v in edges:
    graph[u].append(v)
  return graph 
  
def topsort(graph):
  output = []
  incoming_vertices = []
  for edge, vertices in graph.items():
    if len(vertices) == 1:
      if edge == vertices[0]:
        continue
    incoming_vertices += vertices
  incoming_vertices = list(set(incoming_vertices))
  stack = list(set(graph.keys())-set(incoming_vertices))
  while stack:
    e = stack[-1]
    edges = [edge for edge in graph[e] if edge!=e]
    if not edges:
      stack = stack[:-1]
      output.append(e)
    else:
      for edge in edges:
        if edge not in output:
          stack.append(edge)
      del(graph[e]) 
  output.reverse()
  return output


def test():
  graph = make_graph([('a','b'), ('a','d'), ('b','c'), ('c','d'),
                      ('d', 'e'), ('c', 'e'), ('f','f')])
  print topsort(graph)
  graph = make_graph([(7,11), (5,11), (7,8), (3,8), (3,10), (11,2), (11,9), (11,10), (8,9)]) 
  print topsort(graph)
  graph = make_graph([('g','h'), ('a', 'h'), ('a', 'b'), ('b', 'c'), ('c', 'f'), ('d', 'c'), ('d', 'e'),
                    ('e', 'f'), ('i', 'i')]) 
  print topsort(graph)

test()
