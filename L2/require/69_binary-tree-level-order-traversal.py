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