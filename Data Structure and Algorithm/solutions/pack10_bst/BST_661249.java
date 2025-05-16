package solutions.pack10_bst;

public class BST_661249 {

    TreeNode_661249 root;

    public BST_661249() {
        root = null;
    }

    public TreeNode_661249 getRoot() {
        return root;
    }

    /* your code here */

    public void insert(int data) {
        TreeNode_661249 newNode = new TreeNode_661249(data);
        if (root == null) {
            root = newNode;
            return;
        }

        TreeNode_661249 current = root;
        TreeNode_661249 parent = null;

        while (true) {
            parent = current;
            if (data < current.data) {
                current = current.left;
                if (current == null) {
                    parent.left = newNode;
                    return;
                }
            } else {
                current = current.right;
                if (current == null) {
                    parent.right = newNode;
                    return;
                }
            }
        }
    }

    public TreeNode_661249 search(int data) {
        TreeNode_661249 current = root;
        while (current != null) {
            if (current.data == data) {
                return current;
            } else if (current.data > data) {
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return null;
    }

    public void delete(int data) {
        root = deleteRecurse(root, data);
    }

    private TreeNode_661249 deleteRecurse(TreeNode_661249 root, int data) {
        if (root == null) {
            return root;
        }
        if (data < root.data) {
            root.left = deleteRecurse(root.left, data);
        } else if (data > root.data) {
            root.right = deleteRecurse(root.right, data);
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }
            root.data = minValue(root.right);
            root.right = deleteRecurse(root.right, root.data);
        }
        return root;
    }

    private int minValue(TreeNode_661249 root) {
        int minv = root.data;
        while (root.left != null) {
            minv = root.left.data;
            root = root.left;
        }
        return minv;
    }

    /* Printing */
    public void printInOrder() {
        printInOrderRecurse(root);
        System.out.println();
    }

    public void printInOrderRecurse(TreeNode_661249 node) {
        if (node == null) {
            return;
        }
        printInOrderRecurse(node.left);
        System.out.print(node.data + " ");
        printInOrderRecurse(node.right);
    }

    public void printPreOrder() {
        printPreOrderRecurse(root);
        System.out.println();
    }

    public void printPreOrderRecurse(TreeNode_661249 node) {
        if (node == null) {
            return;
        }
        System.out.print(node.data + " ");
        printPreOrderRecurse(node.left);
        printPreOrderRecurse(node.right);
    }

    public void printPostOrder() {
        printPostOrderRecurse(root);
        System.out.println();
    }

    public void printPostOrderRecurse(TreeNode_661249 node) {
        if (node == null) {
            return;
        }
        printPostOrderRecurse(node.left);
        printPostOrderRecurse(node.right);
        System.out.print(node.data + " ");
    }

    public TreeNode_661249 findMax() {
        TreeNode_661249 current = root;
        while (current.right != null) {
            current = current.right;
        }
        return current;
    }

    public TreeNode_661249 findMin() {
        TreeNode_661249 current = root;
        while (current.left != null) {
            current = current.left;
        }
        return current;
    }

    public int height() {
        return heightRecurse(root);
    }

    private int heightRecurse(TreeNode_661249 node) {
        if (node == null) {
            return 0;
        }
        int leftHeight = heightRecurse(node.left);
        int rightHeight = heightRecurse(node.right);
        return Math.max(leftHeight, rightHeight) + 1;
    }

    public int count() {
        return countRecurse(root);
    }

    private int countRecurse(TreeNode_661249 node) {
        if (node == null) {
            return 0;
        }
        return countRecurse(node.left) + countRecurse(node.right) + 1;
    }

    public int findMedian() {
        int count = count();
        if (count % 2 == 0) {
            return (findKth(count / 2) + findKth(count / 2 + 1)) / 2;
        } else {
            return findKth(count / 2 + 1);
        }
    }

    private int findKth(int k) {
        return findKthRecurse(root, k);
    }

    private int findKthRecurse(TreeNode_661249 node, int k) {
        if (node == null) {
            return 0;
        }
        int leftCount = countRecurse(node.left);
        if (leftCount == k - 1) {
            return node.data;
        } else if (leftCount > k - 1) {
            return findKthRecurse(node.left, k);
        } else {
            return findKthRecurse(node.right, k - leftCount - 1);
        }
    }

    public int findRank(int data) {
        return findRankRecurse(root, data);
    }

    private int findRankRecurse(TreeNode_661249 node, int data) {
        if (node == null) {
            return -1;
        }
        if (node.data == data) {
            return countRecurse(node.left) + 1;
        } else if (node.data > data) {
            return findRankRecurse(node.left, data);
        } else {
            int rightRank = findRankRecurse(node.right, data);
            if (rightRank == -1) {
                return -1;
            }
            return countRecurse(node.left) + 1 + rightRank;
        }
    }
}
