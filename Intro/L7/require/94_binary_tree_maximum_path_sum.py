# 94. Binary Tree Maximum Path Sum
# 中文English
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# Example
# Example 1:
# 	Input:  For the following binary tree（only one node）:
# 	2
# 	Output：2
#
# Example 2:
# 	Input:  For the following binary tree:
#
#       1
#      / \
#     2   3
#
# Output: 6

from helperfunc import TreeNode
import sys


class Solution:
    # 在动态更新self.ans的时候，我们去算以每一个Node 为Root的maximum path sum.
    # 但是在Helper Function的返回中我们只能返回1。必须用当前Node作为root，左右子数只能用一边的maximum path sum.
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxsize
        self._max_path_sum(root)
        return self.ans

    def _max_path_sum(self, root):
        if not root:
            return -sys.maxsize
        left = max(0, self._max_path_sum(root.left))
        right = max(0, self._max_path_sum(root.right))
        self.ans = max(self.ans, root.val + left + right)  # 以Root为根节点的最大的path sum.

        # when reuturn
        # 1. root must be used.
        # 2. at most one child can be used.
        return root.val + max(left, right)

