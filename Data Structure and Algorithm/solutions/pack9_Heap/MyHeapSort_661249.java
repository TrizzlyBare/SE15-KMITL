package solutions.pack9_Heap;

public class MyHeapSort_661249 extends MyMinHeap_661249 {
    public String sort() {
        StringBuilder sb = new StringBuilder();
        while (size > 0) {
            sb.append(remove()).append(" ");
        }
        return sb.toString();
    }
}
