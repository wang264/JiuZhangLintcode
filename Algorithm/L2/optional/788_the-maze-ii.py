# 788.The Maze II
# 中文English
# There is a ball in a maze with empty spaces and walls.The ball can go through empty spaces by rolling up, down,
# left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#
# Given the ball 's start position, the destination and the maze, find the shortest distance for the ball to stop at ' \
# the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position
# (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
#
# The maze is represented by a binary 2 D array. 1 means the wall and 0 means the empty space.You may assume that the
# borders of the maze are all walls.The start and destination coordinates are represented by row and column indexes.
#
# Example
# Example
# 1:
# Input:
# (rowStart, colStart) = (0, 4)
# (rowDest, colDest) = (4, 4)
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Output: 12
#
# Explanation:
# (0, 4)->(0, 3)->(1, 3)->(1, 2)->(1, 1)->(1, 0)->(2, 0)->(2, 1)->(2, 2)->(3, 2)->(4, 2)->(4, 3)->(4, 4)
#
# Example
# 2:
# Input:
# (rowStart, colStart) = (0, 4)
# (rowDest, colDest) = (0, 0)
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Output: 6
#
# Explanation:
# (0, 4)->(0, 3)->(1, 3)->(1, 2)->(1, 1)->(1, 0)->(0, 0)
#
# Notice
# 1. There is only one ball and one destination in the maze.
# 2. Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# 3. The given maze does not contain border(like the red rectangle in the example pictures), but you could
# assume the borderof the maze are all walls.
# 4. The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.


DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

import sys
from collections import deque


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def shortestDistance(self, maze, start, destination):
        # write your code here
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        shortest = [[sys.maxsize] * len(maze[0]) for _ in range(len(maze))]
        start_x, start_y = start
        q = deque([(start_x, start_y, 0)])

        while q:
            x, y, distance = q.popleft()
            visited[x][y] = True

            if distance >= shortest[x][y]:
                continue
            else:
                shortest[x][y] = distance
            # if x == destination[0] and y == destination[1]:
            #    return shortest[x][y]

            for dx, dy in DELTAS:
                new_distance = distance
                # for that direction, if we could move in that direction we
                # continue to move until we hit a wall or out of bound
                new_x, new_y = x, y
                while self.is_valid(maze, new_x + dx, new_y + dy):
                    new_x += dx
                    new_y += dy
                    new_distance += 1

                if not visited[new_x][new_y]:
                    q.append((new_x, new_y, new_distance))

        dest_x, dest_y = destination

        if shortest[dest_x][dest_y] == sys.maxsize:
            return -1
        else:
            return shortest[dest_x][dest_y]

    def is_valid(self, maze, x, y):
        num_row = len(maze)
        num_col = len(maze[0])

        if 0 <= x < num_row and 0 <= y < num_col and maze[x][y] == 0:
            return True
        else:
            return False


sol = Solution()
map = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
sol.shortestDistance(maze=map, start=[0, 4], destination=[4, 4])

map = [[0, 0, 0, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
sol.shortestDistance(maze=map, start=[3, 0], destination=[1, 2])
