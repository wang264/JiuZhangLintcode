"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        _, node, _ = self.find_subtree_helper(root)

        return node

    def find_subtree_helper(self, node):
        """

        @param node:
        @return: a tuple of three elements,
        ( sum of the whole tree,
        root of the min_sum subtree,
        sum value of the min_sum subtree)
        """
        if node is None:
            return 0, None, sys.maxsize

        left_tree_sum, left_min_node, left_min_sum = self.find_subtree_helper(node=node.left)
        right_tree_sum, right_min_node, right_min_sum = self.find_subtree_helper(node=node.right)

        tree_sum = left_tree_sum + right_tree_sum + node.val

        if left_min_sum == min(left_min_sum, right_min_sum, tree_sum):
            return tree_sum, left_min_node, left_min_sum
        elif right_min_sum == min(left_min_sum, right_min_sum, tree_sum):
            return tree_sum, right_min_node, right_min_sum
        else:
            return tree_sum, node, tree_sum