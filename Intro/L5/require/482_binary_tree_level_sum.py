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
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """

    def levelSum(self, root, level):
        if root is None:
            return 0
        # write your code here
        q = deque([root])
        curr_level = 1
        ans = 0
        while q:
            for _ in range(len(q)):
                if level == curr_level:
                    ans += q.popleft().val
                else:
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            curr_level += 1
        return ans
