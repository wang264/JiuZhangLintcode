# 111. Climbing Stairs
# 中文English
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# example 1:
# Input: n = 3
# Output: 3
#
# Explanation:
# 1) 1, 1, 1
# 2) 1, 2
# 3) 2, 1
# total 3.
#
# Example 2:
# Input:  n = 1
# Output: 1
#
# Explanation:
# only 1 way.

class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n <= 2:
            return n

        # write your code here
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]


sol = Solution()
sol.climbStairs(n=3)