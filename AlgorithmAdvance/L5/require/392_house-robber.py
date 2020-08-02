# 392. House Robber
# 中文English
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of
# money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police if two adjacent houses were
# broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum
# amount of money you can rob tonight without alerting the police.
#
# Example
# Example 1:
#
# Input: [3, 8, 4]
# Output: 8
# Explanation: Just rob the second house.
# Example 2:
#
# Input: [5, 2, 1, 3]
# Output: 8
# Explanation: Rob the first and the last house.
# Challenge
# O(n) time and O(1) memory.
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)
        # dp[i] = 打劫前i家房子的最大收入
        dp = [0] * (len(A) + 1)
        dp[0] = 0  # 没房子就不能打劫，不打劫就没收入。
        dp[1] = A[0]
        for i in range(2, len(A)+1):
            # dp[i-1] --> 如果不打劫第i个房子。那么打劫前i家房子的收入就是打劫前i-1家房子的收入。
            # dp[i-2] + A[i-1] ---->如果打劫第i个房子。那么打劫前i家房子的收入就是打劫前i-2家房子的收入
            # 加上打劫第i家房子的收入
            dp[i] = max(dp[i-1], dp[i-2] + A[i-1])

        return dp[len(A)]

sol = Solution()
assert sol.houseRobber(A=[5,2,1,3]) == 8
assert sol.houseRobber(A=[3,8,4]) == 8