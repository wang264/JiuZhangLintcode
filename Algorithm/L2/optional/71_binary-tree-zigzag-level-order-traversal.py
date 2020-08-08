# 71. Binary Tree Zigzag Level Order Traversal
# 中文English
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
# then right to left for the next level and alternate between).
#
# Example
# Example 1:
#
# Input:{1,2,3}
# Output:[[1],[3,2]]
# Explanation:
#     1
#    / \
#   2   3
# it will be serialized {1,2,3}
# Example 2:
#
# Input:{3,9,20,#,#,15,7}
# Output:[[3],[20,9],[15,7]]
# Explanation:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# it will be serialized {3,9,20,#,#,15,7}


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        # write your code here
        rslt = []
        if root is None:
            return rslt
        level = 0
        queue = deque([root])

        while queue:
            level = level + 1
            rslt_this_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                rslt_this_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level%2==0:
                rslt.append(list(reversed(rslt_this_level)))
            else:
                rslt.append(rslt_this_level)

        return rslt