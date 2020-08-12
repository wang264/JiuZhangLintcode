# 597. Subtree with Maximum Average
# 中文English
# Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
#
# Example
# Example 1
#
# Input：
# {1,-5,11,1,2,4,-2}
# Output：11
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     11
#  / \   /  \
# 1   2 4    -2
# The average of subtree of 11 is 4.3333, is the maximun.
# Example 2
#
# Input：
# {1,-5,11}
# Output：11
# Explanation:
#      1
#    /   \
#  -5     11
# The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
# Notice
# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with maximum average.

import sys


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        # write your code here
        max_avg, max_tree, _, _ = self.helper(root)
        return max_tree

    def helper(self, node):
        """
        :param node:
        :return: tuple of 4
        the avgerage of the subtree that have maximum average,
        the root of the subtree that have maximum average,
        subtree size, number of nodes
        subtree sum of node value
        """
        if node is None:
            return -sys.maxsize, None, 0, 0

        l_max_avg, l_max_tree, l_size, l_sum = self.helper(node.left)
        r_max_avg, r_max_tree, r_size, r_sum = self.helper(node.right)

        cur_size, cur_sum = l_size + r_size + 1, l_sum + r_sum + node.val
        cur_avg = cur_sum / cur_size
        if l_max_avg == max(l_max_avg, r_max_avg, cur_avg):
            return l_max_avg, l_max_tree, cur_size, cur_sum
        elif r_max_avg == max(l_max_avg, r_max_avg, cur_avg):
            return r_max_avg, r_max_tree, cur_size, cur_sum
        else:
            return cur_avg, node, cur_size, cur_sum