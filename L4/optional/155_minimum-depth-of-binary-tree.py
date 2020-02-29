"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # if have both left and right child
        if root.left and root.right:
            return min(left_depth, right_depth) + 1
        # if only have left child
        elif root.left and not root.right:
            return left_depth + 1
        # if only have right child
        elif root.right and not root.left:
            return right_depth + 1
        # if this is a leaf node
        else:
            return 1