# 760. Binary Tree Right Side View
# 中文English
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom
#
# Example
# Example 1
#
# Input: {1,2,3,#,5,#,4}
# Output: [1,3,4]
# Explanation:
#    1
#  /   \
# 2     3
#  \     \
#   5     4
# Example 2
#
# Input: {1,2,3}
# Output: [1,3]
# Explanation:
#    1
#  /   \
# 2     3

from collections import deque


class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """

    def rightSideView(self, root):
        # write your code here
        if root is None:
            return []
        q = deque([root])
        rslt = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            rslt.append(node.val)

        return rslt
