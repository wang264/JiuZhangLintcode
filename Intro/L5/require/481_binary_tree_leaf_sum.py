# 481. Binary Tree Leaf Sum
# 中文English
# Given a binary tree, calculate the sum of leaves.
#
# Example
# Example 1:
#
# Input：{1,2,3,4}
# Output：7
# Explanation：
#     1
#    / \
#   2   3
#  /
# 4
# 3+4=7
# Example 2:
#
# Input：{1,#,3}
# Output：3
# Explanation：
#     1
#       \
#        3


from helperfunc import TreeNode
class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root:TreeNode):
        # write your code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val

        left_sum = self.leafSum(root.left)
        right_sum = self.leafSum(root.right)
        return left_sum+right_sum


