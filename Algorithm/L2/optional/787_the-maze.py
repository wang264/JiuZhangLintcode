# 787. 迷宫
# 中文English
# 在迷宫中有一个球，里面有空的空间和墙壁。球可以通过滚上，下，左或右移动，
# 但它不会停止滚动直到撞到墙上。当球停止时，它可以选择下一个方向。

# 给定球的起始位置，目的地和迷宫，确定球是否可以停在终点。

# 迷宫由二维数组表示。1表示墙和0表示空的空间。你可以假设迷宫的边界都是墙。开始和目标坐标用行和列索引表示。

# Example
# 例1:

# 输入:
# map =
# [
#  [0,0,1,0,0],
#  [0,0,0,0,0],
#  [0,0,0,1,0],
#  [1,1,0,1,1],
#  [0,0,0,0,0]
# ]
# start = [0,4]
# end = [3,2]
# 输出:
# false
# 例2:

# 输入:
# map =
# [[0,0,1,0,0],
#  [0,0,0,0,0],
#  [0,0,0,1,0],
#  [1,1,0,1,1],
#  [0,0,0,0,0]
# ]
# start = [0,4]
# end = [4,4]
# 输出:
# true
# Notice
# 1.在迷宫中只有一个球和一个目的地。
# 2.球和目的地都存在于一个空的空间中，它们最初不会处于相同的位置。
# 3.给定的迷宫不包含边框(比如图片中的红色矩形)，但是你可以假设迷宫的边界都是墙。
# 5.迷宫中至少有2个空的空间，迷宫的宽度和高度都不会超过100。

DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

from collections import deque


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def hasPath(self, maze, start, destination):
        visited = set()
        if not self.is_valid(maze, start[0], start[1]):
            return False

        queue = deque([start])
        visited.add((start[0], start[1]))

        while queue:
            x, y = queue.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in DELTAS:
                # for that direction, if we could move in that direction we
                # continue to move until we hit a wall or out of bound
                new_x, new_y = x, y
                while self.is_valid(maze, new_x + dx, new_y + dy):
                    new_x += dx
                    new_y += dy
                if (new_x, new_y) not in visited:
                    queue.append([new_x, new_y])
                    visited.add((new_x, new_y))

        return False

    def is_valid(self, maze, x, y):
        num_row = len(maze)
        num_col = len(maze[0])

        if 0 <= x < num_row and 0 <= y < num_col and maze[x][y] == 0:
            return True
        else:
            return False


sol = Solution()
map = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
assert sol.hasPath(maze=map, start=[0, 4], destination=[3, 2]) == False

map = [
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
assert sol.hasPath(maze=map, start=[0, 4], destination=[4, 4]) == True
