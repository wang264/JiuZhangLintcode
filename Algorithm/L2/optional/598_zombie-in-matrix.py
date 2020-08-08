# 598. Zombie in Matrix
# 中文English
# Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).Zombies can turn
# the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to
# turn all people into zombies? Return -1 if can not turn all people into zombies.
#
# Example
# Example 1:
#
# Input:
# [[0,1,2,0,0],
#  [1,0,0,2,1],
#  [0,1,0,0,0]]
# Output:
# 2
# Example 2:
#
# Input:
# [[0,0,0],
#  [0,0,0],
#  [0,0,1]]
# Output:
# 4

DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
WALL = 2
ZOMBIE = 1
PEOPLE = 0

from collections import deque


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        # write your code here
        visited = set()
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ZOMBIE:
                    queue.append((i, j))
                    visited.add((i, j))
        num_day = -1
        while queue:
            num_day += 1
            for _ in range(len(queue)):
                zombie_x, zombie_y = queue.popleft()
                grid[zombie_x][zombie_y] = ZOMBIE
                for dx, dy in DELTAS:
                    new_x, new_y = zombie_x + dx, zombie_y + dy
                    if self.is_valid(grid, new_x, new_y) and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        new_zombie = (new_x, new_y)
                        queue.append(new_zombie)

        if self.no_one_alive(grid):
            return num_day
        else:
            return -1

    def no_one_alive(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == PEOPLE:
                    return False
        return True

    def is_valid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == PEOPLE


import numpy as np

grid = np.array([[0, 1, 2, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 0, 0]])
sol = Solution()
assert sol.zombie(grid=grid) == 2

grid = np.array([[0,2,0], [2,2,0], [2,0,1]])
assert sol.zombie(grid) == -1