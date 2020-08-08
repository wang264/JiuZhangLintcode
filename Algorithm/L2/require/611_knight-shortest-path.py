# 611. Knight Shortest Path
# 中文English
# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position,
# find the shortest path to a destination position, return the length of the route.
# Return -1 if destination cannot be reached.
#
# Example
# Example 1:
#
# Input:
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2]
# Output: 2
# Explanation:
# [2,0]->[0,1]->[2,2]
# Example 2:
#
# Input:
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2]
# Output:-1
# Clarification
# If the knight is at (x, y), he can get to the following positions in one step:
#
# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
# Notice
# source and destination must be empty.
# Knight can not enter the barrier.
# Path length refers to the number of steps the knight takes.

# Definition for a point.


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2),
]

from collections import deque


class Solution2:
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


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid:
            return -1

        x, y = source.x, source.y
        if grid[x][y] == 1:
            return -1
        q = deque([(x, y)])
        visited = set()
        visited.add((x, y))

        steps = -1
        while q:
            steps += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                if x == destination.x and y == destination.y:
                    return steps
                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    if self.is_valid(grid, new_x, new_y, visited):
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))

        return -1

    def is_valid(self, grid, x, y, visited):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (x, y) not in visited


sol = Solution()
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert sol.shortestPath(grid, Point(2, 0), Point(2, 2)) == 2

grid = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
assert sol.shortestPath(grid, Point(2, 0), Point(2, 2)) == -1
