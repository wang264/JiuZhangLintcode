# 794. Sliding Puzzle II
# 中文English
# On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.
#
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
#
# Given an initial state of the puzzle board and final state, return the least number of moves required so
# that the initial state to final state.
#
# If it is impossible to move from initial state to final state, return -1.
#
# Example
# Example 1:
#
# Input:
# [
#  [2,8,3],
#  [1,0,4],
#  [7,6,5]
# ]
# [
#  [1,2,3],
#  [8,0,4],
#  [7,6,5]
# ]
# Output:
# 4
#
# Explanation:
# [                 [
#  [2,8,3],          [2,0,3],
#  [1,0,4],   -->    [1,8,4],
#  [7,6,5]           [7,6,5]
# ]                 ]
#
# [                 [
#  [2,0,3],          [0,2,3],
#  [1,8,4],   -->    [1,8,4],
#  [7,6,5]           [7,6,5]
# ]                 ]
#
# [                 [
#  [0,2,3],          [1,2,3],
#  [1,8,4],   -->    [0,8,4],
#  [7,6,5]           [7,6,5]
# ]                 ]
#
# [                 [
#  [1,2,3],          [1,2,3],
#  [0,8,4],   -->    [8,0,4],
#  [7,6,5]           [7,6,5]
# ]                 ]
# Example 2：
#
# Input:
# [[2,3,8],[7,0,5],[1,6,4]]
# [[1,2,3],[8,0,4],[7,6,5]]
# Output:
# -1
# Challenge
# How to optimize the memory?
# Can you solve it with A* algorithm?

DELTAS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

from collections import deque
from copy import deepcopy


class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        # # write your code here

        visited = set()
        visited.add(self.state_to_tuple(init_state))
        queue = deque([init_state])

        num_move = -1
        while queue:
            num_move = num_move + 1
            for _ in range(len(queue)):
                curr_state = queue.popleft()
                if curr_state == final_state:
                    return num_move
                x, y = self.find_zero_loc(curr_state)

                # all possible locations for zeros.
                for dx, dy in DELTAS:
                    new_x, new_y = x + dx, y + dy
                    if self.is_valid(new_x, new_y):
                        # try to make a move
                        new_state = self.make_move(state=curr_state, old_zero=(x, y), new_zero=(new_x, new_y))
                        # check if whether we seen the new move before
                        if self.state_to_tuple(new_state) not in visited:
                            visited.add(self.state_to_tuple(new_state))
                            queue.append(new_state)

        return -1

    # swap the zero from old location to new location
    def make_move(self, state, old_zero, new_zero):
        new_state = deepcopy(state)
        old_x, old_y = old_zero
        new_x, new_y = new_zero
        new_state[old_x][old_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[old_x][old_y]
        return new_state

    def is_valid(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3

    # convert state to tuple of tuple becasue otherwise list is un hashable
    def state_to_tuple(self, state):
        return tuple(tuple(row) for row in state)

    # find the location for zero.
    def find_zero_loc(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j


init_state = [
    [2, 8, 3],
    [1, 0, 4],
    [7, 6, 5]
]
final_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

sol = Solution()
sol.minMoveStep(init_state=init_state, final_state=final_state)
