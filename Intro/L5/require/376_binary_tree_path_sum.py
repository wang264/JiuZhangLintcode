# 376. Binary Tree Path Sum
# 中文English
# Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
#
# A valid path is from root node to any of the leaf nodes.
#
# Example
# Example 1:
#
# Input:
# {1,2,4,2,3}
# 5
# Output: [[1, 2, 2],[1, 4]]
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
# Example 2:
#
# Input:
# {1,2,4,2,3}
# 3
# Output: []
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# Notice we need to find all paths from root node to leaf nodes.
# 1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5
# There is no one satisfying it.

from helperfunc import TreeNode, build_tree_breadth_first


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        rslt = self.binary_tree_path_sum_helper(root, target)

        return [list(reversed(x)) for x in rslt]

    def binary_tree_path_sum_helper(self, root, target):
        # write your code here
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == target:
                return [[target]]
            else:
                return []

        left_rslt = self.binary_tree_path_sum_helper(root.left, target - root.val)
        right_rslt = self.binary_tree_path_sum_helper(root.right, target - root.val)

        rslt = left_rslt + right_rslt
        for i in range(len(rslt)):
            rslt[i].append(root.val)

        return rslt


root = build_tree_breadth_first(sequence=[1, 2, 4, 2, 3])
sol = Solution()
rslt = sol.binaryTreePathSum(root=root, target=5)
print(rslt)

root = build_tree_breadth_first(sequence=[1, 2, -5, 4, None, 5, 6])
sol = Solution()
rslt = sol.binaryTreePathSum(root=root, target=2)
