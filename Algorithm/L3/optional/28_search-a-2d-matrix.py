# 28.
# 搜索二维矩阵
# 中文English
# 写出一个高效的算法来搜索
# m × n矩阵中的值。
#
# 这个矩阵具有以下特性：
#
# 每行中的整数从左到右是排序的。
# 每行的第一个数大于上一行的最后一个整数。
# 样例
# 样例
# 1:
# 输入: [[5]], 2
# 输出: false
#
# 样例解释:
# 没有包含，返回false。
#
# 样例
# 2:
# 输入:
# [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ], 3
# 输出: true
#
# 样例解释:
# 包含则返回true。
#
# 挑战
# O(log(n) + log(m))
# 时间复杂度

class Solution2:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return False
        row_idx = self.find_correct_row_index(matrix, target)

        return self.element_exist_in_row(matrix, row_idx, target)

    def find_correct_row_index(self, matrix, target):
        # binary search one, find the correct row
        last_col = len(matrix[0]) - 1
        start = 0
        end = len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][last_col] < target:
                start = mid
            elif matrix[mid][last_col] > target:
                end = mid
            else:
                return mid  # hmm, we find that number lol
        if matrix[start][0] <= target <= matrix[start][last_col]:
            return start
        elif matrix[end][0] <= target <= matrix[end][last_col]:
            return end
        else:
            return -1
        # binary search two, find the element in the correct row.

    def element_exist_in_row(self, matrix, row, target):
        if row == -1:
            return False
        start = 0
        end = len(matrix[0]) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid
            elif matrix[row][mid] > target:
                end = mid
            else:
                return True

        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        else:
            return False


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        n = num_rows * num_cols
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2
            i, j = self.array_idx_to_matrix_coordinate(mid, num_cols)
            if matrix[i][j] < target:
                left = mid
            elif matrix[i][j] > target:
                right = mid
            else:
                return True

        left_i, left_j = self.array_idx_to_matrix_coordinate(left, num_cols)
        right_i, right_j = self.array_idx_to_matrix_coordinate(right, num_cols)

        if matrix[left_i][left_j] == target or matrix[right_i][right_j] == target:
            return True
        else:
            return False

    def array_idx_to_matrix_coordinate(self, array_idx, matrix_num_cols):
        matrix_row_idx = array_idx // matrix_num_cols
        matrix_col_idx = array_idx % matrix_num_cols

        return matrix_row_idx, matrix_col_idx


sol = Solution()
matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
sol.searchMatrix(matrix=matrix, target=3)
