package solutions.pack3;

public class MyArrayBasic {

    protected int MAX_SIZE = 5;
    protected int data[] = new int[MAX_SIZE];
    protected int size = 0;

    public MyArrayBasic(int ... a) {
        MAX_SIZE = a.length;
        data = new int[MAX_SIZE];
        for (int i = 0; i < MAX_SIZE; i++) {
            data[i] = a[i];
            size++;
        }
    }

    public MyArrayBasic() {
        data = new int[MAX_SIZE];
    }

    public void add(int n) {
            data[size] = n;
            size++;
    }

    public void insert(int n, int index) {
            data[size++]=data[index];
            data[index] = n;
    }

    public int find(int n) {
        for (int i = 0; i < size; i++) {
            if (data[i] == n) {
                return i;
            }
        }
        return -1;
    }

    public int binarySearch (int n) {
        int a = 0, b=size-1;
        while(a<=b) {
            int m = (a+b)/2;
            if(data[m]==n) return m;
            if(n<data[m]) b = m-1;
            else a = m+1; 
        }
        return -1;
    }

    public int delete(int index) {
        if (index >= 0 && index < size) {
            int n = data[index];
            for (int i = index; i < size - 1; i++) {
                data[i] = data[i + 1];
            }
            size--;
            return n;
        } else {
            System.out.println("Invalid index");
            return -1;
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < size; i++) {
            sb.append(data[i]);
            if (i < size - 1) sb.append(", ");
        }
        sb.append("]");
        return sb.toString();
    }
}
