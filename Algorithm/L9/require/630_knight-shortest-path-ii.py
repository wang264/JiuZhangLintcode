# 630. Knight Shortest Path II
# 中文English
# Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.
#
# 样例
# Example 1:
#
# Input:
# [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# Output:
# 3
# Explanation:
# [0,0]->[2,1]->[0,2]->[2,3]
# Example 2:
#
# Input:
# [[0,1,0],[0,0,1],[0,0,0]]
# Output:
# -1
# 说明
# If the knight is at (x, y), he can get to the following positions in one step:
#
# (x + 1, y + 2)
# (x - 1, y + 2)
# (x + 2, y + 1)
# (x - 2, y + 1)
import sys


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        # write your code here
        deltas = [(-1, -2), (1, -2), (-2, -1), (2, -1)]
        # number of rows
        m = len(grid)
        # number of columns
        n = len(grid[0])

        # dp[i][j] = the minimum step from [0],[0] to [i],[j]
        dp = [[sys.maxsize] * n for _ in range(m)]

        dp[0][0] = 0
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    continue
                for dx, dy in deltas:
                    # if the knight move to (i, j) --> it could comes from (x, y)
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < m:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)

        if dp[m - 1][n - 1] == sys.maxsize:
            return -1

        return dp[m - 1][n - 1]


sol = Solution()
sol.shortestPath2(grid=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
