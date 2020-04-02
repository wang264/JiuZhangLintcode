# 114. Unique Paths
# 中文English
# A robot is located at the top-left corner of a m x n grid.
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
#
# How many possible unique paths are there?
#
# 样例
# 注意事项
# m and n will be at most 100.
# The answer is guaranteed to be in the range of 32-bit integers


class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        if m == 0 or n == 0:
            return 0

        # m row and n column
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # along the boundary, number of ways will be one
        for j in range(n):
            dp[0][j] = 1

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                # dp this point = from left + from up
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


sol = Solution()
sol.uniquePaths(m=3, n=3)