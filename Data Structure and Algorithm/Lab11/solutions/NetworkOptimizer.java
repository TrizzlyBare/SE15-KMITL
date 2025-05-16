package solutions;

import java.util.PriorityQueue;

public class NetworkOptimizer {

    public int optimizeNetwork(int N, int M, int[][] input) {
        int totalLatency = 0;

        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            nodes[i] = new Node(i + 1);
        }

        for (int i = 0; i < input.length; i++) {
            int node1Id = input[i][0];
            int node2Id = input[i][1];
            int latency = input[i][2];
            Edge edge = new Edge(latency, nodes[node1Id - 1], nodes[node2Id - 1]);
            nodes[node1Id - 1].addEdge(edge);
            nodes[node2Id - 1].addEdge(edge);
        }

        boolean[] inMST = new boolean[N];
        PriorityQueue<Edge> pq = new PriorityQueue<>(new EdgeComparator());

        inMST[0] = true;
        for (Edge edge : nodes[0].getEdges()) {
            pq.add(edge);
        }

        int edgesUsed = 0;

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            Node u = edge.getNode1();
            Node v = edge.getNode2();

            if (inMST[u.getId() - 1] && inMST[v.getId() - 1]) {
                continue;
            }

            totalLatency += edge.getLatency();
            edgesUsed++;

            Node newNode = inMST[u.getId() - 1] ? v : u;
            inMST[newNode.getId() - 1] = true;

            for (Edge nextEdge : newNode.getEdges()) {
                if (!inMST[nextEdge.getNode1().getId() - 1] || !inMST[nextEdge.getNode2().getId() - 1]) {
                    pq.add(nextEdge);
                }
            }
        }

        if (edgesUsed != N - 1) {
            return -1;
        }

        return totalLatency;
    }

    public int optimizeNetwork(int N, int M, int T, int[][] input) {
        int totalLatency = 0;

        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            nodes[i] = new Node(i + 1);
        }

        for (int i = 0; i < input.length; i++) {
            int node1Id = input[i][0];
            int node2Id = input[i][1];
            int latency = input[i][2];
            int bandwidth = input[i][3];
            if (bandwidth >= T) {
                EdgeWithBandwidth edge = new EdgeWithBandwidth(latency, bandwidth, nodes[node1Id - 1], nodes[node2Id - 1]);
                nodes[node1Id - 1].addEdgeWithBandwidth(edge);
                nodes[node2Id - 1].addEdgeWithBandwidth(edge);
            }
        }

        boolean[] inMST = new boolean[N];
        PriorityQueue<EdgeWithBandwidth> pq = new PriorityQueue<>(new EdgeComparator());

        inMST[0] = true;
        for (EdgeWithBandwidth edge : nodes[0].getEdgesWithBandwidth()) {
            pq.add(edge);
        }

        int edgesUsed = 0;

        while (!pq.isEmpty()) {
            EdgeWithBandwidth edge = pq.poll();
            Node u = edge.getNode1();
            Node v = edge.getNode2();

            if (inMST[u.getId() - 1] && inMST[v.getId() - 1]) {
                continue;
            }

            totalLatency += edge.getLatency();
            edgesUsed++;

            Node newNode = inMST[u.getId() - 1] ? v : u;
            inMST[newNode.getId() - 1] = true;

            for (EdgeWithBandwidth nextEdge : newNode.getEdgesWithBandwidth()) {
                if (!inMST[nextEdge.getNode1().getId() - 1] || !inMST[nextEdge.getNode2().getId() - 1]) {
                    pq.add(nextEdge);
                }
            }
        }

        if (edgesUsed != N - 1) {
            return -1; 
        }

        return totalLatency;
    }
}


