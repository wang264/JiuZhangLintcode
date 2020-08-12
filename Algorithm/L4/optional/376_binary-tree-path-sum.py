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


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        rslt = []
        curr_path = []
        curr_sum = 0
        self.dfs_helper(root, curr_path, curr_sum, rslt, target)
        return rslt

    def dfs_helper(self, node, curr_path, curr_sum, rslt, target):
        if node is None:
            return
        curr_path.append(node.val)
        curr_sum += node.val
        if curr_sum == target and node.left is None and node.right is None:
            rslt.append(curr_path[:])

        self.dfs_helper(node.left, curr_path, curr_sum, rslt, target)
        self.dfs_helper(node.right, curr_path, curr_sum, rslt, target)
        curr_path.pop()


from helperfunc import build_tree_breadth_first

sol = Solution()
root = build_tree_breadth_first([1, 1, 1, 3, 4, 4, 3, None, None, 1, None, 5, 7])
assert sol.binaryTreePathSum(root, target=6) == []

root = build_tree_breadth_first([1, 2, 4, 2, 3])
assert sol.binaryTreePathSum(root, target=5) == [[1, 2, 2], [1, 4]]
