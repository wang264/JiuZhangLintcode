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

#     return root

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        balanced, height = self.helper(root)
        return balanced

    def helper(self, root):
        """
        :param root:
        :return: tuple of (is_balanced, height)
        """
        if root is None:
            # for a tree that is empty, it is balanced and height of it is 0
            return True, 0

        left_balanced, left_height = self.helper(root.left)
        right_balanced, right_height = self.helper(root.right)

        if left_balanced and right_balanced and abs(left_height - right_height) <= 1:
            return True, max(left_height, right_height) + 1

        else:
            return False, max(left_height, right_height) + 1

