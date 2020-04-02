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

        visited = [[False] * n for _ in range(m)]
        num_island = 0
        for i in range(m):
            for j in range(n):
                if self.is_valid(grid, i, j, visited):
                    num_island += 1
                    self.bfs_helper(grid, i, j, visited)

        return num_island
    #check if this tile is valid, and also we never visit it before
    def is_valid(self, grid, i, j, visited):
        m = len(grid)
        n = len(grid[0])

        if 0<=i<m and 0<=j<n and not visited[i][j] and grid[i][j] == 1:
            return True
        else:
            return False
    # this function visit that tile (i,j) and its neighbors if  tile(i,j) is valid and never visited
    def bfs_helper(self, grid, i, j, visited):
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if self.is_valid(grid, i, j, visited):
            visited[i][j] = True
            for d_i, d_j in deltas:
                self.bfs_helper(grid, i + d_i, j + d_j, visited)
        else:
            return