# 33. N皇后问题
# 中文English
# n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击(任意两个皇后不能位于同一行，同一列，同一斜线)。
# 给定一个整数n，返回所有不同的n皇后问题的解决方案。
# 每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。
#
# 例1:
#
# 输入:1
# 输出:
#    [["Q"]]
#
# 例2:
#
# 输入:4
# 输出:
# [
#   // Solution 1
#   [".Q..",
#    "...Q",
#    "Q...",
#    "..Q."
#   ],
#   // Solution 2
#   ["..Q.",
#    "Q...",
#    "...Q",
#    ".Q.."
#   ]
# ]
# 挑战
# 你能否不使用递归完成？

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        # curr_col_permutation: 用來記錄每一個Queen的Column, Row默認從0，1，2，3....
        # visited 用來記錄幫助判斷擺放是否合理。列數和行數之和 列數和行數之差，用來判斷是否會
        # 斜綫攻擊。
        rslt = []
        visited = {'col_num': set(), 'row_col_sum': set(), 'row_col_diff': set()}
        self.dfs_helper(n, [], visited, rslt)
        return rslt

    def dfs_helper(self, n, curr_col_permutation, visited, boards):
        if len(curr_col_permutation) == n:
            boards.append(self.draw(curr_col_permutation))
            return
        row = len(curr_col_permutation)
        # try possible column indexes
        for col in range(n):
            if not self.is_valid(col, row, visited):
                continue
            curr_col_permutation.append(col)
            visited['col_num'].add(col)
            visited['row_col_sum'].add(row + col)
            visited['row_col_diff'].add(row - col)
            self.dfs_helper(n, curr_col_permutation, visited, boards)
            visited['col_num'].remove(col)
            visited['row_col_sum'].remove(row + col)
            visited['row_col_diff'].remove(row - col)
            curr_col_permutation.pop()

    def is_valid(self, col, row, visited):
        if col in visited['col_num']:
            return False
        if row + col in visited['row_col_sum']:  # 斜綫，y=x+k
            return False
        if row - col in visited['row_col_diff']:  # 斜綫 y=-x+k
            return False
        return True

    def draw(self, permutation):
        board = []
        n = len(permutation)
        for col in permutation:
            row_string = ''.join(['Q' if c == col else '.' for c in range(n)])
            board.append(row_string)
        return board


sol = Solution()
assert sol.solveNQueens(n=1) == [['Q']]

assert sol.solveNQueens(n=2) == []
