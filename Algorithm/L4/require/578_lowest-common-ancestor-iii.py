# 578. Lowest Common Ancestor III
# 中文English
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
# Return null if LCA does not exist.
#
# Example
# Example1
#
# Input:
# {4, 3, 7, #, #, 5, 6}
# 3 5
# 5 6
# 6 7
# 5 8
# Output:
# 4
# 7
# 7
# null
# Explanation:
#   4
#  / \
# 3   7
#    / \
#   5   6
#
# LCA(3, 5) = 4
# LCA(5, 6) = 7
# LCA(6, 7) = 7
# LCA(5, 8) = null
#
# Example2
#
# Input:
# {1}
# 1 1
# Output:
# 1
# Explanation:
# The tree is just a node, whose value is 1.
# Notice
# node A or node B may not exist in tree.
# Each node has a different value

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a_in_tree, b_in_tree, lca = self.helper(root, A, B)
        if a_in_tree and b_in_tree:
            return lca
        else:
            return None

    def helper(self, root, node_a, node_b) -> tuple:
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

from helperfunc import build_tree_breadth_first, TreeNode

sol=Solution()
root = build_tree_breadth_first([1,2,3,4,5,6,7])
A=root.left
B=root.right

rslt = sol.lowestCommonAncestor3(root, A, B)


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):

        a_in_tree, b_in_tree, lca_node = self.helper(root, a, b)
        if lca_node:
            return lca_node
        else:
            return None

    def helper(self, root, a, b):

        # divide
        a_in_left_tree, b_in_left_tree, lca_left_tree = self.helper(root.left, a, b)
        a_in_right_tree, b_in_right_tree, lca_right_tree = self.helper(root.right, a, b)

        # conqour
        a_in_this_tree = a_in_left_tree or a_in_right_tree or root == a
        b_in_this_tree = b_in_left_tree or b_in_right_tree or root == b

        if a_in_this_tree and b_in_this_tree:
            if lca_left_tree and not lca_right_tree:
                lca_node = lca_left_tree
            elif not lca_left_tree and lca_right_tree:
                lca_node = lca_right_tree
            else:
                # if lca is not in left tree and right tree but a,b, are in the subtrees, root must be lca
                lca_node = root

            return a_in_this_tree, b_in_this_tree, lca_node
        else:
            # either a or b not in this tree, the lca is None
            return a_in_this_tree, b_in_this_tree, None

