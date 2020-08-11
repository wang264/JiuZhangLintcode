# 93. Balanced Binary Tree
# Given a binary tree, determine if it is height - balanced.
#
# For this problem, a height - balanced binary tree is defined as a binary tree in which the depth of
# the two subtrees of every node never differ by more than 1.
#
# Example
# Example 1:
# Input: tree = {1, 2, 3}
# Output: true
#
# Explanation:
# This is a balanced binary tree.
#      1
#     / \
#    2   3
#
# Example 2:
# Input: tree = {3, 9, 20,  # ,#,15,7}
# Output: true
#
# Explanation:
# This is a balanced binary tree.
#     3
#    / \
#   9   20
#       / \
#      15  7
#
# Example 3:
# Input: tree = {1,  # ,2,3,4}
# Output: false
#
# Explanation:
# This is not a balanced tree. The height of node 1 's right sub-tree is 2 but left sub-tree is 0.
#      1
#       \
#        2
#       / \
#      3   4


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        balanced, height = self.helper(root)
        return balanced

    def helper(self, root):
        """
        :param root:
        :return: tuple of (is_balanced, height)
        """
        if root is None:
            # for a tree that is empty, it is balanced and height of it is 0
            return True, 0

        left_balanced, left_height = self.helper(root.left)
        right_balanced, right_height = self.helper(root.right)

        if left_balanced and right_balanced and abs(left_height - right_height) <= 1:
            return True, max(left_height, right_height) + 1

        else:
            return False, max(left_height, right_height) + 1
