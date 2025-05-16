package solutions;

public class EdgeWithBandwidth extends Edge {
    private int bandwidth;

    public EdgeWithBandwidth(int latency, int bandwidth, Node node1, Node node2) {
        super(latency, node1, node2);
        this.bandwidth = bandwidth;
    }

    public int getBandwidth() {
        return bandwidth;
    }

    public void setBandwidth(int bandwidth) {
        this.bandwidth = bandwidth;
    }

    @Override
    public String toString() {
        return "EdgeWithBandwidth [latency=" + getLatency() + ", bandwidth=" + bandwidth + "]";
    }
}
