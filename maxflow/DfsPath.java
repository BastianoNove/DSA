import java.util.ArrayList;
import java.util.HashSet;

class DfsPath {
    public static ArrayList<EdgeNode> Dfs(Graph g, Vertex source, Vertex target,
            ArrayList<EdgeNode> path, HashSet<Vertex> seen) {
        ArrayList<EdgeNode> pathFound;
        Vertex vertexTo;
        int residualCapacity;
        if (seen.contains(source)) {
            return null;
        }
        seen.add(source);

        if (source == target) {
            return path;
        }

        for(EdgeNode edge : source.edges) {
            residualCapacity = edge.capacity - edge.flow;
            if (residualCapacity > 0 ) {
                path.add(edge);
                vertexTo = g.vertices.get(edge.to);
                pathFound = Dfs(g, vertexTo, target, path, seen);
                if (pathFound != null) {
                    return path;
                }
                path.remove(path.size()-1);
           }
        }

        return null;
    }
}
