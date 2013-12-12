import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Iterator;
import java.util.NoSuchElementException;

class Dfs implements Iterator<Vertex> {
  private Vertex currentVertex;
  private Deque<Vertex> stack;
  private Graph graph;
  private HashSet<Vertex> seen;

  public Dfs(Graph g, Vertex source) {
    graph = g;
    currentVertex = source;
    seen = new HashSet<Vertex>();
    stack = new ArrayDeque<Vertex>();
    stack.push(source);
  }

  public boolean hasNext() {
    return !stack.isEmpty();
  }
  
  public Vertex next() throws NoSuchElementException {
    Vertex head =  stack.pop();
    EdgeNode edge;
    Vertex from, to;
    for(int i = 0; i < head.edges.size(); i++) {
      edge = head.edges.get(i);
      from = graph.vertices.get(edge.from);
      to = graph.vertices.get(edge.to);

      if (head == from) {
        if (!seen.contains(to)) {
          stack.push(to);
          seen.add(to);
        }
      }
      else {
        if (!seen.contains(from)) {
          stack.push(from);
          seen.add(from);
        }
      }
    }
    seen.add(head);
    return head;
  }
  
  public void remove() {}
}
