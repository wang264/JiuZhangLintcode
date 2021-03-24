# 470. Tweaked Identical Binary Tree
# 中文English
# Check two given binary trees are identical or not. Assuming any number of tweaks are allowed. A tweak is defined as a swap of the children of one node in the tree.
#
# Example
# Example 1:
#
# Input:{1,2,3,4},{1,3,2,#,#,#,4}
# Output:true
# Explanation:
#         1             1
#        / \           / \
#       2   3   and   3   2
#      /                   \
#     4                     4
#
# are identical.
# Example 2:
#
# Input:{1,2,3,4},{1,3,2,4}
# Output:false
# Explanation:
#
#         1             1
#        / \           / \
#       2   3   and   3   2
#      /             /
#     4             4
#
# are not identical.
# Challenge
# O(n) time
#
# Notice
# There is no two nodes with the same value in the tree.
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are tweaked identical, or false.
    """

    def isTweakedIdentical(self, a, b):
        # Write your code here
        if a is None and b is None:
            return True
        elif a and b and a.val == b.val:
            return self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right) \
                   or \
                   (self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left))
        else:
            return False
