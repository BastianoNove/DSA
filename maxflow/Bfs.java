import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.NoSuchElementException;

class Bfs implements Iterator<Vertex> {
  private Vertex currentVertex;
  private Queue<Vertex> queue;
  private Graph graph;
  private HashSet<Vertex> seen;

  public Bfs(Graph g, Vertex source) {
    graph = g;
    currentVertex = source;
    seen = new HashSet<Vertex>();
    queue = new LinkedList<Vertex>();
    queue.offer(source);
  }

  public boolean hasNext() {
    return !queue.isEmpty();
  }
  
  public Vertex next() throws NoSuchElementException {
    Vertex head =  queue.poll();
    EdgeNode edge;
    Vertex from, to;
    for(int i = 0; i < head.edges.size(); i++) {
      edge = head.edges.get(i);
      from = graph.vertices.get(edge.from);
      to = graph.vertices.get(edge.to);

      if (head == from) {
        if (!seen.contains(to)) {
          queue.offer(to);
          seen.add(to);
        }
      }
      else {
        if (!seen.contains(from)) {
          queue.offer(from);
          seen.add(to);
        }
      }
    }
    seen.add(head);
    return head;
  }
  
  public void remove() {}
}
