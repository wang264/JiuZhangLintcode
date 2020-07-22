# 475. Binary Tree Maximum Path Sum II
# 中文English
# Given a binary tree, find the maximum path sum from root.
#
# The path may end at any node in the tree and contain at least one node in it.
# 475. 二叉树的最大路径和 II
# 中文English
# 给一棵二叉树，找出从根节点出发的路径中，和最大的一条。
#
# 这条路径可以在任何二叉树中的节点结束，但是必须包含至少一个点（也就是根了）。

#
# Example
# Example 1:
#
# Input: {1,2,3}
# Output: 4
# Explanation:
#     1
#    / \
#   2   3
# 1+3=4
# Example 2:
#
# Input: {1,-1,-1}
# Output: 1
# Explanation:
#     1
#    / \
#   -1 -1

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        left = None if self.left is None else self.left.val
        right = None if self.right is None else self.right.val
        return '(D:{}, L:{}, R:{})'.format(self.val, left, right)


def build_tree_breadth_first(sequence):
    # Create a list of trees
    forest = [TreeNode(x) if x is not None else None for x in sequence]

    # Fix up the left- and right links
    count = len(forest)
    for index, tree in enumerate(forest):
        left_index = 2 * index + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * index + 2
        if right_index < count:
            tree.right = forest[right_index]

    for index, tree in enumerate(forest):
        print('[{}]: {}'.format(index, tree))
    return forest[0]  # root


import sys


class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """

    def maxPathSum2(self, root):
        # write your code here
        global_max = root.val
        stack = []
        stack.append((root, root.val))
        while len(stack) != 0:
            curr_node, curr_sum = stack.pop()
            if curr_node.left:
                global_max = max(curr_sum + curr_node.left.val, global_max)
                stack.append((curr_node.left, curr_sum + curr_node.left.val))

            if curr_node.right:
                global_max = max(curr_sum + curr_node.right.val, global_max)
                stack.append((curr_node.right, curr_sum + curr_node.right.val))

        return global_max

    def maxPathSum2_recursive(self, root):
        if root is None:
            return sys.maxsize * -1

        left_subtree_max_path_sum = self.maxPathSum2_recursive(root.left)
        right_subtree_max_path_sum = self.maxPathSum2_recursive(root.right)
        return root.val+max([0, left_subtree_max_path_sum, right_subtree_max_path_sum])


sol = Solution()
root = build_tree_breadth_first([1, -1, -1])
sol.maxPathSum2(root)

root_2 = build_tree_breadth_first([1, 2, 3])
sol.maxPathSum2(root_2)
