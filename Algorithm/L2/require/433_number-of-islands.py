# 433. Number of Islands
# 中文English
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent,
# we consider them in the same island. We only consider up/down/left/right adjacent.
#
# Find the number of islands.
#
# Example
# Example 1:
#
# Input:
# [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,1],
#   [0,0,0,0,0],
#   [0,0,0,0,1]
# ]
# Output:
# 3
# Example 2:
#
# Input:
# [
#   [1,1]
# ]
# Output:
# 1


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = set()
        num_island = 0
        for i in range(m):
            for j in range(n):
                if self.is_valid(grid, i, j, visited):
                    num_island += 1
                    self.bfs_helper(grid, i, j, visited)

        return num_island

    # check if this tile is valid, and also we never visit it before
    def is_valid(self, grid, i, j, visited):
        m = len(grid)
        n = len(grid[0])

        if 0 <= i < m and 0 <= j < n and not visited[i][j] and grid[i][j] == 1:
            return True
        else:
            return False

    # this function visit that tile (i,j) and its neighbors if  tile(i,j) is valid and never visited
    def bfs_helper(self, grid, x, y, visited):

        if self.is_valid(grid, x, y, visited):
            visited.add((x, y))
            for dx, dy in DIRECTIONS:
                self.bfs_helper(grid, x + dx, y + dy, visited)
        else:
            return


from collections import deque

DELTA = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution2:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        n_rows = len(grid)
        if n_rows == 0:
            return 0

        n_cols = len(grid[0])

        visited = set()
        islands = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    if (i, j) not in visited:
                        visited.add((i, j))
                        islands += 1
                        self._bfs_helper(grid, i, j, visited)

        return islands

    def _bfs_helper(self, grid, i, j, visited):
        q = deque([(i, j)])
        while q:
            for _ in range(len(q)):
                curr_x, curr_y = q.popleft()

                for d_x, d_y in DELTA:
                    next_x, next_y = curr_x + d_x, curr_y + d_y
                    if self.is_valid(grid, next_x, next_y) and grid[next_x][next_y] == 1 and (
                    next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y))

    def is_valid(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])


grid = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1]
]
sol = Solution2()
sol.numIslands(grid)
