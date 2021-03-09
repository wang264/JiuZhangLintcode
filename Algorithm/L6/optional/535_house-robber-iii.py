# 535. House Robber III
# 中文English
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example
# Example1
#
# Input:  {3,2,3,#,3,#,1}
# Output: 7
# Explanation:
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#   3
#  / \
# 2   3
#  \   \
#   3   1
# Example2
#
# Input:  {3,4,5,1,3,#,1}
# Output: 9
# Explanation:
# Maximum amount of money the thief can rob = 4 + 5 = 9.
#     3
#    / \
#   4   5
#  / \   \
# 1   3   1
# Notice
# This problem is the extention of House Robber and House Robber II


class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        # write your code here
        # rob --> 搶根節點的收入， not_rob--->不搶根節點的收入
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)

    def visit(self, root):
        if root is None:
            return 0, 0
        # left_rob --> 搶root.left節點的收入， left_not_rob--->不搶root.left節點的收入
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)

        # 因為搶了根節點， 就不能搶它的兒子們了。
        rob = root.val + left_not_rob + right_not_rob
        # 沒搶根節點， 其他的隨便搶。挑多錢的搶
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob


from helperfunc import build_tree_breadth_first

root = build_tree_breadth_first([3, 2, 3, None, 3, None, 1])
sol = Solution()
sol.houseRobber3(root=root)
