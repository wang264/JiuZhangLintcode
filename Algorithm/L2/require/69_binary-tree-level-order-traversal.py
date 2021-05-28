# 69. Binary Tree Level Order Traversal
# 中文English
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# Example
# Example 1:
#
# Input：{1,2,3}
# Output：[[1],[2,3]]
# Explanation：
#   1
#  / \
# 2   3
# it will be serialized {1,2,3}
# level order traversal
# Example 2:
#
# Input：{1,#,2,3}
# Output：[[1],[2],[3]]
# Explanation：
# 1
#  \
#   2
#  /
# 3
# it will be serialized {1,#,2,3}
# level order traversal
# Challenge
# Challenge 1: Using only 1 queue to implement it.
#
# Challenge 2: Use BFS algorithm to do it.
#
# Notice
# The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
# The number of nodes does not exceed 20.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if root is None:
            return []
        
        q = deque([root])
        rslt = list()
        while q:
            this_level = list()
            for _ in range(len(q)):
                node = q.popleft()
                this_level.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            rslt.append(this_level)
        
        return rslt


sol  =Solution()
sol.levelOrder(root=None    )