# 469. Same Tree
# 中文English
# Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.
#
# Example
# Example 1:
#
# Input:{1,2,2,4},{1,2,2,4}
# Output:true
# Explanation:
#         1                   1
#        / \                 / \
#       2   2   and         2   2
#      /                   /
#     4                   4
#
# are identical.
# Example 2:
#
# Input:{1,2,3,4},{1,2,3,#,4}
# Output:false
# Explanation:
#
#         1                  1
#        / \                / \
#       2   3   and        2   3
#      /                        \
#     4                          4
#
# are not identical.

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        # write your code here
        if a is None and b is None:
            return True
        elif a is None and b is not None:
            return False
        elif a is not None and b is None:
            return False

        return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right) and a.val == b.val