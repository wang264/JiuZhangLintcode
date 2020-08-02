# 86. Binary Search Tree Iterator
# 中文English
# Design an iterator over a binary search tree with the following rules:
#
# Elements are visited in ascending order (i.e. an in-order traversal)
# next() and hasNext() queries run in O(1) time in average.
# Example
# Example 1
#
# Input:  {10,1,11,#,6,#,12}
# Output:  [1, 6, 10, 11, 12]
# Explanation:
# The BST is look like this:
#   10
#   /\
#  1 11
#   \  \
#    6  12
# You can return the inorder traversal of a BST [1, 6, 10, 11, 12]
# Example 2
#
# Input: {2,1,3}
# Output: [1,2,3]
# Explanation:
# The BST is look like this:
#   2
#  / \
# 1   3
# You can return the inorder traversal of a BST tree [1,2,3]
# Challenge
# Extra memory usage O(h), h is the height of the tree.
#
# Super Star: Extra memory usage O(1)


# Definition of TreeNode:
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def __repr__(self):
        left = None if self.left is None else self.left.value
        right = None if self.right is None else self.right.value
        return '(D:{}, L:{}, R:{})'.format(self.value, left, right)


def build_tree_breadth_first(sequence):
    # Create a list of trees
    forest = [TreeNode(x) if x is not None else None for x in sequence]

    # Fix up the left- and right links
    count = len(forest)
    for index, tree in enumerate(forest):
        left_index = 2 * index + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * index + 2
        if right_index < count:
            tree.right = forest[right_index]

    for index, tree in enumerate(forest):
        print('[{}]: {}'.format(index, tree))
    return forest[0]  # root


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    """
    @return: True if there has next node, or false
    """

    def hasNext(self, ):
        return len(self.stack)>0

    """
    @return: return next node
    """
    def next(self, ):
        node = self.stack.pop()
        ret_val = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node=node.left

        return ret_val


# Example of iterate a tree:
bst = build_tree_breadth_first([10, 1, 11, -1, 6, 10.5, 12])

iterator = BSTIterator(bst)
while iterator.hasNext():
    node = iterator.next()
    print(node.value)
#     do something for node
