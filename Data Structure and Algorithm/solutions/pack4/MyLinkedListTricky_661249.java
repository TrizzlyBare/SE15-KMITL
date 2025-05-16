package solutions.pack4;

import java.util.HashSet;
import java.util.Set;

public class MyLinkedListTricky_661249 extends MyLinkedList_661249 {
    public void q1_rotate_clockwise(int k) {
        if ((head == null )|| (k <= 0) ||  (k >= size())) {
            return;
        }

        Node current = head;
        int count = 1;
        while (count < k && current != null) {
            current = current.next;
            count++;
        }

        if (current == null) {
            return;
        }

        Node kthNode = current;
        while (current.next != null) {
            current = current.next;
        }

        current.next = head;
        head = kthNode.next;
        kthNode.next = null;
    }

    
    public void q2_reverse() {
        Node prev = null;
        Node current = head;
        Node next = null;

        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    public void q3_remove_dup() {
        if (head == null) return;

        Set<Integer> seen = new HashSet<>();
        Node current = head;
        Node prev = null;

        while (current != null) {
            if (seen.contains(current.data)) {
                prev.next = current.next; 
            } else {
                seen.add(current.data);
                prev = current;
            }
            current = current.next;
        }
    }
    
    public void q4_add_one() {
        head = reverseList(head);
        Node current = head;
        int carry = 1;

        while (current != null && carry > 0) {
            int sum = current.data + carry;
            carry = sum / 10;
            current.data = sum % 10;
            current = current.next;
        }

        if (carry > 0) {
            Node newNode = new Node(carry);
            newNode.next = head;
            head = newNode;
        }

        head = reverseList(head);
    }

    private Node reverseList(Node node) {
        Node prev = null;
        Node current = node;
        Node next = null;

        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

    public boolean q5_isPalindrome() {
        if (head == null) return true;

        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        Node secondHalf = reverseList(slow);
        Node firstHalf = head;

        Node secondHalfCopy = secondHalf;
        while (secondHalfCopy != null) {
            if (firstHalf.data != secondHalfCopy.data) {
                return false;
            }
            firstHalf = firstHalf.next;
            secondHalfCopy = secondHalfCopy.next;
        }

        return true;
    }
}
