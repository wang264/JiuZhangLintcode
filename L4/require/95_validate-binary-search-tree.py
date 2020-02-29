# # Definition of TreeNode:
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None

#     def __repr__(self):
#         left_val = self.left.val if self.left is not None else '-'
#         right_val = self.right.val if self.right is not None else '-'

#         return "V:{} L:{} R:{}".format(self.val, left_val, right_val)
#     # def __repr__(self):
#     #     return 'val:{}  left:{}  right:{}'.format(self.val, self.left,self.right)

# from typing import Tuple
# def build_tree_from_list(arr):
#     # build tree nodes
#     if len(arr) == 0:
#         return None
#     if len(arr) == 1:
#         return TreeNode(arr[0])

#     # fix left and right child
#     tree_nodes = [TreeNode(val) if val is not None else None for val in arr ]
#     root = tree_nodes[0]

#     count = len(tree_nodes)
#     for i in range(count):
#         if tree_nodes[i] is None:
#             continue

#         left_child_idx = i*2 + 1
#         right_child_idx = i*2 + 2

#         if left_child_idx<count:
#             tree_nodes[i].left = tree_nodes[left_child_idx]

#         if right_child_idx< count:
#             tree_nodes[i].right = tree_nodes[right_child_idx]

#     return root, tree_nodes


import sys
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        _, _, flag = self.helper(root)
        return flag

    def helper(self, root) -> tuple:
        """
        :param root:
        :return: tree_min_val, tree_max_val, tree_sum
        """
        if root is None:
            return sys.maxsize, -1*sys.maxsize, True

        left_min, left_max, left_valid = self.helper(root.left)
        right_min, right_max, right_valid = self.helper(root.right)

        if left_valid and right_valid and root.val> left_max and root.val<right_min:
            return min(left_min, right_min, root.val), max(left_max, right_max, root.val), True
        else:
            return min(left_min, right_min, root.val), max(left_max, right_max, root.val), False

