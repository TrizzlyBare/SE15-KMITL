package solutions.pack10_bst;

public class TreeNode_661249 {
    int data;
    TreeNode_661249 left, right;

    public TreeNode_661249(int item) {
        data = item;
        left = right = null;
    }

    @Override
    public String toString() {
        String leftData = (left == null) ? "null" : String.valueOf(left.data);
        String rightData = (right == null) ? "null" : String.valueOf(right.data);
        return leftData + "<-" + data + "->" + rightData;
    }
}