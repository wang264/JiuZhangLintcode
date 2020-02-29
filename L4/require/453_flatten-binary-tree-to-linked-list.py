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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        """
        idea: similar to pre-order travesal using stack.
        :param root: TreeNode
        :return: return the
        """
        if root is None:
            return root

        rslt = root
        stack = [root]
        last_node = TreeNode(-1)

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            last_node.right = node
            node.left = None
            last_node = node

        return rslt