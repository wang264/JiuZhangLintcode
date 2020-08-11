# 596. Minimum Subtree
# 中文English
# Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
#
# Example
# Example 1:
#
# Input:
# {1,-5,2,1,2,-4,-5}
# Output:1
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     2
#  / \   /  \
# 1   2 -4  -5
# The sum of whole tree is minimum, so return the root.
# Example 2:
#
# Input:
# {1}
# Output:1
# Explanation:
# The tree is look like this:
#    1
# There is one and only one subtree in the tree. So we return 1.
# Notice
# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

import sys


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        _, node, _ = self.find_subtree_helper(root)

        return node

    def find_subtree_helper(self, node):
        """

        @param node:
        @return: a tuple of three elements,
        ( sum of the whole tree,
        root of the min_sum subtree,
        sum value of the min_sum subtree)
        """
        if node is None:
            return 0, None, sys.maxsize

        left_tree_sum, left_min_node, left_min_sum = self.find_subtree_helper(node=node.left)
        right_tree_sum, right_min_node, right_min_sum = self.find_subtree_helper(node=node.right)

        tree_sum = left_tree_sum + right_tree_sum + node.val

        if left_min_sum == min(left_min_sum, right_min_sum, tree_sum):
            return tree_sum, left_min_node, left_min_sum
        elif right_min_sum == min(left_min_sum, right_min_sum, tree_sum):
            return tree_sum, right_min_node, right_min_sum
        else:
            return tree_sum, node, tree_sum


class Solution2:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        _, _, node = self.divider_conquer_helper(root)
        return node

    def divider_conquer_helper(self, root):
        """
        :param root:
        :return: (tree_sum, sum_of_minsumsubtree, root_node_of_minsumsubtree)
        """
        if root is None:
            return 0, 0, None

        left_subtree_sum, left_minsubtree_sum, left_minsubtree_root = self.divider_conquer_helper(root.left)
        right_subtree_sum, right_minsubtree_sum, right_minsubtree_root = self.divider_conquer_helper(root.right)

        # no child
        if root.left is None and root.right is None:
            return root.val, root.val, root

        # only left child
        if root.left and root.right is None:
            if left_minsubtree_sum < left_subtree_sum + root.val:
                return left_subtree_sum + root.val, left_minsubtree_sum, left_minsubtree_root
            else:
                return left_subtree_sum + root.val, left_subtree_sum + root.val, root

        # only right child
        if root.right and root.left is None:
            if right_minsubtree_sum < right_subtree_sum + root.val:
                return right_subtree_sum + root.val, right_minsubtree_sum, right_minsubtree_root
            else:
                return right_subtree_sum + root.val, right_subtree_sum + root.val, root

        # both left and right subtree
        tree_sum = root.val + left_subtree_sum + right_subtree_sum
        if tree_sum <= left_minsubtree_sum and tree_sum <= right_minsubtree_sum:
            return tree_sum, tree_sum, root

        if left_minsubtree_sum <= tree_sum and left_minsubtree_sum <= right_minsubtree_sum:
            return tree_sum, left_minsubtree_sum, left_minsubtree_root

        if right_minsubtree_sum <= tree_sum and right_minsubtree_sum <= left_minsubtree_sum:
            return tree_sum, right_minsubtree_sum, right_minsubtree_root

        print("oops should not get here")


from helperfunc import build_tree_breadth_first

sol = Solution2()
root = build_tree_breadth_first([1, None, 2])
sol.findSubtree(root=root)

root = build_tree_breadth_first(
    sequence=[1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1])
sol.findSubtree(root=root)
