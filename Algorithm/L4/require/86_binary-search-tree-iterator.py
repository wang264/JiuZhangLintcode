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


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        dummy = TreeNode(-1)
        dummy.right = root
        self.stack.append(dummy)
        self.next()

    """
    @return: True if there has next node, or false
    """

    def hasNext(self, ):
        return len(self.stack) > 0

    """
    @return: return next node
    """

    def next(self, ):
        node = self.stack.pop()
        node_to_return = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left

        return node_to_return


from helperfunc import build_tree_breadth_first

root = build_tree_breadth_first(sequence=[6, 2, 8, 1, 3, 7, 9])
# Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    print(node.val)
