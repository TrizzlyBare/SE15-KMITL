package solutions.pack3;

public class MyArray_661249 extends MyArrayBasic {
    public MyArray_661249(int max) {
        super();
        MAX_SIZE = max;
        data = new int[MAX_SIZE];
    }

    public MyArray_661249() {
        super();
        MAX_SIZE = 100_000;
        data = new int[MAX_SIZE];
    }

    public boolean isFull() {
        return size == MAX_SIZE;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    int[] expandByK(int k) {
        int newSize = MAX_SIZE + k;
        int[] temp = new int[newSize];
        for (int i = 0; i < size; i++) {
            temp[i] = data[i];
        }
        MAX_SIZE = newSize;
        data = temp;
        return data;
    }

    int[] expand() {
        return expandByK(6);
    }

    @Override
    public void add(int n) {
        if (isFull()) {
            expand();
            super.add(n);
        }
    }

    @Override
    public void insert(int n, int index) {
        if (isFull()) {
            expand();
        }
        super.insert(n, index);
    }
}
