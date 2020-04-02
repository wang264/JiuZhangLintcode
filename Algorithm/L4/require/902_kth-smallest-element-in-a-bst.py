# # # Definition of TreeNode:
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None
#
#     def __repr__(self):
#         left_val = self.left.val if self.left is not None else '-'
#         right_val = self.right.val if self.right is not None else '-'
#
#         return "V:{} L:{} R:{}".format(self.val, left_val, right_val)
#     # def __repr__(self):
#     #     return 'val:{}  left:{}  right:{}'.format(self.val, self.left,self.right)
#
# from typing import Tuple
# def build_tree_from_list(arr):
#     # build tree nodes
#     if len(arr) == 0:
#         return None
#     if len(arr) == 1:
#         return TreeNode(arr[0])
#
#     # fix left and right child
#     tree_nodes = [TreeNode(val) if val is not None else None for val in arr ]
#     root = tree_nodes[0]
#
#     count = len(tree_nodes)
#     for i in range(count):
#         if tree_nodes[i] is None:
#             continue
#
#         left_child_idx = i*2 + 1
#         right_child_idx = i*2 + 2
#
#         if left_child_idx<count:
#             tree_nodes[i].left = tree_nodes[left_child_idx]
#
#         if right_child_idx< count:
#             tree_nodes[i].right = tree_nodes[right_child_idx]
#
#     return root

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):

        if root is None:
            return root

        count = 0
        stack = []
        rslt = []
        node = root

        while True:
            if node:
                stack.append(node)
                node = node.left

            elif stack:
                node = stack.pop()
                rslt.append(node.val)
                count += 1
                if count == k:
                    return node.val
                #if node.right:
                node = node.right
            else:
                break

# sol = Solution()
# root = build_tree_from_list([1,None,2])
#
# sol.kthSmallest(root, 2)