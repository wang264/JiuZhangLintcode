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


class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # write your code here
        # write your code here
        if m == 0 or n == 0:
            return 0

        # m row and n column
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # init the boundary
        # along the boundary, number of ways will be one, until hit the first obstacle
        first_obstacle_idx_in_first_row = n
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                first_obstacle_idx_in_first_row = j
                break
        for j in range(n):
            if j < first_obstacle_idx_in_first_row:
                dp[0][j] = 1
            else:
                dp[0][j] = 0

        first_obstacle_idx_in_first_col = m
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                first_obstacle_idx_in_first_col = i
                break

        for i in range(m):
            if i < first_obstacle_idx_in_first_col:
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                # dp this point = from left + from up
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]


sol = Solution()
sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
