#Write a recursive function to traverse a binary tree and print a binary binary tree. For example, print_btree([1, [[11, [111,112]], [12,[121, [122, [1221,1222]]]]]], 0)

#The tree pattern of the first parameter is : [node, [left sub-tree], [right sub-tree]]. The second parameter is a depth that the recursive function will use to count the number of dots when it prints out the result. At the beginning, this parameter will be set to zero and it will get increase incrementally when the function makes a recursive to call itself.

#The output of the above function should be:
# 1
# . 11
# . . 111
# . . 112
# . 12
# . . 121
# . . 122
# . . . 1221
# . . . 1222

def print_btree(tree, depth):
    if not tree:
        return

    node = tree[0]
    left_subtree = tree[1]
    right_subtree = tree[2]

    # Print the current node with the appropriate number of dots for the depth
    print("." * depth + str(node))

    # Recursively print the left and right subtrees with increased depth
    if left_subtree:
        print_btree(left_subtree, depth + 1)
    if right_subtree:
        print_btree(right_subtree, depth + 1)

# Example usage
tree = [1, [[11, [111, 112]], [12, [121, [122, [1221, 1222]]]]]]
print_btree(tree, 2)
