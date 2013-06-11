#!/usr/bin/env python

from collections import defaultdict 

def make_graph(edges):
  vertices = set(u for u,v in edges)
  graph = defaultdict(list)
  for u,v in edges:
    graph[u].append(v)
  return graph 
  
def topsort(graph):
  output = []
  outgoing_vertices = graph.keys()
  incoming_vertices = []
  for edge, vertices in graph.items():
    if len(vertices) == 1:
      if edge == vertices[0]:
        continue
    incoming_vertices += vertices
  incoming_vertices = list(set(incoming_vertices))
  start = list(set(outgoing_vertices)-set(incoming_vertices))
  stack = [] + start
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

graph = make_graph([('a','b'), ('a','d'), ('b','c'), ('c','d'),
         ('d', 'e'), ('c', 'e'), ('f','f')])

print topsort(graph)
