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
#     @return: Postorder in ArrayList which contains node values.
#     """
#     def postorderTraversal(self, root):
#         # write your code here
#         if not root:
#             return []
#         ans, stack, cur = [], [], root
#         while cur:
#             stack.append(cur)
#             if cur.left:
#                 cur = cur.left
#             else:
#                 cur = cur.right
#
#         while stack:
#             cur = stack.pop()
#             ans.append(cur.val)
#             if stack and stack[-1].left == cur:
#                 cur = stack[-1].right
#                 while cur:
#                     stack.append(cur)
#                     if cur.left:
#                         cur = cur.left
#                     else:
#                         cur = cur.right
#
#         return ans

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    # by using two stacks
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result

        # Initialize two stacks
        s1 = []
        s2 = []


        s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        # pop stack2 to get postorder traversal
        while s2:
            result.append(s2.pop().val)

        return result

# sol = Solution()
# root, _ = build_tree_from_list([1,2,3,4,5,None, None,None, 7])
#
# sol.postorderTraversal(root)