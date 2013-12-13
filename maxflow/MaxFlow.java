import java.util.ArrayList;
import java.util.HashSet;

class MaxFlow {
  public static void main(String args[]) {
  }

  public static int maxFlow(Graph g, Vertex source, Vertex target) {
      ArrayList<EdgeNode> path;
      int minResidual;
      path = DfsPath.Dfs(g, source, target, new ArrayList<EdgeNode>(),
              new HashSet<Vertex>());
      while (path != null) {
         minResidual = findMinResidual(path);
         for (EdgeNode edge : path) {
             if (g.edges.containsKey(edge)) {
                 edge.flow = edge.flow + minResidual;
             }
             else {
                 edge.reverse.flow = edge.reverse.flow - minResidual;
             }
         }
         path = DfsPath.Dfs(g, source, target, new ArrayList<EdgeNode>(),
                 new HashSet<Vertex>());
      }
      return vertexFlow(target);
  }

  public static int findMinResidual(ArrayList<EdgeNode> path) {
      int minResidual;
      if (path.size() < 1) {
          return 0;
      }
      EdgeNode firstEdge = path.get(0);
      minResidual = firstEdge.capacity - firstEdge.flow;

      for (EdgeNode edge : path) {
          if (edge.capacity - edge.flow < minResidual) {
              minResidual = edge.capacity - edge.flow;
          }
      }
      return minResidual;
  }

  public static int vertexFlow(Vertex vertex) {
      int flow = 0;
      for (EdgeNode edge : vertex.edges) {
          if (edge.reverse != null) {
              flow += edge.flow;
          }
      }
      return flow;
  }
}
