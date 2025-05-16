package solutions.pack5_Postfix;

import java.util.Iterator;
import java.util.LinkedList;

public class MyQueueExtendLinkedList<T> implements Iterable<T> {
    private LinkedList<T> items = new LinkedList<>();
    private int count;

    public void enqueue(T d) {
        items.add(d);
        count++;
    }

    public T dequeue() {
        count--;
        return items.poll();
    }

    public T top() {
        return items.peek();
    }

    public T getLast() {
        return items.getLast();
    }

    public String dumpToString() {
        return items.toString();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < items.size(); i++) {
            sb.append(items.get(i));
            if (i < items.size() - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

    @Override
    public Iterator<T> iterator() {
        return new AnyItemsIterator(this);
    }

    private class AnyItemsIterator implements Iterator<T> {
        private MyQueueExtendLinkedList<T> list;
        private int idx;

        public AnyItemsIterator(MyQueueExtendLinkedList<T> arg) {
            this.list = arg;
            this.idx = 0;
        }

        @Override
        public boolean hasNext() {
            return idx < list.count;
        }

        @Override
        public T next() {
            return list.items.get(idx++);
        }
    }
}
