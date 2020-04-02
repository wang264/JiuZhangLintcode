# 110.
# Minimum Path Sum
# 中文English
# Given a mxn grid filled with non - negative numbers, find a path from top left to
# bottom right which minimizes the sum of all numbers along its path.
#
# 样例
# Example
# 1:
# Input: [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# Output: 7
#
# Explanation:
# Path is: 1 -> 3 -> 1 -> 1 -> 1
#
# Example
# 2:
# Input: [[1, 3, 2]]
# Output: 6
#
# Explanation:
# Path is: 1 -> 3 -> 2
#
# 注意事项
# You can only go right or down in the path..


class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]
        # initialized the first row/ first column
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                # min sum would be the value on the cell + min value from left/up
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]