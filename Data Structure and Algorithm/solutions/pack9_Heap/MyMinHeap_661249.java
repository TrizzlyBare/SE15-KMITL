package solutions.pack9_Heap;

public class MyMinHeap_661249 {

    int MAX_SIZE = 6;
    int[] heap = new int[MAX_SIZE];
    int size = 0;

    public void insert(int value) {
        if (size == MAX_SIZE) {
            System.out.println("Heap is full");
            return;
        }
        heap[size] = value;
        int current = size;
        while (current > 0 && heap[current] < heap[parent(current)]) {
            swap(current, parent(current));
            current = parent(current);
        }
        size++;
    }

    public int remove() {
        if (size == 0) {
            System.out.println("Heap is empty");
            return -1;
        }
        int popped = heap[0];
        heap[0] = heap[--size];
        heapify(0);
        return popped;
    }

    public int peek() {
        if (size == 0) {
            System.out.println("Heap is empty");
            return -1;
        }
        return heap[0];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == MAX_SIZE;
    }

    private int parent(int current) {
        return (current - 1) / 2;
    }

    private void swap(int current, int parent) {
        int temp = heap[current];
        heap[current] = heap[parent];
        heap[parent] = temp;
    }

    private void heapify(int i) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int smallest = i;
        if (left < size && heap[left] < heap[i]) {
            smallest = left;
        }
        if (right < size && heap[right] < heap[smallest]) {
            smallest = right;
        }
        if (smallest != i) {
            swap(i, smallest);
            heapify(smallest);
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(heap[i]).append(" ");
        }
        return sb.toString();
    }
}
