# 88. Lowest Common Ancestor of a Binary Tree
# 中文English
# Given the root and two nodes in a Binary Tree.Find the lowest common ancestor(LCA) of the two nodes.
#
# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
#
# Example
# Example
# 1:
#
# Input：{1}, 1, 1
# Output：1
# Explanation： For the following binary tree（only one node）: 1
# LCA(1, 1) = 1
#
# Example 2:
#
# Input：{4, 3, 7,  # ,#,5,6},3,5
# Output：4
# Explanation： For the following binary tree:
#
#             4
#            / \
#           3    7
#               / \
#              5   6
#
# LCA(3, 5) = 4
# Notice
# Assume two nodes are exist in tree.




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
            if not lca_left_tree and not lca_right_tree:
                return True, True, root
            elif lca_left_tree and not lca_right_tree:
                return True, True, lca_left_tree
            elif not lca_left_tree and lca_right_tree:
                return True, True, lca_right_tree

        else:
            # if either of A or B does not exist in this tree. it means no LCA, so we return None for LCA.
            return a_exist_in_tree, b_exist_in_tree, None

#
# sol=Solution()
# root, nodes = build_tree_from_list([4,3,7,None,None,5,6])
#
# sol.lowestCommonAncestor(root, A=nodes[2], B=nodes[6])