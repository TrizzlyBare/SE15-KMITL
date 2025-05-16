package solutions.pack4;

public class MyLinkedList_661249 {
    public class Node {
        int data;
        Node next;

        public Node(int d) {
            data = d;
            next = null;
        }
    }

    Node head = null;
    int size = 0;

    public void add(int d) {
        Node p = new Node(d);
        p.next = head;
        head = p;
        size++;
    }

    public void add(int[] d) {
        for (int i = d.length - 1; i >= 0; i--) {
            add(d[i]);
            size++;
        }
    }
    
    public void insert(int d) {
        Node newNode = new Node(d);

        if (head == null || head.data >= newNode.data)   {
            newNode.next = head;
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null && current.next.data < newNode.data) {
                current = current.next;
            }
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    public void insert(int[] arr) {
        for (int d : arr) {
            insert(d);
        }
    }

    public int find(int d) {
        Node p = head;
        int i= 0;
        while (p != null) {
            if (p.data == d) return i;
            p = p.next;
            i++;
        }
        return -1;
    }

    public void delete(int d) {
        Node t = new Node(0);
        t.next = head;
        Node p = t;
        while ((p.next != null) && (p.next.data != d)) {
            p = p.next;
        }
        if (p.next != null) {
            p.next = p.next.next;
        }
        head = t.next;
        size--;
    }

    public void delete(int d) {
        Node p = head;
        while ( p != null) {
            if (p.next.data == d) {
                p.next = p.next.next;
            }
        }
    }

    public int size(){
        return size;
    }

    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer("head ");
        Node p = head;
        while(p!=null) {
        sb.append("--> [");
        sb.append(p.data);
        sb.append("] ");
        p = p.next;
        }
        sb.append("-> null");
        return new String(sb);
    }
}
