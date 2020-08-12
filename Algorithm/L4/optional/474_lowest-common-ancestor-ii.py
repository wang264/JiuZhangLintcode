# 474. Lowest Common Ancestor II
# 中文English
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
#
# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
#
# The node has an extra attribute parent which point to the father of itself. The root's parent is null.
#
# Example
# Example 1:
#
# Input：{4,3,7,#,#,5,6},3,5
# Output：4
# Explanation：
#      4
#      / \
#     3   7
#        / \
#       5   6
# LCA(3, 5) = 4
# Example 2:
#
# Input：{4,3,7,#,#,5,6},5,6
# Output：7
# Explanation：
#       4
#      / \
#     3   7
#        / \
#       5   6
# LCA(5, 6) = 7

class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        path_A = self.get_path_to_root(A)
        path_B = self.get_path_to_root(B)

        ind_A = len(path_A) - 1
        ind_B = len(path_B) - 1

        while ind_A >= 0 and ind_B >= 0:
            if path_A[ind_A] != path_B[ind_B]:
                break
            else:
                LCA = path_A[ind_A]
                ind_A -= 1
                ind_B -= 1

        return LCA

    def get_path_to_root(self, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path