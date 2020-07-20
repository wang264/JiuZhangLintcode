# 123. Word Search
# 中文English
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# 123. 单词搜索
# 中文English
# 给出一个二维的字母板和一个单词，寻找字母板网格中是否存在这个单词。
#
# 单词可以由按顺序的相邻单元的字母组成，其中相邻单元指的是水平或者垂直方向相邻。每个单元中的字母最多只能使用一次。
# Example
# Example 1:
#
# Input：["ABCE","SFCS","ADEE"]，"ABCCED"
# Output：true
# Explanation：
# [
#      A B C E
#      S F C S
#      A D E E
# ]
# (0,0)A->(0,1)B->(0,2)C->(1,2)C->(2,2)E->(2,1)D
# Example 2:
#
# Input：["z"]，"z"
# Output：true
# Explanation：
# [ z ]
# (0,0)z

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        # write your code here
        if board is None or len(board) == 0:
            return False

        board = [list(row) for row in board]

        num_rows = len(board)
        num_cols = len(board[0])

        visited = set()
        # pick starting point
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    temp = self.dfs_helper(board, word, word_idx=0, x=i, y=j, visited=visited)
                    visited.remove((i, j))
                    if temp:
                        return True

        return False

    def is_valid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    def dfs_helper(self, board, word, word_idx, x, y, visited):
        if word_idx == len(word) - 1:
            return True

        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if not self.is_valid(board, new_x, new_y): # out of board
                continue
            if board[new_x][new_y] != word[word_idx+1]: # character does not match
                continue
            if (new_x, new_y) in visited: # already visited. 
                continue
            visited.add((new_x, new_y))
            rslt = self.dfs_helper(board, word, word_idx + 1, new_x, new_y, visited)
            visited.remove((new_x, new_y))
            if rslt:
                return True

        return False


sol = Solution()
assert sol.exist(board=["ABCE", "SFCS", "ADEE"], word="ABCCED") == True
assert sol.exist(board=["ABCE", "SFCS", "ADEE"], word="ABCB") == False
assert sol.exist(board=["a"], word="b") == False
assert sol.exist(board=["z"], word="z") == True
