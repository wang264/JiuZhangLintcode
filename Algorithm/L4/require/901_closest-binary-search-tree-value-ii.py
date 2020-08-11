# 901. Closest Binary Search Tree Value II
# 中文English
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Example
# Example 1:
#
# Input:
# {1}
# 0.000000
# 1
# Output:
# [1]
# Explanation：
# Binary tree {1},  denote the following structure:
#  1
# Example 2:
#
# Input:
# {3,1,4,#,2}
# 0.275000
# 2
# Output:
# [1,2]
# Explanation：
# Binary tree {3,1,4,#,2},  denote the following structure:
#   3
#  /  \
# 1    4
#  \
#   2
# Challenge
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
#
# Notice
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

import heapq
import sys


# this is not the best method.
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # write your code here
        dummy = TreeNode(sys.maxsize)
        dummy.right = root
        stack = [dummy]
        # use a max_heap to store the max_distance
        max_heap = []
        while stack:
            node = stack.pop()
            heapq.heappush(max_heap, (-1 * abs(node.val - target), node.val))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            # print(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        rslt = []
        for _, val in reversed(max_heap):
            rslt.append(val)

        return rslt


from helperfunc import TreeNode, build_tree_breadth_first

root = build_tree_breadth_first([6, 2, 8, 1, 3, 7, 9])
sol = Solution()
sol.closestKValues(root=root, target=10, k=2)

root = build_tree_breadth_first(sequence=[3, 1, 4, None, 2])
sol = Solution()
sol.closestKValues(root, 0.275, 2)
