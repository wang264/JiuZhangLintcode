# 177. Convert Sorted Array to Binary Search Tree With Minimal Height.
# 中文English
# Given a sorted (increasing order) array, Convert it to create a binary search tree with minimal height.
#
# Example
# Example 1:
#
# Input: []
# Output:  {}
# Explanation: The binary search tree is null
# Example 2:
#
# Input: [1,2,3,4,5,6,7]
# Output:  {4,2,6,1,3,5,7}
# Explanation:
# A binary search tree with minimal height.
#
#          4
#        /   \
#       2     6
#      / \    / \
#     1   3  5   7
#
#
# Notice
# There may exist multiple valid solutions, return any of them.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from helperfunc import TreeNode, build_tree_breadth_first


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """

    # use in order traversal
    def sortedArrayToBST(self, A):
        # write your code here
        return self.convert(A, 0, len(A) - 1)

    def convert(self, A, start, end):
        middle = (start + end) // 2
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        tree_node = TreeNode(A[middle])
        tree_node.left = self.convert(A, start, middle - 1)
        tree_node.right = self.convert(A, middle + 1, end)
        return tree_node


arr = [1, 2, 3, 4, 5, 6, 7]

sol = Solution()
rslt = sol.sortedArrayToBST(A=arr)