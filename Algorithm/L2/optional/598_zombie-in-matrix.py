DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        # write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1

        zombies = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    zombies.append((i, j))

        days = 0
        while zombies:
            days += 1
            new_zombies = []
            for zombie_x, zombie_y in zombies:
                for dx, dy in DELTAS:
                    new_zombie = (zombie_x + dx, zombie_y + dy)
                    if self.is_valid_infect(new_zombie[0], new_zombie[1], grid):
                        new_zombies.append(new_zombie)
                        grid[new_zombie[0]][new_zombie[1]] = 1
            zombies = new_zombies

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1

        return days -1 

    def is_valid_infect(self, i, j, grid):
        # the zombie can move up, down, left, right, but not hit another zobie or wall.
        num_row = len(grid)
        num_col = len(grid[0])

        if 0 <= i < num_row and 0 <= j < num_col and grid[i][j] == 0:
            return True
        else:
            return False

# import numpy as np
# grid = np.array([[0,1,2,0,0],[1,0,0,2,1],[0,1,0,0,0]])
# sol = Solution()
# sol.zombie(grid=grid)