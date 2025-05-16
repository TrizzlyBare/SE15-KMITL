package solutions.pack5_Postfix;

public class MyStackA_661249 {
    private int MAX_SIZE = 100;
    private double[] stack = new double[MAX_SIZE];
    private int top = -1;

    public void push(double d) {
        if (isFull()) {
            throw new IllegalStateException("Stack is full");
        }
        stack[++top] = d;
    }

    public double pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stack[top--];
    }

    public double peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stack[top];
    }

    public boolean isFull() {
        return top == MAX_SIZE - 1;
    }

    public boolean isEmpty() {
        return top == -1;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= top; i++) {
            sb.append(stack[i]).append(" ");
        }
        return sb.toString();
    }
}
