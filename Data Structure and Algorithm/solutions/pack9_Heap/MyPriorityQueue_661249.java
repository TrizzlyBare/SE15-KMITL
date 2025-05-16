package solutions.pack9_Heap;

import java.util.PriorityQueue;

public class MyPriorityQueue_661249 {

    private static int MAX_SIZE = 6;
    private PriorityQueue<Integer> pq;

    public MyPriorityQueue_661249() {
        pq = new PriorityQueue<>(MAX_SIZE);
    }

    public void enqueue(int value) {
        if (isFull()) {
            System.out.println("PriorityQueue is full");
            return;
        }
        pq.offer(value);
    }

    public int dequeue() {
        if (isEmpty()) {
            System.out.println("PriorityQueue is empty");
            return -1;
        }
        return pq.poll();
    }

    public int front() {
        if (isEmpty()) {
            System.out.println("PriorityQueue is empty");
            return -1;
        }
        return pq.peek();
    }

    public boolean isEmpty() {
        return pq.isEmpty();
    }

    public boolean isFull() {
        return pq.size() == MAX_SIZE;
    }

    @Override
    public String toString() {
        return pq.toString();
    }
}
