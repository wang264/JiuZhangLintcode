#Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]

from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        q = deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}  # dictionary to store the smallest  #of step to that point from source

        while q:
            x, y = q.popleft()

            if x == destination.x and y == destination.y:
                return distance[(x, y)]

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                # if we visited that before, continue to the next for loop
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue

                # if the location is valid and we never visit that tile before
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                q.append((next_x, next_y))

        return -1

    def is_valid(self, x, y, grid):
        m = len(grid)
        n = len(grid[0])

        # print('x:{} y:{}'.format(x, y))
        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
            return True
        return False

# sol = Solution()
# grid = [[0,0,0],[0,0,0],[0,0,0]]
# sol.shortestPath(grid, Point(2,0), Point(2,2))