package solutions;

public class Edge {
    private int latency;
    private Node node1;
    private Node node2;

    public Edge(int latency, Node node1, Node node2) {
        this.latency = latency;
        this.node1 = node1;
        this.node2 = node2;
    }
    
    public int getLatency( ) {
        return latency;
    }
    
    public Node getNode1() {
        return node1;
    }

    public Node getNode2() {
        return node2;
    }

    @Override
    public String toString() {
        return "Edge: " + latency;
    }

}
