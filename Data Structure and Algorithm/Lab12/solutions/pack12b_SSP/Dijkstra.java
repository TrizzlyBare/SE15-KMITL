package solutions.pack12b_SSP;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Dijkstra {

    int[][] adjMatrix;
    int[] previous, distance;
    boolean[] visited;
    int source;

    public Dijkstra(int[][] adjMatrix, int source) {
        this.adjMatrix = adjMatrix;
        this.source = source;
        previous = new int[adjMatrix.length];
        distance = new int[adjMatrix.length];
        visited = new boolean[adjMatrix.length];
    }

    //Task 1 imeplement the findSSP method using Dijkstra's algorithm
    public void findSSP() {
        int n = adjMatrix.length;
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[source] = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(node -> distance[node]));
        pq.add(source);

        while (!pq.isEmpty()) {
            int u = pq.poll();
            if (visited[u]) {
                continue;
            }
            visited[u] = true;

            for (int v = 0; v < n; v++) {
                if (adjMatrix[u][v] != -1 && !visited[v]) {
                    int newDist = distance[u] + adjMatrix[u][v];
                    if (newDist < distance[v]) {
                        distance[v] = newDist;
                        previous[v] = u;
                        pq.add(v);
                    }
                }
            }
        }
        for (int i = 0; i < distance.length; i++) {
            System.out.println("Distance from node " + source + " to node " + i + " is " + distance[i]);
        }
    }

    //Task 2 implement the printAllSSP method to print the shortest path 
    //from the source to all other nodes
    public void printAllSSP() {
        for (int i = 0; i < distance.length; i++) {
            System.out.println("Shortest path from " + source + " to " + i + " is " + getPath(i));
            System.out.println("with a distance of " + distance[i]);
            System.out.println();
        }
    }

    private String getPath(int node) {
        StringBuilder path = new StringBuilder();
        while (node != source) {
            path.insert(0, " -> " + node);
            node = previous[node];
        }
        path.insert(0, source);
        return path.toString();
    }
}
