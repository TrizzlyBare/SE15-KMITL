package solutions.pack5_Postfix;

public class MyStackL_661249 {
    class Node {
        String value;
        Node next;

        Node(String value) {
            this.value = value;
            this.next = null;
        }
    }

    private Node top;
    public MyStackL_661249() {
        top = null;
    }

    public void push(String value) {
        Node newNode = new Node(value);
        newNode.next = top;
        top = newNode;
    }

    public String pop() {
        if (top == null) {
            return null;
        }
        String value = top.value;
        top = top.next;
        return value;
    }

    public String peek() {
        if (top == null) {
            return null;
        }
        return top.value;
    }

    public boolean isFull() {
        return false;
    }

    public boolean isEmpty() {
        return top == null;
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Top->");
        Node temp = top;

        while (temp != null) {
            sb.append(temp.value).append("->");
            temp = temp.next;
        }
        
        sb.append("Bottom");
        return sb.toString();
    }
}
