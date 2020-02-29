"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        rslt = []
        this_path = []
        self.helper(root, this_path, rslt)
        return rslt

    def helper(self, node, this_path, rslt):
        # if this node is leave node
        this_path.append(str(node.val))
        if node.left is None and node.right is None:
            temp_str = '->'.join(this_path)
            rslt.append(temp_str)
        else:
            if node.left:
                self.helper(node.left, this_path, rslt)
                this_path.pop()
            if node.right:
                self.helper(node.right, this_path, rslt)
                this_path.pop()