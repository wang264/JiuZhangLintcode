"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        sef.val = val
        self.left, self.right = None, None
"""


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
