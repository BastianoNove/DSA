class Main {
  public static void main(String args[]) {
    Graph g = new Graph(10);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(2, 5);
    g.addEdge(2, 4);
    g.addEdge(3, 6);
    g.addEdge(1, 7);
    g.addEdge(5, 7);
    g.addEdge(6, 8);
    g.addEdge(3, 8);
    g.addEdge(4, 9);
    g.addEdge(8, 9);

    Bfs iter = new Bfs(g, g.vertices.get(1));
    //Dfs iter = new Dfs(g, g.vertices.get(1));
    Vertex current;
    while (iter.hasNext()) {
      current = iter.next();
      System.out.printf("Visiting vertex %d.\n", current.key);
    }
  }
}
 
