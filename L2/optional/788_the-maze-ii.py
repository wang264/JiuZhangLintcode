DELTAS = [(0 ,1), (1 ,0) ,(0 ,-1), (-1 ,0)]

from collections import deque
import sys
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        visited = [[False ] *len(maze[0]) for _ in range(len(maze))]
        shortest = [[sys.maxsize] *len(maze[0]) for _ in range(len(maze))]
        start_x, start_y = start
        q = deque([(start_x, start_y, 0)])

        while q:
            x, y, distance = q.popleft()
            visited[x][y] = True
            
            if distance >= shortest[x][y]:
                continue
            else:
                shortest[x][y] = distance
            #if x == destination[0] and y == destination[1]:
            #    return shortest[x][y]

            for dx, dy in DELTAS:
                new_distance = distance
                # for that direction, if we could move in that direction we
                # continue to move until we hit a wall or out of bound
                new_x, new_y = x, y
                while self.is_valid(maze, new_x +dx, new_y +dy):
                    new_x+=dx
                    new_y+=dy
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

        if 0<= x < num_row and 0 <= y < num_col and maze[x][y] == 0:
            return True
        else:
            return False