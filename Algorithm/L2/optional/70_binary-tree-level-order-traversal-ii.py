# 70. Binary Tree Level Order Traversal II
# 中文English
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# Example
# Example 1:
#
# Input:
# {1,2,3}
# Output:
# [[2,3],[1]]
# Explanation:
#     1
#    / \
#   2   3
# it will be serialized {1,2,3}
# level order traversal
# Example 2:
#
# Input:
# {3,9,20,#,#,15,7}
# Output:
# [[15,7],[9,20],[3]]
# Explanation:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# it will be serialized {3,9,20,#,#,15,7}
# level order traversal

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        import collections
        ans = []
        if root is None:
            return ans
        q = collections.deque()
        q.append(root)
        # 层次遍历
        while len(q) is not 0:
            row = []
            for i in range(len(q)):
                if q[0].left:  # 左子树不为空的话压入队列
                    q.append(q[0].left)
                if q[0].right:  # 右子树不为空的话压入队列
                    q.append(q[0].right)
                row.append(q[0].val)
                q.popleft()
            ans += [row]  # 储存当前层的节点
        # 倒序
        ans = ans[::-1]
        return ans
