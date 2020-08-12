"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# class Solution:
#     """
#     @param root: A Tree
#     @return: Inorder in ArrayList which contains node values.
#     """
#     def inorderTraversal(self, root):
#         # write your code here
#         if root is None:
#             return []
#
#         stack = []
#         rslt = []
#         node = root
#         while True:
#             if node:
#                 stack.append(node)
#                 node = node.left
#
#             elif stack:
#                 node = stack.pop()
#                 rslt.append(node.val)
#                 node = node.right
#             else:
#                 break
#
#         return rslt

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        if not root:
            return []

        rslt = []
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            curr_node = stack.pop()
            rslt.append(curr_node.val)

            if curr_node.right:
                curr_node = curr_node.right
                while curr_node:
                    stack.append(curr_node)
                    curr_node = curr_node.left

        return rslt


class Solution2:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]
        rslt = []
        while stack:
            node = stack.pop()
            rslt.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return rslt[1:]

from helperfunc import build_tree_breadth_first

root = build_tree_breadth_first(sequence=[1, 2, 3, 4, 5, 6, 7])
