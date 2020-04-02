"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

#https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/
# 1. If root is NULL then return
# 2. if key is found then
#     a. If its left subtree is not null
#         Then predecessor will be the right most
#         child of left subtree or left child itself.
#     b. If its right subtree is not null
#         The successor will be the left most child
#         of right subtree or right child itself.
#     return
# 3. If key is smaller then root node
#         set the successor as root
#         search recursively into left subtree
#     else
#         set the predecessor as root
#         search recursively into right subtree
class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        self.suc = None
        self.helper(root, p)
        return self.suc

    def helper(self, root, p):
        if root is None:
            return None
        # If key is present at root
        if root.val == p.val:
            # the minimum value in right subtree is successor
            if root.right is not None:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                self.suc = tmp

        # If key is smaller than root's key, go to left subtree

        elif p.val < root.val:
            self.suc = root
            self.helper(root.left, p)

        # If key is larger than root's key, go to left subtree
        # the must must in the right subtree or it does not exist
        elif p.val > root.val:
            self.helper(root.right, p)