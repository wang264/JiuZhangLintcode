# 573. Build Post Office II
# 中文English
# Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to
# build a post office so that the sum of the distance from the post office to all the houses is smallest.
#
# Return the smallest sum of distance. Return -1 if it is not possible.
#
# Example
# Example 1:
#
# Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
# Output：8
# Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
# Example 2:
#
# Input：[[0,1,0],[1,0,1],[0,1,0]]
# Output：4
# Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
# Notice
# You cannot pass through wall and house, but can pass through empty.
# You only build post office on an empty.

# 573. 邮局的建立 II
# 中文English
# 给出一个二维的网格，每一格可以代表墙 2 ，房子 1，以及空 0 (用数字0,1,2来表示)，在网格中找到一个位置去建立邮局，使得所有的房子到邮局的距离和是最小的。
# 返回所有房子到邮局的最小距离和，如果没有地方建立邮局，则返回-1.
#
# Example
# 样例 1:
#
# 输入：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
# 输出：8
# 解释： 在(1,1)处建立邮局，所有房子到邮局的距离和是最小的。
# 样例 2:
#
# 输入：[[0,1,0],[1,0,1],[0,1,0]]
# 输出：4
# 解释：在(1,1)处建立邮局，所有房子到邮局的距离和是最小的。
# Notice
# 你不能穿过房子和墙，只能穿过空地。
# 你只能在空地建立邮局。

EMPTY = 0
HOUSE = 1
WALL = 2
INFINITY = float('inf')
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

import sys
from collections import deque


class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        # write your code here
        if not grid:
            return -1

        num_rows = len(grid)
        num_cols = len(grid[0])
        sum_dist = [[0] * (num_cols) for _ in range(num_rows)]  # total distance to house for EMPTY land (i,j)
        count = [[0] * (num_cols) for _ in range(num_rows)]  # total number of  house accessible for EMPTY land (i,j)

        total_houses_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == HOUSE:
                    self.bfs(grid, i, j, sum_dist, count)
                    total_houses_count += 1

        min_dist = sys.maxsize
        for i in range(num_rows):
            for j in range(num_cols):
                if count[i][j] == total_houses_count and sum_dist[i][j] < min_dist:
                    min_dist = sum_dist[i][j]

        return min_dist if min_dist != sys.maxsize else -1

    def bfs(self, grid, x, y, dist, count):
        queue = deque([(x, y)])
        visited = set()
        visited.add((x, y))

        level = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                x, y = queue.popleft()
                if dist[x][y] == sys.maxsize:
                    dist[x][y] = 0

                dist[x][y] += level
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if (new_x, new_y) in visited:
                        continue

                    if not self.is_valid_path(grid, new_x, new_y):
                        continue

                    count[new_x][new_y] += 1
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
            level += 1

    def is_valid_path(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == EMPTY


sol = Solution()
sol.shortestDistance(grid=[[0, 1, 0, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 0, 0]])