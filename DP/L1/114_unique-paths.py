# 114. Unique Paths
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?
# Example
# Example 1:
#
# Input: n = 1, m = 3
# Output: 1
# Explanation: Only one path to target position.
# Example 2:
#
# Input:  n = 3, m = 3
# Output: 6
# Explanation:
# 	D : Down
# 	R : Right
# 	1) DDRR
# 	2) DRDR
# 	3) DRRD
# 	4) RRDD
# 	5) RDRD
# 	6) RDDR
# Notice
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
        dp = [[0] * n for _ in range(m)]

        if m == 0 or n == 0:
            return 0
        # because for each cell, we need the cell on its left and cell above it. the sequence we calculate need to be
        # outer loop is each row, then within that row, each column from left to right.
        for i in range(m):
            for j in range(n):
                # there is only one way to get to all the cells in top row and left most column
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                # current = cell on the left + cell above
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]
