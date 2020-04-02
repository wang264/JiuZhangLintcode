# 553. Bomb Enemy
# 中文English
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),
# return the maximum enemies you can kill using one bomb. The bomb kills all the enemies in the same row and
# column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# CAN ONLY PLACE BOMB IN '0'
#
# Example
# Example1
#
# Input:
# grid =[
#      "0 E 0 0",
#      "E 0 W E",
#      "0 E 0 0"
# ]
# Output: 3
# Explanation:
# Placing a bomb at (1,1) kills 3 enemies
# Example2
#
# Input:
# grid =[
#      "0 E 0 0",
#      "E E W E",
#      "0 E 0 0"
# Output: 2
# Explanation:
# Placing a bomb at (0,0) or (0,3) or (2,0) or (2,3) kills 2 enemies
# Notice
# You can only put the bomb at an empty cell.


class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """

    def maxKilledEnemies(self, grid):
        # write your code here
        # up[i][j] = 在(i.j)格上放一个炸弹，能向上炸死多少人
        # 如果(i,j) == 0, 是空地，那能向上炸死 up[i-1][j]人
        # 如果(i.j) == 'E', 是敌人， 那能向上炸死 up[i-1][j] +1 人
        # 如果（i,j) == 'W', 是墙， 那能向上炸死 0 人
        if len(grid) == 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        up = [[0] * cols for _ in range(rows)]
        down = [[0] * cols for _ in range(rows)]
        left = [[0] * cols for _ in range(rows)]
        right = [[0] * cols for _ in range(rows)]

        # up.
        for i in range(rows):
            for j in range(cols):
                # if first row
                if i == 0:
                    if grid[i][j] == '0':
                        up[i][j] = 0
                    if grid[i][j] == 'W':
                        up[i][j] = 0
                    if grid[i][j] == 'E':
                        up[i][j] = 1
                    continue
                if grid[i][j] == '0':
                    up[i][j] = up[i - 1][j]
                if grid[i][j] == 'W':
                    up[i][j] = 0
                if grid[i][j] == 'E':
                    up[i][j] = up[i - 1][j] + 1

        # down
        for i in reversed(range(rows)):
            for j in range(cols):
                # if last row
                if i == rows - 1:
                    if grid[i][j] == '0':
                        down[i][j] = 0
                    if grid[i][j] == 'W':
                        down[i][j] = 0
                    if grid[i][j] == 'E':
                        down[i][j] = 1
                    continue
                if grid[i][j] == '0':
                    down[i][j] = down[i + 1][j]
                if grid[i][j] == 'W':
                    down[i][j] = 0
                if grid[i][j] == 'E':
                    down[i][j] = down[i + 1][j] + 1

        # left
        for j in range(cols):
            for i in range(rows):
                # if first column
                if j == 0:
                    if grid[i][j] == '0':
                        left[i][j] = 0
                    if grid[i][j] == 'W':
                        left[i][j] = 0
                    if grid[i][j] == 'E':
                        left[i][j] = 1
                    continue
                if grid[i][j] == '0':
                    left[i][j] = left[i][j - 1]
                if grid[i][j] == 'W':
                    left[i][j] = 0
                if grid[i][j] == 'E':
                    left[i][j] = left[i][j - 1] + 1

        # right
        for j in reversed(range(cols)):
            for i in range(rows):
                # if last column
                if j == cols - 1:
                    if grid[i][j] == '0':
                        right[i][j] = 0
                    if grid[i][j] == 'W':
                        right[i][j] = 0
                    if grid[i][j] == 'E':
                        right[i][j] = 1
                    continue
                if grid[i][j] == '0':
                    right[i][j] = right[i][j + 1]
                if grid[i][j] == 'W':
                    right[i][j] = 0
                if grid[i][j] == 'E':
                    right[i][j] = right[i][j + 1] + 1

        rslt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    rslt = max(rslt, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        return rslt


sol = Solution()
grid = ["0E00",
        "E0WE",
        "0E00"]
sol.maxKilledEnemies(grid)
