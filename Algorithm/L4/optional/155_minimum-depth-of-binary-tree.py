# 155. Minimum Depth of Binary Tree
# 中文English
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Example
# Example 1:
#
# Input: {}
# Output: 0
# Example 2:
#
# Input:  {1,#,2,3}
# Output: 3
# Explanation:
# 	1
# 	 \
# 	  2
# 	 /
# 	3
# it will be serialized {1,#,2,3}
# Example 3:
#
# Input:  {1,2,3,#,#,4,5}
# Output: 2
# Explanation:
#       1
#      / \
#     2   3
#        / \
#       4   5
# it will be serialized {1,2,3,#,#,4,5}


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # if have both left and right child
        if root.left and root.right:
            return min(left_depth, right_depth) + 1
        # if only have left child
        elif root.left and not root.right:
            return left_depth + 1
        # if only have right child
        elif root.right and not root.left:
            return right_depth + 1
        # if this is a leaf node
        else:
            return 1