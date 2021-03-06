# 95. Validate Binary Search Tree
# 中文English
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# A single node tree is a BST
# Example
# Example 1:
#
# Input:  {-1}
# Output：true
# Explanation：
# For the following binary tree（only one node）:
# 	      -1
# This is a binary search tree.
# Example 2:
#
# Input:  {2,1,4,#,#,3,5}
# Output: true
# For the following binary tree:
# 	  2
# 	 / \
# 	1   4
# 	   / \
# 	  3   5
# This is a binary search tree.

import sys


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        _, _, flag = self.helper(root)
        return flag

    def helper(self, root) -> tuple:
        """
        :param root:
        :return: tree_min_val, tree_max_val, tree_sum
        """
        if root is None:
            return sys.maxsize, -1 * sys.maxsize, True

        left_min, left_max, left_valid = self.helper(root.left)
        right_min, right_max, right_valid = self.helper(root.right)

        if left_valid and right_valid and root.val > left_max and root.val < right_min:
            return min(left_min, right_min, root.val), max(left_max, right_max, root.val), True
        else:
            return min(left_min, right_min, root.val), max(left_max, right_max, root.val), False


from helperfunc import build_tree_breadth_first

sol = Solution()

root = build_tree_breadth_first(sequence=[2, 1])
sol.isValidBST(root=root)
