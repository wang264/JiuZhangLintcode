# # Definition of TreeNode:
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
#     return root, tree_nodes

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        a_in_tree, b_in_tree, lca = self.helper(root, A, B)
        if a_in_tree and b_in_tree:
            return lca
        else:
            return None

    def helper(self, root, node_a, node_b) ->tuple:
        """
        :param root:
        :param node_a:
        :param node_b:
        :return: return tuple of three ( is_a_in_tree, is_b_in_tree, the_lca_node)
        """
        if root is None:
            return False, False, None

        # -----Divide-----#
        a_in_left_tree, b_in_left_tree, lca_left_tree = self.helper(root.left, node_a, node_b)
        a_in_right_tree, b_in_right_tree, lca_right_tree = self.helper(root.right, node_a, node_b)

        # -----Conqure------#
        a_exist_in_tree = a_in_left_tree or a_in_right_tree or root is node_a
        b_exist_in_tree = b_in_left_tree or b_in_right_tree or root is node_b

        if a_exist_in_tree and b_exist_in_tree:
            if lca_left_tree and lca_right_tree:
                return True, True, root
            elif lca_left_tree and not lca_right_tree:
                return True, True, lca_left_tree
            elif not lca_left_tree and lca_right_tree:
                return True, True, lca_right_tree
            else:
                # if there are no lca in either subtree the lca must be root
                return True, True, root
        else:
            # if either of A or B does not exist in this tree. it means no LCA, so we return None for LCA.
            return a_exist_in_tree, b_exist_in_tree, None

#
# sol=Solution()
# root, nodes = build_tree_from_list([4,3,7,None,None,5,6])
#
# sol.lowestCommonAncestor(root, A=nodes[2], B=nodes[6])