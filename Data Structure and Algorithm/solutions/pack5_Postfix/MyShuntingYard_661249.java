package solutions.pack5_Postfix;
import java.util.StringTokenizer;

public class MyShuntingYard_661249 {
    public static int order(String c) {
        return switch (c) {
            case "+", "-" -> 1;
            case "*", "/" -> 2;
            default -> 0;
        };
    }

    public static String infixToPostfix(String infixString) {
        MyQueueExtendLinkedList<String> queue = new MyQueueExtendLinkedList<>();
        MyStackL_661249 stack = new MyStackL_661249();
        StringTokenizer st = new StringTokenizer(infixString);
    
        while (st.hasMoreTokens()) {
            String t = st.nextToken();
            if (MyRPN_661249.isNumeric(t)) {
                queue.enqueue(t);
            } else if (t.equals("(")) {
                stack.push(t);
            } else if (t.equals(")")) {
                while (!stack.isEmpty() && !stack.peek().equals("(")) {
                    queue.enqueue(stack.pop());
                }
                stack.pop(); // Pop the '(' if it exists
            } else {
                while (!stack.isEmpty() && order(stack.peek()) >= order(t)) {
                    queue.enqueue(stack.pop());
                }
                stack.push(t);
            }
            System.out.println("current q: " + queue);
        }
    
        while (!stack.isEmpty()) {
            queue.enqueue(stack.pop());
        }
    
        return queue.toString();
    }
}