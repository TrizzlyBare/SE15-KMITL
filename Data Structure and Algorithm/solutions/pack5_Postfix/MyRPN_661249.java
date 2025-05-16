package solutions.pack5_Postfix;

import java.util.regex.*;

public class MyRPN_661249 {

    private static Pattern pattern
            = Pattern.compile("-?\\d+(\\.\\d+)?");

    public static boolean isNumeric(String strNum) {
        if (strNum == null) {
            return false;
        }
        return pattern.matcher(strNum).matches();
    }

    public static double computeRPN(String rpn) {
        /* your code */
        MyStackA_661249 stack = new MyStackA_661249();
        int size = rpn.length();
        double tempTop;
        for (int i = 0; i < size; i++) {
            char c = rpn.charAt(i);
            if (Character.isDigit(c)) {
                stack.push((double) (c - '0'));
            } else if (c == '+' || c == '-' || c == '*' || c == '/') {
                tempTop = stack.pop();
                switch (c) {
                    case '+' ->
                        stack.push(stack.pop() + tempTop);
                    case '-' ->
                        stack.push(stack.pop() - tempTop);
                    case '*' ->
                        stack.push(stack.pop() * tempTop);
                    case '/' ->
                        stack.push(stack.pop() / tempTop);
                }

            }
        }
        return stack.pop();
    }
}