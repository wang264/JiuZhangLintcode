# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O''s into 'X''s in that surrounded region.
#

# 477. 被围绕的区域
# 中文English
# 给一个二维的矩阵，包含 'X' 和 'O', 找到所有被 'X' 围绕的区域，并用 'X' 替换其中所有的 'O'。

# Example
# Example 1:
#
# Input:
#   X X X X
#   X O O X
#   X X O X
#   X O X X
# Output:
#   X X X X
#   X X X X
#   X X X X
#   X O X X
# Example 2:
#
# Input:
#   X X X X
#   X O O X
#   X O O X
#   X O X X
# Output:
#   X X X X
#   X O O X
#   X O O X
#   X O X X

DIRECTIONS = [(0, -1), (-1, 0), (1, 0), (0, 1)]


# Method 1, Union Find
# class Solution:
#     """
#     @param: board: board a 2D board containing 'X' and 'O'
#     @return: nothing
#     """
#
#     def __init__(self):
#         self.father = {}
#
#     def find(self, x):
#         # if x is root, directly return
#         if self.father[x] == x:
#             return x
#         # try to find the root of x
#         root = x
#         while self.father[root] != root:
#             root = self.father[root]
#         # path compression
#         while self.father[x] != x:
#             temp = self.father[x]
#             self.father[x] = root
#             x = temp
#
#         return root
#
#     def union(self, a, b):
#         root_a, root_b = self.find(a), self.find(b)
#         if root_a != root_b:
#             self.father[root_b] = root_a
#
#     def is_valid(self, board, x, y):
#         if 0 <= x < len(board) and 0 <= y < len(board[0]):
#             return True
#         else:
#             return False
#
#     def on_edge(self, board, x, y):
#         if x == 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) - 1:
#             return True
#         else:
#             return False
#
#     def surroundedRegions(self, board):
#         # reset
#         self.father = {}
#
#         # write your code here
#         if board is None or len(board) == 0:
#             return []
#         num_rows = len(board)
#         num_cols = len(board[0])
#         for x in range(num_rows):
#             for y in range(num_cols):
#                 if board[x][y] == 'X':
#                     continue
#                 self.father[(x, y)] = (x, y)  # initialization
#
#         for x in range(num_rows):
#             for y in range(num_cols):
#                 if board[x][y] == 'X':
#                     continue
#                 # if board[i][j] == 'O'
#                 for dx, dy in DIRECTIONS:
#                     new_x, new_y = x + dx, y + dy
#                     if self.is_valid(board, new_x, new_y)and board[new_x][new_y] == 'O' :
#                         self.union((x, y), (new_x, new_y))
#
#         root_node_to_its_sons = dict()
#         for x in range(num_rows):
#             for y in range(num_cols):
#                 if board[x][y] == 'X':
#                     continue
#                 root_label = self.find((x, y))
#                 if root_label not in root_node_to_its_sons:
#                     root_node_to_its_sons[root_label] = []
#                 root_node_to_its_sons[root_label].append((x, y))
#
#         # iterate each group, if non of the element in that group is on edge, we turn all of them into X.
#         need_to_flip = set()
#         for root_label, cordinates in root_node_to_its_sons.items():
#             at_least_one_on_edge = False
#             for cordinate in cordinates:
#                 x, y = cordinate
#                 if self.on_edge(board, x, y):
#                     at_least_one_on_edge = True
#                     break
#             if not at_least_one_on_edge:
#                 need_to_flip.add(root_label)
#
#         board = [list(x) for x in board]
#         for root_label in need_to_flip:
#             for cordinate in root_node_to_its_sons[root_label]:
#                 x, y = cordinate
#                 board[x][y] = 'X'
#
#         board = [''.join(x) for x in board]
#         return board
# Method 2, DFS

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def is_valid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    def on_edge(self, board, x, y):
        return x == 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) - 1

    def surroundedRegions(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return
        num_rows, num_cols = len(board), len(board[0])

        board = [list(x) for x in board]

        for i in range(num_rows):
            for j in range(num_cols):
                if self.on_edge(board, i, j):
                    self.dfs(board, i, j)  # only start the dfs from boarder.

        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == 'O':  # never visit this node from dfs -> not connect to any node to the boarder
                    board[i][j] = 'X'  # flip to X
                elif board[i][j] == '*':  # we already visited this node --> it is connect to node to the boarder
                    board[i][j] = 'O'  # flip back to O
        board = [''.join(x) for x in board]
        return board

    def dfs(self, board, x, y):
        if not self.is_valid(board, x, y):
            return
        if board[x][y] != 'O':  # if either we visited the node that is originally an 'O' but change to '*" or it is an 'X'
            return
        board[x][y] = '*'
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            self.dfs(board, new_x, new_y)


sol = Solution()
assert sol.surroundedRegions(board=["XXXX", "XOOX", "XXOX", "XOXX"]) == ['XXXX', 'XXXX', 'XXXX', 'XOXX']
assert sol.surroundedRegions(board=["XXXX", "XOOX", "XOOX", "XOXX"]) == ["XXXX", "XOOX", "XOOX", "XOXX"]
