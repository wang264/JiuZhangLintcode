"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = [root]
        rslt = []
        while stack:
            node = stack.pop()
            rslt.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return rslt


from helperfunc import build_tree_breadth_first

sol = Solution()
root = build_tree_breadth_first(sequence=[1, 2, 3, 4, 5, 6, 7])
sol.preorderTraversal(root=root)
