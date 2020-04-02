#
# 115. Unique Paths II
# 中文English
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# 样例
# 注意事项
# m and n will be at most 100.
#
# Example1:
# Input: [[0]]
# Output: 1
#
# Example2:
# Input: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# Output: 2
#
# Explanation:
# Only 2 different path.
#
# Notice m and n will be at most 100.

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 0 or n == 0:
            return 0

        # m row and n column
        # dp[i][j] = numbers of ways to reach (i,j)
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:  # if have obstacle, set to 0
                    dp[i][j] = 0
                elif i == 0 and j == 0:  # initial point
                    dp[i][j] = 1
                elif i == 0:  # first row
                    dp[i][j] = dp[i][j-1]
                elif j == 0:  # first column
                    dp[i][j] = dp[i-1][j]
                else:
                    # current = from above + from left
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

grid = [[0,0,0],[0,1,0],[0,0,0]]
sol = Solution()
sol.uniquePathsWithObstacles(obstacleGrid=grid)